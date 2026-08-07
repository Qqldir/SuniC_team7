"""RawDoc → feed_item / feed_item_tag 적재.

    RawDoc  →  llm.enrich (요약·테마·지표·중요도)  →  classify (규칙 표시값)
            →  entity.tag_affiliates  →  DB

LLM 키가 없거나 호출이 실패하면 naive 요약 + 규칙 분류 + watchlist/키워드 태깅으로
폴백하므로, 이 함수는 어떤 설정에서도 예외 없이 완주합니다.

**화면 필수 4컬럼(kind_label / theme / biz_hint / evidence_grade)은 LLM 성패와 무관하게
항상 채워집니다** — 비면 트렌드룸 필터에서 자료가 통째로 사라집니다.
"""
import json
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Sequence

from app.db.database import get_connection
from app.pipeline.farming import classify, entity, llm
from app.pipeline.farming.base import RawDoc, source_of

# NEW 배지 유지 기간 — 이 기간이 지난 파밍 자료는 배지를 뗀다.
NEW_DAYS = 7


def _grade_rank(col: str) -> str:
    """등급 컬럼 → 순위 SQL(높을수록 상위 등급). 등급 목록은 classify.GRADES 하나만 본다."""
    whens = " ".join(
        f"WHEN '{g}' THEN {len(classify.GRADES) - i}"
        for i, g in enumerate(classify.GRADES)
    )
    return f"CASE {col} {whens} ELSE 0 END"


# 보존 규칙 4갈래:
#   ① 크롤러 사실값        항상 excluded 로 교체 (재크롤이 곧 최신 사실이다)
#   ② is_new              feed_item.is_new 유지 — 재크롤이 NEW 배지를 되살리면 안 된다
#   ③ theme / biz_hint    기존 값 우선. 비어 있을 때만 이번 규칙값을 주입
#   ④ LLM 산출물          정제에 성공한 경우에만 교체
#
# ★ ①·④ 어느 쪽이든 **이미 확보한 근거를 깎는 방향으로는 쓰지 않는다.** 본문을 받지 않는
#   재크롤(--with-docs 0 · 상한 밖 · 확보 실패)은 빈 요약 · 제목만 등급 · Google 토큰 URL 을
#   들고 오는데, 그대로 덮으면 앞선 크롤의 성과가 한 번에 사라진다(url · summary ·
#   evidence_grade 세 곳에 각각 가드가 있다).
# summary 는 ④의 예외이기도 하다. 예전 코드는 무조건 excluded 로 덮어써서 `--no-llm`
# 재크롤 한 번이면 기존 LLM 정제본이 naive 절삭으로 파괴됐다. 그렇다고 ④를 그대로 적용하면
# 첫 적재(feed_item.enriched=0)에서 요약이 안 들어가므로 두 조건이 모두 필요하다.
_UPSERT = f"""
INSERT INTO feed_item
    (id, published_on, kind, source, title, summary, url, farmed_at,
     kind_label, theme, biz_hint, is_new,
     publisher, source_label, title_label, metrics, evidence_grade,
     levers, importance, reason, case_worthy, enriched)
VALUES (?,?,?,?,?,?,?,?, ?,?,?,1, ?,?,?,?,?, ?,?,?,?,?)
ON CONFLICT(id) DO UPDATE SET
    -- ① 크롤러 사실값
    published_on   = excluded.published_on,
    kind           = excluded.kind,
    source         = excluded.source,
    title          = excluded.title,
    -- ★ url 은 '크롤러 사실값' 이지만 뉴스만 예외다. news.fetch_body 가 Google News
    --   불투명 토큰을 매체 원문 URL 로 해석해 doc.url 을 교체하는데, 본문을 다시 받지 않는
    --   재크롤(--with-docs 0 · 상한 밖 · 확보 실패)에서는 doc.url 이 다시 토큰이다.
    --   무조건 덮으면 이미 저장된 매체 원문이 토큰으로 되돌아가 '원문 보기' 링크가 깨진다.
    url            = CASE WHEN excluded.url NOT LIKE 'https://news.google.com/%'
                            OR feed_item.url IS NULL OR feed_item.url = ''
                          THEN excluded.url ELSE feed_item.url END,
    farmed_at      = excluded.farmed_at,
    publisher      = excluded.publisher,
    kind_label     = excluded.kind_label,
    -- evidence_grade 는 크롤러 사실값처럼 보이지만 실제로는 "지금 저장된 요약이 무엇을
    -- 보고 만들어졌는가" 를 뜻한다.
    --
    -- ★ **등급은 내려가지 않는다.** 이번 실행이 본문을 받지 않았다고 해서
    --   이미 원문으로 만든 요약의 등급을 '제목만' 으로 되돌리면 안 된다.
    --   유지보수용 재크롤(--with-docs 0)이나 상한 밖으로 밀린 건이 그 경우다.
    --   실측: 가드 없이 재크롤 한 번에 원문 확보 24 + 요약문 13 이 제목만 43 으로 강등됐다.
    --   (enriched 기준으로 막으려 했으나 --no-llm 경로는 양쪽 다 0 이라 전혀 보호되지 않았다.)
    evidence_grade = CASE WHEN {_grade_rank('excluded.evidence_grade')}
                            >= {_grade_rank('feed_item.evidence_grade')}
                          THEN excluded.evidence_grade ELSE feed_item.evidence_grade END,
    -- ② NEW 배지는 되살리지 않는다
    is_new         = feed_item.is_new,
    -- ③ 표시 필수값 — 기존 값이 있으면 지키고, 없을 때만 이번 값으로 채운다
    theme      = CASE WHEN excluded.enriched THEN excluded.theme
                      ELSE COALESCE(feed_item.theme, excluded.theme) END,
    biz_hint   = CASE WHEN excluded.enriched THEN excluded.biz_hint
                      ELSE COALESCE(feed_item.biz_hint, excluded.biz_hint) END,
    -- ④ LLM 산출물 — 정제 성공분만 교체
    -- 빈 요약으로는 절대 덮지 않는다. --with-docs 0 재크롤은 본문이 없어 요약도 비는데,
    -- 그때 그대로 밀어 넣으면 앞선 크롤이 만든 요약이 사라진다.
    summary      = CASE WHEN excluded.summary <> ''
                         AND (excluded.enriched OR NOT feed_item.enriched)
                        THEN excluded.summary      ELSE feed_item.summary      END,
    source_label = CASE WHEN excluded.enriched THEN excluded.source_label ELSE feed_item.source_label END,
    title_label  = CASE WHEN excluded.enriched THEN excluded.title_label  ELSE feed_item.title_label  END,
    metrics      = CASE WHEN excluded.enriched THEN excluded.metrics      ELSE feed_item.metrics      END,
    levers       = CASE WHEN excluded.enriched THEN excluded.levers       ELSE feed_item.levers       END,
    importance   = CASE WHEN excluded.enriched THEN excluded.importance   ELSE feed_item.importance   END,
    reason       = CASE WHEN excluded.enriched THEN excluded.reason       ELSE feed_item.reason       END,
    case_worthy  = CASE WHEN excluded.enriched THEN excluded.case_worthy  ELSE feed_item.case_worthy  END,
    enriched     = MAX(excluded.enriched, feed_item.enriched)
"""

