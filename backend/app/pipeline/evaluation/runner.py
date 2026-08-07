"""저장된 과제(proposal)를 평가하고 결과를 DB 에 남기는 실행기.

app/pipeline/evaluation 의 validator·scorer·priority 는 **저장 전 draft** 를 다룬다.
이 모듈은 그 사이를 잇는다 — proposal 행을 TaskDraft 로 바꿔 평가하고,
결과를 proposal_evaluation / proposal_evaluation_issue 에 이력으로 쌓는다.

경계 규칙 세 가지.

1) **영문 → 한국어 매핑은 여기서만 한다.**
   평가 파이프라인 내부는 pass/review/blocked · block/warn ·
   supported/weak/unsupported/unknown · llm/heuristic/none 을 그대로 쓰고,
   DB 와 화면은 한국어만 본다. 양쪽 어휘가 섞이면 화면 조건문이 조용히 깨진다.

2) **저장은 반드시 BEGIN IMMEDIATE 안에서 `UPDATE is_latest=0` → `INSERT` 순서.**
   idx_pev_latest 가 `proposal_id WHERE is_latest = 1` 부분 유니크 인덱스라
   순서를 뒤집으면 두 번째 평가가 UNIQUE 위반으로 죽는다.

3) **LLM 호출은 트랜잭션 밖에서 끝낸다.** 채점이 수십 초 걸리는데 쓰기 잠금을
   잡고 있으면 그동안 재생성·피드백 저장이 전부 막힌다.

사용:
    from app.pipeline.evaluation.runner import evaluate_proposals
    evaluate_proposals(use_llm=False)                  # 전량 규칙 채점 (LLM 0회)
    evaluate_proposals(ids=[1301, 1302], use_llm=False)  # 재생성 훅이 쓰는 경로
    evaluate_proposals(oc="SKEO", use_llm=True)        # 계열사 1곳 LLM 채점

CLI (전량 LLM 재채점은 계열사 9곳 × 배치라 10~15분이다. HTTP 로 돌리지 마라):
    python -m app.pipeline.evaluation.runner --all --llm
"""
import json
import logging
import secrets
import time
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Sequence

from app.db.database import get_connection
from app.models import EvaluatedTask, Kpi, TaskDraft
from app.pipeline.evaluation import WEIGHTS, criteria_text, evaluate_tasks

log = logging.getLogger(__name__)

# ─────────── 영문 리터럴 → 한국어 (저장 경계) ───────────
VERDICT_KO = {"pass": "통과", "review": "검토필요", "blocked": "차단"}
SEVERITY_KO = {"block": "차단", "warn": "경고"}
GROUNDING_KO = {
    "supported": "뒷받침", "weak": "느슨함",
    "unsupported": "무관", "unknown": "미확인",
}
SCORED_BY_KO = {"llm": "LLM", "heuristic": "규칙", "none": "미채점"}

_SELECT = """
    SELECT p.id, p.aff_code, p.ver_id, p.name, p.lever, p.summary, p.plan,
           p.background, p.risk, p.effect, p.kpi_name, p.kpi_formula,
           l.metric  AS lever_metric,
           l.formula AS lever_formula,
           GROUP_CONCAT(pe.feed_id) AS ev
    FROM proposal p
    LEFT JOIN proposal_evidence pe ON pe.proposal_id = p.id
    LEFT JOIN lever l ON l.name = p.lever
"""


def _to_draft(row) -> TaskDraft:
    """proposal 행(+ lever 조인) → 평가용 TaskDraft.

    ★ kpi 폴백을 빼면 안 된다. validator 의 NO_KPI 는 block 이라 kpi_name/formula 가
      NULL 인 기존 과제가 전부 차단된다. 화면이 이미 lever.metric/formula 로 폴백해
      보여 주고 있으므로, 평가도 같은 값을 봐야 판정이 화면과 어긋나지 않는다.
    ★ category 와 lever 에 같은 값을 넣는다 — validator/scorer 는 category 를,
      저장 경로(persist)는 lever 를 본다(설계 conflicts 4번).
    """
    lever = row["lever"] or ""
    return TaskDraft(
        title=row["name"] or "",
        category=lever,
        lever=lever,
        summary=row["summary"] or "",
        background=row["background"] or row["summary"] or "",
        plan=row["plan"] or "",
        risk=row["risk"] or "",
        effect=row["effect"] or "",
        kpi=Kpi(
            name=row["kpi_name"] or row["lever_metric"] or "",
            formula=row["kpi_formula"] or row["lever_formula"] or "",
        ),
        evidence=[x for x in (row["ev"] or "").split(",") if x],
    )


