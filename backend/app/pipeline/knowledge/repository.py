"""지식 기반 조회 — feed_item / kb_* 테이블 접근."""
from datetime import date
from typing import List, Optional

from app.db.database import get_connection
from app.models import FeedItem, InnovationCase, Kpi


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


# ─────────────── 혁신 사례 ───────────────

def _row_to_case(r) -> InnovationCase:
    return InnovationCase(
        id=r["id"], title=r["title"], category=r["category"] or "",
        background=r["background"] or "", effect=r["effect"] or "",
        kpi=Kpi(name=r["kpi_name"] or "-", formula=r["kpi_formula"] or "-"),
        sourceOrg=r["source_org"] or "", sourceType=r["source_type"] or "manual",
        sourceRef=r["source_ref"] or "", status=r["status"] or "approved",
        affiliates=r["affs"].split(",") if r["affs"] else [],
        createdAt=r["created_at"],
    )


_CASE_SELECT = """
    SELECT c.id, c.title, c.category, c.background, c.effect, c.kpi_name, c.kpi_formula,
           c.source_org, c.source_type, c.source_ref, c.status, c.created_at,
           GROUP_CONCAT(ca.aff_code) AS affs
    FROM kb_innovation_case c
    LEFT JOIN kb_case_affiliate ca ON ca.case_id = c.id
"""


def list_cases(status: Optional[str] = None, aff_code: Optional[str] = None) -> List[InnovationCase]:
    """혁신 사례 목록. status(approved/pending) 및 계열사로 선택 필터."""
    where, params = [], []
    if status:
        where.append("c.status = ?")
        params.append(status)
    if aff_code:
        where.append("c.id IN (SELECT case_id FROM kb_case_affiliate WHERE aff_code = ?)")
        params.append(aff_code)
    sql = _CASE_SELECT
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " GROUP BY c.id ORDER BY c.created_at DESC, c.id DESC"

    conn = get_connection()
    try:
        rows = conn.execute(sql, params).fetchall()
        return [_row_to_case(r) for r in rows]
    finally:
        conn.close()


def get_case(case_id: int) -> Optional[InnovationCase]:
    conn = get_connection()
    try:
        row = conn.execute(
            _CASE_SELECT + " WHERE c.id = ? GROUP BY c.id", (case_id,)
        ).fetchone()
        return _row_to_case(row) if row else None
    finally:
        conn.close()


def create_case(data: dict) -> InnovationCase:
    conn = get_connection()
    try:
        cur = conn.execute(
            """INSERT INTO kb_innovation_case
               (title, category, background, effect, kpi_name, kpi_formula,
                source_org, source_type, source_ref, status, created_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
            (data["title"], data.get("category"), data.get("background"), data.get("effect"),
             data.get("kpi_name"), data.get("kpi_formula"), data.get("source_org"),
             data.get("source_type", "manual"), data.get("source_ref"),
             data.get("status", "approved"), data.get("created_at")),
        )
        case_id = cur.lastrowid
        for aff in data.get("affiliates", []):
            conn.execute(
                "INSERT OR IGNORE INTO kb_case_affiliate(case_id, aff_code) VALUES (?,?)",
                (case_id, aff),
            )
        conn.commit()
    finally:
        conn.close()
    return get_case(case_id)


def set_case_status(case_id: int, status: str) -> bool:
    conn = get_connection()
    try:
        cur = conn.execute(
            "UPDATE kb_innovation_case SET status = ? WHERE id = ?", (status, case_id)
        )
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def delete_case(case_id: int) -> bool:
    conn = get_connection()
    try:
        # foreign_keys=ON + ON DELETE CASCADE 로 계열사 연결도 함께 삭제됨
        cur = conn.execute("DELETE FROM kb_innovation_case WHERE id = ?", (case_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()
