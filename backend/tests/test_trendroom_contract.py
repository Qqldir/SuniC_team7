"""GET /api/bootstrap 계약 + 트렌드룸 신규 데이터(evOc·evKw·evBrief·kwTrend) 회귀 테스트.

여기서 지키려는 것은 넷이다.

1. **최상위 키 집합이 계약과 정확히 같다.** 프론트 applyBootstrap 이 이 이름들로
   화면 상수를 채운다 — 하나만 빠져도 그 화면이 상수 데모로 되돌아가고,
   남는 키는 매 요청 페이로드를 키운다.
2. 키워드 추출이 **결정론적**이다. 사전을 고치면 결과가 바뀌어야 하지만,
   같은 입력에 같은 출력이 나와야 트리맵 라벨·필터가 새로고침마다 흔들리지 않는다.
3. `kwTrend` 는 **비교 기준이 없으면 {}** 다. 첫 스냅샷뿐인데 n-0=+n 을 내리면
   전 키워드에 ▲ 가 붙어 "어제보다 늘었다" 는 거짓 정보가 화면에 박힌다.
4. `evBrief` 는 **빈 값이면 키를 안 내린다.** 화면이 `EV_BRIEF[k] || e.sum` 으로
   요약에 폴백하므로, 빈 문자열을 내리면 브리핑 카드가 빈 줄이 된다.

    cd backend && .venv/bin/python -m pytest tests/ -q
"""
import re
import sqlite3
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

from app import store  # noqa: E402
from app.pipeline.farming import keywords  # noqa: E402

# 계약이 정한 최상위 22키 — 순서까지 그대로다(프론트 계약 문서와 1:1).
# crawlAt 은 나중에 붙었다 — 사이드바 '수집 파이프라인' 이 crawl_source.last_at(아무도
# 갱신하지 않는 시드 컬럼)을 읽다가 "수집 이력 없음" 이라는 거짓을 띄웠기 때문이다.
BOOTSTRAP_KEYS = [
    "user", "today", "kinds", "ocs", "ocColor", "bizColor", "levers",
    "evidence", "evBizFallback", "evNew",
    "evOc", "evKw", "evBrief", "kwTrend",
    "kindMap", "versions", "tasks", "sources", "crawlAt", "uploads",
    "instruction", "state",
]


@pytest.fixture
def db(tmp_path, monkeypatch):
    """시드까지 끝난 임시 DB 를 물린 커넥션 팩토리.

    ★ 원본 oi_scout.db 는 건드리지 않는다 — tmp_path 아래 새 파일을 만든다.
    """
    path = tmp_path / "t.db"
    monkeypatch.setattr("app.config.DB_PATH", str(path))
    monkeypatch.setattr("app.db.database.DB_PATH", str(path))

    from app.db import seed

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    seed.create_schema(conn)
    seed.seed_trendroom.seed_all(conn)
    # ★ seed.main() 과 같은 순서다. 시드 행의 name_key 가 비어 있으면 중복 차단
    #   (name_key_exists · UNIQUE 인덱스)이 시드 과제를 못 보고 통과시킨다.
    seed.backfill_name_key(conn)
    conn.commit()
    yield conn
    conn.close()


# ── bootstrap 계약 ──────────────────────────────────────────────────────

def test_bootstrap_최상위_키가_계약과_같다(db, monkeypatch):
    monkeypatch.setattr(store, "get_connection", lambda: db)
    payload = store.bootstrap("admin@sk.com")
    assert list(payload) == BOOTSTRAP_KEYS


