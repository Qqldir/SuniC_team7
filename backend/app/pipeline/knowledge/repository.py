"""지식 기반 조회 — feed_item / kb_* 테이블 접근."""
from typing import List

from app.db.database import get_connection
from app.models import FeedItem


def _rows_to_feed(rows) -> List[FeedItem]:
    items = []
    for r in rows:
        items.append(
            FeedItem(
                id=r["id"], d=r["published_on"], kind=r["kind"],
                src=r["source"], title=r["title"], sum=r["summary"],
                tags=r["tags"].split(",") if r["tags"] else [],
                url=r["url"],
                levers=r["levers"].split(",") if r["levers"] else [],
                importance=r["importance"],
                reason=r["reason"] or "",
                caseWorthy=bool(r["case_worthy"]),
                enriched=bool(r["enriched"]),
            )
        )
    return items


_BASE_SELECT = """
    SELECT f.id, f.published_on, f.kind, f.source, f.title, f.summary, f.url,
           f.levers, f.importance, f.reason, f.case_worthy, f.enriched,
           GROUP_CONCAT(t.aff_code) AS tags
    FROM feed_item f
    LEFT JOIN feed_item_tag t ON t.feed_id = f.id
"""


def all_feed() -> List[FeedItem]:
    conn = get_connection()
    try:
        rows = conn.execute(
            _BASE_SELECT + " GROUP BY f.id ORDER BY f.published_on DESC"
        ).fetchall()
        return _rows_to_feed(rows)
    finally:
        conn.close()


# ★ 계열사별 피드 조회를 여기에 만들지 마라. 발굴 컨텍스트의 [외부 동향] 블록은
#   prefetch._feed_block 이 만든다 — 계열사 태그뿐 아니라 is_new·importance·
#   evidence_grade 로 정렬·상한을 걸고 (ev:...) id 화이트리스트까지 함께 돌려준다.
#   비슷한 함수를 여기 두면 "발굴이 어떤 자료를 봤는가" 를 추적할 때 틀린 쪽을 읽게 된다.

def affiliate_name(aff_code: str) -> str:
    conn = get_connection()
    try:
        row = conn.execute("SELECT name FROM affiliate WHERE code = ?", (aff_code,)).fetchone()
        return row["name"] if row else aff_code
    finally:
        conn.close()


# ─────────────── 혁신 사례 ───────────────
#
# ★ 혁신 사례는 **시드로만 관리한다**(사용자 결정). 유일한 관리 경로는
#   app/db/seed_data.INNOVATION_CASES + app/db/seed.seed_cases 다.
# ★ 테이블(kb_innovation_case · kb_case_affiliate)과 시드는 그대로 둔다 —
#   발굴 프롬프트의 [검증된 혁신 사례] 블록을 prefetch._case_block 이 직접 SQL 로 읽는다.
#   이 모듈에는 사례 조회 함수가 없다(읽는 쪽이 prefetch 하나뿐이라 거기서 직접 읽는다).
