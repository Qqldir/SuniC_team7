"""수집 자료의 표시값 규칙 분류 — 자료 종류 · 테마 · 사업분야 · 근거 등급.

LLM 없이 **규칙만으로** 화면 표시에 필요한 값을 확정합니다.
트렌드룸은 kind_label(자료 종류) · theme(테마) · biz_hint(사업분야)가 비면 필터에서
자료가 사라지므로, 이 값들은 LLM 실패 여부와 무관하게 항상 채워져야 합니다.

    RawDoc(meta) ─ kind_of() ─→ (kind_label, kind_key)
                 └ theme_by_rule() ─→ theme.name 7종 중 하나
                 └ biz_hint_of()   ─→ biz_segment.label 3종 중 하나
                 └ evidence_grade_of() ─→ 원문 확보 / 요약문 / 제목만

용어 구분:
    kind      화면 축 6종 키. source_kind.key 와 같다 (disclosure/earnings/ir/market/assoc/news)
    kind_label 자료 종류 세부 표기. '사업보고서', '실적발표 (8-K)', '뉴스 (연합뉴스)' …
              화면의 KIND_MAP 이 kind_label → source_kind.label 로 묶어 필터 칩을 만든다.
    source    발표 주체 (감시 대상 기업명)
    publisher 매체·발행처 (연합뉴스 / Reuters / SEC EDGAR / DART)
"""
import re
from collections import Counter
from typing import Dict, List, Optional, Sequence, Tuple

# ── 화면 축 6종 (source_kind.key → source_kind.label) ────────────────────
# 이 라벨은 트렌드룸 '종류' 필터 칩 문자열이므로 source_kind.label 과 글자까지 같아야 한다.
KIND_DISCLOSURE = "disclosure"
KIND_EARNINGS = "earnings"
KIND_IR = "ir"
KIND_MARKET = "market"
KIND_ASSOC = "assoc"
KIND_NEWS_AXIS = "news"

AXIS_LABELS: Dict[str, str] = {
    KIND_DISCLOSURE: "공시",
    KIND_EARNINGS: "실적발표",
    KIND_IR: "IR·보고서",
    KIND_MARKET: "시황·전문지",
    KIND_ASSOC: "협회 자료",
    KIND_NEWS_AXIS: "뉴스",
}

# ── DART ────────────────────────────────────────────────────────────────
# 선두 정정 태그([기재정정]/[첨부정정]/[발행조건확정] …)와 후미 '(YYYY.MM)' 을 떼고 매핑한다.
_DART_PREFIX_RE = re.compile(r"^\s*(?:\[[^\]]*\]\s*)+")
_DART_SUFFIX_RE = re.compile(r"\s*\(\s*\d{4}\.\d{1,2}\s*\)\s*$")

# 정규화된 report_nm 이 이 키로 '시작' 하면 채택 (주요사항보고서(회사합병결정) 처럼 괄호가 붙는다)
_DART_PREFIX_MAP: List[Tuple[str, Tuple[str, str]]] = [
    ("사업보고서", ("사업보고서", KIND_DISCLOSURE)),
    ("반기보고서", ("반기보고서", KIND_DISCLOSURE)),
    ("분기보고서", ("분기보고서", KIND_DISCLOSURE)),
    ("감사보고서", ("감사보고서", KIND_DISCLOSURE)),
    ("연결감사보고서", ("감사보고서", KIND_DISCLOSURE)),
    ("주요사항보고서", ("주요사항보고서", KIND_DISCLOSURE)),
    ("증권신고서", ("증권신고서", KIND_DISCLOSURE)),
    ("기업설명회(IR)개최", ("IR 개최 안내", KIND_IR)),
    ("기업설명회", ("IR 개최 안내", KIND_IR)),
]

# 보고서명 어딘가에 이 조각이 있으면 채택 (실적 공시는 표기 변형이 많다)
_DART_CONTAINS_MAP: List[Tuple[str, Tuple[str, str]]] = [
    ("영업(잠정)실적", ("잠정실적 공시", KIND_EARNINGS)),
    ("영업잠정실적", ("잠정실적 공시", KIND_EARNINGS)),
    ("매출액또는손익구조", ("잠정실적 공시", KIND_EARNINGS)),
    ("매출액또는손익", ("잠정실적 공시", KIND_EARNINGS)),
    ("결산실적", ("잠정실적 공시", KIND_EARNINGS)),
]