def test_bootstrap_이_삭제된_키를_되살리지_않는다(db, monkeypatch):
    """themes·evTheme·admins·evalCriteria 는 화면에 렌더 지점이 없어 뺐다.

    theme **테이블**은 그대로 산다(FK · LLM 분류가 쓴다) — 지운 것은 페이로드 2키뿐이라
    테이블이 있다는 이유로 키를 되살리는 실수를 여기서 막는다.
    """
    # bootstrap 은 finally 에서 커넥션을 닫는다 — 테이블 확인이 먼저다.
    assert db.execute("SELECT COUNT(*) FROM theme").fetchone()[0] > 0
    monkeypatch.setattr(store, "get_connection", lambda: db)
    payload = store.bootstrap("admin@sk.com")
    for gone in ("themes", "evTheme", "admins", "evalCriteria"):
        assert gone not in payload


def test_시드_자료의_키워드와_브리핑이_실려온다(db, monkeypatch):
    """화면 상수 EV_KW·EV_BRIEF 를 옮긴 시드 14건이 그대로 나와야 한다."""
    monkeypatch.setattr(store, "get_connection", lambda: db)
    payload = store.bootstrap("admin@sk.com")
    assert payload["evKw"]["e1"] == ["정기보수", "공기 단축", "고정비", "원가 절감"]
    assert payload["evBrief"]["e1"].startswith("안전·품질 검증은")
    # evOc 는 feed_item_tag 에서 온다 — 자료 90건 전량이 계열사 태그를 갖는다.
    assert len(payload["evOc"]) == len(payload["evidence"])


def test_evBrief_는_빈_값이면_키를_내리지_않는다(db):
    db.execute("UPDATE feed_item SET brief = '' WHERE id = 'e1'")
    db.execute("UPDATE feed_item SET brief = NULL WHERE id = 'e2'")
    assert "e1" not in store._ev_brief(db)
    assert "e2" not in store._ev_brief(db)


# ── kwTrend ────────────────────────────────────────────────────────────

def test_스냅샷이_하루뿐이면_증감을_내리지_않는다(db):
    db.execute("INSERT INTO keyword_daily(day, keyword, n) VALUES ('2026-08-06','고정비',5)")
    assert store._kw_trend(db) == {}


def test_증감은_최근_두_스냅샷의_차분이고_0은_뺀다(db):
    rows = [
        ("2026-08-05", "고정비", 5), ("2026-08-05", "물류비", 3), ("2026-08-05", "수율", 2),
        ("2026-08-06", "고정비", 8), ("2026-08-06", "물류비", 3),
    ]
    db.executemany("INSERT INTO keyword_daily(day, keyword, n) VALUES (?,?,?)", rows)
    trend = store._kw_trend(db)
    assert trend["고정비"] == 3          # 늘어난 것
    assert trend["수율"] == -2           # 사라진 것도 감소로 잡힌다
    assert "물류비" not in trend         # 차분 0 은 렌더 결과가 같아 뺀다


def test_증감은_가장_최근_두_날짜만_본다(db):
    rows = [
        ("2026-08-01", "고정비", 100),   # 오래된 날짜는 무시돼야 한다
        ("2026-08-05", "고정비", 5),
        ("2026-08-06", "고정비", 8),
    ]
    db.executemany("INSERT INTO keyword_daily(day, keyword, n) VALUES (?,?,?)", rows)
    assert store._kw_trend(db) == {"고정비": 3}


# ── 사전 기반 키워드 추출 ────────────────────────────────────────────────

def test_표시형은_전부_제_이름으로_걸린다():
    for display in keywords.KEYWORD_LEXICON:
        assert display in keywords.extract(display, limit=1), display


def test_추출은_결정론적이고_상한을_지킨다():
    text = ("정기보수 공기 단축으로 고정비를 흡수하고 원가 절감과 통합 조달, "
            "전수검사 자동화까지 검토")
    first = keywords.extract(text)
    assert first == keywords.extract(text)
    assert len(first) <= keywords.KEYWORDS_MAX


def test_영문_약어는_단어_경계를_본다():
    """'TA' 가 data·metadata 에, 'MRO' 가 mrophy 류에 걸리면 안 된다.

    classify._count_hits 의 경계 규칙을 그대로 쓰는지 확인하는 자리다.
    """
    assert "정기보수" not in keywords.extract("data metadata database update", limit=8)
    assert "정기보수" in keywords.extract("TA 공기 산정", limit=8)


