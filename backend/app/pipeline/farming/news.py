"""뉴스 크롤러 — Google News RSS (키 불필요) + 매체 원문 본문 확보.

검색어별 RSS 를 받아 최근 기사만 RawDoc 로 변환하고,
crawler 가 선별한 건에 한해 **매체 사이트의 기사 본문**을 직접 받아옵니다.
운영 단계에서는 정식 뉴스 API(예: 사내 계약 벤더)로 교체 가능.

⚠ robots 방침 — 두 층이 서로 다릅니다. 헷갈리지 마십시오.
  · **매체 기사 본문**(_fetch_article) → robots 를 지킵니다. 금지면 REASON_ROBOTS 로 건너뜁니다.
  · **Google News 진입 경로**(RSS 목록 · 기사 셸 · batchexecute RPC) → 지키지 **않습니다**.
    news.google.com/robots.txt 는 `Disallow: /` 에 /rss/ 를 Allow 하지 않으므로
    이 세 경로는 전부 금지 대상이고, 아래 _robots_allows() 도 셋 다 False 를 돌려줍니다.
    사내 검증 용도라 현행 유지하기로 사용자가 결정했습니다(2026-08-07).
    config.NEWS_ROBOTS_STRICT=1 로 두면 진입 자체를 막습니다 — 외부 배포 전 필수.

⚠ 저작권 방침 — 여기서 받은 본문은 **LLM 정제 입력으로만** 씁니다.
  RawDoc.body 는 프로세스 안에서만 살고 DB 에는 들어가지 않으며,
  feed_item.summary 에는 LLM 이 만든 요약만 남습니다.
  정제에 실패했을 때 본문 앞부분을 잘라 요약 자리에 넣는 폴백도 막혀 있습니다
  (llm.naive_summary 가 meta['body_restricted'] 를 보고 제목으로 되돌립니다).
"""
import html
import json
import re
import hashlib
import time
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from email.utils import parsedate_to_datetime
from typing import Dict, List, Optional
from urllib.parse import quote, urlsplit
from urllib.robotparser import RobotFileParser

import httpx

from app.config import NEWS_ROBOTS_STRICT, NEWS_USER_AGENT
from app.pipeline.farming import classify
from app.pipeline.farming.base import (
    NEWS_SLEEP, REASON_EXTRACT, REASON_REQUEST, REASON_RESOLVE, REASON_ROBOTS,
    REASON_SKIP, RawDoc, KIND_NEWS, polite,
)
from app.pipeline.farming.watchlist import Watch, news_targets

RSS = "https://news.google.com/rss/search?q={q}&hl={hl}&gl={gl}&ceid={ceid}"
# 로케일을 ko 로 고정하면 영어 검색어가 전부 0건이 됩니다.
# (실측: "Dow Chemical cost reduction" → ko 0건 / en-US 74건)
LOCALE_KO = {"hl": "ko", "gl": "KR", "ceid": "KR:ko"}
LOCALE_EN = {"hl": "en-US", "gl": "US", "ceid": "US:en"}

_TAG_RE = re.compile(r"<[^>]+>")
_HANGUL_RE = re.compile(r"[가-힣]")

# 금융 포털이 SEC 공시를 그대로 재게시한 항목. **수집 단계에서 버린다.**
#
# 왜 본문 확보가 아니라 수집에서 거르는가 — 이건 품질 문제가 아니라 중복 문제다.
# 실측(2026-08-07): 애그리게이터 본문과 SEC 원문의 어휘 포함률이 0.99~1.00 이었다
# (Stock Titan 'Cheniere 10-Q' 20,000자 ⊂ SEC 10-Q 170,825자 / Valero 8-K EX-99 는 1.00).
# 게다가 재게시본은 표지·XBRL 헤더만 남아 있어 SEC 원문보다 정보가 적다.
# 그 4개사(Dow·LyondellBasell·Cheniere·Valero)는 SEC 소스가 이미 12/12 로 원문을 확보한다.
# 즉 받아도 같은 사실을 두 번 적재하고 LLM 예산만 두 번 쓴다.
#
# 판정은 **매체명이 아니라 제목**으로 한다 — 같은 매체라도 실적 컨퍼런스콜 전사처럼
# SEC 공시에 없는 자료를 내놓기 때문이다(그건 버리면 안 된다).
# 서식명을 헤드라인으로 쓴 제목만 걸린다: "Form 8K Cheniere Energy Partners For: 6 August".
# 실측 43건에 오탐 0 · 적중 1.
_SEC_REPOST_RE = re.compile(
    r"\bForm\s*(?:8-?K|10-?[QK]|6-?K|20-?F|S-\d)\b", re.I,
)


def enabled() -> bool:
    return True


