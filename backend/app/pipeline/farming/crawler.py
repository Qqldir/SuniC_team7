"""지식 파밍 오케스트레이션.

watchlist 를 대상으로 DART · SEC · 뉴스 소스를 크롤해 RawDoc 목록으로 통합하고,
선별된 건에 한해 원문(body)을 확보합니다.

개별 소스는 키 미설정/네트워크 오류 시 조용히 빈 결과를 반환하므로,
일부 소스만으로도 부분 동작합니다.

    crawl_all()    → 목록(메타)만. 저렴.
    fetch_bodies() → 선별 건의 원문 확보. rate limit·API 한도가 걸리므로 상한을 둡니다.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

from app.config import CRAWL_SINCE_DAYS
from app.pipeline.farming.base import (
    REASON_ERROR, REASON_EXTRACT, REASON_QUOTA, RawDoc, source_of,
)
from app.pipeline.farming import dart, sec, news

# 소스 모듈은 crawl / body_priority / fetch_body 를 동일 시그니처로 제공합니다.
# 키는 RawDoc.feed_id 의 접두어와 일치해야 합니다 (base.RawDoc.feed_id 참고).
#
# 선택 속성 두 가지(없으면 기본값):
#   MIN_SINCE_DAYS  이 소스가 의미 있으려면 필요한 최소 크롤 창(일). 기본 0.
#   BODY_FACTOR     per_source 상한에 곱할 배수. 기본 1.
#                   소스마다 원문 확보 비용이 자릿수 단위로 다르기 때문에 필요한 훅이다.
#                   각 모듈의 BODY_FACTOR 주석에 그 소스의 실측 비용이 적혀 있다.
SOURCES: Dict[str, object] = {"dart": dart, "sec": sec, "news": news}


def crawl_all(
    since_days: Optional[int] = None,
    sources: Optional[List[str]] = None,
) -> List[RawDoc]:
    days = since_days if since_days is not None else CRAWL_SINCE_DAYS
    names = sources or list(SOURCES)
    docs: List[RawDoc] = []
    for name in names:
        mod = SOURCES.get(name)
        if mod is None:
            print(f"[crawler] 알 수 없는 소스: {name}")
            continue
        # 소스마다 자료가 나오는 주기가 다릅니다. 뉴스 기준의 창(30일)을 그대로 쓰면
        # 분기마다 나오는 DART 정기보고서가 구조적으로 0건이 됩니다(실측). 바닥만 올립니다.
        floor = getattr(mod, "MIN_SINCE_DAYS", 0)
        src_days = max(days, floor)
        if src_days != days:
            print(f"[crawler] {name}: 창을 {days}일 → {src_days}일로 넓힘 (자료 주기)")
        docs += mod.crawl(src_days)
    return _dedup(docs)


@dataclass
class SourceStat:
    """소스 하나의 원문 확보 결과. 크롤 로그 끝 요약표의 한 행."""
    collected: int = 0     # 목록에서 수집된 건수
    prefilled: int = 0     # 목록 단계에서 이미 본문이 있던 건 (재조회하지 않음)
    attempted: int = 0     # 실제로 원문을 받으러 간 건수
    filled: int = 0        # 그중 확보에 성공한 건수
    reasons: Counter = field(default_factory=Counter)   # 미확보 사유별 건수

    @property
    def with_body(self) -> int:
        return self.prefilled + self.filled


def fetch_bodies(docs: List[RawDoc], per_source: int = 0) -> Dict[str, SourceStat]:
    """소스별 상한만큼 원문을 확보한다. 반환: 소스별 SourceStat.

    상한은 `per_source × 모듈의 BODY_FACTOR` 입니다. 배수가 소스마다 다른 이유는
    원문 확보 비용이 자릿수 단위로 다르기 때문입니다 — 하나의 숫자에 묶으면 가장 비싼
    소스(뉴스)에 맞춰 공시가 통째로 잘립니다. 근거 수치는 각 모듈의 BODY_FACTOR 주석에 있습니다.
    per_source=0 이면 아무것도 받지 않습니다(목록만).
    실패는 건 단위로 격리되어 한 건이 전체를 중단시키지 않습니다.
    """
    by_source: Dict[str, List[RawDoc]] = defaultdict(list)
    for d in docs:
        by_source[source_of(d)].append(d)
    stats: Dict[str, SourceStat] = {
        name: SourceStat(collected=len(group)) for name, group in by_source.items()
    }
    if per_source <= 0:
        for name, st in stats.items():
            st.prefilled = sum(1 for d in by_source[name] if d.body)
            st.reasons[REASON_QUOTA] = st.collected - st.prefilled
        return stats

    for name, group in by_source.items():
        st = stats[name]
        mod = SOURCES.get(name)
        if mod is None:
            continue
        quota = per_source * getattr(mod, "BODY_FACTOR", 1)
        # ★ 이미 본문이 있는 건은 **선별에서 먼저 뺀다.**
        #   예전에는 _pick 이 quota 개를 뽑은 뒤 루프에서 `if doc.body: continue` 로 건너뛰었다.
        #   그러면 재조회하지도 않을 문서가 상한 슬롯만 먹고 사라져, 정작 본문이 필요한 건이
        #   '한도밖' 으로 밀린다. 뉴스는 RSS description 이 본문을 채우는 날이 있어 실제로 터진다.
        st.prefilled = sum(1 for d in group if d.body)
        pending = [d for d in group if not d.body]
        picked = _pick(pending, mod.body_priority, quota)
        st.reasons[REASON_QUOTA] += len(pending) - len(picked)

        for doc in picked:
            st.attempted += 1
            try:
                body = mod.fetch_body(doc)
            except Exception as e:
                print(f"[{name}] 원문 실패 {doc.ext_id}: {e}")
                st.reasons[doc.meta.get("body_reason") or REASON_ERROR] += 1
                continue
            if body:
                doc.body = body
                st.filled += 1
                print(f"[{name}] 원문 확보: {doc.source} {doc.title[:34]} ({len(body):,}자)")
            else:
                # 모듈이 사유를 남기지 않았으면 '추출은 했으나 쓸 만한 본문이 없었다' 로 본다.
                st.reasons[doc.meta.get("body_reason") or REASON_EXTRACT] += 1
    return stats


def format_report(stats: Dict[str, SourceStat]) -> str:
    """운영자용 요약표 — 소스별 (수집 / 원문 확보 / 미확보 사유별).

    성공만 찍히는 로그로는 "무엇이 왜 빠졌는지" 를 알 수 없다. 특히 '한도밖' 은
    --with-docs 를 올리면 그대로 회수되는 물량이라 다른 사유와 구분해서 보여야 한다.
    """
    if not stats:
        return "  (수집된 자료가 없습니다)"
    lines = [f"  {'소스':<6}{'수집':>6}{'원문확보':>8}{'확보율':>8}  미확보 사유"]
    total = SourceStat()
    for name in sorted(stats):
        st = stats[name]
        total.collected += st.collected
        total.prefilled += st.prefilled
        total.attempted += st.attempted
        total.filled += st.filled
        total.reasons.update(st.reasons)
        why = " · ".join(f"{k} {v}" for k, v in st.reasons.most_common() if v) or "-"
        rate = f"{st.with_body / st.collected * 100:.0f}%" if st.collected else "-"
        lines.append(f"  {name:<6}{st.collected:>6}{st.with_body:>8}{rate:>8}  {why}")
    rate = f"{total.with_body / total.collected * 100:.0f}%" if total.collected else "-"
    why = " · ".join(f"{k} {v}" for k, v in total.reasons.most_common() if v) or "-"
    lines.append(f"  {'합계':<5}{total.collected:>6}{total.with_body:>8}{rate:>8}  {why}")
    return "\n".join(lines)


def _pick(docs: List[RawDoc], priority: Callable[[RawDoc], int], limit: int) -> List[RawDoc]:
    """우선순위 정렬 후 기업(source)별로 돌아가며 뽑는다.

    우선순위로만 자르면 한 기업의 공시가 상한을 독식합니다
    (실측: SEC 원문 2건이 모두 Dow 였음).
    """
    buckets: Dict[str, List[RawDoc]] = defaultdict(list)
    for d in sorted(docs, key=priority):
        buckets[d.source].append(d)

    picked: List[RawDoc] = []
    while len(picked) < limit:
        added = False
        for group in buckets.values():
            if not group:
                continue
            picked.append(group.pop(0))
            added = True
            if len(picked) >= limit:
                break
        if not added:
            break
    return picked


def _dedup(docs: List[RawDoc]) -> List[RawDoc]:
    """feed_id 기준 중복 제거 (동일 문서가 여러 검색어에 걸릴 수 있음)."""
    seen = set()
    out = []
    for d in docs:
        if d.feed_id in seen:
            continue
        seen.add(d.feed_id)
        out.append(d)
    return out
