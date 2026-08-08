"""API 입출력 스키마."""
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Kpi(BaseModel):
    name: str = "-"
    formula: str = "-"


# ── 인증 ──
class LoginIn(BaseModel):
    email: str
    password: str


class ChangePwIn(BaseModel):
    current_password: str
    new_password: str


# 관리자가 만드는 **로그인 계정**. 화면 표시용 명단이 아니라 app_user 그 자체라
# 관리자 섹션이 아니라 이 인증 섹션에 둔다.
# password 는 프론트가 보내지 않는다 — 서버가 기본 '1111' 을 쓴다(seed_users 기본값과 동일).
class AdminUserIn(BaseModel):
    email: str
    password: Optional[str] = None
    is_admin: bool = False


class FeedItem(BaseModel):
    id: str
    d: str            # published_on (프론트 데이터 형태와 일치)
    kind: str
    src: str
    title: str
    sum: str          # 정제 시 3줄 요약(개행 포함), 아니면 naive 절삭
    tags: List[str] = []
    url: Optional[str] = None
    # ── 지식 파밍 정제 결과 (farming/llm.py). 미정제면 기본값 ──
    levers: List[str] = []
    importance: Optional[int] = None    # 0~100. top-n 선정 기준
    reason: str = ""                    # 중요도 판단 근거
    caseWorthy: bool = False            # 혁신사례 승격 후보
    enriched: bool = False              # LLM 정제 여부


# ── 과제 발굴 ──
# 발굴 요청/응답 스키마는 없다. 'OC 지정 + note 주입' 은 커스텀 생성 화면이 담당하고
# 그 입력은 아래 CustomProposalIn 이다(→ store.create_custom_llm).


class TaskDraft(BaseModel):
    """발굴 LLM 이 만든 과제 초안 1건.

    ★ title · category · kpi 는 **개명하지 않는다.** 평가 파이프라인(validator/scorer)이
      task.title / task.category / task.kpi 를 그대로 읽는다. 필드는 추가만 한다.
      발굴 agent._parse 가 정규화된 레버를 category 와 lever 두 곳에 같은 값으로 넣는다 —
      category 는 평가 쪽 호환용, lever 는 저장 경로(persist)가 보는 값이다.
    """
    title: str
    category: str = "기타"
    background: str = ""
    plan: str = ""
    risk: str = ""
    effect: str = ""
    kpi: Kpi = Field(default_factory=Kpi)
    evidence: List[str] = []
    lever: str = ""             # lever 마스터 정식명. 정규화 실패 시 빈 문자열 → 저장 skip
    summary: str = ""           # 한 줄 요약 → proposal.summary
    kb_refs: List[str] = []     # 근거로 쓴 내부 지식 문서 id → proposal.kb_refs


# ── 과제 기록 ──
class ProposalDocIn(BaseModel):
    id: Optional[str] = None
    createdAt: str
    aff: str
    title: str
    category: str = ""
    background: str = ""
    plan: str = ""
    risk: str = ""
    effect: str = ""
    kpiName: str = "-"
    kpiFormula: str = "-"
    evidence: List[str] = []
    status: str = "검토중"
    origin: str = "생성"


# ── 혁신 사례 ──
# 혁신 사례에는 API 도 입출력 스키마도 없다. 시드(app/db/seed_data.INNOVATION_CASES)로만
# 관리하고, 발굴 프롬프트가 쓸 때는 prefetch._case_block 이 테이블을 직접 SQL 로 읽는다.


# ★ 화면 응답 모델(과제 제안 · 생성 버전 · 근거 자료 · bootstrap)을 여기에 만들어
#   response_model 로 붙이지 마라 — 모델에 없는 키(evalScore·metrics 등)가 조용히
#   응답에서 사라진다(api/bootstrap.py 주석 참조). GET /api/bootstrap 은 일부러
#   response_model 없이 store.bootstrap() 의 dict 를 그대로 내보낸다.
#   '기존 8키는 이름·의미·순서 불변' 계약은 그 dict 를 만드는
#   store._proposals() / _versions() / _evidence() 의 docstring 이 지킨다.


class FeedbackIn(BaseModel):
    score: Optional[int] = None       # 0~5. None 이면 점수는 그대로 두고 memo 만 갱신
    memo: Optional[str] = None


class FieldsIn(BaseModel):
    fields: Dict[str, str] = {}


class FormulaIn(BaseModel):
    sysOff: bool = False
    text: Optional[str] = None


class CustomProposalIn(BaseModel):
    oc: str
    lever: str
    ev: List[str] = []
    plan: str = ""
    name: Optional[str] = None
    sum: Optional[str] = None
    # 유사 중복(duplicate_similar) 경고를 사용자가 확인하고 진행한 경우에만 True.
    # ★ 완전일치(duplicate_exact)는 이 값으로도 못 뚫는다 — 이름을 바꿔야 한다.
    force: bool = False


