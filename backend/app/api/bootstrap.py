"""화면 초기 데이터 — trendroom.html 이 뜰 때 한 번 호출한다.

프론트가 상수로 들고 있던 OC·레버·테마·근거자료·과제·소스·권한과
로그인 사용자별 작업 상태(평가·기준값·수식·발송설정)를 한 번에 내려준다.
"""
from fastapi import APIRouter, Depends

from app import store
from app.api.deps import current_email

router = APIRouter(prefix="/api", tags=["bootstrap"])


@router.get("/bootstrap")
def get_bootstrap(email: str = Depends(current_email)):
    return store.bootstrap(email)
