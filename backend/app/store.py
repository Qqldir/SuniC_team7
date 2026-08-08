"""화면(O/I Spark) 데이터 저장소.

프론트(frontend/public/trendroom.html)가 쓰던 상수들을 그대로 대체하는 계층입니다.
반환 형태는 화면 코드가 기대하는 키(`ev`, `sum`, `oc`, `st` ...)에 맞춰 두었습니다.
파이프라인(app/pipeline/*)이 채우는 feed_item 을 그대로 근거 자료로 씁니다.
"""
import json
import logging
import re
import unicodedata
from datetime import date, datetime
from typing import Any, Dict, List, Optional

from app import llm_client
from app.config import (
    LOCAL_TZ_SQL, OI_CODEX_MODEL, OI_MODEL, OI_REGEN_LLM, OI_REGEN_OCS,
    OI_REGEN_TASKS, OI_REGEN_TIMEOUT, OI_TASK_PROVIDER, today_local,
)
from app.db.database import get_connection

log = logging.getLogger(__name__)

# ─────────────── 공통 ───────────────

DEFAULT_CHANNELS = {"outlook": True, "teams": True}
DEFAULT_REPORT = {"freq": "매일", "time": "08:00", "lastAt": ""}


def dot(iso: Optional[str]) -> str:
    """2026-07-17 → 2026.07.17 (화면 표기)."""
    return (iso or "").replace("-", ".")


def _loads(raw: Optional[str], fallback):
    try:
        return json.loads(raw) if raw else fallback
    except (ValueError, TypeError):
        return fallback


def get_setting(conn, key: str, default: str = "") -> str:
    row = conn.execute("SELECT value FROM app_setting WHERE key = ?", (key,)).fetchone()
    return row["value"] if row else default


def set_setting(key: str, value: str) -> None:
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO app_setting(key, value) VALUES (?,?) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
            (key, value),
        )
        conn.commit()
    finally:
        conn.close()


# ─────────────── 마스터 조회 ───────────────

def _ocs(conn):
    rows = conn.execute(
        "SELECT a.code, a.name, a.color, b.label AS biz FROM affiliate a "
        "JOIN biz_segment b ON b.key = a.biz ORDER BY a.sort_order, a.code"
    ).fetchall()
    ocs = [{"code": r["code"], "name": r["name"], "biz": r["biz"]} for r in rows]
    colors = {r["code"]: r["color"] for r in rows if r["color"]}
    return ocs, colors


def _biz_colors(conn):
    rows = conn.execute("SELECT label, color FROM biz_segment ORDER BY rowid").fetchall()
    return {r["label"]: r["color"] for r in rows}


def _kind_labels(conn) -> List[str]:
    """트렌드룸 '종류' 필터 항목 — 실제로 자료가 붙어 있는 종류만."""
    # source_kind 의 rowid 는 레거시 4종(adhoc/periodic/sec/news)이 먼저 시드되어 있어
    # 뉴스가 쌓이는 순간 '뉴스' 칩이 '공시' 앞에 온다. 화면 축 순서를 명시적으로 고정한다.
    rows = conn.execute(
        "SELECT k.label FROM source_kind k "
        "WHERE EXISTS (SELECT 1 FROM feed_item f WHERE f.kind = k.key) "
        "ORDER BY CASE k.key WHEN 'disclosure' THEN 1 WHEN 'earnings' THEN 2 "
        "WHEN 'ir' THEN 3 WHEN 'market' THEN 4 WHEN 'assoc' THEN 5 "
        "WHEN 'news' THEN 6 ELSE 9 END, k.rowid"
    ).fetchall()
    return [r["label"] for r in rows]


def _levers(conn):
    rows = conn.execute(
        "SELECT name, metric, formula, fields FROM lever ORDER BY sort_order, name"
    ).fetchall()
    return {
        r["name"]: {"metric": r["metric"], "text": r["formula"], "fields": _loads(r["fields"], [])}
        for r in rows
    }


# ─────────────── 근거 자료 (feed_item) ───────────────

# ★ theme 은 여기서 **읽지 않는다.** 화면이 테마 축을 쓰지 않게 되어 bootstrap 에서
#   themes/evTheme 두 키를 뺐다(프론트 TH2·EV_TH·S.trTheme 은 정의만 있고 참조 0건).
#   theme **테이블과 feed_item.theme 컬럼은 그대로 둔다** — FK 이고 파밍이 90/90 채우며
#   LLM 분류·평가가 쓴다. 없앤 것은 페이로드 2키뿐이다.
_EV_SELECT = """
    SELECT f.id, f.published_on, f.url,
           f.biz_hint,
           -- NEW 배지 = '오늘(KST) 크롤분'. 저장 플래그가 아니라 읽는 시점 판정이다.
           -- ★ substr(farmed_at,1,10) 로 비교하면 안 된다 — 그건 UTC 날짜라
           --   KST 새벽 크롤분이 통째로 '어제' 가 된다(실측 76건 → 0건).
           CASE WHEN f.farmed_at IS NOT NULL
                 AND date(f.farmed_at, :tz) = :today
                THEN 1 ELSE 0 END AS is_new,
           -- 표시용 라벨이 있으면 그것을, 없으면 크롤러 원문 값을 쓴다.
           COALESCE(NULLIF(f.source_label, ''), f.source) AS src,
           COALESCE(NULLIF(f.title_label, ''), f.title)   AS title,
           f.summary, f.metrics,
           COALESCE(NULLIF(f.kind_label, ''), k.label) AS kind_label,
           k.label AS kind_cat
    FROM feed_item f
    LEFT JOIN source_kind k ON k.key = f.kind
"""


def _evidence(conn):
    """화면의 EV / EV_BIZ_FB / EV_NEW / KIND_MAP 을 한 번에 만든다.

    ★ EV 원소의 키(src/kind/date/url/title/sum/metrics)는 이름·의미가 불변이다.
      화면 벤치마크 카드와 검색 haystack 이 EV[id] 를 직접 읽는다.
    """
    # ★ _EV_SELECT 는 문자열 결합으로 쓰이므로 반드시 named placeholder 다.
    rows = conn.execute(
        _EV_SELECT + " ORDER BY f.published_on DESC, f.id",
        {"tz": LOCAL_TZ_SQL, "today": today_local()},
    ).fetchall()
    ev, biz_fb, is_new, kind_map = {}, {}, {}, {}
    for r in rows:
        ev[r["id"]] = {
            "src": r["src"],
            "kind": r["kind_label"] or "",
            "date": dot(r["published_on"]),
            "url": r["url"] or "",
            "title": r["title"],
            "sum": r["summary"] or "",
            # 핵심 지표 [{label,value,period}]. 화면 벤치마크 카드가 그대로 렌더링한다.
            "metrics": _loads(r["metrics"], []),
        }
        if r["biz_hint"]:
            biz_fb[r["id"]] = r["biz_hint"]
        if r["is_new"]:
            is_new[r["id"]] = 1
        # 자료명(Earnings call) → 종류 필터 카테고리(실적발표) 매핑
        if r["kind_label"] and r["kind_cat"]:
            kind_map[r["kind_label"]] = r["kind_cat"]
    return ev, biz_fb, is_new, kind_map


def _ev_oc(conn) -> Dict[str, List[str]]:
    """자료 → 관련 계열사 코드 배열 (화면 EV_OC).

    원천은 feed_item_tag — 파밍의 entity.tag_affiliates 가 채우고, 시드 자료는
    seed_trendroom.seed_feed_tags 가 과제 인용 관계에서 역산한다(실측 90/90 태그 보유).
    ★ 정렬은 affiliate.sort_order 다. 화면 OC 칩 순서가 계열사 마스터 순서와 같아야
      트리맵·필터와 나란히 읽힌다(코드 알파벳 순이면 SKE 가 SKGC 뒤로 간다).
    """
    rows = conn.execute(
        "SELECT t.feed_id, t.aff_code FROM feed_item_tag t "
        "JOIN affiliate a ON a.code = t.aff_code "
        "ORDER BY t.feed_id, a.sort_order, t.aff_code"
    ).fetchall()
    out: Dict[str, List[str]] = {}
    for r in rows:
        out.setdefault(r["feed_id"], []).append(r["aff_code"])
    return out


def _ev_kw(conn) -> Dict[str, List[str]]:
    """자료 → 동향 키워드 배열 (화면 EV_KW). seq 가 곧 화면 칩 순서다."""
    rows = conn.execute(
        "SELECT feed_id, keyword FROM feed_item_keyword ORDER BY feed_id, seq, keyword"
    ).fetchall()
    out: Dict[str, List[str]] = {}
    for r in rows:
        out.setdefault(r["feed_id"], []).append(r["keyword"])
    return out


def _ev_brief(conn) -> Dict[str, str]:
    """자료 → 데일리 브리핑 문장 (화면 EV_BRIEF).

    ★ 비면 **키 자체를 내리지 않는다.** 화면이 `EV_BRIEF[k] || e.sum` 으로 요약에
      폴백하므로, 빈 문자열을 내리면 브리핑 카드가 빈 줄로 뜬다.
    """
    rows = conn.execute(
        "SELECT id, brief FROM feed_item WHERE brief IS NOT NULL AND brief <> ''"
    ).fetchall()
    return {r["id"]: r["brief"] for r in rows}


