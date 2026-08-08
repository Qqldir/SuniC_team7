"""수집 원문의 LLM 정제 — 한국어 한 줄 제목 · 단일 문단 요약 · 테마 · 지표 · 중요도.

crawler/pdf 로 확보한 원문을 과제 발굴 agent 가 판단할 수 있는 형태로 압축합니다.
정제하지 않으면 feed_item.summary 는 제목을 절삭한 값에 그쳐 근거로 쓸 수 없습니다.

**폴백이 핵심**: provider 미설정·네트워크·파싱 실패는 전부 naive 요약으로 떨어지고 예외를
올리지 않습니다. 설정이 없어도 파이프라인 E2E 가 돌고, 붙이면 품질만 올라갑니다.
(평가 단계 evaluation/scorer.py 의 score_batch 와 동일한 규약)

provider 는 `OI_LLM_PROVIDER` 로 고릅니다. 다만 `OI_CODEX_ONLY=1`(기본)이면
codex-cli 외에는 ready() 가 거부합니다 — 사내망 정책입니다.

    codex-cli   (기본) 로컬 `codex exec` 서브프로세스. API 키가 아니라 ChatGPT 로그인을 씁니다.
                응답 형태를 `--output-schema` 로 강제할 수 있는 유일한 provider 입니다.
                호출당 10~16초.
    claude-cli  로컬 `claude -p` 서브프로세스. 별도 API 키 없이 Claude Code 로그인을 씁니다.
                호출당 20초 안팎이라 배치(파밍)에만 적합합니다.
    openai      OpenAI API. `OPENAI_API_KEY` 필요.

발굴·평가·제안 단계는 `OI_TASK_PROVIDER` 축을 씁니다 — 파밍과 축이 다를 뿐,
모든 호출이 app/llm_client.py 를 거칩니다(tests/test_llm_policy.py 가 SDK 직접 호출을 막습니다).
"""
import json
from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence

from app import llm_client
from app.config import (
    AFFILIATE_CODES, OI_LLM_CONCURRENCY, OI_LLM_MODEL, OI_LLM_PROVIDER,
)
from app.pipeline.farming import classify
from app.pipeline.farming.base import RawDoc
from app.pipeline.farming.keywords import KEYWORDS_MAX

LEVERS = ["비용 절감", "수익 증대", "운영 효율"]

# 본문을 통째로 넣으면 비용이 폭증합니다. 공시는 앞부분에 개요가 오므로 절삭으로 충분합니다.
BODY_CHARS = 4_000
# 요약은 단일 문단 3문장 90~160자가 규격입니다. 300자는 그 상한을 넉넉히 감싼 안전판이며
# 화면 .tr2-s 가 2줄 클램프라 이보다 길어도 어차피 보이지 않습니다.
SUMMARY_CHARS = 300
HEADLINE_CHARS = 60
ORG_CHARS = 40
METRICS_MAX = 3          # 지표는 최대 3개 (설계 확정값)
METRIC_FIELD_CHARS = 40
# 브리핑은 1~2문장 규격. 200자는 그 상한을 감싼 안전판이며 화면 .bf-s 가 잘라 보여준다.
BRIEF_CHARS = 200
KEYWORD_CHARS = 20       # 키워드 1개 길이 상한. 화면 칩이 한 줄로 들어가는 폭

SYSTEM = (
    "당신은 SK이노베이션 계열의 O/I(운영개선) 과제 발굴을 지원하는 외부 동향 분석가다. "
    "모든 출력은 한국어로 쓰고, 지정된 JSON 객체 하나만 출력한다. "
    "자료에 없는 사실·수치를 만들어 내지 않는다."
)

