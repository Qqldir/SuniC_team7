"""과제 검증 — 결정적(deterministic) 게이트.

발굴 agent 가 만든 draft 가 '사용자에게 보여줄 만한가'를 LLM 없이 판정합니다.
LLM 출력의 형식·근거 오류는 LLM 에게 다시 묻지 않고 규칙으로 잡습니다.
(빠르고, 재현 가능하고, API 키 없이도 동작)

severity:
    block — 사용자 노출 불가. 목록에서 제외한다.
    warn  — 노출하되 플래그를 달아 검토를 유도한다.
"""
import re
from difflib import SequenceMatcher
from datetime import date
from typing import Iterable, List, Optional, Sequence

from app.config import TODAY
from app.db.database import get_connection
from app.models import TaskDraft, ValidationIssue, ValidationResult

# ─────────── 튜닝 파라미터 ───────────
MIN_TITLE_LEN = 6          # 과제명 최소 길이
MIN_TEXT_LEN = 15          # 배경/실행방안 최소 길이
EVIDENCE_MAX_AGE_DAYS = 90  # 근거 신선도 한계
DUP_THRESHOLD = 0.82       # 과제명 유사도(중복 판정)

PLACEHOLDER_TITLES = {"무제 과제", "제목 없음", "untitled", "-", "n/a"}

# 발굴 프롬프트가 지시하는 레버 분류
KNOWN_CATEGORIES = {
    "에너지비", "정비·TA", "정비/TA", "정비", "TA",
    "물류비", "수율", "구매", "간접비", "운전자본",
}

# 정량 신호: 숫자 또는 퍼센트
_QUANT_RE = re.compile(r"\d|[%％]")

# KPI 산출식이 '계산 가능한' 형태인지
_FORMULA_RE = re.compile(r"[/*×÷x+\-=]|대비|당\s|당$|비율|[%％]")

# 한국어 보고서 상투어 — 구체성이 없다는 신호
_VAGUE_PHRASES = [
    "적극 검토", "다각도로", "지속적으로 검토", "필요시 검토",
    "방안 마련", "제고 방안", "활성화 방안", "등등", "다양한 방법",
    "최선을 다", "노력한다", "추진할 예정",
]


# ─────────── 내부 조회 ───────────
def _feed_index(ids: Iterable[str]) -> dict:
    """근거 id → {published_on, affs} 매핑. 존재하지 않는 id 는 빠진다."""
    ids = [i for i in set(ids) if i]
    if not ids:
        return {}
    ph = ",".join("?" * len(ids))
    conn = get_connection()
    try:
        rows = conn.execute(
            f"""
            SELECT f.id, f.published_on, GROUP_CONCAT(t.aff_code) AS affs
            FROM feed_item f
            LEFT JOIN feed_item_tag t ON t.feed_id = f.id
            WHERE f.id IN ({ph})
            GROUP BY f.id
            """,
            ids,
        ).fetchall()
    finally:
        conn.close()
    return {
        r["id"]: {
            "published_on": r["published_on"],
            "affs": set((r["affs"] or "").split(",")) - {""},
        }
        for r in rows
    }


def _existing_titles(aff_code: str) -> List[str]:
    """같은 계열사에 이미 저장된 과제명 (중복 발굴 방지)."""
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT title FROM task WHERE aff_code = ?", (aff_code,)
        ).fetchall()
        return [r["title"] for r in rows]
    finally:
        conn.close()


def _ga(word: str) -> str:
    """받침 유무에 따라 주격조사 '이/가'를 고른다."""
    if not word:
        return "가"
    ch = word[-1]
    if "가" <= ch <= "힣":
        return "이" if (ord(ch) - 0xAC00) % 28 else "가"
    return "가"


def _norm(s: str) -> str:
    return re.sub(r"[\s·,./()\[\]-]", "", (s or "").lower())


def _similar(a: str, b: str) -> float:
    return SequenceMatcher(None, _norm(a), _norm(b)).ratio()