def test_키워드가_없으면_빈_리스트다():
    assert keywords.extract("주식보상 계획 관련 보통주 등록") == []


# ── 적재 시 키워드 합성 (LLM 앞자리 + 사전으로 채우기) ──────────────────────

def _kw_rows(conn, feed_id):
    return [r["keyword"] for r in conn.execute(
        "SELECT keyword FROM feed_item_keyword WHERE feed_id = ? ORDER BY seq", (feed_id,)
    )]


def _store_text(conn, feed_id, *, title="", summary="", metrics="[]"):
    """추출 원문을 feed_item 행에 심는다 — _sync_keywords 가 읽는 곳이 거기다."""
    conn.execute(
        "UPDATE feed_item SET title = ?, title_label = NULL, summary = ?, metrics = ? WHERE id = ?",
        (title, summary, metrics, feed_id),
    )


def test_LLM_키워드가_앞자리를_차지하고_사전이_나머지를_채운다(db):
    from app.pipeline.farming import ingest

    _store_text(db, "e1", title="정기보수 공기 단축으로 고정비 흡수")
    n = ingest._sync_keywords(db, "e1", ["현장 실증"])
    got = _kw_rows(db, "e1")
    assert got[0] == "현장 실증"
    assert n == len(got) == keywords.KEYWORDS_MAX
    assert "정기보수" in got


def test_LLM_이_없어도_사전만으로_채워진다(db):
    from app.pipeline.farming import ingest

    _store_text(db, "e1", title="정기보수 공기 단축으로 고정비를 흡수")
    ingest._sync_keywords(db, "e1", [])
    assert _kw_rows(db, "e1")[:2] == ["정기보수", "공기 단축"]


def test_키워드는_추가가_아니라_교체다(db):
    """KEYWORD_LEXICON 을 고치면 재크롤 한 번으로 갱신돼야 한다 — 옛 값이 남으면 안 된다."""
    from app.pipeline.farming import ingest

    _store_text(db, "e1")
    ingest._sync_keywords(db, "e1", ["옛 키워드"])
    ingest._sync_keywords(db, "e1", ["새 키워드"])
    assert _kw_rows(db, "e1") == ["새 키워드"]


def test_추출_원문은_이번_실행값이_아니라_저장된_행에서_읽는다(db):
    """본문 없는 재크롤(`--no-llm` · `--with-docs 0`)이 기존 키워드를 지우면 안 된다.

    `_UPSERT` 는 summary·title_label·metrics 에 보존 가드가 있어 재크롤이 좋은 값을
    덮지 못한다. 그런데 키워드를 이번 실행의 빈 ref 로 뽑으면 '지우고 다시 넣기' 가
    그 가드를 우회해 버린다 — 실측으로 키워드 보유 자료가 77→43 건으로 무너졌다.
    저장된 행에서 읽으면 같은 행 → 같은 결과라 재크롤이 멱등하다.
    """
    from app.pipeline.farming import ingest

    _store_text(db, "e1", title="정기보수 공기 단축으로 고정비를 흡수한다")
    first = _kw_rows(db, "e1") if ingest._sync_keywords(db, "e1", []) else []
    assert first, "사전 추출이 최소 1개는 뽑아야 이 테스트가 의미를 갖는다"

    # 재크롤: LLM 도 없고 이번 실행이 들고 온 텍스트도 없다. 행은 그대로다.
    ingest._sync_keywords(db, "e1", [])
    assert _kw_rows(db, "e1") == first


# ── NEW 배지 = '오늘(KST) 크롤분' (읽는 시점 판정) ───────────────────────────
#
# 저장 플래그(feed_item.is_new)는 파밍이 돌 때만 감쇠했다 — 기준일을 3개월 뒤로 밀어도
# evNew 가 76 그대로였다(실측). 그래서 store._evidence 가 farmed_at 의 **KST 날짜**로
# 읽는 시점에 판정한다. 아래 두 테스트가 그 계약을 고정한다.

