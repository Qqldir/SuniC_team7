"""엔티티 추출 · 계열사 태깅.

watchlist 는 "이 기업을 보면 이 계열사와 관련 있다"는 1차 태깅만 합니다.
같은 기업이라도 기사 내용에 따라 관련 계열사가 달라지므로 여기서 보정합니다.

    watchlist 1차 태깅  →  LLM 정밀 태깅(있으면)  →  키워드 폴백  →  feed_item_tag

LLM 을 별도로 호출하지 않습니다. llm.enrich() 가 이미 계열사를 뽑아주므로 그 결과를
받아 검증만 하고, 없을 때만 키워드 규칙으로 보완합니다 (중복 호출 = 중복 비용).
"""
from typing import Iterable, List, Optional, Sequence

from app.config import AFFILIATE_CODES

# 사업영역 키워드 → 계열사. LLM 이 없을 때 watchlist 태깅을 보완하는 용도라
# 재현율보다 정밀도를 우선해 오태깅을 피합니다.
KEYWORDS = {
    "SKE": ["정유", "정제마진", "석유제품", "휘발유", "경유", "refinery", "refining"],
    "SKGC": ["석유화학", "NCC", "에틸렌", "나프타", "리사이클", "재활용 플라스틱", "petrochemical"],
    "SKEN": ["윤활유", "윤활기유", "베이스오일", "열관리", "액침냉각", "lubricant", "base oil"],
    "SKIPC": ["인천석유화학", "파라자일렌", "아로마틱"],
    "SKTI": ["트레이딩", "원유 조달", "해상운임", "용선", "freight"],
    "SKEO": ["석유개발", "E&P", "광구", "탐사", "upstream", "exploration"],
    "SKO": ["배터리", "이차전지", "전기차", "셀 수율", "양극재", "음극재", "battery"],
    "SKIET": ["분리막", "separator"],
    "SKES": ["LNG", "액화천연가스", "발전소", "전력", "수소", "power generation"],
}


def _valid(codes: Iterable[str]) -> List[str]:
    """마스터에 있는 계열사 코드만, 순서 유지 + 중복 제거."""
    out: List[str] = []
    for c in codes:
        if c in AFFILIATE_CODES and c not in out:
            out.append(c)
    return out


def tag_by_keyword(text: str) -> List[str]:
    """본문/요약에서 사업영역 키워드로 계열사를 추정한다."""
    if not text:
        return []
    low = text.lower()
    return _valid([
        code for code, words in KEYWORDS.items()
        if any(w.lower() in low for w in words)
    ])


def tag_affiliates(
    text: str,
    base_tags: Sequence[str] = (),
    llm_affiliates: Optional[Sequence[str]] = None,
) -> List[str]:
    """최종 계열사 태그를 결정한다.

    - LLM 결과가 있으면 그것을 채택 (watchlist 보다 문맥을 본다)
    - 없으면 watchlist 1차 태깅 + 키워드 추정의 합집합
    - 어느 경로든 **빈 배열을 반환하지 않는다** — 태그가 없으면 계열사 필터에서 사라져
      수집해 놓고도 발굴에 쓰이지 못한다. 최후에는 base_tags 로 되돌립니다.
    """
    if llm_affiliates:
        tagged = _valid(llm_affiliates)
        if tagged:
            return tagged

    merged = _valid(list(base_tags) + tag_by_keyword(text))
    return merged or _valid(base_tags)