PROMPT = """아래 [자료]를 읽고 JSON 객체 하나만 출력하라. 코드펜스·설명·주석을 붙이지 마라.

이 자료는 SK이노베이션이 **벤치마크 목적으로 감시하는 외부 기업·토픽**의 공시·보고서·뉴스다.
자료의 주체가 SK 계열사가 아닌 것은 당연하므로 그 이유로 감점하지 마라.
평가할 것은 "이 외부 동향이 SK 계열사의 O/I 과제 발굴에 어떤 시사점을 주는가"이다.

────────────────────────────────
1. 사실 원칙 — 가장 중요
────────────────────────────────
- [자료]에 적힌 것만 쓴다. 배경지식으로 보충하거나 추측으로 메우지 마라.
- 본문이 "(본문 없음)"이거나 제목을 되풀이한 수준이면 다음을 지킨다.
    · summary 는 제목이 말하는 사실만 1~2문장으로 재진술한다.
    · headline 은 빈 문자열("")로 둔다.  metrics 는 []로 둔다.
    · importance 는 40을 넘기지 않는다.  case_worthy 는 false 로 둔다.
- 수치는 원문에 있는 값만 옮긴다. 반올림·환산·추정 금지.
- 확인되지 않은 인과("~때문에 ~했다")를 쓰지 마라. 자료가 그렇게 서술한 경우에만 쓴다.

────────────────────────────────
2. 한국어 문체 규칙
────────────────────────────────
- summary 는 **한 문단**이다. 줄바꿈, 불릿(-, ·, •), 번호를 절대 넣지 마라.
- summary 는 3문장(본문이 없으면 1~2문장), 전체 90~160자.
- 종결은 개조식(명사형)으로 맺는다:
    "…설명." "…밝힘." "…제시." "…기재." "…공시." "…분석." "…언급." "…평가."
    "…지적." "…소개." "…부연." "…검토." "…제시됨." "…다뤄짐."
  "…입니다" "…합니다" "…한다" "…했다." 같은 서술형 종결은 쓰지 마라.
- 첫 문장은 자료 유형으로 연다:
    "분기 공시에서 …", "2분기 실적발표 콜에서 …", "IR 자료에서 …",
    "연차보고서에서 …", "중기경영계획 자료에서 …", "주간 시황 리포트에서 …",
    "업계 공동 검토 자료에서 …", "보도에 따르면 …"
- 주어(회사명)를 반복하지 마라. 발표 주체는 화면에 따로 표시된다.
- 세 번째 문장에는 가능하면 전제·단서·한계를 담는다.
    "다만 …", "…점도 지적", "…이 선행되어야 한다고 언급", "…문제가 있어 …조정했다고 부연"
- headline 은 18~34자의 **명사구**로 끝낸다. 마침표·따옴표·회사명·매체명을 넣지 마라.
    예) "정기보수(TA) 공정 표준화·병렬화로 공기 단축"
        "머신비전 기반 전수검사 전환으로 셀 수율 개선"
        "연 10억 달러 규모 비용절감 프로그램 영역별 진척"
        "컨테이너 해상운임 지수 하락세 지속"
- reason 도 개조식 1문장으로 맺는다.

────────────────────────────────
3. 표기 규칙
────────────────────────────────
A. 고유명사 — 영문 원문을 한국어로 옮길 때
   - 국내에서 영문 사명이 그대로 통용되는 기업은 영문을 유지한다:
     Dow, LyondellBasell, Valero, Cheniere, CATL, ExxonMobil, Chevron, BASF, Shell.
   - 한국어 표기가 통용되는 기업·기관은 한국어로 쓴다:
     미쓰이화학, 아사히카세이, 스미토모화학, 롯데케미칼, 에쓰오일, 포스코인터내셔널,
     대한석유협회.
   - 설비·공정·기술 용어는 한국어 통용어를 쓰되 원문 약어를 괄호로 병기한다:
     정기보수(TA), 나프타분해설비(NCC), 소모성 자재(MRO), 전수검사, 머신비전, 예지보전.
   - 한국어 문장에서 이미 굳어진 약어는 그대로 쓴다: NCC, TA, MRO, E&P, LNG, IR, 오펙스, CAPEX.
   - 영문 문장을 그대로 옮기지 마라. 항상 한국어 문장으로 다시 쓴다.
B. 숫자
   - 원문 단위를 유지한다: 10억 달러, 9,650억원, 12일, 3.2%, 배럴당 1.5달러, 249만 톤.
   - 네 자리 이상 정수에는 천 단위 쉼표를 넣는다.
   - 회계기간은 원문 표기를 따른다: FY2025, 2026년 2분기, 2026.03.
   - 원문에 수치가 없으면 만들지 말고 방향만 쓴다: "단축", "확대", "축소".
C. org — 자료가 다루는 주체
   - 매체명이 아니다. 자료가 다루는 **기업·기관**의 표기다.
   - 감시 대상과 본문의 주체가 다르면 본문의 주체를 쓴다.
     예) 감시 대상이 "롯데케미칼"이어도 기사가 여천NCC 를 다루면 org 는 "여천NCC".
   - 표기는 3-A 규칙을 따른다.
   - 판단이 서지 않으면 [자료]의 '발표 주체' 값을 그대로 쓴다.

────────────────────────────────
4. 분류값 — 아래 목록 밖의 값은 폐기된다
────────────────────────────────
theme — 반드시 아래 7개 중 **하나만** 고른다. 판정 기준:
  정비·설비 신뢰성 : 정기보수(TA)·예방/예지 정비·정비 주기 재설계·설비 고장·비계획 정지
  에너지·유틸리티 : 전력·스팀·연료비·에너지 원단위·자가발전·요금제·피크 관리
  구매·조달       : 구매 단가·통합 입찰·소모성 자재(MRO)·규격 표준화·공급사 관리
  공정 수율·품질   : 수율·불량·검사·재작업·품질 관리·공정 개선
  물류·계약       : 운임·해상운송·용선·창고·배송·장기 운송계약 협상
  간접비·원가구조 : 판관비·간접비·지원 기능 통합·조직 재편·원가구조 전반의 절감 프로그램
  가동률·운전자본 : 가동률 조정·감산·설비 통합·재고·회전일수·운전자본
  → 두 축 이상에 걸치면 **자료가 가장 많은 분량을 할애한 축**을 고른다.
  → 어느 축도 아니면 자료의 비용·원가 서술이 가장 가까운 축을 고른다. 빈 값은 허용되지 않는다.

levers — 해당하는 것만 고른다. 없으면 []:
  "비용 절감" / "수익 증대" / "운영 효율"

affiliates — 이 동향이 **시사점을 주는** SK 계열사 코드.
  자료 주체가 그 계열사인지가 아니라, 같은 사업을 하는 계열사가 어디인지로 판단한다
  (정유사 자료 → SKE, 석화사 자료 → SKGC, 배터리사 자료 → SKO).
  SKE(SK에너지·정유) SKGC(SK지오센트릭·석화/리사이클) SKEN(SK엔무브·윤활/열관리)
  SKIPC(SK인천석유화학) SKTI(SK트레이딩인터내셔널) SKEO(SK어스온·E&P)
  SKO(SK온·배터리) SKIET(SKIET·분리막) SKES(SK E&S·LNG/전력)

metrics — 원문에 **숫자로** 적힌 핵심 지표만 최대 3개. 없으면 [].
  label  : 한국어 지표명 8자 이내 (예: "TA 공기", "절감 목표", "영업이익", "운임 지수")
  value  : 단위를 포함한 원문 값 (예: "12일 → 9일", "연 10억 달러", "9,650억원", "3.2% 하락")
  period : 그 값이 속한 기간. 없으면 "" (예: "FY2025", "2026년 2분기", "2026~2028")
  → 원문에 없는 지표를 만들지 마라. 본문이 없으면 반드시 [].

keywords — 이 자료의 **동향 키워드** 최대 4개. 없으면 [].
  화면 트렌드룸의 키워드 칩·필터에 그대로 찍히는 말이라 아래를 지킨다.
  - 명사구 2~8자. 회사명·매체명·날짜·숫자는 넣지 마라.
  - levers 3종("비용 절감"…)처럼 뭉뚱그린 말이 아니라 **무엇을 건드렸는지** 를 쓴다:
    "정기보수", "공기 단축", "통합 조달", "전수검사", "해상운임", "자가발전", "안전재고".
  - 중요한 것부터 나열한다. 앞자리가 화면 칩의 첫 칸이다.

brief — 트렌드룸 '데일리 브리핑' 카드 1~2문장. 근거가 없으면 "".
  **무슨 일이 있었고 우리에게 무슨 의미인지**를 쓴다. 개조식 종결(…했습니다./…입니다.).
  - summary(사실 재진술)·reason(중요도 판단 근거)과 목적이 다르다. 셋을 같은 문장으로 쓰지 마라.
  - 자료의 쓸모를 깎아내리는 평가문("사례성은 제한적임")은 brief 가 아니다 — 그건 reason 이다.
  - 본문이 없어 할 말이 없으면 억지로 짓지 말고 빈 문자열을 낸다(화면이 summary 로 폴백한다).

case_worthy — 구체적인 손익개선·혁신 '사례'(무엇을 어떻게 바꿨는지)가 담겼으면 true.
  단순 실적 발표·목차·시황·인사·투자 계획 발표는 false.

importance — 0~100. 구체적 개선 수단과 수치가 있으면 높게, 일반적 실적·시황이면 낮게.
  본문이 없으면 40을 넘기지 마라.

────────────────────────────────
5. 출력 형식
────────────────────────────────
아래 키를 **모두** 가진 JSON 객체 하나만 출력한다. 값이 없으면 빈 문자열 또는 빈 배열을 쓴다.

{{"headline": "한국어 한 줄 제목 18~34자, 명사구 종결, 마침표·회사명 없음",
  "summary": "단일 문단 3문장 90~160자, 개조식 종결, 줄바꿈·불릿 금지",
  "org": "자료가 다루는 주체 기업·기관 표기",
  "theme": "정비·설비 신뢰성 | 에너지·유틸리티 | 구매·조달 | 공정 수율·품질 | 물류·계약 | 간접비·원가구조 | 가동률·운전자본 중 하나",
  "levers": ["비용 절감" | "수익 증대" | "운영 효율"],
  "affiliates": ["SKE" | "SKGC" | "SKEN" | "SKIPC" | "SKTI" | "SKEO" | "SKO" | "SKIET" | "SKES"],
  "metrics": [{{"label": "지표명", "value": "단위 포함 값", "period": "기간 또는 빈 문자열"}}],
  "keywords": ["동향 키워드 명사구 최대 4개"],
  "brief": "무슨 일이 있었고 우리에게 무슨 의미인지 1~2문장, 개조식 종결. 근거 없으면 빈 문자열",
  "case_worthy": true,
  "importance": 0,
  "reason": "중요도 판단 근거 1문장, 개조식 종결"}}

[자료]
제목: {title}
발표 주체: {source}
매체·발행처: {publisher}
자료 종류: {kind_label}
발행일: {published_on}
본문 수준: {body_note}
본문: {body}
"""

