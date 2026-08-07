"""외부 동향 조회 API — 지식 파밍 품질 점검용.

용도: 크롤러·LLM 정제(pipeline/farming/*)가 feed_item 에 무엇을 넣었는지 원본 형태로
확인한다. 화면(trendroom.html)은 이 경로를 쓰지 않는다 — 화면이 쓰는 근거 자료는
GET /api/bootstrap 의 evidence(표시용 라벨·지표만 추린 형태)다.
그래서 파밍을 돌린 뒤 "정제가 실제로 붙었는가"(enriched·importance·levers·reason)를
보려면 여기가 유일한 HTTP 경로다.

★ 인증을 붙였다. feed_item 에는 사내 자료 요약과 원문 URL 이 들어 있는데, 이 라우트만
  인증이 없어 토큰 없이 전량을 받아 갈 수 있었다(다른 모든 API 는 Bearer 필수).
"""
from fastapi import APIRouter, Depends

from app.api.deps import current_email
from app.pipeline.knowledge import repository as kb

router = APIRouter(prefix="/api/feed", tags=["feed"])


@router.get("")
def list_feed(_: str = Depends(current_email)):
    """지식 파밍 결과(feed_item) 전체를 프론트 데이터 형태로 반환."""
    return {"feed": [it.model_dump() for it in kb.all_feed()]}
