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

# ─────────── 등급 컷 ───────────
# 임의로 고른 값이 아니라 **실측 priority 분포의 '빈 구간' 중점**이다.
# 저장된 80건을 규칙 채점으로 전량 재평가해 얻은 값 사이의 간격은 이렇다
# (폭 1.0 이상인 구간만, 괄호 안은 그 위쪽 누적 비율):
#
#     (74.8 , 76.5)  폭 1.7  →  위쪽 12건 (15.0%)      ← A 컷
#     (71.5 , 74.1)  폭 2.6  →  위쪽 29건 (36.2%)
#     (69.8 , 71.2)  폭 1.4  →  위쪽 38건 (47.5%)
#     (66.2 , 69.1)  폭 2.9  →  위쪽 44건 (55.0%)
#     (64.3 , 66.0)  폭 1.7  →  위쪽 52건 (65.0%)      ← B 컷
#     (60.7 , 64.3)  폭 3.6  →  위쪽 68건 (85.0%)
#
# 목표(A 15~25% · B 45~60%)를 만족하는 조합은 사실상 하나뿐이다:
#   A 컷을 (74.8, 76.5) 안에, B 컷을 (64.3, 66.0) 안에 두면 A 12건(15.0%) ·
#   B 40건(50.0%) · C 28건(35.0%). A 컷을 74.8 아래로 내리면 74.8 에 몰린 14건이
#   한꺼번에 들어와 A 가 32.5% 로 튀고, B 컷을 66.2 위로 올리면 B 가 40% 로 떨어진다.
#
# 구간 안에서 **중점**을 고른 이유: 값이 규칙 채점 특성상 소수의 값에 뭉쳐 있어
# (74.8 에 14건 · 64.3 에 16건) 컷이 덩어리에 붙어 있으면 채점을 조금만 손봐도
# 등급이 통째로 요동친다. 75.5 는 아래 덩어리에서 0.7, 위 값에서 1.0 떨어져 있다.
GRADE_A = float(os.getenv("OI_GRADE_A", "75.5"))
GRADE_B = float(os.getenv("OI_GRADE_B", "65"))

# 근거 적합성에 따른 감점 계수
#
# ★ unknown 은 1.00 이다. '미확인' 은 근거가 나쁘다는 판정이 아니라 **아직 안 본 것**이다
#   (규칙 채점은 grounding 을 판정하지 않으므로 LLM 없이 돌리면 100% 가 unknown 이 된다).
#   0.95 로 두면 전 과제에 똑같이 5% 를 깎아 변별력 0인 감점이 되고, LLM 을 못 돌리는
#   환경에서는 등급이 통째로 한 단계 내려앉는다. 실제로 나쁘다고 **판정된** weak /
#   unsupported 만 감점한다. scorer.importance_map 의 'NULL 은 무시' 규칙과 같은 정책이다.
GROUNDING_FACTOR = {
    "supported": 1.00,
    "unknown": 1.00,
    "weak": 0.85,
    "unsupported": 0.60,
}

WEIGHTS = {"impact": W_IMPACT, "feasibility": W_FEASIBILITY, "roi": W_ROI}


def criteria_text(top_n: Optional[int] = None) -> str:
    """사용자·봇에 그대로 노출할 선정 기준 문장."""
    base = (
        f"우선순위 = (임팩트×{W_IMPACT:.0%} + 실현가능성×{W_FEASIBILITY:.0%} + ROI×{W_ROI:.0%}) "
        f"× 근거적합성 계수, 100점 환산. "
        # :g 로 찍는다 — :.0f 는 75.5 를 '76' 으로 반올림해 실제 컷과 다른 숫자를 보여 준다.
        f"등급 A≥{GRADE_A:g} · B≥{GRADE_B:g} · 그 미만 C. "
        # 중복은 더 이상 제외 사유가 아니다 — 경고만 달고 목록에 그대로 남긴다.
        "과제명·실행방안 누락이나 근거 없음은 점수와 무관하게 차단되고, "
        "중복 의심 과제는 차단하지 않고 경고만 답니다."
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