def _locale_for(query: str) -> dict:
    """검색어에 한글이 있으면 한국 로케일, 아니면 미국 로케일."""
    return LOCALE_KO if _HANGUL_RE.search(query or "") else LOCALE_EN


def _strip_html(s: str) -> str:
    return html.unescape(_TAG_RE.sub("", s or "")).strip()


_BODY_MIN = 20


def _body_of(description: str, title: str, publisher: str) -> str:
    """RSS description → 본문. 실질 내용이 없으면 ''.

    Google News 의 description 은 본문이 아니라 제목 + 매체명 재출력이다(실측 41/41).
    이걸 body 로 두면 evidence_grade 가 '요약문' 으로 부풀고, LLM 은 제목을 두 번 읽는다.
    ''를 돌려주면 crawler.fetch_bodies 가 이 건을 원문 확보 대상으로 집는다.
    """
    text = _strip_html(description)
    if not text:
        return ""
    residue = text.replace(title, " ")
    if publisher:
        residue = residue.replace(publisher, " ")
    residue = re.sub(r"\s+", " ", residue).strip(" -–—·|,")
    return text if len(residue) >= _BODY_MIN else ""


def _to_date(pub: str) -> str:
    try:
        return parsedate_to_datetime(pub).date().isoformat()
    except (TypeError, ValueError):
        return ""


def _crawl_query(w: Watch, since: date, per_query: int) -> List[RawDoc]:
    url = RSS.format(q=quote(w.news_query), **_locale_for(w.news_query))
    r = httpx.get(url, timeout=20, follow_redirects=True)
    r.raise_for_status()
    root = ET.fromstring(r.content)

    docs: List[RawDoc] = []
    for item in root.iter("item"):
        title = _strip_html(item.findtext("title") or "")
        link = (item.findtext("link") or "").strip()
        pub = item.findtext("pubDate") or ""
        published = _to_date(pub)
        if not title or not published:
            continue
        if date.fromisoformat(published) < since:
            continue
        # RSS <source> 는 '어디에 실렸나'(매체)다. 발표 주체(source)는 감시 대상 이름이어야
        # 화면의 계열사·기업 축이 흔들리지 않는다.
        source_el = item.find("source")
        raw_publisher = (source_el.text.strip() if source_el is not None and source_el.text else "")
        # 접미사 제거는 **원본 <source> 값**으로 해야 한다 — 제목 끝에 붙는 건
        # 'ㅡ v.daum.net' 처럼 정규화 전 표기이기 때문이다.
        title = classify.strip_outlet_suffix(title, raw_publisher)
        publisher = classify.publisher_label(raw_publisher)
        if _SEC_REPOST_RE.search(title):
            # SEC 원문이 이미 커버하는 재게시물 (위 _SEC_REPOST_RE 주석 참고)
            print(f"[news] SEC 재게시 제외: {publisher} — {title[:50]}")
            continue
        guid = item.findtext("guid") or link or title
        ext = hashlib.sha1(guid.encode("utf-8")).hexdigest()[:12]
        docs.append(RawDoc(
            ext_id=ext,
            source=w.name,
            kind=KIND_NEWS,
            published_on=published,
            title=title,
            publisher=publisher,
            url=link,
            body=_body_of(item.findtext("description") or "", title, publisher),
            tags=list(w.tags),
            # <source url> 은 매체 홈페이지다. 기사 URL 해석에 실패했을 때 출처 도메인으로 쓴다.
            meta={"outlet_url": (source_el.get("url") if source_el is not None else "") or ""},
        ))
        if len(docs) >= per_query:
            break
    return docs


def crawl(since_days: int, per_query: int = 5) -> List[RawDoc]:
    if NEWS_ROBOTS_STRICT:
        # Google News 진입 경로가 robots 금지라 소스 전체를 건너뛴다(모듈 docstring 참조).
        print("[news] OI_NEWS_ROBOTS_STRICT=1 — Google News 경로 skip, 0건")
        return []
    since = date.today() - timedelta(days=since_days)
    docs: List[RawDoc] = []
    for w in news_targets():
        try:
            got = _crawl_query(w, since, per_query)
            docs.extend(got)
            if not got:
                # RSS 는 반환하나 기사가 since 보다 오래된 경우가 많습니다(니치 검색어).
                # 계속 0건이면 news_query 를 다시 설계하세요.
                print(f"[news] '{w.news_query}' 0건")
        except Exception as e:
            print(f"[news] '{w.news_query}' 조회 실패: {e}")
        polite(NEWS_SLEEP)
    print(f"[news] {len(docs)}건 수집")
    return docs


