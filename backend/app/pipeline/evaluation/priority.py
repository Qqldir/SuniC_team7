"""우선순위 평가 — 축별 점수를 종합해 순위를 매긴다.

멘토 피드백("Top n 선정 기준이 궁금하다")에 대응해, 점수는 항상
가중치와 축별 사유를 함께 노출한다. 블랙박스 숫자를 만들지 않는다.
"""
import os
from typing import List, Optional, Sequence

from app.models import Evaluation, EvaluatedTask, TaskDraft, ValidationResult

# ─────────── 가중치 (env 로 조정 가능) ───────────
W_IMPACT = float(os.getenv("OI_W_IMPACT", "0.40"))
W_FEASIBILITY = float(os.getenv("OI_W_FEASIBILITY", "0.35"))
W_ROI = float(os.getenv("OI_W_ROI", "0.25"))

GRADE_A = float(os.getenv("OI_GRADE_A", "75"))
GRADE_B = float(os.getenv("OI_GRADE_B", "55"))

# 근거 적합성에 따른 감점 계수
GROUNDING_FACTOR = {
    "supported": 1.00,
    "unknown": 0.95,
    "weak": 0.85,
    "unsupported": 0.60,
}

WEIGHTS = {"impact": W_IMPACT, "feasibility": W_FEASIBILITY, "roi": W_ROI}


def criteria_text(top_n: Optional[int] = None) -> str:
    """사용자·봇에 그대로 노출할 선정 기준 문장."""
    base = (
        f"우선순위 = (임팩트×{W_IMPACT:.0%} + 실현가능성×{W_FEASIBILITY:.0%} + ROI×{W_ROI:.0%}) "
        f"× 근거적합성 계수, 100점 환산. "
        f"등급 A≥{GRADE_A:.0f} · B≥{GRADE_B:.0f} · 그 미만 C. "
        "필수 항목 누락·근거 없음·중복 과제는 점수와 무관하게 제외됩니다."
    )
    if top_n:
        base += f" 이 목록은 통과 과제 중 상위 {top_n}건입니다."
    return base


def compute_priority(
    impact: float, feasibility: float, roi: float, grounding: str = "unknown"
) -> float:
    """0~100 우선순위 점수."""
    weighted = impact * W_IMPACT + feasibility * W_FEASIBILITY + roi * W_ROI
    pct = (weighted / 5.0) * 100.0
    return round(pct * GROUNDING_FACTOR.get(grounding, 0.95), 1)


def grade_of(priority: float) -> str:
    if priority >= GRADE_A:
        return "A"
    if priority >= GRADE_B:
        return "B"
    return "C"


def build_evaluations(
    tasks: Sequence[TaskDraft],
    validations: Sequence[ValidationResult],
    scores: Sequence[dict],
) -> List[EvaluatedTask]:
    """검증 결과 + 채점 결과를 Evaluation 으로 합친다."""
    out: List[EvaluatedTask] = []
    for i, task in enumerate(tasks):
        val = validations[i]
        sc = scores[i] if i < len(scores) else None

        if sc is None or not val.ok:
            # 차단된 과제는 채점하지 않는다 (토큰 낭비 방지)
            ev = Evaluation(
                verdict=val.verdict,
                validation=val,
                grounding="unknown",
                groundingReason="검증 미통과로 채점하지 않음" if not val.ok else "",
                priority=0.0,
                grade="C",
                scoredBy="none",
            )
        else:
            grounding = sc["grounding"]
            priority = compute_priority(
                sc["impact"].score, sc["feasibility"].score, sc["roi"].score, grounding
            )
            # 근거가 주장을 뒷받침하지 못하면 통과시키지 않는다
            verdict = val.verdict
            if grounding == "unsupported":
                verdict = "review"
            ev = Evaluation(
                verdict=verdict,
                validation=val,
                impact=sc["impact"],
                feasibility=sc["feasibility"],
                roi=sc["roi"],
                grounding=grounding,
                groundingReason=sc.get("grounding_reason", ""),
                priority=priority,
                grade=grade_of(priority),
                scoredBy=sc.get("scored_by", "heuristic"),
            )
        out.append(EvaluatedTask(task=task, evaluation=ev))
    return out


def rank(results: Sequence[EvaluatedTask], top_n: Optional[int] = None) -> List[EvaluatedTask]:
    """우선순위 내림차순 정렬. blocked 는 항상 뒤로 보내고 rank 를 주지 않는다."""
    ordered = sorted(
        results,
        key=lambda r: (r.evaluation.verdict == "blocked", -r.evaluation.priority),
    )
    n = 0
    for r in ordered:
        if r.evaluation.verdict != "blocked":
            n += 1
            r.evaluation.rank = n
        else:
            r.evaluation.rank = None

    if top_n:
        keep = [r for r in ordered if r.evaluation.rank and r.evaluation.rank <= top_n]
        return keep
    return ordered


def prioritize(tasks: List[TaskDraft]) -> List[TaskDraft]:
    """스텁 호환 시그니처 — 평가 후 정렬된 draft 목록만 반환.

    점수와 사유가 필요하면 evaluation.evaluate_tasks() 를 쓸 것.
    """
    from app.pipeline.evaluation import evaluate_tasks
    evaluated = evaluate_tasks(tasks, aff_code="", use_llm=False)
    return [r.task for r in evaluated if r.evaluation.verdict != "blocked"]
