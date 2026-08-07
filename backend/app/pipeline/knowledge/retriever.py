"""기업 지식 베이스 조회 — search_docs / read_doc / list_docs 의 구현부.

이 파일과 tools/kb_build/* 의 '전략 §x.y' 는 docs/llm-agent-knowledge-strategy.md 의
절 번호다.

전략 §4.1 의 2단계 분리를 그대로 따른다.

    search_docs  요약만 반환 (본문 없음)  → 에이전트가 무엇을 열지 고른다
    read_doc     지정 문서의 전문 또는 한 섹션만 반환

전략 §5 권고대로 **파일 탐색형**으로 먼저 구현한다. 임베딩 인프라(청킹 전략,
모델 선택, 벡터 DB 운영, 재색인) 없이 manifest 의 title·summary·keywords·tags 를
BM25 유사 가중 점수로 훑는다. 문서 742건 규모에서는 이 편이 더 정확한 경우가 많고,
검색 실패 로그가 쌓인 뒤에 하이브리드로 올리면 된다.

지식 베이스는 `knowledge/<회사코드>/` 에 회사별로 나란히 놓인다. 현재 SKO(SK온)와
SKES(SK E&S)가 올라가 있고, 계열사를 늘려도 이 파일은 바뀌지 않는다
— 빌드(`tools/kb_build`)가 디렉터리를 하나 더 만들 뿐이다. `available()` 참고.
"""
from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Optional

from app.config import BASE_DIR

KB_ROOT = Path(BASE_DIR) / "knowledge"

# 필드별 가중치 — 제목·키워드 일치가 본문 언급보다 강한 신호다.
W_TITLE, W_KEYWORD, W_SUMMARY, W_TAG, W_ID = 6.0, 4.0, 2.5, 2.0, 3.0
SNIPPET_CHARS = 220

_TOKEN = re.compile(r"[0-9A-Za-z]+|[가-힣]{2,}")


def _terms(text: str) -> List[str]:
    return [t.lower() for t in _TOKEN.findall(text or "")]


@dataclass
class Hit:
    id: str
    title: str
    summary: str
    domain: str
    shelf: str
    tags: List[str]
    tokens: int
    score: float
    matched: str = ""

    def as_dict(self) -> Dict:
        return {
            "id": self.id, "title": self.title, "summary": self.summary,
            "domain": self.domain, "shelf": self.shelf, "tags": self.tags,
            "tokens": self.tokens, "matched_snippet": self.matched,
        }


@dataclass
class KnowledgeBase:
    company: str
    root: Path
    manifest: List[Dict] = field(default_factory=list)
    bodies: Dict[str, str] = field(default_factory=dict)
    postings: Dict[str, Dict[str, int]] = field(default_factory=dict)
    doc_len: Dict[str, int] = field(default_factory=dict)
    avg_len: float = 1.0

    @property
    def by_id(self) -> Dict[str, Dict]:
        return {d["id"]: d for d in self.manifest}


def available() -> List[str]:
    """빌드가 끝난 회사 코드 목록. 디렉터리가 곧 등록이다."""
    if not KB_ROOT.exists():
        return []
    return sorted(p.name for p in KB_ROOT.iterdir() if (p / "manifest.json").exists())


@lru_cache(maxsize=8)
def load(company: str = "SKO") -> KnowledgeBase:
    """회사 코드로 지식 베이스를 로드한다. 프로세스 수명 동안 캐시된다.

    본문 역색인을 메모리에 올린다. 문서 742건 / 약 2MB 규모라 부담이 없고,
    이게 없으면 제목이 영문인 문서를 한국어로 질의할 때 전부 놓친다
    (예: "수율" → `Yield-to-Margin Causal AI`).
    """
    root = KB_ROOT / company
    path = root / "manifest.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{company} 지식 베이스가 없습니다 ({path}). "
            f"`python -m tools.kb_build.run --out knowledge/{company}` 로 먼저 빌드하세요."
        )
    manifest = json.loads(path.read_text(encoding="utf-8"))

    bodies: Dict[str, str] = {}
    postings: Dict[str, Dict[str, int]] = {}
    doc_len: Dict[str, int] = {}
    for doc in manifest:
        text = (root / doc["path"]).read_text(encoding="utf-8")
        _, _, rest = text.partition("---\n")
        _, _, body = rest.partition("---\n")
        body = body.strip()
        bodies[doc["id"]] = body

        terms = _terms(body)
        doc_len[doc["id"]] = len(terms) or 1
        for t in set(terms):
            postings.setdefault(t, {})[doc["id"]] = terms.count(t)

    avg = sum(doc_len.values()) / max(len(doc_len), 1)
    return KnowledgeBase(company, root, manifest, bodies, postings, doc_len, avg)


# ★ INDEX.md·core/*.md 전문을 통째로 돌려주는 함수를 만들지 마라 — SKO INDEX.md 하나가
#   프롬프트 예산 OI_RAG_TOTAL_TOKENS 를 혼자 넘긴다. 발굴 프롬프트에 내부 지식을 싣는
#   경로는 prefetch._kb_blocks 뿐이고, 그쪽은 seeds()/search_docs() 로 **골라 뽑은 발췌**를 쓴다.
#   ★ seeds() · list_docs() · search_docs 의 shelf/tags 인자는 지우지 마라 — 계열사가
#     늘어날 때 서가·태그로 좁히는 진입점이다.


# ── search_docs ─────────────────────────────────────────────────────────