def _kw_trend(conn) -> Dict[str, int]:
    """키워드 → 직전 스냅샷 대비 증감 (화면 KW_TREND).

    ★ distinct day 가 2개 미만이면 **{} 를 내린다.** 화면은 `KW_TREND[w] || 0` 을
      '–' 로 그리므로 "비교 기준이 아직 없다"는 정직한 표시가 된다.
      첫 스냅샷만 있는 상태에서 n-0=+n 을 내려 전 키워드에 ▲ 를 붙이는 편이 훨씬 나쁘다.
    ★ 증감이 0 인 키워드는 뺀다 — 화면 렌더 결과가 같고 페이로드만 커진다.
    """
    days = [r["day"] for r in conn.execute(
        "SELECT DISTINCT day FROM keyword_daily ORDER BY day DESC LIMIT 2"
    ).fetchall()]
    if len(days) < 2:
        return {}

    def counts(day: str) -> Dict[str, int]:
        return {
            r["keyword"]: r["n"] for r in
            conn.execute("SELECT keyword, n FROM keyword_daily WHERE day = ?", (day,))
        }

    cur, prev = counts(days[0]), counts(days[1])
    return {
        w: cur.get(w, 0) - prev.get(w, 0)
        for w in (cur.keys() | prev.keys())
        if cur.get(w, 0) != prev.get(w, 0)
    }


# ─────────────── 과제 제안 ───────────────

def _versions(conn) -> List[Dict[str, str]]:
    """화면 VERSIONS 원소 목록.

    ★ 키 3개(id/label/trigger)는 이름·의미·순서가 불변이다.
      label 은 화면 표기(2026.08.06)이고, 버전 선택·정렬은 label 이 아니라
      id 와 sort_order 로 한다(_next_version 주석 참조).

    ★ 네 번째 키 at 은 **날짜가 아니라 시각**이다('2026.08.06 16:05').
      AI Reporting 의 '지난 발송 이후 생성분' 필터가 이 값을 report_setting.last_at
      과 문자열 비교한다. 예전에는 label(날짜)만으로 비교해서, 발송한 날에 만든
      과제가 그날 하루 통째로 발송 대상에서 빠졌다(같은 날짜끼리는 > 가 거짓).
      그래서 last_at 과 **같은 표기(점 구분 · 분 단위)** 로 맞춰서 내린다 —
      두 값의 포맷이 다르면 문자열 비교가 조용히 뒤집힌다('-'(45) < '.'(46)).
    """
    rows = conn.execute(
        "SELECT id, label, trigger, created_at FROM gen_version "
        " ORDER BY sort_order DESC, id DESC"
    ).fetchall()
    return [
        {
            "id": r["id"],
            "label": dot(r["label"]),
            "trigger": r["trigger"] or "",
            # created_at 은 ISO('2026-08-06T16:05:24'). 없으면 label 로 폴백한다
            # (시각을 모르는 시드 버전은 날짜만으로 비교돼 그날 발송분에서 빠진다 —
            #  없는 시각을 지어내는 것보다 낫다).
            "at": _dot_minute(r["created_at"]) or dot(r["label"]),
        }
        for r in rows
    ]


def _dot_minute(iso: Optional[str]) -> str:
    """'2026-08-06T16:05:24' → '2026.08.06 16:05'. 값이 없으면 빈 문자열.

    화면 표기(report_setting.last_at)와 **한 글자도 다르지 않은** 형식이어야 한다.
    """
    text = (iso or "").strip()
    if len(text) < 16:
        return ""
    return f"{dot(text[:10])} {text[11:16]}"


def _eval_flags(conn) -> Dict[int, List[Dict[str, str]]]:
    """과제 id → 최신 평가의 검증 이슈 목록 [{sev, msg}].

    ★ _proposals 의 SELECT 에 합치지 않는다. 이슈는 과제당 0~n건이라 조인하면
      행이 곱해져 GROUP_CONCAT(pe.feed_id) 의 근거 목록이 이슈 수만큼 부풀어
      화면의 근거 칩이 중복된다. 별도 쿼리 1회가 정답이다.
    """
    rows = conn.execute(
        """SELECT e.proposal_id AS pid, i.severity, i.message
           FROM proposal_evaluation e
           JOIN proposal_evaluation_issue i ON i.eval_id = e.id
           WHERE e.is_latest = 1
           ORDER BY e.proposal_id, i.seq"""
    ).fetchall()
    out: Dict[int, List[Dict[str, str]]] = {}
    for r in rows:
        out.setdefault(r["pid"], []).append({"sev": r["severity"], "msg": r["message"]})
    return out


def _proposals(conn) -> List[Dict[str, Any]]:
    """화면 TASKS 원소 목록 — 원소 1건이 21키다.

    ★ 기존 8키(id/ver/oc/lever/ev/name/sum/plan)는 이름·의미·순서가 불변이다.
      프론트 fill(TASKS, d.tasks) 가 이 키에 묶여 있어 **추가만** 허용된다.
      (이 계약을 pydantic 모델로 옮겨 response_model 로 붙이지 마라 — 모델에 없는
      키가 조용히 사라진다.)
    ★ ORDER BY v.sort_order DESC, p.id DESC 도 바꾸지 마라 —
      viewList 의 버전 그룹 헤더가 이 정렬을 전제로 그려진다.
    ★ **차단(verdict='차단') 과제도 목록에서 빼지 않는다.** 플래그만 단다 —
      숨기면 생성 버전 대다수가 0건이 되어 일별 생성 건수 차트와 캘린더가 통째로 빈다.

    kpi/kpiFx 는 과제별 값이 NULL 이면 레버 기본값으로 폴백한다(하위호환).
    lever 은 PK 조인이라 GROUP BY 결과가 부풀지 않는다.
    평가(proposal_evaluation)는 idx_pev_latest 부분 유니크 인덱스가 과제당
    is_latest=1 행을 하나로 강제하므로 LEFT JOIN 해도 행이 곱해지지 않는다.
    """
    rows = conn.execute(
        """SELECT p.id, p.ver_id, p.aff_code, p.lever, p.name, p.summary, p.plan,
                  p.background, p.risk, p.effect,
                  COALESCE(NULLIF(p.kpi_name, ''),    l.metric)  AS kpi,
                  COALESCE(NULLIF(p.kpi_formula, ''), l.formula) AS kpi_fx,
                  p.status, p.origin, p.created_at,
                  e.priority AS score, e.grade, e.verdict, e.scored_by,
                  GROUP_CONCAT(pe.feed_id) AS ev
           FROM proposal p
           LEFT JOIN proposal_evidence pe ON pe.proposal_id = p.id
           JOIN gen_version v ON v.id = p.ver_id
           LEFT JOIN lever l ON l.name = p.lever
           LEFT JOIN proposal_evaluation e
                  ON e.proposal_id = p.id AND e.is_latest = 1
           GROUP BY p.id
           ORDER BY v.sort_order DESC, p.id DESC"""
    ).fetchall()
    flags = _eval_flags(conn)
    return [
        {
            # ── 기존 8키 (불변) ──
            "id": r["id"], "ver": r["ver_id"], "oc": r["aff_code"], "lever": r["lever"],
            "ev": sorted(r["ev"].split(",")) if r["ev"] else [],
            "name": r["name"], "sum": r["summary"] or "", "plan": r["plan"] or "",
            # ── 과제 본문 8키 ──
            "bg": r["background"] or "",        # 배경 2문장
            "risk": r["risk"] or "",            # 핵심 리스크 1문장
            "eff": r["effect"] or "",           # 기대효과 1문장
            "kpi": r["kpi"] or "",              # 관리지표명 (없으면 lever.metric)
            "kpiFx": r["kpi_fx"] or "",         # KPI 산출식 (없으면 lever.formula)
            "status": r["status"] or "검토중",   # 검토중 / 채택 / 보류 / 반려
            "origin": r["origin"] or "자동",     # 자동 / 커스텀 / AI생성
            "at": r["created_at"] or "",
            # ── AI 평가 5키. 미평가 과제는 score=None · verdict='' 이다 ──
            # ★ evalScore = AI 채점 우선순위 0~100. 사용자 별점(state.fb[id].s, 0~5)과
            #   전혀 다른 값이다. 둘 다 "score" 로 불리던 시절에 화면에서 계속 혼동됐다.
            "evalScore": r["score"],            # 0~100 우선순위 (미평가면 None)
            "grade": r["grade"] or "",          # A / B / C
            "verdict": r["verdict"] or "",      # 통과 / 검토필요 / 차단 (기계 판정)
            "scoredBy": r["scored_by"] or "",   # LLM / 규칙 / 미채점
            "flags": flags.get(r["id"], []),    # [{sev: 차단|경고, msg: 한국어 설명}]
        }
        for r in rows
    ]


# ─────────────── 관리자 화면 ───────────────

def _sources(conn):
    rows = conn.execute(
        "SELECT name, url, type, paid, last_at, doc_count, fresh_count, status "
        "FROM crawl_source ORDER BY sort_order, id"
    ).fetchall()
    return [
        {
            "name": r["name"], "url": r["url"] or "", "type": r["type"] or "",
            "paid": bool(r["paid"]), "last": r["last_at"] or "—",
            "cnt": r["doc_count"], "fresh": r["fresh_count"], "st": r["status"],
        }
        for r in rows
    ]


def _crawl_at(conn) -> str:
    """마지막 파밍 완료 시각 '2026.08.07 03:00'(KST). 크롤 이력이 없으면 빈 문자열.

    ★ crawl_source.last_at 을 쓰지 않는 이유: 파이프라인이 그 컬럼에 **쓰지 않는다.**
      시드가 넣어 둔 '오늘 08:00' 을 그대로 보여 주다가 한 달 뒤에도 "오늘 08:00 갱신"
      이라고 말하는 화면이 됐고, 그래서 전부 '—' 로 지웠다. 그 결과 이번에는 자료가
      90건 실재하는데 사이드바가 '수집 이력 없음' 이라고 단정했다. 둘 다 거짓이다.
      **실제로 크롤한 시각은 feed_item.farmed_at 에 있다** — 진짜 값을 여기서 만든다.
    ★ farmed_at 은 UTC ISO 라 표시 전에 KST 로 옮긴다(NEW 배지와 같은 시계).
    ★ 값이 없으면 빈 문자열이다. 화면은 이때 그 줄을 통째로 렌더하지 않는다 —
      '수집 이력 없음' 같은 문구로 때우지 않는다.
    """
    row = conn.execute(
        "SELECT MAX(datetime(farmed_at, ?)) AS at FROM feed_item WHERE farmed_at IS NOT NULL",
        (LOCAL_TZ_SQL,),
    ).fetchone()
    return _dot_minute((row["at"] or "").replace(" ", "T")) if row else ""


