"""과제 제안 API — 재생성 · 커스텀 생성 · 사용자 작업 상태 저장.

화면의 "과제 제안" 목록과 상세가 쓰는 엔드포인트입니다.
평가·기준값·산출식은 사람마다 다르므로 로그인 계정별로 저장됩니다.
"""
from fastapi import APIRouter, Depends, HTTPException

from app import jobs, store
from app.api.deps import current_email
from app.db.database import get_connection
from app.models import CustomProposalIn, FeedbackIn, FieldsIn, FormulaIn

router = APIRouter(prefix="/api/proposals", tags=["proposals"])


def _must_exist(pid: int):
    conn = get_connection()
    try:
        if not conn.execute("SELECT 1 FROM proposal WHERE id = ?", (pid,)).fetchone():
            raise HTTPException(status_code=404, detail="과제를 찾을 수 없습니다.")
    finally:
        conn.close()


# ★ 목록만 다시 받는 GET 라우트는 두지 않는다 — GET /api/bootstrap 이 같은
#   versions·tasks 를 내려주고, 재생성·커스텀 생성 응답에도 갱신된 목록이 함께 실려
#   온다(store.proposals_payload). ★ store.proposals_payload 는 지우지 마라.


@router.post("/regenerate")
def regenerate(_: str = Depends(current_email)):
    """새 생성 버전을 만든다 — **비동기**. 즉시 작업 id 를 돌려준다.

    LLM 발굴은 계열사 1곳당 1분 내외(codex medium 실측 58~62초, 기본 2곳)라 응답으로
    붙잡고 있을 수 없다(프록시 타임아웃 — 근거는 app/jobs.py 모듈 docstring).
    화면은 `GET /api/proposals/regenerate/{job}` 을 완료까지 폴링한다.

    LLM 을 끈 상태(OI_REGEN_LLM=0)에서는 후보 풀 경로라 1초도 안 걸리지만,
    호출 측 분기를 줄이려고 그 경우에도 같은 작업 흐름을 탄다.
    """
    return {"job": jobs.start("regenerate", store.regenerate), "status": "running"}


@router.get("/regenerate/{job_id}")
def regenerate_status(job_id: str, _: str = Depends(current_email)):
    """재생성 작업 상태. 완료면 versions·tasks 가 함께 실려 온다."""
    job = jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")
    return job


@router.post("/custom")
def create_custom(body: CustomProposalIn, _: str = Depends(current_email)):
    """커스텀 과제 1건을 만든다 — **비동기**. 즉시 작업 id 를 돌려준다.

    사람이 발굴 조건(OC 지정 + note 주입)을 직접 넣는 유일한 경로다.
    사용자가 고른 OC·근거·레버를 제약으로, 적용 방향을 note 로 넘겨 발굴 LLM 이
    배경·리스크·기대효과·KPI 까지 채운다(계열사당 60초 안팎 → 재생성과 같은 폴링).
    LLM 이 실패하면 예전 문자열 조립으로 폴백하므로 과제는 반드시 만들어진다.
    """
    if not body.oc or not body.lever:
        raise HTTPException(status_code=400, detail="대상 OC 와 레버는 필수입니다.")
    oc, lever, ev, plan = body.oc, body.lever, list(body.ev), body.plan
    name, summary = body.name, body.sum
    return {
        "job": jobs.start(
            "custom",
            lambda: store.create_custom_llm(oc, lever, ev, plan, name, summary),
        ),
        "status": "running",
    }


@router.get("/custom/{job_id}")
def create_custom_status(job_id: str, _: str = Depends(current_email)):
    """커스텀 생성 작업 상태. 완료면 id·ver·versions·tasks 가 함께 실려 온다.

    ★ 이 라우트는 아래 /{pid}/... 보다 **먼저** 선언돼야 한다. FastAPI 는 선언 순서로
      매칭하므로 뒤에 두면 'custom' 이 {pid}(int) 로 해석되려다 422 가 된다.
    """
    job = jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")
    return job


# ★ 과제 1건의 평가 조회 라우트는 두지 않는다 — 화면이 쓰는
#   verdict·grade·evalScore·scoredBy·flags 는 GET /api/bootstrap 의 tasks[] 가 이미 준다.
#   축별 점수·사유·재평가 이력은 화면에 표시되지 않지만 proposal_evaluation / _issue 에
#   그대로 쌓이므로, 붙일 때는 조회 함수만 만들면 된다(store.py 참조).


@router.put("/{pid}/feedback")
def put_feedback(pid: int, body: FeedbackIn, email: str = Depends(current_email)):
    _must_exist(pid)
    if body.score is not None and not 0 <= body.score <= 5:
        raise HTTPException(status_code=400, detail="점수는 0~5 사이여야 합니다.")
    store.save_feedback(email, pid, body.score, body.memo)
    return {"ok": True}


@router.put("/{pid}/fields")
def put_fields(pid: int, body: FieldsIn, email: str = Depends(current_email)):
    _must_exist(pid)
    store.save_fields(email, pid, body.fields)
    return {"ok": True}


@router.put("/{pid}/formula")
def put_formula(pid: int, body: FormulaIn, email: str = Depends(current_email)):
    """sysOff=True 면 사용자 수식 사용, False 면 시스템 제안 산출식으로 복귀."""
    _must_exist(pid)
    at = store.save_formula(email, pid, body.sysOff, body.text)
    return {"ok": True, "at": at}
