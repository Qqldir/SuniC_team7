"""SEC EDGAR 크롤러.

- company_tickers.json : ticker → CIK 매핑
- submissions/CIK{10자리}.json : 최근 공시 목록
- Archives/... : primary document 원문 (본문 텍스트 확보용)
- efts.sec.gov/LATEST/search-index : 전문검색 — watchlist 밖 기업의 사례 역방향 발굴

SEC 는 연락처 포함 User-Agent 를 요구합니다(SEC_USER_AGENT). 미설정 시 skip.
초당 10건을 넘기면 약 10분간 IP 가 차단되므로 모든 요청 뒤에 polite() 를 둡니다.
"""
import html
import json
import re
from datetime import date, timedelta
from typing import Dict, List

import httpx

from app.config import SEC_USER_AGENT, DATA_DIR
from app.pipeline.farming.base import SEC_SLEEP, RawDoc, KIND_SEC, polite
from app.pipeline.farming.watchlist import Watch, sec_targets

TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik10}.json"
ARCHIVE = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{doc}"
INDEX_HEADERS = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc_nodash}/{acc}-index-headers.html"
FTS_URL = "https://efts.sec.gov/LATEST/search-index"
_TICKER_CACHE = DATA_DIR / "sec_tickers.json"

# index-headers 의 SGML DOCUMENT 블록에서 타입과 파일명 추출
_DOC_RE = re.compile(r"<TYPE>([^\r\n<]+).*?<FILENAME>([^\r\n<]+)", re.S)

# 수집 대상 서식
FORMS = {"10-K", "10-Q", "8-K", "6-K", "20-F", "40-F"}

# crawler 가 주는 per_source 상한에 곱할 배수. 목록 전량을 덮는 것이 목표다.
#
# 차단선은 '초당 10건' 이지 '하루 몇 건' 이 아니다 — 건수를 늘려도 요청률은 변하지 않는다.
# 실측(2026-08-07, 감시 대상 4개사 · 목록 12건):
#   fetch_body 12/12 성공(실패 0), 건당 0.53초 → 12건 전량 6.3초.
#   건당 요청 2회(index-headers + document)이고 그 사이마다 SEC_SLEEP=0.15 가 들어가
#   **실측 요청률 3.80 req/s** — 차단선 10 req/s 의 38% 다. 건수와 무관하게 일정하다.
# ⚠ 따라서 상한을 올리는 것은 안전하지만 SEC_SLEEP 을 줄이는 것은 안전하지 않다.
#   네트워크 왕복만 요청당 약 0.115초라 SEC_SLEEP=0 이면 8.7 req/s 로 차단선에 붙는다.
#   IP 가 약 10분 차단된다. 간격은 건드리지 말고 건수만 늘려라.
# 기본값 --with-docs 5 × 4 = 20 ≥ 목록 12건. _pick 은 그룹 크기에서 멈춘다.
BODY_FACTOR = 4

_SCRIPT_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
_TAG_RE = re.compile(r"<[^>]+>")
# \xa0 은 &nbsp; 를 unescape 한 결과 — 일반 공백으로 눕혀야 토큰이 낭비되지 않습니다.
_WS_RE = re.compile(r"[ \t\xa0]+")


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


def html_to_text(raw_html: str, max_chars: int = 300_000) -> str:
    """SEC 원문 HTML → 평문 텍스트.

    unescape 를 빠뜨리면 &#160; / &#9744; 같은 숫자 엔티티가 그대로 남습니다.
    """
    # 첨부 문서는 SGML <DOCUMENT><TYPE>...<TEXT> 봉투에 싸여 옵니다.
    # 태그만 벗기면 헤더 값이 본문 앞에 텍스트로 남으므로 봉투를 먼저 걷어냅니다.
    marker = raw_html.find("<TEXT>")
    if marker != -1 and marker < 2000:
        raw_html = raw_html[marker + len("<TEXT>"):]

    text = _SCRIPT_RE.sub(" ", raw_html)
    text = _TAG_RE.sub(" ", text)
    text = html.unescape(text)
    text = _WS_RE.sub(" ", text)
    lines = [ln.strip() for ln in text.split("\n")]
    return "\n".join(ln for ln in lines if ln)[:max_chars]


def fetch_primary_doc(cik: int, accession: str, doc: str) -> str:
    """지정한 문서 하나를 텍스트로 확보."""
    url = ARCHIVE.format(cik=cik, acc_nodash=accession.replace("-", ""), doc=doc)
    r = httpx.get(url, headers=_headers(), timeout=60, follow_redirects=True)
    r.raise_for_status()
    return html_to_text(r.text)


