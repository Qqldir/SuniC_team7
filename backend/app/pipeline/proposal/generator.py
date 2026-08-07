"""제안서 생성 — 과제 정의 · 기대효과 · 추진 logic · 예상 투자/사전 단계.

평가를 통과한 과제를 실행 문서로 확장한다.

원칙: 투자비·회수기간처럼 근거 없이는 알 수 없는 숫자를 지어내지 않는다.
LLM 에도 '금액 대신 산정 방식과 범위를 쓰라'고 지시하고, 폴백 경로는
비워 둔 채 '(산정 필요)' 로 남긴다. 제안서의 신뢰도는 여기서 갈린다.
"""
import json
from typing import List, Sequence

from app import llm_client
# ★ provider 축은 OI_TASK_PROVIDER 다(과제 발굴 agent · 과제 평가 scorer 와 같은 축).
#   OI_LLM_PROVIDER 는 **지식 파밍(farming/llm.py)** 전용 축이다. 여기서 그걸 쓰면
#   "발굴·평가만 provider 를 바꿨는데 제안서만 옛 provider 로 돈다" 는 교차 사용이 된다.
from app.config import OI_MODEL, OI_TASK_PROVIDER
from app.db.database import get_connection
from app.models import ProposalDoc, ProposalPhase, ProposalDocIn

PLACEHOLDER = "(산정 필요)"


def _evidence_text(ids: Sequence[str]) -> str:
    ids = [i for i in set(ids) if i]
    if not ids:
        return "- (없음)"
    ph = ",".join("?" * len(ids))
    conn = get_connection()
    try:
        rows = conn.execute(
            f"SELECT id, published_on, source, title, summary FROM feed_item WHERE id IN ({ph})",
            ids,
        ).fetchall()
    finally:
        conn.close()
    if not rows:
        return "- (없음)"
    return "\n".join(
        f"- (id:{r['id']}) [{r['published_on']} · {r['source']}] {r['title']} — {r['summary']}"
        for r in rows
    )


# ─────────── 폴백: 골격만 만든다 ───────────
def build_skeleton(task: ProposalDocIn) -> ProposalDoc:
    """LLM 없이 만드는 제안서 골격.

    과제 필드를 재배치할 뿐 새로운 사실을 만들어내지 않는다.
    담당자가 채워야 할 칸은 명시적으로 비워 둔다.
    """
    definition = " ".join(filter(None, [
        f"{task.title}.",
        task.background.strip() if task.background else "",
    ])).strip()

    effect = task.effect.strip() if task.effect else PLACEHOLDER

    phases = [
        ProposalPhase(
            name="1단계 · 현황 진단",
            duration="1~2개월",
            activities=[
                "대상 공정·설비 범위 확정 및 baseline 데이터 수집",
                f"KPI '{task.kpiName}' 현재 수준 측정",
                "개선 여지 정량화 및 목표 수준 합의",
            ],
            deliverable="진단 결과 및 목표 KPI 합의서",
        ),
        ProposalPhase(
            name="2단계 · 파일럿 적용",
            duration="3~6개월",
            activities=[
                task.plan.strip() if task.plan else "실행방안 상세 설계",
                "제한 범위 파일럿 운영 및 효과 검증",
                "운영 표준·매뉴얼 초안 작성",
            ],
            deliverable="파일럿 효과 검증 보고서",
        ),
        ProposalPhase(
            name="3단계 · 확산",
            duration="6~12개월",
            activities=[
                "전 라인·전 사업장 순차 확산",
                "KPI 모니터링 체계 정착 및 성과 확정",
            ],
            deliverable="확산 완료 보고 및 성과 정산",
        ),
    ]

    prerequisites = [
        "대상 범위 및 주관 조직 확정",
        f"KPI '{task.kpiName}' 산출에 필요한 데이터 확보 ({task.kpiFormula})",
        "관련 부서 사전 협의 및 예산 반영",
    ]

    risks = [task.risk.strip()] if (task.risk or "").strip() else []

    return ProposalDoc(
        taskId=task.id or "",
        title=task.title,
        definition=definition,
        expectedEffect=effect,
        kpiBaseline=PLACEHOLDER,
        kpiTarget=PLACEHOLDER,
        phases=phases,
        prerequisites=prerequisites,
        investmentItems=[
            f"시스템·설비 투자: {PLACEHOLDER}",
            f"인건비·외부 용역: {PLACEHOLDER}",
        ],
        investmentSummary=f"총 투자 규모 {PLACEHOLDER} — 파일럿 결과 확정 후 산정",
        risks=risks,
        evidence=list(task.evidence or []),
        generatedBy="heuristic",
    )