# pblntf_ty 폴백 — A: 정기공시, 그 외: 수시공시
_DART_TY_MAP: Dict[str, Tuple[str, str]] = {
    "A": ("정기공시", KIND_DISCLOSURE),
    "B": ("수시공시", KIND_DISCLOSURE),
}
_DART_TY_DEFAULT = ("수시공시", KIND_DISCLOSURE)


def normalize_report_nm(report_nm: str) -> str:
    """DART report_nm 정규화 — 선두 [기재정정]/[첨부정정] 과 후미 '(YYYY.MM)' 제거."""
    s = (report_nm or "").strip()
    s = _DART_PREFIX_RE.sub("", s)
    s = _DART_SUFFIX_RE.sub("", s)
    return s.strip()


def dart_kind(report_nm: str, pblntf_ty: str = "") -> Tuple[str, str]:
    """DART 보고서명 → (kind_label, kind). 매칭 실패 시 pblntf_ty 로 폴백."""
    name = normalize_report_nm(report_nm)
    flat = name.replace(" ", "")
    for frag, hit in _DART_CONTAINS_MAP:
        if frag in flat:
            return hit
    for prefix, hit in _DART_PREFIX_MAP:
        if flat.startswith(prefix):
            return hit
    return _DART_TY_MAP.get((pblntf_ty or "").strip().upper(), _DART_TY_DEFAULT)


# ── SEC EDGAR ───────────────────────────────────────────────────────────
# form → (kind_label, kind). 8-K/6-K 는 primaryDocDescription 을 함께 본다.
_SEC_FORM_MAP: Dict[str, Tuple[str, str]] = {
    "10-K": ("연차보고서 (10-K)", KIND_IR),
    "20-F": ("연차보고서 (20-F)", KIND_IR),
    "40-F": ("연차보고서 (40-F)", KIND_IR),
    "10-Q": ("분기보고서 (10-Q)", KIND_DISCLOSURE),
}
# 8-K 본문 설명에 이 단어가 있으면 실적발표로 본다 (Item 2.02 Results of Operations 등)
_SEC_EARNINGS_WORDS = ("EARNINGS", "RESULTS", "QUARTER")
_SEC_EVENT_FORMS = ("8-K", "6-K")


def sec_kind(form: str, desc: str = "") -> Tuple[str, str]:
    """SEC 서식 → (kind_label, kind)."""
    f = (form or "").strip().upper()
    hit = _SEC_FORM_MAP.get(f)
    if hit:
        return hit
    if f in _SEC_EVENT_FORMS:
        up = (desc or "").upper()
        if any(w in up for w in _SEC_EARNINGS_WORDS):
            return (f"실적발표 ({f})", KIND_EARNINGS)
        return (f"수시공시 ({f})", KIND_DISCLOSURE)
    if not f:
        return ("수시공시", KIND_DISCLOSURE)
    return (f"공시 ({f})", KIND_DISCLOSURE)


# ── 뉴스 매체 ───────────────────────────────────────────────────────────
# 시황 벤더 — 가격·운임 지수를 내는 유료 리포트 발행처
_MARKET_VENDORS = ("argus", "icis", "platts", "s&p global", "s&p global commodity insights")
# 산업 전문 매체 — 라벨에 매체명을 노출한다 ('전문지 (SNE Research)')
_TRADE_PRESS = (
    "sne research", "chemical week", "bloombergnef", "bnef", "wood mackenzie",
    "c&en", "chemical & engineering news", "icis chemical business", "energy intelligence",
)
# 협회·단체
_ASSOCIATIONS = (
    "대한석유협회", "한국석유화학협회", "한국배터리산업협회", "한국무역협회",
    "한국화학산업연합회", "석유화학협회", "전국경제인연합회", "대한상공회의소",
)
_ASSOC_SUFFIXES = ("협회", "연합회", "학회", "조합", "상공회의소")


