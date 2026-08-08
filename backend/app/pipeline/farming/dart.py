"""OpenDART(전자공시) 크롤러.

API 문서: https://opendart.fss.or.kr/guide/main.do
- corpCode.xml : 전체 기업 고유번호(corp_code) ↔ 명칭 매핑 (zip, 약 30MB)
- list.json    : 기업별 공시 목록 (rcept_no, report_nm, rcept_dt ...)
- document.xml : 공시서류 원본파일 (zip) — 본문 텍스트 확보용

키가 없으면(DART_API_KEY 미설정) 이 소스는 조용히 건너뜁니다.
목록 조회는 저렴하지만 원문은 건당 비용이 있으므로(일 20,000건 한도),
fetch_document 는 crawler 가 선별한 건에만 호출합니다.
"""
import io
import re
import zipfile
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from typing import Dict, List

import httpx

from app.config import DART_API_KEY, DATA_DIR
from app.pipeline.farming.base import (
    DART_SLEEP, RawDoc, KIND_ADHOC, KIND_PERIODIC, polite,
)
from app.pipeline.farming.watchlist import Watch, dart_targets

BASE = "https://opendart.fss.or.kr/api"
VIEWER = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo={}"
_CORP_CACHE = DATA_DIR / "dart_corpcode.xml"

# 이 소스가 의미를 가지려면 필요한 최소 크롤 창(일). crawler.crawl_all 이 max() 로 적용한다.
#
# 왜 30일(CRAWL_SINCE_DAYS 기본값)로는 안 되는가 — 버그가 아니라 자료 주기의 문제다.
# 정기보고서 제출기한은 분기(3/31·9/30 종료) +45일, 반기(6/30) +45일, 사업(12/31) +90일이라
# 제출일이 5/15 · 8/14 · 11/14 · 3/31 에 몰린다. 인접 제출일 간격은
#   5/15→8/14 = 91일, 8/14→11/14 = 92일, 11/14→3/31 = **137일**, 3/31→5/15 = 45일.
# 따라서 연중 어느 날에 크롤해도 기업당 정기보고서를 최소 1건 잡으려면 창이 137일 이상이어야 한다.
# 실측(2026-08-06, 감시 대상 6개사): 30일 0건 · 60일 0건 · 90일 6건(1건씩) · 150일 13건(2건씩).
# 여유를 둬 150일로 잡는다. 목록 조회는 창을 넓혀도 4초대로 같고(페이지네이션만 늘어남),
# 재크롤은 UPSERT 라 이미 정제된 건을 덮지 않는다.
#
# 반대로 전역 CRAWL_SINCE_DAYS 를 150 으로 올리지 않는 이유: 뉴스는 관련성이 며칠 단위로
# 식어서 5개월치를 끌어오면 화면이 지난 기사로 덮인다. 창은 소스마다 달라야 한다.
MIN_SINCE_DAYS = 150

# crawler 가 주는 per_source 상한에 곱할 배수. 목록 전량을 덮는 것이 목표다.
#
# 왜 뉴스와 같은 상한에 묶으면 안 되는가 — 원문 확보 비용이 자릿수 단위로 다르다.
# 실측(2026-08-07, 감시 대상 6개사 · 목록 14건):
#   fetch_document 14/14 성공(실패 0), 건당 0.37초 + polite 0.10 = 0.47초 → 14건 전량 6.6초.
#   일 20,000건 한도 대비 0.07%. 하루 20회 크롤해도 1.4% 라 한도가 사실상 제약이 아니다.
# 반면 --with-docs 6 으로 크롤한 프로덕션에서는 DART 8건이 '한도밖' 으로 통째 빠져 있었다.
# 즉 여기서 잃는 것이 뉴스 페이월보다 크고, 되찾는 비용은 3.8초다.
# 기본값 --with-docs 5 × 4 = 20 ≥ 목록 14건. _pick 은 그룹 크기에서 멈추므로 과잉 설정은 무해하다.
BODY_FACTOR = 4

_TAG_RE = re.compile(r"<[^>]+>")
# 개행은 보존하고 나머지 공백만 축약 (표 구조를 줄 단위로 남기기 위해)
_WS_RE = re.compile(r"[ \t\r\f\v]+")


def enabled() -> bool:
    return bool(DART_API_KEY)


def _guard_json_error(r: httpx.Response) -> None:
    """zip 을 기대한 응답이 JSON 이면 API 오류다(키 만료·한도 초과 등).

    가드가 없으면 zipfile.BadZipFile 로 튀어 원인 파악이 어렵습니다.
    """
    if r.headers.get("content-type", "").startswith("application/json"):
        raise RuntimeError(f"DART API 오류: {r.text[:200]}")


def _load_corp_map() -> Dict[str, str]:
    """정식 명칭 → corp_code. CORPCODE.xml 을 받아 캐시 후 파싱."""
    if not _CORP_CACHE.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        # 약 30MB 라 timeout 을 넉넉히 잡습니다.
        r = httpx.get(f"{BASE}/corpCode.xml", params={"crtfc_key": DART_API_KEY}, timeout=60)
        r.raise_for_status()
        _guard_json_error(r)
        with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
            name = zf.namelist()[0]
            _CORP_CACHE.write_bytes(zf.read(name))

    root = ET.fromstring(_CORP_CACHE.read_text(encoding="utf-8"))
    mapping: Dict[str, str] = {}
    for node in root.iter("list"):
        corp = (node.findtext("corp_name") or "").strip()
        code = (node.findtext("corp_code") or "").strip()
        if corp and code:
            mapping.setdefault(corp, code)
    return mapping


