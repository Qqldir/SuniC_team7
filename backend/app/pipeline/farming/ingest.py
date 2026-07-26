"""RawDoc → feed_item / feed_item_tag 적재.

요약(summary)은 아직 LLM 요약(llm.py) 미구현이므로, 본문/제목 기반의 naive 요약을
임시로 사용합니다. llm 단계 구현 후 _summary() 를 교체하세요.
"""
from datetime import datetime, timezone
from typing import List

from app.db.database import get_connection
from app.pipeline.farming.base import RawDoc


def _summary(doc: RawDoc, limit: int = 200) -> str:
    text = (doc.body or doc.title).strip()
    return text[:limit]


def store(docs: List[RawDoc]) -> dict:
    """적재 후 {inserted, updated, tags} 통계 반환."""
    if not docs:
        return {"seen": 0, "written": 0, "tags": 0}

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    written = tag_count = 0
    try:
        for d in docs:
            # 마스터에 없는 source_kind 방어 (crawler kind 는 항상 유효하지만 안전차원)
            conn.execute(
                """INSERT INTO feed_item (id, published_on, kind, source, title, summary, url, farmed_at)
                   VALUES (?,?,?,?,?,?,?,?)
                   ON CONFLICT(id) DO UPDATE SET
                       published_on=excluded.published_on, kind=excluded.kind,
                       source=excluded.source, title=excluded.title,
                       summary=excluded.summary, url=excluded.url, farmed_at=excluded.farmed_at""",
                (d.feed_id, d.published_on, d.kind, d.source, d.title, _summary(d), d.url, now),
            )
            written += 1
            for aff in d.tags:
                # 존재하는 계열사 코드만 태깅
                cur = conn.execute(
                    """INSERT OR IGNORE INTO feed_item_tag (feed_id, aff_code)
                       SELECT ?, ? WHERE EXISTS (SELECT 1 FROM affiliate WHERE code = ?)""",
                    (d.feed_id, aff, aff),
                )
                tag_count += cur.rowcount
        conn.commit()
    finally:
        conn.close()
    return {"seen": len(docs), "written": written, "tags": tag_count}
