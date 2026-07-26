"""과제 발굴 API."""
from fastapi import APIRouter, HTTPException

from app.models import GenerateRequest, GenerateResponse
from app.pipeline.discovery import agent

router = APIRouter(prefix="/api/discovery", tags=["discovery"])


@router.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    try:
        drafts = agent.generate_tasks(req.aff, req.note)
    except RuntimeError as e:      # API 키 등 설정 오류
        raise HTTPException(status_code=503, detail=str(e))
    except ValueError as e:        # 응답 파싱 실패
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:         # 그 외(네트워크·API)
        raise HTTPException(status_code=500, detail=f"과제 생성 실패: {e}")
    return GenerateResponse(tasks=drafts)
