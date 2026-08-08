"""과제 발굴 프롬프트 조립 — 파일 KB + DB 3종을 하나의 토큰 예산 안에 넣는다.

왜 prefetch(미리 골라 싣기)인가
--------------------------------
codex 는 단발 호출이라 툴 루프를 돌 수 없다. 즉 에이전트가 "이 문서를 열어 달라"고
되물을 수 없으므로, 서버가 **미리 정답 문서를 골라** 프롬프트에 실어 보내야 한다.
계층1 INDEX 전체(64,252토큰)를 매 호출 싣는 방식은 쓰지 않는다 —
문서 742건짜리 목차는 툴 루프가 있을 때만 의미가 있고, 여기서는 예산의 10배다.
계층 0 core(1,577토큰)도 뺀다. 용어 정의는 read_doc 본문에 문맥으로 이미 들어온다.

블록 순서는 고정이다 (바꾸지 말 것)
------------------------------------
    1 역할·판단 규칙(SYSTEM)   2 레버 체계        3 대상 계열사 프로필
    4 내부 지식 — 검색 결과    5 내부 지식 — 본문  6 내부 자료 — 업로드 발췌
    7 검증된 혁신 사례         8 외부 동향        9 내부 현황 메모

**내부 지식(4~6)을 외부 동향(8) 앞에 둔 것은 의도적이다.** 조사에서 확인된 핵심 결함이
"내부 지식이 프롬프트에 0바이트 기여" 였고, 뒤에 붙이면 뉴스 8줄이 앵커가 되어
계열사 공정과 무관한 일반론이 나온다. 가장 구체적인 지시인 사용자 메모는 맨 뒤에 둔다.

내부 지식이 없는 계열사
------------------------
`affiliate.kb_company` 가 NULL 이면 4·5번 블록을 통째로 생략한다. NULL 을 그대로
retriever.load 에 넘기면 FileNotFoundError 가 나고, 현재 backend/knowledge/ 아래
디렉터리가 있는 회사는 일부뿐이라 나머지 계열사의 발굴이 전부 500 이 된다.
KB 디렉터리가 지워졌을 때를 대비해 FileNotFoundError 도 여기서 잡아 degrade 한다.
"""
from __future__ import annotations

import sqlite3
from typing import Dict, List, Optional, Tuple

from app.config import (
    OI_RAG_CASE_TOKENS,
    OI_RAG_FEED_TOKENS,
    OI_RAG_KB_BODY_TOKENS,
    OI_RAG_KB_DOC_CHARS,
    OI_RAG_KB_LIST_TOKENS,
    OI_RAG_KB_OPEN_DOCS,
    OI_RAG_LEVER_TOKENS,
    OI_RAG_NOTE_TOKENS,
    OI_RAG_PROFILE_TOKENS,
    OI_RAG_ROLE_TOKENS,
    OI_RAG_TOTAL_TOKENS,
    OI_RAG_UPLOAD_TOKENS,
    TODAY,
)
from app.db.database import get_connection
from app.pipeline.knowledge import retriever
from tools.kb_build.common import est_tokens

# 외부 동향 조회 창(일)과 최대 건수 — discovery 가 쓰던 값과 같다.
FEED_DAYS = 30
FEED_LIMIT = 8
CASE_LIMIT = 6
UPLOAD_LIMIT = 3
KB_TOP_K = 2          # 레버당 상위 몇 건을 목록에 올릴지

# ── 1. 역할·판단 규칙 (SYSTEM) ────────────────────────────────────────────
ROLE = """너는 SK이노베이션 O/I추진단의 과제 발굴 애널리스트다.
아래 근거만을 사용해 {aff_name}에 적용 가능한 O/I(Operation Improvement) 과제 2건을 제안한다.

판단 규칙:
- 확장 투자형보다 비용·효율·수익성 개선 과제를 우선한다.
- [내부 지식]과 [내부 자료]는 대상 계열사의 실제 공정·원가 구조다. 여기에 닿지 않는
  일반론은 제안하지 마라. 외부 동향은 "무엇을 벤치마크할 것인가"에만 쓴다.
- lever 는 반드시 [레버 체계]에 있는 이름 중 하나를 그대로 쓴다. 새 이름을 만들지 마라.
- evidence 는 (ev:...) id 에서만, kb_refs 는 (kb:...) 와 (up:...) id 에서만 고른다.
  근거가 없으면 빈 배열로 두고, 없는 id 를 지어내지 마라.
- 문장은 짧고 구체적으로. 숫자가 근거에 있으면 인용하고, 없으면 지어내지 마라."""


