"""과제 발굴 agent — 컨텍스트 조립 · LLM 호출 · 응답 파싱.

provider 는 `OI_TASK_PROVIDER` 로 고릅니다(app/llm_client.py). 기본값 codex-cli 는
API 키가 아니라 ChatGPT 로그인을 쓰므로, 팀 공용 키 크레딧과 무관하게 동작합니다.

프롬프트 구성
-------------
컨텍스트는 `knowledge/prefetch.build_context()` 가 만든다 — 레버 체계 · 계열사 프로필 ·
내부 지식(파일 KB) · 업로드 자료 · 혁신 사례 · 외부 동향 · 사용자 메모가 한 번에 실린다.
여기(agent)는 그 위에 **작성 규칙 system 프롬프트**와 **[이미 등록된 과제명]**,
**[현업 평가 이력]**(별점 되먹임) 블록만 얹는다.
관리자 화면의 인스트럭션(app_setting.instruction)도 system 안에 블록으로 주입한다 —
넣지 않으면 관리자 화면이 생성 결과에 아무 영향을 주지 못한다.

출력 강제
---------
codex 는 `--output-schema` 로 응답 형태를 강제할 수 있다(supports_schema=True).
최상위는 **반드시 object** 라서 {"tasks":[...]} 로 감싼다 — type:"array" 는 HTTP 400 이다.
lever 는 enum 으로 막는데, 그 목록은 코드 상수가 아니라 DB(`SELECT name FROM lever`)에서
만든다. 표기 불일치(정비·TA / 기타)는 프롬프트 문구가 아니라 enum 이 막는 것이 실측이다.
스키마를 못 쓰는 provider 는 프롬프트 유도 + _parse 의 관대한 파싱으로 폴백한다.
"""
import json
import re
from typing import Dict, List, Optional, Tuple

from app import llm_client
from app.config import OI_MODEL, OI_REGEN_TASKS, OI_TASK_PROVIDER
from app.db.database import get_connection
from app.models import Kpi, TaskDraft
from app.pipeline.discovery.lever_map import known_levers, normalize_lever
from app.pipeline.knowledge import prefetch

# ★ 자료 종류 라벨(feed_item.kind → 한국어)을 코드 상수로 두지 마라 — 관리자가
#   source_kind 를 고쳐도 프롬프트만 옛 라벨로 남는다. 프롬프트의 [외부 동향] 블록은
#   prefetch._feed_block 이 만들고, 거기서 **DB 값**(feed_item.kind_label, 없으면
#   source_kind.label)을 읽는다.


# [이미 등록된 과제명] 블록에 넣을 최대 건수
KNOWN_NAME_LIMIT = 40