def _set_farmed(conn, feed_id, iso, *, is_new=0):
    """farmed_at 을 직접 심는다. is_new 는 일부러 반대로 넣어 '읽지 않는다' 를 증명한다."""
    conn.execute("UPDATE feed_item SET farmed_at = ?, is_new = ? WHERE id = ?",
                 (iso, is_new, feed_id))


def test_NEW_는_오늘_크롤분에만_붙고_어제분은_빠진다(db, monkeypatch):
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)
    # is_new 를 정반대로 심는다 — 그래도 결과는 farmed_at 만 따라야 한다.
    _set_farmed(db, "e1", now.isoformat(timespec="seconds"), is_new=0)
    _set_farmed(db, "e2", (now - timedelta(days=1)).isoformat(timespec="seconds"), is_new=1)
    monkeypatch.setattr(store, "get_connection", lambda: db)
    ev_new = store.bootstrap("admin@sk.com")["evNew"]
    assert ev_new.get("e1") == 1
    assert "e2" not in ev_new


def test_NEW_판정은_UTC_가_아니라_KST_날짜로_한다(db, monkeypatch):
    """KST 새벽 크롤분은 UTC 로는 '어제' 다. substr(farmed_at,1,10) 로 비교하면
    오늘 수집분이 통째로 사라진다(실측 76건 → 0건)."""
    from datetime import date, datetime, time, timedelta, timezone

    from app.config import LOCAL_TZ, today_local

    # 오늘(KST) 00:30 = 어제(UTC) 15:30
    kst_dawn = datetime.combine(date.fromisoformat(today_local()), time(0, 30), LOCAL_TZ)
    utc_iso = kst_dawn.astimezone(timezone.utc).isoformat(timespec="seconds")
    assert utc_iso[:10] != today_local(), "이 테스트는 UTC 날짜가 달라야 의미가 있다"
    _set_farmed(db, "e1", utc_iso)
    # 오늘(KST) 자정 직전의 하루 전 = 확실한 '어제'
    _set_farmed(db, "e2", (kst_dawn - timedelta(days=1)).astimezone(timezone.utc)
                .isoformat(timespec="seconds"))
    monkeypatch.setattr(store, "get_connection", lambda: db)
    ev_new = store.bootstrap("admin@sk.com")["evNew"]
    assert ev_new.get("e1") == 1
    assert "e2" not in ev_new


def test_today_는_모듈_상수가_아니라_요청_시점_KST_다(db, monkeypatch):
    from app.config import today_local

    monkeypatch.setattr(store, "get_connection", lambda: db)
    assert store.bootstrap("admin@sk.com")["today"] == today_local()


# ── 마지막 수집 시각(crawlAt) ───────────────────────────────────────────────
#
# crawl_source.last_at 은 파이프라인이 **쓰지 않는** 표시용 컬럼이다. 시드가 넣은
# '오늘 08:00' 을 지우자 이번에는 화면이 "크롤링 · 수집 이력 없음" 이라고 단정했다 —
# 자료가 90건 실재하고 바로 옆 헤더는 '수집 90건' 인데도. 진짜 값은 farmed_at 에 있다.

def test_crawlAt_은_실제_파밍_시각이고_KST_다(db, monkeypatch):
    from datetime import date, datetime, time, timezone

    from app.config import LOCAL_TZ, today_local

    db.execute("UPDATE feed_item SET farmed_at = NULL")
    # 오늘(KST) 03:00 = 어제(UTC) 18:00 — UTC 그대로 표시하면 날짜가 하루 어긋난다.
    kst = datetime.combine(date.fromisoformat(today_local()), time(3, 0), LOCAL_TZ)
    _set_farmed(db, "e1", kst.astimezone(timezone.utc).isoformat(timespec="seconds"))
    monkeypatch.setattr(store, "get_connection", lambda: db)
    assert store.bootstrap("admin@sk.com")["crawlAt"] == f"{today_local().replace('-', '.')} 03:00"