# ── 관리자 ──
class InstructionIn(BaseModel):
    text: str


# ★ AdminMemberIn(화면 표시용 관리자 명단)은 제거했다. 계정 관리 탭이 로그인 계정을
#   직접 다루므로 입력 스키마는 AdminUserIn(인증 섹션) 하나뿐이다.

# 내부 자료 업로드에는 입력 스키마가 없다 — 경로가 multipart 하나뿐이고
# (POST /api/admin/uploads/file), 승인 여부는 그 요청의 use_now 폼 필드로 정해진다.
# upload_file.status 값: 검수 대기 / 본문 추출됨 / 본문 미지원 / 검수 완료.


# ── AI Reporting ──
class ReportSettingIn(BaseModel):
    freq: Optional[str] = None
    time: Optional[str] = None
    channels: Optional[Dict[str, bool]] = None
    recipients: Optional[List[str]] = None
    sendOff: Optional[List[int]] = None


# ── 과제 평가 ──
class ValidationIssue(BaseModel):
    """검증 이슈 1건. severity 는 파이프라인 내부에서 block/warn 으로 두고,
    DB·화면에 나갈 때(runner 저장 경계) 차단/경고로 매핑한다."""
    code: str                      # MISSING_FIELD, NO_EVIDENCE, DUPLICATE ...
    severity: str                  # block / warn
    field: str = ""
    message: str


class ValidationResult(BaseModel):
    ok: bool                       # block 이슈 없음 = 사용자 노출 가능
    verdict: str                   # pass / review / blocked
    issues: List[ValidationIssue] = []


class AxisScore(BaseModel):
    score: float = 0.0             # 1.0 ~ 5.0
    reason: str = ""


class Evaluation(BaseModel):
    verdict: str                   # pass / review / blocked
    validation: ValidationResult
    impact: AxisScore = Field(default_factory=AxisScore)
    feasibility: AxisScore = Field(default_factory=AxisScore)
    roi: AxisScore = Field(default_factory=AxisScore)
    grounding: str = "unknown"     # supported / weak / unsupported / unknown
    groundingReason: str = ""
    priority: float = 0.0          # 0 ~ 100
    grade: str = "C"               # A / B / C
    rank: Optional[int] = None     # 통과 과제 내 순위 (1부터)
    scoredBy: str = "heuristic"    # llm / heuristic / none


class EvaluatedTask(BaseModel):
    task: TaskDraft
    evaluation: Evaluation


# ★ 과제 본문을 요청 바디로 받는 평가 스키마를 다시 만든다면 tasks 개수 상한
#   (max_length=50)을 반드시 함께 넣어라 — 한 요청이 codex 를 수십 회 부르면
#   라우트 하나가 수십 분을 점유한다. 지금 평가는 저장된 과제를 id 로 지정한다.


class EvaluationRunIn(BaseModel):
    """저장된 과제 재평가 범위. 셋 다 비우면 전량이다.

    useLlm=True 는 계열사당 수십 초라 반드시 비동기 작업(jobs)으로 돈다.
    """
    ids: List[int] = []
    ver: Optional[str] = None       # 생성 버전 id (예: g12)
    oc: Optional[str] = None        # 계열사 코드 (예: SKEO)
    useLlm: bool = False


# ── 제안서 문서 ──
class ProposalPhase(BaseModel):
    name: str
    duration: str = ""
    activities: List[str] = []
    deliverable: str = ""


class ProposalDoc(BaseModel):
    """제안서 문서 1건.

    ★ 이름을 `Proposal` 로 바꾸지 마라. 화면의 '과제 제안 1건'(store._proposals 가
      만드는 21키 dict)과 개념이 다른데 필드 교집합이 0이라, 이름이 겹치면 텍스트
      병합기가 잡아내지 못한 채 서로 다른 것이 같은 이름을 갖게 된다.
      화면 쪽 응답 모델은 지금 클래스가 아니라 store 의 dict 다(위 주석 참조).
    """
    taskId: str = ""
    title: str
    definition: str = ""           # 혁신 과제 정의
    expectedEffect: str = ""       # 기대효과
    kpiBaseline: str = ""
    kpiTarget: str = ""
    phases: List[ProposalPhase] = []       # 추진 logic
    prerequisites: List[str] = []          # 필요 사전 단계
    investmentItems: List[str] = []        # 예상 투자 비용
    investmentSummary: str = ""
    risks: List[str] = []
    evidence: List[str] = []
    generatedBy: str = "heuristic"         # llm / heuristic
