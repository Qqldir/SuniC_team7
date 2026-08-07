"""과제 평가 — Impact · Feasibility · ROI 채점.

두 가지 경로를 둔다.
    score_batch_llm()       LLM 호출. 근거 원문까지 넣어 grounding 도 함께 판정.
    score_batch_heuristic() 규칙 기반. LLM 이 없거나 호출이 실패해도 완주한다.

score_batch() 가 llm → heuristic 순으로 자동 폴백한다.

★ 스키마 강제 금지 ★
이 모듈의 LLM 프롬프트는 **최상위가 JSON 배열**이다. llm_client.call 에
`schema=` 를 넘기면 codex 의 --output-schema 가 붙는데, codex 는 최상위가
object 인 스키마만 받는다 — 배열을 주면 HTTP 400
(`schema must be a JSON Schema of 'type: "object"'`) 로 즉사한다.
그래서 여기서는 schema= 없이 soft 경로로만 호출한다.
스키마 강제가 꼭 필요해지면 프롬프트를 {"scores":[...]} 로 감싸고
_parse 를 함께 고쳐야 한다. 한쪽만 바꾸면 조용히 폴백으로 떨어진다.
"""
import json
import re
from typing import Dict, List, Optional, Sequence, Tuple

from app import llm_client
from app.config import OI_EVAL_BATCH, OI_MODEL, OI_TASK_PROVIDER
from app.db.database import get_connection
from app.models import AxisScore, TaskDraft

# ─────────── 휴리스틱 파라미터 ───────────
# 레버별 임팩트 기준값은 **lever.impact_base 컬럼**에서 읽는다.
# ★ 레버별 임팩트를 코드 딕셔너리로 두지 마라 — 관리자가 레버를 추가·개명하면
#   즉시 어긋난다. 조회 실패 시에만 DEFAULT_IMPACT 를 쓴다.
DEFAULT_IMPACT = 3.0

# 자본투자 신호 — 실현가능성/ROI 를 낮춘다 (발굴 프롬프트도 확장투자형을 후순위로 지시)
_CAPEX_RE = re.compile(r"증설|신설|신규\s*투자|플랜트\s*건설|설비\s*도입|라인\s*신규|공장\s*신축")
# 실행 구체성 신호
_CONCRETE_RE = re.compile(r"\d|시스템|모델|센서|알고리즘|파일럿|표준화|스케줄|모니터링|자동화")
_QUANT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*[%％]")


def _clamp(v: float, lo: float = 1.0, hi: float = 5.0) -> float:
    return round(max(lo, min(hi, v)), 1)


# ─────────── DB 신호 ───────────
def impact_base_map() -> Dict[str, float]:
    """레버 표기 → impact_base. lever_alias 의 표기 변형도 같은 값으로 접는다.

    조회에 실패하면 빈 dict 를 돌린다 — 그러면 전부 DEFAULT_IMPACT 로 채점되고
    예외 없이 완주한다.
    """
    try:
        conn = get_connection()
    except Exception:
        return {}
    try:
        base = {
            r["name"]: float(r["impact_base"])
            for r in conn.execute("SELECT name, impact_base FROM lever")
        }
        for r in conn.execute("SELECT alias, lever FROM lever_alias"):
            if r["lever"] in base:
                base[r["alias"]] = base[r["lever"]]
        return base
    except Exception:
        return {}
    finally:
        conn.close()


def importance_map(ids: Sequence[str]) -> Dict[str, int]:
    """근거 id → feed_item.importance(0~100).

    ★ NULL 은 **키 자체를 넣지 않는다.** NULL 을 0 으로 치면 파밍 정제 전
      (현재 feed_item 14건 전부 importance IS NULL) 모든 과제가 균일하게
      감점돼 순위가 무의미해진다. '있으면 쓰고 없으면 무시' 가 유일한 안전 규칙이다.
    """
    ids = [i for i in set(ids) if i]
    if not ids:
        return {}
    ph = ",".join("?" * len(ids))
    try:
        conn = get_connection()
    except Exception:
        return {}
    try:
        rows = conn.execute(
            f"SELECT id, importance FROM feed_item "
            f"WHERE id IN ({ph}) AND importance IS NOT NULL",
            ids,
        ).fetchall()
        return {r["id"]: int(r["importance"]) for r in rows}
    except Exception:
        return {}
    finally:
        conn.close()


