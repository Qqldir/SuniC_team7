"""라우터 공용 의존성 — 요청자 식별."""
from fastapi import Header, HTTPException

from app.security import verify_token


def current_email(authorization: str | None = Header(default=None)) -> str:
    """Bearer 토큰에서 로그인 이메일을 꺼낸다. 없거나 만료면 401."""
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="인증이 필요합니다.")
    email = verify_token(authorization.split(" ", 1)[1])
    if not email:
        raise HTTPException(status_code=401, detail="세션이 만료되었거나 올바르지 않습니다.")
    return email
