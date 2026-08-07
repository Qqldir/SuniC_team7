"""과제 평가 API — 선정 기준 조회 + 저장된 과제 재평가(비동기).

★ 저장하지 않는 채점 미리보기 라우트를 추가하지 마라. 결과를 다시 쓰는 곳이 없어
  같은 판정이 두 경로로 노출될 뿐이다. 채점 함수(evaluate_tasks · validate_batch)를
  쓰는 곳은 저장 경로인 pipeline/evaluation/runner.py 하나로 모아 둔다 —
  재생성 직후 자동 채점과 아래 /run 이 그것을 쓴다.
"""
from fastapi import APIRouter, Depends, HTTPException

from app import jobs
from app.api.deps import current_email
from app.models import EvaluationRunIn
from app.pipeline.evaluation import WEIGHTS, criteria_text

router = APIRouter(prefix="/api/evaluation", tags=["evaluation"])


@router.get("/criteria")
def criteria(_: str = Depends(current_email)):
    """선정 기준 + 축 가중치.

    화면은 이 값을 GET /api/bootstrap 의 evalCriteria(문장)로 받는다. 여기는 가중치
    원본까지 필요한 곳(봇·대시보드·운영자 확인)이 쓰는 경로라 남긴다.
    """
    return {"criteria": criteria_text(), "weights": WEIGHTS}


# ─────────── 저장된 과제 재평가 (비동기) ───────────
@router.post("/run")
def run(body: EvaluationRunIn, _: str = Depends(current_email)):
    """이미 저장된 proposal 을 다시 평가하고 결과를 DB 에 남긴다 — **비동기**.

    ★ 화면 진입점은 없지만 **남긴다.** 재생성·커스텀 생성 직후 자동으로 도는 것은
      규칙 채점뿐이고(store._auto_evaluate 가 use_llm=False 로 고정), 저장된 과제에
      LLM 채점을 다시 돌리는 수단은 이 라우트와 아래 CLI 둘뿐이다.
      CLI: python -m app.pipeline.evaluation.runner --all --llm   (--ids/--ver/--oc 도 가능)
      운영 중인 서버에 셸이 없을 때는 이 라우트가 유일한 수단이다.

    LLM 채점(useLlm=True)은 계열사당 배치 여러 번이라 전량이면 10분을 넘긴다.
    재생성과 같은 패턴으로 작업 id 를 즉시 돌려주고 호출자가 폴링한다.
    규칙 채점(기본)은 1초 미만이지만 호출 측 분기를 줄이려고 같은 흐름을 탄다.
    """
    from app.pipeline.evaluation.runner import evaluate_proposals

    ids = list(body.ids)
    return {
        "job": jobs.start(
            "evaluate",
            lambda: evaluate_proposals(
                ids=ids or None, ver=body.ver or None, oc=body.oc or None,
                use_llm=body.useLlm,
            ),
        ),
        "status": "running",
    }


@router.get("/run/{job_id}")
def run_status(job_id: str, _: str = Depends(current_email)):
    """평가 작업 상태. 완료면 counts·grades·batch 가 함께 실려 온다."""
    job = jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="작업을 찾을 수 없습니다.")
    return job
