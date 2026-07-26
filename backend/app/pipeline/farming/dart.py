"""OpenDART(전자공시) 크롤러.

API 문서: https://opendart.fss.or.kr/guide/main.do
- corpCode.xml : 전체 기업 고유번호(corp_code) ↔ 명칭 매핑 (zip)
- list.json    : 기업별 공시 목록 (rcept_no, report_nm, rcept_dt ...)

키가 없으면(DART_API_KEY 미설정) 이 소스는 조용히 건너뜁니다.
"""
import io
import zipfile
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from typing import Dict, List

import httpx

from app.config import DART_API_KEY, DATA_DIR
from app.pipeline.farming.base import RawDoc, KIND_ADHOC, KIND_PERIODIC
from app.pipeline.farming.watchlist import Watch, dart_targets

BASE = "https://opendart.fss.or.kr/api"
VIEWER = "https://dart.fss.or.kr/dsaf001/main.do?rcpNo={}"
_CORP_CACHE = DATA_DIR / "dart_corpcode.xml"


def enabled() -> bool:
    return bool(DART_API_KEY)


def _load_corp_map() -> Dict[str, str]:
    """정식 명칭 → corp_code. CORPCODE.xml 을 받아 캐시 후 파싱."""
    if not _CORP_CACHE.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        r = httpx.get(f"{BASE}/corpCode.xml", params={"crtfc_key": DART_API_KEY}, timeout=30)
        r.raise_for_status()
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
            if data.get("status") != "000":  # 013: 데이터 없음 등
                break
            for row in data.get("list", []):
                row["_pblntf_ty"] = ty
                out.append(row)
            if page >= int(data.get("total_page", 1)):
                break
            page += 1
    return out


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
                url=VIEWER.format(rcept),
                tags=list(w.tags),
            ))
    print(f"[dart] {len(docs)}건 수집")
    return docs