def _fetch(conn, ids=None, ver=None, oc=None) -> List[Any]:
    where, args = [], []
    if ids:
        ids = [int(i) for i in ids]
        where.append(f"p.id IN ({','.join('?' * len(ids))})")
        args += ids
    if ver:
        where.append("p.ver_id = ?")
        args.append(ver)
    if oc:
        where.append("p.aff_code = ?")
        args.append(oc)
    sql = _SELECT
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " GROUP BY p.id ORDER BY p.aff_code, p.id"
    return conn.execute(sql, args).fetchall()


def _aff_names(conn) -> Dict[str, str]:
    return {r["code"]: r["name"] for r in conn.execute("SELECT code, name FROM affiliate")}


def _pid_of(results: Sequence[EvaluatedTask], drafts: Sequence[TaskDraft],
            pids: Sequence[int]) -> List[Optional[int]]:
    """평가 결과(정렬된 순서) 각각에 원래 proposal.id 를 되붙인다.

    evaluate_tasks 는 우선순위 내림차순으로 **정렬해서** 돌려주므로 입력 순서로
    zip 하면 점수가 엉뚱한 과제에 붙는다. 객체 동일성(id())으로 짝짓고,
    혹시 모델 재검증으로 사본이 만들어졌으면 과제명으로 폴백한다.
    """
    by_obj = {id(d): pid for d, pid in zip(drafts, pids)}
    by_title: Dict[str, List[int]] = {}
    for d, pid in zip(drafts, pids):
        by_title.setdefault(d.title, []).append(pid)

    out: List[Optional[int]] = []
    for r in results:
        pid = by_obj.pop(id(r.task), None)
        if pid is None:                      # 폴백 — 같은 이름이 여럿이면 앞에서부터
            bucket = by_title.get(r.task.title) or []
            pid = bucket.pop(0) if bucket else None
        out.append(pid)
    return out


def _save(rows: Sequence[dict], batch_id: str) -> int:
    """평가 결과를 한 트랜잭션으로 저장한다. 저장된 행 수를 돌려준다.

    ★ 순서 고정: BEGIN IMMEDIATE → UPDATE is_latest=0 → INSERT.
      부분 유니크 인덱스(idx_pev_latest) 때문에 INSERT 를 먼저 하면 즉사한다.
    """
    if not rows:
        return 0
    now = datetime.now().isoformat(timespec="seconds")
    weights = json.dumps(WEIGHTS, ensure_ascii=False)
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        for r in rows:
            conn.execute(
                "UPDATE proposal_evaluation SET is_latest = 0 "
                "WHERE proposal_id = ? AND is_latest = 1",
                (r["proposal_id"],),
            )
            cur = conn.execute(
                """INSERT INTO proposal_evaluation(
                       proposal_id, evaluated_at, verdict, priority, grade, rank_in_aff,
                       impact_score, impact_reason, feas_score, feas_reason,
                       roi_score, roi_reason, grounding, grounding_reason,
                       scored_by, weights, batch_id, is_latest)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,1)""",
                (r["proposal_id"], now, r["verdict"], r["priority"], r["grade"],
                 r["rank"], r["impact"], r["impact_reason"], r["feas"], r["feas_reason"],
                 r["roi"], r["roi_reason"], r["grounding"], r["grounding_reason"],
                 r["scored_by"], weights, batch_id),
            )
            eval_id = cur.lastrowid
            for seq, issue in enumerate(r["issues"]):
                conn.execute(
                    "INSERT INTO proposal_evaluation_issue"
                    "(eval_id, seq, code, severity, field, message) VALUES (?,?,?,?,?,?)",
                    (eval_id, seq, issue["code"], issue["severity"],
                     issue["field"], issue["message"]),
                )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return len(rows)


