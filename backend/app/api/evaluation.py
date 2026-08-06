"""과제 평가 API."""
from fastapi import APIRouter, HTTPException

from app.models import (
    EvaluateRequest, EvaluateResponse, TaskDraft, ValidationResult,
)
from app.pipeline.evaluation import WEIGHTS, criteria_text, evaluate_tasks, validate_batch

router = APIRouter(prefix="/api/evaluation", tags=["evaluation"])


@router.post("/evaluate", response_model=EvaluateResponse)
def evaluate(req: EvaluateRequest):
    """발굴 draft 를 검증·채점하고 우선순위 순으로 돌려준다."""
    if not req.tasks:
        raise HTTPException(status_code=400, detail="평가할 과제가 없습니다.")
    try:
        # top_n 은 여기서 적용하지 않는다 — 집계는 배치 전체 기준이어야 한다.
        results = evaluate_tasks(
            req.tasks, req.aff,
            use_llm=req.useLlm, check_saved=req.checkSaved,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"과제 평가 실패: {e}")

    counts = {"pass": 0, "review": 0, "blocked": 0}
    for r in results:
        counts[r.evaluation.verdict] = counts.get(r.evaluation.verdict, 0) + 1

    shown = results
    if req.topN:
        shown = [r for r in results if r.evaluation.rank and r.evaluation.rank <= req.topN]

    return EvaluateResponse(
        results=shown,
        criteria=criteria_text(req.topN),
        weights=WEIGHTS,
        passed=counts["pass"],
        review=counts["review"],
        blocked=counts["blocked"],
    )


@router.post("/validate", response_model=list[ValidationResult])
def validate(req: EvaluateRequest):
    """결정적 검증만 수행 (LLM 호출 없음 — 즉시 응답)."""
    if not req.tasks:
        raise HTTPException(status_code=400, detail="검증할 과제가 없습니다.")
    return validate_batch(req.tasks, req.aff, check_saved=req.checkSaved)


@router.get("/criteria")
def criteria():
    """선정 기준 노출 — 봇·대시보드에서 'Top N 기준'을 설명할 때 쓴다."""
    return {"criteria": criteria_text(), "weights": WEIGHTS}
