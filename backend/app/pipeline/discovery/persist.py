"""발굴 LLM 산출물 → proposal 저장.

지금까지 LLM 이 만든 과제는 HTTP 응답으로 한 번 보이고 버려졌다. 이 모듈이 그 연결이다.

버리는(skip) 기준 — 조용히 틀린 것보다 1건을 버리는 쪽이 낫다
--------------------------------------------------------------
  1. 과제명이 없다
  2. 레버 정규화 실패(normalize_lever → None)
     `proposal.lever` 는 lever(name) FK 라 애초에 INSERT 가 실패하고, 억지로 다른 레버를
     붙이면 화면의 LOGIC[lever].calc 가 **틀린 금액**을 계산해 보여 준다.
  3. 같은 계열사에 같은 name_key 가 이미 있다(중복)
  4. 근거(evidence)가 feed_item 실재 id 와 교집합해서 0건
     proposal_evidence.feed_id 는 feed_item FK 라 없는 id 는 IntegrityError 이고,
     화면 벤치마크 카드와 검색 haystack 이 EV[id] 를 무조건 참조한다.

호출자는 반환된 id 목록의 길이로 성패를 판정한다. 예외는 던지지 않는다(0건 = 실패).

proposal.kb_refs 의 값 형태
---------------------------
prefetch 가 프롬프트에 실은 내부 근거 두 종류가 섞여 들어온다. 구분은 형태로 한다.
    'skon-d06-…'(슬러그)  → 파일 KB 문서 id      : retriever.read_doc(id, company=…)
    '5'(숫자 문자열)      → upload_file.id       : SELECT … FROM upload_file WHERE id=?
둘 다 build_context 의 화이트리스트(kb_ids ∪ up_ids)를 통과한 값이라 실재가 보장된다.
"""
import os
from difflib import SequenceMatcher
from typing import List, Optional, Sequence

from app import store
from app.models import TaskDraft
from app.pipeline.discovery.lever_map import normalize_lever


def _existing_feed_ids(conn, ids: Sequence[str]) -> set:
    """feed_item 에 실재하는 id 만 남긴다(환각 근거 차단의 마지막 관문)."""
    ids = [str(i) for i in ids if i]
    if not ids:
        return set()
    marks = ",".join("?" * len(ids))
    return {
        r["id"]
        for r in conn.execute(
            f"SELECT id FROM feed_item WHERE id IN ({marks})", ids
        )
    }


# ─────────────── 중복 판정 ───────────────
# 과제명 완전일치만 막으면 재생성마다 '표현만 바꾼 같은 과제' 가 무한히 쌓인다
# (실측: 2회 재생성으로 같은 계열사·레버·근거 조합이 4건까지 늘었다).
# 이름 유사도만으로 판정하려 했으나 실 데이터에서 경계가 겹쳤다 —
#   서로 다른 과제 최대 0.43 / 실제 변형 0.50~0.89  (한국어는 글자 단위 비교가 흔들린다)
# 그래서 **더 정확한 신호를 먼저 쓴다**: 같은 계열사·같은 레버·같은 근거 집합이면
# 표현과 무관하게 같은 아이디어다. 이름 유사도는 근거가 조금 다를 때만 보조로 쓰고,
# 레버까지 같은 경우로 한정해 오탐을 줄인다.
SIMILARITY_LIMIT = float(os.getenv("OI_DUP_SIMILARITY", "0.55"))