# ── 매체명 정규화 ───────────────────────────────────────────────────────
# Google News 의 <source> 는 보통 매체명('연합뉴스')이지만, 구글이 그 매체를 모르면
# **도메인을 그대로** 내려준다(실측 44건 중 4종: v.daum.net · investchosun.com ·
# fortune.com · finance.biggo.com. 이전 회차에서는 ebn.co.kr · news.chemnet.com 도 나왔다).
# 도메인이 화면 '뉴스 (v.daum.net)' 자리에 그대로 박히면 출처가 읽히지 않는다.
#
# 방침: **아는 것만 이름으로 바꾼다.** 도메인에서 이름을 지어내지 않는다 —
#   ebn.co.kr → "Ebn", finance.biggo.com → "Biggo" 처럼 틀린 표기가 만들어지고,
#   그 틀린 이름이 feed_item.publisher 로 굳어 사례 인용에 그대로 쓰이기 때문이다.
# 매핑에 없으면 www./m. 만 떼고 도메인을 그대로 둔다(도메인은 최소한 검증 가능한 사실이다).
# 새 도메인이 관측되면 여기에 실측값으로 추가하라.
_DOMAIN_PUBLISHERS: Dict[str, str] = {
    # 포털·아카이브 (원 매체가 아니라 재게시처다. 그래도 도메인보다는 읽힌다)
    "v.daum.net": "다음뉴스",
    "news.daum.net": "다음뉴스",
    "n.news.naver.com": "네이버뉴스",
    "news.naver.com": "네이버뉴스",
    # 국내 매체
    "investchosun.com": "인베스트조선",
    "biz.chosun.com": "조선비즈",
    "ebn.co.kr": "EBN",
    "etnews.com": "전자신문",
    "hankyung.com": "한국경제",
    "mk.co.kr": "매일경제",
    "sedaily.com": "서울경제",
    "yna.co.kr": "연합뉴스",
    "newsis.com": "뉴시스",
    "dt.co.kr": "디지털타임스",
    "theguru.co.kr": "더구루",
    "energy-news.co.kr": "에너지신문",
    # 해외 매체·전문지
    "news.chemnet.com": "ChemNet",
    "fortune.com": "Fortune",
    "reuters.com": "Reuters",
    "bloomberg.com": "Bloomberg",
    "cnbc.com": "CNBC",
    "ft.com": "Financial Times",
    "chemanalyst.com": "ChemAnalyst",
    "icis.com": "ICIS",
    # 가격·시세 애그리게이터 (매체가 아니다. 이름을 밝혀 두면 화면에서 걸러 볼 수 있다)
    "finance.biggo.com": "BigGo Finance",
    "investing.com": "Investing.com",
}

# 'a.b.c' 처럼 점으로 이어진 ASCII 라벨만 도메인으로 본다.
# 'Investing.com UK' 처럼 공백이 섞인 정식 매체명은 여기 걸리지 않는다(의도).
_DOMAIN_RE = re.compile(r"^[a-z0-9][a-z0-9\-]*(?:\.[a-z0-9][a-z0-9\-]*)+$", re.I)
_TRIM_PREFIXES = ("www.", "m.", "amp.")


def publisher_label(publisher: str) -> str:
    """RSS <source> 값 → 화면에 쓸 매체 표기.

    이미 사람이 읽는 이름이면 그대로 돌려준다. 도메인이면 매핑을 찾고,
    없으면 www./m. 만 떼어 도메인 그대로 둔다(이름을 지어내지 않는다).
    """
    name = (publisher or "").strip()
    if not name or not _DOMAIN_RE.match(name):
        return name
    low = name.lower()
    for pre in _TRIM_PREFIXES:
        if low.startswith(pre):
            low = low[len(pre):]
    if low in _DOMAIN_PUBLISHERS:
        return _DOMAIN_PUBLISHERS[low]
    # 서브도메인만 다른 경우(news.hankyung.com)도 등록 도메인으로 한 번 더 본다.
    parts = low.split(".")
    for i in range(1, len(parts) - 1):
        tail = ".".join(parts[i:])
        if tail in _DOMAIN_PUBLISHERS:
            return _DOMAIN_PUBLISHERS[tail]
    return low


def news_kind(publisher: str = "") -> Tuple[str, str]:
    """뉴스 매체명 → (kind_label, kind). 매체명이 없으면 ('뉴스', news)."""
    name = (publisher or "").strip()
    if not name:
        return ("뉴스", KIND_NEWS_AXIS)
    low = name.lower()
    if any(v in low for v in _MARKET_VENDORS):
        return ("시황 리포트", KIND_MARKET)
    if any(v in low for v in _TRADE_PRESS):
        return (f"전문지 ({name})", KIND_MARKET)
    if name in _ASSOCIATIONS or any(name.endswith(s) for s in _ASSOC_SUFFIXES):
        return ("협회 자료", KIND_ASSOC)
    return (f"뉴스 ({name})", KIND_NEWS_AXIS)


