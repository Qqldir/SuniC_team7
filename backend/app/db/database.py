"""SQLite 커넥션 헬퍼."""
import sqlite3

from app.config import DB_PATH


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# ★ with 블록용 자동 커밋 커서를 추가하지 마라. 커넥션을 직접 받아 커밋 시점을
#   호출자가 잡는 형태(get_connection + try/finally)로 통일돼 있고, 재생성·저장 경로는
#   여러 함수가 **같은 트랜잭션**을 공유해야 해서 with 단위 자동 커밋과 맞지 않는다.