# NEW 배지 감쇠 — farmed_at 이 NULL 인 시드 자료는 건드리지 않는다.
_DECAY_NEW = """
UPDATE feed_item SET is_new = 0
 WHERE is_new = 1 AND farmed_at IS NOT NULL AND farmed_at < ?
"""


def _db_themes(conn) -> List[str]:
    """theme 테이블 화이트리스트. feed_item.theme 은 theme(name) FK 라 이 밖의 값은 넣을 수 없다."""
    rows = conn.execute("SELECT name FROM theme ORDER BY sort_order, name").fetchall()
    return [r["name"] if hasattr(r, "keys") else r[0] for r in rows]


def _pick_theme(ref: dict, text: str, allowed: List[str]) -> tuple:
    """(theme, 규칙기본값으로_떨어졌는지) — LLM 값 → 규칙 → DB 첫 테마 순으로 확정한다."""
    llm_theme = ref.get("theme")
    if llm_theme and llm_theme in allowed:
        return llm_theme, False
    rule = classify.theme_by_rule(text)
    if rule in allowed:
        return rule, True
    # theme 시드가 코드 상수와 어긋난 경우의 최후 방어 — FK 위반만은 막는다.
    return (allowed[0] if allowed else None), True


def store(
    docs: Sequence[RawDoc],
    *,
    use_llm: bool = True,
    enrich_limit: int = 12,
) -> dict:
    """적재 후 {seen, written, tags, enriched, theme_default, by_source} 통계 반환.

    theme_default 는 LLM 테마를 못 써서 규칙 폴백으로 떨어진 건수입니다. 이 값이 크면
    본문·요약이 부족하다는 신호입니다(제목만으로는 키워드 규칙이 절반도 못 맞춥니다).

    by_source 는 소스(dart|sec|news)별 {적재, 정제, 등급별 건수} 입니다. 크롤 로그 끝의
    요약표가 crawler 의 확보 통계와 나란히 찍기 위해 씁니다 — 두 통계는 base.source_of
    라는 **같은 기준**으로 소스를 세야 서로 맞습니다.
    """
    empty_stats = {"seen": 0, "written": 0, "tags": 0, "enriched": 0,
                   "theme_default": 0, "by_source": {}}
    if not docs:
        return empty_stats

    refined = llm.enrich(docs, limit=enrich_limit, use_llm=use_llm)

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    cutoff = (datetime.now(timezone.utc) - timedelta(days=NEW_DAYS)).isoformat(timespec="seconds")
    conn = get_connection()
    written = tag_count = enriched = theme_default = 0
    by_source: Dict[str, Counter] = defaultdict(Counter)
    try:
        allowed_themes = _db_themes(conn)
        for doc, ref in zip(docs, refined):
            # ★ 제목으로 폴백하지 않는다 — 요약 자리에 제목을 넣으면 화면에
            #   같은 문장이 두 번 찍히고 원문 미확보 사실이 가려진다(llm.naive_summary 참고).
            summary = ref["summary"] or ""
            was_enriched = bool(ref["enriched"])

            # ── 규칙 표시값 (LLM 성패와 무관) ──
            kind_label, kind = classify.kind_of(doc)
            # 근거 등급은 원본 body 가 아니라 **프롬프트에 실제로 들어간 발췌** 길이로 판정한다.
            # 요약이 비었으면 본문을 받았더라도 '제목만' 이다 — 등급은 크롤러가 무엇을
            # 내려받았는지가 아니라 **저장된 요약이 무엇을 보고 만들어졌는지** 를 뜻한다.
            # 뉴스 본문은 저작물이라 요약 자리에 남기지 않으므로(llm.naive_summary),
            # 정제를 건너뛴 건은 본문이 있어도 화면에 근거로 쓸 것이 없다.
            grade = (classify.evidence_grade_of(len(llm.body_for_prompt(doc)))
                     if summary else classify.GRADE_TITLE)

            # 계열사 태그를 먼저 확정해야 biz_hint 를 그 태그에서 유도할 수 있다.
            tags = entity.tag_affiliates(
                f"{doc.title}\n{summary}\n{doc.body[:2000]}",
                base_tags=doc.tags,
                llm_affiliates=ref["affiliates"],
            )
            biz_hint = classify.biz_hint_of(conn, tags)
            theme, fell_back = _pick_theme(
                ref, f"{doc.title} {summary} {doc.body[:2000]}", allowed_themes,
            )
            theme_default += int(fell_back)

            conn.execute(_UPSERT, (
                doc.feed_id, doc.published_on, kind, doc.source, doc.title,
                summary, doc.url, now,
                kind_label, theme, biz_hint,
                doc.publisher or None,
                ref["org"] or None, ref["headline"] or None,
                json.dumps(ref["metrics"], ensure_ascii=False), grade,
                ",".join(ref["levers"]) or None,
                ref["importance"], ref["reason"] or None,
                int(ref["case_worthy"]), int(was_enriched),
            ))
            written += 1
            enriched += int(was_enriched)
            tag_count += _sync_tags(conn, doc.feed_id, tags)

            src = by_source[source_of(doc)]
            src["written"] += 1
            src["enriched"] += int(was_enriched)
            src[grade] += 1

        # 오래된 NEW 배지 정리 — 루프 밖에서 1회.
        conn.execute(_DECAY_NEW, (cutoff,))
        conn.commit()

        # ★ 등급 집계는 커밋 뒤 DB 에서 다시 읽는다.
        #   위 루프가 센 것은 '이번 실행이 계산한 등급' 이라, UPSERT 보존 가드가
        #   기존 등급을 지킨 경우와 어긋난다. 유지보수용 재크롤(--with-docs 0)에서
        #   표만 '전부 제목만' 이라고 보고해 운영자가 전량 유실로 오독하게 된다.
        #   적재·정제 건수는 실행 기준 그대로 두고, 등급만 실제 상태로 채운다.
        src_of_id = {d.feed_id: source_of(d) for d in docs}
        if src_of_id:
            # ★ 세 등급을 **모두 0 으로 선언**하고 시작한다. 이번 실행이 만들지 않은
            #   등급까지 키를 깔아둬야 한다 — 예전에는 `if g in src` 로 기존 키만
            #   비웠고, 아래 집계도 `in src` 로 걸러서 보존 가드가 지켜준
            #   원문 확보·요약문이 표에서 통째로 빠졌다(실측 43건 중 8건만 계수).
            for src in by_source.values():
                for g in classify.GRADES:
                    src[g] = 0
            ph = ",".join("?" * len(src_of_id))
            for r in conn.execute(
                f"SELECT id, evidence_grade FROM feed_item WHERE id IN ({ph})",
                list(src_of_id),
            ):
                src = by_source.get(src_of_id.get(r["id"]))
                if src is not None and r["evidence_grade"] in classify.GRADES:
                    src[r["evidence_grade"]] += 1
    finally:
        conn.close()
    return {
        "seen": len(docs), "written": written, "tags": tag_count,
        "enriched": enriched, "theme_default": theme_default,
        "by_source": {k: dict(v) for k, v in by_source.items()},
    }


def _sync_tags(conn, feed_id: str, tags: List[str]) -> int:
    """계열사 태그를 교체한다.

    정밀 태깅이 watchlist 1차 태깅을 **좁히는** 경우가 있어(문맥상 무관한 계열사 제거)
    추가만 해서는 반영되지 않습니다. 따라서 지우고 다시 넣습니다.
    """
    if not tags:
        return 0
    conn.execute("DELETE FROM feed_item_tag WHERE feed_id = ?", (feed_id,))
    n = 0
    for aff in tags:
        # 마스터에 존재하는 계열사 코드만 (FK 위반 방어)
        cur = conn.execute(
            """INSERT OR IGNORE INTO feed_item_tag (feed_id, aff_code)
               SELECT ?, ? WHERE EXISTS (SELECT 1 FROM affiliate WHERE code = ?)""",
            (feed_id, aff, aff),
        )
        n += cur.rowcount
    return n