# ── system 프롬프트 ───────────────────────────────────────────────────────
# 길이·종결형 규칙은 시드 47건을 실측해 뽑은 분포다(name 13~29자 / summary 31~56자 /
# plan 34~66자, 마침표·종결형 47/47 일치). 지어낸 수치가 아니므로 임의로 완화하지 말 것.
# 금지 표현 12개는 평가 validator 의 _VAGUE_PHRASES 와 같은 목록이다 —
# 생성기가 모르는 규칙으로 검증기가 감점하는 상태를 없애기 위함이다.
SYSTEM_TMPL = """너는 SK이노베이션 O/I추진단의 과제 발굴 애널리스트다.
아래 근거만을 사용해 {aff_name}({aff_code})에 적용할 O/I(Operation Improvement) 과제 {n}건을 만든다.

■ 근거 사용 규칙
- [내부 지식]·[내부 자료]는 대상 계열사의 실제 공정·원가 구조다. 여기에 닿지 않는 일반론은 내지 않는다.
- [외부 동향]과 [검증된 혁신 사례]는 "무엇을 벤치마크할 것인가"에만 쓴다.
- 근거에 없는 내부 수치를 지어내지 않는다.
{instruction_block}{feedback_rule_block}
■ 출력
- 최상위 JSON 객체 {{"tasks":[...]}} 하나만 낸다. 코드펜스·설명·주석·인사말 금지.
- tasks 는 정확히 {n}개.

■ 항목별 작성 규칙 — 어기면 저장되지 않는다

1) name — 과제명
   · 13~30자. 명사구로 끝낸다(…개선 / …표준화 / …최적화 / …재협상 / …전환 / …단축).
   · 마침표를 찍지 않는다. "~한다", "~하기", "~할 것" 으로 끝내지 않는다.
   · 예) NCC 정기보수 공기 단축 — 공정 병렬화
   · 예) 전력 다소비 공정 요금제·피크 관리 최적화

2) lever — 개선 레버
   · 다음 {lever_n}개 중 정확히 하나를 글자 그대로 쓴다.
     {lever_list}
   · "정비·TA", "정비", "TA", "기타", "가동률", "판관비" 는 모두 오답이다.
     특히 구분자는 가운뎃점(·)이 아니라 슬래시(/)다 — 정비/TA.
   · 어디에도 들어맞지 않으면 그 과제를 만들지 말고 다른 과제를 낸다.
   · 한 응답 안에서 같은 레버를 두 번 쓰지 않는다.

3) summary — 한 줄 요약  ★형식 고정★
   · 형식: {{벤치마크 주체}} {{무엇을 했는가}} — {{우리는 어디에 어떻게 적용하는가}}
   · 30~56자. 구분자는 em dash( — ) 정확히 한 개.
   · 문장이 아니라 명사형으로 끊는다. 마침표를 찍지 않고 "~한다" 로 끝내지 않는다.
   · 예) ENEOS 정비 주기 재설계 — 고장 이력 기반 예방정비 주기 차등화
   · 예) BASF 운전자본 관리 — 공정 간 재공품 대기 시간 축소로 회전일수 단축
   · 나쁜 예) 정기보수 작업별 표준 공기를 수립해 전체 TA 기간을 단축한다.  ← 문장형이라 오답

4) background — 배경
   · 정확히 2문장. 각 문장은 "~다." 로 끝낸다. 합계 60~140자.
   · 1문장은 지금 무엇이 문제인가(현재 상태), 2문장은 왜 지금 손대야 하는가.
   · 내부 값을 모르면 "…를 측정한 데이터가 없다" 처럼 부재를 쓴다.

5) plan — 적용 방안
   · 정확히 1문장. "~한다." 로 끝낸다. 34~70자. 마침표는 문장 끝 1개뿐이다.
   · 대상(무엇을)과 수단(어떻게)을 모두 쓴다. 조직 구성·검토 착수만 쓰지 않는다.
   · 예) 직전 3회 TA의 공정별 소요일을 분해해 상호 독립 공정을 식별하고 1개 라인에 병렬 배치를 시범 적용한다.

6) risk — 핵심 리스크
   · 1문장, "~다." 로 끝낸다. 25~70자. 실행을 막을 수 있는 것 하나만 쓴다.
   · 예) 병렬 배치 시 안전작업허가 충돌로 오히려 대기 시간이 늘 수 있다.

7) effect — 기대효과
   · 1문장, "~다." 로 끝낸다. 20~60자.
   · 숫자 또는 % 를 반드시 하나 이상 넣는다. 범위는 "8~10%" 처럼 쓴다.
   · **금액(억원·원·달러·$)을 쓰지 않는다.** 금액은 시스템이 현업 기준값 입력으로 계산한다.
   · 예) TA 공기를 기준 대비 8~10% 단축한다.

8) kpi_name — 관리지표
   · 4~20자 명사구. 단위가 있으면 괄호로 붙인다.
   · 예) TA 공기(일) / 에너지 원단위(kWh/t) / 재고자산 회전일수(일)

9) kpi_formula — 산출식
   · 10~60자. ×, −, ÷, /, % 중 최소 하나를 포함한다. 서술 문장으로 쓰지 않는다.
   · 금액을 산정하는 식이 아니라 **성과 지표를 재는 식**이다.
   · 예) (기준 TA 일수 − 개선 후 TA 일수) ÷ 기준 TA 일수 × 100

10) evidence — 외부 근거
   · [외부 동향] 항목의 (ev:...) id 값만 문자열 배열로 넣는다. 1~2개.
   · "e1" 처럼 id 값만 쓴다.
     "(ev:e1)" 이나 "(ev:e1) [2026-07-11 · 미쓰이화학] 정기보수 공기 표준화…" 처럼
     줄 전체를 복사해 넣으면 근거가 통째로 버려진다.
   · 목록에 없는 id 를 만들어 내지 않는다. 쓸 근거가 없으면 그 과제를 내지 않는다.

11) kb_refs — 내부 근거
   · [내부 지식]의 (kb:...) 와 [내부 자료]의 (up:...) id 값만 문자열 배열로 넣는다. 0~3개.
   · 여기서도 id 값만 쓴다. 해당 블록이 없으면 빈 배열로 둔다.

■ 금지 표현 — 하나라도 들어가면 검토 대상으로 밀린다
   적극 검토 / 다각도로 / 지속적으로 검토 / 필요시 검토 / 방안 마련 /
   제고 방안 / 활성화 방안 / 등등 / 다양한 방법 / 최선을 다 / 노력한다 / 추진할 예정

■ 과제 선정
   · 확장 투자형(증설·신설·플랜트 건설·공장 신축)이 아니라 비용·효율·수익성 개선을 우선한다.
   · 같은 벤치마크를 여러 OC에 적용할 때는 각각 별건으로 만든다.
   · [이미 등록된 과제명]과 같거나 뜻이 겹치는 과제를 내지 않는다."""


