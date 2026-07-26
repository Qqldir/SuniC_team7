"""감시 대상 peer 기업/토픽 목록.

각 항목은 어떤 소스에서 크롤할지와, 수집된 문서를 어떤 SK 계열사에 태깅할지를 정의합니다.
(정밀 태깅은 이후 entity 단계에서 보정 — 여기서는 watchlist 기준의 1차 태깅)

- dart_name : OpenDART 등록 정식 명칭 (예: 삼성SDI → "삼성에스디아이"). None 이면 DART skip.
- sec_ticker: SEC 티커. None 이면 SEC skip.
- news_query: 뉴스 검색어. None 이면 뉴스 skip.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Watch:
    name: str
    tags: List[str] = field(default_factory=list)
    dart_name: Optional[str] = None
    sec_ticker: Optional[str] = None
    news_query: Optional[str] = None


# 데모 피드의 peer 구성을 기준으로 초기 watchlist 구성.
WATCHLIST: List[Watch] = [
    # ── 국내 석유화학·정유 (DART + 뉴스) ──
    Watch("롯데케미칼", ["SKGC", "SKIPC"], dart_name="롯데케미칼", news_query="롯데케미칼 NCC"),
    Watch("에쓰오일", ["SKE"], dart_name="에쓰오일", news_query="에쓰오일 정기보수"),
    Watch("GS칼텍스", ["SKE"], dart_name="지에스칼텍스", news_query="GS칼텍스 투자"),
    # ── 배터리·소재 (DART + 뉴스) ──
    Watch("LG에너지솔루션", ["SKO"], dart_name="엘지에너지솔루션", news_query="LG에너지솔루션 투자"),
    Watch("삼성SDI", ["SKO"], dart_name="삼성에스디아이", news_query="삼성SDI 가동률"),
    Watch("포스코인터내셔널", ["SKEO"], dart_name="포스코인터내셔널", news_query="포스코인터내셔널 E&P"),
    # ── 해외 peer (SEC + 뉴스) ──
    Watch("Dow", ["SKGC"], sec_ticker="DOW", news_query="Dow Chemical cost reduction"),
    Watch("LyondellBasell", ["SKGC"], sec_ticker="LYB", news_query="LyondellBasell assets"),
    Watch("Cheniere", ["SKES"], sec_ticker="LNG", news_query="Cheniere operating cost"),
    Watch("Valero", ["SKE"], sec_ticker="VLO", news_query="Valero opex refining"),
    # ── 뉴스 전용 (SEC/DART 미해당) ──
    Watch("CATL", ["SKO"], news_query="CATL yield inspection automation"),
    Watch("아사히카세이", ["SKIET"], news_query="아사히카세이 분리막"),
    Watch("미쓰이화학", ["SKGC", "SKE"], news_query="미쓰이화학 정기보수"),
    # ── 산업·정책·시황 토픽 (뉴스 전용) ──
    Watch("에너지 정책", ["SKE", "SKGC", "SKIPC"], news_query="산업용 전기요금 인상"),
    Watch("해운 시황", ["SKTI", "SKE", "SKO"], news_query="컨테이너 해상운임 지수"),
]


def dart_targets() -> List[Watch]:
    return [w for w in WATCHLIST if w.dart_name]


def sec_targets() -> List[Watch]:
    return [w for w in WATCHLIST if w.sec_ticker]


def news_targets() -> List[Watch]:
    return [w for w in WATCHLIST if w.news_query]