# codex `exec --output-schema <파일>` 용. OpenAI structured outputs 의 strict 부분집합만 쓴다.
#   · 최상위는 반드시 object (type:"array" 는 HTTP 400 invalid_json_schema)
#   · 모든 object 노드에 properties 전 키가 required, additionalProperties:false
#   · minLength/maxLength/minimum/maximum/pattern 은 거부되거나 무시된다 →
#     길이·개수·범위 제약은 프롬프트 문구와 _parse() 후처리가 강제한다
#   · 판단 기준(0~100 등)은 type 만으로 전달되지 않으므로 description 안에 넣는다
OUTPUT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    # ★ keywords · brief 도 required 에 넣는다. 위 규칙("properties 전 키가 required")은
    #   OpenAI strict structured outputs 의 하드 제약이라, 빼면 codex 경로가 통째로
    #   HTTP 400 invalid_json_schema 로 죽는다. 값이 없을 때는 빈 배열·빈 문자열을
    #   내도록 프롬프트가 지시하고, _parse 가 다시 한 번 정규화한다
    #   (headline·org·reason 도 같은 방식이다).
    "required": ["headline", "summary", "org", "theme", "levers", "affiliates",
                 "metrics", "keywords", "brief", "case_worthy", "importance", "reason"],
    "properties": {
        "headline": {
            "type": "string",
            "description": "한국어 한 줄 제목. 18~34자 명사구, 마침표·회사명·매체명 없음. 근거가 없으면 빈 문자열",
        },
        "summary": {
            "type": "string",
            "description": "단일 문단 3문장 90~160자. 개조식 종결(…설명./…밝힘./…제시.). 줄바꿈·불릿 금지",
        },
        "org": {
            "type": "string",
            "description": "자료가 다루는 주체 기업·기관 표기. 매체명이 아님. 영문 사명이 통용되면 영문 유지",
        },
        "theme": {
            "type": "string",
            "enum": list(classify.THEMES),
        },
        "levers": {
            "type": "array",
            "items": {"type": "string", "enum": LEVERS},
        },
        "affiliates": {
            "type": "array",
            "items": {"type": "string", "enum": list(AFFILIATE_CODES)},
        },
        "metrics": {
            "type": "array",
            "description": "원문에 숫자로 적힌 핵심 지표 최대 3개. 없으면 빈 배열",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["label", "value", "period"],
                "properties": {
                    "label": {"type": "string", "description": "한국어 지표명 8자 이내"},
                    "value": {"type": "string", "description": "단위를 포함한 원문 값"},
                    "period": {"type": "string", "description": "값이 속한 기간. 없으면 빈 문자열"},
                },
            },
        },
        # ★ keywords · brief 는 required 에 넣지 않는다. 이미 검증된 정제 경로를
        #   흔들지 않기 위해서다 — 모델이 빠뜨려도 _parse 가 빈 값으로 정규화하고,
        #   evKw 는 사전 추출(farming/keywords.py)이 주(主)라 비어도 화면이 산다.
        "keywords": {
            "type": "array",
            "description": "동향 키워드 명사구 2~8자 최대 4개. 회사명·숫자 금지. 중요한 것부터",
            "items": {"type": "string"},
        },
        "brief": {
            "type": "string",
            "description": "트렌드룸 브리핑 1~2문장. 무슨 일이 있었고 우리에게 무슨 의미인지."
                           " 개조식 종결. 근거가 없으면 빈 문자열",
        },
        "case_worthy": {
            "type": "boolean",
            "description": "구체적 손익개선·혁신 사례가 담겼으면 true. 단순 실적·시황은 false",
        },
        "importance": {
            "type": "integer",
            "description": "0~100. 본문이 없으면 40 이하",
        },
        "reason": {"type": "string", "description": "중요도 판단 근거 1문장, 개조식 종결"},
    },
}


