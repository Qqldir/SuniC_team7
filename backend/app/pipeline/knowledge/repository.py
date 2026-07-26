"""지식 기반 조회 — feed_item / kb_* 테이블 접근."""
from datetime import date
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
            )
        )
    return items


_BASE_SELECT = """
    SELECT f.id, f.published_on, f.kind, f.source, f.title, f.summary, f.url,
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


def feed_for_affiliate(aff_code: str, within_days: int = 30, limit: int = 8, today: str | None = None) -> List[FeedItem]:
    """계열사 태그가 달린 최근 외부 동향 (과제 발굴 컨텍스트)."""
    conn = get_connection()
    try:
        rows = conn.execute(
            _BASE_SELECT
            + """
            WHERE f.id IN (SELECT feed_id FROM feed_item_tag WHERE aff_code = ?)
            GROUP BY f.id
            ORDER BY f.published_on DESC
            """,
            (aff_code,),
        ).fetchall()
        items = _rows_to_feed(rows)
    finally:
        conn.close()

    if today:
        anchor = date.fromisoformat(today)
        items = [
            it for it in items
            if (anchor - date.fromisoformat(it.d)).days <= within_days
        ]
    return items[:limit]


def affiliate_name(aff_code: str) -> str:
    conn = get_connection()
    try:
        row = conn.execute("SELECT name FROM affiliate WHERE code = ?", (aff_code,)).fetchone()
        return row["name"] if row else aff_code
    finally:
        conn.close()