def _uploads(conn):
    """내부 자료 목록 — bootstrap 페이로드용.

    ★ SELECT 는 반드시 컬럼을 **명시 열거**한다. `SELECT *` 로 바꾸지 마라.
      upload_file.body 는 내부 문서 전문(최대 300,000자)이고, 이 결과는 그대로
      /api/bootstrap 응답에 실려 브라우저로 나간다. `*` 한 글자면 검수 전 내부
      문서 본문이 전량 유출되고, 응답 크기도 수 MB 로 부푼다.
      화면에 새 값이 필요하면 여기에 컬럼을 하나 더 적어 넣어라(반환 키 추가는 허용,
      기존 6키 id/name/oc/size/at/st 의 이름 변경·삭제는 금지 — 프론트가 묶여 있다).
    """
    rows = conn.execute(
        "SELECT id, name, aff, size, uploaded_at, status FROM upload_file ORDER BY id DESC"
    ).fetchall()
    return [
        {"id": r["id"], "name": r["name"], "oc": r["aff"] or "전사",
         "size": r["size"] or "", "at": r["uploaded_at"] or "", "st": r["status"]}
        for r in rows
    ]


# ─────────────── 사용자별 상태 ───────────────

def _user_state(conn, email: str) -> Dict[str, Any]:
    fb = {
        # s = 사용자 별점(0~5). AI 채점(tasks[].evalScore, 0~100)과 다른 개념이다.
        str(r["proposal_id"]): {"s": r["star"], "t": r["memo"]}
        for r in conn.execute(
            "SELECT proposal_id, star, memo FROM proposal_feedback WHERE user_email = ?", (email,)
        )
    }
    fields = {
        str(r["proposal_id"]): _loads(r["fields"], {})
        for r in conn.execute(
            "SELECT proposal_id, fields FROM proposal_input WHERE user_email = ?", (email,)
        )
    }
    fx, sys_off = {}, {}
    for r in conn.execute(
        "SELECT proposal_id, sys_off, text, updated_at FROM proposal_formula WHERE user_email = ?",
        (email,),
    ):
        pid = str(r["proposal_id"])
        if r["text"]:
            fx[pid] = {"text": r["text"], "at": r["updated_at"] or ""}
        if r["sys_off"]:
            sys_off[pid] = True

    send_off = {
        str(r["proposal_id"]): True
        for r in conn.execute(
            "SELECT proposal_id FROM report_exclude WHERE user_email = ?", (email,)
        )
    }
    # 아직 저장한 설정이 없는 계정에는 시드된 기본값을 보여 준다.
    defaults = _loads(get_setting(conn, "report_defaults"), {})
    rs = conn.execute(
        "SELECT freq, send_time, channels, last_at FROM report_setting WHERE user_email = ?",
        (email,),
    ).fetchone()
    if rs:
        send = {"freq": rs["freq"], "time": rs["send_time"], "lastAt": rs["last_at"] or ""}
        channels = _loads(rs["channels"], dict(DEFAULT_CHANNELS))
        recipients = [
            r["label"]
            for r in conn.execute(
                "SELECT label FROM report_recipient WHERE user_email = ? ORDER BY rowid", (email,)
            )
        ]
    else:
        send = {
            "freq": defaults.get("freq", DEFAULT_REPORT["freq"]),
            "time": defaults.get("time", DEFAULT_REPORT["time"]),
            "lastAt": defaults.get("lastAt", ""),
        }
        channels = defaults.get("channels", dict(DEFAULT_CHANNELS))
        recipients = list(defaults.get("recipients", []))
    return {
        "fb": fb, "fields": fields, "fx": fx, "sysOff": sys_off,
        "sendOff": send_off, "send": send, "recipients": recipients, "channels": channels,
    }


# ─────────────── bootstrap ───────────────
# ★ eval_criteria() 래퍼는 지웠다. bootstrap 의 evalCriteria 키 하나만 쓰던 함수인데
#   화면이 그 문장을 렌더하는 지점이 없다. 평가 기준 문장이 필요하면
#   GET /api/evaluation/criteria (가중치까지 함께 준다)를 쓰면 된다.


def bootstrap(email: str) -> Dict[str, Any]:
    """화면이 뜰 때 한 번 호출하는 초기 데이터 묶음 — 최상위 22키.

    ★ 키 이름은 프론트 상수명을 camelCase 로 옮긴 것이다(EV_OC→evOc, KW_TREND→kwTrend).
      화면 applyBootstrap 이 이 이름으로 상수를 채우므로 마음대로 바꾸지 마라.
    ★ 여기 없는 키를 화면이 쓰면 그 화면은 상수 데모로 되돌아간다. 반대로 화면이 안 쓰는
      키를 내리면 페이로드만 커진다 — themes/evTheme/admins/evalCriteria 4키를 뺀 이유다.
    """
    conn = get_connection()
    try:
        ocs, oc_color = _ocs(conn)
        ev, ev_biz, ev_new, kind_map = _evidence(conn)
        return {
            "user": {"email": email},
            # 기간 필터 기준일 — **매 요청 시점의 실제 날짜(KST)** 다.
            # 화면 TR_TODAY 의 유일한 출처이고 기간 필터의 시작·종료 양쪽이 이 값을 쓴다.
            # ★ 모듈 상수(config.TODAY)를 쓰면 서버를 며칠 띄웠을 때 부팅일에 굳는다.
            "today": today_local(),
            "kinds": _kind_labels(conn),
            "ocs": ocs,
            "ocColor": oc_color,
            "bizColor": _biz_colors(conn),
            "levers": _levers(conn),
            "evidence": ev,
            "evBizFallback": ev_biz,
            "evNew": ev_new,
            # ── 트렌드룸 신규 4키 ──
            "evOc": _ev_oc(conn),        # 자료 → 계열사 코드 (feed_item_tag)
            "evKw": _ev_kw(conn),        # 자료 → 동향 키워드 (feed_item_keyword)
            "evBrief": _ev_brief(conn),  # 자료 → 브리핑 문장 (feed_item.brief, LLM 전용)
            "kwTrend": _kw_trend(conn),  # 키워드 → 전일 대비 증감 (keyword_daily)
            "kindMap": kind_map,
            "versions": _versions(conn),
            "tasks": _proposals(conn),
            "sources": _sources(conn),
            # 마지막 파밍 완료 시각(KST). 사이드바 '수집 파이프라인' 과 트렌드룸 헤더가
            # 쓴다. crawl_source.last_at 은 아무도 갱신하지 않는 시드 값이라 못 쓴다.
            "crawlAt": _crawl_at(conn),
            "uploads": _uploads(conn),
            "instruction": get_setting(conn, "instruction"),
            "state": _user_state(conn, email),
        }
    finally:
        conn.close()


# ★ 아래 sources()/uploads()/user_state() 는 커넥션 관리만 감싼 1:1 래퍼다.
#   화면은 이 데이터를 GET /api/bootstrap 이 부르는 _sources/_uploads/_user_state
#   (커넥션을 받는 쪽)로 받으므로, app/ 안에서 부르는 곳은 없다
#   (user_state 는 tests/test_discovery_context.py 가 쓴다).
#   **지우지 마라.** 비용이 0 이고, 관리자 화면을 부분 갱신하는 라우트를 다시 붙일 때
#   여기가 그대로 진입점이 된다. 지우면 그때 _xxx(conn) 호출부마다 커넥션 열고 닫는
#   코드가 복사된다.
def sources() -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        return _sources(conn)
    finally:
        conn.close()


def uploads() -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        return _uploads(conn)
    finally:
        conn.close()


def instruction() -> Dict[str, str]:
    conn = get_connection()
    try:
        return {
            "text": get_setting(conn, "instruction"),
            "default": get_setting(conn, "instruction_default"),
        }
    finally:
        conn.close()


def user_state(email: str) -> Dict[str, Any]:
    conn = get_connection()
    try:
        return _user_state(conn, email)
    finally:
        conn.close()


# ★ 과제 1건의 축별 점수·사유·재평가 이력을 화면에 붙일 자리다. 데이터는 지금도
#   proposal_evaluation / proposal_evaluation_issue 에 쌓이고 있으니 조회 함수만
#   만들면 된다(화면 진입점이 없어 라우트와 함께 두지 않았다).


def proposals_payload() -> Dict[str, Any]:
    """재생성·커스텀 생성 후 화면이 갈아끼울 목록."""
    conn = get_connection()
    try:
        return {"versions": _versions(conn), "tasks": _proposals(conn)}
    finally:
        conn.close()


# ─────────────── 변경 (과제 제안) ───────────────

# 지우는 문자: 공백류 · 구분기호 · 문장부호 · 각종 따옴표/괄호/대시.
# ★ '#' 는 절대 넣지 마라 — seed._disambiguate_proposal_name_key 가 중복 해소용으로
#   키 뒤에 '#id' 를 붙인다. 여기서 지우면 그 구분이 사라져 마이그레이션이 무한 반복된다.
_NAME_KEY_RE = re.compile(r"[\s·・/\\|()\[\]{}<>〈〉《》「」『』"
                          r"\-‐‑‒–—―~〜!?.,:;'\"“”‘’„‟`´…·]+")

