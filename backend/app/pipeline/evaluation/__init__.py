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
    "criteria_text", "compute_priority", "grade_of", "rank", "WEIGHTS",
]


# ★ 후보 풀 재사용 과제만 DUPLICATE 를 완화하는 예외 통로를 만들지 마라.
#   validator 는 DUPLICATE 를 **항상 warn** 으로 낸다 — 낮출 block 이 애초에 없다.
#   예외 경로가 있으면 "여기서는 중복이 차단될 수도 있다" 는 잘못된 인상을 주고,
#   나중에 severity 를 block 으로 되돌릴 때 후보풀 과제만 조용히 다르게 동작한다.


def evaluate_tasks(
    tasks: Sequence[TaskDraft],
    aff_code: str,
    *,
    top_n: Optional[int] = None,
    use_llm: bool = True,
    check_saved: bool = True,
    aff_name: str = "",
    self_ids: Sequence[Optional[int]] = (),
) -> List[EvaluatedTask]:
    """발굴 draft 목록을 검증·채점·정렬해 반환한다.

    blocked 과제는 채점을 건너뛰고, top_n 을 주면 통과 과제 상위 N건만 남긴다.

    self_ids: tasks 와 같은 순서의 proposal.id 목록. **이미 저장된 proposal 을
        재평가할 때는 반드시 넘겨라.** 안 넘기면 자기 자신이 중복 후보에 들어가
        유사도 100% 로 전 과제가 중복 경고를 받는다(validate_batch 참조).
    """
    if not tasks:
        return []

    validations = _validator.validate_batch(
        tasks, aff_code, check_saved=check_saved, self_ids=self_ids
    )

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


# ★ 축 하나씩만 채점하는 진입점을 따로 만들지 마라. 그 경로에는 검증(validator)도
#   grounding 도 없어 같은 과제에 다른 점수가 나온다. 축별 점수가 필요하면
#   evaluate_tasks() 가 돌려주는 EvaluatedTask.evaluation.{impact,feasibility,roi} 를 읽어라.