def _instruction_block(conn) -> str:
    """관리자 화면의 인스트럭션을 system 블록으로. 비어 있으면 블록을 통째로 생략한다."""
    row = conn.execute(
        "SELECT value FROM app_setting WHERE key = 'instruction'"
    ).fetchone()
    text = (row["value"] if row else "").strip()
    if not text:
        return ""
    return (
        "\n──── 관리자 인스트럭션 ────\n"
        f"{text}\n"
        "──────────────────────────\n"
    )


# ── 현업 평가 되먹임 ──────────────────────────────────────────────────────
# 화면(trendroom.html)에는 "별점과 피드백은 과제 생성·필터링 에이전트의 학습 데이터로
# 사용됩니다" 라고 적혀 있다. 그 문장을 사실로 만드는 것이 이 블록이다.
#
# 원칙 두 가지.
#  1) 별점이 한 건도 없으면 블록을 **통째로 생략한다**. 빈 블록은 모델에게
#     '현업 평가가 전부 중립' 이라는 없는 사실을 알리는 것과 같다.
#  2) 예시 문장은 store.feedback_signals 가 proposal_feedback_log(스냅샷)에서 뽑는다 —
#     낮은 점수를 받고 이미 삭제된 과제일수록 '피해야 할 방향' 으로서 값어치가 크다.

# system 규칙 — 되먹임 데이터가 있을 때만 붙인다.
FEEDBACK_RULE_BLOCK = """
■ 현업 평가 반영 — [현업 평가 이력] 블록
- 저평가 과제와 같은 주제·서술 방식을 되풀이하지 않는다. 지적된 사유(메모)가 그대로 적용될 과제를 내지 않는다.
- 고평가 과제가 보인 구체성(대상 공정·수단·측정 지표를 명시하는 수준)을 이번 과제의 기준선으로 삼는다.
"""

# user 블록에 실을 예시 건수(레버 집계는 전량).
FEEDBACK_TITLE = "[현업 평가 이력 — 현업이 매긴 별점]"


