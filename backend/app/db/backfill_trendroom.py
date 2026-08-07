"""이미 쌓인 feed_item 에 트렌드룸 신규 데이터를 채우는 1회성 백필.

    python -m app.db.backfill_trendroom            # 키워드가 없는 자료만 채운다
    python -m app.db.backfill_trendroom --force    # 전량 재추출 (lexicon 을 고친 뒤)
    python -m app.db.backfill_trendroom --dry-run  # 무엇이 바뀌는지만 출력

무엇을 하나
    ① feed_item_keyword  — keywords.extract(제목+요약+지표 라벨)로 채운다.
    ② is_new 정리        — **레거시.** NEW 배지는 이제 store._evidence() 가 farmed_at 의
                          KST 날짜로 읽는 시점에 판정하므로 이 단계는 화면에 아무 영향이 없다.
                          멱등하고 무해해서 남겨 둘 뿐이다.
    ③ keyword_daily      — 가장 최근 farmed_at 날짜의 스냅샷 1회.

왜 필요한가
    evKw 는 파밍 파이프라인(ingest.store)이 앞으로 채우지만, **이미 DB 에 있는 자료**는
    다시 크롤하지 않는 한 영영 비어 있다. 그러면 트렌드룸의 '오늘 언급된 키워드' 카드가
    자료 90건을 두고도 비고, 트리맵 셀의 최다 키워드 라벨 · 행 키워드 칩 · 키워드 필터가
    한꺼번에 죽는다. LLM 크레딧 없이 화면을 DB 로 돌리는 유일한 수단이다.

    ② 는 예전에 파밍이 저장 플래그(is_new)를 감쇠시키던 시절의 잔재다. 지금은 배지를
    farmed_at 으로 읽는 시점에 판정하므로 이 컬럼을 읽는 코드가 없다 — 이 단계는
    화면을 바꾸지 않는다. is_new 를 다시 '진실' 로 착각해 읽지 마라.

기본값이 '비어 있는 것만' 인 이유
    시드 14건의 키워드는 화면 상수(EV_KW)를 옮긴 손질된 값이라 사전 추출보다 정확하다.
    기본 실행이 그것을 덮지 않게 한다. lexicon 을 고쳐 전량 다시 뽑고 싶으면 --force.

★ brief 는 건드리지 않는다. LLM 만 만들 수 있는 값이고(farming/llm.py), 규칙으로
  지어내면 트렌드룸 브리핑 카드에 근거 없는 문장이 박힌다. 시드 14건만 자산 파일에
  담긴 값으로 채워지고 나머지는 화면이 요약(e.sum)으로 폴백한다.
★ 실행 전 `cp oi_scout.db oi_scout.db.bak` 를 권장한다.
"""
import json
import sys

from app.db.database import get_connection
from app.pipeline.farming import keywords

_SELECT = """
    SELECT id,
           COALESCE(NULLIF(title_label, ''), title) AS title,
           summary, metrics
      FROM feed_item
     ORDER BY id
"""


def backfill_keywords(conn, *, force: bool = False, dry_run: bool = False) -> dict:
    """feed_item_keyword 를 사전 추출로 채운다. {대상, 채움, 빈손} 반환."""
    have = {
        r["feed_id"]
        for r in conn.execute("SELECT DISTINCT feed_id FROM feed_item_keyword")
    }
    targets, filled, empty = 0, 0, []
    for r in conn.execute(_SELECT).fetchall():
        if not force and r["id"] in have:
            continue
        targets += 1
        try:
            metrics = json.loads(r["metrics"] or "[]")
        except ValueError:
            metrics = []
        words = keywords.extract(keywords.text_of(r["title"], r["summary"], metrics))
        if not words:
            empty.append(r["id"])
            continue
        filled += 1
        if dry_run:
            continue
        conn.execute("DELETE FROM feed_item_keyword WHERE feed_id = ?", (r["id"],))
        for seq, word in enumerate(words):
            conn.execute(
                "INSERT OR IGNORE INTO feed_item_keyword(feed_id, keyword, seq) VALUES (?,?,?)",
                (r["id"], word, seq),
            )
    return {"targets": targets, "filled": filled, "empty": empty}