# ── RawDoc 디스패치 ──────────────────────────────────────────────────────
# RawDoc.kind 는 크롤러 내부 분류값(adhoc/periodic/sec/news)이고 feed_id 접두어의 근거라
# 건드리지 않는다. 화면 축(kind)과 kind_label 은 여기서 meta 를 보고 계산한다.

def kind_of(doc) -> Tuple[str, str]:
    """RawDoc → (kind_label, kind). ingest 가 feed_item.kind/kind_label 에 그대로 넣는다."""
    meta = getattr(doc, "meta", None) or {}
    raw_kind = getattr(doc, "kind", "") or ""
    if raw_kind == "sec":
        return sec_kind(meta.get("form", ""), meta.get("desc", ""))
    if raw_kind == "news":
        return news_kind(getattr(doc, "publisher", "") or "")
    if raw_kind in ("adhoc", "periodic"):
        return dart_kind(
            meta.get("report_nm", "") or getattr(doc, "title", ""),
            meta.get("pblntf_ty", "A" if raw_kind == "periodic" else "B"),
        )
    # 미지의 소스가 붙어도 화면이 죽지 않도록 공시로 떨어뜨린다.
    return ("수시공시", KIND_DISCLOSURE)


# ── 테마 (theme 테이블 7종) ──────────────────────────────────────────────
# 키는 theme.name 과 **정확히** 같아야 한다 (feed_item.theme 이 화면 필터 문자열).
# 순서는 theme.sort_order 순 — 동점일 때 앞에 있는 테마가 이긴다.
THEME_KEYWORDS: Dict[str, Tuple[str, ...]] = {
    "정비·설비 신뢰성": (
        "정기보수", "TA", "턴어라운드", "예방정비", "예지보전", "정비", "설비 고장",
        "고장", "가동중단", "비가동", "셧다운", "공기 단축", "설비종합효율", "OEE", "신뢰성",
        "maintenance", "turnaround", "shutdown", "reliability", "downtime", "outage",
    ),
    "에너지·유틸리티": (
        "전력", "전기요금", "에너지", "유틸리티", "스팀", "열효율", "원단위", "연료비",
        "자가발전", "피크", "폐열", "재생에너지", "수소", "탄소", "전력비",
        "energy", "power", "utility", "steam", "fuel cost", "emission",
    ),
    "구매·조달": (
        # '단가' 단독은 넣지 않는다 — 생산 단가·판매 단가까지 걸려 원가 이야기를 구매로 끌어온다
        # (실측: e13 'E&P 생산 단가' 가 간접비·원가구조 대신 구매·조달로 분류됐다).
        "구매", "조달", "소싱", "원자재", "공급사", "입찰", "MRO", "규격 표준화",
        "협상", "벤더", "납품", "통합 입찰", "원료 구매", "계약 단가",
        "procurement", "sourcing", "supplier", "purchasing", "raw material",
    ),
    "공정 수율·품질": (
        "수율", "불량", "품질", "검사", "전수검사", "공정 개선", "머신비전", "결함",
        "재작업", "스크랩", "양산", "셀 수율", "공정 능력", "검출률", "자동화 검사",
        "yield", "quality", "defect", "inspection", "scrap", "rework",
    ),
    "물류·계약": (
        "물류", "운송", "해상운임", "운임", "용선", "컨테이너", "창고", "배송", "선복",
        "하역", "공급망", "이송", "선박", "장기계약", "재협상",
        "freight", "logistics", "shipping", "charter", "supply chain",
    ),
    "간접비·원가구조": (
        "간접비", "판관비", "고정비", "원가", "비용 절감", "비용절감", "지원 기능",
        "조직 통합", "구조조정", "오펙스", "운영비", "인건비", "관리비", "원가 구조", "효율화",
        "opex", "cost reduction", "cost saving", "overhead", "sg&a", "restructuring",
    ),
    "가동률·운전자본": (
        "가동률", "가동 조정", "재고", "운전자본", "회전율", "회전일수", "감산", "현금흐름",
        "캐파", "증설", "수요 부진", "다운사이클", "설비 투자", "회수 기간", "안전재고",
        "utilization", "inventory", "working capital", "capacity", "cash flow",
    ),
}

# theme 테이블 화이트리스트 (sort_order 순)
THEMES: Tuple[str, ...] = tuple(THEME_KEYWORDS)
# 키워드가 하나도 안 걸릴 때. '어느 자료든 원가 이야기는 한다' 는 가장 무난한 축.
THEME_DEFAULT = "간접비·원가구조"

