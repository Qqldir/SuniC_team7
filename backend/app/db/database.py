"""SQLite 커넥션 헬퍼."""
import sqlite3
from contextlib import contextmanager

from app.config import DB_PATH


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def ensure_auth_columns():
    """기존 DB(app_user)에 신규 컬럼이 없으면 추가 (idempotent 마이그레이션)."""
    conn = get_connection()
    try:
        info = conn.execute("PRAGMA table_info(app_user)").fetchall()
        cols = {r["name"] for r in info}
        if info and "is_admin" not in cols:
            conn.execute("ALTER TABLE app_user ADD COLUMN is_admin INTEGER NOT NULL DEFAULT 0")
            conn.commit()
    except Exception:
        pass
    finally:
        conn.close()


@contextmanager
def db_cursor(commit: bool = False):
    """with 블록용 커서. commit=True 면 정상 종료 시 커밋."""
    conn = get_connection()
    try:
        yield conn.cursor()
        if commit:
            conn.commit()
    finally:
        conn.close()