BM25_K1, BM25_B = 1.4, 0.72


def _score(kb: KnowledgeBase, doc: Dict, terms: List[str]) -> float:
    """메타데이터 가중 일치 + 본문 BM25."""
    if not terms:
        return 0.0
    doc_id = doc["id"]
    title = " ".join(_terms(doc["title"]))
    summary = " ".join(_terms(doc.get("summary") or ""))
    keywords = " ".join(_terms(" ".join(doc.get("keywords") or [])))
    tags = " ".join(_terms(" ".join(doc.get("tags") or [])))

    total = 0.0
    n_docs = len(kb.manifest)
    for t in terms:
        if t in doc_id.lower():
            total += W_ID
        if t in title:
            total += W_TITLE
        if t in keywords:
            total += W_KEYWORD
        if t in summary:
            total += W_SUMMARY
        if t in tags:
            total += W_TAG

        # 본문 BM25 — 흔한 용어("배터리")는 idf 로 자동 감점된다.
        post = kb.postings.get(t)
        if not post:
            continue
        tf = post.get(doc_id, 0)
        if not tf:
            continue
        idf = math.log(1 + (n_docs - len(post) + 0.5) / (len(post) + 0.5))
        norm = 1 - BM25_B + BM25_B * kb.doc_len[doc_id] / kb.avg_len
        total += idf * (tf * (BM25_K1 + 1)) / (tf + BM25_K1 * norm)
    return total


def search_docs(
    query: str,
    tags: Optional[List[str]] = None,
    shelf: Optional[str] = None,
    top_k: int = 5,
    company: str = "SKO",
) -> List[Dict]:
    """요약만 반환한다. 본문은 read_doc 으로만 열린다 (전략 §4.1)."""
    kb = load(company)
    terms = _terms(query)
    want = {t.lower() for t in (tags or [])}

    scored: List[Hit] = []
    for doc in kb.manifest:
        if shelf and doc["shelf"] != shelf:
            continue
        if want and not want.issubset({t.lower() for t in doc["tags"]}):
            continue
        s = _score(kb, doc, terms)
        if s <= 0:
            continue
        scored.append(Hit(
            id=doc["id"], title=doc["title"],
            summary=doc.get("summary") or doc["title"],
            domain=doc["domain"], shelf=doc["shelf"], tags=doc["tags"],
            tokens=doc["tokens"], score=s,
        ))

    scored.sort(key=lambda h: -h.score)
    top = scored[:top_k]
    for hit in top:
        hit.matched = _snippet(kb, hit.id, terms)
    return [h.as_dict() for h in top]


def _snippet(kb: KnowledgeBase, doc_id: str, terms: List[str]) -> str:
    """질의어가 처음 나오는 지점의 앞뒤 한두 문장. 본문 유출을 막으려 짧게 자른다."""
    body = _body(kb, doc_id)
    low = body.lower()
    for t in terms:
        i = low.find(t)
        if i != -1:
            start = max(0, i - SNIPPET_CHARS // 3)
            return " ".join(body[start:start + SNIPPET_CHARS].split())
    return " ".join(body[:SNIPPET_CHARS].split())


# ── read_doc ────────────────────────────────────────────────────────────

def _body(kb: KnowledgeBase, doc_id: str) -> str:
    return kb.bodies.get(doc_id, "")


def read_doc(doc_id: str, section: Optional[str] = None, company: str = "SKO") -> str:
    """문서 전문, 또는 지정한 헤딩 섹션만 반환한다."""
    kb = load(company)
    doc = kb.by_id.get(doc_id)
    if not doc:
        return f"[오류] 문서 id `{doc_id}` 가 존재하지 않습니다. INDEX 나 search_docs 의 id 만 유효합니다."

    body = _body(kb, doc_id)
    header = f"# {doc['title']}\n> {doc['domain']} · {doc.get('breadcrumb') or '-'}\n\n"

    if not section:
        return header + body

    want = section.strip().lower()
    lines, buf, hit, level = body.splitlines(), [], False, 0
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if hit and len(m.group(1)) <= level:
                break
            if want in m.group(2).strip().lower():
                hit, level = True, len(m.group(1))
        if hit:
            buf.append(line)
    if not buf:
        return (f"[오류] `{doc_id}` 에 '{section}' 섹션이 없습니다. "
                f"section 없이 호출하면 전문을 반환합니다.")
    return header + "\n".join(buf).strip()


# ── list_docs ───────────────────────────────────────────────────────────

def list_docs(
    domain: Optional[str] = None,
    section: Optional[str] = None,
    shelf: Optional[str] = None,
    company: str = "SKO",
) -> List[Dict]:
    """도메인·절로 문서 목록을 훑는다. 검색어가 안 떠오를 때의 진입로."""
    kb = load(company)
    out = []
    for doc in kb.manifest:
        if domain and doc["domain"].upper() != domain.upper():
            continue
        if section and not (doc.get("section") or "").upper().startswith(section.upper()):
            continue
        if shelf and doc["shelf"] != shelf:
            continue
        out.append({
            "id": doc["id"], "title": doc["title"],
            "summary": doc.get("summary") or doc["title"],
            "section": doc.get("section", ""), "tokens": doc["tokens"],
            "shelf": doc["shelf"],
        })
    return sorted(out, key=lambda d: d["id"])


def seeds(company: str = "SKO") -> List[Dict]:
    """과제 시드 전량 — 과제 발굴 agent 의 1차 소비 대상."""
    return list_docs(shelf="seeds", company=company)
