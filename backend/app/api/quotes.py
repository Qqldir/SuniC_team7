"""관심 종목 시세 API — 화면 상단 티커가 쓴다.

bootstrap 에 싣지 않은 이유: bootstrap 은 화면이 뜰 때 한 번 받는 무거운 묶음(약 145KB)이고
계정별 작업 상태까지 들어 있어 캐시 수명이 짧다. 시세는 하루 1회만 바뀌는 외부 값이라
수명이 전혀 다르다. 같이 묶으면 티커 때문에 bootstrap 이 외부 API 응답을 기다리게 되고,
외부가 죽으면 화면 전체가 못 뜬다. 그래서 분리하고, 프론트는 이 호출을 **비동기로**
따로 던진다(실패해도 화면은 이미 떠 있다).
"""
from fastapi import APIRouter, Depends

from app import market
from app.api.deps import current_email

router = APIRouter(prefix="/api/quotes", tags=["quotes"])


@router.get("")
def get_quotes(_: str = Depends(current_email)):
    """관심 종목 최신 영업일 종가. 실패해도 200 이고 close=null 로 내려간다.

    ★ 500 을 던지지 않는다. 시세는 화면의 곁가지라, 외부 API 사정으로 에러를 올리면
      프론트가 티커 하나 때문에 오류 처리를 해야 한다. 값이 없다는 사실은
      close=null 과 stale 플래그로 충분히 전달된다.
    """
    return market.quotes()
