"""뉴스 원문 확보 · 매체명 정규화 회귀 테스트.

네트워크 없이 돌아가는 순수 함수만 고정한다 —
Google News 링크 해석과 실제 기사 요청은 외부 서비스에 의존하므로 여기서 다루지 않는다.

여기서 지키려는 것은 넷이다.

1. 본문 추출이 **엉뚱한 기사 블록**을 물어오지 않는다.
   실측으로 두 건이 그랬다(newspim → '한반도 평화공존', fortune → 'Watch Fortune Daily').
   조용히 다른 기사 요약이 만들어지는 쪽이 요약이 없는 것보다 나쁘다.
2. body_priority 가 상수가 아니다. 상수면 crawler._pick 의 선별이 무의미해진다.
3. 매체명 자리에 도메인이 그대로 박히지 않는다. 다만 모르는 도메인에서 이름을 지어내지도 않는다.
4. 저작권 방침 — 뉴스 본문은 요약 자리로 새지 않는다(llm.naive_summary 가 제목으로 되돌린다).

    cd backend && .venv/bin/python -m pytest tests/ -q
"""
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

from app.pipeline.farming import classify, llm, news  # noqa: E402
from app.pipeline.farming.base import KIND_NEWS, RawDoc  # noqa: E402

_PARA = (
    "여천NCC 여수 2공장과 3공장의 가동이 중단되면서 연간 생산량이 228만톤에서 90만톤 수준으로 "
    "줄어들게 된다고 산업통상부가 22일 밝혔다. "
)
# 실제 기사 페이지에서 블록과 블록 사이에 늘 끼는 짧은 줄(날짜·바이라인·소제목).
# 추출기는 이 짧은 줄들을 경계로 덩어리를 나눈다 — 없으면 붙어 있는 다른 기사와 한 덩어리가 된다.
_SEP = "<p>입력 2026.08.06</p><p>홍길동 기자</p><p>공유하기</p><p>댓글 0</p>"


def _page(body_paras, extra=""):
    paras = "".join(f"<p>{p}</p>" for p in body_paras)
    return (f"<html><head><title>t</title></head><body>{extra}{_SEP}"
            f"<div>{paras}</div>{_SEP}</body></html>")


# ── 본문 추출 ───────────────────────────────────────────────────────────

def test_노이즈_태그는_본문에_섞이지_않는다():
    noise = ("<script>var x='" + "가" * 500 + "';</script>"
             "<style>.a{color:red}</style>"
             "<nav>" + "메뉴" * 200 + "</nav>"
             "<footer>" + "저작권" * 200 + "</footer>")
    got = news.extract_text(_page([_PARA * 3], extra=noise), "여천NCC 가동 중단")
    assert "여천NCC" in got
    assert "var x" not in got and "메뉴메뉴" not in got and "저작권저작권" not in got


def test_제목과_무관한_더_긴_블록을_고르지_않는다():
    """실측 회귀 — 본문보다 긴 '다른 기사' 가 같은 페이지에 실려 있는 경우."""
    other = "정부는 한반도 평화공존 발전 구상을 설명하면서 3대 기본 방향을 제시했다고 밝혔다. " * 6
    html = _page([_PARA * 2], extra=f"<div><p>{other}</p></div>")
    got = news.extract_text(html, "여천NCC 여수 2·3공장 가동 중단")
    assert "여천NCC" in got
    assert "한반도" not in got


def test_관련기사_article_카드보다_실제_본문을_고른다():
    """CMS 가 관련기사까지 <article> 로 감싸는 경우(실측: 한 페이지에 97개)."""
    cards = "".join(
        f"<article><p>{'다른 기사 제목이 길게 늘어선 관련기사 카드 목록입니다 ' * 2}</p>"
        f"<p>2026.08.0{i}</p><p>더보기</p><p>공유</p></article>"
        for i in range(8)
    )
    got = news.extract_text(_page([_PARA * 2], extra=cards), "여천NCC 여수 공장 가동 중단")
    assert "여천NCC" in got
    assert "관련기사 카드" not in got


def test_본문이_없으면_빈_문자열():
    assert news.extract_text("<html><body><nav>메뉴</nav></body></html>", "제목") == ""


def test_추출_결과는_상한으로_잘린다():
    got = news.extract_text(_page([_PARA * 400]), "여천NCC")
    assert len(got) == news.BODY_MAX_CHARS


