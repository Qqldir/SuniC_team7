"""라우터 공용 의존성 — 요청자 식별 · 권한."""
from fastapi import Depends, Header, HTTPException

from app.db.database import get_connection
from app.security import verify_token


def current_email(authorization: str | None = Header(default=None)) -> str:
    """Bearer 토큰에서 로그인 이메일을 꺼낸다. 없거나 만료면 401."""
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")
    email = verify_token(authorization.split(" ", 1)[1])
    if not email:
        raise HTTPException(status_code=401, detail="세션이 만료되었거나 올바르지 않습니다.")
    return email


def current_admin(email: str = Depends(current_email)) -> str:
    """관리자 계정만 통과시킨다. 아니면 403.

    ★ 401(비로그인)과 403(권한 없음)의 계층을 반드시 지킨다 — 화면의 계정 관리 탭이
      403 만 특별 취급해 '관리자 권한이 있는 계정만…' 을 띄우고, 그 외 실패는 전부
      '목록을 불러오지 못했습니다.' 라는 뭉뚱그린 메시지가 된다.
    ★ SELECT * + row.keys() 방어는 의도적이다. 마이그레이션이 안 돈 DB 에서
      `SELECT is_admin` 은 OperationalError → 500 이 되어 프론트가 403 분기를 못 탄다.
      컬럼이 없으면 조용히 403 으로 떨어뜨리는 편이 화면 메시지가 정확하다.
      (auth.login 도 같은 이유로 SELECT * 를 쓴다.)
    """
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM app_user WHERE email = ?", (email,)).fetchone()
    finally:
        conn.close()
    if not row or "is_admin" not in row.keys() or not row["is_admin"]:
        raise HTTPException(status_code=403, detail="관리자 권한이 필요합니다.")
    return email
