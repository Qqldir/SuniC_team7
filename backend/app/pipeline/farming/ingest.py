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
from datetime import datetime, timezone
from typing import Dict, List, Sequence

from app.db.database import get_connection
from app.pipeline.farming import classify, entity, keywords, llm
from app.config import LOCAL_TZ_SQL, today_local
from app.pipeline.farming.base import RawDoc, source_of


def _grade_rank(col: str) -> str:
    """등급 컬럼 → 순위 SQL(높을수록 상위 등급). 등급 목록은 classify.GRADES 하나만 본다."""
    whens = " ".join(
        f"WHEN '{g}' THEN {len(classify.GRADES) - i}"
        for i, g in enumerate(classify.GRADES)
    )
    return f"CASE {col} {whens} ELSE 0 END"


# 보존 규칙 4갈래:
#   ① 크롤러 사실값        항상 excluded 로 교체 (재크롤이 곧 최신 사실이다)
#   ② is_new              **레거시·미사용 컬럼.** NEW 배지는 store._evidence() 가
#                         farmed_at 의 KST 날짜로 **읽는 시점에** 판정한다. 이 컬럼을
#                         읽는 코드는 이제 없다. UPSERT 가 흔들지 않도록만 유지한다.
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
     levers, importance, reason, brief, case_worthy, enriched)
VALUES (?,?,?,?,?,?,?,?, ?,?,?,1, ?,?,?,?,?, ?,?,?,?,?,?)
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
    -- ② 레거시 컬럼 — 읽는 곳이 없다. 값을 흔들지만 않는다.
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
    -- brief 는 LLM 만 만들 수 있다. --with-docs 0 · --no-llm 재크롤이 이미 확보한
    -- 브리핑을 빈 값으로 덮으면 트렌드룸 브리핑 카드가 요약 폴백으로 되돌아간다.
    -- ★ **정제 성공이어도 빈 brief 로는 덮지 않는다.** enriched 만 보면 정제가 성공하고
    --   모델이 brief 를 빈 문자열로 낸 정상 응답에서 기존 brief 가 NULL 로 사라진다
    --   (app/db/backfill_brief.py 로 채운 값이 다음 파밍 한 번에 전부 날아간다).
    --   위 summary 가드와 같은 형태다.
    brief        = CASE WHEN excluded.brief IS NOT NULL AND excluded.brief <> ''
                        THEN excluded.brief        ELSE feed_item.brief        END,
    case_worthy  = CASE WHEN excluded.enriched THEN excluded.case_worthy  ELSE feed_item.case_worthy  END,
    enriched     = MAX(excluded.enriched, feed_item.enriched)
"""

# 그날치 키워드 등장 건수 스냅샷 (화면 KW_TREND 의 전일 대비 증감 원천).
# 실행 끝에 1회. INSERT OR REPLACE 라 같은 날 여러 번 돌려도 행이 늘지 않고 최신값으로 덮인다.
# ★ 자료 건수(COUNT(*))를 센다 — 같은 자료 안의 중복 키워드는 PK 가 이미 막는다.
# ★ day 축은 **KST** 다(store._evidence 의 NEW 판정과 같은 시계).
#   substr(farmed_at,1,10) = UTC 날짜로 끊으면 KST 같은 날 두 실행이 다른 day 로 갈라져
#   헛 차분을 내고, KST 다른 두 날이 같은 UTC day 로 뭉치면 INSERT OR REPLACE 가
#   전날 기준선을 덮어 kwTrend 가 {} 로 되돌아간다.
_KW_SNAPSHOT = """
INSERT OR REPLACE INTO keyword_daily(day, keyword, n)
SELECT date(f.farmed_at, :tz), k.keyword, COUNT(*)
  FROM feed_item f
  JOIN feed_item_keyword k ON k.feed_id = f.id
 WHERE date(f.farmed_at, :tz) = :day
 GROUP BY 1, 2
