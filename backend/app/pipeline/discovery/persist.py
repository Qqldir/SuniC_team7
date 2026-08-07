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
import logging
import os
from difflib import SequenceMatcher
from typing import List, Optional, Sequence

from app import store
from app.models import TaskDraft
from app.pipeline.discovery.lever_map import normalize_lever

log = logging.getLogger(__name__)


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
# 그래서 신호를 둘로 나눈다: **근거를 2건 이상 똑같이 쓰는 같은 레버 과제**는 표현과
# 무관하게 같은 아이디어로 보고, 그 밖에는 이름 유사도로 본다.
#
# ★ '근거집합 일치' 에 len(ev) >= 2 조건이 붙은 이유 (실측으로 되돌린 규칙이다)
#   예전에는 근거 1건만 같아도 즉시 중복으로 판정했다. 그런데 현 코퍼스의 과제 75건 중
#   68건이 근거 1건짜리다(화면 커스텀 생성이 근거를 1건만 보낸다 — trendroom.html).
#   그래서 이 규칙이 사실상 '같은 계열사 + 같은 레버 + 같은 벤치마크 1건' 으로 퇴화했고,
#   같은 (계열사,레버) 60쌍 중 **37쌍**이 중복으로 걸렸다. 그 37쌍은 전부 근거 1건짜리이며
#   이름 유사도가 0.06~0.36 인 **명백히 다른 과제**들이다:
#       0.074  '셀 완제품 수출 물류 적재율 개선' ↔ '원재료 해상운송 계약 조건 재협상'
#       0.071  '양극재 부자재 통합 구매 전환'   ↔ '핵심설비 MRO 교체부품 규격 표준화'
#   같은 벤치마크 1건에서 서로 다른 과제가 나오는 것은 정상이다. 근거가 2건 이상 겹치면
#   그때는 우연이 아니다(현 코퍼스에 2건 이상 일치 쌍은 0쌍 — 즉 이 완화로 실제 중복이
#   풀린 사례는 없다. 반복 생성된 SKO 수율 과제군은 이름 유사도 0.96 으로 그대로 걸린다).
#
# 임계값 0.70 의 근거 — 같은 (계열사, 레버)인 60쌍 전수 측정:
#   실제 중복(반복 생성된 SKO 수율 과제군) 0.96
#   유일한 오탐 0.645 — '육상운송 계약 재협상' ↔ '해상운송 계약 재협상' (다른 과제다)
#   나머지 최고 0.36
# 0.36~0.645 사이가 비어 있고 예전 기본값 0.55 는 오탐 쪽(0.645)에 붙어 있었다.
# 0.70 은 양쪽으로 0.15 여유를 준다. 표본이 60쌍뿐이니 코퍼스가 커지면 다시 재라.
# ★ 0.55 → 0.70 이 실제로 판정을 바꾸는 쌍은 위 0.645 오탐 1쌍뿐이다. 그 1쌍은 근거가
#   1건(둘 다 {e6})이라 예전 규칙에서는 이름을 보기 전에 '근거집합 일치' 로 먼저 걸렸다 —
#   즉 임계값만 올렸을 때는 실효가 0 이었고, 위 len>=2 조건과 **함께** 있어야 살아난다.
SIMILARITY_LIMIT = float(os.getenv("OI_DUP_SIMILARITY", "0.70"))

# 근거집합 일치를 '같은 아이디어' 로 인정하는 최소 근거 수. 위 주석 참조.
EV_MATCH_MIN = 2


def find_duplicate(conn, aff_code: str, lever: str, key: str,
                   ev_ids: Sequence[str], batch: Sequence[tuple] = ()) -> Optional[dict]:
    """사실상 같은 과제가 이미 있으면 {id, name, why}, 없으면 None.

    ★ bool 이 아니라 행을 돌려주는 이유: 커스텀 생성 거부 화면이 '무엇과 중복인지'
      (#id · 과제명)를 보여 줘야 한다. 이번 배치 안의 중복(batch)은 아직 id 가 없어
      id·name 이 None 이다 — 그 경로는 save_drafts 가 조용히 버리므로 화면에 안 나온다.

    ★ 첫 매치에서 바로 돌려주지 않는다. 그러면 '무엇과 중복인지' 가 **가장 비슷한 과제가
      아니라 그냥 먼저 읽힌 행**이 된다. 예전에는 ORDER BY 도 없어서 SQLite 가
      idx_proposal_namekey 를 타 name_key 사전순으로 행을 줬고, 라틴 문자로 시작하는
      과제가 하나 생기자 실제 근접 중복이 #1243 인데도 거부 문구가 엉뚱한 #1413 을
      가리켰다(사용자가 '기존 과제 보기' 를 누르면 관련 없는 과제가 열린다).
      그래서 매치를 **전부 모은 뒤** 이름 유사도 최대값, 동률이면 가장 먼저 만들어진
      행(id 오름차순)을 고른다. 근거집합 일치는 이름 유사도보다 강한 신호라 우선한다.
    """
    ev_set = frozenset(ev_ids)
    rows = [
        (r["lever"], r["name_key"],
         frozenset((r["ev"] or "").split(",")) - {""},
         r["id"], r["name"])
        for r in conn.execute(
            # ORDER BY 가 없으면 반환 순서가 인덱스 선택에 좌우된다(결정론 확보용).
            """SELECT p.id, p.name, p.lever, p.name_key,
                      (SELECT GROUP_CONCAT(feed_id) FROM proposal_evidence e
                        WHERE e.proposal_id = p.id) AS ev
               FROM proposal p
               WHERE p.aff_code = ? AND p.name_key IS NOT NULL
               ORDER BY p.id""",
            (aff_code,),
        )
    ]
    batch_rows = [(b[0], b[1], b[2], None, None) for b in batch]

    ev_hits: List[tuple] = []    # (유사도, id, {id,name,why})
    name_hits: List[tuple] = []
    for other_lever, other_key, other_ev, other_id, other_name in batch_rows + rows:
        if not other_key or other_lever != lever:
            continue
        ratio = SequenceMatcher(None, key, other_key).ratio()
        if len(ev_set) >= EV_MATCH_MIN and ev_set == other_ev:
            ev_hits.append((ratio, other_id or 0,
                            {"id": other_id, "name": other_name,
                             "why": f"근거 {len(ev_set)}건 전부 일치"}))
        elif ratio >= SIMILARITY_LIMIT:
            name_hits.append((ratio, other_id or 0,
                              {"id": other_id, "name": other_name,
                               "why": f"이름 유사도 {ratio:.2f}"}))
    hits = ev_hits or name_hits
    if not hits:
        return None
    # 유사도 최대 → 동률이면 가장 먼저 만들어진 원본(id 최소)
    return min(hits, key=lambda h: (-h[0], h[1]))[2]


