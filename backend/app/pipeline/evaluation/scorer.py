"""과제 평가 — Impact · Feasibility · ROI 채점.

두 가지 경로를 둔다.
    score_batch_llm()       Claude 호출. 근거 원문까지 넣어 grounding 도 함께 판정.
    score_batch_heuristic() 규칙 기반. API 키가 없거나 호출이 실패해도 데모가 돌아간다.

score_batch() 가 llm → heuristic 순으로 자동 폴백한다.
"""
import json
import re
from typing import List, Optional, Sequence, Tuple

from app.config import ANTHROPIC_API_KEY, OI_MODEL
from app.db.database import get_connection
from app.models import AxisScore, TaskDraft

# ─────────── 휴리스틱 파라미터 ───────────
# 레버별 임팩트 사전값 — 정유·화학 O/I 에서 통상 크기 순.
CATEGORY_IMPACT = {
    "에너지비": 4.5, "수율": 4.5, "정비·TA": 4.0, "정비/TA": 4.0,
    "물류비": 3.5, "구매": 3.5, "운전자본": 3.5, "간접비": 3.0,
}
DEFAULT_IMPACT = 3.0

# 자본투자 신호 — 실현가능성/ROI 를 낮춘다 (발굴 프롬프트도 확장투자형을 후순위로 지시)
_CAPEX_RE = re.compile(r"증설|신설|신규\s*투자|플랜트\s*건설|설비\s*도입|라인\s*신규|공장\s*신축")
# 실행 구체성 신호
_CONCRETE_RE = re.compile(r"\d|시스템|모델|센서|알고리즘|파일럿|표준화|스케줄|모니터링|자동화")
_QUANT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*[%％]")


def _clamp(v: float, lo: float = 1.0, hi: float = 5.0) -> float:
    return round(max(lo, min(hi, v)), 1)


# ─────────── 휴리스틱 ───────────
def _heuristic_one(task: TaskDraft) -> Tuple[AxisScore, AxisScore, AxisScore]:
    blob = " ".join([task.background or "", task.plan or "", task.effect or ""])
    capex = bool(_CAPEX_RE.search(blob))
    concrete = bool(_CONCRETE_RE.search(task.plan or ""))
    n_evidence = len(task.evidence)

    # Impact — 레버 사전값 + 정량 목표 크기
    impact = CATEGORY_IMPACT.get((task.category or "").strip(), DEFAULT_IMPACT)
    reasons = [f"레버 '{task.category or '미분류'}' 기준값"]
    pcts = [float(m) for m in _QUANT_RE.findall(task.effect or "")]
    if pcts:
        top = max(pcts)
        if top >= 10:
            impact += 0.5
            reasons.append(f"기대효과 {top:g}% 로 폭이 큼")
        elif top < 3:
            impact -= 0.3
            reasons.append(f"기대효과 {top:g}% 로 폭이 작음")
    elif not re.search(r"\d", task.effect or ""):
        impact -= 0.4
        reasons.append("정량 목표 미제시")
    impact_score = AxisScore(score=_clamp(impact), reason=" · ".join(reasons))

    # Feasibility — 실행방안 구체성, 자본투자 여부, 근거 두께
    feas = 3.0
    freasons = []
    if concrete:
        feas += 0.5
        freasons.append("실행방안에 구체적 수단 명시")
    else:
        feas -= 0.4
        freasons.append("실행 수단이 추상적")
    if capex:
        feas -= 0.8
        freasons.append("신규 설비투자 수반")
    if (task.risk or "").strip():
        feas += 0.3
        freasons.append("리스크 식별됨")
    if n_evidence >= 2:
        feas += 0.3
        freasons.append(f"근거 {n_evidence}건")
    elif n_evidence == 0:
        feas -= 0.5
        freasons.append("근거 없음")
    feas_score = AxisScore(score=_clamp(feas), reason=" · ".join(freasons))

    # ROI — 임팩트/실현가능성의 균형에서 자본투자 부담을 뺀다
    roi = impact_score.score * 0.5 + feas_score.score * 0.5
    rreasons = ["임팩트·실현가능성 가중 평균"]
    if capex:
        roi -= 0.7
        rreasons.append("투자 회수기간 부담")
    if not capex and concrete:
        roi += 0.3
        rreasons.append("운영개선형으로 초기비용 낮음")
    roi_score = AxisScore(score=_clamp(roi), reason=" · ".join(rreasons))

    return impact_score, feas_score, roi_score


def score_batch_heuristic(tasks: Sequence[TaskDraft]) -> List[dict]:
    out = []
    for t in tasks:
        i, f, r = _heuristic_one(t)
        out.append({
            "impact": i, "feasibility": f, "roi": r,
            "grounding": "unknown",
            "grounding_reason": "규칙 기반 채점 — 근거 적합성은 미검증",
            "scored_by": "heuristic",
        })
    return out


# ─────────── LLM ───────────
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