def provider_ready() -> tuple[bool, str]:
    """정제에 쓸 provider 를 사용할 수 있는지와 그 사유."""
    return llm_client.ready(OI_LLM_PROVIDER)


def naive_summary(doc: RawDoc, limit: int = 200) -> str:
    """LLM 없이 쓰는 폴백 요약 — 본문/제목 절삭.

    폴백이라도 화면 규격(단일 문단)은 지켜야 한다. DART 정기보고서 본문은 표지·표가
    개행투성이라 그대로 넣으면 트렌드룸 카드가 깨진다.

    ⚠ meta['body_restricted'] 가 서 있으면 본문을 쓰지 않는다 — 뉴스 본문은 매체의
      저작물이라 정제 입력으로만 허용된다(news.fetch_body 주석 참고). 원문 앞 200자를
      요약 자리에 넣으면 그 발췌가 DB 에 그대로 남으므로 제목으로 되돌린다.
      대신 llm.enrich 가 본문 있는 건을 먼저 정제하므로, 확보한 뉴스는 LLM 요약을 받는다.

    ★ 쓸 본문이 없으면 **빈 문자열을 돌려준다.** 예전에는 제목을 그대로 복사했는데,
      그러면 화면 카드에 같은 문장이 제목·요약으로 두 번 찍히고(실측 45/56건)
      "정제된 것처럼" 보여 근거로 쓸 수 없다는 사실이 가려진다.
      요약이 비면 evidence_grade='제목만' 과 함께 "원문 미확보" 로 읽힌다.
    """
    body = "" if (getattr(doc, "meta", None) or {}).get("body_restricted") else doc.body
    if not (body or "").strip():
        return ""
    text = _one_paragraph(body)[:limit]
    # 본문이 제목을 그대로 반복하는 경우(RSS description 등)도 요약으로 치지 않는다.
    return "" if _one_paragraph(text) == _one_paragraph(doc.title or "") else text