# ─────────── 개별 검사 ───────────
def validate_task(
    task: TaskDraft,
    aff_code: str,
    *,
    feed_idx: Optional[dict] = None,
    known_titles: Sequence[str] = (),
    today: str = TODAY,
) -> ValidationResult:
    """draft 1건을 검사한다.

    feed_idx / known_titles 를 주입하면 배치 처리 시 DB 재조회를 피할 수 있다.
    """
    issues: List[ValidationIssue] = []

    def add(code, severity, field, message):
        issues.append(
            ValidationIssue(code=code, severity=severity, field=field, message=message)
        )

    if feed_idx is None:
        feed_idx = _feed_index(task.evidence)

    # 1. 필수 필드
    for field, label in (
        ("title", "과제명"), ("background", "배경"),
        ("plan", "실행방안"), ("effect", "기대효과"),
    ):
        if not (getattr(task, field) or "").strip():
            add("MISSING_FIELD", "block", field, f"{label}{_ga(label)} 비어 있습니다.")

    # 2. 과제명 품질
    title = (task.title or "").strip()
    if title and title.lower() in PLACEHOLDER_TITLES:
        add("PLACEHOLDER_TITLE", "block", "title", "생성 실패 시의 기본값이 그대로 남아 있습니다.")
    elif title and len(title) < MIN_TITLE_LEN:
        add("TITLE_TOO_SHORT", "warn", "title", f"과제명이 {MIN_TITLE_LEN}자 미만입니다.")

    # 3. 본문 길이
    for field, label in (("background", "배경"), ("plan", "실행방안")):
        v = (getattr(task, field) or "").strip()
        if v and len(v) < MIN_TEXT_LEN:
            add("TOO_SHORT", "warn", field, f"{label} 설명이 지나치게 짧습니다.")

    # 4. 근거(evidence) — 가장 중요한 게이트
    if not task.evidence:
        add("NO_EVIDENCE", "block", "evidence", "외부 동향 근거가 없어 출처를 추적할 수 없습니다.")
    else:
        unknown = [e for e in task.evidence if e not in feed_idx]
        if unknown:
            # 유효한 근거가 하나도 남지 않을 때만 차단한다.
            # 일부만 잘못된 경우는 해당 id 를 떼고 검토 대상으로 넘긴다 — 과도한
            # 차단은 '후보를 많이 확보한다'는 발굴 목적과 충돌한다.
            all_bad = len(unknown) == len(task.evidence)
            add("UNKNOWN_EVIDENCE", "block" if all_bad else "warn", "evidence",
                f"존재하지 않는 근거 id: {', '.join(unknown)} (환각 가능성)"
                + ("" if all_bad else " — 해당 id 는 제외하고 검토하십시오."))

        anchor = date.fromisoformat(today)
        stale, mismatched = [], []
        for e in task.evidence:
            meta = feed_idx.get(e)
            if not meta:
                continue
            try:
                age = (anchor - date.fromisoformat(meta["published_on"])).days
                if age > EVIDENCE_MAX_AGE_DAYS:
                    stale.append(f"{e}({age}일)")
            except (ValueError, TypeError):
                pass
            if meta["affs"] and aff_code not in meta["affs"]:
                mismatched.append(e)

        if stale:
            add("STALE_EVIDENCE", "warn", "evidence",
                f"{EVIDENCE_MAX_AGE_DAYS}일이 지난 근거: {', '.join(stale)}")
        if mismatched:
            add("EVIDENCE_AFF_MISMATCH", "warn", "evidence",
                f"{aff_code} 태그가 없는 근거: {', '.join(mismatched)}")

    # 5. KPI — 측정 불가능한 과제는 성과 연결이 안 된다
    kpi_name = (task.kpi.name or "").strip()
    kpi_formula = (task.kpi.formula or "").strip()
    if kpi_name in ("", "-") or kpi_formula in ("", "-"):
        add("NO_KPI", "block", "kpi", "KPI 지표명 또는 산출식이 없어 성과 측정이 불가능합니다.")
    elif not _FORMULA_RE.search(kpi_formula):
        add("KPI_NOT_COMPUTABLE", "warn", "kpi",
            "산출식에 연산자·비율 표현이 없어 계산식으로 보기 어렵습니다.")

    # 6. 정량성
    effect = task.effect or ""
    if effect.strip() and not _QUANT_RE.search(effect):
        add("NO_QUANT_EFFECT", "warn", "effect", "기대효과에 수치·비율 표현이 없습니다.")

    # 7. 상투어
    blob = " ".join([task.background or "", task.plan or "", task.effect or ""])
    hits = [p for p in _VAGUE_PHRASES if p in blob]
    if hits:
        add("VAGUE_LANGUAGE", "warn", "plan", f"구체성이 낮은 표현: {', '.join(hits)}")

    # 8. 레버 분류
    cat = (task.category or "").strip()
    if cat and cat not in KNOWN_CATEGORIES:
        add("UNKNOWN_CATEGORY", "warn", "category",
            f"정의된 레버 분류가 아닙니다: {cat}")

    # 9. 중복
    for known in known_titles:
        ratio = _similar(title, known)
        if ratio >= DUP_THRESHOLD:
            add("DUPLICATE", "block", "title",
                f"기존 과제와 유사도 {ratio:.0%}: \"{known}\"")
            break

    blocked = any(i.severity == "block" for i in issues)
    verdict = "blocked" if blocked else ("review" if issues else "pass")
    return ValidationResult(ok=not blocked, verdict=verdict, issues=issues)


def validate_batch(
    tasks: Sequence[TaskDraft],
    aff_code: str,
    *,
    check_saved: bool = True,
    today: str = TODAY,
) -> List[ValidationResult]:
    """draft 목록을 한 번에 검사한다.

    배치 안에서의 상호 중복도 함께 잡는다 — 대량 생성 시 같은 과제가
    다른 문장으로 반복되는 것이 흔하기 때문.
    """
    all_ids = [e for t in tasks for e in t.evidence]
    feed_idx = _feed_index(all_ids)
    saved = _existing_titles(aff_code) if check_saved else []

    results: List[ValidationResult] = []
    accepted: List[str] = []   # 배치 내 이미 통과한 과제명
    for t in tasks:
        res = validate_task(
            t, aff_code,
            feed_idx=feed_idx,
            known_titles=list(saved) + accepted,
            today=today,
        )
        results.append(res)
        if res.ok:
            accepted.append(t.title)
    return results