def _build_messages(tasks: Sequence[TaskDraft], aff_name: str):
    ev_ids = [e for t in tasks for e in t.evidence]
    task_lines = []
    for idx, t in enumerate(tasks):
        task_lines.append("\n".join([
            f"### 과제 {idx}",
            f"- 과제명: {t.title}",
            f"- 레버: {t.category}",
            f"- 배경: {t.background}",
            f"- 실행방안: {t.plan}",
            f"- 리스크: {t.risk}",
            f"- 기대효과: {t.effect}",
            f"- KPI: {t.kpi.name} = {t.kpi.formula}",
            f"- 인용 근거: {', '.join(t.evidence) if t.evidence else '(없음)'}",
        ]))

    system = "\n".join([
        f"너는 SK이노베이션 O/I추진단의 과제 심사역이다. {aff_name}에 대해 발굴된 O/I 과제 후보를 심사한다.",
        "각 과제를 세 축으로 1~5점(정수 또는 .5 단위)으로 채점하고, 인용된 근거가 실제로 그 과제를 뒷받침하는지 판정한다.",
        "",
        "채점 기준:",
        "- impact: 비용절감·수익확대의 크기. 5=연간 수백억 규모 레버, 3=의미 있으나 국지적, 1=효과 미미하거나 부정영향 우려.",
        "- feasibility: 기존 기술·조직으로 착수 가능한 정도. 5=현 역량으로 즉시 착수, 3=사전 검토 필요, 1=신규 설비·미확보 기술 의존.",
        "- roi: 투자 대비 회수. 5=투자 거의 없이 효과, 3=1~2년 회수, 1=대규모 capex·회수 불투명.",
        "- grounding: supported=인용 근거가 배경·기대효과를 실제로 뒷받침 / weak=느슨하게만 관련 / unsupported=근거가 주장과 무관하거나 과장.",
        "",
        "규칙:",
        "- 출력은 JSON 배열만. 코드펜스·설명·주석 금지.",
        '- 원소 스키마: {"index":0,"impact":{"score":4,"reason":"1문장"},"feasibility":{"score":3,"reason":"1문장"},"roi":{"score":3.5,"reason":"1문장"},"grounding":"supported","grounding_reason":"1문장"}',
        "- 입력 과제 수와 같은 개수를 index 순서대로 반환한다.",
        "- reason 은 한국어 1문장. 점수를 반복하지 말고 근거를 쓴다.",
        "- 후하게 주지 마라. 근거 없이 정량 효과를 주장하면 impact 를 낮춘다.",
    ])

    user = "\n\n".join([
        "[인용 가능한 외부 동향 원문]",
        _evidence_text(ev_ids),
        "[심사 대상 과제]",
        "\n\n".join(task_lines),
    ])
    return system, user


def _parse(text: str, n: int) -> List[dict]:
    clean = text.replace("```json", "").replace("```", "").strip()
    start, end = clean.find("["), clean.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("평가 응답을 해석하지 못했습니다.")
    arr = json.loads(clean[start:end + 1])
    if not isinstance(arr, list):
        raise ValueError("평가 응답이 배열이 아닙니다.")

    by_index = {}
    for item in arr:
        if not isinstance(item, dict):
            continue
        try:
            idx = int(item.get("index", -1))
        except (TypeError, ValueError):
            continue
        by_index[idx] = item

    out = []
    for i in range(n):
        item = by_index.get(i, {})

        def axis(key) -> AxisScore:
            raw = item.get(key) or {}
            if not isinstance(raw, dict):
                raw = {}
            try:
                s = float(raw.get("score", 3))
            except (TypeError, ValueError):
                s = 3.0
            return AxisScore(score=_clamp(s), reason=str(raw.get("reason") or "").strip())

        g = str(item.get("grounding") or "unknown").strip().lower()
        if g not in ("supported", "weak", "unsupported"):
            g = "unknown"
        out.append({
            "impact": axis("impact"),
            "feasibility": axis("feasibility"),
            "roi": axis("roi"),
            "grounding": g,
            "grounding_reason": str(item.get("grounding_reason") or "").strip(),
            "scored_by": "llm",
        })
    return out


def score_batch_llm(tasks: Sequence[TaskDraft], aff_name: str) -> List[dict]:
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY 가 설정되지 않았습니다.")
    from anthropic import Anthropic

    system, user = _build_messages(tasks, aff_name)
    resp = Anthropic(api_key=ANTHROPIC_API_KEY).messages.create(
        model=OI_MODEL,
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text")
    return _parse(text, len(tasks))


def score_batch(
    tasks: Sequence[TaskDraft],
    aff_name: str = "",
    *,
    use_llm: bool = True,
) -> List[dict]:
    """LLM 채점을 시도하고, 불가하면 규칙 기반으로 폴백한다."""
    if not tasks:
        return []
    if use_llm:
        try:
            return score_batch_llm(tasks, aff_name)
        except Exception as e:            # 키 없음·네트워크·파싱 실패 모두 폴백
            fallback = score_batch_heuristic(tasks)
            for f in fallback:
                f["grounding_reason"] = f"LLM 채점 실패로 규칙 기반 폴백 ({type(e).__name__})"
            return fallback
    return score_batch_heuristic(tasks)
