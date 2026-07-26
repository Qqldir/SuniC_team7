"""DB 초기화 + 데모 데이터 주입.

    python -m app.db.seed          # 스키마 생성 후 마스터/피드 시드
    python -m app.db.seed --reset  # 기존 DB 삭제 후 재생성
"""
import sys
from pathlib import Path

from app.config import DB_PATH
from app.db.database import get_connection
from app.db import seed_data as S

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def create_schema(conn):
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def seed_master(conn):
    conn.executemany("INSERT OR REPLACE INTO biz_segment(key,label,color) VALUES (?,?,?)", S.BIZ)
    conn.executemany("INSERT OR REPLACE INTO affiliate(code,name,biz) VALUES (?,?,?)", S.AFFILIATES)
    conn.executemany("INSERT OR REPLACE INTO source_kind(key,label,css_class) VALUES (?,?,?)", S.SOURCE_KINDS)


def seed_feed(conn):
    for fid, pub, kind, source, title, summary, tags in S.FEED:
        conn.execute(
            "INSERT OR REPLACE INTO feed_item(id,published_on,kind,source,title,summary) VALUES (?,?,?,?,?,?)",
            (fid, pub, kind, source, title, summary),
        )
        for aff in tags:
            conn.execute(
                "INSERT OR REPLACE INTO feed_item_tag(feed_id,aff_code) VALUES (?,?)",
                (fid, aff),
            )


def main():
    if "--reset" in sys.argv:
        p = Path(DB_PATH)
        if p.exists():
            p.unlink()
            print(f"삭제됨: {DB_PATH}")

    conn = get_connection()
    try:
        create_schema(conn)
        seed_master(conn)
        seed_feed(conn)
        conn.commit()
        n_feed = conn.execute("SELECT COUNT(*) FROM feed_item").fetchone()[0]
        n_aff = conn.execute("SELECT COUNT(*) FROM affiliate").fetchone()[0]
        print(f"완료: {DB_PATH}")
        print(f"  계열사 {n_aff}개 · 외부 동향 {n_feed}건 주입")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
