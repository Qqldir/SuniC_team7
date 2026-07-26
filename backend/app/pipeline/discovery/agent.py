"""과제 발굴 agent — Claude 호출."""
import json
from typing import List

from anthropic import Anthropic

from app.config import ANTHROPIC_API_KEY, OI_MODEL, TODAY
from app.models import TaskDraft, Kpi
from app.pipeline.knowledge import repository as kb

KIND_LABEL = {"adhoc": "DART 수시", "periodic": "DART 정기", "sec": "SEC", "news": "뉴스"}


def _client() -> Anthropic:
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY 가 설정되지 않았습니다. backend/.env 를 확인하세요.")
    return Anthropic(api_key=ANTHROPIC_API_KEY)


def _build_messages(aff_code: str, note: str):
    aff_name = kb.affiliate_name(aff_code)
    items = kb.feed_for_affiliate(aff_code, within_days=30, limit=8, today=TODAY)
    valid_ids = {it.id for it in items}

    ctx_lines = [
        f"- (id:{it.id}) [{it.d[5:]} · {KIND_LABEL.get(it.kind, it.kind)} · {it.src}] {it.title} — {it.sum}"
        for it in items
    ]
    ctx = "\n".join(ctx_lines) if ctx_lines else "- (해당 없음)"

    system = "\n".join([
        f"너는 SK이노베이션 O/I추진단의 과제 발굴 애널리스트다. [외부 동향]과 [내부 현황]을 근거로 {aff_name}에 적용 가능한 O/I(Operation Improvement) 과제 2건을 제안한다.",
        "규칙:",
        "- 출력은 JSON 배열만. 코드펜스·설명·주석 금지.",
        '- 원소 스키마: {"title":"과제명","category":"레버 분류(에너지비/정비·TA/물류비/수율/구매/간접비/운전자본 중 택1 또는 유사)","background":"배경 1~2문장","plan":"실행방안 1~2문장","risk":"핵심 리스크 1문장","effect":"기대효과 1문장(정량 방향성 포함)","kpi":{"name":"지표명","formula":"산출식"},"evidence":["근거로 쓴 외부 동향 id"]}',
        "- evidence는 [외부 동향]의 id에서만 고른다. 없으면 빈 배열.",
        "- 확장 투자형보다 비용·효율·수익성 개선 과제를 우선한다. 문장은 짧고 구체적으로.",
    ])

    user = "\n".join([
        f"[외부 동향] (최근 30일, {aff_name} 관련)",
        ctx,
        "",
        "[내부 현황]",
        note.strip() if note and note.strip() else "(제공되지 않음 — 외부 동향만으로 제안)",
    ])
    return system, user, valid_ids


def _parse(text: str, valid_ids: set) -> List[TaskDraft]:
    clean = text.replace("```json", "").replace("```", "").strip()
    start, end = clean.find("["), clean.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("응답 형식을 해석하지 못했습니다.")
    arr = json.loads(clean[start:end + 1])
    if not isinstance(arr, list) or not arr:
        raise ValueError("생성된 과제가 없습니다.")

    drafts = []
    for t in arr:
        kpi = t.get("kpi") or {}
        drafts.append(TaskDraft(
            title=t.get("title") or "무제 과제",
            category=t.get("category") or "기타",
            background=t.get("background") or "",
            plan=t.get("plan") or "",
            risk=t.get("risk") or "",
            effect=t.get("effect") or "",
            kpi=Kpi(name=kpi.get("name") or "-", formula=kpi.get("formula") or "-"),
            evidence=[e for e in (t.get("evidence") or []) if e in valid_ids],
        ))
    return drafts


def generate_tasks(aff_code: str, note: str = "") -> List[TaskDraft]:
    system, user, valid_ids = _build_messages(aff_code, note)
    resp = _client().messages.create(
        model=OI_MODEL,
        max_tokens=1000,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text")
    return _parse(text, valid_ids)
