"""API 입출력 스키마."""
from typing import List, Optional

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


class AdminUserIn(BaseModel):
    email: str
    password: Optional[str] = None   # 미지정 시 초기비번 1111
    is_admin: bool = False


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
