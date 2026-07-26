"""혁신 사례 API — 조회 + 입력 + 검토(승인/반려) + 삭제.

3층 구조 지원:
- 사람이 입력한 사례: source_type=manual, status=approved 로 바로 등록
- AI 추출 사례(source_type=ai)는 status=pending 으로 들어와, 여기서 승인/반려
"""
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.config import TODAY
from app.models import CaseCreate, CaseStatusUpdate
from app.pipeline.knowledge import repository as kb

router = APIRouter(prefix="/api/cases", tags=["cases"])


@router.get("")
def list_cases(
    status: Optional[str] = Query(None, description="approved / pending / rejected"),
    aff: Optional[str] = Query(None, description="계열사 코드 (예: SKGC)"),
):
    cases = kb.list_cases(status=status, aff_code=aff)
    return {"cases": [c.model_dump() for c in cases]}


@router.post("")
def create_case(payload: CaseCreate):
    if not payload.title.strip():
        raise HTTPException(status_code=400, detail="사례명은 필수입니다.")
    data = {
        "title": payload.title.strip(), "category": payload.category,
        "background": payload.background, "effect": payload.effect,
        "kpi_name": payload.kpiName, "kpi_formula": payload.kpiFormula,
        "source_org": payload.sourceOrg, "source_type": payload.sourceType,
        "source_ref": payload.sourceRef, "status": payload.status,
        "affiliates": payload.affiliates, "created_at": TODAY,
    }
    return {"case": kb.create_case(data).model_dump()}


@router.patch("/{case_id}/status")
def update_status(case_id: int, payload: CaseStatusUpdate):
    if payload.status not in ("approved", "pending", "rejected"):
        raise HTTPException(status_code=400, detail="status 값이 올바르지 않습니다.")
    if not kb.set_case_status(case_id, payload.status):
        raise HTTPException(status_code=404, detail="사례를 찾을 수 없습니다.")
    return {"ok": True}


@router.delete("/{case_id}")
def remove_case(case_id: int):
    if not kb.delete_case(case_id):
        raise HTTPException(status_code=404, detail="사례를 찾을 수 없습니다.")
    return {"ok": True}