def _is_duplicate(conn, aff_code: str, lever: str, key: str,
                  ev_ids: Sequence[str], batch: Sequence[tuple]) -> bool:
    """이미 있는(또는 이번 배치의) 과제와 사실상 같은가."""
    ev_set = frozenset(ev_ids)
    rows = [
        (r["lever"], r["name_key"],
         frozenset((r["ev"] or "").split(",")) - {""})
        for r in conn.execute(
            """SELECT p.lever, p.name_key,
                      (SELECT GROUP_CONCAT(feed_id) FROM proposal_evidence e
                        WHERE e.proposal_id = p.id) AS ev
               FROM proposal p
               WHERE p.aff_code = ? AND p.name_key IS NOT NULL""",
            (aff_code,),
        )
    ]
    for other_lever, other_key, other_ev in list(batch) + rows:
        if not other_key:
            continue
        if other_lever == lever:
            # 같은 레버 + 같은 근거 = 표현이 달라도 같은 아이디어
            if ev_set and ev_set == other_ev:
                return True
            if SequenceMatcher(None, key, other_key).ratio() >= SIMILARITY_LIMIT:
                return True
    return False


def save_drafts(conn, ver_id: str, aff_code: str, drafts: List[TaskDraft],
                origin: str = "AI생성",
                status: str = "검토중") -> List[int]:
    """과제 초안 목록을 proposal 로 저장하고 새 id 목록을 돌려준다.

    ★ commit 하지 않는다. 호출자가 gen_version INSERT 와 같은 트랜잭션으로 묶는다 —
      과제가 하나도 저장되지 않았을 때 빈 생성 버전만 남는 것을 막기 위해서다.
    """
    saved: List[int] = []
    seen_keys: set = set()          # 같은 배치 안의 중복도 막는다
    batch_seen: List[tuple] = []    # (레버, 과제명키, 근거집합) — 배치 내 유사 중복 판정용
    for d in drafts:
        name = (d.title or "").strip()
        if not name:
            continue

        # (2) 레버 — TaskDraft.lever 가 이미 정규화돼 있지만, 외부에서 만든 초안이
        #     들어올 수 있으므로 여기서 한 번 더 확인한다(저장 직전 단일 관문).
        lever = normalize_lever(d.lever or d.category, conn)
        if not lever:
            continue

        # (3) 중복 — 같은 계열사에 같은 정규화 과제명, 그리고 '표현만 바꾼 같은 과제'.
        #     판정 규칙과 그 근거는 상단 '중복 판정' 블록 참조.
        key = store.name_key(name)
        if key in seen_keys or store.name_key_exists(conn, aff_code, key):
            continue

        # (4) 근거 — 실재하는 feed_item id 만
        wanted = [str(e) for e in d.evidence if e]
        real = _existing_feed_ids(conn, wanted)
        ev_ids = [e for e in wanted if e in real]
        if not ev_ids:
            continue

        # (5) 사실상 같은 과제인지 — 근거가 확정된 뒤에 판정한다
        if _is_duplicate(conn, aff_code, lever, key, ev_ids, batch_seen):
            continue
        batch_seen.append((lever, key, frozenset(ev_ids)))

        summary = (d.summary or "").strip() or (d.effect or "").strip()
        pid = store._insert_proposal(
            conn, ver_id, aff_code, lever, name, summary, (d.plan or "").strip(),
            ev_ids, origin,
            background=(d.background or "").strip() or None,
            risk=(d.risk or "").strip() or None,
            effect=(d.effect or "").strip() or None,
            kpi_name=_clean_kpi(d.kpi.name),
            kpi_formula=_clean_kpi(d.kpi.formula),
            kb_refs=list(d.kb_refs) or None,
            status=status,
        )
        saved.append(pid)
        seen_keys.add(key)
    return saved


def _clean_kpi(value: Optional[str]) -> Optional[str]:
    """'-' 는 Kpi 의 기본값(=모델이 안 준 것)이므로 NULL 로 둔다.

    NULL 이어야 store._proposals() 가 읽기 시점에 lever.metric / lever.formula 로 폴백하고,
    나중에 이 KPI 가 LLM 산인지 레버 기본값인지도 구분된다.
    """
    text = (value or "").strip()
    return text if text and text != "-" else None


# 저장 결과를 알리는 문장은 호출자가 각자 만든다 — store.regenerate 는
# gen_version.trigger 를 "AI 생성 · SK온 2건 · …" 로 UPDATE 하고, 커스텀 생성은
# 과제 1건이라 요약할 것이 없다.