def _blank(doc: RawDoc) -> dict:
    return {
        "summary": naive_summary(doc), "levers": [], "affiliates": [],
        "case_worthy": False, "importance": None, "reason": "", "enriched": False,
        "headline": "", "org": "", "theme": None, "metrics": [],
        # 키워드는 ingest 가 사전 추출(farming/keywords.py)로 채우고, brief 는 LLM 전용이라
        # 폴백에서는 빈 값이다 — 화면이 EV_BRIEF 대신 요약(e.sum)으로 폴백한다.
        "keywords": [], "brief": "",
    }


def _one_paragraph(text: str) -> str:
    """개행·불릿·연속 공백을 제거해 단일 문단으로 만든다.

    화면 `.tr2-s` 는 `-webkit-line-clamp:2` 에 `white-space:pre` 가 없어 개행이 공백으로
    붕괴되고 세 번째 줄이 잘린다. 모델이 규칙을 어기고 불릿을 내도 DB 에는 문단만 들어가게 한다.
    """
    s = " ".join(str(text or "").split())
    for bullet in ("- ", "· ", "• ", "* "):
        if s.startswith(bullet):
            s = s[len(bullet):]
    # 문장 사이에 남은 불릿 마커도 없앤다 ('… 설명. - 두 번째 …')
    for bullet in (" - ", " · ", " • ", " * "):
        s = s.replace(bullet, " ")
    return s.strip()


