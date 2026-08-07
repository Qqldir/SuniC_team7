"""과제 발굴 컨텍스트 조립 회귀 테스트 — LLM 을 호출하지 않는다.

`_build_messages` 는 RAG 컨텍스트 · 인스트럭션 · 현업 평가 이력을 조립하기만 하므로
LLM 없이 전 계열사에 대해 돌려볼 수 있다. 이 경로는 조용히 깨지기 쉽다:

- 별점 컬럼을 `score` → `star` 로 바꿨을 때 SQL 은 고쳤는데 dict 접근이 남아
  **별점이 있는 계열사(SKE·SKEO·SKGC)만** IndexError 로 죽었다. 별점이 없는 계열사는
  통과하므로 개발 중에는 드러나지 않고, 운영에서 그 계열사 발굴만 후보 풀로 폴백한다.
- `affiliate.kb_company` 가 NULL 인 계열사에서 retriever 를 부르면 FileNotFoundError 다.

그래서 "9개 계열사 전부가 예외 없이 프롬프트를 만든다"를 못박아 둔다.

    cd backend && .venv/bin/python -m pytest tests/ -q
"""
import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BACKEND))

from app.db.database import get_connection      # noqa: E402
from app.pipeline.discovery import agent        # noqa: E402
from app.pipeline.knowledge import prefetch     # noqa: E402
from app import store                           # noqa: E402


def _affiliates():
    conn = get_connection()
    try:
        return [r["code"] for r in conn.execute("SELECT code FROM affiliate ORDER BY sort_order")]
    finally:
        conn.close()


AFFS = _affiliates()


@pytest.mark.parametrize("aff", AFFS)
def test_피드백_신호가_전_계열사에서_조회된다(aff):
    """별점이 있는 계열사에서만 터지던 컬럼 별칭 버그를 막는다."""
    sig = store.feedback_signals(aff)
    assert isinstance(sig, dict)
    for group in ("low", "high"):
        for ex in sig.get(group, []):
            # 바깥으로 나가는 키는 score(= 사용자 별점). 컬럼명 star 와 다르다.
            assert "score" in ex, f"{aff} {group} 예시에 score 키가 없습니다: {ex}"
            assert ex["score"] is None or 0 <= ex["score"] <= 5


@pytest.mark.parametrize("aff", AFFS)
def test_RAG_컨텍스트가_전_계열사에서_만들어진다(aff):
    """지식 베이스가 없는 계열사도 degrade 만 하고 예외를 내면 안 된다."""
    text, meta = prefetch.build_context(aff, "")
    assert text.strip(), f"{aff} 컨텍스트가 비었습니다"
    assert meta["tokens"]["total"] > 0
    for key in ("kb_ids", "up_ids", "case_ids", "ev_ids"):
        assert isinstance(meta[key], list)
        # 화이트리스트 계약 — 프롬프트에 실제로 실린 것만 들어 있어야 한다
        tag = {"kb_ids": "kb", "up_ids": "up", "case_ids": "case", "ev_ids": "ev"}[key]
        for i in meta[key]:
            assert f"({tag}:{i})" in text, f"{aff} {key} 의 {i} 가 프롬프트에 없습니다"


@pytest.mark.parametrize("aff", AFFS)
def test_발굴_프롬프트가_전_계열사에서_조립된다(aff):
    """LLM 호출 없이 프롬프트 조립까지만 확인한다."""
    system, user, meta = agent._build_messages(aff, "")
    assert system.strip() and user.strip()
    # meta 는 prefetch 가 만든 근거 화이트리스트 — 인용 검증에 쓰인다
    assert isinstance(meta, dict)
    for key in ("kb_ids", "ev_ids"):
        assert key in meta, f"{aff} meta 에 {key} 가 없습니다"
    # 레버 목록이 프롬프트에 실려야 LLM 이 enum 을 지킬 수 있다
    assert "레버 체계" in user


def test_지식베이스가_있는_계열사는_내부_지식이_실린다():
    conn = get_connection()
    try:
        withkb = [r["code"] for r in conn.execute(
            "SELECT code FROM affiliate WHERE kb_company IS NOT NULL ORDER BY sort_order")]
    finally:
        conn.close()
    assert withkb, "kb_company 가 설정된 계열사가 없습니다"
    for aff in withkb:
        _, meta = prefetch.build_context(aff, "")
        assert meta["kb_ids"], f"{aff} 는 지식 베이스가 있는데 문서가 하나도 안 실렸습니다"


# ─────────────── AI Reporting 설정 ───────────────

def test_테스트발송이_기본_수신자를_지우지_않는다(tmp_path, monkeypatch):
    """'테스트 발송' 한 번에 수신자 칩이 사라지던 회귀를 막는다.

    _user_state 는 report_setting 행이 있으면 "저장된 설정이 있다" 로 보고 기본값
    폴백을 타지 않는다. mark_report_sent 가 그 행만 만들고 report_recipient 를
    비워 두면 화면 수신자가 조용히 0개가 된다.
    """
    import os
    import subprocess

    db = tmp_path / "rep.db"
    env = {**os.environ, "OI_DB_PATH": str(db), "PYTHONPATH": str(BACKEND)}
    subprocess.run([sys.executable, "-m", "app.db.seed"], cwd=BACKEND, env=env,
                   check=True, capture_output=True)

    code = (
        "import sys; sys.path.insert(0,'.')\n"
        "from app import store\n"
        "e='qa@sk.com'\n"
        "before = store.user_state(e)['recipients']\n"
        "store.mark_report_sent(e)\n"
        "after = store.user_state(e)['recipients']\n"
        "store.save_report(e, recipients=[])\n"
        "store.mark_report_sent(e)\n"
        "emptied = store.user_state(e)['recipients']\n"
        "print(repr((before, after, emptied)))\n"
    )
    out = subprocess.run([sys.executable, "-c", code], cwd=BACKEND, env=env,
                         check=True, capture_output=True, text=True).stdout
    before, after, emptied = eval(out.strip())
    assert before, "기본 수신자가 시드되어 있어야 합니다"
    assert after == before, f"테스트 발송이 수신자를 바꿨습니다: {before} → {after}"
    # 사용자가 의도적으로 비운 것은 되살리지 않는다
    assert emptied == [], f"비운 수신자가 되살아났습니다: {emptied}"