def _feedback_block(conn, aff_code: str) -> str:
    """현업 별점 되먹임 블록. 데이터가 0건이면 빈 문자열(= 블록 생략)."""
    from app import store          # store ↔ pipeline 순환 import 방지 (함수 안에서 import)

    sig = store.feedback_signals(aff_code, conn=conn)
    if not sig:
        return ""

    lines = [FEEDBACK_TITLE,
             "이 계열사 과제에 현업이 실제로 매긴 평가다. 낮은 평가의 특징은 피하고 높은 평가의 방향을 따른다."]

    if sig["levers"]:
        agg = " · ".join(
            f"{x['lever']} 평균 {x['avg']}점({x['n']}건)" for x in sig["levers"]
        )
        lines.append(f"- 레버별 평균: {agg}")

    def _fmt(item: dict) -> str:
        memo = (item["memo"] or "").strip().replace("\n", " ")
        tail = f' — 사유: "{memo}"' if memo else ""
        return f"  · ({item['score']}점) {item['name']} [{item['lever']}]{tail}"

    if sig["low"]:
        lines.append("- 낮은 평가(1~2점) — 이런 과제는 내지 않는다")
        lines.extend(_fmt(x) for x in sig["low"])
    if sig["high"]:
        lines.append("- 높은 평가(4점 이상) — 이 수준의 구체성을 따른다")
        lines.extend(_fmt(x) for x in sig["high"])
    return "\n".join(lines)


def _known_names(conn, aff_code: str) -> List[str]:
    """같은 계열사에 이미 등록된 과제명(최신순). 중복을 사후 필터가 아니라 사전에 막는다."""
    return [
        r["name"]
        for r in conn.execute(
            "SELECT name FROM proposal WHERE aff_code = ? ORDER BY id DESC LIMIT ?",
            (aff_code, KNOWN_NAME_LIMIT),
        )
        if r["name"]
    ]


def build_schema(levers: List[str]) -> dict:
    """codex `--output-schema` 용 JSON Schema.

    제약(실측):
      · 최상위는 반드시 object. type:"array" 는 HTTP 400.
      · 모든 object 노드에 properties 전 키 required + additionalProperties:false.
      · 판단 기준은 description 안에 넣어야 전달된다(type 만으로는 안 먹는다).
      · minLength/maxLength/pattern 은 지원되지 않으므로 길이 규칙은 프롬프트가 담당한다.
    lever enum 만 스키마로 강제한다 — FK 충돌의 근본 해결책이 문구가 아니라 enum 이다.
    """
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["tasks"],
        "properties": {
            "tasks": {
                "type": "array",
                "description": "O/I 과제 목록",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": [
                        "name", "lever", "summary", "background", "plan", "risk",
                        "effect", "kpi_name", "kpi_formula", "evidence", "kb_refs",
                    ],
                    "properties": {
                        "name": {"type": "string", "description": "과제명. 13~30자, 명사구 종결, 마침표 없음"},
                        "lever": {"type": "string", "enum": list(levers),
                                  "description": "개선 레버. 이 목록의 표기를 글자 그대로 쓴다"},
                        "summary": {"type": "string", "description": "{벤치마크 주체} {무엇} — {적용 대상·방식}. 30~56자, 명사형, 마침표 없음"},
                        "background": {"type": "string", "description": "배경 2문장, 각 '~다.' 종결, 합계 60~140자"},
                        "plan": {"type": "string", "description": "적용 방안 1문장, '~한다.' 종결, 34~70자"},
                        "risk": {"type": "string", "description": "핵심 리스크 1문장, '~다.' 종결, 25~70자"},
                        "effect": {"type": "string", "description": "기대효과 1문장, '~다.' 종결, 숫자/% 포함, 금액 금지, 20~60자"},
                        "kpi_name": {"type": "string", "description": "관리지표 4~20자 명사구. 단위는 괄호"},
                        "kpi_formula": {"type": "string", "description": "산출식 10~60자, ×/−/÷/// 중 1개 이상 포함"},
                        "evidence": {"type": "array", "items": {"type": "string"},
                                     "description": "[외부 동향]의 (ev:...) id 값만. 예 [\"e1\",\"e5\"]"},
                        "kb_refs": {"type": "array", "items": {"type": "string"},
                                    "description": "[내부 지식]의 (kb:...) 와 [내부 자료]의 (up:...) id 값만. 없으면 []"},
                    },
                },
            }
        },
    }