def evaluate_proposals(
    ids: Optional[Iterable[int]] = None,
    ver: Optional[str] = None,
    oc: Optional[str] = None,
    *,
    use_llm: bool = False,
) -> Dict[str, Any]:
    """저장된 과제를 평가하고 proposal_evaluation 에 남긴다.

    범위: ids / ver / oc 를 모두 생략하면 전량. 여러 개를 주면 AND 로 좁힌다.
    use_llm=False 면 LLM 을 한 번도 부르지 않는다(재생성 훅이 쓰는 경로, 1초 미만).

    계열사(aff_code)별로 나눠 평가한다 — validator 의 중복 검사와 scorer 의
    프롬프트가 모두 '같은 계열사 안에서' 를 전제로 하기 때문이다.
    예외는 밖으로 올리지 않는다. 한 계열사가 실패해도 나머지는 저장한다.
    """
    t0 = time.monotonic()
    batch_id = f"ev{datetime.now().strftime('%Y%m%d%H%M%S')}-{secrets.token_hex(2)}"

    conn = get_connection()
    try:
        rows = _fetch(conn, ids, ver, oc)
        names = _aff_names(conn)
    finally:
        conn.close()

    groups: Dict[str, List[Any]] = {}
    for r in rows:
        groups.setdefault(r["aff_code"], []).append(r)

    to_save: List[dict] = []
    counts = {"통과": 0, "검토필요": 0, "차단": 0}
    grades = {"A": 0, "B": 0, "C": 0}
    scored = {"LLM": 0, "규칙": 0, "미채점": 0}
    failed: List[str] = []

    for aff, group in groups.items():
        drafts = [_to_draft(r) for r in group]
        pids = [r["id"] for r in group]
        try:
            # self_ids 는 **필수**다. 안 넘기면 저장된 과제가 자기 자신과 유사도
            # 100% 로 비교돼 전량 중복 경고를 받는다(실측: 65/65).
            results = evaluate_tasks(
                drafts, aff,
                use_llm=use_llm, check_saved=True,
                aff_name=names.get(aff, ""), self_ids=pids,
            )
        except Exception as e:                 # noqa: BLE001 — 한 계열사 실패로 전체를 버리지 않는다
            log.warning("과제 평가 실패 (%s): %s: %s", aff, type(e).__name__, e)
            failed.append(aff)
            continue

        for pid, r in zip(_pid_of(results, drafts, pids), results):
            if pid is None:
                continue
            ev = r.evaluation
            verdict = VERDICT_KO.get(ev.verdict, "검토필요")
            scored_by = SCORED_BY_KO.get(ev.scoredBy, "규칙")
            counts[verdict] = counts.get(verdict, 0) + 1
            grades[ev.grade] = grades.get(ev.grade, 0) + 1
            scored[scored_by] = scored.get(scored_by, 0) + 1
            to_save.append({
                "proposal_id": pid,
                "verdict": verdict,
                "priority": ev.priority,
                "grade": ev.grade,
                "rank": ev.rank,
                "impact": ev.impact.score,
                "impact_reason": ev.impact.reason,
                "feas": ev.feasibility.score,
                "feas_reason": ev.feasibility.reason,
                "roi": ev.roi.score,
                "roi_reason": ev.roi.reason,
                "grounding": GROUNDING_KO.get(ev.grounding, "미확인"),
                "grounding_reason": ev.groundingReason,
                "scored_by": scored_by,
                "issues": [
                    {
                        "code": i.code,
                        "severity": SEVERITY_KO.get(i.severity, "경고"),
                        "field": i.field or "",
                        "message": i.message,
                    }
                    for i in ev.validation.issues
                ],
            })

    saved = _save(to_save, batch_id)
    return {
        "batch": batch_id,
        "n": saved,
        "counts": counts,
        "grades": grades,
        "scoredBy": scored,
        "failed": failed,
        "seconds": round(time.monotonic() - t0, 2),
        "criteria": criteria_text(),
    }


def evaluate_after_write(ids: Sequence[int]) -> None:
    """저장 직후 훅 — 규칙 채점만 돌리고 **절대 예외를 올리지 않는다**.

    재생성·커스텀 생성의 응답 경로에 걸리므로, 평가가 실패해도 과제 생성 자체는
    성공으로 끝나야 한다(평가는 나중에 다시 돌릴 수 있다).
    """
    ids = [i for i in ids if i]
    if not ids:
        return
    try:
        evaluate_proposals(ids=ids, use_llm=False)
    except Exception as e:                     # noqa: BLE001
        log.warning("저장 직후 자동 평가 실패: %s: %s", type(e).__name__, e)


# ─────────── CLI ───────────
def _main() -> None:
    import argparse

    ap = argparse.ArgumentParser(description="저장된 과제를 평가해 DB 에 기록한다.")
    ap.add_argument("--all", action="store_true", help="전량 평가 (범위 옵션 없이)")
    ap.add_argument("--ids", default="", help="proposal.id 콤마 결합")
    ap.add_argument("--ver", default="", help="생성 버전 id (예: n62)")
    ap.add_argument("--oc", default="", help="계열사 코드 (예: SKEO)")
    ap.add_argument("--llm", action="store_true", help="LLM 채점 사용 (기본은 규칙)")
    a = ap.parse_args()

    ids = [int(x) for x in a.ids.split(",") if x.strip()]
    if not (a.all or ids or a.ver or a.oc):
        ap.error("--all 또는 --ids/--ver/--oc 중 하나가 필요합니다.")

    out = evaluate_proposals(ids=ids or None, ver=a.ver or None, oc=a.oc or None,
                             use_llm=a.llm)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    _main()
