"""지식 파밍 오케스트레이션.

watchlist 를 대상으로 DART · SEC · 뉴스 소스를 크롤해 RawDoc 목록으로 통합합니다.
개별 소스는 키 미설정/네트워크 오류 시 조용히 빈 결과를 반환하므로,
일부 소스만으로도 부분 동작합니다.
"""
from typing import List

from app.config import CRAWL_SINCE_DAYS
from app.pipeline.farming.base import RawDoc
from app.pipeline.farming import dart, sec, news


def crawl_all(since_days: int | None = None) -> List[RawDoc]:
    days = since_days if since_days is not None else CRAWL_SINCE_DAYS
    docs: List[RawDoc] = []
    docs += dart.crawl(days)
    docs += sec.crawl(days)
    docs += news.crawl(days)
    return _dedup(docs)


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
