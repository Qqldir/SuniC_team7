"""비밀번호 해시 + 로그인 토큰 — 표준 라이브러리만 사용.

- 비밀번호: pbkdf2_sha256 (per-user salt) 로 해시 저장, 평문 저장 안 함.
- 토큰: 'payload.signature' (payload=email|만료시각, HMAC-SHA256 서명). 서버 상태 불필요.
"""
import base64
import hashlib
import hmac
import os
import time

from app.config import AUTH_SECRET, AUTH_TTL_HOURS

_ITER = 200_000


def hash_password(pw: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, _ITER)
    return f"pbkdf2_sha256${_ITER}${salt.hex()}${dk.hex()}"


def verify_password(pw: str, stored: str) -> bool:
    try:
        _algo, iter_s, salt_hex, hash_hex = stored.split("$")
        dk = hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt_hex), int(iter_s))
        return hmac.compare_digest(dk.hex(), hash_hex)
    except Exception:
        return False


def _b64(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode().rstrip("=")


def _unb64(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def make_token(email: str, ttl_hours: int | None = None) -> str:
    exp = int(time.time()) + (ttl_hours or AUTH_TTL_HOURS) * 3600
    payload = f"{email}|{exp}"
    sig = hmac.new(AUTH_SECRET.encode(), payload.encode(), hashlib.sha256).digest()
    return f"{_b64(payload.encode())}.{_b64(sig)}"


def verify_token(token: str):
    """유효하면 email, 아니면 None."""
    try:
        p_b64, sig_b64 = token.split(".")
        payload = _unb64(p_b64).decode()
        expected = hmac.new(AUTH_SECRET.encode(), payload.encode(), hashlib.sha256).digest()
        if not hmac.compare_digest(_unb64(sig_b64), expected):
            return None
        email, exp = payload.rsplit("|", 1)
        if int(exp) < int(time.time()):
            return None
        return email
    except Exception:
        return None
