"""제안서 생성 API."""
from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from app.models import Proposal, ProposalRequest
from app.pipeline.knowledge import repository as kb
from app.pipeline.proposal import generate, to_markdown

router = APIRouter(prefix="/api/proposal", tags=["proposal"])


def _build(req: ProposalRequest) -> tuple[Proposal, str]:
    aff_name = kb.affiliate_name(req.task.aff) if req.task.aff else ""
    try:
        return generate(req.task, aff_name, use_llm=req.useLlm), aff_name
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"제안서 생성 실패: {e}")


@router.post("/build", response_model=Proposal)
def build(req: ProposalRequest):
    """과제를 제안서 구조로 확장한다."""
    proposal, _ = _build(req)
    return proposal


@router.post("/markdown", response_class=PlainTextResponse)
def markdown(req: ProposalRequest):
    """제안서를 Markdown 으로 내보낸다 (내보내기·메신저 발송용)."""
    proposal, aff_name = _build(req)
    return to_markdown(proposal, aff_name)
