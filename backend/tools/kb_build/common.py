"""KB 빌드 공용 유틸 — 토큰 추정, 헤딩 파싱, 슬러그, frontmatter I/O.

원본 md 를 안전하게 다루기 위한 최소 도구만 둡니다. 특히 헤딩 파싱은
**펜스 코드블록 안의 `#` 를 헤딩으로 오인하지 않는 것**이 핵심입니다.
DB_SK_ON 은 ```yaml 블록을 대량으로 쓰기 때문에 이걸 놓치면 분할이 깨집니다.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, List, Optional

# ── 토큰 추정 ────────────────────────────────────────────────────────────
# 정확한 토크나이저 없이 예산을 잡기 위한 근사치. 한글은 글자당 ~1.15 토큰,
# 라틴/숫자/기호는 ~3.6자당 1 토큰으로 계산합니다. 실측 대비 ±15% 수준이며
# 상한 판정용으로는 충분합니다. (과소추정이 위험하므로 보수적으로 잡음)
_HANGUL = re.compile(r"[가-힣㄰-㆏]")


def est_tokens(text: str) -> int:
    if not text:
        return 0
    ko = len(_HANGUL.findall(text))
    rest = len(text) - ko
    return int(ko * 1.15 + rest / 3.6)


# ── 헤딩 파싱 ────────────────────────────────────────────────────────────

_FENCE = re.compile(r"^\s*(```|~~~)")
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def iter_lines_outside_fence(lines: List[str]) -> Iterator[tuple[int, str]]:
    """펜스 코드블록 바깥의 (인덱스, 줄) 만 흘려보낸다."""
    fence: Optional[str] = None
    for i, line in enumerate(lines):
        m = _FENCE.match(line)
        if m:
            tok = m.group(1)
            if fence is None:
                fence = tok
            elif fence == tok:
                fence = None
            continue
        if fence is None:
            yield i, line


@dataclass
class Heading:
    level: int
    text: str
    line: int          # 0-based


def parse_headings(text: str) -> List[Heading]:
    lines = text.splitlines()
    out: List[Heading] = []
    for i, line in iter_lines_outside_fence(lines):
        m = _HEADING.match(line)
        if m:
            out.append(Heading(len(m.group(1)), m.group(2).strip(), i))
    return out


# ── 슬러그 / ID ──────────────────────────────────────────────────────────

# 한글을 로마자로 바꾸지 않고 그대로 둡니다. 에이전트도 사용자도 한국어로
# 질의하므로, 로마자화는 정보만 잃고 검색 재현율을 떨어뜨립니다.
_SLUG_DROP = re.compile(r"[^\w가-힣\-]+", re.UNICODE)
_SLUG_SQUEEZE = re.compile(r"-{2,}")
# 헤딩 앞머리의 번호/코드: "D06-04.", "1.1", "## 8.15", "SRC-SKON-D04-001 —"
_LEAD_NUM = re.compile(r"^(?:[A-Z]{1,6}\d*[-–]\w+[.)]?|\d+(?:\.\d+)*[.)]?)\s*[—–\-|｜]?\s*")


def slugify(text: str, max_len: int = 48) -> str:
    s = unicodedata.normalize("NFC", text).strip()
    s = s.replace("｜", " ").replace("·", "-").replace("—", "-").replace("–", "-")
    s = _SLUG_DROP.sub("-", s).strip("-").lower()
    s = _SLUG_SQUEEZE.sub("-", s)
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"


def strip_lead_number(title: str) -> str:
    """헤딩에서 앞 번호를 떼어낸 표시용 제목. 원문 번호는 section_no 로 따로 보관."""
    return _LEAD_NUM.sub("", title).strip() or title.strip()


_SECTION_NO = re.compile(r"^([A-Z]{1,6}\d*[-–][\w.]+|\d+(?:\.\d+)*)")


def section_no(title: str) -> str:
    m = _SECTION_NO.match(title.strip())
    return m.group(1).replace("–", "-") if m else ""


# ── frontmatter ─────────────────────────────────────────────────────────

_FM = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def split_frontmatter(text: str) -> tuple[str, str]:
    """(frontmatter 본문, 나머지). frontmatter 가 없으면 ("", 원문)."""
    m = _FM.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def _fm_scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if v is None:
        return "null"
    s = str(v)
    # 콜론·따옴표·선행 특수문자가 있으면 인용. YAML 파서 호환을 위한 최소 처리.
    if s == "" or re.search(r'[:#\[\]{}",]|^[\s\-&*!|>%@`]', s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def dump_frontmatter(meta: dict) -> str:
    """빌드 산출물용 최소 YAML 직렬화 (스칼라 + 문자열 리스트만 지원)."""
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, (list, tuple)):
            lines.append(f"{k}: [{', '.join(_fm_scalar(x) for x in v)}]")
        else:
            lines.append(f"{k}: {_fm_scalar(v)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def load_frontmatter(text: str) -> dict:
    """dump_frontmatter 가 쓴 형식을 되읽는다 (외부 YAML 의존 없이)."""
    raw, _ = split_frontmatter(text)
    meta: dict = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            meta[k] = [x.strip().strip('"') for x in inner.split(",")] if inner else []
        else:
            meta[k] = v.strip('"')
    return meta


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# ── 도메인 맵 (D00-01 Domain Master 기준) ────────────────────────────────
# tags 의 두 번째 값(주제 태그)과 INDEX 의 그룹 제목으로 씁니다.

DOMAIN_THEME = {
    "D00": ("governance", "소스·엔티티·ID·변경이력 마스터"),
    "D01": ("identity", "기업 기본정보·법인구조·연혁"),
    "D02": ("business", "사업 포트폴리오"),
    "D03": ("product", "제품·솔루션"),
    "D04": ("technology", "기술 분류체계·핵심기술 마스터"),
    "D05": ("rnd", "R&D·특허·지식재산"),
    "D06": ("process", "제조공정·운영"),
    "D07": ("footprint", "생산거점·캐파"),
    "D08": ("supply-chain", "원소재·공급사·공급망"),
    "D09": ("customer", "고객·수주·OEM 관계"),
    "D10": ("market", "시장·경쟁·산업동향"),
    "D11": ("cost", "원가·수익성·비즈니스 이코노믹스"),
    "D12": ("capex", "CAPEX·투자·자금조달"),
    "D13": ("contract", "계약·JV·거버넌스·파트너십"),
    "D14": ("policy", "정책·규제·인센티브·컴플라이언스"),
    "D15": ("risk", "전사 리스크·품질·안전·회복탄력성"),
    "D16": ("ecosystem", "외부 솔루션·스타트업·벤더 생태계"),
    "D17": ("oi-portfolio", "오픈이노베이션 과제 포트폴리오·AI 추천"),
}

DOMAIN_RE = re.compile(r"_?(D\d{2})_")


def domain_of(filename: str) -> str:
    m = DOMAIN_RE.search(filename)
    return m.group(1) if m else "D??"


@dataclass
class Segment:
    """분할 산출 단위 — 계층 2 문서 하나가 될 후보."""
    domain: str
    path: List[str]            # 헤딩 경로 (상위 → 자신), 번호 제거
    path_raw: List[str]        # 같은 경로의 원문 헤딩 (번호 포함) — section_no 추출용
    title: str                 # 표시용 제목 (번호 제거)
    section_no: str
    body: str                  # 헤딩 줄 포함한 본문
    part: int = 1              # 원본 파일이 여러 구간으로 이어붙은 경우
    split_of: int = 0          # 크기 초과로 다시 쪼갠 경우 1-based 순번 (0 = 미분할)
    split_total: int = 0
    tags: List[str] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)
    entities: List[str] = field(default_factory=list)
    refs: List[str] = field(default_factory=list)

    @property
    def tokens(self) -> int:
        return est_tokens(self.body)
