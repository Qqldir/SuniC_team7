"""외부 동향 조회 API."""
from fastapi import APIRouter

from app.pipeline.knowledge import repository as kb

router = APIRouter(prefix="/api/feed", tags=["feed"])


@router.get("")
def list_feed():
    """지식 파밍 결과(feed_item) 전체를 프론트 데이터 형태로 반환."""
    return {"feed": [it.model_dump() for it in kb.all_feed()]}
