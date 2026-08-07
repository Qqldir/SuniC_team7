"""원문 확보 흐름 회귀 테스트 — 소스별 상한 · 추출 규칙 · 미확보 사유 · 보존 가드.

네트워크 없이 돌아가는 것만 고정한다. 여기서 지키려는 것은 다섯이다.

1. 소스별 원문 확보 상한이 **하나의 숫자에 묶이지 않는다**.
   묶이면 가장 비싼 소스(뉴스)에 맞춰 공시가 통째로 잘린다 —
   실측으로 프로덕션 '제목만' 43건 중 15건(DART 8 · SEC 7)이 순전히 그 이유였다.
2. 이미 본문이 있는 문서가 상한 슬롯을 먹지 않는다(예전 fetch_bodies 의 구조적 결함).
3. 추출 규칙이 한국어 굴절 때문에 멀쩡한 본문을 버리지 않고,
   XBRL 덤프·면책조항 같은 비산문을 본문으로 착각하지 않는다.
4. 구조적으로 못 받는 곳은 **요청 자체를 하지 않는다**(페이월·CSR 우회 금지 방침).
5. 재크롤이 이미 정제된 요약을 파괴하지 않는다(ingest UPSERT 보존 가드).

    cd backend && .venv/bin/python -m pytest tests/ -q
"""
import sqlite3
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

from app.pipeline.farming import crawler, dart, ingest, news, sec  # noqa: E402
from app.pipeline.farming.base import (  # noqa: E402
    KIND_NEWS, KIND_PERIODIC, KIND_SEC, REASON_QUOTA, REASON_SKIP, RawDoc, source_of,
)


def _doc(kind, ext, source="롯데케미칼", title="제목", publisher="", body=""):
    return RawDoc(ext_id=ext, source=source, kind=kind, published_on="2026-08-01",
                  title=title, publisher=publisher, body=body)


# ── 소스별 상한 ─────────────────────────────────────────────────────────

def test_소스별_상한이_하나의_숫자에_묶이지_않는다():
    """DART·SEC 는 목록 전량을 덮을 만큼, 뉴스는 그보다 넓게 — 각 모듈의 BODY_FACTOR 가 결정한다."""
    # 실측 목록 크기(dart 14 · sec 12 · 뉴스 43)를 기본값 --with-docs 5 에서 덮어야 한다.
    assert 5 * dart.BODY_FACTOR >= 14
    assert 5 * sec.BODY_FACTOR >= 12
    assert 5 * news.BODY_FACTOR >= 43


def test_SEC_는_요청_간격을_줄여서_상한을_늘리지_않는다():
    """차단선은 '초당 10건' 이라 간격이 안전 마진이다. 건수는 늘려도 간격은 못 줄인다."""
    from app.pipeline.farming.base import SEC_SLEEP
    # 건당 요청 2회 + 그 사이 SEC_SLEEP → 실측 3.80 req/s. 0.1 아래로 내리면 차단선에 붙는다.
    assert SEC_SLEEP >= 0.1


class _FakeMod:
    """fetch_body 호출 순서를 기록하는 가짜 소스 모듈."""
    BODY_FACTOR = 1

    def __init__(self, factor=1):
        self.BODY_FACTOR = factor
        self.calls = []

    @staticmethod
    def body_priority(doc):
        return 0

    def fetch_body(self, doc):
        self.calls.append(doc.ext_id)
        return "본문 " * 100


def _with_fake(monkey_sources):
    original = dict(crawler.SOURCES)
    crawler.SOURCES.update(monkey_sources)
    return original


def test_이미_본문이_있는_문서는_상한_슬롯을_먹지_않는다():
    """예전 결함 회귀 — _pick 이 quota 개를 뽑은 뒤 루프에서 건너뛰면 슬롯만 낭비된다.

    본문이 있는 2건 + 없는 2건에 상한 2 를 주면, 본문 없는 2건이 **모두** 시도돼야 한다.
    """
    fake = _FakeMod(factor=1)
    original = _with_fake({"news": fake})
    try:
        docs = [
            _doc(KIND_NEWS, "a", body="이미 있음"),
            _doc(KIND_NEWS, "b", body="이미 있음"),
            _doc(KIND_NEWS, "c"),
            _doc(KIND_NEWS, "d"),
        ]
        stats = crawler.fetch_bodies(docs, per_source=2)
    finally:
        crawler.SOURCES.clear()
        crawler.SOURCES.update(original)

    assert sorted(fake.calls) == ["c", "d"], f"상한 슬롯이 낭비됐습니다: {fake.calls}"
    st = stats["news"]
    assert (st.prefilled, st.filled) == (2, 2)
    assert st.with_body == 4


