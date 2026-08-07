"""관리자용 사용자 계정 시드 — 초기 비밀번호는 해시로 저장(기본 1111).

    python -m app.db.seed_users                        # 기본 데모 계정 생성
    python -m app.db.seed_users a@sk.com b@sk.com      # 지정 이메일 생성
    python -m app.db.seed_users --pw 0000 a@sk.com     # 초기 비밀번호 지정
    python -m app.db.seed_users --reset-pw a@sk.com    # 기존 계정 비밀번호도 초기화
    python -m app.db.seed_users --file emails.txt      # 파일(한 줄에 하나)에서 읽기
    python -m app.db.seed_users --admin admin@sk.com   # 관리자로 지정(기존 계정도 승격)

기존 계정은 기본적으로 건너뜁니다(비밀번호 보존). --reset-pw 로 초기화.
--admin 만은 예외로 기존 계정도 그 자리에서 is_admin=1 로 승격합니다 —
관리자를 만드는 유일한 API(POST /api/admin/users)가 관리자 권한 뒤에 있어서,
승격 경로가 없으면 아무도 관리자가 될 수 없는 데드락이 됩니다.
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

from app.db.database import get_connection
from app.security import hash_password


# 데모용 기본 계정 (실제로는 관리자가 이메일 목록을 넘겨줌)
DEFAULT_USERS = [
    "admin@sk.com",
    "user1@sk.com",
    "user2@sk.com",
]

# --admin 을 하나도 안 주면 이 계정이 관리자가 된다.
# ★ 기본값이 없으면 새 DB 를 시드한 직후 관리자가 0명이라 계정 관리 탭이 전원 403 이 된다.
DEFAULT_ADMINS = {"admin@sk.com"}


def ensure_table(conn):
    # app_user 테이블이 없으면 스키마로 생성 (CREATE IF NOT EXISTS 라 기존 데이터 안전).
    #
    # seed.create_schema 를 그대로 쓴다 — schema.sql 을 직접 executescript 하면 안 된다.
    # 인덱스 일부가 나중에 추가된 컬럼(proposal.name_key 등)을 참조하므로, 마이그레이션이
    # 안 된 기존 DB 에서는 "no such column" 으로 죽는다. create_schema 는 마이그레이션을
    # 먼저 돌리므로 새 DB·기존 DB 양쪽에서 안전하다.
    from app.db.seed import create_schema

    create_schema(conn)


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
            # --admin 은 대상 지정이자 계정 지정이다 — 목록에 없던 이메일이면 함께 생성한다.
            m = argv[i + 1].strip().lower()
            admins.add(m); emails.append(m); i += 2; continue
        if a == "--file":
            emails += Path(argv[i + 1]).read_text(encoding="utf-8").split(); i += 2; continue
        emails.append(a); i += 1
    emails = [e.strip().lower() for e in (emails or DEFAULT_USERS) if e.strip()]
    # 목록에 없는 이메일을 관리자로 지정할 수는 없다(계정이 없으니 승격할 대상도 없다).
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
            exists = conn.execute("SELECT 1 FROM app_user WHERE email = ?", (e,)).fetchone()
            if exists:
                if reset:
                    conn.execute(
                        "UPDATE app_user SET password_hash = ?, is_active = 1 WHERE email = ?",
                        (hash_password(pw), e),
                    )
                    reseted.append(e)
                else:
                    skipped.append(e)
                # ★ 승격은 --reset-pw 와 무관하게 항상 한다. is_admin 이 나중에 추가된
                #   컬럼이라 기존 계정은 전부 0 으로 시작하는데, 비밀번호를 건드리지
                #   않고서는 관리자를 만들 수 없다면 이 CLI 로도 데드락을 못 푼다.
                if e in admins:
                    conn.execute("UPDATE app_user SET is_admin = 1 WHERE email = ?", (e,))
            else:
                conn.execute(
                    "INSERT INTO app_user(email, password_hash, is_active, is_admin, created_at) "
                    "VALUES (?,?,1,?,?)",
                    (e, hash_password(pw), 1 if e in admins else 0, now),
                )
                created.append(e)
        conn.commit()
    finally:
        conn.close()

    print(f"[seed_users] 생성 {len(created)}건: {created}")
    if admins:
        print(f"[seed_users] 관리자 {len(admins)}건: {sorted(admins)}")
    if reseted:
        print(f"[seed_users] 비밀번호 초기화 {len(reseted)}건: {reseted}")
    if skipped:
        print(f"[seed_users] 이미 존재해 건너뜀 {len(skipped)}건: {skipped}  (--reset-pw 로 초기화 가능)")
    print(f"[seed_users] 초기 비밀번호: {pw!r}")


if __name__ == "__main__":
    main(sys.argv[1:])