def _kind(pblntf_ty: str) -> str:
    # A: 정기공시, 그 외(B 주요사항 등): 수시로 간주
    return KIND_PERIODIC if pblntf_ty == "A" else KIND_ADHOC


def _list_disclosures(corp_code: str, bgn: str, end: str) -> List[dict]:
    """기업 공시 목록 (정기 A + 주요사항 B). 페이지네이션 포함."""
    out: List[dict] = []
    for ty in ("A", "B"):
        page = 1
        while True:
            r = httpx.get(
                f"{BASE}/list.json",
                params={
                    "crtfc_key": DART_API_KEY, "corp_code": corp_code,
                    "bgn_de": bgn, "end_de": end, "pblntf_ty": ty,
                    "page_no": page, "page_count": 100,
                },
                timeout=20,
            )
            data = r.json()
            status = data.get("status")
            if status != "000":
                # 013(데이터 없음)은 정상. 그 외는 키·파라미터 문제일 수 있어 남깁니다.
                if status != "013":
                    print(f"[dart] list.json status={status} {data.get('message', '')}")
                break
            for row in data.get("list", []):
                row["_pblntf_ty"] = ty
                out.append(row)
            if page >= int(data.get("total_page", 1)):
                break
            page += 1
            polite(DART_SLEEP)
    return out


def xml_to_text(xml_bytes: bytes) -> str:
    """DART 공시 원본 XML → 평문 텍스트.

    원본은 인코딩이 utf-8 / cp949 로 섞여 있어 순차 폴백합니다.
    (euc-kr 은 cp949 의 부분집합이라 별도 시도 의미가 없습니다.)
    """
    for enc in ("utf-8", "cp949"):
        try:
            text = xml_bytes.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = xml_bytes.decode("utf-8", errors="ignore")

    text = _TAG_RE.sub(" ", text)
    text = _WS_RE.sub(" ", text)
    lines = [ln.strip() for ln in text.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def _merge_fragments(text: str, min_len: int = 40) -> str:
    """짧은 줄을 문단으로 병합.

    태그 제거만 하면 표 셀 하나가 한 줄이 되어 줄당 평균 10여 자로 파편화됩니다.
    LLM 입력 토큰이 개행으로 낭비되므로, 짧은 줄은 이어 붙입니다.
    """
    out: List[str] = []
    buf = ""
    for ln in text.split("\n"):
        buf = f"{buf} {ln}".strip() if buf else ln
        if len(buf) >= min_len:
            out.append(buf)
            buf = ""
    if buf:
        out.append(buf)
    return "\n".join(out)


def fetch_document(rcept_no: str, max_chars: int = 200_000) -> str:
    """공시서류 원본(document.xml zip) → 본문 텍스트.

    zip 안에 여러 파일이 들어있을 수 있어 전 멤버를 이어 붙입니다.
    호출 측에서 rate limit(polite)을 지켜야 합니다.
    """
    r = httpx.get(
        f"{BASE}/document.xml",
        params={"crtfc_key": DART_API_KEY, "rcept_no": rcept_no},
        timeout=60,
    )
    r.raise_for_status()
    _guard_json_error(r)

    parts: List[str] = []
    with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
        for name in zf.namelist():
            parts.append(xml_to_text(zf.read(name)))
    return _merge_fragments("\n\n".join(parts))[:max_chars]


def crawl(since_days: int) -> List[RawDoc]:
    if not enabled():
        print("[dart] DART_API_KEY 미설정 — 건너뜀")
        return []

    targets: List[Watch] = dart_targets()
    end = date.today()
    bgn = end - timedelta(days=since_days)
    bgn_s, end_s = bgn.strftime("%Y%m%d"), end.strftime("%Y%m%d")

    try:
        corp_map = _load_corp_map()
    except Exception as e:  # 키 오류·네트워크
        print(f"[dart] corpCode 로드 실패: {e}")
        return []

    docs: List[RawDoc] = []
    for w in targets:
        code = corp_map.get(w.dart_name)
        if not code:
            print(f"[dart] corp_code 미발견: {w.dart_name}")
            continue
        try:
            rows = _list_disclosures(code, bgn_s, end_s)
        except Exception as e:
            print(f"[dart] {w.name} 목록 조회 실패: {e}")
            continue
        for row in rows:
            rcept = row.get("rcept_no", "")
            rcept_dt = row.get("rcept_dt", "")
            published = f"{rcept_dt[:4]}-{rcept_dt[4:6]}-{rcept_dt[6:]}" if len(rcept_dt) == 8 else rcept_dt
            docs.append(RawDoc(
                ext_id=rcept,
                source=row.get("corp_name", w.name),
                kind=_kind(row.get("_pblntf_ty", "B")),
                published_on=published,
                title=(row.get("report_nm") or "").strip(),
                publisher="DART",
                url=VIEWER.format(rcept),
                tags=list(w.tags),
                # classify.dart_kind 의 입력 (자료 종류 라벨 계산용)
                meta={
                    "report_nm": (row.get("report_nm") or "").strip(),
                    "pblntf_ty": row.get("_pblntf_ty", "B"),
                },
            ))
    print(f"[dart] {len(docs)}건 수집")
    return docs


# 원문 확보 우선순위: 정기보고서(사업·분기)가 사례 밀도가 높습니다.
def body_priority(doc: RawDoc) -> int:
    return 0 if doc.kind == KIND_PERIODIC else 1


def fetch_body(doc: RawDoc) -> str:
    """crawler 가 선별한 RawDoc 의 본문을 확보한다. rate limit 포함."""
    text = fetch_document(doc.ext_id)
    polite(DART_SLEEP)
    return text
