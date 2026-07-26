"""제안서 생성 agent — 혁신 과제 정의 · 기대효과 · 추진 logic · 예상 투자/사전 단계 (스텁).

평가를 통과한 과제를 실행 가능한 제안서 문서로 확장합니다.
"""
from app.models import TaskOut


def build_proposal(task: TaskOut) -> dict:
    """과제 기록을 제안서 구조(정의/기대효과/추진 logic/투자)로 확장."""
    raise NotImplementedError("제안서 생성 미구현")
