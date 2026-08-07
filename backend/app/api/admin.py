"""관리자 화면 API — 생성 인스트럭션 · 내부 자료 · 로그인 계정 관리."""
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from app import store
from app.api.deps import current_admin, current_email
from app.db.database import get_connection
from app.models import AdminUserIn, InstructionIn
from app.security import hash_password

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
#   instruction·sources·uploads 를 같은 store 함수
#   (store.instruction/_sources/_uploads)로 내려준다. 여기에는 변경(PUT/POST/DELETE)만 둔다.
#   **그 store 함수들은 절대 지우지 마라** — bootstrap 과 아래 reset_instruction 이 쓴다.
#   예외는 로그인 계정 목록(GET /users)이다 — 계정은 화면 초기 데이터가 아니고
#   관리자만 볼 수 있어야 해서 bootstrap 에 실을 수 없다.


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


# ─────────────── 로그인 계정 관리 (화면 '계정 관리' 탭) ───────────────
#
# ★ 이 4개에만 current_admin(403)을 씌운다. 위쪽 instruction / instruction-reset /
#   uploads/file 에는 **씌우지 마라** — 관리자 탭은 모든 로그인 사용자에게 보이고
#   프론트가 그 3개에는 403 분기를 두지 않아, 게이트를 씌우면 저장 버튼이 아무 메시지
#   없이 실패한다. 계정 목록만 403 메시지로 "권한 있는 계정만" 을 안내하는 설계다.
#
# 초기 비밀번호는 서버가 정한다(프론트가 password 를 보내지 않는다). seed_users 와 같은 값.
DEFAULT_PASSWORD = "1111"


@router.get("/users")
def list_users(_: str = Depends(current_admin)):
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT email, is_active, is_admin, created_at FROM app_user "
            "ORDER BY is_admin DESC, created_at"
        ).fetchall()
    finally:
        conn.close()
    # is_admin/is_active 는 화면이 truthy 로만 보므로 SQLite 0/1 정수 그대로 내린다.
    return {"users": [dict(r) for r in rows]}


@router.post("/users")
def create_user(body: AdminUserIn, _: str = Depends(current_admin)):
    email = body.email.strip().lower()
    if "@" not in email:
        raise HTTPException(status_code=400, detail="올바른 이메일이 아닙니다.")
    pw = body.password or DEFAULT_PASSWORD
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    try:
        if conn.execute("SELECT 1 FROM app_user WHERE email = ?", (email,)).fetchone():
            raise HTTPException(status_code=409, detail="이미 등록된 계정입니다.")
        conn.execute(
            "INSERT INTO app_user(email, password_hash, is_active, is_admin, created_at) "
            "VALUES (?,?,1,?,?)",
            (email, hash_password(pw), int(body.is_admin), now),
        )
        conn.commit()
    finally:
        conn.close()
    return {"email": email, "initial_password": pw}


@router.post("/users/{email}/reset-password")
def reset_user_password(email: str, _: str = Depends(current_admin)):
    # 경로 파라미터는 프론트가 encodeURIComponent 로 보내고 Starlette 이 디코딩해 준다.
    email = email.strip().lower()
    conn = get_connection()
    try:
        n = conn.execute(
            "UPDATE app_user SET password_hash = ? WHERE email = ?",
            (hash_password(DEFAULT_PASSWORD), email),
        ).rowcount
        conn.commit()
    finally:
        conn.close()
    if n == 0:
        raise HTTPException(status_code=404, detail="해당 계정을 찾을 수 없습니다.")
    return {"ok": True, "email": email, "initial_password": DEFAULT_PASSWORD}


@router.delete("/users/{email}")
def delete_user(email: str, me: str = Depends(current_admin)):
    """계정 삭제 — 개인 데이터까지 **한 트랜잭션으로** 함께 지운다.

    ★ `DELETE FROM app_user` 한 줄로 하면 안 된다. app_user.email 을 참조하는 FK 가
      하나도 없어 CASCADE 가 돌지 않고, 같은 이메일로 계정을 다시 만들면 신규 사용자가
      전임자의 별점·기준값·산출식·발송설정을 그대로 물려받는다.
      탈퇴(DELETE /api/auth/me)와 같은 범위를 쓰려고 store.purge_user 를 부른다.
    ★ 마지막 관리자 가드가 필요하다. 관리자 둘이 서로를 지우면 0명이 될 수 있고,
      관리자를 만드는 유일한 API(POST /users)가 current_admin 뒤에 있어 그 순간부터
      CLI 로 다시 시드하기 전엔 아무도 계정 관리를 못 쓴다.
    """
    email = email.strip().lower()
    if email == me.strip().lower():
        raise HTTPException(status_code=400, detail="본인 계정은 삭제할 수 없습니다.")
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute(
            "SELECT is_admin FROM app_user WHERE email = ?", (email,)
        ).fetchone()
        if not row:
            conn.rollback()
            raise HTTPException(status_code=404, detail="해당 계정을 찾을 수 없습니다.")
        if row["is_admin"]:
            n = conn.execute("SELECT COUNT(*) AS n FROM app_user WHERE is_admin = 1").fetchone()["n"]
            if n <= 1:
                conn.rollback()
                raise HTTPException(status_code=400, detail="마지막 관리자 계정은 삭제할 수 없습니다.")
        store.purge_user(conn, email)
        conn.commit()
    except HTTPException:
        raise
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return {"ok": True}
