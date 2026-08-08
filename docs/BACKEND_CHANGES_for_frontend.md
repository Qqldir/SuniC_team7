# 백엔드 반영 요청 — 프론트(`feat/frontend-redesign`)가 의존하는 변경 4건

> 대상: `roki_backend` 담당자
> 배경: 프론트 재작업 중, 로컬 worktree 백엔드에 아래 4가지를 임시로 추가해 화면을 붙였습니다.
> **실제 `roki_backend`(원격 PR)에는 아직 없습니다.** 이게 main에 반영되지 않으면
> 과제삭제 · 관리자권한변경 · 리포팅 발송기본값 · 관리자메뉴 노출이 프론트에서 깨집니다.
>
> 모두 `backend/app/` 하위 **코드 추가/수정만**이고, **DB 스키마 마이그레이션은 필요 없습니다**
> (아래 1·4의 전제조건이 현재 스키마에 이미 있습니다 — 근거는 각 항목에).

---

## 1. `DELETE /api/proposals/{id}` — 과제 1건 삭제 (신규 엔드포인트)

- **파일**: `app/api/proposals.py` (맨 끝에 추가)
- **인증**: `current_email` (로그인 사용자면 됨)
- **응답**: `{"ok": true, "id": <pid>}` / 없는 id면 404
- **전제조건(이미 충족)**: `proposal` 자식테이블(평가·기준값·수식·피드백 등)이 모두
  `REFERENCES proposal(id) ON DELETE CASCADE` 이고, 커넥션마다 `PRAGMA foreign_keys = ON`
  (`app/db/database.py`). → **CASCADE가 스키마에 이미 있어 별도 마이그레이션 불필요.**

```python
@router.delete("/{pid}")
def delete_proposal(pid: int, _: str = Depends(current_email)):
    """과제 1건 삭제. 관련 평가·기준값·수식·피드백은 ON DELETE CASCADE 로 함께 지워진다."""
    _must_exist(pid)
    conn = get_connection()
    try:
        conn.execute("DELETE FROM proposal WHERE id = ?", (pid,))
        conn.commit()
    finally:
        conn.close()
    return {"ok": True, "id": pid}
```

---

## 2. `POST /api/admin/users/{email}/admin` — 기존 계정 관리자 권한 토글 (신규 엔드포인트)

- **파일**: `app/api/admin.py`
- **인증**: `current_admin` (관리자 전용)
- **요청 body**: `{"is_admin": true|false}` (embed)
- **응답**: `{"ok": true, "email": ..., "is_admin": bool}` / 없는 계정 404
- **import 추가 필요**: `from fastapi import ... Body ...` (기존 import 줄에 `Body` 추가)
- **전제조건(이미 충족)**: `app_user.is_admin` 컬럼 존재(기존 `GET /api/admin/users`가 이미 SELECT 중).

```python
# 상단 import 에 Body 추가
from fastapi import APIRouter, Body, Depends, File, Form, HTTPException, UploadFile

@router.post("/users/{email}/admin")
def set_user_admin(email: str, is_admin: bool = Body(..., embed=True), _: str = Depends(current_admin)):
    """기존 계정의 관리자 권한을 켜거나 끈다."""
    email = email.strip().lower()
    conn = get_connection()
    try:
        n = conn.execute(
            "UPDATE app_user SET is_admin = ? WHERE email = ?",
            (int(is_admin), email),
        ).rowcount
        conn.commit()
    finally:
        conn.close()
    if n == 0:
        raise HTTPException(status_code=404, detail="해당 계정을 찾을 수 없습니다.")
    return {"ok": True, "email": email, "is_admin": bool(is_admin)}
```

---

## 3. AI Reporting 발송주기 기본값 `"매일"` → `"발송 안함"`

- **파일**: `app/store.py` — 모듈 상수 한 줄
- **이유**: 신규 사용자에게 리포트가 자동 발송되지 않도록 기본값을 opt-in 으로.

```python
# 변경 전
DEFAULT_REPORT = {"freq": "매일", "time": "08:00", "lastAt": ""}
# 변경 후
DEFAULT_REPORT = {"freq": "발송 안함", "time": "08:00", "lastAt": ""}
```

---

## 4. `GET /api/bootstrap` 의 `user` 에 `is_admin` 추가 ★ 이번에 새로 추가된 항목

- **파일**: `app/store.py`
- **이유**: 프론트가 **사이드바 '관리자' 메뉴 노출**을 이 값으로 판단.
  없으면(=falsy) **관리자 메뉴가 아무에게도 안 뜹니다.**
- **전제조건(이미 충족)**: `app_user.is_admin` 컬럼 존재. 헬퍼는 컬럼 없는 옛 DB에서도 안 죽게 방어.

```python
# bootstrap() 정의 위에 헬퍼 추가
def _is_admin(conn, email: str) -> bool:
    """토큰 주인이 관리자인지. bootstrap 의 user.is_admin 으로 내려, 화면이 사이드바
    '관리자' 메뉴 노출을 결정한다. is_admin 컬럼이 없는 옛 DB 여도 죽지 않게 방어한다."""
    try:
        row = conn.execute(
            "SELECT is_admin FROM app_user WHERE email = ?", (email,)
        ).fetchone()
    except Exception:
        return False
    return bool(row["is_admin"]) if row and "is_admin" in row.keys() else False


# bootstrap() 반환 dict 의 user 키
# 변경 전
            "user": {"email": email},
# 변경 후
            "user": {"email": email, "is_admin": _is_admin(conn, email)},
```