def clear_seed_new_badge(conn, *, dry_run: bool = False) -> int:
    """시드 자료(farmed_at IS NULL)의 is_new 를 0 으로 내린다.

    ★ 레거시 단계다. NEW 배지는 store._evidence() 가 farmed_at 의 KST 날짜로 판정하므로
      이 UPDATE 는 더 이상 화면에 영향이 없다(farmed_at 이 NULL 이면 판정 자체가 거짓).
      멱등·무해해서 남겨 둔다.
    """
    n = conn.execute(
        "SELECT COUNT(*) FROM feed_item WHERE is_new = 1 AND farmed_at IS NULL"
    ).fetchone()[0]
    if n and not dry_run:
        conn.execute("UPDATE feed_item SET is_new = 0 WHERE farmed_at IS NULL")
    return n


def snapshot_keyword_daily(conn, *, dry_run: bool = False) -> tuple:
    """가장 최근 파밍 날짜의 키워드 등장 건수를 keyword_daily 에 1회 기록한다.

    ★ 하루치만 생긴다. store._kw_trend 는 distinct day 가 2개 미만이면 {} 를 내리므로
      화면 KW_TREND 는 전부 '–' 로 뜬다 — 비교 기준이 아직 없다는 정직한 표시다.
      다음 파밍 실행이 둘째 날 스냅샷을 남기는 순간부터 증감이 나온다.
    """
    day = conn.execute(
        "SELECT MAX(substr(farmed_at, 1, 10)) FROM feed_item WHERE farmed_at IS NOT NULL"
    ).fetchone()[0]
    if not day:
        return None, 0
    rows = conn.execute(
        """SELECT k.keyword, COUNT(*) AS n
             FROM feed_item f JOIN feed_item_keyword k ON k.feed_id = f.id
            WHERE substr(f.farmed_at, 1, 10) = ?
            GROUP BY k.keyword""",
        (day,),
    ).fetchall()
    if not dry_run:
        for r in rows:
            conn.execute(
                "INSERT OR REPLACE INTO keyword_daily(day, keyword, n) VALUES (?,?,?)",
                (day, r["keyword"], r["n"]),
            )
    return day, len(rows)


def main(argv=None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    force = "--force" in argv
    dry_run = "--dry-run" in argv

    conn = get_connection()
    try:
        kw = backfill_keywords(conn, force=force, dry_run=dry_run)
        badge = clear_seed_new_badge(conn, dry_run=dry_run)
        day, n_kw = snapshot_keyword_daily(conn, dry_run=dry_run)
        if not dry_run:
            conn.commit()
    finally:
        conn.close()

    head = "[dry-run] " if dry_run else ""
    print(f"{head}키워드 백필: 대상 {kw['targets']}건 · 채움 {kw['filled']}건 "
          f"· 키워드 0개 {len(kw['empty'])}건")
    if kw["empty"]:
        print(f"  키워드가 안 걸린 자료(사전에 없는 주제): {', '.join(kw['empty'][:8])}"
              + (" …" if len(kw["empty"]) > 8 else ""))
    print(f"{head}시드 자료 NEW 배지 해제: {badge}건")
    if day:
        # dry-run 은 키워드를 넣지 않았으므로 이 수치는 '백필 반영 전' 기준이다.
        note = " (백필 반영 전 기준)" if dry_run else ""
        print(f"{head}keyword_daily 스냅샷: {day} · 키워드 {n_kw}종{note}")
        print("  ※ 하루치뿐이라 화면 KW_TREND 는 '–' 로 뜬다(비교 기준 없음). "
              "다음 파밍 실행부터 증감이 나온다.")
    else:
        print(f"{head}keyword_daily 스냅샷: 파밍 자료가 없어 건너뜀")


if __name__ == "__main__":
    main()
