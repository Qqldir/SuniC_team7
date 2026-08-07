"""로그인 / 계정 관리 API.

- POST   /api/auth/login            {email, password}        → {token, email}
- GET    /api/auth/me               (Bearer)                 → {email}
- POST   /api/auth/change-password  (Bearer) {current,new}   → {ok}
- DELETE /api/auth/me               (Bearer)                 → {ok}  (탈퇴)
"""
from fastapi import APIRouter, Depends, HTTPException

from app import store
from app.api.deps import current_email
from app.db.database import get_connection
from app.models import LoginIn, ChangePwIn
from app.security import hash_password, verify_password, make_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


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
def me(email: str = Depends(current_email)):
    return {"email": email}


@router.post("/change-password")
def change_password(body: ChangePwIn, email: str = Depends(current_email)):
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
def withdraw(email: str = Depends(current_email)):
    """탈퇴 — 계정과 그 계정의 개인 데이터를 **한 트랜잭션으로** 함께 지운다.

    삭제 범위는 store.purge_user 한 곳에 있다 — 관리자 삭제
    (DELETE /api/admin/users/{email})와 같은 범위여야 하기 때문이다.
    범위를 바꿀 일이 있으면 store.USER_TABLES 를 고쳐라.

    ★ 한 트랜잭션이어야 한다. 중간에 실패하면 계정만 지워지고 개인 데이터가 남는
      상태가 되므로, 전부 성공하거나 전부 되돌아가야 한다.
    """
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        store.purge_user(conn, email)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return {"ok": True}