def _build_messages(aff_code: str, note: str, n: int = OI_REGEN_TASKS,
                    conn=None) -> Tuple[str, str, Dict]:
    """(system, user, meta) 를 만든다.

    meta 는 prefetch 가 준 것에 다음을 더한 것이다.
        'levers'      : lever 마스터 정식명(스키마 enum 원본)
        'aff_name'    : 계열사명
        'known_names' : [이미 등록된 과제명] 블록에 실린 과제명
    meta['ev_ids'] / ['kb_ids'] / ['up_ids'] 는 **프롬프트에 실제로 실린 id 화이트리스트**이며
    _parse 가 이 집합과 교집합을 취해 환각 id 를 걸러낸다.
    """
    context, meta = prefetch.build_context(aff_code, note)

    own = conn is None
    if own:
        conn = get_connection()
    try:
        levers = known_levers(conn)
        instruction_block = _instruction_block(conn)
        feedback = _feedback_block(conn, aff_code)
        names = _known_names(conn, aff_code)
        row = conn.execute(
            "SELECT name FROM affiliate WHERE code = ?", (aff_code,)
        ).fetchone()
    finally:
        if own:
            conn.close()
    aff_name = row["name"] if row else aff_code

    system = SYSTEM_TMPL.format(
        aff_name=aff_name, aff_code=aff_code, n=n,
        instruction_block=instruction_block,
        # 되먹임 데이터가 없으면 system 규칙도 넣지 않는다 —
        # 없는 블록을 가리키는 규칙은 모델을 혼란시킨다.
        feedback_rule_block=FEEDBACK_RULE_BLOCK if feedback else "",
        lever_n=len(levers), lever_list=" · ".join(levers),
    )

    # prefetch 의 role 블록(meta['system'])은 쓰지 않는다 — 위 SYSTEM_TMPL 이 그 역할을
    # 흡수했고, 둘 다 넣으면 같은 지시가 두 번 들어가 서로 우선순위를 다툰다.
    parts = [meta["user"]]
    if feedback:
        parts.append(feedback)
    if names:
        parts.append(
            "[이미 등록된 과제명 — 중복 금지]\n"
            + "\n".join(f"- {x}" for x in names)
        )
    user = "\n\n".join(parts)

    meta = dict(meta, levers=levers, aff_name=aff_name, known_names=names,
                context=context)
    return system, user, meta


# ── 응답 파싱 ─────────────────────────────────────────────────────────────

# 모델이 id 대신 컨텍스트 줄 전체를 넣어 돌려준 실측이 있다.
# "(ev:e1) [2026-07-11 · 미쓰이화학] …" → 'e1' 을 먼저 뽑아낸 뒤 화이트리스트와 교집합한다.
_REF_RE = re.compile(r"(?:ev|kb|up|id)\s*[:：]\s*([A-Za-z0-9_.\-]+)")


def _pick_ids(values, allowed: set) -> List[str]:
    """모델이 돌려준 근거 목록을 화이트리스트 id 로 정제한다(순서 보존·중복 제거)."""
    out: List[str] = []
    for raw in values or []:
        token = str(raw).strip()
        if not token:
            continue
        cands = _REF_RE.findall(token) or [token.strip("()[] ")]
        for c in cands:
            c = c.strip()
            if c in allowed and c not in out:
                out.append(c)
    return out


def _tasks_of(payload) -> List[dict]:
    """{"tasks":[...]} 와 레거시 최상위 배열을 둘 다 받는다."""
    if isinstance(payload, dict):
        arr = payload.get("tasks")
    else:
        arr = payload
    if not isinstance(arr, list):
        raise ValueError("생성된 과제가 없습니다.")
    return [t for t in arr if isinstance(t, dict)]