def test_상한_밖으로_밀린_건은_한도밖으로_집계된다():
    """'한도밖' 은 --with-docs 를 올리면 그대로 회수되는 물량이라 다른 사유와 구분해야 한다."""
    fake = _FakeMod(factor=1)
    original = _with_fake({"news": fake})
    try:
        docs = [_doc(KIND_NEWS, str(i)) for i in range(5)]
        stats = crawler.fetch_bodies(docs, per_source=2)
    finally:
        crawler.SOURCES.clear()
        crawler.SOURCES.update(original)
    assert stats["news"].reasons[REASON_QUOTA] == 3


def test_목록만_받아도_사유가_한도밖으로_남는다():
    docs = [_doc(KIND_NEWS, "a"), _doc(KIND_SEC, "b")]
    stats = crawler.fetch_bodies(docs, per_source=0)
    assert stats["news"].reasons[REASON_QUOTA] == 1
    assert stats["sec"].reasons[REASON_QUOTA] == 1


def test_요약표에_소스와_미확보_사유가_모두_찍힌다():
    """성공만 찍히는 로그로는 무엇이 왜 빠졌는지 알 수 없다."""
    stats = {"dart": crawler.SourceStat(collected=14, filled=14),
             "news": crawler.SourceStat(collected=43, filled=36)}
    stats["news"].reasons[REASON_SKIP] = 3
    stats["news"].reasons[REASON_QUOTA] = 4
    out = crawler.format_report(stats)
    assert "dart" in out and "news" in out and "합계" in out
    assert REASON_SKIP in out and REASON_QUOTA in out
    assert "100%" in out          # dart 확보율


def test_소스_판별은_crawler_와_ingest_가_같은_기준을_쓴다():
    """요약표의 두 열(확보·정제)이 서로 맞으려면 같은 함수로 세야 한다."""
    assert source_of(_doc(KIND_NEWS, "x")) == "news"
    assert source_of(_doc(KIND_SEC, "x")) == "sec"
    assert source_of(_doc(KIND_PERIODIC, "x")) == "dart"


# ── 추출 규칙: 한국어 굴절 ───────────────────────────────────────────────

def test_한국어는_어간이_겹치면_같은_기사로_본다():
    """실측 회귀 — 헤럴드경제 «배터리주 다시 뛰나» 기사.

    본문은 '배터리 3사의 주가가' 라고 쓴다. 완전일치만 보면 겹침 0.00 이 되어
    1,682자 본문이 통째로 버려졌다.
    """
    title = "“이날이 올 줄 알았다” 배터리주 다시 뛰나…여기저기서 호재 만발 [투자360]"
    body = ("국내 배터리 3사의 주가가 본격적인 반등 흐름을 탈지 주목된다. "
            "전기차 시장 캐즘을 넘어 2분기 3사가 나란히 흑자 전환에 성공했고 "
            "여기저기서 호재가 이어지고 있다는 분석이다. ")
    assert news._title_overlap(body, title) >= news._RELEVANCE_MIN


def test_어간_인정이_무관한_기사를_통과시키지_않는다():
    """실측 회귀 — 중부일보·뉴시스 페이지에 같이 실린 다른 기사."""
    title = "산업용 전기료 지역별 차등 인하… 경기도 '고지서 부담' 초읽기"
    other = "올여름 기록적인 폭염으로 전력수급 경보가 발령되면서 예비력이 크게 낮아졌다. " * 4
    assert news._title_overlap(other, title) < news._RELEVANCE_MIN


def test_영문은_두글자_접두로_넓히지_않는다():
    """영어는 굴절하지 않는다. 두 글자 접두('Ch','re')는 아무 문서에나 걸려 잡음만 키운다."""
    title = "Cheniere Reports Second Quarter 2026 Results"
    unrelated = ("Chelsea chefs report changes across the restaurant sector this quarter. "
                 "Charts show research results are secondary to real revenue. ") * 3
    assert news._title_overlap(unrelated, title) < news._RELEVANCE_MIN


# ── 추출 규칙: 비산문 후보 ───────────────────────────────────────────────