_ASCII_RE = re.compile(r"^[\x00-\x7f]+$")


def _count_hits(text_low: str, keyword: str) -> int:
    """키워드 등장 횟수. 영문·숫자 키워드는 단어 경계를 본다(TA 가 data 에 걸리는 것 방지)."""
    kw = keyword.lower()
    if _ASCII_RE.match(kw):
        return len(re.findall(rf"(?<![a-z0-9]){re.escape(kw)}(?![a-z0-9])", text_low))
    return text_low.count(kw)


def theme_score(text: str) -> Dict[str, int]:
    """테마별 키워드 적중 합계. 디버깅·튜닝용."""
    low = (text or "").lower()
    return {name: sum(_count_hits(low, k) for k in kws) for name, kws in THEME_KEYWORDS.items()}


def theme_by_rule(text: str) -> str:
    """제목+요약+본문 → theme 테이블 7종 중 하나. 0히트면 THEME_DEFAULT."""
    scores = theme_score(text)
    # dict 는 삽입 순서(=sort_order)를 보존하므로 동점이면 앞선 테마가 이긴다.
    best = max(scores, key=lambda n: scores[n]) if scores else THEME_DEFAULT
    return best if scores.get(best, 0) > 0 else THEME_DEFAULT


def valid_theme(name: Optional[str]) -> Optional[str]:
    """LLM 이 준 테마명을 화이트리스트로 검증. 아니면 None."""
    s = (name or "").strip()
    return s if s in THEME_KEYWORDS else None


# ── 사업분야 (biz_segment.label 3종) ─────────────────────────────────────
# 계열사 태그가 하나도 없을 때. 감시 대상 대부분이 정유·석화라 이 값이 최빈이다.
BIZ_DEFAULT = "에너지·화학"


def biz_hint_of(conn, aff_codes: Sequence[str]) -> str:
    """계열사 코드 목록 → biz_segment.label 최빈값. 못 정하면 BIZ_DEFAULT."""
    codes = [c for c in (aff_codes or []) if c]
    if not codes:
        return BIZ_DEFAULT
    placeholders = ",".join("?" * len(codes))
    rows = conn.execute(
        f"""SELECT a.code, b.label
            FROM affiliate a JOIN biz_segment b ON b.key = a.biz
            WHERE a.code IN ({placeholders})
            ORDER BY a.sort_order, a.code""",
        tuple(codes),
    ).fetchall()
    labels = [r["label"] if hasattr(r, "keys") else r[1] for r in rows]
    if not labels:
        return BIZ_DEFAULT
    counts = Counter(labels)
    top = max(counts.values())
    # 동점이면 affiliate.sort_order 가 앞선 계열사의 사업분야를 택한다(labels 는 그 순서다).
    for label in labels:
        if counts[label] == top:
            return label
    return BIZ_DEFAULT


# ── 근거 등급 ───────────────────────────────────────────────────────────
GRADE_FULL = "원문 확보"
GRADE_SUMMARY = "요약문"
GRADE_TITLE = "제목만"
# 높은 등급부터. ingest 의 강등 방지 가드와 소스별 등급표가 이 목록만 본다.
GRADES = (GRADE_FULL, GRADE_SUMMARY, GRADE_TITLE)
_GRADE_FULL_CHARS = 1_000


def evidence_grade_of(body_len: int) -> str:
    """LLM 에 실제로 들어간 본문 길이 → 근거 등급."""
    n = int(body_len or 0)
    if n >= _GRADE_FULL_CHARS:
        return GRADE_FULL
    if n >= 1:
        return GRADE_SUMMARY
    return GRADE_TITLE


# ── 제목 정리 ───────────────────────────────────────────────────────────
# Google News RSS 제목은 실측 41/41 이 ' - 매체명' 으로 끝난다.
_DASHES = ("-", "–", "—")


def strip_outlet_suffix(title: str, publisher: str = "") -> str:
    """제목 끝의 ' - 매체명' 접미사를 제거한다. 매체명이 없거나 안 맞으면 원본 유지."""
    t = (title or "").strip()
    pub = (publisher or "").strip()
    if not t or not pub:
        return t
    for dash in _DASHES:
        suffix = f" {dash} {pub}"
        if t.endswith(suffix):
            return t[: -len(suffix)].strip()
    return t
