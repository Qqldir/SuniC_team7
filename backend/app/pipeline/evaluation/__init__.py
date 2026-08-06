"""과제 평가 agent — Impact · Feasibility · ROI · 우선순위.

발굴된 과제 후보를 두 단계로 거른다.

    1) validator  결정적 검증. 형식·근거·중복 — LLM 없이 판정하고 block/warn 을 낸다.
    2) scorer     LLM 채점. 임팩트·실현가능성·ROI + 근거 적합성(grounding).
    3) priority   가중 합산 → 0~100 우선순위, A/B/C 등급, Top-N.

핵심 원칙: '보여줄 수 있는가'(1)와 '얼마나 좋은가'(2)를 섞지 않는다.
형식 오류를 LLM 에게 되묻지 않고, 채점은 차단되지 않은 과제에만 돌린다.

사용 예:
    from app.pipeline.evaluation import evaluate_tasks
    results = evaluate_tasks(drafts, aff_code="SKE", top_n=5)
"""
from typing import List, Optional, Sequence

from app.models import EvaluatedTask, TaskDraft
from app.pipeline.evaluation import priority as _priority
from app.pipeline.evaluation import scorer as _scorer
from app.pipeline.evaluation import validator as _validator
from app.pipeline.evaluation.priority import (
    WEIGHTS, compute_priority, criteria_text, grade_of, rank,
)
from app.pipeline.evaluation.validator import validate_batch, validate_task

__all__ = [
    "evaluate_tasks", "validate_task", "validate_batch",
    "assess_impact", "assess_feasibility", "assess_roi", "prioritize",
    "criteria_text", "compute_priority", "grade_of", "rank", "WEIGHTS",
]


def evaluate_tasks(
    tasks: Sequence[TaskDraft],
    aff_code: str,
    *,
    top_n: Optional[int] = None,
    use_llm: bool = True,
    check_saved: bool = True,
    aff_name: str = "",
) -> List[EvaluatedTask]:
    """발굴 draft 목록을 검증·채점·정렬해 반환한다.

    blocked 과제는 채점을 건너뛰고, top_n 을 주면 통과 과제 상위 N건만 남긴다.
    """
    if not tasks:
        return []

    validations = _validator.validate_batch(tasks, aff_code, check_saved=check_saved)

    # 통과한 것만 채점 — 차단된 draft 에 토큰을 쓰지 않는다
    passable_idx = [i for i, v in enumerate(validations) if v.ok]
    scores: List[Optional[dict]] = [None] * len(tasks)
    if passable_idx:
        if not aff_name:
            from app.pipeline.knowledge import repository as kb
            aff_name = kb.affiliate_name(aff_code) if aff_code else ""
        subset = [tasks[i] for i in passable_idx]
        subset_scores = _scorer.score_batch(subset, aff_name, use_llm=use_llm)
        for pos, i in enumerate(passable_idx):
            scores[i] = subset_scores[pos] if pos < len(subset_scores) else None

    results = _priority.build_evaluations(tasks, validations, scores)
    return _priority.rank(results, top_n)


# ─────────── 단건 평가 (스텁 시그니처 호환) ───────────
def _single(task: TaskDraft) -> dict:
    i, f, r = _scorer._heuristic_one(task)
    return {"impact": i, "feasibility": f, "roi": r}


def assess_impact(task: TaskDraft) -> dict:
    """비용절감·수익확대 관점의 임팩트 평가 (규칙 기반 단건)."""
    s = _single(task)["impact"]
    return {"score": s.score, "reason": s.reason}


def assess_feasibility(task: TaskDraft) -> dict:
    """기술 보유 현황·사전 단계 관점의 실현가능성 평가 (규칙 기반 단건)."""
    s = _single(task)["feasibility"]
    return {"score": s.score, "reason": s.reason}


def assess_roi(task: TaskDraft) -> dict:
    """투자 대비 효과(ROI) 산정 (규칙 기반 단건)."""
    s = _single(task)["roi"]
    return {"score": s.score, "reason": s.reason}


def prioritize(tasks: List[TaskDraft]) -> List[TaskDraft]:
    """평가 점수를 종합해 우선순위 정렬."""
    return _priority.prioritize(tasks)