"""

# 키워드 추출에 쓸 텍스트를 **저장된 행에서 다시 읽는다** (_sync_keywords 주석 참고).
_KW_TEXT = """
SELECT COALESCE(NULLIF(title_label, ''), title) AS title, summary, metrics
  FROM feed_item WHERE id = ?
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
    """적재 후 {seen, written, tags, keywords, enriched, theme_default, by_source} 통계 반환.

    theme_default 는 LLM 테마를 못 써서 규칙 폴백으로 떨어진 건수입니다. 이 값이 크면
    본문·요약이 부족하다는 신호입니다(제목만으로는 키워드 규칙이 절반도 못 맞춥니다).

    by_source 는 소스(dart|sec|news)별 {적재, 정제, 등급별 건수} 입니다. 크롤 로그 끝의
    요약표가 crawler 의 확보 통계와 나란히 찍기 위해 씁니다 — 두 통계는 base.source_of
    라는 **같은 기준**으로 소스를 세야 서로 맞습니다.
    """
    empty_stats = {"seen": 0, "written": 0, "tags": 0, "keywords": 0, "enriched": 0,
                   "theme_default": 0, "by_source": {}}
    if not docs:
        return empty_stats

    refined = llm.enrich(docs, limit=enrich_limit, use_llm=use_llm)

    # farmed_at 은 **UTC ISO 로 저장한다** — 저장은 UTC 가 정답이고 해석(=오늘인가)만 KST 로 한다.
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    written = tag_count = kw_count = enriched = theme_default = 0
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
                ref["importance"], ref["reason"] or None, ref["brief"] or None,
                int(ref["case_worthy"]), int(was_enriched),
            ))
            written += 1
            enriched += int(was_enriched)
            tag_count += _sync_tags(conn, doc.feed_id, tags)
            # ★ _UPSERT 뒤에 부른다 — 추출 원문을 저장된 행에서 다시 읽기 때문이다.
            kw_count += _sync_keywords(conn, doc.feed_id, ref["keywords"])

            src = by_source[source_of(doc)]
            src["written"] += 1
            src["enriched"] += int(was_enriched)
            src[grade] += 1

        # 오늘치(KST) 키워드 스냅샷 — 루프 밖에서 1회. 내일 실행분과 차분해 화면 KW_TREND 가 된다.
        conn.execute(_KW_SNAPSHOT, {"tz": LOCAL_TZ_SQL, "day": today_local()})
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
        "keywords": kw_count, "enriched": enriched, "theme_default": theme_default,
        "by_source": {k: dict(v) for k, v in by_source.items()},
    }


def _sync_keywords(conn, feed_id: str, llm_keywords: List[str]) -> int:
    """동향 키워드를 교체한다 (화면 EV_KW → bootstrap.evKw).

    LLM 이 낸 키워드를 **앞자리에** 두고, 모자란 자리를 사전 추출로 채운다.
    LLM 이 없거나 실패해도(크레딧 소진·--no-llm) 사전 추출만으로 채워지는 것이 핵심이다 —
    비면 트렌드룸의 키워드 카드·트리맵 라벨·행 칩·키워드 필터가 한꺼번에 죽는다.

    태그와 같은 이유로 **지우고 다시 넣는다**: KEYWORD_LEXICON 을 고쳤을 때
    재크롤 한 번으로 갱신되어야 하고, 추가만 하면 옛 키워드가 영원히 남는다.

    ★ 추출 원문은 **이번 실행이 들고 온 값이 아니라 방금 UPSERT 된 행에서 다시 읽는다.**
      `_UPSERT` 의 보존 가드(summary · title_label · metrics)가 본문 없는 재크롤
      (`--with-docs 0` · `--no-llm` · 상한 밖 · 확보 실패)로부터 기존 값을 지켜 주는데,
      키워드만 이번 실행의 빈 ref/naive 요약으로 뽑으면 **지우고 다시 넣기가 그 가드를
      우회해** 이미 확보한 키워드를 통째로 날린다. 실측: `--no-llm --with-docs 5` 재크롤
      한 번에 키워드 보유 자료가 **77건 → 43건**(156행 → 89행)으로 무너졌다.
      저장된 행을 읽으면 같은 입력 → 같은 결과라 재크롤이 멱등해진다.
    """
    row = conn.execute(_KW_TEXT, (feed_id,)).fetchone()
    if row is None:                      # UPSERT 직후라 정상 경로에서는 없을 수 없다
        return 0
    try:
        metrics = json.loads(row["metrics"] or "[]")
    except ValueError:
        metrics = []
    text = keywords.text_of(row["title"] or "", row["summary"] or "", metrics)

    picked: List[str] = []
    for word in list(llm_keywords or []) + keywords.extract(text):
        if word and word not in picked:
            picked.append(word)
        if len(picked) >= keywords.KEYWORDS_MAX:
            break

    conn.execute("DELETE FROM feed_item_keyword WHERE feed_id = ?", (feed_id,))
    for seq, word in enumerate(picked):
        conn.execute(
            "INSERT OR IGNORE INTO feed_item_keyword(feed_id, keyword, seq) VALUES (?,?,?)",
            (feed_id, word, seq),
        )
    return len(picked)


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