_XBRL = ("0000003570 false --12-31 2026 Q2 "
         + "http://fasb.org/us-gaap/2025#Revenues " * 60)
_BOILER = ("This press release contains certain statements that may include "
           "“forward-looking statements.” Undue reliance should not be placed on these "
           "forward-looking statements, which speak only as of the date hereof. "
           "See the risk factors described in our filings. We assume no obligation to update "
           "any forward-looking statement. ") * 3


def test_XBRL_덤프는_본문으로_치지_않는다():
    """실측 회귀 — Stock Titan 10-Q 재게시에서 XBRL 20,000자가 실제 실적 서술을 눌렀다."""
    assert news._is_nonprose(_XBRL)


def test_면책조항_문단은_본문으로_치지_않는다():
    assert news._is_nonprose(_BOILER)


def test_실적_전사는_면책_문구를_언급해도_지켜진다():
    """버리면 안 되는 자료 — 컨퍼런스콜 전사는 SEC 공시에 없는 유일한 재료다.

    전사 60,927자 안에 면책 문구가 3회 나오지만 밀도는 0.05/1k 다(면책 문단은 1.7~4.0/1k).
    횟수로 판정하면 이 자료가 통째로 사라진다.
    """
    transcript = ("Operator: Good morning and welcome to the second quarter earnings call. "
                  "Our refining margin improved on lower operating expenses per barrel. ") * 200
    transcript += ("Please see our forward-looking statements and the risk factors in our "
                   "annual report. ")
    assert not news._is_nonprose(transcript)


# 실제 기사 페이지에서 블록 사이에 늘 끼는 짧은 줄. 이게 없으면 덩어리가 하나로 붙는다.
_SEP = "<p>2026.08.06</p><p>공유</p><p>댓글</p>"


def test_비산문_후보를_제치고_실제_서술을_고른다():
    real = ("Net income attributable to Cheniere increased by $1.4 billion compared with the "
            "prior year, driven by higher LNG volumes and lower operating costs per unit. ") * 6
    page = (f"<html><body><div><p>{_XBRL}</p></div>{_SEP}<div><p>{_BOILER}</p></div>{_SEP}"
            f"<div><p>{real}</p></div>{_SEP}</body></html>")
    got = news.extract_text(page, "Cheniere Q2 profit jumps as LNG revenues grow")
    assert "Net income attributable to Cheniere" in got
    assert "fasb.org" not in got and "forward-looking" not in got


def test_전부_비산문이면_거르지_않는다():
    """판정이 틀렸을 때 본문을 통째로 잃지 않기 위한 안전판."""
    page = f"<html><body><div><p>{_BOILER}</p></div>{_SEP}</body></html>"
    assert news.extract_text(page, "Valero Returns $2.6B to Stockholders") != ""


# ── 수집 단계: SEC 재게시 ────────────────────────────────────────────────

def test_SEC_재게시_제목은_수집에서_걸러진다():
    """SEC 원문과 어휘 포함률 0.99~1.00 인 중복이다. SEC 소스가 이미 100% 확보한다."""
    assert news._SEC_REPOST_RE.search("Form 8K Cheniere Energy Partners For: 6 August By Investing.com")
    assert news._SEC_REPOST_RE.search("Form 10-Q Valero Energy For: 30 June")


def test_실적_전사_제목은_걸러지지_않는다():
    """같은 매체라도 SEC 에 없는 자료는 지켜야 한다 — 매체명이 아니라 제목으로 판정하는 이유."""
    for title in ("Valero Energy (VLO) Q2 2026 Earnings Call Transcript",
                  "Earnings call transcript: Valero Energy posts huge Q2 2026 beat",
                  "Cheniere Reports Second Quarter 2026 Results"):
        assert not news._SEC_REPOST_RE.search(title), title


# ── 구조적 불가 매체 ────────────────────────────────────────────────────

def test_구조적_불가_매체는_요청_없이_사유를_남긴다():
    """페이월·CSR·봇차단을 우회하지 않는다. 시도해 봐야 상대 서버 부하만 쓴다."""
    for publisher in ("Investing.com UK", "Chosunbiz", "주달"):
        doc = _doc(KIND_NEWS, "x", publisher=publisher)
        doc.url = "https://news.google.com/rss/articles/CBMiTEST"
        assert news.fetch_body(doc) == ""
        assert doc.meta["body_reason"] == REASON_SKIP, publisher