# ══════════════════════════════════════════════════════════════════════
# 본문 확보
# ══════════════════════════════════════════════════════════════════════
# 뉴스는 DART/SEC 와 달리 API 한도도 IP 차단도 없고(공개 웹), 수집량이 가장 많으며,
# 본문이 없으면 요약이 제목 복사로 떨어지는 유일한 소스다.
# 그래서 crawler 가 주는 per_source 상한을 이 배수만큼 늘려 받는다.
#
# 뉴스의 제약은 한도가 아니라 **시간**이다. 실측(2026-08-07) 건당 1.9초:
#   Google News 셸 대기 1.0 + 링크 해석 0.9(셸 + 내부 RPC) + robots·호스트 간격 0.1 + 기사 0.1
# 목록이 43건이었으므로 전량 시도는 약 82초. DART(6.6초)·SEC(6.3초)와 자릿수가 다르다.
# 그래도 전량을 덮는 쪽을 택한 이유 — 확보 성공률이 34/43(79%)이라 뒤쪽 꼬리에도 원문이 있고,
# body_priority 가 애그리게이터를 뒤로 미는 탓에 상한이 좁으면 **꼬리만 잘려** 나갔다
# (프로덕션 '제목만' 뉴스 28건 중 11건이 정확히 그 꼬리였다).
# 기본값 --with-docs 5 × 9 = 45 ≥ 목록 43건.
BODY_FACTOR = 9

# ── Google News 리다이렉트 해석 ────────────────────────────────────────
# RSS <link> 는 https://news.google.com/rss/articles/CBMi...  형태의 **불투명 토큰**이다.
# 실험으로 확인한 것(스크래치 probe_decode/probe_follow/probe_batch):
#   ① 토큰을 base64 로 풀면 protobuf 가 나오지만 예전과 달리 URL 이 들어있지 않다
#      (신형 'AU_yqL…' 토큰. 구형 디코딩 트릭은 더 이상 통하지 않는다).
#   ② 그 링크를 GET 하면 302 → 200 이지만 목적지가 Google 자신이고, 본문은 591KB 짜리
#      JS 셸이라 HTML 안에 기사 URL 이 없다.
#   ③ 통하는 방법: 그 셸 안에 있는 data-n-a-sg(서명) / data-n-a-ts(발급시각) 을 꺼내
#      Google 내부 RPC(batchexecute, rpcid=Fbv4je)에 넘기면 원본 URL 이 평문으로 온다.
#      실측 응답: ["garturlres","https://www.yna.co.kr/view/AKR20260722035100003",1,…]
# 건당 2요청(셸 1.4초 + RPC 0.3초)이 든다. 서명에 유효기간이 있어 미리 캐시할 수 없다.
GNEWS_HOST = "news.google.com"
BATCH_URL = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
_SIG_RE = re.compile(r'data-n-a-sg="([^"]+)"')
_TS_RE = re.compile(r'data-n-a-ts="(\d+)"')
_ART_ID_RE = re.compile(r"/(?:rss/)?articles/([^?/#]+)")
# 셸 페이지는 591KB 다. 서명이 문서 끝(99.7% 지점)에 있어 Range 로 줄일 수 없고
# (실측: 서버가 Range 를 무시하고 200 전체를 보낸다) gzip 에 기대는 수밖에 없다.
_SHELL_TIMEOUT = 20

# ── 예의 ────────────────────────────────────────────────────────────────
# 같은 매체를 연타하지 않는다. 호스트별 마지막 요청 시각을 기억해 간격을 벌린다.
HOST_SLEEP = 2.0
ARTICLE_TIMEOUT = 15
# 이보다 짧으면 본문 추출에 실패한 것으로 본다(동의 배너·페이월·JS 셸).
BODY_MIN_CHARS = 300
# 프롬프트 예산이 4,000자라 그 이상은 의미가 없다. 넉넉히 남기고 자른다.
BODY_MAX_CHARS = 20_000

_LAST_HIT: Dict[str, float] = {}
_ROBOTS: Dict[str, Optional[RobotFileParser]] = {}


def _headers() -> dict:
    return {
        "User-Agent": NEWS_USER_AGENT,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Encoding": "gzip, deflate",
    }


def _host_polite(host: str) -> None:
    """같은 호스트 연타 방지 — 직전 요청으로부터 HOST_SLEEP 초를 채운다."""
    wait = HOST_SLEEP - (time.monotonic() - _LAST_HIT.get(host, 0.0))
    if wait > 0:
        polite(wait)
    _LAST_HIT[host] = time.monotonic()