def test_crawlAt_은_크롤_이력이_없으면_빈_값이다(db, monkeypatch):
    """빈 값이어야 화면이 그 줄을 통째로 안 그린다 — '수집 이력 없음' 은 거짓말이었다."""
    db.execute("UPDATE feed_item SET farmed_at = NULL")
    monkeypatch.setattr(store, "get_connection", lambda: db)
    assert store.bootstrap("admin@sk.com")["crawlAt"] == ""


# ── 발송 대상 필터의 시간 축 ────────────────────────────────────────────────

def test_버전_at_은_발송이력과_같은_표기의_분_단위다(db, monkeypatch):
    """'지난 발송 이후' 필터는 두 값을 **문자열 비교**한다.

    한쪽이 하이픈('2026-08-07')이고 다른 쪽이 점('2026.08.07')이면 '-'(45) < '.'(46) 라
    비교가 통째로 뒤집힌다. 그리고 날짜만 비교하면 발송한 날 만든 과제가 그날 하루
    대상에서 빠진다 — 그래서 분 단위까지 내려간다.
    """
    import re as _re

    db.execute("UPDATE gen_version SET created_at = '2026-08-07T15:51:49' WHERE id = 'g1'")
    monkeypatch.setattr(store, "get_connection", lambda: db)
    ver = next(v for v in store.bootstrap("admin@sk.com")["versions"] if v["id"] == "g1")
    assert ver["at"] == "2026.08.07 15:51"
    # store.mark_report_sent 가 쓰는 표기와 **한 글자도** 다르면 안 된다.
    from datetime import datetime

    assert _re.fullmatch(r"\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}",
                         datetime.now().strftime("%Y.%m.%d %H:%M"))
    assert ver["at"] > "2026.08.07 15:50" and not ver["at"] > "2026.08.07 15:52"


# ── 커스텀 생성 중복 차단 (L1 · L1' · L2 · L3) ──────────────────────────────
#
# 사용자가 커스텀 생성을 반복 클릭해 같은 과제가 5번 생겼다(id 1401~1405).
# 예전 create_custom 은 "현업이 지시한 경로" 라는 근거로 중복 검사를 건너뛰었고,
# 그 근거는 기각됐다. 아래 테스트가 4개 층을 각각 고정한다.

# ★ 시드 SKO 는 정비/TA 과제가 없다(간접비·구매·물류비·수율·에너지비만 있다).
#   레버가 겹치면 시드 과제와의 이름 유사도가 걸려 테스트가 무엇을 재는지 흐려진다 —
#   실제로 '수율' 로 두면 시드 #1237 과 0.74 로 붙는다(퍼지 판정이 도는 증거이기도 하다).
CG_OC = "SKO"
CG_OC2 = "SKEO"          # 계열사 스코프 확인용 — 여기도 정비/TA 가 비어 있다
CG_LEVER = "정비/TA"
CG_EV = ["e1"]
CG_EV2 = ["e1", "e2"]     # 근거 2건 — '근거집합 일치' 판정이 도는 최소 조건
CG_NAME = "테스트 전용 커스텀 과제 알파"


@pytest.fixture
def api(db, monkeypatch):
    """TestClient — 임시 DB · 인증 우회 · LLM 0회 · 자동 평가 0회.

    OI_REGEN_LLM=0 이라 create_custom_llm 은 문자열 조립 폴백으로 내려간다.
    중복 차단은 LLM 성패와 무관한 층이므로 이 조건에서 전부 검증된다.
    """
    from fastapi.testclient import TestClient

    from app.api.deps import current_email
    from app.main import app as fastapi_app

    monkeypatch.setattr(store, "OI_REGEN_LLM", False)
    monkeypatch.setattr(store, "_auto_evaluate", lambda pids: None)
    fastapi_app.dependency_overrides[current_email] = lambda: "admin@sk.com"
    try:
        yield TestClient(fastapi_app)
    finally:
        fastapi_app.dependency_overrides.clear()


