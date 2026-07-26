"""SQLite 커넥션 헬퍼."""
import sqlite3
from contextlib import contextmanager

from app.config import DB_PATH


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


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
