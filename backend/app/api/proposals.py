"""과제 제안 API — 재생성 · 커스텀 생성 · 사용자 작업 상태 저장.

화면의 "과제 제안" 목록과 상세가 쓰는 엔드포인트입니다.
평가·기준값·산출식은 사람마다 다르므로 로그인 계정별로 저장됩니다.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

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
    LLM 이 실패하면 예전 문자열 조립으로 폴백한다 — 즉 과제가 만들어지지 않는 유일한
    사유는 **중복**이다.

    중복 차단 3층 (사용자 요구: "물리적으로 막아야 한다")
      L1  (aff_code, name_key) 완전일치 → 409 duplicate_exact. force 로도 못 뚫는다.
      L1' persist.find_duplicate 퍼지  → 409 duplicate_similar. 화면 확인 후
                                          force:true 재요청으로 통과한다(오탐이 실재한다 —
                                          '육상운송'↔'해상운송' 재협상 0.645).
      L2  store.create_custom 저장 직전 재확인 → {"id": null, "reason": …}
      L3  DB UNIQUE INDEX (aff_code, name_key)
    ★ L1/L1' 은 jobs.start **앞**에 있다. 커스텀 발굴은 계열사당 60초라, 중복인 게
      확정인 요청에 1분을 태우고 나서 거부하면 안 된다.
    ★ detail 은 반드시 **문자열**이다 — 화면 api() 가 그대로 표시하므로 dict 를 실으면
      '[object Object]' 가 뜬다. 부가 정보는 별도 키로 싣는다.
    """
    if not body.oc or not body.lever:
        raise HTTPException(status_code=400, detail="대상 OC 와 레버는 필수입니다.")
    oc, lever, ev, plan = body.oc, body.lever, list(body.ev), body.plan
    name, summary = body.name, body.sum

    from app.pipeline.discovery import persist
    from app.pipeline.discovery.lever_map import normalize_lever

    conn = get_connection()
    try:
        canon = normalize_lever(lever, conn)
        if not canon:
            raise HTTPException(status_code=400, detail=f"알 수 없는 레버입니다: {lever}")

        key = store.name_key(name) if name else ""
        if key:
            row = store.find_by_name_key(conn, oc, key)
            if row is not None:
                return JSONResponse(status_code=409, content={
                    "detail": f"같은 이름의 과제가 이미 있습니다 — #{row['id']} "
                              f"({(row['created_at'] or '')[:10]} 생성). "
                              f"과제명을 바꾸거나 기존 과제를 여세요.",
                    "code": "duplicate_exact",
                    "id": row["id"], "name": row["name"],
                })

        if not body.force:
            dup = persist.find_duplicate(conn, oc, canon, key, ev)
            if dup is not None:
                return JSONResponse(status_code=409, content={
                    "detail": f"비슷한 과제가 이미 있습니다 — #{dup['id']} {dup['name']} "
                              f"({dup['why']}).",
                    "code": "duplicate_similar",
                    "id": dup["id"], "name": dup["name"],
                })
    finally:
        conn.close()

    return {
        "job": jobs.start(
            "custom",
            lambda: store.create_custom_llm(oc, canon, ev, plan, name, summary),
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