def _is_duplicate(conn, aff_code: str, lever: str, key: str,
                  ev_ids: Sequence[str], batch: Sequence[tuple]) -> bool:
    """이미 있는(또는 이번 배치의) 과제와 사실상 같은가. find_duplicate 의 bool 래퍼."""
    return find_duplicate(conn, aff_code, lever, key, ev_ids, batch) is not None


def save_drafts(conn, ver_id: str, aff_code: str, drafts: List[TaskDraft],
                origin: str = "AI생성",
                status: str = "검토중") -> List[int]:
    """과제 초안 목록을 proposal 로 저장하고 새 id 목록을 돌려준다.

    ★ commit 하지 않는다. 호출자가 gen_version INSERT 와 같은 트랜잭션으로 묶는다 —
      과제가 하나도 저장되지 않았을 때 빈 생성 버전만 남는 것을 막기 위해서다.

    ★ 버리는 초안은 **반드시 로그를 남긴다**(log.info). 예전에는 조용히 continue 만
      해서 '초안 5건이 들어왔는데 왜 2건만 저장됐나' 를 사용자도 개발자도 알 수 없었다.
      화면에는 띄우지 않는다 — 새 안내 문구를 만들지 않는다는 규칙이 있고, 이건
      운영자가 서버 로그에서 확인할 정보다. 반환 타입(List[int])은 그대로 둔다:
      호출자(store.regenerate / create_custom)가 len() 으로 성패를 판정한다.
    """
    saved: List[int] = []
    dropped: List[str] = []         # 로그 요약용 — '이름(사유)' 문자열
    seen_keys: set = set()          # 같은 배치 안의 중복도 막는다
    batch_seen: List[tuple] = []    # (레버, 과제명키, 근거집합) — 배치 내 유사 중복 판정용

    def drop(name: str, why: str) -> None:
        dropped.append(f"{name}({why})")
        log.info("초안 버림 — %s / %s: %s", aff_code, why, name)

    for d in drafts:
        name = (d.title or "").strip()
        if not name:
            drop("(이름 없음)", "과제명이 비었다")
            continue

        # (2) 레버 — TaskDraft.lever 가 이미 정규화돼 있지만, 외부에서 만든 초안이
        #     들어올 수 있으므로 여기서 한 번 더 확인한다(저장 직전 단일 관문).
        lever = normalize_lever(d.lever or d.category, conn)
        if not lever:
            drop(name, f"레버 정규화 실패: {d.lever or d.category!r}")
            continue

        # (3) 중복 — 같은 계열사에 같은 정규화 과제명, 그리고 '표현만 바꾼 같은 과제'.
        #     판정 규칙과 그 근거는 상단 '중복 판정' 블록 참조.
        key = store.name_key(name)
        if key in seen_keys:
            drop(name, "이번 배치 안에 같은 과제명")
            continue
        if store.name_key_exists(conn, aff_code, key):
            drop(name, "같은 과제명이 이미 있음")
            continue

        # (4) 근거 — 실재하는 feed_item id 만
        wanted = [str(e) for e in d.evidence if e]
        real = _existing_feed_ids(conn, wanted)
        ev_ids = [e for e in wanted if e in real]
        if not ev_ids:
            drop(name, f"실재하는 근거 0건(요청 {wanted})")
            continue

        # (5) 사실상 같은 과제인지 — 근거가 확정된 뒤에 판정한다
        dup = find_duplicate(conn, aff_code, lever, key, ev_ids, batch_seen)
        if dup is not None:
            where = f"#{dup['id']} {dup['name']}" if dup["id"] else "이번 배치 안의 초안"
            drop(name, f"{dup['why']} → {where}")
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

    if dropped:
        log.info("%s 초안 %d건 중 %d건 저장 · %d건 제외 — %s",
                 aff_code, len(drafts), len(saved), len(dropped), " / ".join(dropped))
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
