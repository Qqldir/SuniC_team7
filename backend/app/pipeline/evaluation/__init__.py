"""과제 평가 agent — Impact · Feasibility · ROI · 우선순위 (스텁).

발굴된 과제 후보를 다면 평가해 점수/우선순위를 부여합니다.
"""
from app.models import TaskDraft


def assess_impact(task: TaskDraft) -> dict:
    """비용절감·수익확대·부정영향 관점의 임팩트 평가."""
    raise NotImplementedError("Impact assessment 미구현")


def assess_feasibility(task: TaskDraft) -> dict:
    """기술 보유 현황·사전 단계·준비물 관점의 실현가능성 평가."""
    raise NotImplementedError("Feasibility assessment 미구현")


def assess_roi(task: TaskDraft) -> dict:
    """투자 대비 효과(ROI) 산정."""
    raise NotImplementedError("ROI assessment 미구현")


def prioritize(tasks: list[TaskDraft]) -> list[TaskDraft]:
    """평가 점수를 종합해 우선순위 정렬."""
    raise NotImplementedError("우선순위 평가 미구현")