def _loads(text: str):
    """코드펜스·산문이 섞여 있어도 최상위 JSON 하나를 건져낸다."""
    clean = (text or "").replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(clean)
    except json.JSONDecodeError:
        pass
    # object 우선(스키마 경로), 없으면 배열(레거시 경로)
    for opener, closer in (("{", "}"), ("[", "]")):
        start, end = clean.find(opener), clean.rfind(closer)
        if start != -1 and end > start:
            try:
                return json.loads(clean[start:end + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError("응답 형식을 해석하지 못했습니다.")


def _parse(text: str, meta: Dict, conn=None) -> List[TaskDraft]:
    """LLM 응답 → TaskDraft 목록.

    · lever 는 normalize_lever 로 정식명화한다. 실패하면 lever='' 로 두고 저장 경로가 버린다
      (임의 레버로 떨어뜨리면 화면이 틀린 금액을 계산한다).
    · category 에는 같은 값을 복사한다 — 평가 validator/scorer 가 task.category 를 읽는다.
    · evidence/kb_refs 는 프롬프트에 실제로 실린 id 화이트리스트와 교집합을 취한다.
    """
    ev_allowed = set(meta.get("ev_ids") or [])
    kb_allowed = set(meta.get("kb_ids") or []) | set(meta.get("up_ids") or [])

    arr = _tasks_of(_loads(text))
    if not arr:
        raise ValueError("생성된 과제가 없습니다.")

    own = conn is None
    if own:
        conn = get_connection()
    try:
        drafts: List[TaskDraft] = []
        for t in arr:
            raw_lever = t.get("lever") or t.get("category") or ""
            canon = normalize_lever(raw_lever, conn)
            # 레거시 응답(중첩 kpi{name,formula})도 받아 준다.
            nested = t.get("kpi") if isinstance(t.get("kpi"), dict) else {}
            drafts.append(TaskDraft(
                title=(t.get("name") or t.get("title") or "").strip() or "무제 과제",
                # category 는 평가 쪽 호환용 — 정규화에 실패하면 원문을 남겨 검증기가 잡게 둔다.
                category=canon or (str(raw_lever).strip() or "기타"),
                lever=canon or "",
                summary=(t.get("summary") or "").strip(),
                background=(t.get("background") or "").strip(),
                plan=(t.get("plan") or "").strip(),
                risk=(t.get("risk") or "").strip(),
                effect=(t.get("effect") or "").strip(),
                kpi=Kpi(
                    name=(t.get("kpi_name") or nested.get("name") or "-").strip() or "-",
                    formula=(t.get("kpi_formula") or nested.get("formula") or "-").strip() or "-",
                ),
                evidence=_pick_ids(t.get("evidence"), ev_allowed),
                kb_refs=_pick_ids(t.get("kb_refs"), kb_allowed),
            ))
    finally:
        if own:
            conn.close()
    return drafts


def generate_tasks(aff_code: str, note: str = "", n: int = OI_REGEN_TASKS,
                   conn=None) -> List[TaskDraft]:
    """계열사 1곳의 과제 초안 n건. LLM 호출 1회(스키마 경로) 또는 최대 2회(폴백 경로).

    ★ 호출 비용: codex-cli 기준 1회 10~16초. 예외는 그대로 올린다 —
      재생성 경로(store.regenerate)가 잡아서 후보 풀로 폴백한다.
    """
    ok, why = llm_client.ready(OI_TASK_PROVIDER)
    if not ok:
        raise RuntimeError(f"과제 발굴 LLM 을 쓸 수 없습니다 ({OI_TASK_PROVIDER}): {why}")

    system, user, meta = _build_messages(aff_code, note, n=n, conn=conn)
    schema = build_schema(meta["levers"])

    if llm_client.supports_schema(OI_TASK_PROVIDER):
        # 형태가 서버측에서 보장되므로 1회만 호출한다.
        text = llm_client.call(user, system, OI_MODEL, OI_TASK_PROVIDER, schema=schema)
        return _parse(text, meta, conn=conn)

    # 스키마 미지원 provider — 프롬프트 유도(_with_schema_hint)만 걸리므로 파싱 재시도를 남긴다.
    last: Optional[Exception] = None
    for attempt in range(2):
        try:
            text = llm_client.call(user, system, OI_MODEL, OI_TASK_PROVIDER, schema=schema)
            return _parse(text, meta, conn=conn)
        except ValueError as e:
            last = e
    raise ValueError(f"응답 형식을 해석하지 못했습니다: {last}")
