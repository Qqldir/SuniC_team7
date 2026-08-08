"""과제 검증 — 결정적(deterministic) 게이트.

발굴 agent 가 만든 draft 가 '사용자에게 보여줄 만한가'를 LLM 없이 판정합니다.
LLM 출력의 형식·근거 오류는 LLM 에게 다시 묻지 않고 규칙으로 잡습니다.
(빠르고, 재현 가능하고, API 키 없이도 동작)

severity:
    block — 검증 미통과. 채점을 건너뛴다.
    warn  — 플래그를 달아 검토를 유도한다.

★ 확정된 운영 규칙: block 과제도 **화면 목록에서 빼지 않는다.** 플래그만 단다.
  숨기면 생성 버전 대부분이 0건이 되어 일별 생성 건수 차트와 캘린더가 통째로 빈다.
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
# 과제명 유사도(중복 판정) — 실측 분포의 '빈 구간' 한가운데로 잡았다.
#
#   저장된 80건에 대해 '같은 계열사의 나보다 먼저 등록된 과제' 중 최고 유사도를 재면
#   분포가 두 덩어리로 확실히 갈린다:
#       진짜 중복 : 1.000 × 15건(과제명 완전 동일) · 0.889 · 0.850
#                   (0.850 = "머신비전 기반 전수검사 전환으로 셀 수율 개선 적용 검토"
#                    vs "머신비전 전수검사 전환으로 셀 수율 개선" — 같은 과제의 변형)
#       ── 0.645 ~ 0.850 구간은 완전히 비어 있다 ──
#       서로 다른 과제 : 0.645("해상운송 계약조건 재협상" vs "육상운송 단가 재협상"
#                       — 해상/육상이라 다른 과제다) 이하 63건
#
#   그 빈 구간의 중점이 (0.645+0.850)/2 ≈ 0.75 다. 여기 두면 양쪽 여유가 거의 같다
#   (진짜 중복까지 0.10 · 서로 다른 과제까지 0.105). 종전 0.82 는 검출 건수는 같지만
#   (0.70~0.85 어디에 두든 17건으로 동일) 진짜 중복 쪽 여유가 0.03 밖에 없어,
#   과제명이 조금만 더 길어진 변형이 그대로 새 과제로 새어 나간다.
DUP_THRESHOLD = 0.75

PLACEHOLDER_TITLES = {"무제 과제", "제목 없음", "untitled", "-", "n/a"}

# 필수 필드 중 **비면 차단**하는 것은 title / plan 두 개뿐이다.
# background · effect 는 warn 으로 낮춘다 — 본문 필드가 생기기 전에 저장된 proposal
# 행은 배경·기대효과가 NULL 인데, 이를 block 으로 두면 화면 목록의 거의 전부가
# '차단' 으로 물든다.
_REQUIRED_BLOCK = (("title", "과제명"), ("plan", "실행방안"))
_REQUIRED_WARN = (("background", "배경"), ("effect", "기대효과"))

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


def known_levers() -> set:
    """레버 마스터 + 표기 변형(alias) 전량.

    ★ 레버 목록을 코드 상수로 두지 마라 — 관리자가 DB 에서 추가·개명할 수 있어
      상수로 두면 정상 레버가 UNKNOWN_CATEGORY 경고를 받는다.
    조회 실패(테이블 없음 등)면 빈 집합을 돌려 이 검사를 통째로 건너뛴다 —
    LLM 없이도 예외 없이 완주해야 하기 때문이다.
    """
    try:
        conn = get_connection()
    except Exception:
        return set()
    try:
        out = {r["name"] for r in conn.execute("SELECT name FROM lever")}
        out |= {r["alias"] for r in conn.execute("SELECT alias FROM lever_alias")}
        return {x for x in out if x}
    except Exception:
        return set()
    finally:
        conn.close()


def _existing_names(aff_code: str) -> List[tuple]:
    """같은 계열사에 이미 저장된 과제 (id, name) 목록 — 중복 발굴 방지.

    ★ 과제 실체는 `proposal` 이다. 다른 테이블(예: 옛 task)에서 읽으면 0행이 나와
      중복 게이트가 절대 발동하지 않는다.
    ★ id 를 함께 돌려주는 이유: 이미 저장된 proposal 을 재평가할 때 자기 자신과
      비교하면 유사도 100% 로 전 과제가 DUPLICATE 차단된다. 호출부가 `id < 자기id`
      로 걸러 '나보다 먼저 등록된 과제' 하고만 비교하게 한다.
    """
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, name FROM proposal WHERE aff_code = ? ORDER BY id", (aff_code,)
        ).fetchall()
        return [(r["id"], r["name"]) for r in rows]
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
    known_lever_names: Optional[set] = None,
    today: str = TODAY,
) -> ValidationResult:
    """draft 1건을 검사한다.

    feed_idx / known_titles / known_lever_names 를 주입하면 배치 처리 시
    DB 재조회를 피할 수 있다.
    """
    issues: List[ValidationIssue] = []

    def add(code, severity, field, message):
        issues.append(
            ValidationIssue(code=code, severity=severity, field=field, message=message)
        )

    if feed_idx is None:
        feed_idx = _feed_index(task.evidence)

    # 1. 필수 필드 — title/plan 만 차단, background/effect 는 경고
    for field, label in _REQUIRED_BLOCK:
        if not (getattr(task, field) or "").strip():
            add("MISSING_FIELD", "block", field, f"{label}{_ga(label)} 비어 있습니다.")
    for field, label in _REQUIRED_WARN:
        if not (getattr(task, field) or "").strip():
            add("MISSING_FIELD", "warn", field, f"{label}{_ga(label)} 비어 있습니다.")

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

    # 8. 레버 분류 — 하드코딩 상수가 아니라 lever + lever_alias 마스터와 대조한다
    if known_lever_names is None:
        known_lever_names = known_levers()
    cat = (task.category or "").strip()
    if cat and known_lever_names and cat not in known_lever_names:
        add("UNKNOWN_CATEGORY", "warn", "category",
            f"정의된 레버 분류가 아닙니다: {cat}")

    # 9. 중복 — **경고이지 차단이 아니다.**
    #    "이건 이미 있는 과제다" 를 사람이 볼 수 있게만 하고, 화면 목록에서 빼거나
    #    채점을 건너뛰지 않는다. 차단으로 두면 priority 가 0 이 되고 등급이 C 로 떨어져,
    #    중복이 아니라 '나쁜 과제' 처럼 보인다. 판단은 사람이 한다.
    for known in known_titles:
        ratio = _similar(title, known)
        if ratio >= DUP_THRESHOLD:
            add("DUPLICATE", "warn", "title",
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
    self_ids: Sequence[Optional[int]] = (),
    today: str = TODAY,
) -> List[ValidationResult]:
    """draft 목록을 한 번에 검사한다.

    배치 안에서의 상호 중복도 함께 잡는다 — 대량 생성 시 같은 과제가
    다른 문장으로 반복되는 것이 흔하기 때문.

    self_ids: tasks 와 같은 길이의 proposal.id 목록(없으면 None).
        ★ 이미 저장된 proposal 을 재평가할 때 반드시 넘겨라. 안 넘기면
          자기 자신이 중복 후보에 들어가 유사도 100% 로 전 과제가 차단된다.
          i 번째 과제는 `id < self_ids[i]` 인 과제하고만 비교한다.
    """
    all_ids = [e for t in tasks for e in t.evidence]
    feed_idx = _feed_index(all_ids)
    saved = _existing_names(aff_code) if check_saved else []
    levers = known_levers()          # 배치당 1회만 조회

    ids = list(self_ids) + [None] * max(0, len(tasks) - len(self_ids))

    results: List[ValidationResult] = []
    accepted: List[str] = []   # 배치 내 이미 통과한 '신규' 과제명
    for i, t in enumerate(tasks):
        me = ids[i]
        if me is None:
            prior = [n for _pid, n in saved]
        else:
            prior = [n for pid, n in saved if pid < me]
        res = validate_task(
            t, aff_code,
            feed_idx=feed_idx,
            known_titles=prior + accepted,
            known_lever_names=levers,
            today=today,
        )
        results.append(res)
        # 저장 전 draft 끼리의 상호 중복만 누적한다. 이미 저장된 과제는
        # saved 에 들어 있으므로 여기서 또 쌓으면 이중 계산이 된다.
        if res.ok and me is None:
            accepted.append(t.title)
    return results
