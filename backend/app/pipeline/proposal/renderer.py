"""제안서 → Markdown 직렬화 (내보내기·메신저 발송용)."""
from typing import Sequence

from app.db.database import get_connection
from app.models import ProposalDoc


def _evidence_lines(ids: Sequence[str]) -> list:
    ids = [i for i in ids if i]
    if not ids:
        return ["- (없음)"]
    ph = ",".join("?" * len(ids))
    conn = get_connection()
    try:
        rows = conn.execute(
            f"SELECT id, published_on, source, title, url FROM feed_item WHERE id IN ({ph})",
            ids,
        ).fetchall()
    finally:
        conn.close()
    found = {r["id"]: r for r in rows}
    out = []
    for i in ids:
        r = found.get(i)
        if not r:
            out.append(f"- ({i}) — 원문을 찾을 수 없음")
            continue
        link = f" — {r['url']}" if r["url"] else ""
        out.append(f"- [{r['published_on']} · {r['source']}] {r['title']}{link}")
    return out


def to_markdown(p: ProposalDoc, aff_name: str = "") -> str:
    """제안서를 Markdown 문서로 만든다."""
    head = f"# {p.title}"
    if aff_name:
        head += f"  \n**대상**: {aff_name}"
    if p.taskId:
        head += f"  \n**과제 ID**: {p.taskId}"

    lines = [head, ""]

    lines += ["## 1. 과제 정의", p.definition or "(미작성)", ""]

    lines += ["## 2. 기대효과", p.expectedEffect or "(미작성)", ""]
    if p.kpiBaseline or p.kpiTarget:
        lines += [
            "| 구분 | 내용 |",
            "|---|---|",
            f"| 현재 수준 | {p.kpiBaseline or '-'} |",
            f"| 목표 수준 | {p.kpiTarget or '-'} |",
            "",
        ]

    lines += ["## 3. 추진 logic"]
    if p.phases:
        for ph in p.phases:
            title = ph.name + (f" ({ph.duration})" if ph.duration else "")
            lines.append(f"### {title}")
            for a in ph.activities:
                lines.append(f"- {a}")
            if ph.deliverable:
                lines.append(f"- **산출물**: {ph.deliverable}")
            lines.append("")
    else:
        lines += ["(미작성)", ""]

    lines += ["## 4. 필요 사전 단계"]
    lines += [f"- {x}" for x in p.prerequisites] or ["- (없음)"]
    lines.append("")

    lines += ["## 5. 예상 투자 비용"]
    lines += [f"- {x}" for x in p.investmentItems] or ["- (없음)"]
    if p.investmentSummary:
        lines += ["", f"**총계**: {p.investmentSummary}"]
    lines.append("")

    if p.risks:
        lines += ["## 6. 리스크"] + [f"- {x}" for x in p.risks] + [""]

    lines += ["## 근거"] + _evidence_lines(p.evidence) + [""]

    note = (
        "> 이 제안서는 AI가 생성한 초안입니다. 투자 금액과 목표 수준은 담당자 검증이 필요합니다."
        if p.generatedBy == "llm"
        else "> 이 제안서는 과제 정보로 자동 구성한 골격입니다. 각 항목은 담당자가 작성해야 합니다."
    )
    lines.append(note)

    return "\n".join(lines)
