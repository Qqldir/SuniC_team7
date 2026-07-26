"""SEC EDGAR 크롤러.

- company_tickers.json : ticker → CIK 매핑
- submissions/CIK{10자리}.json : 최근 공시 목록

SEC 는 연락처 포함 User-Agent 를 요구합니다(SEC_USER_AGENT). 미설정 시 skip.
"""
import json
from datetime import date, timedelta
from typing import Dict, List

import httpx

from app.config import SEC_USER_AGENT, DATA_DIR
from app.pipeline.farming.base import RawDoc, KIND_SEC
from app.pipeline.farming.watchlist import Watch, sec_targets

TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik10}.json"
ARCHIVE = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{doc}"
_TICKER_CACHE = DATA_DIR / "sec_tickers.json"

# 수집 대상 서식
FORMS = {"10-K", "10-Q", "8-K", "6-K", "20-F", "40-F"}


def enabled() -> bool:
    return bool(SEC_USER_AGENT)


def _headers() -> dict:
    return {"User-Agent": SEC_USER_AGENT, "Accept-Encoding": "gzip, deflate"}


def _ticker_to_cik() -> Dict[str, int]:
    if _TICKER_CACHE.exists():
        raw = json.loads(_TICKER_CACHE.read_text(encoding="utf-8"))
    else:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        r = httpx.get(TICKERS_URL, headers=_headers(), timeout=30)
        r.raise_for_status()
        raw = r.json()
        _TICKER_CACHE.write_text(json.dumps(raw), encoding="utf-8")
    return {row["ticker"].upper(): int(row["cik_str"]) for row in raw.values()}


def _recent_filings(cik: int, since: date) -> List[dict]:
    r = httpx.get(SUBMISSIONS_URL.format(cik10=f"{cik:010d}"), headers=_headers(), timeout=20)
    r.raise_for_status()
    data = r.json()
    recent = data.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accs = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    prim_desc = recent.get("primaryDocDescription", [])

    out = []
    for i, form in enumerate(forms):
        if form not in FORMS:
            continue
        fdate = dates[i] if i < len(dates) else ""
        try:
            if date.fromisoformat(fdate) < since:
                continue
        except ValueError:
            continue
        out.append({
            "form": form, "date": fdate,
            "accession": accs[i] if i < len(accs) else "",
            "doc": docs[i] if i < len(docs) else "",
            "desc": prim_desc[i] if i < len(prim_desc) else "",
        })
    return out


def crawl(since_days: int) -> List[RawDoc]:
    if not enabled():
        print("[sec] SEC_USER_AGENT 미설정 — 건너뜀")
        return []

    targets: List[Watch] = sec_targets()
    since = date.today() - timedelta(days=since_days)

    try:
        cik_map = _ticker_to_cik()
    except Exception as e:
        print(f"[sec] 티커 매핑 로드 실패: {e}")
        return []

    docs: List[RawDoc] = []
    for w in targets:
        cik = cik_map.get(w.sec_ticker.upper())
        if not cik:
            print(f"[sec] CIK 미발견: {w.sec_ticker}")
            continue
        try:
            filings = _recent_filings(cik, since)
        except Exception as e:
            print(f"[sec] {w.name} 공시 조회 실패: {e}")
            continue
        for f in filings:
            acc = f["accession"]
            acc_nodash = acc.replace("-", "")
            url = ARCHIVE.format(cik=cik, acc_nodash=acc_nodash, doc=f["doc"]) if f["doc"] else VIEWER_FALLBACK(cik, acc)
            desc = (f["desc"] or "").strip()
            title = f"{f['form']} — {desc}" if desc and desc != f["form"] else f["form"]
            docs.append(RawDoc(
                ext_id=acc,
                source=w.name,
                kind=KIND_SEC,
                published_on=f["date"],
                title=title,
                url=url,
                tags=list(w.tags),
            ))
    print(f"[sec] {len(docs)}건 수집")
    return docs


def VIEWER_FALLBACK(cik: int, acc: str) -> str:
    return f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}"
