"""제안서 생성 agent — 혁신 과제 정의 · 기대효과 · 추진 logic · 예상 투자/사전 단계.

평가를 통과한 과제를 실행 가능한 제안서 문서로 확장한다.

    generator  LLM 확장 (+ 실패 시 골격 폴백)
    renderer   Markdown 직렬화 (내보내기·메신저 발송용)

사용 예:
    from app.pipeline.proposal import generate, to_markdown
    p = generate(task, aff_name="SK에너지")
    md = to_markdown(p, aff_name="SK에너지")

CLI — 제안서 생성의 유일한 진입점이다(화면·HTTP 경로 없음). 지우지 마라:
    python -m app.pipeline.proposal --pid 1240            # 규칙 골격, Markdown 출력
    python -m app.pipeline.proposal --pid 1240 --llm      # LLM 확장
    python -m app.pipeline.proposal --pid 1240 --json     # ProposalDoc JSON
"""
from app.models import ProposalDoc, ProposalDocIn
from app.pipeline.proposal.generator import build_skeleton, generate, generate_llm
from app.pipeline.proposal.renderer import to_markdown

__all__ = [
    "generate", "generate_llm", "build_skeleton", "to_markdown", "load_task",
]


def load_task(pid: int) -> tuple[ProposalDocIn, str]:
    """proposal 1건을 제안서 입력(ProposalDocIn)과 계열사명으로 바꾼다.

    ★ kpi_name/kpi_formula 가 NULL 이면 lever 기본값으로 폴백한다 —
      store._proposals() 가 화면에 내리는 값과 같은 규칙이어야 제안서와 화면이 안 어긋난다.
    """
    from app.db.database import get_connection

    conn = get_connection()
    try:
        r = conn.execute(
            """SELECT p.*, a.name AS aff_name,
                      COALESCE(NULLIF(p.kpi_name, ''), l.metric)   AS kpi_n,
                      COALESCE(NULLIF(p.kpi_formula, ''), l.formula) AS kpi_f,
                      (SELECT GROUP_CONCAT(feed_id) FROM proposal_evidence e
                        WHERE e.proposal_id = p.id) AS ev
                 FROM proposal p
                 LEFT JOIN affiliate a ON a.code = p.aff_code
                 LEFT JOIN lever l     ON l.name = p.lever
                WHERE p.id = ?""",
            (pid,),
        ).fetchone()
    finally:
        conn.close()
    if not r:
        raise ValueError(f"과제를 찾을 수 없습니다: {pid}")
    return ProposalDocIn(
        id=str(r["id"]),
        createdAt=r["created_at"] or "",
        aff=r["aff_code"] or "",
        title=r["name"] or "",
        category=r["lever"] or "",
        background=r["background"] or "",
        plan=r["plan"] or "",
        risk=r["risk"] or "",
        effect=r["effect"] or "",
        kpiName=r["kpi_n"] or "-",
        kpiFormula=r["kpi_f"] or "-",
        evidence=[e for e in (r["ev"] or "").split(",") if e],
        status=r["status"] or "검토중",
        origin=r["origin"] or "자동",
    ), (r["aff_name"] or "")


def _main() -> None:
    import argparse
    import json

    ap = argparse.ArgumentParser(description="저장된 과제를 제안서 문서로 확장한다.")
    ap.add_argument("--pid", type=int, required=True, help="proposal.id")
    ap.add_argument("--llm", action="store_true", help="LLM 확장 (기본은 규칙 골격)")
    ap.add_argument("--json", action="store_true", help="Markdown 대신 JSON 출력")
    a = ap.parse_args()

    task, aff_name = load_task(a.pid)
    doc: ProposalDoc = generate(task, aff_name, use_llm=a.llm)
    print(json.dumps(doc.model_dump(), ensure_ascii=False, indent=2)
          if a.json else to_markdown(doc, aff_name))


if __name__ == "__main__":
    _main()
