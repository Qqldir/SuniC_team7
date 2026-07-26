"""엔티티 추출 · 계열사 태깅 (스텁).

요약문에서 계열사/경쟁사/공정/기술 엔티티를 추출해 feed_item_tag 로 연결.
"""
from typing import List


def tag_affiliates(summary: str) -> List[str]:
    """요약문과 관련된 계열사 코드 목록을 반환."""
    raise NotImplementedError("엔티티 태깅 미구현")