# ── 토큰 예산 유틸 ────────────────────────────────────────────────────────

def _fit_lines(head: str, lines: List[str], budget: int) -> Tuple[str, List[int]]:
    """머리글 + 목록을 예산 안에 담는다. 넘치면 **뒤에서부터** 버린다.

    앞쪽이 점수가 높은 항목이므로 뒤를 버리는 것이 맞다.
    반환값의 두 번째는 실제로 살아남은 줄의 인덱스 목록(화이트리스트 산출용).
    """
    kept: List[int] = []
    out: List[str] = [head]
    used = est_tokens(head)
    for i, line in enumerate(lines):
        cost = est_tokens(line) + 1
        if used + cost > budget:
            break
        out.append(line)
        used += cost
        kept.append(i)
    return "\n".join(out), kept


_ELLIPSIS = " …"


def _fit_text(text: str, budget: int) -> str:
    """자유 텍스트를 예산 안에 담는다. 넘치면 뒤를 잘라낸다.

    잘렸다는 표시(' …')도 토큰을 쓰므로 그만큼 미리 빼고 자른다.
    이걸 빼먹으면 결과가 상한을 1~2 토큰 넘긴다(실측).
    """
    if est_tokens(text) <= budget:
        return text
    room = max(0, budget - est_tokens(_ELLIPSIS))
    # est_tokens 는 한글 1.15 / 그 외 1/3.6 이라 글자수 상한을 이분탐색으로 찾는다.
    lo, hi = 0, len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if est_tokens(text[:mid]) <= room:
            lo = mid
        else:
            hi = mid - 1
    # est_tokens 가 int() 내림이라 rstrip·말줄임을 붙이는 과정에서 1 토큰이 되살아날 수
    # 있다. 상한은 '넘지 않는다' 가 계약이므로 실제 값으로 다시 재서 맞춘다.
    out = text[:lo].rstrip() + _ELLIPSIS
    while lo > 0 and est_tokens(out) > budget:
        lo -= 8
        out = text[:max(0, lo)].rstrip() + _ELLIPSIS
    return out


# ── 2. 레버 체계 ──────────────────────────────────────────────────────────

def _lever_rows(conn) -> List[sqlite3.Row]:
    return conn.execute(
        "SELECT name, metric, formula, kb_query FROM lever ORDER BY sort_order"
    ).fetchall()


def _lever_block(rows) -> str:
    lines = [f"- {r['name']} | 관리지표: {r['metric']} | 산출식: {r['formula']}" for r in rows]
    head = f"[레버 체계] (lever 는 이 {len(rows)}개 중 하나여야 한다)"
    text, _ = _fit_lines(head, lines, OI_RAG_LEVER_TOKENS)
    return text


# ── 3. 대상 계열사 프로필 ─────────────────────────────────────────────────

def _profile_block(conn, aff_code: str) -> Tuple[str, str, Optional[str]]:
    """(블록 텍스트, 계열사명, kb_company) 를 돌려준다."""
    row = conn.execute(
        "SELECT a.code, a.name, a.kb_company, b.label AS biz_label "
        "FROM affiliate a LEFT JOIN biz_segment b ON b.key = a.biz WHERE a.code = ?",
        (aff_code,),
    ).fetchone()
    if not row:
        return f"[대상 계열사]\n{aff_code}", aff_code, None

    aff_name = row["name"]
    lines = [f"{row['code']} {aff_name} (사업부문 {row['biz_label'] or '-'})"]
    for b in conn.execute(
        "SELECT summary FROM kb_business WHERE aff_code = ? ORDER BY id", (aff_code,)
    ):
        if b["summary"]:
            lines.append(b["summary"].strip())
    text = _fit_text("[대상 계열사]\n" + "\n".join(lines), OI_RAG_PROFILE_TOKENS)
    return text, aff_name, row["kb_company"]


# ── 4·5. 내부 지식 (파일 KB) ──────────────────────────────────────────────

