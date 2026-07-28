"""API 입출력 스키마."""
from typing import List, Optional

from pydantic import BaseModel, Field


class Kpi(BaseModel):
    name: str = "-"
    formula: str = "-"


class FeedItem(BaseModel):
    id: str
    d: str            # published_on (프론트 데이터 형태와 일치)
    kind: str
    src: str
    title: str
    sum: str
    tags: List[str] = []
    url: Optional[str] = None


# ── 과제 발굴 ──
class GenerateRequest(BaseModel):
    aff: str
    note: str = ""


class TaskDraft(BaseModel):
    title: str
    category: str = "기타"
    background: str = ""
    plan: str = ""
    risk: str = ""
    effect: str = ""
    kpi: Kpi = Field(default_factory=Kpi)
    evidence: List[str] = []


class GenerateResponse(BaseModel):
    tasks: List[TaskDraft]


# ── 과제 기록 ──
class TaskIn(BaseModel):
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


class TaskOut(TaskIn):
    id: str


class DeleteRequest(BaseModel):
    ids: List[str]


# ── 혁신 사례 ──
class InnovationCase(BaseModel):
    id: int
    title: str
    category: str = ""
    background: str = ""
    effect: str = ""
    kpi: Kpi = Field(default_factory=Kpi)
    sourceOrg: str = ""
    sourceType: str = "manual"   # manual / ai / auto
    sourceRef: str = ""
    status: str = "approved"     # approved / pending / rejected
    affiliates: List[str] = []
    createdAt: Optional[str] = None


class CaseCreate(BaseModel):
    title: str
    category: str = ""
    background: str = ""
    effect: str = ""
    kpiName: str = "-"
    kpiFormula: str = "-"
    sourceOrg: str = ""
    sourceType: str = "manual"
    sourceRef: str = ""
    status: str = "approved"
    affiliates: List[str] = []


class CaseStatusUpdate(BaseModel):
    status: str  # approved / pending / rejected


# ── 과제 평가 ──
class ValidationIssue(BaseModel):
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
    scoredBy: str = "heuristic"    # llm / heuristic


class EvaluatedTask(BaseModel):
    task: TaskDraft
    evaluation: Evaluation


class EvaluateRequest(BaseModel):
    aff: str
    tasks: List[TaskDraft]
    topN: Optional[int] = None
    useLlm: bool = True
    checkSaved: bool = True


class EvaluateResponse(BaseModel):
    results: List[EvaluatedTask]   # priority 내림차순, blocked 는 뒤로
    criteria: str                  # 선정 기준 설명 (사용자·봇 노출용)
    weights: dict = {}
    passed: int = 0
    review: int = 0
    blocked: int = 0


# ── 제안서 ──
class ProposalPhase(BaseModel):
    name: str
    duration: str = ""
    activities: List[str] = []
    deliverable: str = ""


class Proposal(BaseModel):
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


class ProposalRequest(BaseModel):
    task: TaskIn
    useLlm: bool = True