def _metrics(raw) -> List[dict]:
    """metrics 를 [{label,value,period}] 로 정규화한다. 형태가 아니면 버린다."""
    out: List[dict] = []
    for item in (raw or [])[:METRICS_MAX]:
        if not isinstance(item, dict):
            continue
        label = _one_paragraph(item.get("label"))[:METRIC_FIELD_CHARS]
        value = _one_paragraph(item.get("value"))[:METRIC_FIELD_CHARS]
        if not label or not value:
            continue  # 라벨·값이 없는 지표는 화면에 쓸 수 없다
        out.append({
            "label": label,
            "value": value,
            "period": _one_paragraph(item.get("period"))[:METRIC_FIELD_CHARS],
        })
    return out


def _keywords(raw) -> List[str]:
    """동향 키워드를 [표시형] 로 정규화한다.

    화면 칩에 그대로 찍히므로 공백 정리 · 길이 상한 · 중복 제거까지 여기서 끝낸다.
    개수 상한은 keywords.KEYWORDS_MAX 하나만 본다 — 사전 추출과 같은 규격이어야
    ingest 가 두 출처를 이어 붙일 때 자릿수가 어긋나지 않는다.
    """
    out: List[str] = []
    for item in (raw or []):
        word = _one_paragraph(item)[:KEYWORD_CHARS]
        if word and word not in out:
            out.append(word)
    return out[:KEYWORDS_MAX]


def _parse(raw: str) -> dict:
    """모델 응답에서 JSON 을 꺼내 화이트리스트로 정규화한다.

    codex 는 `--output-schema` 로 형태가 보장되지만, 화이트리스트·클램프는 **이중 방어로
    남긴다** — 스키마를 못 쓰는 provider(claude-cli/openai/anthropic)가 같은 코드를 타고,
    enum 밖의 theme 하나가 feed_item.theme FK 를 깨뜨리기 때문이다.
    """
    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    start, end = clean.find("{"), clean.rfind("}")
    if start == -1 or end == -1:
        # 무엇이 돌아왔는지 남긴다 — 안 그러면 원인 추적이 불가능하다.
        raise ValueError(f"JSON 을 찾지 못했습니다: {clean[:160]!r}")
    data = json.loads(clean[start:end + 1])

    try:
        importance = int(data.get("importance", 50))
    except (TypeError, ValueError):
        importance = 50

    return {
        "headline": _one_paragraph(data.get("headline"))[:HEADLINE_CHARS],
        "summary": _one_paragraph(data.get("summary"))[:SUMMARY_CHARS],
        "org": _one_paragraph(data.get("org"))[:ORG_CHARS],
        # 목록 밖이면 None → ingest 가 classify.theme_by_rule 로 폴백한다.
        "theme": classify.valid_theme(data.get("theme")),
        "levers": [x for x in (data.get("levers") or []) if x in LEVERS],
        "affiliates": [x for x in (data.get("affiliates") or []) if x in AFFILIATE_CODES],
        "metrics": _metrics(data.get("metrics")),
        # 동향 키워드 — 사전 추출(farming/keywords.py)보다 앞자리에 놓인다(ingest.store).
        "keywords": _keywords(data.get("keywords")),
        # 트렌드룸 브리핑. summary(사실 재진술)·reason(중요도 근거)과 목적이 다르다.
        "brief": _one_paragraph(data.get("brief"))[:BRIEF_CHARS],
        "case_worthy": bool(data.get("case_worthy", False)),
        "importance": max(0, min(100, importance)),
        "reason": _one_paragraph(data.get("reason")),
    }