def _kb_blocks(kb_company: Optional[str], lever_rows,
               levers: Optional[List[str]]) -> Tuple[str, str, List[str]]:
    """(목록 블록, 본문 블록, kb_ids) — KB 가 없으면 ('', '', []) 로 degrade.

    넓게 보되(레버당 top2 요약) 깊게는 2건만 연다. 실측 점수 분포에서 1위와 10위
    격차가 27% 밖에 안 돼 top_k 를 늘리면 노이즈가 빠르게 섞이기 때문이다.
    """
    if not kb_company:
        return "", "", []
    try:
        retriever.load(kb_company)
    except FileNotFoundError:
        # KB 디렉터리가 지워졌거나 아직 빌드 전 — 발굴을 막지 않고 블록만 생략한다.
        return "", "", []
    except Exception:
        return "", "", []

    want = set(levers) if levers else None
    seen: Dict[str, Dict] = {}
    order: List[str] = []
    for r in lever_rows:
        if want and r["name"] not in want:
            continue
        query = r["kb_query"] or r["name"]
        try:
            hits = retriever.search_docs(query, top_k=KB_TOP_K, company=kb_company)
        except Exception:
            continue
        for h in hits:
            # 한 문서가 여러 레버에 걸릴 수 있다. 먼저 잡은 레버로 라벨을 고정하면
            # 물류 문서에 [정비/TA] 가 붙는 식으로 잘못 표기돼 모델이 오해한다.
            # 문서는 한 번만 싣되 라벨은 걸린 레버를 모두 모은다.
            if h["id"] in seen:
                if r["name"] not in seen[h["id"]]["levers"]:
                    seen[h["id"]]["levers"].append(r["name"])
                continue
            seen[h["id"]] = dict(h, levers=[r["name"]])
            order.append(h["id"])

    if not order:
        return "", "", []

    lines = [
        f"- (kb:{seen[i]['id']}) [{'·'.join(seen[i]['levers'])}] {seen[i]['title']} — "
        f"{' '.join((seen[i]['summary'] or '').split())}"
        for i in order
    ]
    list_block, kept = _fit_lines(
        "[내부 지식 — 검색 결과]", lines, OI_RAG_KB_LIST_TOKENS
    )
    kb_ids = [order[i] for i in kept]

    # 본문은 목록에 살아남은 상위 문서만 연다.
    parts: List[str] = []
    for doc_id in kb_ids[:OI_RAG_KB_OPEN_DOCS]:
        try:
            body = retriever.read_doc(doc_id, company=kb_company)
        except Exception:
            continue
        parts.append(f"[kb:{doc_id}]\n{body[:OI_RAG_KB_DOC_CHARS]}")
    body_block = ""
    if parts:
        body_block = _fit_text(
            "[내부 지식 — 본문 발췌]\n" + "\n\n".join(parts), OI_RAG_KB_BODY_TOKENS
        )
    return list_block, body_block, kb_ids


# ── 6. 내부 자료 (업로드 문서) ────────────────────────────────────────────

