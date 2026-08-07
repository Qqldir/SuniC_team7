"""감시 대상 peer 기업/토픽 목록.

각 항목은 어떤 소스에서 크롤할지와, 수집된 문서를 어떤 SK 계열사에 태깅할지를 정의합니다.
(정밀 태깅은 이후 entity 단계에서 보정 — 여기서는 watchlist 기준의 1차 태깅)

- dart_name : OpenDART corpCode.xml 에 등록된 명칭 **그대로**. None 이면 DART skip.
               통칭이 아니라 등록부 표기여서 직관과 다를 수 있습니다 (에쓰오일 → "S-Oil").
               매핑 실패 시 corpCode 캐시에서 검색해 수정하세요.
- sec_ticker: SEC 티커. None 이면 SEC skip.
- news_query: 뉴스 검색어. None 이면 뉴스 skip.
               검색어 언어에 따라 뉴스 RSS 로케일이 자동 분기됩니다 (news.py 참고).
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
# dart_name 은 2026-07 corpCode 등록부 기준으로 실제 조회 검증을 마친 값입니다.
WATCHLIST: List[Watch] = [
    # ── 국내 석유화학·정유 (DART + 뉴스) ──
    Watch("롯데케미칼", ["SKGC", "SKIPC"], dart_name="롯데케미칼", news_query="롯데케미칼 NCC"),
    Watch("에쓰오일", ["SKE"], dart_name="S-Oil", news_query="에쓰오일 정기보수"),
    Watch("GS칼텍스", ["SKE"], dart_name="GS칼텍스", news_query="GS칼텍스 투자"),
    # ── 배터리·소재 (DART + 뉴스) ──
    Watch("LG에너지솔루션", ["SKO"], dart_name="LG에너지솔루션", news_query="LG에너지솔루션 투자"),
    Watch("삼성SDI", ["SKO"], dart_name="삼성SDI", news_query="삼성SDI 가동률"),
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

# ── 확장 후보 ──────────────────────────────────────────────────────────
# 기본 크롤에는 포함되지 않고, include_candidates=True 일 때만 대상이 됩니다.
# 수집 품질을 확인한 뒤 WATCHLIST 로 승격하세요.
#
# 추가 검토 대상(미작성): 한화솔루션·HD현대오일뱅크·포스코퓨처엠·SK가스·한국가스공사(DART),
#   ExxonMobil 외 Shell(SHEL, 20-F)·TotalEnergies(TTE)·Albemarle(ALB)(SEC),
#   "정유 예지보전"·"battery dry electrode"·"데이터센터 액침냉각"·"탄소포집 CCS 상용화"(뉴스)
CANDIDATES: List[Watch] = [
    Watch("ExxonMobil", ["SKE", "SKEN"], sec_ticker="XOM", news_query="ExxonMobil cost savings program"),
    Watch("Chevron", ["SKE", "SKEO"], sec_ticker="CVX", news_query="Chevron structural cost reduction"),
    Watch("Phillips 66", ["SKE"], sec_ticker="PSX", news_query="Phillips 66 refining margin improvement"),
    Watch("NextEra", ["SKES"], sec_ticker="NEE", news_query="NextEra O&M productivity"),
    Watch("금호석유화학", ["SKGC"], dart_name="금호석유화학", news_query="금호석유화학 원가"),
    Watch("한화솔루션", ["SKGC"], dart_name="한화솔루션", news_query="한화솔루션 케미칼"),
]


def _pool(include_candidates: bool) -> List[Watch]:
    return WATCHLIST + (CANDIDATES if include_candidates else [])


def dart_targets(include_candidates: bool = False) -> List[Watch]:
    return [w for w in _pool(include_candidates) if w.dart_name]


def sec_targets(include_candidates: bool = False) -> List[Watch]:
    return [w for w in _pool(include_candidates) if w.sec_ticker]


def news_targets(include_candidates: bool = False) -> List[Watch]:
    return [w for w in _pool(include_candidates) if w.news_query]
