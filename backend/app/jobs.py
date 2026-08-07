"""오래 걸리는 작업을 백그라운드로 돌리고 상태를 DB 에 남긴다.

LLM 발굴은 계열사 1곳당 1분 내외(codex medium 실측 58~62초)라 HTTP 응답으로
붙잡고 있을 수 없다 — nginx 기본 proxy_read_timeout 이 60초, Cloudflare 가 100초다.
그래서 요청은 작업을 만들고 즉시 id 를 돌려주고, 화면이 상태를 폴링한다.

상태를 프로세스 메모리가 아니라 `job` 테이블에 두는 이유는 uvicorn 워커가 여럿일 때
폴링 요청이 작업을 시작한 워커로 간다는 보장이 없기 때문이다.
(작업 자체는 시작한 프로세스의 스레드에서 돈다 — 그 프로세스가 죽으면 running 인 채로
남으므로, 조회 측에서 STALE_AFTER 를 넘긴 작업은 실패로 본다.)
"""
import json
import logging
import secrets
import threading
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, Optional

from app.db.database import get_connection

log = logging.getLogger(__name__)

# 이 시간을 넘도록 running 인 작업은 프로세스가 죽은 것으로 보고 실패 처리한다.
STALE_AFTER = timedelta(minutes=15)


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def create(kind: str) -> str:
    job_id = secrets.token_urlsafe(9)
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO job(id, kind, status, created_at) VALUES (?,?,'running',?)",
            (job_id, kind, _now()),
        )
        conn.commit()
    finally:
        conn.close()
    return job_id


def _finish(job_id: str, status: str, result: Any = None, error: str = "") -> None:
    conn = get_connection()
    try:
        conn.execute(
            "UPDATE job SET status = ?, result = ?, error = ?, finished_at = ? WHERE id = ?",
            (status, json.dumps(result, ensure_ascii=False) if result is not None else None,
             error, _now(), job_id),
        )
        conn.commit()
    finally:
        conn.close()


def start(kind: str, fn: Callable[[], Any]) -> str:
    """작업을 만들고 별도 스레드에서 fn 을 돌린다. 즉시 작업 id 를 돌려준다."""
    job_id = create(kind)

    def run():
        try:
            _finish(job_id, "done", fn())
        except Exception as e:                     # noqa: BLE001 — 작업 실패는 상태로 남긴다
            log.exception("작업 실패: %s", kind)
            _finish(job_id, "failed", None, f"{type(e).__name__}: {e}"[:300])

    threading.Thread(target=run, name=f"job-{kind}-{job_id}", daemon=True).start()
    return job_id


def get(job_id: str) -> Optional[Dict[str, Any]]:
    """작업 상태. 없으면 None.

    완료된 작업은 result 를 그대로 펼쳐 돌려준다 — 화면이 동기 응답과 같은 모양을
    받도록 해서 호출 측 분기를 줄인다.
    """
    conn = get_connection()
    try:
        r = conn.execute(
            "SELECT id, kind, status, result, error, created_at, finished_at "
            "FROM job WHERE id = ?", (job_id,)
        ).fetchone()
    finally:
        conn.close()
    if not r:
        return None

    status, error = r["status"], r["error"] or ""
    if status == "running":
        try:
            started = datetime.fromisoformat(r["created_at"])
        except ValueError:
            started = datetime.now()
        if datetime.now() - started > STALE_AFTER:
            # 작업을 돌리던 프로세스가 죽었다. 영원히 '생성 중' 으로 두지 않는다.
            status, error = "failed", "작업이 중단되었습니다. 다시 시도해 주세요."
            _finish(job_id, status, None, error)

    out: Dict[str, Any] = {"job": r["id"], "status": status, "error": error}
    if status == "done" and r["result"]:
        try:
            payload = json.loads(r["result"])
        except ValueError:
            payload = None
        if isinstance(payload, dict):
            out.update(payload)
    return out