# ─────────── LLM ───────────
def _build_messages(task: ProposalDocIn, aff_name: str):
    system = "\n".join([
        f"너는 SK이노베이션 O/I추진단의 제안서 작성 담당이다. 승인된 O/I 과제를 {aff_name} 경영진에 보고할 실행 제안서로 확장한다.",
        "",
        "규칙:",
        "- 출력은 JSON 객체만. 코드펜스·설명·주석 금지.",
        "- 스키마: {\"definition\":\"과제 정의 2~3문장\",\"expected_effect\":\"기대효과 2~3문장(정량 방향 포함)\","
        "\"kpi_baseline\":\"현재 수준 또는 측정 방법\",\"kpi_target\":\"목표 수준\","
        "\"phases\":[{\"name\":\"1단계 · 이름\",\"duration\":\"기간\",\"activities\":[\"활동\"],\"deliverable\":\"산출물\"}],"
        "\"prerequisites\":[\"필요 사전 단계\"],\"investment_items\":[\"투자 항목 — 산정 방식\"],"
        "\"investment_summary\":\"투자 규모 요약\",\"risks\":[\"리스크\"]}",
        "- phases 는 3~4단계. 각 단계 activities 2~4개.",
        "- 중요: 투자 금액·회수기간을 근거 없이 특정 숫자로 쓰지 마라. 대신 산정 방식이나 범위로 표현하고,"
        " 알 수 없으면 '(산정 필요)' 라고 명시하라. 지어낸 금액은 제안서 전체의 신뢰를 무너뜨린다.",
        "- 인용 근거에 없는 사실을 새로 만들지 마라.",
        "- 한국어. 문장은 짧고 구체적으로.",
    ])

    user = "\n".join([
        "[과제]",
        f"- 과제명: {task.title}",
        f"- 레버: {task.category}",
        f"- 배경: {task.background}",
        f"- 실행방안: {task.plan}",
        f"- 리스크: {task.risk}",
        f"- 기대효과: {task.effect}",
        f"- KPI: {task.kpiName} = {task.kpiFormula}",
        "",
        "[인용 근거 원문]",
        _evidence_text(task.evidence or []),
    ])
    return system, user


def _parse(text: str, task: ProposalDocIn) -> ProposalDoc:
    clean = text.replace("```json", "").replace("```", "").strip()
    start, end = clean.find("{"), clean.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("제안서 응답을 해석하지 못했습니다.")
    obj = json.loads(clean[start:end + 1])

    phases = []
    for p in obj.get("phases") or []:
        if not isinstance(p, dict):
            continue
        phases.append(ProposalPhase(
            name=str(p.get("name") or "단계"),
            duration=str(p.get("duration") or ""),
            activities=[str(a) for a in (p.get("activities") or [])],
            deliverable=str(p.get("deliverable") or ""),
        ))

    def slist(key) -> List[str]:
        return [str(x) for x in (obj.get(key) or []) if str(x).strip()]

    return ProposalDoc(
        taskId=task.id or "",
        title=task.title,
        definition=str(obj.get("definition") or "").strip(),
        expectedEffect=str(obj.get("expected_effect") or "").strip(),
        kpiBaseline=str(obj.get("kpi_baseline") or PLACEHOLDER).strip(),
        kpiTarget=str(obj.get("kpi_target") or PLACEHOLDER).strip(),
        phases=phases,
        prerequisites=slist("prerequisites"),
        investmentItems=slist("investment_items"),
        investmentSummary=str(obj.get("investment_summary") or PLACEHOLDER).strip(),
        risks=slist("risks"),
        evidence=list(task.evidence or []),
        generatedBy="llm",
    )


def generate_llm(task: ProposalDocIn, aff_name: str = "") -> ProposalDoc:
    ready, why = llm_client.ready(OI_TASK_PROVIDER)
    if not ready:
        raise RuntimeError(why)
    system, user = _build_messages(task, aff_name)
    text = llm_client.call(user, system, OI_MODEL, OI_TASK_PROVIDER)
    return _parse(text, task)


def generate(task: ProposalDocIn, aff_name: str = "", *, use_llm: bool = True) -> ProposalDoc:
    """제안서 생성. LLM 실패 시 골격으로 폴백한다."""
    if use_llm:
        try:
            return generate_llm(task, aff_name)
        except Exception:
            pass
    return build_skeleton(task)