def test_구조적_불가_매체는_우선순위_맨_뒤로_밀린다():
    """상한이 좁을 때 못 받을 건이 슬롯을 먹지 않게."""
    title = "삼성SDI 가동률 3.2% 회복"
    normal = news.body_priority(_doc(KIND_NEWS, "x", title=title, publisher="연합뉴스"))
    aggregator = news.body_priority(_doc(KIND_NEWS, "x", title=title, publisher="Stock Titan"))
    blocked = news.body_priority(_doc(KIND_NEWS, "x", title=title, publisher="Investing.com UK"))
    assert normal < aggregator < blocked


def test_애그리게이터를_매체명으로_통째_배제하지_않는다():
    """실측 정정 — Stock Titan 4/4 · TradingView 1/2 로 추출은 성공한다.

    문제는 추출 실패가 아니라 SEC 중복·XBRL 잡음이고, 그건 다른 두 규칙이 처리한다.
    여기서 통째로 막으면 실적 컨퍼런스콜 전사를 잃는다.
    """
    for name in ("Stock Titan", "TradingView", "The Globe and Mail", "BigGo Finance"):
        assert news._no_body_reason(name) == "", name


# ── 재크롤 보존 가드 ────────────────────────────────────────────────────

_MINI_SCHEMA = """
CREATE TABLE feed_item (
    id TEXT PRIMARY KEY, published_on TEXT NOT NULL, kind TEXT NOT NULL,
    source TEXT NOT NULL, title TEXT NOT NULL, summary TEXT NOT NULL, url TEXT,
    farmed_at TEXT, kind_label TEXT, theme TEXT, biz_hint TEXT,
    is_new INTEGER NOT NULL DEFAULT 0, levers TEXT, importance INTEGER, reason TEXT,
    case_worthy INTEGER NOT NULL DEFAULT 0, enriched INTEGER NOT NULL DEFAULT 0,
    source_label TEXT, title_label TEXT, publisher TEXT,
    metrics TEXT NOT NULL DEFAULT '[]', evidence_grade TEXT NOT NULL DEFAULT '제목만'
);
"""


def _upsert(conn, *, summary, grade, enriched, theme="간접비·원가구조"):
    conn.execute(ingest._UPSERT, (
        "news-x", "2026-08-01", "news", "롯데케미칼", "제목", summary, "u", "t",
        "뉴스", theme, "에너지·화학", "연합뉴스", None, None, "[]", grade,
        None, 50, None, 0, int(enriched),
    ))


def _row(conn):
    return conn.execute("SELECT summary, evidence_grade, enriched FROM feed_item").fetchone()


def test_재크롤이_정제본을_파괴하지_않는다():
    """--with-docs 없이 돌린 재크롤 한 번에 기존 LLM 요약이 날아가면 안 된다.

    등급도 같이 지켜야 한다 — 요약만 보존하고 등급을 덮으면 '제목만' 등급 행에
    원문에서 뽑은 요약이 남는 모순이 생긴다.
    """
    conn = sqlite3.connect(":memory:")
    conn.executescript(_MINI_SCHEMA)
    _upsert(conn, summary="정제된 요약임.", grade="원문 확보", enriched=True)
    _upsert(conn, summary="", grade="제목만", enriched=False)   # 원문 미확보 재크롤
    assert _row(conn) == ("정제된 요약임.", "원문 확보", 1)


def test_첫_적재는_정제되지_않아도_기록된다():
    """보존 가드가 첫 적재를 막으면 안 된다(feed_item.enriched=0 인 상태)."""
    conn = sqlite3.connect(":memory:")
    conn.executescript(_MINI_SCHEMA)
    _upsert(conn, summary="", grade="제목만", enriched=False)
    _upsert(conn, summary="이번엔 본문을 받았다.", grade="요약문", enriched=False)
    assert _row(conn) == ("이번엔 본문을 받았다.", "요약문", 0)


def test_새로_정제되면_교체된다():
    conn = sqlite3.connect(":memory:")
    conn.executescript(_MINI_SCHEMA)
    _upsert(conn, summary="옛 요약.", grade="요약문", enriched=True)
    _upsert(conn, summary="새 정제 요약.", grade="원문 확보", enriched=True)
    assert _row(conn) == ("새 정제 요약.", "원문 확보", 1)