def _upload_block(conn, aff_code: str, aff_name: str) -> Tuple[str, List[str]]:
    """검수를 통과하고 본문 추출까지 끝난 업로드 자료만 발췌해 넣는다.

    게이트가 `status='검수 완료' AND extracted_at IS NOT NULL` 인 이유:
    - status 만 보면 본문이 없는 기존 시드 3행이 빈 블록을 만든다.
    - extracted_at 만 보면 **검토되지 않은 내부 문서가 자동으로 프롬프트에 흘러든다.**
    두 조건을 동시에 요구해야 '사람이 승인한 문서만' 이 성립한다.
    """
    rows = conn.execute(
        "SELECT id, name, aff, body, chars FROM upload_file "
        "WHERE status = '검수 완료' AND extracted_at IS NOT NULL "
        "  AND body IS NOT NULL AND body <> '' "
        "  AND (aff IS NULL OR aff = '' OR aff = '전사' OR aff = ? OR aff = ?) "
        "ORDER BY id DESC LIMIT ?",
        (aff_code, aff_name, UPLOAD_LIMIT),
    ).fetchall()
    if not rows:
        return "", []

    # 발췌는 farming.llm.select_excerpt 재사용 — O/I 신호(원가·가동률·정기보수 …)
    # 주변만 골라낸다. 정기보고서는 앞부분이 표지·목차라 단순 절삭하면 알맹이를 버린다.
    from app.pipeline.farming.llm import select_excerpt

    per = max(400, (OI_RAG_UPLOAD_TOKENS * 3) // max(len(rows), 1))  # 대략적 글자 예산
    parts, up_ids = [], []
    for r in rows:
        excerpt = " ".join(select_excerpt(r["body"], per).split())
        if not excerpt:
            continue
        up_ids.append(str(r["id"]))
        parts.append(f"- (up:{r['id']}) {r['name']} ({r['aff'] or '전사'})\n{excerpt}")
    if not parts:
        return "", []
    block = _fit_text(
        "[내부 자료 — 업로드 문서 발췌]\n" + "\n".join(parts), OI_RAG_UPLOAD_TOKENS
    )
    # up_ids 는 "프롬프트에 실제로 실린 문서" 계약이다. _fit_text 가 뒤쪽을 잘라내므로
    # 잘린 문서는 화이트리스트에서도 빠져야 한다 — 안 그러면 모델이 인용하지도 않은
    # 문서 id 를 근거로 반환해도 검증을 통과한다.
    up_ids = [i for i in up_ids if f"(up:{i})" in block]
    return block, up_ids


# ── 7. 검증된 혁신 사례 ───────────────────────────────────────────────────

def _case_block(conn, aff_code: str) -> Tuple[str, List[str]]:
    rows = conn.execute(
        """SELECT c.id, c.title, c.category, c.background, c.effect,
                  c.kpi_name, c.kpi_formula, c.source_org,
                  EXISTS(SELECT 1 FROM kb_case_affiliate ca
                         WHERE ca.case_id = c.id AND ca.aff_code = ?) AS mine
           FROM kb_innovation_case c
           WHERE c.status = 'approved'
           ORDER BY mine DESC, c.created_at DESC, c.id DESC
           LIMIT ?""",
        (aff_code, CASE_LIMIT),
    ).fetchall()
    if not rows:
        return "", []
    lines, ids = [], []
    for r in rows:
        ids.append(str(r["id"]))
        org = f" ({r['source_org']})" if r["source_org"] else ""
        bg = " ".join((r["background"] or "").split())
        eff = " ".join((r["effect"] or "").split())
        kpi = r["kpi_name"] or ""
        if kpi and r["kpi_formula"]:
            kpi = f"{kpi}={r['kpi_formula']}"
        lines.append(
            f"- (case:{r['id']}) [{r['category'] or '-'}] {r['title']}{org} — {bg}"
            + (f" 효과: {eff}" if eff else "")
            + (f" KPI: {kpi}" if kpi else "")
        )
    text, kept = _fit_lines("[검증된 혁신 사례]", lines, OI_RAG_CASE_TOKENS)
    return text, [ids[i] for i in kept]


# ── 8. 외부 동향 ──────────────────────────────────────────────────────────

def _flatten(text: str) -> str:
    """여러 줄 요약을 한 줄로 — 마크다운 불릿 한 항목이 여러 줄로 쪼개지지 않게.

    discovery/agent.py 의 _flatten 과 같은 규칙이다(DB 는 원본 3줄 그대로 보관).
    """
    return " / ".join(
        ln.lstrip("- ").strip() for ln in (text or "").splitlines() if ln.strip()
    )


def _feed_block(conn, aff_code: str, aff_name: str) -> Tuple[str, List[str]]:
    rows = conn.execute(
        """SELECT f.id, f.published_on, f.source, f.source_label, f.title,
                  f.title_label, f.summary
           FROM feed_item f
           WHERE f.id IN (SELECT feed_id FROM feed_item_tag WHERE aff_code = ?)
           ORDER BY f.published_on DESC""",
        (aff_code,),
    ).fetchall()
    if not rows:
        return "", []

    def _recent(days: int):
        from datetime import date
        anchor = date.fromisoformat(TODAY)
        out = []
        for r in rows:
            try:
                gap = (anchor - date.fromisoformat(r["published_on"])).days
            except (TypeError, ValueError):
                continue
            if gap <= days:
                out.append(r)
        return out[:FEED_LIMIT]

    picked = _recent(FEED_DAYS)
    head = f"[외부 동향] (최근 {FEED_DAYS}일, {aff_name} 관련)"
    if not picked:
        # 창 안에 자료가 하나도 없으면 빈 블록 대신 최신 자료로 되돌린다.
        # 근거 0건이면 발굴 결과가 통째로 버려지므로, 오래됐다는 사실만 머리글에 밝힌다.
        picked = rows[:FEED_LIMIT]
        head = f"[외부 동향] ({aff_name} 관련 — 최근 {FEED_DAYS}일 내 자료 없음, 최신순)"

    lines, ids = [], []
    for r in picked:
        ids.append(r["id"])
        org = r["source_label"] or r["source"]
        title = r["title_label"] or r["title"]
        lines.append(
            f"- (ev:{r['id']}) [{r['published_on']} · {org}] {title} — {_flatten(r['summary'])}"
        )
    text, kept = _fit_lines(head, lines, OI_RAG_FEED_TOKENS)
    return text, [ids[i] for i in kept]


# ── 9. 사용자 메모 ────────────────────────────────────────────────────────

def _note_block(note: str) -> str:
    body = (note or "").strip()
    if not body:
        return "[내부 현황 메모]\n(제공되지 않음 — 위 근거만으로 제안)"
    return _fit_text("[내부 현황 메모]\n" + body, OI_RAG_NOTE_TOKENS)


# ── 공개 API ──────────────────────────────────────────────────────────────

def build_context(aff_code: str, note: str = "",
                  levers: Optional[List[str]] = None) -> Tuple[str, Dict]:
    """발굴 프롬프트 전문과 메타를 만든다.

    반환값
        text : 블록 1~9 를 순서대로 이어 붙인 전문. 합계 OI_RAG_TOTAL_TOKENS 이하.
        meta : {
            'system'   : 블록 1(역할). LLM 의 system 자리에 넣을 때 쓴다.
            'user'     : 블록 2~9. system 을 분리해 넣을 때 text 대신 이걸 쓴다.
            'kb_ids'   : 프롬프트에 실제로 실린 내부 지식 문서 id
            'up_ids'   : 실린 업로드 자료 id (문자열)
            'case_ids' : 실린 혁신 사례 id (문자열)
            'ev_ids'   : 실린 외부 동향 feed_item.id
            'tokens'   : 블록별 근사 토큰 수 + 'total'
            'kb_company' : 쓰인 KB 디렉터리명 (없으면 None)
        }

    meta 의 id 목록은 **화이트리스트**다. LLM 이 돌려준 evidence/kb_refs 를 이 집합과
    교집합 처리해야 없는 id 를 지어낸 응답을 걸러낼 수 있다.

    아무 계열사 코드로 불러도 예외를 던지지 않는다. 내부 지식이 없으면 그 블록만
    빠지고 나머지 근거로 컨텍스트가 만들어진다.
    """
    conn = get_connection()
    try:
        lever_rows = _lever_rows(conn)
        profile, aff_name, kb_company = _profile_block(conn, aff_code)
        lever_text = _lever_block(lever_rows)
        kb_list, kb_body, kb_ids = _kb_blocks(kb_company, lever_rows, levers)
        upload, up_ids = _upload_block(conn, aff_code, aff_name)
        cases, case_ids = _case_block(conn, aff_code)
        feed, ev_ids = _feed_block(conn, aff_code, aff_name)
    finally:
        conn.close()

    role = _fit_text(ROLE.format(aff_name=aff_name), OI_RAG_ROLE_TOKENS)
    note_text = _note_block(note)

    # ★ 순서 고정. 내부 지식(kb_list/kb_body/upload)이 외부 동향(feed) 앞이다.
    blocks = [
        ("role", role),
        ("lever", lever_text),
        ("profile", profile),
        ("kb_list", kb_list),
        ("kb_body", kb_body),
        ("upload", upload),
        ("case", cases),
        ("feed", feed),
        ("note", note_text),
    ]
    tokens = {k: est_tokens(v) for k, v in blocks if v}

    user = "\n\n".join(v for k, v in blocks if v and k != "role")
    text = role + "\n\n" + user

    # 블록별 상한의 합이 총상한과 같아 여기서 걸리는 일은 드물지만, 상한을 넘긴 채로
    # 나가면 codex 가 조용히 앞부분만 읽는다. 마지막 안전망으로 한 번 더 자른다.
    if est_tokens(text) > OI_RAG_TOTAL_TOKENS:
        text = _fit_text(text, OI_RAG_TOTAL_TOKENS)
        user = _fit_text(user, OI_RAG_TOTAL_TOKENS - est_tokens(role))
        # 총상한에서 잘린 항목도 화이트리스트에서 빼야 계약이 유지된다.
        kb_ids = [i for i in kb_ids if f"(kb:{i})" in text]
        up_ids = [i for i in up_ids if f"(up:{i})" in text]
        case_ids = [i for i in case_ids if f"(case:{i})" in text]
        ev_ids = [i for i in ev_ids if f"(ev:{i})" in text]
    tokens["total"] = est_tokens(text)

    meta = {
        "system": role,
        "user": user,
        "kb_ids": kb_ids,
        "up_ids": up_ids,
        "case_ids": case_ids,
        "ev_ids": ev_ids,
        "tokens": tokens,
        "kb_company": kb_company,
    }
    return text, meta
