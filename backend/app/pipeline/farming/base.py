"""파밍 공통 타입."""
from dataclasses import dataclass, field
from typing import List

# feed_item.kind 와 동일한 분류값
KIND_ADHOC = "adhoc"        # DART 수시(주요사항)
KIND_PERIODIC = "periodic"  # DART 정기
KIND_SEC = "sec"            # SEC EDGAR
KIND_NEWS = "news"          # 뉴스


@dataclass
class RawDoc:
    """크롤러가 반환하는 정규화된 원문 메타데이터.

    이후 pdf/llm(요약)·entity(태깅) 단계를 거쳐 feed_item 으로 적재됩니다.
    """
    ext_id: str                       # 소스 내 고유 id (rcept_no, accession_no, guid)
    source: str                       # 발표 주체 (롯데케미칼, Dow ...)
    kind: str                         # KIND_*
    published_on: str                 # YYYY-MM-DD
    title: str
    url: str = ""
    body: str = ""                    # 본문/요약 원문 (있으면)
    tags: List[str] = field(default_factory=list)  # 관련 SK 계열사 코드

    @property
    def feed_id(self) -> str:
        """feed_item.id — 소스 접두어 + 고유 id (재크롤 시 중복 방지)."""
        prefix = {KIND_SEC: "sec", KIND_NEWS: "news"}.get(self.kind, "dart")
        return f"{prefix}-{self.ext_id}"
