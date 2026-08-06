"""관리자 전용 사용자 관리 API. (관리자 토큰 필요)

- GET    /api/admin/users                        → {users:[...]}
- POST   /api/admin/users        {email,password?,is_admin?}  → 계정 생성
- POST   /api/admin/users/{email}/reset-password → 비밀번호 1111 로 초기화
- DELETE /api/admin/users/{email}                → 계정 삭제
"""
from datetime import datetime, timezone

from fastapi import APIRouter, Header, HTTPException

from app.db.database import get_connection
from app.models import AdminUserIn
from app.security import verify_token, hash_password

router = APIRouter(prefix="/api/admin", tags=["admin"])


def _require_admin(authorization: str | None) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")
    email = verify_token(authorization.split(" ", 1)[1])
    if not email:
        raise HTTPException(status_code=401, detail="세션이 만료되었거나 올바르지 않습니다.")
    conn = get_connection()
    try:
        row = conn.execute("SELECT is_admin FROM app_user WHERE email = ?", (email,)).fetchone()
    finally:
        conn.close()
    if not row or not row["is_admin"]:
        raise HTTPException(status_code=403, detail="관리자 권한이 필요합니다.")
    return email


@router.get("/users")
def list_users(authorization: str | None = Header(default=None)):
    _require_admin(authorization)
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT email, is_active, is_admin, created_at FROM app_user ORDER BY is_admin DESC, created_at"
        ).fetchall()
        return {"users": [dict(r) for r in rows]}
    finally:
        conn.close()


@router.post("/users")
def create_user(body: AdminUserIn, authorization: str | None = Header(default=None)):
    _require_admin(authorization)
    email = body.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="올바른 이메일을 입력하세요.")
    pw = body.password or "1111"
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    conn = get_connection()
    try:
        if conn.execute("SELECT 1 FROM app_user WHERE email = ?", (email,)).fetchone():
            raise HTTPException(status_code=400, detail="이미 존재하는 계정입니다.")
        conn.execute(
            "INSERT INTO app_user(email, password_hash, is_active, is_admin, created_at) VALUES (?,?,1,?,?)",
            (email, hash_password(pw), 1 if body.is_admin else 0, now),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "email": email, "initial_password": pw}


@router.post("/users/{email}/reset-password")
def reset_password(email: str, authorization: str | None = Header(default=None)):
    _require_admin(authorization)
    email = email.strip().lower()
    conn = get_connection()
    try:
        if not conn.execute("SELECT 1 FROM app_user WHERE email = ?", (email,)).fetchone():
            raise HTTPException(status_code=404, detail="계정을 찾을 수 없습니다.")
        conn.execute(
            "UPDATE app_user SET password_hash = ?, is_active = 1 WHERE email = ?",
            (hash_password("1111"), email),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "email": email, "initial_password": "1111"}


@router.delete("/users/{email}")
def delete_user(email: str, authorization: str | None = Header(default=None)):
    admin = _require_admin(authorization)
    email = email.strip().lower()
    if email == admin:
        raise HTTPException(status_code=400, detail="본인 계정은 삭제할 수 없습니다.")
    conn = get_connection()
    try:
        conn.execute("DELETE FROM app_user WHERE email = ?", (email,))
        conn.commit()
    finally:
        conn.close()
    return {"ok": True}