# ─────────── 휴리스틱 ───────────
def _heuristic_one(
    task: TaskDraft,
    base_map: Optional[Dict[str, float]] = None,
    imp_map: Optional[Dict[str, int]] = None,
) -> Tuple[AxisScore, AxisScore, AxisScore]:
    if base_map is None:
        base_map = impact_base_map()
    if imp_map is None:
        imp_map = importance_map(task.evidence)

    blob = " ".join([task.background or "", task.plan or "", task.effect or ""])
    capex = bool(_CAPEX_RE.search(blob))
    concrete = bool(_CONCRETE_RE.search(task.plan or ""))
    n_evidence = len(task.evidence)

    # Impact — lever.impact_base + 정량 목표 크기 + 근거 중요도(있을 때만)
    cat = (task.category or "").strip()
    impact = base_map.get(cat, base_map.get((task.lever or "").strip(), DEFAULT_IMPACT))
    reasons = [f"레버 '{cat or '미분류'}' 기준값 {impact:g}"]
    effect_text = (task.effect or "").strip()
    pcts = [float(m) for m in _QUANT_RE.findall(effect_text)]
    if pcts:
        top = max(pcts)
        if top >= 10:
            impact += 0.5
            reasons.append(f"기대효과 {top:g}% 로 폭이 큼")
        elif top < 3:
            impact -= 0.3
            reasons.append(f"기대효과 {top:g}% 로 폭이 작음")
    elif not effect_text:
        # ★ 기대효과가 **통째로 비어 있는** 것은 과제가 나빠서가 아니라 항목이 안 채워진 것이다.
        #   실측 80건 중 67건(84%)이 여기 해당해 감점이 전 과제에 균일하게 걸렸다 —
        #   변별력은 0이면서 전체 점수만 끌어내린다. 게다가 validator 가 같은 사실을
        #   MISSING_FIELD 경고로 이미 화면에 띄우므로 한 사실에 벌을 두 번 주는 꼴이었다.
        #   → 감점하지 않고 사유만 남긴다. importance NULL 을 무시하는 규칙과 같은 정책이다.
        reasons.append("기대효과 미기재 — 감점 없음(항목 누락은 검증 경고로 표시)")
    elif not re.search(r"\d", effect_text):
        # 기대효과를 **썼는데도** 수치가 없는 경우만 감점한다. 이건 실제 품질 신호다.
        impact -= 0.2
        reasons.append("기대효과에 정량 목표 없음")
    # 근거 중요도 가산 — importance 가 **실제로 있는** 근거만 평균낸다.
    # 하나도 없으면(정제 전 상태) 이 항목은 통째로 건너뛴다: 감점 0.
    imps = [imp_map[e] for e in task.evidence if e in imp_map]
    if imps:
        avg = sum(imps) / len(imps)
        if avg >= 70:
            impact += 0.3
            reasons.append(f"근거 중요도 평균 {avg:.0f}")
        elif avg <= 30:
            impact -= 0.3
            reasons.append(f"근거 중요도 평균 {avg:.0f} 로 낮음")
    impact_score = AxisScore(score=_clamp(impact), reason=" · ".join(reasons))

    # Feasibility — 실행방안 구체성, 자본투자 여부, 근거 두께
    feas = 3.0
    freasons = []
    if concrete:
        feas += 0.5
        freasons.append("실행방안에 구체적 수단 명시")
    else:
        # ★ 실측 80건 중 55건(69%)이 이 감점을 받았다. _CONCRETE_RE 가 못 잡는 표현이
        #   흔하다는 뜻이지 과제 3분의 2가 실제로 부실하다는 뜻이 아니다.
        #   가점(+0.5)은 그대로 두고 감점만 -0.4 → -0.15 로 낮춰, 구체적인 과제를
        #   끌어올리는 쪽으로 변별한다(감점 일변도 완화).
        feas -= 0.15
        freasons.append("실행 수단 표현이 추상적")
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
    # DB 조회는 배치당 각 1회 — 과제 수만큼 커넥션을 열면 165건에서 눈에 띄게 느려진다.
    base_map = impact_base_map()
    imp_map = importance_map([e for t in tasks for e in t.evidence])
    out = []
    for t in tasks:
        i, f, r = _heuristic_one(t, base_map, imp_map)
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