# O/I 관점에서 신호가 있는 구간을 찾는 키워드.
# 정기보고서는 앞부분이 표지·목차라 단순 절삭하면 알맹이를 통째로 버리게 됩니다
# (실측: S-Oil 분기보고서 159,534자 중 '원가'는 13,739자, '매출원가'는 40,398자 지점에서 첫 등장).
SIGNAL_WORDS = [
    "원가", "매출원가", "가동률", "생산능력", "정기보수", "설비투자", "수율",
    "물류비", "절감", "효율", "에너지", "전력", "고정비", "수익성", "마진",
    "cost", "efficiency", "margin", "productivity", "savings", "utilization",
]
# 그중에서도 **먼저 담아야 하는** 말. 나머지(에너지·전력·효율 …)는 표지·회사 개요·연혁에서
# 먼저 터져서, 문서 순서대로 예산을 채우면 정작 원가·가동률 구간에 닿기 전에 예산이 바닥난다.
# 실측(정기보고서 6건, 예산 4,000자): 문서 순서만 쓰면 핵심어 커버 12/54,
# 롯데케미칼 분기보고서는 발췌 4,012자가 **전부 표지**였다. 핵심어를 먼저 담으면 20/54 이고
# 6건 모두 '가동률·생산능력' 구간이 들어온다.
CORE_SIGNAL_WORDS = {
    "원가", "매출원가", "가동률", "생산능력", "정기보수", "설비투자", "수율",
    "물류비", "절감", "고정비", "cost", "utilization", "margin",
}
# 키워드 앞뒤로 확보할 문맥. 뒤를 더 크게 잡는 이유는 수치가 키워드 뒤에 오기 때문이다
# ("매출원가는 ... 조원으로 전년 대비 ...%"). 앞300/뒤700 과 앞200/뒤800 은 실측 동점.
WINDOW_BACK = 300
WINDOW_FWD = 700
HEAD_CHARS = 800      # 발췌 앞에 붙일 도입부 (무슨 문서인지 알려주는 용도)


def select_excerpt(body: str, budget: int = BODY_CHARS) -> str:
    """본문에서 O/I 신호가 있는 구간만 발췌한다.

    budget 안에 들어가면 그대로 두고, 넘칠 때만 키워드 주변을 골라냅니다.
    신호가 하나도 없으면 앞부분 절삭으로 되돌립니다(뉴스·짧은 공시).

    담는 순서는 **핵심어 먼저, 그다음 문서 순서**입니다(CORE_SIGNAL_WORDS 주석 참고).
    출력은 다시 문서 순서로 되돌려 붙이므로 읽는 사람에게는 앞에서 뒤로 흐릅니다.
    """
    if len(body) <= budget:
        return body

    low = body.lower()
    hits = []
    for word in SIGNAL_WORDS:
        rank = 0 if word in CORE_SIGNAL_WORDS else 1
        start = 0
        while True:
            i = low.find(word.lower(), start)
            if i == -1:
                break
            hits.append((rank, i))
            start = i + len(word)

    if not hits:
        return body[:budget]

    head = body[:HEAD_CHARS]
    room = budget - len(head)
    hits.sort()                       # (핵심어 여부, 문서 위치)

    taken: List[tuple] = []
    used = 0
    for _rank, i in hits:
        if used >= room:
            break
        s = max(0, i - WINDOW_BACK)
        e = min(len(body), i + WINDOW_FWD)
        # 이미 담은 구간과 겹치면 건너뛴다. 같은 내용을 두 번 실어 예산을 낭비하지 않는다.
        if any(s < t_e and t_s < e for t_s, t_e in taken):
            continue
        # 남은 예산만큼만. **뒤에서** 자른다 — 앞에서 자르면 구간 가운데 있는 키워드가
        # 통째로 잘려 나가 신호가 없는 조각만 남는다(실측: 그 경우 커버가 0이 됐다).
        e = min(e, s + (room - used))
        taken.append((s, e))
        used += e - s

    taken.sort()
    return "\n…\n".join([head] + [body[s:e] for s, e in taken])


def body_for_prompt(doc: RawDoc) -> str:
    """프롬프트에 실제로 들어가는 본문 발췌.

    evidence_grade 는 '이 요약이 무엇을 보고 만들어졌는가' 이므로 원본 body 길이가 아니라
    이 값의 길이로 판정해야 합니다. ingest 가 같은 함수를 써서 등급을 매깁니다.
    """
    return select_excerpt(doc.body or "")