def _run_custom(client, **body):
    """POST /api/proposals/custom → job 완료까지 폴링. (응답, 마지막 job 결과)"""
    import time

    res = client.post("/api/proposals/custom", json=body)
    if res.status_code != 200:
        return res, None
    job = res.json()["job"]
    for _ in range(200):
        d = client.get(f"/api/proposals/custom/{job}").json()
        if d["status"] != "running":
            return res, d
        time.sleep(0.05)
    raise AssertionError("job 이 끝나지 않았습니다")


def _count(conn):
    return conn.execute("SELECT COUNT(*) FROM proposal").fetchone()[0]


def test_L1_같은_이름_커스텀_두번째는_409_로_막힌다(api, db):
    body = {"oc": CG_OC, "lever": CG_LEVER, "ev": CG_EV, "plan": "파일럿", "name": CG_NAME}
    _, done = _run_custom(api, **body)
    assert done["status"] == "done" and done["id"] is not None

    res = api.post("/api/proposals/custom", json=body)
    assert res.status_code == 409
    data = res.json()
    assert data["code"] == "duplicate_exact"
    assert isinstance(data["detail"], str)      # dict 면 화면이 '[object Object]' 를 띄운다
    assert data["id"] == done["id"]


def test_L1_완전일치는_force_로도_뚫리지_않는다(api, db):
    body = {"oc": CG_OC, "lever": CG_LEVER, "ev": CG_EV, "plan": "파일럿", "name": CG_NAME}
    _run_custom(api, **body)
    before = _count(db)
    res = api.post("/api/proposals/custom", json={**body, "force": True})
    assert res.status_code == 409
    assert res.json()["code"] == "duplicate_exact"
    assert _count(db) == before


def test_L1_퍼지_중복은_409_지만_force_로_통과한다(api, db):
    """근거를 2건 이상 똑같이 쓰는 같은 레버 과제는 이름이 달라도 같은 아이디어다.
    다만 오탐이 실재해서('육상운송'↔'해상운송' 0.645) 확인 후 진행 경로를 남긴다."""
    _run_custom(api, oc=CG_OC, lever=CG_LEVER, ev=CG_EV2, plan="파일럿", name=CG_NAME)
    other = {"oc": CG_OC, "lever": CG_LEVER, "ev": CG_EV2, "plan": "파일럿",
             "name": "표현을 통째로 바꾼 이름이지만 같은 근거다"}

    res = api.post("/api/proposals/custom", json=other)
    assert res.status_code == 409
    assert res.json()["code"] == "duplicate_similar"
    assert isinstance(res.json()["detail"], str)

    before = _count(db)
    _, done = _run_custom(api, **{**other, "force": True})
    assert done["status"] == "done" and done["id"] is not None
    assert _count(db) == before + 1


def test_근거_1건만_같은_다른_과제는_막지_않는다(api, db):
    """같은 벤치마크 1건에서 서로 다른 과제가 나오는 것은 정상이다.

    예전에는 근거가 1건만 같아도 즉시 중복으로 판정했다. 화면 커스텀 생성이 근거를
    1건만 보내고 실제 과제 75건 중 68건이 근거 1건짜리라, 그 규칙이 '같은 계열사 +
    같은 레버 + 같은 벤치마크 1건' 으로 퇴화해 같은 (계열사,레버) 60쌍 중 37쌍을
    중복으로 잡았다 — 이름 유사도 0.06~0.36 인 명백히 다른 과제들이다.
    재생성 경로에는 force 우회로가 없어서 그런 초안이 조용히 사라졌다.
    """
    _run_custom(api, oc=CG_OC, lever=CG_LEVER, ev=CG_EV, plan="파일럿", name=CG_NAME)
    before = _count(db)
    res, done = _run_custom(api, oc=CG_OC, lever=CG_LEVER, ev=CG_EV, plan="파일럿",
                            name="완전히 다른 주제의 지원조직 운영구조 재설계")
    assert res.status_code == 200, "근거 1건 겹침만으로 거부하면 정상 사용을 깨뜨린다"
    assert done["id"] is not None
    assert _count(db) == before + 1