# 정규화 규칙 개정 번호. 규칙을 바꾸면 **반드시 +1** 하라 —
# seed._recompute_name_key 가 이 값이 DB 에 기록된 값과 다를 때만 전량 재계산한다.
# (기존 행의 키가 옛 규칙 그대로면 새 규칙으로 만든 키와 안 걸려 중복이 통과한다.)
NAME_KEY_REV = 2


def name_key(name: str) -> str:
    """중복 차단용 정규화 과제명 — 공백·괄호·문장부호를 지우고 소문자화.

    'NCC 정기보수 공기 단축 — 공정 병렬화' → 'ncc정기보수공기단축공정병렬화'
    같은 aff_code 안에서 같은 키가 이미 있으면 그 과제를 버린다.

    ★ 문장부호를 지우고 NFKC 정규화를 먼저 하는 이유 (실측으로 뚫렸다)
      예전 규칙은 공백··/()-[] 만 지웠다. 그래서 과제명 **끝에 마침표 하나**만 붙이면
      키가 달라져 L1(완전일치)과 L3(UNIQUE)를 둘 다 통과했고, 남는 것은 force 로 넘길 수
      있는 퍼지 판정뿐이라 확인 한 번에 화면상 글자가 똑같은 과제가 만들어졌다
      (실측: '…적용 검토' 와 '…적용 검토.' 가 나란히 저장됨). 쉼표·물음표·느낌표·
      따옴표·전각공백도 같은 구멍이었다. NFKC 는 전각/반각·호환문자를 한 표기로 모은다
      ('ＮＣＣ'→'NCC', '　'→' ', '㈜'→'(株)' 후 괄호 제거).

    ★ (aff_code, name_key) 는 **DB UNIQUE 제약**이다(schema.sql idx_proposal_namekey).
      예전에는 이미 쌓인 중복 행 때문에 인덱스를 못 만들었는데, seed._disambiguate_
      proposal_name_key 가 늦게 만들어진 쪽의 키에 '#id' 를 붙여 해소한 뒤 승격했다.
      즉 파이썬 검사(name_key_exists / find_by_name_key)는 **친절한 사전 안내**이고,
      마지막 방어는 DB 다 — 동시 job 두 개가 같은 이름을 넣으면 IntegrityError 가 난다.

    ★ 이 함수의 계산식을 바꾸면 **이미 저장된 행의 키는 옛 규칙 그대로**라 새 키와
      안 걸린다. 반드시 NAME_KEY_REV 를 올려 seed 가 전량 재계산하게 하라.
    """
    return _NAME_KEY_RE.sub("", unicodedata.normalize("NFKC", name or "")).lower()


def name_key_exists(conn, aff_code: str, key: str, exclude_id: Optional[int] = None) -> bool:
    """같은 계열사에 같은 정규화 과제명이 이미 있는가. (idx_proposal_namekey 사용)"""
    if not key:
        return False
    sql = "SELECT 1 FROM proposal WHERE aff_code = ? AND name_key = ?"
    args: List[Any] = [aff_code, key]
    if exclude_id is not None:
        sql += " AND id <> ?"
        args.append(exclude_id)
    return conn.execute(sql + " LIMIT 1", args).fetchone() is not None


def find_by_name_key(conn, aff_code: str, key: str) -> Optional[Any]:
    """같은 계열사의 동일 과제명 행(id·name·created_at) 또는 None.

    name_key_exists 의 '무엇과 중복인지' 를 알려 주는 버전이다 — 거부 화면이 #id 와
    과제명을 보여 주려면 bool 로는 부족하다. (idx_proposal_namekey 사용)
    """
    if not key:
        return None
    return conn.execute(
        "SELECT id, name, created_at FROM proposal WHERE aff_code = ? AND name_key = ? LIMIT 1",
        (aff_code, key),
    ).fetchone()


def _next_version(conn):
    """다음 생성 버전 id·label·정렬값. label 은 **오늘 날짜**(= 실제 생성일).

    ★ 반드시 `BEGIN IMMEDIATE` 트랜잭션 안에서 불러야 한다(_open_version 참조).
      읽고-쓰기 사이에 다른 요청이 끼어들면 같은 id 를 두 번 발급해
      UNIQUE constraint 로 500 이 난다.

    id 는 COUNT 가 아니라 **기존 최대 번호 + 1** 이다. COUNT 를 쓰면 중간 버전이
    삭제됐을 때 이미 있는 번호를 다시 발급한다(빈 버전 정리 후 실제로 겹쳤다).

    ★ label 을 '직전 라벨 + 1일' 로 만들지 마라. 화면(캘린더·차트·버전 헤더)이
      label 을 **생성일로 그대로 표시**하므로, 하루에 여러 번 재생성하면 표시 날짜가
      실제 생성일보다 미래로 계속 밀린다(실측: 하루 11회 재생성으로 두 달이 밀렸다).
      같은 날 여러 버전이 생기면 label 이 겹치는데, 겹쳐도 화면은 깨지지 않는다 —
      버전 선택은 label 이 아니라 id(data-ver / data-cal-d)로 하고, 캘린더는 그날의
      모든 버전을 합산해 한 칸으로 그린다.
      정렬은 label 이 아니라 sort_order 가 담당하므로 순서도 흐트러지지 않는다.
    """
    row = conn.execute(
        "SELECT id, sort_order FROM gen_version ORDER BY sort_order DESC, id DESC LIMIT 1"
    ).fetchone()
    order = (row["sort_order"] if row else 0) + 1
    nxt = date.today().isoformat()
    n = conn.execute(
        "SELECT COALESCE(MAX(CAST(SUBSTR(id, 2) AS INTEGER)), 0) AS m "
        "FROM gen_version WHERE id GLOB 'n[0-9]*'"
    ).fetchone()["m"]
    return f"n{n + 1}", nxt, order


def _open_version(conn, trigger: str, source: str, model: Optional[str] = None):
    """쓰기 트랜잭션을 잡고 새 생성 버전을 만든다. 새 ver_id 를 돌려준다.

    BEGIN IMMEDIATE 로 시작하므로 두 번째 동시 요청은 sqlite3 의 busy timeout 만큼
    기다렸다가 갱신된 값을 읽는다 — 동시 재생성이 UNIQUE 충돌로 죽지 않는다.
    """
    conn.execute("BEGIN IMMEDIATE")
    ver_id, label, order = _next_version(conn)
    conn.execute(
        "INSERT INTO gen_version(id, label, trigger, created_at, sort_order, source, model) "
        "VALUES (?,?,?,?,?,?,?)",
        (ver_id, label, trigger, datetime.now().isoformat(timespec="seconds"),
         order, source, model),
    )
    return ver_id


