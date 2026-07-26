"""과제 기록 CRUD API."""
import time

from fastapi import APIRouter

from app.db.database import get_connection
from app.models import TaskIn, TaskOut, DeleteRequest

router = APIRouter(prefix="/api/tasks", tags=["tasks"])


def _row_to_task(conn, r) -> TaskOut:
    ev = conn.execute(
        "SELECT feed_id FROM task_evidence WHERE task_id = ?", (r["id"],)
    ).fetchall()
    return TaskOut(
        id=r["id"], createdAt=r["created_at"], aff=r["aff_code"], title=r["title"],
        category=r["category"] or "", background=r["background"] or "", plan=r["plan"] or "",
        risk=r["risk"] or "", effect=r["effect"] or "",
        kpiName=r["kpi_name"] or "-", kpiFormula=r["kpi_formula"] or "-",
        status=r["status"] or "검토중", origin=r["origin"] or "생성",
        evidence=[e["feed_id"] for e in ev],
    )


@router.get("")
def list_tasks():
    conn = get_connection()
    try:
        rows = conn.execute("SELECT * FROM task ORDER BY created_at DESC, rowid DESC").fetchall()
        return {"tasks": [_row_to_task(conn, r).model_dump() for r in rows]}
    finally:
        conn.close()


@router.post("")
def create_task(task: TaskIn):
    task_id = task.id or ("OI-" + str(int(time.time() * 1000))[-6:])
    conn = get_connection()
    try:
        conn.execute(
            """INSERT INTO task
               (id, created_at, aff_code, title, category, background, plan,
                risk, effect, kpi_name, kpi_formula, status, origin)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (task_id, task.createdAt, task.aff, task.title, task.category,
             task.background, task.plan, task.risk, task.effect,
             task.kpiName, task.kpiFormula, task.status, task.origin),
        )
        for feed_id in task.evidence:
            conn.execute(
                "INSERT OR IGNORE INTO task_evidence(task_id, feed_id) VALUES (?,?)",
                (task_id, feed_id),
            )
        conn.commit()
        row = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,)).fetchone()
        return {"task": _row_to_task(conn, row).model_dump()}
    finally:
        conn.close()


@router.delete("")
def delete_tasks(req: DeleteRequest):
    if not req.ids:
        return {"deleted": 0}
    conn = get_connection()
    try:
        placeholders = ",".join("?" for _ in req.ids)
        cur = conn.execute(f"DELETE FROM task WHERE id IN ({placeholders})", req.ids)
        conn.commit()
        return {"deleted": cur.rowcount}
    finally:
        conn.close()
