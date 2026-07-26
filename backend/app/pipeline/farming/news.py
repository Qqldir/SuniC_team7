"""뉴스 크롤러 — Google News RSS (키 불필요).

검색어별 RSS 를 받아 최근 기사만 RawDoc 로 변환합니다.
운영 단계에서는 정식 뉴스 API(예: 사내 계약 벤더)로 교체 가능.
"""
import re
import hashlib
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import List
from urllib.parse import quote

import httpx

from app.pipeline.farming.base import RawDoc, KIND_NEWS
from app.pipeline.farming.watchlist import Watch, news_targets

RSS = "https://news.google.com/rss/search?q={q}&hl=ko&gl=KR&ceid=KR:ko"
_TAG_RE = re.compile(r"<[^>]+>")


def enabled() -> bool:
    return True


def _strip_html(s: str) -> str:
    return _TAG_RE.sub("", s or "").strip()


def _to_date(pub: str) -> str:
    try:
        return parsedate_to_datetime(pub).date().isoformat()
    except (TypeError, ValueError):
        return ""


def _crawl_query(w: Watch, since: date, per_query: int) -> List[RawDoc]:
    url = RSS.format(q=quote(w.news_query))
    r = httpx.get(url, timeout=20, follow_redirects=True)
    r.raise_for_status()
    root = ET.fromstring(r.content)

    docs: List[RawDoc] = []
    for item in root.iter("item"):
        title = _strip_html(item.findtext("title") or "")
        link = (item.findtext("link") or "").strip()
        pub = item.findtext("pubDate") or ""
        published = _to_date(pub)
        if not title or not published:
            continue
        if date.fromisoformat(published) < since:
            continue
        source_el = item.find("source")
        source = (source_el.text.strip() if source_el is not None and source_el.text else w.name)
        guid = item.findtext("guid") or link or title
        ext = hashlib.sha1(guid.encode("utf-8")).hexdigest()[:12]
        docs.append(RawDoc(
            ext_id=ext,
            source=source,
            kind=KIND_NEWS,
            published_on=published,
            title=title,
            url=link,
            body=_strip_html(item.findtext("description") or ""),
            tags=list(w.tags),
        ))
        if len(docs) >= per_query:
            break
    return docs


def crawl(since_days: int, per_query: int = 5) -> List[RawDoc]:
    since = date.today() - timedelta(days=since_days)
    docs: List[RawDoc] = []
    for w in news_targets():
        try:
            docs.extend(_crawl_query(w, since, per_query))
        except Exception as e:
            print(f"[news] '{w.news_query}' 조회 실패: {e}")
    print(f"[news] {len(docs)}건 수집")
    return docs