def _insert_proposal(conn, ver_id, aff, lever, name, summary, plan, ev_ids, origin,
                     *, background=None, risk=None, effect=None,
                     kpi_name=None, kpi_formula=None, kb_refs=None,
                     status="검토중") -> int:
    """과제 1건을 넣고 **새로 채번된 id** 를 돌려준다.

    ★ id 는 반드시 NULL 로 넣는다. proposal.id 는 INTEGER PRIMARY KEY = rowid 별칭이라
      SQLite 가 INSERT 시점에 원자적으로 채번하고, 그 값을 cur.lastrowid 로 받는다.
      예전처럼 MAX(id)+1 을 미리 읽어 넣으면 두 요청이 같은 값을 읽어 뒤엣것이
      UNIQUE 위반(500)으로 죽는다 — 읽기와 쓰기 사이에 잠금이 없기 때문이다.

    name_key 는 여기서 name 에서 파생 계산한다(저장 시점 단일 계산 지점).
    kb_refs 는 리스트/문자열 둘 다 받아 콤마 결합해 저장한다.
    """
    if isinstance(kb_refs, (list, tuple, set)):
        kb_refs = ",".join(str(x) for x in kb_refs) or None
    cur = conn.execute(
        """INSERT INTO proposal(id, ver_id, aff_code, lever, name, summary, plan,
                                origin, created_at, background, risk, effect,
                                kpi_name, kpi_formula, status, name_key, kb_refs)
           VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (ver_id, aff, lever, name, summary, plan, origin,
         datetime.now().isoformat(timespec="seconds"),
         background, risk, effect, kpi_name, kpi_formula,
         status or "검토중", name_key(name), kb_refs),
    )
    pid = cur.lastrowid
    for fid in ev_ids:
        conn.execute(
            "INSERT OR IGNORE INTO proposal_evidence(proposal_id, feed_id) VALUES (?,?)",
            (pid, fid),
        )
    return pid


def _auto_evaluate(pids: List[int]) -> None:
    """새로 저장된 과제에 **규칙 채점**을 자동으로 붙인다 (LLM 0회 · 실측 0.02초).

    ★ import 를 함수 안에서 한다 — store ↔ app.pipeline.evaluation 순환 import 방지.
    ★ use_llm=False 를 절대 빼지 마라. LLM 채점은 계열사당 수십 초라 재생성
      응답 시간에 그대로 얹힌다(1초를 넘으면 이 인자가 안 먹은 것이다).
    ★ 예외를 삼킨다 — 평가가 실패해도 과제 생성 자체는 성공으로 끝나야 한다.
      나중에 POST /api/evaluation/run 으로 다시 돌릴 수 있다.
    ★ DB 커넥션을 새로 열므로 반드시 **commit 이후**에 부를 것. 열린 쓰기
      트랜잭션 안에서 부르면 BEGIN IMMEDIATE 가 자기 자신과 잠금 경합한다.
    """
    if not pids:
        return
    from app.pipeline.evaluation.runner import evaluate_after_write
    evaluate_after_write(pids)


def _fresh_count(conn) -> int:
    """오늘(KST) 크롤한 자료 건수 — 버전 trigger 문구 '외부 자료 N건 반영' 의 N.

    ★ 이 값은 gen_version.trigger 에 **영구 기록**된다. 저장 플래그(is_new)를 읽으면
      파밍을 안 돌린 몇 달 뒤에도 같은 화석 숫자가 새 버전에 박힌다.
    """
    return conn.execute(
        "SELECT COUNT(*) AS c FROM feed_item "
        " WHERE farmed_at IS NOT NULL AND date(farmed_at, ?) = ?",
        (LOCAL_TZ_SQL, today_local()),
    ).fetchone()["c"]


def _regen_targets(conn, limit: int) -> List[str]:
    """이번 재생성에서 발굴할 계열사 코드.

    우선순위: 새로 들어온 외부 자료(오늘(KST) 크롤분)가 많은 계열사 → 그 다음으로 오래 전에
    과제를 만든 계열사. 자료가 하나도 안 붙은 계열사는 근거 0건이라 어차피 저장되지
    않으므로 대상에서 빠진다(feed_item_tag INNER JOIN).
    """
    rows = conn.execute(
        # last_pid 를 LEFT JOIN 으로 구하면 행이 곱해져 SUM(fresh) 이 계열사 과제수 배로
        # 부풀고, 우선순위가 '자료가 새로 많이 들어온 계열사' 가 아니라 '이미 과제가 많은
        # 계열사' 로 뒤집힌다(그러면 대상이 두 곳에 영구 고착된다). 상관 서브쿼리로 분리한다.
        """SELECT t.aff_code AS oc,
                  SUM(CASE WHEN f.farmed_at IS NOT NULL
                            AND date(f.farmed_at, ?) = ? THEN 1 ELSE 0 END) AS fresh,
                  (SELECT COALESCE(MAX(p.id), 0) FROM proposal p
                    WHERE p.aff_code = t.aff_code) AS last_pid
           FROM feed_item_tag t
           JOIN feed_item f ON f.id = t.feed_id
           GROUP BY t.aff_code
           ORDER BY fresh DESC, last_pid ASC""",
        (LOCAL_TZ_SQL, today_local()),
    ).fetchall()
    return [r["oc"] for r in rows[:max(0, limit)]]


def _llm_drafts(targets: List[str]) -> Dict[str, list]:
    """계열사별 과제 초안을 LLM 으로 만든다. **절대 예외를 올리지 않는다.**

    비용: 계열사 1곳당 LLM 1회(codex-cli 실측 10~16초). 기본 2곳이므로 호출 2회.
    동시 실행이라 벽시계는 15~30초 — codex 는 동시 3건까지 안전하다는 실측이 있어
    max_workers 는 대상 수(≤3)로 제한한다.

    한 계열사가 타임아웃·파싱 실패로 죽어도 나머지는 그대로 살린다(부분 실패 허용).

    ★ ThreadPoolExecutor 를 쓰지 않고 **데몬 스레드**를 직접 쓴다. 이유가 둘이다(실측).
      1) `with ThreadPoolExecutor(...)` 의 __exit__ 는 shutdown(wait=True) 라서 아직 도는
         codex 를 끝까지 기다린다 → OI_REGEN_TIMEOUT 이 무력해지고 재생성이 4분을 넘겼다.
      2) shutdown(wait=False) 로 바꿔도 concurrent.futures 가 인터프리터 종료 시
         워커 스레드를 join 하는 atexit 훅을 걸어 두어, CLI/테스트 프로세스가 안 끝난다.
      데몬 스레드는 둘 다 없다. 마감시각을 넘긴 스레드는 그대로 버린다 — codex 는
      read-only 서브프로세스이고 결과를 아무도 읽지 않으므로 DB 에는 영향이 없다.
    """
    import threading
    import time as _time

    from app.pipeline.discovery import agent

    out: Dict[str, list] = {}
    if not targets:
        return out

    results: Dict[str, Any] = {}          # oc -> drafts 또는 Exception (GIL 하에서 원자적)

    def _work(oc: str) -> None:
        try:
            results[oc] = agent.generate_tasks(oc, "", OI_REGEN_TASKS)
        except Exception as e:            # 파싱 실패·CLI 오류·codex 자체 타임아웃
            results[oc] = e

    threads = [
        threading.Thread(target=_work, args=(oc,), name=f"oi-discovery-{oc}", daemon=True)
        for oc in targets
    ]
    for t in threads:
        t.start()
    # 계열사별이 아니라 **전체 한 번의 마감시각**이다. 스레드마다 같은 상한을 주면
    # 마감이 계열사 수만큼 곱해진다.
    deadline = _time.monotonic() + OI_REGEN_TIMEOUT
    for t in threads:
        t.join(max(0.0, deadline - _time.monotonic()))

    for oc in targets:
        value = results.get(oc)
        if value is None:
            log.warning("과제 발굴 시간 초과 (%s) — %d초에서 끊고 버립니다.", oc, OI_REGEN_TIMEOUT)
        elif isinstance(value, Exception):
            # TimeoutError 는 메시지가 비어 있어 타입명을 반드시 같이 남긴다.
            log.warning("과제 발굴 실패 (%s): %s: %s", oc, type(value).__name__, value)
        elif value:
            out[oc] = value
    return out


# 새로 저장할 과제가 하나도 없을 때 화면에 그대로 보여 줄 문장.
# 프론트가 `d.reason` 을 alert 로 띄우므로 사용자가 읽는 문장 그대로 둔다.
NO_CANDIDATE = "새 후보가 없습니다."


def regenerate(count: int = 2) -> Dict[str, Any]:
    """새 생성 버전을 만든다 — **LLM 발굴이 기본, 후보 풀이 폴백**.

    경로 1 (기본) : 대상 계열사 OI_REGEN_OCS 곳에 대해 발굴 LLM 을 돌리고
                    persist.save_drafts 로 proposal 에 저장한다. gen_version.source='AI생성'.
    경로 2 (폴백) : LLM 이 없거나(ready=False) 전부 실패했거나 저장된 과제가 0건이면
                    기존처럼 후보 풀을 순환 재사용한다. gen_version.source='후보풀'.

    ★ 재생성 횟수에는 제한이 없다(사용자 결정). 대신 **중복만 차단**한다 —
      두 경로 모두 persist.save_drafts 한 곳에서 같은 기준(레버 정규화 · name_key
      완전일치 · 같은 레버·근거 조합 · 근거 실재성)으로 판정한다.
    ★ 후보 풀 SELECT 에 `WHERE used_at IS NULL` 을 넣지 않는다(사용자 결정).
      LLM 이 없는 환경에서도 재생성 버튼이 계속 동작해야 하므로 풀은 소진되지 않는다.
    ★ 어떤 경우에도 예외를 밖으로 올리지 않는다. 새로 저장할 과제가 하나도 없으면
      {"ver": None, "reason": …} 을 돌려주고 **화면이 사유를 표시**한다 —
      조용히 아무 일도 안 일어난 것처럼 보이면 사용자가 버튼을 계속 누른다.
    """
    # LLM 호출은 DB 커넥션을 잡기 전에 끝낸다 — 30초 동안 쓰기 트랜잭션을 여는 것을 피한다.
    drafts_by_oc: Dict[str, list] = {}
    model = None
    if OI_REGEN_LLM:
        try:
            ok, why = llm_client.ready(OI_TASK_PROVIDER)
        except Exception as e:            # provider 판정 자체가 죽어도 폴백으로 간다
            ok, why = False, str(e)
        if ok:
            conn = get_connection()
            try:
                targets = _regen_targets(conn, OI_REGEN_OCS)
            finally:
                conn.close()
            drafts_by_oc = _llm_drafts(targets)
            # codex 는 OI_MODEL 을 무시하고 OI_CODEX_MODEL 만 본다(빈 값이면 codex 기본 모델).
            # 여기에 claude 별칭을 적어 두면 나중에 '어느 모델 산인가' 추적이 거짓이 된다.
            model = (f"{OI_TASK_PROVIDER}/{OI_CODEX_MODEL or '기본'}"
                     if OI_TASK_PROVIDER == "codex-cli"
                     else f"{OI_TASK_PROVIDER}/{OI_MODEL}")
        else:
            log.info("발굴 LLM 미사용 — 후보 풀로 폴백합니다: %s", why)

    conn = get_connection()
    try:
        now = datetime.now().isoformat(timespec="seconds")
        fresh = _fresh_count(conn)

        # ── 경로 1: LLM 생성분 저장 ────────────────────────────────────
        if drafts_by_oc:
            from app.pipeline.discovery import persist

            ver_id = _open_version(conn, "", "AI생성", model)
            parts, total, new_pids = [], 0, []
            for oc, drafts in drafts_by_oc.items():
                ids = persist.save_drafts(conn, ver_id, oc, drafts, origin="AI생성")
                if ids:
                    total += len(ids)
                    new_pids += list(ids)
                    row = conn.execute(
                        "SELECT name FROM affiliate WHERE code = ?", (oc,)
                    ).fetchone()
                    parts.append(f"{row['name'] if row else oc} {len(ids)}건")
            if total:
                # viewList 가 trigger 를 그대로 렌더한다 — 프론트 0줄로 생성 방식이 노출된다.
                conn.execute(
                    "UPDATE gen_version SET trigger = ? WHERE id = ?",
                    (f"AI 생성 · {' · '.join(parts)} · 외부 자료 {fresh}건 반영", ver_id),
                )
                conn.commit()
                # 규칙 채점 자동 실행 — LLM 0회 · 실측 0.02초. 화면이 재생성 직후
                # 바로 점수·플래그를 보게 하려고 payload 를 만들기 **전에** 돌린다.
                _auto_evaluate(new_pids)
                return {"ver": ver_id, **proposals_payload()}
            # 한 건도 저장되지 않았다 — 빈 생성 버전을 남기지 않고 폴백한다.
            conn.rollback()
            log.warning("발굴 결과가 전부 걸러졌습니다 — 후보 풀로 폴백합니다.")

        # ── 경로 2: 후보 풀 폴백 ──────────────────────────────────────
        # LIMIT 을 걸지 않고 풀 전체를 훑는다. 앞쪽 몇 건이 이미 저장된 과제와 중복이어도
        # 뒤쪽에 남은 새 후보까지 찾아내야 하기 때문이다(LIMIT 2 면 앞의 2건이 영원히
        # 중복이라 재생성이 항상 0건이 된다).
        pool = conn.execute(
            "SELECT * FROM proposal_pool ORDER BY (used_at IS NOT NULL), used_at, id"
        ).fetchall()
        if not pool:
            return {"ver": None, "reason": NO_CANDIDATE, **proposals_payload()}

        from app.pipeline.discovery import persist
        from app.models import TaskDraft

        ver_id = _open_version(
            conn, f"후보 풀 · 외부 자료 {max(fresh, len(pool))}건 갱신", "후보풀"
        )
        pool_pids: List[int] = []
        for p in pool:
            if len(pool_pids) >= count:
                break
            # ★ 중복 판정을 여기서 다시 구현하지 않는다. 초안 1건씩 save_drafts 에 넘겨
            #   LLM 경로와 **완전히 같은 규칙**을 태운다. 같은 커넥션·같은 트랜잭션이라
            #   방금 INSERT 한 행도 다음 반복의 중복 검사에 그대로 보인다.
            draft = TaskDraft(
                title=p["name"],
                category=p["lever"], lever=p["lever"],
                summary=p["summary"] or "", plan=p["plan"] or "",
                evidence=[e for e in (p["evidence"] or "").split(",") if e],
            )
            ids = persist.save_drafts(conn, ver_id, p["aff_code"], [draft], origin="자동")
            if not ids:
                continue          # 중복·레버 불명·근거 없음 — used_at 도 올리지 않는다
            pool_pids += ids
            conn.execute("UPDATE proposal_pool SET used_at = ? WHERE id = ?", (now, p["id"]))
        if not pool_pids:
            # 빈 생성 버전을 남기지 않는다(LLM 경로와 같은 처리).
            conn.rollback()
            log.info("후보 풀에 새 후보가 없습니다 — 생성 버전을 만들지 않습니다.")
            return {"ver": None, "reason": NO_CANDIDATE, **proposals_payload()}
        conn.commit()
    finally:
        conn.close()
    _auto_evaluate(pool_pids)
    return {"ver": ver_id, **proposals_payload()}


def create_custom(oc: str, lever: str, ev_ids: List[str], plan: str,
                  name: Optional[str] = None, summary: Optional[str] = None,
                  *, background: Optional[str] = None, risk: Optional[str] = None,
                  effect: Optional[str] = None, kpi_name: Optional[str] = None,
                  kpi_formula: Optional[str] = None, kb_refs=None,
                  origin: str = "커스텀", status: str = "검토중") -> Dict[str, Any]:
    """커스텀 생성 — 최신 버전에 과제 1건을 붙인다. **문자열 조립만 한다(LLM 0회).**

    발굴 LLM 산출 본문(background/risk/effect/kpi_*/kb_refs)은 인자로 받는다.
    화면 경로는 create_custom_llm 이 이 값들을 채워서 부른다 — LLM 이 실패했을 때만
    아무것도 안 넘긴 채로 불려서 예전처럼 이름·요약만 조립한 과제가 만들어진다.
    (그때 background 등이 NULL 인 것은 폴백의 정상 동작이다.)

    ★ **중복이면 만들지 않는다(L2 게이트).** 예전에는 "현업이 명시적으로 지시한
      경로라 같은 이름이어도 만들어져야 한다" 는 근거로 검사를 건너뛰었는데, 그 결과
      같은 과제가 5번 반복 생성됐다(id 1401~1405). 그 설계 근거는 기각됐다 —
      되돌리지 마라. 라우트가 이미 사전검사(api/proposals.create_custom)를 하지만
      이름을 근거·LLM 에서 **파생하는 경로**(name 미지정)는 라우트가 볼 수 없어
      저장 직전에 한 번 더 본다.
      거부 시 예외가 아니라 {"id": None, "reason": ...} 을 돌려준다 — 이 함수는
      jobs.start 안에서 돌아 job 봉투가 상태코드를 소유하기 때문이다.
    """
    from app.pipeline.discovery.lever_map import normalize_lever

    conn = get_connection()
    try:
        # 레버는 lever(name) FK 다. 변형 표기를 정식명으로 바꾸고, 못 바꾸면 저장하지 않는다
        # (임의 레버를 넣으면 화면이 틀린 금액을 계산한다).
        canon = normalize_lever(lever, conn)
        if not canon:
            raise ValueError(f"알 수 없는 레버입니다: {lever}")
        lever = canon
        ver = conn.execute(
            "SELECT id FROM gen_version ORDER BY sort_order DESC, id DESC LIMIT 1"
        ).fetchone()
        if not ver:
            raise ValueError("생성 버전이 없습니다. 먼저 시드를 넣어 주세요.")
        srcs = []
        for fid in ev_ids:
            # 과제 이름·요약에 들어가는 문자열이므로 표시용 라벨을 우선한다
            # (SEC title 은 '8-K' 같은 서식코드 단독이라 그대로 쓰면 이름이 망가진다).
            r = conn.execute(
                """SELECT COALESCE(NULLIF(source_label, ''), source) AS source,
                          COALESCE(NULLIF(title_label, ''), title)   AS title
                     FROM feed_item WHERE id = ?""",
                (fid,),
            ).fetchone()
            if r:
                srcs.append((r["source"], r["title"]))
        if not name:
            base = srcs[0][1] if srcs else f"{lever} 개선"
            name = f"{base} 적용 검토"
        if not summary:
            summary = (f"{srcs[0][0]} 사례 — {plan}" if srcs else plan) or ""

        # L2 — 이름이 확정된 뒤 저장 직전. 여기서 걸리면 INSERT 도 commit 도 하지 않는다.
        dup = find_by_name_key(conn, oc, name_key(name))
        if dup is not None:
            return {
                "id": None, "ver": ver["id"],
                "reason": f"같은 이름의 과제가 이미 있습니다 — #{dup['id']}. 새로 만들지 않았습니다.",
                "dupId": dup["id"],
                **proposals_payload(),
            }

        pid = _insert_proposal(
            conn, ver["id"], oc, lever, name, summary, plan, ev_ids, origin,
            background=background, risk=risk, effect=effect,
            kpi_name=kpi_name, kpi_formula=kpi_formula, kb_refs=kb_refs, status=status,
        )
        conn.commit()
    finally:
        conn.close()
    _auto_evaluate([pid])
    return {"id": pid, "ver": ver["id"], **proposals_payload()}


# ─────────────── 커스텀 생성 + 발굴 LLM ───────────────
#
# 사람이 발굴 조건을 직접 지정하는 유일한 경로다 —
#   ① 계열사(OC)를 직접 고르고  ② note(현업 지정 조건)를 프롬프트에 주입한다.
# 커스텀 생성 화면의 입력(OC · 근거 사례 · 레버 · 적용 방향)이 그대로 여기로 들어온다.

_CUSTOM_NOTE = """[현업 지정 조건 — 이번 과제는 아래 조건을 반드시 지킨다]
- 과제는 정확히 1건만 만든다.
- 개선 레버는 반드시 "{lever}" 하나로 한다. 다른 레버를 쓰면 이 과제는 버려진다.
- 아래 벤치마크 사례를 근거로 삼는다. evidence 에는 이 (ev:...) id 만 넣는다.
{ev_block}
- 적용 방향(현업이 고른 것): {plan}
  plan 은 이 방향을 그대로 따르되, 대상(무엇을)과 수단(어떻게)이 드러나는 1문장으로 구체화한다.
{name_line}"""


def _custom_note(conn, lever: str, ev_ids: List[str], plan: str,
                 name: Optional[str]) -> str:
    """커스텀 생성 입력을 발굴 프롬프트의 note 블록 문장으로 바꾼다.

    ★ 사용자가 고른 근거는 계열사 [외부 동향] 블록에 없을 수도 있다(다른 계열사 자료를
      벤치마크로 고를 수 있다). 그래서 note 안에 자료 본문을 직접 실어 준다 —
      실지 않으면 모델이 (ev:e12) 라는 id 만 보고 내용을 모른 채 과제를 지어낸다.
    """
    lines = []
    for fid in ev_ids:
        r = conn.execute(
            """SELECT COALESCE(NULLIF(source_label, ''), source) AS src,
                      COALESCE(NULLIF(title_label, ''), title)   AS title,
                      published_on, summary
                 FROM feed_item WHERE id = ?""",
            (fid,),
        ).fetchone()
        if not r:
            continue
        body = (r["summary"] or "").strip().replace("\n", " ")
        lines.append(
            f"  · (ev:{fid}) [{r['published_on']} · {r['src']}] {r['title']}"
            + (f"\n    {body[:300]}" if body else "")
        )
    return _CUSTOM_NOTE.format(
        lever=lever,
        ev_block="\n".join(lines) or "  · (근거로 고른 자료가 없다. 내부 지식만으로 만든다.)",
        plan=(plan or "").strip() or "(지정 없음)",
        name_line=f'- 과제명은 "{name}" 을 쓴다.' if name else "",
    )


def create_custom_llm(oc: str, lever: str, ev_ids: List[str], plan: str,
                      name: Optional[str] = None,
                      summary: Optional[str] = None) -> Dict[str, Any]:
    """커스텀 생성(화면 경로) — 발굴 LLM 으로 본문을 채우고 과제 1건을 저장한다.

    ★ **중복이면 만들지 않고 사유를 돌려준다**({"id": None, "reason": ...}).
      LLM 미설정·타임아웃·파싱 실패는 폴백일 뿐이다 — 그때는 예전 문자열 조립
      경로(create_custom 인자 없이 호출)로 내려가 과제가 만들어진다.
      즉 '만들어지지 않는' 유일한 사유는 중복이고, 화면은 그 문장을 그대로 보여 준다.
    ★ 사용자가 고른 OC·레버·근거는 **제약**이다. LLM 이 다른 값을 돌려줘도 여기서
      덮어쓴다 — 화면 미리보기에 보여 준 것과 다른 과제가 저장되면 안 되고,
      레버가 바뀌면 화면 LOGIC[lever].calc 가 틀린 금액을 계산한다.
    ★ 계열사당 60초 안팎이라 **반드시 jobs.start 로 감싸 비동기로 돌린다**
      (api/proposals.create_custom 참조). 동기로 부르면 프록시 뒤에서 끊긴다.
    ★ OI_REGEN_LLM=0 이면 LLM 을 아예 시도하지 않는다 — 재생성과 같은 스위치다.
    """
    from app.pipeline.discovery.lever_map import normalize_lever

    conn = get_connection()
    try:
        canon = normalize_lever(lever, conn)
        if not canon:
            raise ValueError(f"알 수 없는 레버입니다: {lever}")
        note = _custom_note(conn, canon, ev_ids, plan, name)
    finally:
        conn.close()

    draft = None
    if OI_REGEN_LLM:
        try:
            from app.pipeline.discovery import agent
            drafts = agent.generate_tasks(oc, note, 1)
            draft = drafts[0] if drafts else None
        except Exception as e:                 # noqa: BLE001 — 폴백이 정상 경로다
            log.warning("커스텀 생성 LLM 실패 — 문자열 조립으로 폴백합니다: %s: %s",
                        type(e).__name__, e)

    if draft is None:
        # 폴백 — 예전과 완전히 같은 결과(background/risk/effect/kpi_* 는 NULL).
        return create_custom(oc, canon, ev_ids, plan, name, summary)

    def _pick(value: Optional[str], fallback: Optional[str] = None) -> Optional[str]:
        text = (value or "").strip()
        return text or fallback

    # kb_refs 는 LLM 이 실제로 프롬프트에서 본 내부 지식 id 만 남은 상태다(agent._parse).
    return create_custom(
        oc, canon, ev_ids,
        _pick(draft.plan, plan) or "",
        _pick(name, _pick(draft.title)),
        _pick(summary, _pick(draft.summary)),
        background=_pick(draft.background),
        risk=_pick(draft.risk),
        effect=_pick(draft.effect),
        kpi_name=_pick(draft.kpi.name if draft.kpi.name != "-" else ""),
        kpi_formula=_pick(draft.kpi.formula if draft.kpi.formula != "-" else ""),
        kb_refs=list(draft.kb_refs) or None,
    )


# ─────────────── 변경 (사용자 상태) ───────────────

# 별점을 매긴 순간의 과제 스냅샷. 과제가 사라진 뒤에도 '무엇을 보고 몇 점을 줬는가'가
# 남아야 하므로 조인 결과를 값으로 복사해 둔다(참조가 아니다).
_FEEDBACK_SNAPSHOT = """
    SELECT p.ver_id, p.aff_code, p.lever, p.name, p.summary, p.plan, p.origin,
           GROUP_CONCAT(pe.feed_id) AS ev,
           e.id       AS eval_id,
           e.grade    AS eval_grade,
           e.priority AS eval_priority
    FROM proposal p
    LEFT JOIN proposal_evidence pe ON pe.proposal_id = p.id
    LEFT JOIN proposal_evaluation e ON e.proposal_id = p.id AND e.is_latest = 1
    WHERE p.id = ?
    GROUP BY p.id