def build_prompt(doc: RawDoc) -> str:
    excerpt = body_for_prompt(doc)
    kind_label, _ = classify.kind_of(doc)
    return PROMPT.format(
        title=doc.title,
        source=doc.source,
        publisher=doc.publisher or "(없음)",
        kind_label=kind_label,
        published_on=doc.published_on,
        body_note=classify.evidence_grade_of(len(excerpt)),
        body=excerpt or "(본문 없음)",
    )


def enrich_one(doc: RawDoc) -> dict:
    """문서 1건을 정제한다. 실패하면 예외를 올린다 (호출 측에서 격리).

    provider 가 스키마를 강제할 수 있으면(codex-cli) 1회 호출로 끝냅니다 — 형태가 서버측에서
    보장되므로 재시도가 낭비입니다. 아니면 기존 2회 경로를 유지합니다: 모델이 JSON 대신
    산문을 내놓는 일이 가끔 있고 재시도 한 번으로 대부분 회복됩니다.
    네트워크/프로세스 오류는 어느 경로에서도 재시도하지 않습니다.
    """
    prompt = build_prompt(doc)

    if llm_client.supports_schema(OI_LLM_PROVIDER):
        return _parse(llm_client.call(
            prompt, SYSTEM, OI_LLM_MODEL, OI_LLM_PROVIDER, schema=OUTPUT_SCHEMA,
        ))

    def ask(text: str) -> str:
        return llm_client.call(text, SYSTEM, OI_LLM_MODEL, OI_LLM_PROVIDER)

    try:
        return _parse(ask(prompt))
    except (ValueError, json.JSONDecodeError):
        return _parse(ask(prompt + "\n\n반드시 JSON 객체 하나만 출력하라. 설명·코드펜스 금지."))


def enrich(docs: Sequence[RawDoc], limit: int = 12, use_llm: bool = True) -> List[dict]:
    """수집 문서를 정제해 docs 와 같은 순서의 결과 목록을 반환한다.

    비용 통제를 위해 본문이 있는 문서를 우선해 limit 건까지만 LLM 을 호출하고,
    나머지(및 실패 건)는 naive 요약으로 채웁니다.

    ★ **본문이 없는 문서는 아예 호출하지 않는다.** limit 를 크게 잡아도 마찬가지다.
      재료가 없으면 모델은 "본문이 없어 구체적인 내용은 확인되지 않음" 같은
      정보량 0인 문장을 지어낸다(실측). 그건 요약이 아니라 요약처럼 보이는 것이고,
      화면에서 '원문 미확보' 라는 사실을 가린다. 호출도 낭비다.
    """
    results: List[dict] = [_blank(d) for d in docs]
    if not use_llm or not docs:
        return results

    ready, why = provider_ready()
    if not ready:
        print(f"[llm] {why} — naive 요약으로 대체")
        return results

    # 본문이 있는 문서만 대상으로 삼는다(위 ★ 참고). 그 안에서 limit 로 자른다.
    targets = [i for i, d in enumerate(docs) if (d.body or "").strip()][:limit]
    skipped = len(docs) - len(targets)
    if skipped:
        print(f"[llm] 본문 없는 {skipped}건은 정제하지 않습니다 (원문 미확보로 남김)")

    def work(i: int):
        return i, enrich_one(docs[i])

    print(f"[llm] {OI_LLM_PROVIDER}/{OI_LLM_MODEL} — {len(targets)}건 정제 시작 "
          f"(동시 {OI_LLM_CONCURRENCY})")
    done = 0
    # claude-cli 는 호출당 20초 안팎이라 순차 처리하면 배치가 너무 길어집니다.
    with ThreadPoolExecutor(max_workers=max(1, OI_LLM_CONCURRENCY)) as pool:
        for future in [pool.submit(work, i) for i in targets]:
            try:
                i, data = future.result()
            except Exception as e:
                # 항목 단위 격리 — 한 건 실패가 전체를 중단시키지 않게
                print(f"[llm] ✗ {type(e).__name__}: {str(e)[:120]}")
                continue
            results[i] = {**data, "enriched": True}
            done += 1
            print(f"[llm] ✓ [{data['importance']:>3}] {docs[i].title[:44]} → {data['affiliates']}")

    print(f"[llm] 정제 {done}/{len(targets)}건")
    return results
