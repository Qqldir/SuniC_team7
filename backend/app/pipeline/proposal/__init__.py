"""제안서 생성 agent — 혁신 과제 정의 · 기대효과 · 추진 logic · 예상 투자/사전 단계.

평가를 통과한 과제를 실행 가능한 제안서 문서로 확장한다.

    generator  LLM 확장 (+ 실패 시 골격 폴백)
    renderer   Markdown 직렬화 (내보내기·메신저 발송용)

사용 예:
    from app.pipeline.proposal import generate, to_markdown
    p = generate(task, aff_name="SK에너지")
    md = to_markdown(p, aff_name="SK에너지")
"""
from typing import Optional

from app.models import Proposal, TaskIn
from app.pipeline.proposal.generator import build_skeleton, generate, generate_llm
from app.pipeline.proposal.renderer import to_markdown

__all__ = [
    "generate", "generate_llm", "build_skeleton", "to_markdown", "build_proposal",
]


def build_proposal(task: TaskIn) -> dict:
    """과제 기록을 제안서 구조(정의/기대효과/추진 logic/투자)로 확장.

    스텁 시그니처 호환용 — dict 를 돌려준다.
    구조화된 객체가 필요하면 generate() 를 직접 쓸 것.
    """
    aff_name = ""
    aff_code = getattr(task, "aff", "")
    if aff_code:
        from app.pipeline.knowledge import repository as kb
        aff_name = kb.affiliate_name(aff_code)
    return generate(task, aff_name).model_dump()