def test_문장부호만_다른_과제명은_완전일치로_막힌다(api, db):
    """과제명 끝에 마침표 하나면 L1·L3 을 둘 다 빠져나갔다(실측으로 뚫린 구멍).

    남는 것은 force 로 넘길 수 있는 퍼지 판정뿐이라, 확인 한 번에 화면상 글자가
    똑같아 보이는 과제가 만들어졌다.
    """
    _run_custom(api, oc=CG_OC, lever=CG_LEVER, ev=CG_EV, plan="파일럿", name=CG_NAME)
    before = _count(db)
    for variant in (CG_NAME + ".", CG_NAME + "!", CG_NAME.replace(" ", "　"),
                    f"'{CG_NAME}'"):
        res = api.post("/api/proposals/custom", json={
            "oc": CG_OC, "lever": CG_LEVER, "ev": CG_EV, "plan": "파일럿",
            "name": variant, "force": True,      # force 로도 못 뚫는 층이어야 한다
        })
        assert res.status_code == 409, f"{variant!r} 가 통과했다"
        assert res.json()["code"] == "duplicate_exact"
    assert _count(db) == before


def test_거부_문구는_가장_비슷한_과제를_가리킨다(db, monkeypatch):
    """'기존 과제 보기' 가 엉뚱한 과제를 열면 안 된다.

    예전에는 첫 매치에서 바로 돌려줬고 SELECT 에 ORDER BY 도 없어서, 반환되는 행이
    name_key **사전순**으로 결정됐다. 라틴 문자로 시작하는 과제가 하나 생기자
    실제 근접 중복을 두고 그쪽을 가리켰다.
    """
    from app.pipeline.discovery import persist

    monkeypatch.setattr(store, "_auto_evaluate", lambda pids: None)
    near = store.create_custom(CG_OC, CG_LEVER, CG_EV, "파일럿", "정기보수 공기 단축 파일럿 확대 검토")
    far = store.create_custom(CG_OC, CG_LEVER, CG_EV, "파일럿", "AOI 장비 도입 타당성 사전검토")
    assert near["id"] and far["id"]

    dup = persist.find_duplicate(
        db, CG_OC, CG_LEVER, store.name_key("정기보수 공기 단축 파일럿 확대 검토 재추진"), CG_EV)
    assert dup is not None and dup["id"] == near["id"], dup


def test_중복_판정은_계열사_스코프다(api, db):
    """다른 계열사에 같은 이름은 정당하다 — 막으면 정상 사용을 깨뜨린다."""
    _run_custom(api, oc=CG_OC, lever=CG_LEVER, ev=CG_EV, plan="파일럿", name=CG_NAME)
    _, done = _run_custom(api, oc=CG_OC2, lever=CG_LEVER, ev=CG_EV, plan="파일럿", name=CG_NAME)
    assert done["status"] == "done" and done["id"] is not None