def _looks_like_payload(value) -> bool:
    """평가 배치로 볼 만한 모양인가 — dict 의 배열, 또는 그런 배열을 값으로 가진 object."""
    if isinstance(value, list):
        return bool(value) and all(isinstance(x, dict) for x in value)
    if isinstance(value, dict):
        return any(_looks_like_payload(v) for v in value.values())
    return False


def _loads(text: str):
    """코드펜스·산문이 섞여 있어도 평가 배치 JSON 하나를 건져낸다.

    ★ 옛 구현은 **첫 '[' 와 마지막 ']' 사이를 통째로 잘라** json.loads 에 넘겼다.
      그래서 모델이 앞뒤에 한 줄이라도 산문을 붙이면서 거기에 대괄호를 쓰면
      (실측: "아래는 평가입니다 [총 8건]" / 말미의 "참고 [1]") 잘려 나온 조각이 JSON 이
      아니게 되고, **배치 8건 전체가 규칙 폴백으로** 떨어졌다. 대괄호 한 글자에 LLM
      채점 한 배치가 통째로 날아가는 것이 이 함수의 실패 모드였다.

    전략(agent._loads 와 같은 계열이되, 여기는 최상위가 배열이라 한 단계 더 든든하게):
      1) 펜스 제거 후 통째로 파싱해 본다.
      2) 실패하면 '[' 와 '{' 가 나오는 **모든 위치**에서 raw_decode 를 시도한다.
         raw_decode 는 유효한 JSON 값 하나를 읽고 **뒤에 뭐가 붙어 있든 무시**하므로
         산문 접두·접미가 저절로 떨어져 나간다.
      3) 우연히 먼저 디코드되는 산문 속 배열(예: "[1]")을 집지 않도록, 평가 배치처럼
         생긴 것(_looks_like_payload)을 우선 고르고 없을 때만 첫 성공값을 쓴다.

    ★ agent/farming/generator 에도 비슷한 파서가 있지만 합치지 않는다 — 기대하는
      최상위 형태(object / array)와 실패 시 처리가 서로 다르다.
    """
    clean = (text or "").replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(clean)
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()
    first = None
    for i, ch in enumerate(clean):
        if ch not in "[{":
            continue
        try:
            value, _ = decoder.raw_decode(clean, i)
        except json.JSONDecodeError:
            continue
        if _looks_like_payload(value):
            return value
        if first is None:
            first = value
    if first is not None:
        return first
    raise ValueError("평가 응답을 해석하지 못했습니다.")


def _parse(text: str, n: int) -> List[dict]:
    arr = _loads(text)
    if isinstance(arr, dict):
        # {"results":[...]} / {"tasks":[...]} 처럼 감싸 온 경우 — 첫 리스트 값을 취한다.
        arr = next((v for v in arr.values() if isinstance(v, list)), None)
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

    # 응답에 빠진 index 를 기본값 3.0 으로 메우면 '가짜 LLM 채점' 이 조용히 저장된다
    # (사유 공란 · grounding=미확인 인데 scored_by 는 LLM). 규칙 폴백으로 떨어뜨리는 편이 정직하다.
    missing = [i for i in range(n) if i not in by_index]
    if missing:
        raise ValueError(f"평가 응답에 {len(missing)}건이 빠졌습니다 (index {missing[:5]}).")

    out = []
    for i in range(n):
        item = by_index[i]

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
    """LLM 채점. OI_EVAL_BATCH 건씩 나눠 호출한다.

    ★ llm_client.MAX_TOKENS 가 2000 이라 51건을 한 번에 넣으면 출력이 중간에서
      잘려 _parse 가 통째로 실패한다. 그러면 전 과제가 규칙 폴백으로 떨어진다.
    ★ schema= 를 넘기지 않는다 — 모듈 상단 주석 참조(최상위가 배열이라 HTTP 400).
    """
    ready, why = llm_client.ready(OI_TASK_PROVIDER)
    if not ready:
        raise RuntimeError(why)
    size = max(1, OI_EVAL_BATCH)
    out: List[dict] = []
    for start in range(0, len(tasks), size):
        chunk = list(tasks[start:start + size])
        system, user = _build_messages(chunk, aff_name)
        text = llm_client.call(user, system, OI_MODEL, OI_TASK_PROVIDER)
        out.extend(_parse(text, len(chunk)))
    return out


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