"""


def save_feedback(email: str, pid: int, score: Optional[int], memo: Optional[str]) -> None:
    """넘어온 항목만 갱신하고, 같은 트랜잭션에서 학습용 로그를 한 줄 쌓는다.

    별점과 피드백은 화면에서 따로 저장되므로, 읽고-쓰기로 처리하면 두 요청이
    겹칠 때 한쪽이 다른 쪽을 덮어쓴다. COALESCE 로 한 문장에서 처리한다.

    proposal_feedback 은 '지금 값'(화면 왕복용, 사용자·과제당 1행)이고
    proposal_feedback_log 는 '언제 어떤 문장을 보고 몇 점을 줬는가'(append-only)다.
    한 트랜잭션으로 묶어야 화면 값과 학습 데이터가 어긋나지 않는다.

    ★ proposal_feedback_log 에는 **일부러 FK 를 걸지 않았다.**
      proposal 은 gen_version 에 ON DELETE CASCADE 로 매달려 있어서 생성 버전 하나만
      지워도 과제·근거·현재 피드백이 통째로 사라진다. 로그에 FK 를 걸면 학습 데이터도
      같이 증발한다. 그래서 조인 결과를 그 자리에서 값으로 복사해 둔다.
      → 과제가 지워진 로그 행(고아 행)이 남는 것은 **의도한 동작**이다.
         "참조가 깨진 행 정리" 를 하지 마라. 그 순간 축적된 현업 평가가 사라진다.
    """
    at = datetime.now().isoformat(timespec="seconds")
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute(
            """INSERT INTO proposal_feedback(user_email, proposal_id, star, memo, updated_at)
               VALUES (:email, :pid, COALESCE(:star, 0), COALESCE(:memo, ''), :at)
               ON CONFLICT(user_email, proposal_id) DO UPDATE SET
                    star = COALESCE(:star, proposal_feedback.star),
                    memo  = COALESCE(:memo,  proposal_feedback.memo),
                    updated_at = :at""",
            {"email": email, "pid": pid, "star": score, "memo": memo, "at": at},
        )
        snap = conn.execute(_FEEDBACK_SNAPSHOT, (pid,)).fetchone()
        row = dict(snap) if snap else {}
        conn.execute(
            """INSERT INTO proposal_feedback_log(
                   user_email, proposal_id, star, memo, created_at,
                   ver_id, aff_code, lever, name, summary, plan, origin, evidence_ids,
                   eval_id, eval_grade, eval_priority)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (email, pid, score, memo or "", at,
             row.get("ver_id") or "", row.get("aff_code") or "",
             row.get("lever") or "", row.get("name") or "",
             row.get("summary") or "", row.get("plan") or "",
             row.get("origin") or "", row.get("ev") or "",
             row.get("eval_id"), row.get("eval_grade") or "",
             row.get("eval_priority")),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