def test_L2_store_create_custom_은_중복이면_만들지_않는다(db, monkeypatch):
    """라우트를 우회해도 저장 직전 게이트가 막는다(이름을 LLM·근거에서 파생하는 경로).

    ★ get_connection 은 monkeypatch 하지 않는다 — proposals_payload 가 커넥션을
      스스로 닫으므로 fixture 커넥션을 물리면 그 뒤 SELECT 가 전부 죽는다.
      DB_PATH 가 이미 tmp 를 가리키므로 실제 경로 그대로 검증된다.
    """
    monkeypatch.setattr(store, "_auto_evaluate", lambda pids: None)
    first = store.create_custom(CG_OC, CG_LEVER, CG_EV, "파일럿", "중복 게이트 확인용 과제")
    assert first["id"] is not None
    before = _count(db)

    again = store.create_custom(CG_OC, CG_LEVER, CG_EV, "파일럿", "중복 게이트 확인용 과제")
    assert again["id"] is None
    assert again["dupId"] == first["id"]
    assert "이미 있습니다" in again["reason"]
    assert _count(db) == before          # INSERT 도 commit 도 하지 않았다


def test_L3_DB_가_같은_계열사_같은_과제명을_거부한다(db):
    """파이썬 검사를 전부 우회한 INSERT 도 UNIQUE 인덱스가 막는다(동시 job 최후 방어)."""
    row = db.execute(
        "SELECT ver_id, aff_code, lever, name, name_key FROM proposal "
        " WHERE name_key IS NOT NULL LIMIT 1"
    ).fetchone()
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO proposal(ver_id, aff_code, lever, name, name_key, origin)"
            " VALUES (?,?,?,?,?,'커스텀')",
            (row["ver_id"], row["aff_code"], row["lever"], row["name"], row["name_key"]),
        )
    db.rollback()


def test_재생성_후보풀_폴백은_임계값_0_70_에서도_저장된다(db, monkeypatch):
    """중복 임계값을 0.55 → 0.70 으로 올린 것이 재생성 경로를 깨지 않는지."""
    from app.pipeline.discovery import persist

    assert persist.SIMILARITY_LIMIT == 0.70
    monkeypatch.setattr(store, "_auto_evaluate", lambda pids: None)
    monkeypatch.setattr(store, "OI_REGEN_LLM", False)
    before = _count(db)
    out = store.regenerate()
    assert out["ver"] is not None, "후보 풀 폴백이 한 건도 저장하지 못했다"
    assert _count(db) > before


def test_name_key_규칙을_바꾸면_기존_행이_재계산된다(db):
    """정규화 규칙만 바꾸고 기존 행을 두면 중복 차단이 조용히 뚫린다.

    옛 키('…검토.')와 새 키('…검토')는 서로 안 걸리므로, 새 규칙으로 만든 요청이
    이미 있는 과제를 못 보고 통과한다. seed._recompute_name_key 가 그 구멍을 닫는다.
    """
    from app.db import seed

    row = db.execute("SELECT id, name FROM proposal ORDER BY id LIMIT 1").fetchone()
    legacy = re.sub(r"[\s·/()\-\[\]]+", "", row["name"] + ".").lower()   # 옛 규칙 그대로
    db.execute("UPDATE proposal SET name_key = ? WHERE id = ?", (legacy, row["id"]))
    db.execute("DELETE FROM app_setting WHERE key = 'name_key_rev'")
    assert legacy != store.name_key(row["name"])

    seed._recompute_name_key(db)
    seed._disambiguate_proposal_name_key(db)
    assert db.execute(
        "SELECT name_key FROM proposal WHERE id = ?", (row["id"],)
    ).fetchone()["name_key"] == store.name_key(row["name"])
    # 중복 클러스터가 남으면 UNIQUE 인덱스를 다시 못 만든다.
    assert db.execute(
        "SELECT COUNT(*) FROM (SELECT 1 FROM proposal WHERE name_key IS NOT NULL"
        "  GROUP BY aff_code, name_key HAVING COUNT(*) > 1)"
    ).fetchone()[0] == 0

    # 멱등: 개정 번호를 기록한 뒤에는 다시 돌지 않는다.
    seed._mark_name_key_rev(db)
    snapshot = db.execute("SELECT id, name_key FROM proposal ORDER BY id").fetchall()
    seed._recompute_name_key(db)
    assert db.execute("SELECT id, name_key FROM proposal ORDER BY id").fetchall() == snapshot