def test_cp949_문서를_읽는다():
    raw = "<html><head><meta charset='euc-kr'></head><body><p>가동률 개선</p></body></html>"
    assert "가동률" in news.decode_html(raw.encode("cp949"), "text/html")


# ── 우선순위 ────────────────────────────────────────────────────────────

def _news_doc(title, publisher=""):
    return RawDoc(ext_id="x", source="s", kind=KIND_NEWS, published_on="2026-08-01",
                  title=title, publisher=publisher)


def test_body_priority_는_상수가_아니다():
    rich = _news_doc("에쓰오일 정기보수 공기 12일 단축으로 원가 3.2% 절감")
    plain = _news_doc("신임 대표이사 선임 안내")
    assert news.body_priority(rich) < news.body_priority(plain)


def test_애그리게이터는_뒤로_밀린다():
    title = "삼성SDI 가동률 3.2% 회복"
    assert news.body_priority(_news_doc(title, "Stock Titan")) > news.body_priority(_news_doc(title, "연합뉴스"))


# ── 매체명 정규화 ───────────────────────────────────────────────────────

def test_아는_도메인은_매체명으로_바뀐다():
    assert classify.publisher_label("v.daum.net") == "다음뉴스"
    assert classify.publisher_label("www.ebn.co.kr") == "EBN"


def test_모르는_도메인은_이름을_지어내지_않는다():
    assert classify.publisher_label("nosuch-outlet.co.kr") == "nosuch-outlet.co.kr"


def test_이미_매체명이면_건드리지_않는다():
    for name in ("연합뉴스", "Investing.com UK", "SEC EDGAR", ""):
        assert classify.publisher_label(name) == name


def test_정규화된_매체명이_화면_라벨로_이어진다():
    assert classify.news_kind(classify.publisher_label("v.daum.net")) == ("뉴스 (다음뉴스)", classify.KIND_NEWS_AXIS)


# ── 저작권 방침 ─────────────────────────────────────────────────────────

def test_크롤한_뉴스_본문은_요약_자리로_새지_않는다():
    """저작물인 뉴스 본문이 DB 요약 자리로 새면 안 된다.

    예전에는 제목으로 되돌렸는데, 그러면 화면에 같은 문장이 제목·요약으로 두 번
    찍히고 '원문 미확보' 라는 사실이 가려졌다(실측 45/56건). 지금은 빈 값이고,
    화면이 그 자리에 '원문 미확보' 를 표시한다.
    """
    doc = _news_doc("여천NCC 여수 공장 가동 중단")
    doc.body = _PARA * 3
    doc.meta["body_restricted"] = True
    out = llm.naive_summary(doc)
    assert _PARA[:30] not in out, "뉴스 본문이 요약으로 샜습니다"
    assert out == "", f"제목 복사가 남아 있습니다: {out!r}"


def test_본문이_없으면_요약을_지어내지_않는다():
    """제목만 수집된 자료는 요약이 비어야 한다 — 제목을 복사하지 않는다."""
    assert llm.naive_summary(_news_doc("산업용 전기요금 개편")) == ""


def test_본문이_제목_반복이면_요약으로_치지_않는다():
    """Google News RSS 의 description 은 제목 재출력이라 요약 가치가 없다."""
    doc = _news_doc("에쓰오일, 2분기 영업익 9650억")
    doc.body = "에쓰오일, 2분기 영업익 9650억"
    assert llm.naive_summary(doc) == ""


def test_공시_본문은_기존대로_폴백_요약에_쓰인다():
    doc = _news_doc("분기보고서")
    doc.body = "매출원가 구조 개선 " * 20
    assert doc.title not in llm.naive_summary(doc)


# ── 원문 발췌 ───────────────────────────────────────────────────────────

def test_예산_안에_드는_본문은_손대지_않는다():
    body = "짧은 공시 본문입니다. " * 10
    assert llm.select_excerpt(body, budget=4_000) == body


def test_신호어가_없으면_앞부분_절삭으로_되돌린다():
    body = "가나다라마바사아자차카타파하 " * 1_000
    assert llm.select_excerpt(body, budget=500) == body[:500]


