"""관리자 화면 API — 생성 인스트럭션 · 크롤링 소스 · 내부 자료 · 권한."""
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from app import store
from app.api.deps import current_email
from app.models import AdminMemberIn, InstructionIn

router = APIRouter(prefix="/api/admin", tags=["admin"])

# 본문을 평문으로 뽑을 수 있는 확장자.
#   pdf          → farming/pdf.py 의 기존 추출기 재사용 (신규 의존성 없음)
#   csv/txt/md   → UTF-8 → cp949 순으로 디코딩 (사내 엑셀 산 CSV 가 cp949 다)
# 그 외(xlsx/pptx/docx/hwp …)는 본문 없이 status='본문 미지원' 으로 등록만 한다.
# 목록에는 남겨야 관리자가 무엇이 왜 안 들어갔는지 화면에서 볼 수 있다.
TEXT_EXTS = {".csv", ".txt", ".md"}
PDF_EXTS = {".pdf"}
MAX_BODY_CHARS = 300_000


# ★ 관리자 데이터의 조회는 GET /api/bootstrap 이 담당한다 —
#   instruction·sources·uploads·admins 를 같은 store 함수
#   (store.instruction/_sources/_uploads/_admins)로 내려준다. 여기에는 변경(PUT/POST/DELETE)만 둔다.
#   **그 store 함수들은 절대 지우지 마라** — bootstrap 과 아래 reset_instruction 이 쓴다.


@router.put("/instruction")
def put_instruction(body: InstructionIn, _: str = Depends(current_email)):
    store.set_setting("instruction", body.text)
    return {"ok": True}


@router.post("/instruction/reset")
def reset_instruction(_: str = Depends(current_email)):
    default = store.instruction()["default"]
    store.set_setting("instruction", default)
    return {"ok": True, "text": default}


# ★ 메타데이터만 받는 업로드 경로(JSON)를 만들지 마라 — body 와 extracted_at 이 NULL 인
#   행이 생겨 RAG 게이트(status='검수 완료' AND extracted_at IS NOT NULL)를 영원히
#   통과하지 못한다. 목록에만 뜨고 아무 데도 쓰이지 않는 유령 행이 된다.
#   업로드 경로는 아래 /uploads/file 하나뿐이고, 승인은 '업로드 시 선택'(use_now)이다.


def _human_size(n: int) -> str:
    """화면 표기용 파일 크기. 기존 시드가 '2.4 MB' 형태라 같은 모양으로 맞춘다."""
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def _extract(filename: str, raw: bytes) -> tuple[str | None, str]:
    """(본문, status) — 추출 불가 포맷은 (None, '본문 미지원').

    추출 자체가 예외로 실패하는 경우(깨진 PDF 등)도 '본문 미지원' 으로 떨어뜨린다.
    업로드는 성공시켜야 관리자가 목록에서 실패 사실을 볼 수 있다.
    """
    ext = ("." + filename.rsplit(".", 1)[-1].lower()) if "." in filename else ""
    if ext in PDF_EXTS:
        try:
            from app.pipeline.farming import pdf
            text = pdf.extract_text(raw, max_chars=MAX_BODY_CHARS)
        except Exception:
            return None, "본문 미지원"
    elif ext in TEXT_EXTS:
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = raw.decode("cp949")
            except UnicodeDecodeError:
                return None, "본문 미지원"
        text = text[:MAX_BODY_CHARS]
    else:
        return None, "본문 미지원"

    text = text.strip()
    if not text:
        return None, "본문 미지원"
    return text, "본문 추출됨"


# 업로드 상한. 이보다 큰 파일은 413 으로 거절한다 — 본문 전체를 메모리에 올리기 때문이다.
MAX_UPLOAD_BYTES = 20 * 1024 * 1024


@router.post("/uploads/file")
def add_upload_file(
    file: UploadFile = File(...),
    aff: str = Form("전사"),
    use_now: bool = Form(False),
    _: str = Depends(current_email),
):
    """내부 자료 파일 업로드(multipart) — 본문까지 추출해 저장한다.

    승인은 **업로드 시 선택**한다(사용자 결정). 화면의 '바로 사용' 체크박스가
    use_now 로 온다.
      use_now=True  → status='검수 완료'. 본문 추출이 됐다면 그 자리에서
                      RAG 게이트(status='검수 완료' AND extracted_at IS NOT NULL)를 통과한다.
      use_now=False → 지금처럼 '본문 추출됨' 에 머문다(프롬프트에 투입되지 않는다).
    별도 승인 화면·엔드포인트는 없다.

    ★ 본문 추출에 실패한 파일(xlsx/pptx/hwp · 깨진 PDF)은 use_now=True 라도
      '본문 미지원' 그대로 둔다. 본문이 없으면 프롬프트에 실을 것이 없고,
      status 만 '검수 완료' 로 올리면 게이트를 통과한 것처럼 보이는 거짓 상태가 된다.

    ★ 일부러 `async def` 가 아니다. PDF 파싱(CPU)과 SQLite 쓰기를 동기로 하는데
      async 핸들러 안에서 하면 이벤트 루프를 통째로 막아 업로드 한 건이 서버 전체를
      세운다(269p PDF 로 2초 정지 실측). 동기 함수로 두면 FastAPI 가 threadpool 에서
      돌려 다른 요청이 계속 처리된다.
    """
    name = (file.filename or "").strip()
    if not name:
        raise HTTPException(status_code=400, detail="파일명이 필요합니다.")
    raw = file.file.read(MAX_UPLOAD_BYTES + 1)
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"파일이 너무 큽니다. {MAX_UPLOAD_BYTES // (1024 * 1024)}MB 이하만 올릴 수 있습니다.",
        )
    if not raw:
        raise HTTPException(status_code=400, detail="빈 파일입니다.")

    body, status = _extract(name, raw)
    if use_now and body:
        status = "검수 완료"
    upload = store.add_upload(name, aff or "전사", _human_size(len(raw)), body, status)
    # chars 는 화면 계약(6키)에 없으므로 응답에만 참고값으로 덧붙인다.
    return {"upload": upload, "chars": len(body) if body else 0, "st": status}


@router.post("/members")
def add_member(body: AdminMemberIn, _: str = Depends(current_email)):
    mail = body.mail.strip().lower()
    if "@" not in mail:
        raise HTTPException(status_code=400, detail="올바른 이메일이 아닙니다.")
    store.add_admin(mail, body.role, body.note)
    return {"ok": True}


@router.delete("/members/{mail}")
def remove_member(mail: str, _: str = Depends(current_email)):
    if not store.remove_admin(mail.strip().lower()):
        raise HTTPException(status_code=404, detail="해당 계정을 찾을 수 없습니다.")
    return {"ok": True}