# ─────────────── 되먹임 (발굴 프롬프트 학습 신호) ───────────────

# 프롬프트에 실을 저평가·고평가 예시 건수. 늘리면 프롬프트가 길어지고 최신 신호가 묻힌다.
FEEDBACK_EXAMPLE_LIMIT = 5

# 같은 과제를 다시 평가하면 로그에 두 줄이 쌓인다(append-only). 예시로는 **최신 1줄만**
# 쓴다 — 2점 → 5점으로 바뀐 과제가 저평가·고평가 양쪽에 동시에 실리면 모델에게 모순된
# 신호가 된다. 이력 자체는 로그에 그대로 남아 있다.
_FEEDBACK_EXAMPLE = """
    SELECT l.star, l.name, l.lever, l.memo, l.eval_grade
    FROM proposal_feedback_log l
    WHERE l.aff_code = ? AND {cond}
      AND l.id = (SELECT MAX(x.id) FROM proposal_feedback_log x
                  WHERE x.proposal_id = l.proposal_id AND x.star IS NOT NULL)
    ORDER BY l.id DESC LIMIT ?
"""


def feedback_signals(aff_code: str, conn=None) -> Dict[str, Any]:
    """계열사 1곳의 현업 별점 신호. 데이터가 없으면 **빈 dict** 를 돌려준다.

    돌려주는 것:
        levers : [{lever, n, avg, low_n, high_n}]  — v_feedback_by_lever 집계(현재 값)
        low    : 저평가(1~2점) 예시 최대 5건       — proposal_feedback_log(스냅샷)
        high   : 고평가(4점 이상) 예시 최대 5건

    집계는 뷰(현재 값)에서, 예시 문장은 **로그에서** 뽑는다.
    뷰는 proposal 을 조인하므로 과제가 CASCADE 로 지워지면 같이 사라지지만,
    로그는 과제명·요약을 값으로 복사해 두어 지워진 뒤에도 문장이 남는다.
    "어떤 과제가 낮은 점수를 받았는가" 는 지워진 과제일수록 오히려 중요한 신호다.

    빈 dict 를 돌려주는 이유: 호출부(발굴 프롬프트)가 falsy 하나로 블록을 통째로
    생략할 수 있어야 한다. 빈 블록은 모델에게 '평가가 전부 중립' 이라는 잘못된 신호다.
    """
    own = conn is None
    if own:
        conn = get_connection()
    try:
        levers = [
            {"lever": r["lever"], "n": r["n"], "avg": r["avg_star"],
             "low_n": r["low_n"], "high_n": r["high_n"]}
            for r in conn.execute(
                "SELECT lever, n, avg_star, low_n, high_n FROM v_feedback_by_lever "
                "WHERE aff_code = ? ORDER BY n DESC, lever",
                (aff_code,),
            )
        ]

        def _examples(cond: str) -> List[Dict[str, Any]]:
            return [
                # r["star"] = 사용자 별점(0~5). 바깥으로 내보내는 키가 "score" 인 것은
                # agent._fmt 가 그 이름을 읽기 때문이다 — 컬럼명(star)과 다르다는 점에 주의.
                {"score": r["star"], "name": r["name"], "lever": r["lever"],
                 "memo": r["memo"], "grade": r["eval_grade"]}
                for r in conn.execute(
                    _FEEDBACK_EXAMPLE.format(cond=cond),
                    (aff_code, FEEDBACK_EXAMPLE_LIMIT),
                )
                if (r["name"] or "").strip()
            ]

        low = _examples("l.star BETWEEN 1 AND 2")
        high = _examples("l.star >= 4")
    finally:
        if own:
            conn.close()

    if not levers and not low and not high:
        return {}
    return {"levers": levers, "low": low, "high": high}