def _robots_allows(url: str) -> bool:
    """robots.txt 허용 여부. 못 읽으면 허용으로 본다(표준 관행).

    urllib 의 RobotFileParser.read() 는 타임아웃이 없어 느린 서버에서 프로세스를 잡아둔다.
    그래서 httpx 로 받아 parse() 에 먹인다.
    """
    parts = urlsplit(url)
    host = parts.netloc
    if host not in _ROBOTS:
        rp: Optional[RobotFileParser] = None
        try:
            r = httpx.get(f"{parts.scheme}://{host}/robots.txt",
                          headers=_headers(), timeout=8, follow_redirects=True)
            if r.status_code == 200 and len(r.content) < 500_000:
                rp = RobotFileParser()
                rp.parse(r.text.splitlines())
        except Exception:
            rp = None            # 없거나 못 읽으면 제한 없음으로 간주
        _ROBOTS[host] = rp
    rp = _ROBOTS[host]
    if rp is None:
        return True
    try:
        return rp.can_fetch(NEWS_USER_AGENT, url)
    except Exception:
        return True


def resolve_google_link(url: str, client: httpx.Client) -> str:
    """news.google.com 리다이렉트 링크 → 매체의 실제 기사 URL. 실패하면 ''.

    Google News 링크가 아니면 그대로 돌려준다.
    """
    parts = urlsplit(url)
    if parts.netloc != GNEWS_HOST:
        return url
    m = _ART_ID_RE.search(parts.path)
    if not m:
        return ""
    article_id = m.group(1)

    shell = client.get(url, headers=_headers(), timeout=_SHELL_TIMEOUT, follow_redirects=True)
    shell.raise_for_status()
    sig, ts = _SIG_RE.search(shell.text), _TS_RE.search(shell.text)
    if not sig or not ts:
        # 셸 구조가 바뀌면 여기가 먼저 깨진다. 조용히 실패하되 원인을 알 수 있게 남긴다.
        raise ValueError("Google News 셸에서 서명(data-n-a-sg)을 찾지 못했습니다")

    # batchexecute 의 f.req 는 'JSON 문자열을 담은 JSON' 이라 이중 직렬화가 필요하다.
    payload = [
        "garturlreq",
        [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1,
          None, None, None, None, None, 0, 1],
         "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
        article_id, int(ts.group(1)), sig.group(1),
    ]
    f_req = json.dumps(
        [[["Fbv4je", json.dumps(payload, separators=(",", ":")), None, "generic"]]],
        separators=(",", ":"),
    )
    r = client.post(
        BATCH_URL,
        data={"f.req": f_req},
        headers={**_headers(),
                 "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                 "Referer": f"https://{GNEWS_HOST}/"},
        timeout=25,
    )
    r.raise_for_status()
    return _parse_batch(r.text)


def _parse_batch(text: str) -> str:
    """batchexecute 응답에서 원본 URL 을 꺼낸다. 응답은 `)]}'` 접두어로 시작한다."""
    start = text.find("[")
    if start == -1:
        return ""
    for row in json.loads(text[start:]):
        if not (isinstance(row, list) and len(row) > 2 and row[0] == "wrb.fr"):
            continue
        inner = json.loads(row[2] or "[]")
        # ["garturlres", "<url>", 1, "<amp url>"]
        if len(inner) > 1 and isinstance(inner[1], str) and inner[1].startswith("http"):
            return inner[1]
    return ""


# ── 본문 추출 ───────────────────────────────────────────────────────────
# 외부 라이브러리 없이 표준 라이브러리만 씁니다(신규 의존성 없음).
_NOISE_RE = re.compile(
    r"<(script|style|nav|footer|header|aside|form|noscript|iframe|figure|svg|select|button|template)"
    r"\b[^>]*>.*?</\1\s*>",
    re.S | re.I,
)
_VOID_NOISE_RE = re.compile(r"<(script|style|link|meta)\b[^>]*/?>", re.I)
# 블록 경계를 개행으로 바꿔야 문단 단위로 길이를 잴 수 있다.
_BLOCK_RE = re.compile(
    r"(?:</(?:p|div|section|article|li|ul|ol|h[1-6]|tr|td|th|blockquote|pre)\s*>|<br\s*/?>)",
    re.I,
)
_ANY_TAG_RE = re.compile(r"<[^>]+>")
_ARTICLE_RE = re.compile(r"<article\b[^>]*>(.*?)</article\s*>", re.S | re.I)
_META_CHARSET_RE = re.compile(rb"""charset=["']?([\w\-]+)""", re.I)
_SPACES_RE = re.compile(r"[ \t\xa0​]+")
# 이 길이를 넘는 줄만 '문단' 으로 본다. 메뉴·저작권 표시·기자 이메일은 대개 이보다 짧다.
_PROSE_MIN = 40
# 문단 사이에 끼어드는 짧은 줄(사진 설명·소제목)을 몇 줄까지 참을지.
_GAP_TOLERANCE = 2
# 제목 어휘가 이 비율 이상 본문에 나오면 '같은 기사' 로 본다.
# 저장해 둔 실측 28건으로 0.20 / 0.25 / 0.35 를 비교했으나 결과가 동일했다(둔감한 구간).
# 가운데 값을 쓴다.
#
# ⚠ 이 문턱을 **낮추지 마라.** 실측 41건으로 0.0 까지 내려 봤더니 회수되는 건 한 건뿐이고
#   한국경제는 결제 안내문 1,015자를, 중부일보는 폭염 기사 300자를, 뉴시스는 축구협회 기사
#   194자를 물어왔다. 고쳐야 하는 것은 문턱이 아니라 지표였다(_title_overlap 참고).
_RELEVANCE_MIN = 0.25
_TOKEN_RE = re.compile(r"[0-9A-Za-z가-힣]{2,}")
# 어느 기사에나 나와서 관련성을 재는 데 쓸모가 없는 토큰
_TOKEN_STOP = {"기자", "뉴스", "news", "com", "www", "the", "and", "for"}
_TITLE_TOKENS_MAX = 14
# 한국어 토큰을 어간으로 자를 길이 (_title_overlap 참고)
_STEM_CHARS = 2

# ── 산문이 아닌 후보 ────────────────────────────────────────────────────
# 애그리게이터 페이지에는 사람이 읽는 문단보다 **긴** 비산문 블록이 실려 있어
# '가장 긴 관련 덩어리' 규칙이 그쪽을 물어온다. 두 종류를 실측으로 확인했다.
#
# ① 기계판독 덤프 — SEC XBRL 인라인 태그가 텍스트로 눕혀진 것.
#    실측: Stock Titan 'Cheniere 10-Q' 추출 20,000자가 통째로
#    "0000003570 false --12-31 2026 Q2 http://fasb.org/us-gaap/2025#Revenues …" 였다.
#    BODY_MIN_CHARS 를 가뿐히 넘겨 LLM 프롬프트를 먹지만 사람이 읽을 문장이 하나도 없다.
# ② 면책조항 — safe harbor / forward-looking statements 문단.
#    실측: Valero 보도자료 재게시 2,795자가 전부 면책 문구였다.
#
# 매체명으로 거르지 않는 이유: 같은 Stock Titan 이라도 배당 공시 본문은 멀쩡했다.
# 판정은 **텍스트 자체의 성질**로 한다.
_MACHINE_MARKERS = ("us-gaap", "fasb.org", "xbrl", "iso4217", "dei:", "srt/20")
_BOILERPLATE_MARKERS = (
    "forward-looking statement", "safe harbor", "securities litigation reform act",
    "undue reliance", "no obligation to update", "risk factors",
)
# 밀도(1,000자당 마커 수)로 판정한다. **횟수만 세면 안 된다** — 실적 컨퍼런스콜 전사는
# 60,927자 안에 면책 문구를 3회 언급하지만(밀도 0.05) 그건 버리면 안 되는 자료다.
# 실측 분리: 면책 문단 1.71~4.03 /1k · 전사 0.05 /1k · XBRL 덤프 8.85~8.91 /1k · 정상 본문 0.00.
_NONPROSE_DENSITY = 1.0
_MACHINE_MIN_HITS = 3
_BOILERPLATE_MIN_KINDS = 2


def decode_html(content: bytes, content_type: str = "") -> str:
    """바이트 → 문자열. 국내 매체는 아직 cp949 가 남아 있어 순차 폴백한다."""
    encodings: List[str] = []
    m = re.search(r"charset=([\w\-]+)", content_type or "", re.I)
    if m:
        encodings.append(m.group(1))
    m2 = _META_CHARSET_RE.search(content[:4096])
    if m2:
        encodings.append(m2.group(1).decode("ascii", "ignore"))
    encodings += ["utf-8", "cp949"]
    for enc in encodings:
        try:
            return content.decode(enc)
        except (LookupError, UnicodeDecodeError):
            continue
    return content.decode("utf-8", errors="ignore")


def _prose_groups(fragment: str) -> List[str]:
    """HTML 조각 → '연속 문단 덩어리' 목록.

    블록 경계를 개행으로 바꿔 줄 단위로 세운 뒤, 40자 넘는 줄이 이어지는 구간을 묶는다.
    메뉴·저작권 표시·기자 이메일·관련기사 제목은 대개 40자를 넘지 못해 덩어리를 끊는다.

    가장 긴 덩어리 하나만 돌려주면 안 된다 — 같은 페이지에 본문보다 **긴** 다른 기사가
    실려 있을 때 올바른 덩어리가 후보에서 아예 사라진다. 판정은 호출 측에서 한다.
    """
    body = _BLOCK_RE.sub("\n", fragment)
    body = _ANY_TAG_RE.sub(" ", body)
    body = html.unescape(body)

    groups: List[str] = []
    current: List[str] = []
    gap = 0
    for line in body.split("\n"):
        line = _SPACES_RE.sub(" ", line).strip()
        if len(line) >= _PROSE_MIN:
            current.append(line)
            gap = 0
        elif current:
            gap += 1
            if gap > _GAP_TOLERANCE:
                groups.append("\n".join(current))
                current, gap = [], 0
    if current:
        groups.append("\n".join(current))
    return groups


def _title_overlap(text: str, title: str) -> float:
    """본문이 제목의 어휘를 얼마나 담고 있는지(0~1). 제목이 없으면 1.0(판정 보류).

    한국어 토큰은 **어간 2글자 접두**로도 인정한다. 한국어는 조사·접미가 붙어 굴절하므로
    완전일치(`t in text`)만 보면 같은 기사인데도 겹침이 0 이 되는 일이 생긴다.
    실측 회귀 — 헤럴드경제 «"이날이 올 줄 알았다" 배터리주 다시 뛰나…» 기사:
      본문은 "국내 배터리 3사의 주가가 …" 라고 쓴다. 제목의 '배터리주'·'호재'·'만발' 이
      본문 표현과 정확히 일치하지 않아 겹침 0.00 → 1,682자 본문이 통째로 버려졌다.
      어간 2글자를 인정하면 0.44 가 되어 회수된다.

    영문 토큰에는 접두 일치를 쓰지 않는다. 영어는 이런 식으로 굴절하지 않는 데다
    두 글자 접두("Ch", "re")는 아무 문서에나 걸려 잡음만 키운다
    (실측: Fortune 오답 후보의 겹침이 0.07 → 0.14 로 두 배가 됐다).
    한국어에만 적용하면 실측 41건 중 겹침 판정이 달라지는 영문 기사가 하나도 없다.
    """
    tokens = [t for t in _TOKEN_RE.findall(title or "")
              if t.lower() not in _TOKEN_STOP][:_TITLE_TOKENS_MAX]
    if not tokens:
        return 1.0
    hits = 0
    for t in tokens:
        if t in text or (_HANGUL_RE.search(t) and t[:_STEM_CHARS] in text):
            hits += 1
    return hits / len(tokens)


def _is_nonprose(text: str) -> bool:
    """사람이 읽을 문장이 아닌 후보인지 (기계판독 덤프 · 면책조항). 상수 주석 참고."""
    n = len(text)
    if n < BODY_MIN_CHARS:
        return False        # 짧은 조각은 어차피 뒤에서 걸러진다. 굳이 판정하지 않는다.
    low = text.lower()

    machine = sum(low.count(m) for m in _MACHINE_MARKERS)
    if machine >= _MACHINE_MIN_HITS and machine / n * 1000 >= _NONPROSE_DENSITY:
        return True

    kinds = sum(1 for m in _BOILERPLATE_MARKERS if m in low)
    hits = sum(low.count(m) for m in _BOILERPLATE_MARKERS)
    return kinds >= _BOILERPLATE_MIN_KINDS and hits / n * 1000 >= _NONPROSE_DENSITY


def extract_text(raw_html: str, title: str = "") -> str:
    """기사 HTML → 본문 텍스트.

    <script>/<style>/<nav>/<footer> 등을 걷어낸 뒤, 문서 전체와 각 <article> 을 후보로 두고
    **제목 어휘가 겹치는 후보 중 가장 긴 것**을 고른다.
    매체별 셀렉터를 두지 않는 이유는 감시 대상이 35개 매체로 흩어져 있어
    유지보수가 불가능하기 때문이다(실측: 44건에 매체 35종).

    후보는 '연속 문단 덩어리' 전부다(문서 전체 기준 + <article> 안 기준).
    '가장 긴 덩어리' 만으로 고르면 안 되는 이유 — 국내 매체 페이지에는 본문보다 긴
    **다른 기사** 블록이 흔히 같이 실려 있다. 실측으로 두 건이 통째로 엉뚱한 본문을 물어왔다:
      · newspim(LG에너지솔루션 리포트 기사) → '한반도 평화공존 구상' 1,312자
      · fortune(Dow 신임 CEO 기사)        → 'Watch Fortune Daily' 홍보문 1,019자
    이런 본문이 LLM 에 들어가면 요약이 조용히 다른 기사 이야기가 된다 — 빈 요약보다 나쁘다.
    제목 어휘 겹침으로 거르면 두 건 모두 올바른 본문(377자 / 511자)을 집어낸다.

    <article> 태그를 무조건 믿지 않는 이유도 같다 — 관련기사 카드까지 <article> 로 감싸는
    CMS 가 흔하다(실측: newsis 한 페이지에 <article> 97개).

    겹치는 후보가 하나도 없으면 가장 긴 것으로 되돌린다. 제목이 본문 어휘를 거의 쓰지 않는
    기사가 실제로 있어서(실측 2건: 운임 시황 기사) 여기서 버리면 멀쩡한 본문을 잃는다.

    관련성을 재기 **전에** 비산문 후보(XBRL 덤프·면책조항)를 뺀다. 그것들은 제목 어휘를
    그대로 담고 있어 관련성 판정을 통과하는 데다 본문보다 길어서 그냥 두면 이긴다
    (실측: Stock Titan 10-Q 재게시에서 XBRL 20,000자가 실제 실적 서술 4,934자를 눌렀다).
    전부 비산문이면 거르지 않는다 — 판정이 틀렸을 때 본문을 통째로 잃지 않기 위해서다.
    """
    body = _NOISE_RE.sub(" ", raw_html)
    body = _VOID_NOISE_RE.sub(" ", body)

    candidates = _prose_groups(body)
    # <article> 안에서 다시 나누면 문서 전체 기준으로는 하나로 붙어 버린 덩어리가 갈라진다.
    for art in _ARTICLE_RE.findall(body):
        candidates += _prose_groups(art)
    if not candidates:
        return ""
    candidates = [c for c in candidates if not _is_nonprose(c)] or candidates
    relevant = [c for c in candidates if _title_overlap(c, title) >= _RELEVANCE_MIN]
    return max(relevant or candidates, key=len)[:BODY_MAX_CHARS]


# ── 우선순위 ────────────────────────────────────────────────────────────
# 수치(숫자 + 단위/기호)가 있는 제목은 지표를 뽑을 수 있어 정제 가치가 크다.
_NUMERIC_RE = re.compile(
    r"\d[\d,.]*\s*(?:%|원|억|조|만|톤|t\b|배럴|달러|년|월|일|분기|billion|million|bn|percent|\$)",
    re.I,
)
# 애그리게이터·시세 봇. **뒤로 밀되 버리지는 않는다.**
#
# ⚠ 예전 주석은 "추출이 거의 실패한다" 고 적었는데 그건 사실이 아니었다.
#   실측(2026-08-07): Stock Titan 4/4 · TradingView 1/2 · Pluang 1/1 · BigGo 1/1 · Quiver 1/1 성공.
#   실제 문제는 추출 실패가 아니라 ① SEC 원문과의 중복(포함률 0.99~1.00)과
#   ② XBRL·면책조항 잡음이다. ①은 _SEC_REPOST_RE 가 수집 단계에서, ②는 _is_nonprose 가
#   추출 단계에서 처리한다.
# 그래서 여기 남은 역할은 '우선순위를 뒤로 미는 것' 뿐이다. 매체명으로 통째 배제하면 안 된다 —
# 실적 컨퍼런스콜 전사(The Globe and Mail 20,000자 = 임원 발언 원문, TradingView 8,180자)는
# SEC 공시에 없는 유일한 재료이고 O/I 사례 밀도가 가장 높다.
_LOW_YIELD_PUBLISHERS = (
    "stock titan", "tradingview", "quiver quantitative", "pluang", "biggo",
    "simply wall st", "marketscreener", "zacks", "msn",
)

# 본문을 **구조적으로** 받을 수 없다고 실측으로 확인된 곳. 요청 자체를 하지 않는다.
# 페이월·로그인·JS 렌더링을 우회하지 않는 것이 이 크롤러의 방침이므로, 여기 있는 건은
# '원문 미확보' 로 남기는 것이 정답이다. 시도해 봐야 건당 1.9초와 상대 서버 부하만 쓴다.
#
# 매체 고유 처리는 여기에만 둔다(추출 규칙에는 매체명을 넣지 않는다). 사유를 반드시 적을 것 —
# 사이트가 바뀌면 다시 열어 봐야 하고, 근거 없는 항목은 멀쩡한 매체를 영원히 잠근다.
_NO_BODY_PUBLISHERS = {
    # HTTP 403. robots.txt 가 아니라 요청 자체를 거부한다(2026-08-07 두 차례 크롤에서 4/4 실패).
    "investing.com": "봇 차단(403)",
    # Next.js CSR. 초기 HTML 395KB 에 문단 후보가 제목 하나뿐이고 __NEXT_DATA__ 로만 본문이 온다.
    # JSON-LD 에도 articleBody 가 없다(실측 0자). 렌더링 없이는 불가.
    "chosunbiz": "JS 렌더링(본문이 초기 HTML 에 없음)",
    "조선비즈": "JS 렌더링(본문이 초기 HTML 에 없음)",
    # 기사가 아니라 AI 종목분석 봇 출력. 텍스트가 면책조항 152자뿐이다.
    "주달": "기사가 아님(자동 생성 종목분석)",
    "judal": "기사가 아님(자동 생성 종목분석)",
}


def _no_body_reason(publisher: str) -> str:
    """이 매체가 구조적으로 본문을 못 주는 이유. 해당 없으면 ''."""
    low = (publisher or "").lower()
    for key, why in _NO_BODY_PUBLISHERS.items():
        if key in low:
            return why
    return ""


def body_priority(doc: RawDoc) -> int:
    """작을수록 먼저 본문을 받는다.

    상수를 돌려주면 crawler._pick 의 선별이 무의미해진다. 제목만 보고
    '본문을 받을 값어치' 를 매긴다 — 수치와 O/I 어휘가 있을수록 지표·사례가 나온다.
    """
    title = doc.title or ""
    has_number = bool(_NUMERIC_RE.search(title))
    has_signal = any(v > 0 for v in classify.theme_score(title).values())
    score = 2 - int(has_number) - int(has_signal)
    publisher = (doc.publisher or "").lower()
    if any(p in publisher for p in _LOW_YIELD_PUBLISHERS):
        score += 2      # SEC 원문과 겹치기 쉬운 곳은 뒤로 민다
    if _no_body_reason(publisher):
        score += 4      # 어차피 못 받는 곳은 맨 뒤로 (상한이 좁을 때 슬롯을 낭비하지 않게)
    return score


def fetch_body(doc: RawDoc) -> str:
    """매체 사이트에서 기사 본문을 받아온다. 실패하면 '' (조용히 건너뛴다).

    ⚠ 반환된 본문은 LLM 정제 입력 전용이다. DB 에 저장하지 않는다 —
      meta['body_restricted'] 를 세워 두면 llm.naive_summary 가 본문 절삭 폴백을 거부하고
      제목으로 되돌린다. 화면에 남는 것은 LLM 이 새로 쓴 요약뿐이다.
    """
    if not doc.url:
        doc.meta["body_reason"] = REASON_RESOLVE
        return ""

    # 구조적으로 못 받는 곳은 요청 전에 끝낸다 (_NO_BODY_PUBLISHERS 주석 참고).
    why = _no_body_reason(doc.publisher)
    if why:
        print(f"[news] 시도 생략({why}): {doc.publisher} — {doc.title[:40]}")
        doc.meta["body_reason"] = REASON_SKIP
        return ""

    with httpx.Client(follow_redirects=True) as client:
        _host_polite(GNEWS_HOST)
        try:
            article_url = resolve_google_link(doc.url, client)
        except Exception as e:
            print(f"[news] 링크 해석 실패 {doc.ext_id}: {type(e).__name__}: {str(e)[:80]}")
            doc.meta["body_reason"] = REASON_RESOLVE
            return ""
        if not article_url:
            print(f"[news] 링크 해석 실패 {doc.ext_id}: 원본 URL 없음")
            doc.meta["body_reason"] = REASON_RESOLVE
            return ""

        if not _robots_allows(article_url):
            print(f"[news] robots 금지 — 건너뜀: {urlsplit(article_url).netloc}")
            doc.meta["body_reason"] = REASON_ROBOTS
            return ""

        host = urlsplit(article_url).netloc
        _host_polite(host)
        try:
            r = client.get(article_url, headers=_headers(), timeout=ARTICLE_TIMEOUT)
            r.raise_for_status()
        except Exception as e:
            print(f"[news] 본문 요청 실패 {host}: {type(e).__name__}: {str(e)[:80]}")
            doc.meta["body_reason"] = REASON_REQUEST
            return ""

        ctype = r.headers.get("content-type", "")
        if "html" not in ctype.lower():
            print(f"[news] HTML 아님({ctype[:40]}) — 건너뜀: {host}")
            doc.meta["body_reason"] = REASON_EXTRACT
            return ""

        text = extract_text(decode_html(r.content, ctype), doc.title)
        if len(text) < BODY_MIN_CHARS:
            # 페이월·동의 배너·JS 렌더링 기사. 억지로 우회하지 않는다.
            print(f"[news] 본문 추출 실패({len(text)}자) — 건너뜀: {host}")
            doc.meta["body_reason"] = REASON_EXTRACT
            return ""

        # 해석에 성공했으면 화면 링크도 매체 원문으로 바꾼다(출처가 실제로 열려야 한다).
        doc.url = article_url
        doc.meta["resolved_url"] = article_url
        doc.meta["body_restricted"] = True
        return text