def list_documents(cik: int, accession: str) -> List[dict]:
    """공시에 포함된 문서 목록 [{type, filename}].

    index-headers 파일에 SGML 헤더가 HTML 이스케이프된 채 들어있습니다.
    index.json 은 문서 '타입'을 주지 않아(아이콘 이름만 있음) 이쪽을 씁니다.
    """
    url = INDEX_HEADERS.format(
        cik=cik, acc_nodash=accession.replace("-", ""), acc=accession,
    )
    r = httpx.get(url, headers=_headers(), timeout=30, follow_redirects=True)
    r.raise_for_status()
    raw = html.unescape(r.text)
    return [
        {"type": t.strip(), "filename": f.strip()}
        for t, f in _DOC_RE.findall(raw)
    ]


def pick_content_doc(docs: List[dict], primary: str) -> str:
    """본문이 실제로 들어있는 문서를 고른다.

    8-K 의 primary document 는 표지 서식일 뿐이고 실적·보도자료는 EX-99 첨부에 있습니다
    (실측: Dow 8-K primary 26KB=표지 / EX-99.1 553KB=press release).
    EX-99 가 없으면 primary 로 되돌립니다.
    """
    for d in docs:
        if d["type"].upper().startswith("EX-99") and d["filename"].lower().endswith((".htm", ".html", ".txt")):
            return d["filename"]
    return primary


def full_text_search(query: str, forms: str = "8-K", days: int = 90, size: int = 10) -> List[dict]:
    """EDGAR 전문검색 — watchlist 에 없는 기업의 사례를 역방향으로 찾는다.

    예: full_text_search("cost reduction program") → 해당 문구가 담긴 8-K 목록.
    반환: [{company, form, date, id}] — id 는 "accession:document.htm".
    """
    if not enabled():
        print("[sec] SEC_USER_AGENT 미설정 — 전문검색 건너뜀")
        return []

    end = date.today()
    bgn = end - timedelta(days=days)
    r = httpx.get(
        FTS_URL,
        params={
            "q": f'"{query}"', "forms": forms, "dateRange": "custom",
            "startdt": bgn.isoformat(), "enddt": end.isoformat(),
            "from": 0, "size": size,
        },
        headers=_headers(), timeout=30,
    )
    r.raise_for_status()
    polite(SEC_SLEEP)

    hits = r.json().get("hits", {}).get("hits", [])
    out = []
    # 서버가 size 를 무시하고 최대 100건까지 돌려주므로 클라이언트에서 자른다.
    for h in hits[:size]:
        src = h.get("_source", {})
        names = src.get("display_names") or []
        roots = src.get("root_forms") or []
        out.append({
            "company": names[0] if names else "",
            # file_type 은 "EX-99.1" 같은 첨부 타입이라 원 서식이 아니다.
            "form": roots[0] if roots else src.get("file_type", ""),
            "date": src.get("file_date", ""),
            "id": h.get("_id", ""),
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
        finally:
            polite(SEC_SLEEP)
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
                publisher="SEC EDGAR",
                url=url,
                tags=list(w.tags),
                # desc 는 classify.sec_kind 의 8-K 실적 판정 입력이다.
                meta={"cik": cik, "doc": f["doc"], "form": f["form"], "desc": desc},
            ))
    print(f"[sec] {len(docs)}건 수집")
    return docs


# 원문 확보 우선순위: 8-K 는 보도자료성이라 사례 밀도가 가장 높습니다.
def body_priority(doc: RawDoc) -> int:
    return 0 if doc.meta.get("form") == "8-K" else 1


def fetch_body(doc: RawDoc) -> str:
    """crawler 가 선별한 RawDoc 의 본문을 확보한다. rate limit 포함.

    primary document 대신 EX-99 첨부(보도자료)를 우선합니다 — 8-K 의 primary 는
    표지 서식뿐이라 그대로 쓰면 LLM 이 판단할 내용이 없습니다.
    """
    cik, primary = doc.meta.get("cik"), doc.meta.get("doc")
    if not cik or not primary:
        return ""

    target = primary
    try:
        docs = list_documents(cik, doc.ext_id)
        polite(SEC_SLEEP)
        target = pick_content_doc(docs, primary)
    except Exception as e:
        # 첨부 목록을 못 읽어도 primary 로 진행 — 본문 확보 자체를 포기하지 않는다.
        print(f"[sec] 첨부 목록 실패 {doc.ext_id}: {e}")

    if target != primary:
        print(f"[sec] EX-99 첨부 사용: {target}")
    text = fetch_primary_doc(cik, doc.ext_id, target)
    polite(SEC_SLEEP)
    return text


def VIEWER_FALLBACK(cik: int, acc: str) -> str:
    return f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}"