def save_fields(email: str, pid: int, fields: Dict[str, str]) -> None:
    conn = get_connection()
    try:
        conn.execute(
            """INSERT INTO proposal_input(user_email, proposal_id, fields) VALUES (?,?,?)
               ON CONFLICT(user_email, proposal_id) DO UPDATE SET fields = excluded.fields""",
            (email, pid, json.dumps(fields, ensure_ascii=False)),
        )
        conn.commit()
    finally:
        conn.close()


def save_formula(email: str, pid: int, sys_off: bool, text: Optional[str]) -> str:
    """수정 시각(화면 표기용)을 돌려준다."""
    at = datetime.now().strftime("%Y. %m. %d %H:%M")
    conn = get_connection()
    try:
        conn.execute(
            """INSERT INTO proposal_formula(user_email, proposal_id, sys_off, text, updated_at)
               VALUES (?,?,?,?,?)
               ON CONFLICT(user_email, proposal_id)
               DO UPDATE SET sys_off = excluded.sys_off, text = excluded.text,
                             updated_at = excluded.updated_at""",
            (email, pid, 1 if sys_off else 0, text, at),
        )
        conn.commit()
    finally:
        conn.close()
    return at


# ─────────────── 변경 (관리자 · 리포팅) ───────────────

# 계정을 지울 때 함께 비우는 사용자별 테이블. 전부 user_email 컬럼을 가진다.
#
# ★ proposal_feedback_log 는 **일부러 뺐다.** 별점 이력 + 당시 과제 스냅샷(학습 데이터)이라
#   FK 도 걸지 않았고, 탈퇴해도 남아야 하는 값이다. 여기에 추가하면 축적된 학습 신호가
#   계정 하나 지울 때마다 날아간다(발굴 프롬프트의 [현업 평가 이력] 블록이 이걸 읽는다).
#   되살리고 싶다면 익명화(user_email 을 해시로)를 먼저 설계할 것.
# ★ report_recipient 는 PK 가 (user_email, label) 이라 다른 테이블과 컬럼이 다르지만
#   삭제 조건은 같다.
USER_TABLES = [
    "proposal_feedback", "proposal_input", "proposal_formula",
    "report_exclude", "report_recipient", "report_setting",
]


def purge_user(conn, email: str) -> None:
    """계정과 그 계정의 개인 데이터를 지운다. **커밋은 호출자가 한다.**

    탈퇴(DELETE /api/auth/me)와 관리자 삭제(DELETE /api/admin/users/{email})가
    반드시 같은 삭제 범위를 쓰게 하려고 여기에 둔다.

    ★ app_user 만 지우면 안 된다. app_user.email 을 참조하는 FK 가 하나도 없어서
      (사용자별 테이블은 email 을 그냥 TEXT 로 들고 있다) CASCADE 가 돌지 않고,
      별점·기준값·산출식·발송설정이 고아 행으로 남는다. 같은 이메일로 계정을 다시
      만들면 **전임자의 개인 데이터가 그대로 되살아나** 붙는다.
    ★ 호출자가 BEGIN IMMEDIATE ~ commit 으로 감쌀 것. 중간에 실패하면 계정만 지워지고
      개인 데이터가 남는 상태가 되므로, 전부 성공하거나 전부 되돌아가야 한다.
    """
    for table in USER_TABLES:
        conn.execute(f"DELETE FROM {table} WHERE user_email = ?", (email,))
    conn.execute("DELETE FROM app_user WHERE email = ?", (email,))


def add_upload(name: str, aff: str, size: str, body: Optional[str] = None,
               status: Optional[str] = None) -> Dict[str, Any]:
    """내부 자료 등록. body 가 있으면 chars/extracted_at 도 함께 채운다.

    반환 dict 는 _uploads() 와 같은 6키다 — body 는 절대 포함하지 않는다(아래 주석 참고).
    """
    now = datetime.now()
    chars = len(body) if body else 0
    extracted_at = now.isoformat(timespec="seconds") if body else None
    if status is None:
        status = "본문 추출됨" if body else "검수 대기"
    conn = get_connection()
    try:
        cur = conn.execute(
            "INSERT INTO upload_file(name, aff, size, uploaded_at, status, body, chars, extracted_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (name, aff, size, now.strftime("%Y.%m.%d %H:%M"), status, body, chars, extracted_at),
        )
        conn.commit()
        uid = cur.lastrowid
        r = conn.execute(
            "SELECT id, name, aff, size, uploaded_at, status FROM upload_file WHERE id = ?", (uid,)
        ).fetchone()
        return {"id": r["id"], "name": r["name"], "oc": r["aff"], "size": r["size"],
                "at": r["uploaded_at"], "st": r["status"]}
    finally:
        conn.close()


# ★ 업로드 승인은 '업로드 시 선택'(use_now) 이라 add_upload 가 status 를 확정한다 —
#   prefetch._upload_block 의 RAG 게이트(status='검수 완료' AND extracted_at IS NOT NULL)를
#   통과할지가 그때 정해진다. 나중에 상태를 뒤에서 고치는 화면이 생기면 여기에
#   set_upload_status 를 만들되, 본문이 없는 행을 '검수 완료' 로 올리지 않는 조건을
#   반드시 함께 넣어라.


def save_report(email: str, freq=None, time=None, channels=None,
                recipients=None, send_off=None) -> Dict[str, Any]:
    conn = get_connection()
    try:
        cur = conn.execute(
            "SELECT 1 FROM report_setting WHERE user_email = ?", (email,)
        ).fetchone()
        defaults = _loads(get_setting(conn, "report_defaults"), {})
        # 넘어온 항목만 갱신 (피드백과 같은 이유로 COALESCE)
        conn.execute(
            """INSERT INTO report_setting(user_email, freq, send_time, channels, last_at)
               VALUES (:email, COALESCE(:freq, :dfreq), COALESCE(:time, :dtime),
                       COALESCE(:ch, :dch), :last)
               ON CONFLICT(user_email) DO UPDATE SET
                    freq      = COALESCE(:freq, report_setting.freq),
                    send_time = COALESCE(:time, report_setting.send_time),
                    channels  = COALESCE(:ch,   report_setting.channels)""",
            {
                "email": email, "freq": freq, "time": time,
                "ch": json.dumps(channels, ensure_ascii=False) if channels is not None else None,
                "dfreq": defaults.get("freq", DEFAULT_REPORT["freq"]),
                "dtime": defaults.get("time", DEFAULT_REPORT["time"]),
                "dch": json.dumps(defaults.get("channels", DEFAULT_CHANNELS), ensure_ascii=False),
                "last": defaults.get("lastAt") or None,
            },
        )
        if recipients is None and cur is None:
            # 첫 저장인데 수신자를 안 넘겼으면 기본 수신자를 그대로 굳힌다.
            recipients = _loads(get_setting(conn, "report_defaults"), {}).get("recipients")
        if recipients is not None:
            conn.execute("DELETE FROM report_recipient WHERE user_email = ?", (email,))
            for label in recipients:
                conn.execute(
                    "INSERT OR IGNORE INTO report_recipient(user_email, label) VALUES (?,?)",
                    (email, label),
                )
        if send_off is not None:
            conn.execute("DELETE FROM report_exclude WHERE user_email = ?", (email,))
            for pid in send_off:
                conn.execute(
                    "INSERT OR IGNORE INTO report_exclude(user_email, proposal_id) VALUES (?,?)",
                    (email, pid),
                )
        conn.commit()
        return _user_state(conn, email)
    finally:
        conn.close()


def mark_report_sent(email: str) -> str:
    """발송 시각을 기록한다.

    ★ report_setting 행을 처음 만들 때는 기본 수신자도 함께 굳힌다.
      _user_state 는 "report_setting 행이 있으면 저장된 설정이 있다" 로 보고
      기본값 폴백을 타지 않는다. 그래서 이 행만 만들고 report_recipient 를 비워 두면
      '테스트 발송' 버튼 한 번에 화면의 수신자 칩이 2개 → 0개로 조용히 사라진다(실측).
      save_report 의 첫 저장 처리와 같은 규칙이다.
    """
    at = datetime.now().strftime("%Y.%m.%d %H:%M")
    conn = get_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")
        # ON CONFLICT 만으로는 신규/기존을 구분할 수 없어 먼저 읽는다.
        is_new = conn.execute(
            "SELECT 1 FROM report_setting WHERE user_email = ?", (email,)
        ).fetchone() is None
        conn.execute(
            """INSERT INTO report_setting(user_email, freq, send_time, channels, last_at)
               VALUES (?,?,?,?,?)
               ON CONFLICT(user_email) DO UPDATE SET last_at = excluded.last_at""",
            (email, DEFAULT_REPORT["freq"], DEFAULT_REPORT["time"],
             json.dumps(DEFAULT_CHANNELS, ensure_ascii=False), at),
        )
        if is_new:
            for label in _loads(get_setting(conn, "report_defaults"), {}).get("recipients", []):
                conn.execute(
                    "INSERT OR IGNORE INTO report_recipient(user_email, label) VALUES (?,?)",
                    (email, label),
                )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    return at
