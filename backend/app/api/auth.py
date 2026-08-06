"""로그인 / 계정 관리 API.

- POST   /api/auth/login            {email, password}        → {token, email}
- GET    /api/auth/me               (Bearer)                 → {email}
- POST   /api/auth/change-password  (Bearer) {current,new}   → {ok}
- DELETE /api/auth/me               (Bearer)                 → {ok}  (탈퇴)
"""
from fastapi import APIRouter, Header, HTTPException

from app.db.database import get_connection
from app.models import LoginIn, ChangePwIn
from app.security import hash_password, verify_password, make_token, verify_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _current_email(authorization: str | None) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")
    email = verify_token(authorization.split(" ", 1)[1])
    if not email:
        raise HTTPException(status_code=401, detail="세션이 만료되었거나 올바르지 않습니다.")
    return email


@router.post("/login")
def login(body: LoginIn):
    email = body.email.strip().lower()
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM app_user WHERE email = ?", (email,)).fetchone()
    finally:
        conn.close()
    if not row or not row["is_active"] or not verify_password(body.password, row["password_hash"]):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 올바르지 않습니다.")
    return {"token": make_token(email), "email": email}


@router.get("/me")
def me(authorization: str | None = Header(default=None)):
    return {"email": _current_email(authorization)}


@router.post("/change-password")
def change_password(body: ChangePwIn, authorization: str | None = Header(default=None)):
    email = _current_email(authorization)
    if len(body.new_password) < 4:
        raise HTTPException(status_code=400, detail="새 비밀번호는 4자 이상이어야 합니다.")
    conn = get_connection()
    try:
        row = conn.execute("SELECT password_hash FROM app_user WHERE email = ?", (email,)).fetchone()
        if not row or not verify_password(body.current_password, row["password_hash"]):
            raise HTTPException(status_code=400, detail="현재 비밀번호가 올바르지 않습니다.")
        conn.execute(
            "UPDATE app_user SET password_hash = ? WHERE email = ?",
            (hash_password(body.new_password), email),
        )
        conn.commit()
    finally:
        conn.close()
    return {"ok": True}


@router.delete("/me")
def withdraw(authorization: str | None = Header(default=None)):
    email = _current_email(authorization)
    conn = get_connection()
    try:
        conn.execute("DELETE FROM app_user WHERE email = ?", (email,))
        conn.commit()
    finally:
        conn.close()
    return {"ok": True}
