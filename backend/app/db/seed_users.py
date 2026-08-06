"""관리자용 사용자 계정 시드 — 초기 비밀번호는 해시로 저장(기본 1111).

    python -m app.db.seed_users                        # 기본 데모 계정 생성
    python -m app.db.seed_users a@sk.com b@sk.com      # 지정 이메일 생성
    python -m app.db.seed_users --pw 0000 a@sk.com     # 초기 비밀번호 지정
    python -m app.db.seed_users --reset-pw a@sk.com    # 기존 계정 비밀번호도 초기화
    python -m app.db.seed_users --file emails.txt      # 파일(한 줄에 하나)에서 읽기

기존 계정은 기본적으로 건너뜁니다(비밀번호 보존). --reset-pw 로 초기화.
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

from app.db.database import get_connection, ensure_auth_columns
from app.security import hash_password

SCHEMA_PATH = Path(__file__).with_name("schema.sql")

# 데모용 기본 계정 (실제로는 관리자가 이메일 목록을 넘겨줌)
DEFAULT_USERS = [
    "admin@sk.com",
    "user1@sk.com",
    "user2@sk.com",
]
# 기본 관리자 (사용자 관리 권한). --admin 으로 추가 지정 가능.
DEFAULT_ADMINS = {"admin@sk.com"}


def ensure_table(conn):
    # app_user 테이블 생성(CREATE IF NOT EXISTS) + 기존 DB 컬럼 마이그레이션
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.commit()
    ensure_auth_columns()


def parse_args(argv):
    pw, reset, emails, admins = "1111", False, [], set()
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--pw":
            pw = argv[i + 1]; i += 2; continue
        if a == "--reset-pw":
            reset = True; i += 1; continue
        if a == "--admin":
            admins.add(argv[i + 1].strip().lower()); i += 2; continue
        if a == "--file":
            emails += Path(argv[i + 1]).read_text(encoding="utf-8").split(); i += 2; continue
        emails.append(a); i += 1
    emails = [e.strip().lower() for e in (emails or DEFAULT_USERS) if e.strip()]
    # --admin 지정이 있으면 그걸, 없으면 기본 관리자. 실제 시드하는 이메일과 교집합만.
    admins = (admins or set(DEFAULT_ADMINS)) & set(emails)
    return pw, reset, emails, admins


def main(argv):
    pw, reset, emails, admins = parse_args(argv)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    try:
        ensure_table(conn)
        created, skipped, reseted = [], [], []
        for e in emails:
            adm = 1 if e in admins else 0
            exists = conn.execute("SELECT 1 FROM app_user WHERE email = ?", (e,)).fetchone()
            if exists:
                # 관리자 지정은 항상 반영 (기존 계정도 승격)
                if adm:
                    conn.execute("UPDATE app_user SET is_admin = 1 WHERE email = ?", (e,))
                if reset:
                    conn.execute(
                        "UPDATE app_user SET password_hash = ?, is_active = 1 WHERE email = ?",
                        (hash_password(pw), e),
                    )
                    reseted.append(e)
                else:
                    skipped.append(e)
            else:
                conn.execute(
                    "INSERT INTO app_user(email, password_hash, is_active, is_admin, created_at) VALUES (?,?,1,?,?)",
                    (e, hash_password(pw), adm, now),
                )
                created.append(e)
        conn.commit()
    finally:
        conn.close()

    print(f"[seed_users] 생성 {len(created)}건: {created}")
    if reseted:
        print(f"[seed_users] 비밀번호 초기화 {len(reseted)}건: {reseted}")
    if skipped:
        print(f"[seed_users] 이미 존재해 건너뜀 {len(skipped)}건: {skipped}  (--reset-pw 로 초기화 가능)")
    print(f"[seed_users] 관리자: {sorted(admins)}")
    print(f"[seed_users] 초기 비밀번호: {pw!r}")


if __name__ == "__main__":
    main(sys.argv[1:])
