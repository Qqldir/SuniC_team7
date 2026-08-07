"""로그인 / 계정 관리 API.

- POST   /api/auth/login            {email, password}        → {token, email}
- GET    /api/auth/me               (Bearer)                 → {email}
- POST   /api/auth/change-password  (Bearer) {current,new}   → {ok}
- DELETE /api/auth/me               (Bearer)                 → {ok}  (탈퇴)
"""
from fastapi import APIRouter, Depends, HTTPException

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


# 탈퇴 시 함께 지우는 사용자별 테이블. 전부 user_email 컬럼을 가진다.
#
# ★ proposal_feedback_log 는 **일부러 뺐다.** 별점 이력 + 당시 과제 스냅샷(학습 데이터)이라
#   FK 도 걸지 않았고, 탈퇴해도 남아야 하는 값이다. 여기에 추가하면 축적된 학습 신호가
#   계정 하나 지울 때마다 날아간다(발굴 프롬프트의 [현업 평가 이력] 블록이 이걸 읽는다).
#   되살리고 싶다면 익명화(user_email 을 해시로)를 먼저 설계할 것.
# ★ report_recipient 는 PK 가 (user_email, label) 이라 다른 테이블과 컬럼이 다르지만
#   삭제 조건은 같다.
_USER_TABLES = [
    "proposal_feedback", "proposal_input", "proposal_formula",
    "report_exclude", "report_recipient", "report_setting",
]


@router.delete("/me")
def withdraw(email: str = Depends(current_email)):
    """탈퇴 — 계정과 그 계정의 개인 데이터를 **한 트랜잭션으로** 함께 지운다.

    ★ 예전에는 app_user 만 지웠다. app_user.email 을 참조하는 FK 가 하나도 없어서
      (사용자별 테이블은 email 을 그냥 TEXT 로 들고 있다) CASCADE 가 돌지 않고,
      별점·기준값·산출식·발송설정이 고아 행으로 남았다. 같은 이메일로 다시 계정을
      만들면 남의 것이 아니라 **예전 자기 데이터가 되살아나** 붙는다.
    ★ 한 트랜잭션이어야 한다. 중간에 실패하면 계정만 지워지고 개인 데이터가 남는
      상태가 되므로, 전부 성공하거나 전부 되돌아가야 한다.
    """
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        for table in _USER_TABLES:
            conn.execute(f"DELETE FROM {table} WHERE user_email = ?", (email,))
        conn.execute("DELETE FROM app_user WHERE email = ?", (email,))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return {"ok": True}