def test_표지의_일반_신호어보다_원가_가동률_구간을_먼저_담는다():
    """실측 회귀 — 정기보고서는 표지·회사 개요에서 '에너지·전력' 이 먼저 터진다.

    문서 순서대로만 채우면 그 구간이 예산을 다 먹고 정작 원가·가동률에 닿지 못한다
    (실측: 롯데케미칼 분기보고서 발췌 4,012자가 전부 표지였다).
    """
    cover = "회사의 에너지 사업과 전력 사업 개요를 연혁과 함께 설명합니다. " * 400
    filler = "일반적인 서술이 이어집니다. " * 2_000
    core = "매출원가는 3조 2,000억원이며 정유부문 가동률은 95.9%를 기록했습니다. " * 5
    ex = llm.select_excerpt(cover + filler + core, budget=4_000)
    assert "매출원가" in ex and "가동률" in ex


def test_발췌는_예산을_넘지_않는다():
    """예산은 '내용 글자 수' 기준이다 — 구간 사이 구분자('\\n…\\n')는 세지 않는다."""
    body = ("원가 절감과 가동률 개선을 위한 설비투자 계획입니다. " * 50 + "채움 " * 200) * 20
    ex = llm.select_excerpt(body, budget=4_000)
    assert len(ex.replace("\n…\n", "")) <= 4_000


# ── 크롤 창 ─────────────────────────────────────────────────────────────

def test_DART_는_정기보고서_주기를_담는_창을_요구한다():
    from app.pipeline.farming import dart
    # 정기보고서 제출일 간격 최대 137일(11/14 → 3/31). 그보다 짧으면 0건이 되는 시기가 생긴다.
    assert dart.MIN_SINCE_DAYS >= 137


# ── 재크롤이 이미 확보한 근거를 깎지 않는지 ────────────────────────────────
@pytest.fixture
def db(tmp_path, monkeypatch):
    """빈 스키마만 있는 임시 DB. DB_PATH 는 import 시점에 굳으므로 모듈 속성을 바꾼다."""
    from app.db import database, seed

    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "t.db"))
    conn = database.get_connection()
    try:
        seed.create_schema(conn)
        seed.seed_legacy_kinds(conn)   # feed_item.kind 의 FK 대상(source_kind)
        conn.commit()
    finally:
        conn.close()
    return database


def _row(db, fid):
    conn = db.get_connection()
    try:
        return conn.execute(
            "SELECT evidence_grade, summary, url FROM feed_item WHERE id = ?", (fid,)
        ).fetchone()
    finally:
        conn.close()


def _doc(**kw):
    base = dict(
        ext_id="keep", kind=KIND_NEWS, source="예시화학", published_on="2026-08-01",
        title="정유 공정 최적화", body="가" * 2000, url="https://example.com/a",
        publisher="예시신문",
    )
    return RawDoc(**{**base, **kw})


def test_recrawl_never_downgrades_evidence(db):
    """본문 없이 다시 크롤해도 등급·요약·원문 URL 은 유지된다.

    유지보수용 재크롤(--with-docs 0)은 본문을 받지 않아 '제목만' + 빈 요약 + Google
    토큰 URL 을 들고 온다. 그대로 덮으면 앞선 크롤의 성과가 통째로 사라진다.
    """
    from app.pipeline.farming import ingest

    ingest.store([_doc()], use_llm=False)
    before = _row(db, "news-keep")
    assert before["evidence_grade"] == "원문 확보"
    assert before["summary"]

    stats = ingest.store(
        [_doc(body="", url="https://news.google.com/rss/articles/XYZ")], use_llm=False,
    )

    after = _row(db, "news-keep")
    assert after["evidence_grade"] == "원문 확보", "재크롤이 등급을 강등시켰다"
    assert after["summary"] == before["summary"], "재크롤이 요약을 지웠다"
    assert after["url"] == "https://example.com/a", "매체 원문 URL 이 토큰으로 되돌아갔다"
    # 소스별 등급표도 실행값이 아니라 DB 실제 상태를 보고해야 한다.
    assert stats["by_source"]["news"]["원문 확보"] == 1
    assert stats["by_source"]["news"]["제목만"] == 0


def test_grade_is_title_only_when_summary_empty(db):
    """본문을 받았어도 저장된 요약이 없으면 '제목만' 이다.

    뉴스 본문은 저작물이라 요약 자리에 남기지 않는다(llm.naive_summary). 정제를 건너뛰면
    화면에 근거로 쓸 것이 없는데 배지만 '원문 확보' 로 뜨면 사실과 다르다.
    """
    from app.pipeline.farming import ingest

    ingest.store([_doc(ext_id="restricted", meta={"body_restricted": True})],
                   use_llm=False)
    row = _row(db, "news-restricted")
    assert row["summary"] == ""
    assert row["evidence_grade"] == "제목만"
