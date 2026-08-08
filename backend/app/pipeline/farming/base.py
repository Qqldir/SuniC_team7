"""파밍 공통 타입 · rate limit."""
import time
from dataclasses import dataclass, field
from typing import List

# RawDoc 내부 분류값. feed_item.kind 는 ingest 에서 화면 축 6종으로 변환된다
# (classify.kind_of 참고). feed_id 접두어가 이 값에 의존하므로 바꾸지 말 것.
KIND_ADHOC = "adhoc"        # DART 수시(주요사항)
KIND_PERIODIC = "periodic"  # DART 정기
KIND_SEC = "sec"            # SEC EDGAR
KIND_NEWS = "news"          # 뉴스

# ── rate limit (요청 간 최소 간격, 초) ──
# SEC: 초당 10건 초과 시 약 10분 IP 차단 → 여유 있게 0.15
# DART: 일 20,000건 한도. 초당 제한은 명시 없으나 예의상 0.1
SEC_SLEEP = 0.15
DART_SLEEP = 0.10
NEWS_SLEEP = 0.20


def polite(seconds: float) -> None:
    """소스별 rate limit 준수용 sleep."""
    time.sleep(seconds)


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
    # 매체·발행처 (연합뉴스 / SEC EDGAR / DART). 발표 주체(source)가 아니다.
    # 기본값이 있는 필드는 반드시 non-default 필드 뒤에 와야 한다(dataclass 제약).
    publisher: str = ""
    url: str = ""
    body: str = ""                    # 본문/요약 원문 (있으면)
    tags: List[str] = field(default_factory=list)  # 관련 SK 계열사 코드
    # 소스별 원문 재조회에 필요한 값 (SEC: cik/doc 등). DB 에는 적재되지 않습니다.
    meta: dict = field(default_factory=dict)

    @property
    def feed_id(self) -> str:
        """feed_item.id — 소스 접두어 + 고유 id (재크롤 시 중복 방지)."""
        prefix = {KIND_SEC: "sec", KIND_NEWS: "news"}.get(self.kind, "dart")
        return f"{prefix}-{self.ext_id}"


def source_of(doc: RawDoc) -> str:
    """feed_id 접두어로 소스(dart|sec|news)를 판별.

    crawler(원문 확보 통계)와 ingest(정제 통계)가 **같은 기준**으로 소스를 세야
    운영 요약표의 두 열이 서로 맞는다. 그래서 한쪽에 두지 않고 여기에 둔다.
    """
    return doc.feed_id.split("-", 1)[0]


# ── 원문 미확보 사유 코드 ────────────────────────────────────────────────
# 크롤 로그 끝의 요약표가 쓰는 축이다. 운영자가 "무엇이 왜 빠졌는가" 를 읽어야 하므로
# 소스 모듈은 본문 확보에 실패하면 doc.meta['body_reason'] 에 이 중 하나를 남긴다.
REASON_QUOTA = "한도밖"        # 소스별 상한에 걸려 시도조차 못 함 (--with-docs 를 올리면 회수된다)
REASON_SKIP = "시도안함"       # 페이월·CSR·봇차단으로 확인된 곳 — 요청 자체를 하지 않는다
REASON_RESOLVE = "링크해석실패"  # Google News 토큰에서 원본 URL 을 얻지 못함
REASON_ROBOTS = "robots금지"
REASON_REQUEST = "요청실패"     # HTTP 오류·타임아웃 (403 봇차단 포함)
REASON_EXTRACT = "본문없음"     # 요청은 됐으나 추출 결과가 문턱 미만 (페이월·JS 렌더링)
REASON_ERROR = "오류"          # 그 밖의 예외
