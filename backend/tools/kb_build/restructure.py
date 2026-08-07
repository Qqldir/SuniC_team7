"""S1+S2. 분할 + 결정적 메타 추출.

profile.py 가 고른 레벨로 자르고, 크기를 맞춘 뒤, LLM 없이 뽑을 수 있는
frontmatter 필드를 채웁니다. (summary/keywords 는 S3 enrich 담당)

분할에서 지키는 것 세 가지:

1. **표와 코드블록을 절대 가르지 않는다.** 표 중간을 자르면 헤더 행이 사라져
   남은 조각이 해석 불가능해집니다. 원본 DB 는 정보 대부분이 표에 있습니다.
2. **헤딩 경로를 문서에 남긴다.** H3 로 자른 조각은 상위 H1/H2 문맥이 없으면
   무슨 얘기인지 알 수 없습니다 (전략 §3.3 자기완결성, §5.1 청킹).
3. **작은 형제는 합치고 큰 놈은 더 쪼갠다.** 목표 500~2,000 / 상한 4,000 토큰.

회사별로 달라지는 값(id 접두사·리드 문구·시드 판정)은 companies.py 에서 온다.

    python -m tools.kb_build.restructure --company SKES
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

from tools.kb_build import companies, profile as prof
from tools.kb_build.common import (
    Heading, Segment, domain_of, dump_frontmatter, est_tokens,
    parse_headings, read_text, section_no, slugify, strip_lead_number, write_text,
)
from tools.kb_build.companies import Company

MERGE_BELOW = 300        # 이보다 작은 형제 구간은 앞 구간에 붙인다
HARD_MAX = prof.HARD_MAX


# ── 블록 단위 분해 (표/코드블록 보호) ────────────────────────────────────

def _blocks(lines: List[str]) -> List[List[str]]:
    """줄 목록을 '쪼개면 안 되는 덩어리' 단위로 묶는다."""
    out: List[List[str]] = []
    cur: List[str] = []
    fence: Optional[str] = None
    in_table = False

    def flush():
        nonlocal cur
        if cur:
            out.append(cur)
            cur = []

    for line in lines:
        m = re.match(r"^\s*(```|~~~)", line)
        if m:
            tok = m.group(1)
            if fence is None:
                flush()
                fence, in_table = tok, False
                cur.append(line)
            else:
                cur.append(line)
                if fence == tok:
                    fence = None
                    flush()
            continue
        if fence is not None:
            cur.append(line)
            continue

        is_row = line.lstrip().startswith("|")
        if is_row and not in_table:
            flush()
            in_table = True
        elif in_table and not is_row:
            flush()
            in_table = False
        cur.append(line)
        if not in_table and not line.strip():
            flush()
    flush()
    return out


def _pack(lines: List[str], budget: int) -> List[List[str]]:
    """블록 경계를 지키며 예산 단위로 담는다. 한 블록이 예산을 넘으면 단독으로 둔다."""
    chunks: List[List[str]] = []
    cur: List[str] = []
    used = 0
    for blk in _blocks(lines):
        t = est_tokens("\n".join(blk))
        if cur and used + t > budget:
            chunks.append(cur)
            cur, used = [], 0
        cur.extend(blk)
        used += t
    if cur:
        chunks.append(cur)
    return chunks


# ── 분할 ─────────────────────────────────────────────────────────────────

def _orphans(headings: List[Heading], level: int) -> List[Heading]:
    """분할 레벨의 하위 절을 갖지 않는 상위 절.

    이런 절은 분할 기준에 걸리지 않아 **앞 구간에 통째로 흡수되고, 엉뚱한 제목
    아래로 들어간다.** E&S D04 는 H2 분할인데 `# 5. D04 직접 O/I Seed` 는 H1 이라
    (하위가 H3뿐) 시드 표가 `공통 데이터·OT·SHE` 문서 안에 묻혔다. 자료는 남지만
    검색으로는 영영 안 나온다 — 커버리지 검사에 걸리지 않는 종류의 손실이다.

    같은 레벨이라도 하위 절이 있는 상위 절은 건드리지 않는다. 그건 정상적인
    계층이고, 자르면 내용 없는 껍데기 문서만 늘어난다.
    """
    out = []
    for h in (x for x in headings if x.level < level):
        end = next((x.line for x in headings if x.line > h.line and x.level <= h.level),
                   float("inf"))
        if not any(x.level == level and h.line < x.line < end for x in headings):
            out.append(h)
    return out


def _cut(lines: List[str], headings: List[Heading], level: int,
         rescue_orphans: bool = False) -> List[tuple[Heading, List[str]]]:
    marks = [h for h in headings if h.level == level]
    if rescue_orphans:
        marks = sorted(marks + _orphans(headings, level), key=lambda h: h.line)
    if not marks:
        return []
    bounds = [h.line for h in marks] + [len(lines)]
    return [(marks[i], lines[bounds[i]:bounds[i + 1]]) for i in range(len(marks))]


def _ancestors(headings: List[Heading], h: Heading) -> List[str]:
    """자신보다 얕은 레벨의 가장 가까운 상위 헤딩들 (위 → 아래), 원문 그대로."""
    out: List[str] = []
    seen_level = h.level
    for prev in reversed([x for x in headings if x.line < h.line]):
        if prev.level < seen_level:
            out.append(prev.text)
            seen_level = prev.level
            if seen_level == 1:
                break
    return list(reversed(out))


# 도메인 절 번호: `D08-12`, `D06-04.`, `8.15`. 상위 헤딩에서 물려받는다.
DOMAIN_SECTION = re.compile(r"\b(D\d{2}[-–][\w.]+)")


def _inherited_section(path_raw: List[str]) -> str:
    """헤딩 경로에서 가장 깊은 도메인 절 번호를 가져온다.

    H3 로 자른 조각의 section_no 가 `2`(절 안의 순번)가 되면 쓸모가 없다.
    상위 헤딩의 `D08-12` 를 물려받아야 문서 id 와 인덱스가 해석 가능해진다.
    """
    for raw in reversed(path_raw):
        m = DOMAIN_SECTION.search(raw)
        if m:
            return m.group(1).replace("–", "-")
    for raw in reversed(path_raw):
        no = section_no(raw)
        if no:
            return no
    return ""


def split_file(path: Path, report: Dict, company: Company) -> List[Segment]:
    text = read_text(path)
    lines = text.splitlines()
    headings = parse_headings(text)
    domain = report["domain"]
    level = report["split_level"]
    sub = report.get("subsplit_level")

    # 파일이 여러 파트로 이어붙은 경우(D03~D07), 최상위 H1 반복 위치로 파트를 센다.
    h1s = [h for h in headings if h.level == 1]
    part_starts = [h.line for h in h1s if h1s and h.text == h1s[0].text] if h1s else []

    def part_of(line: int) -> int:
        return sum(1 for s in part_starts if s <= line) or 1

    raw: List[Segment] = []

    cuts = _cut(lines, headings, level, company.rescue_orphan_sections)

    # 첫 분할 지점보다 앞에 있는 서두는 _cut 이 그냥 버린다. 여기에 문서 버전,
    # 기준일, 적용 범위 같은 해석에 필요한 정보가 들어 있어 반드시 살려야 한다.
    # (D04·D08 처럼 분할 레벨이 H3 면 파일 앞부분이 통째로 사라진다.)
    first = cuts[0][0].line if cuts else len(lines)
    preamble = lines[:first]
    if any(l.strip() for l in preamble):
        head_text = next(
            (h.text for h in headings if h.line < first), f"{domain} 문서 서두"
        )
        raw.append(Segment(
            domain=domain,
            path=[strip_lead_number(head_text)],
            path_raw=[head_text],
            title=f"{strip_lead_number(head_text)} — 문서 서두",
            section_no=_inherited_section([head_text]),
            body="\n".join(preamble).strip(),
            part=1,
        ))

    for head, body_lines in cuts:
        title_raw = head.text
        anc = _ancestors(headings, head)
        path_raw = anc + [title_raw]
        raw.append(Segment(
            domain=domain,
            path=[strip_lead_number(x) for x in path_raw],
            path_raw=path_raw,
            title=strip_lead_number(title_raw),
            section_no=_inherited_section(path_raw),
            body="\n".join(body_lines).strip(),
            part=part_of(head.line),
        ))

    file_title = h1s[0].text if h1s else ""
    raw = _absorb_part_headers(raw, file_title)
    raw = _merge_small(raw)
    return _subsplit_large(raw, sub, headings)


def _absorb_part_headers(segs: List[Segment], file_title: str) -> List[Segment]:
    """반복되는 파일 제목 H1(파트 구분자)을 뒤 구간에 흡수시킨다.

    D03~D07 은 여러 파트가 이어붙어 있어 파일 제목 H1 이 최대 10회 반복된다.
    그대로 두면 제목이 같은 껍데기 문서가 파일마다 여러 건 생긴다.
    """
    if not file_title:
        return segs
    out: List[Segment] = []
    carry = ""
    for s in segs:
        if s.path_raw[-1] == file_title:
            carry = (carry + "\n\n" + s.body).strip()
            continue
        if carry:
            s.body = (carry + "\n\n" + s.body).strip()
            carry = ""
        out.append(s)
    if carry and out:
        out[-1].body = (out[-1].body + "\n\n" + carry).strip()
    return out


def _merge_small(segs: List[Segment]) -> List[Segment]:
    """MERGE_BELOW 미만 구간을 직전 구간에 흡수. 단 상한을 넘기지 않는 선에서만."""
    out: List[Segment] = []
    for s in segs:
        if (out and s.tokens < MERGE_BELOW
                and out[-1].part == s.part
                and out[-1].tokens + s.tokens <= HARD_MAX):
            out[-1].body += "\n\n" + s.body
        else:
            out.append(s)
    return out


def _subsplit_large(segs: List[Segment], sub_level: Optional[int],
                    headings: List[Heading]) -> List[Segment]:
    """상한 초과 구간을 한 단계 깊은 헤딩으로, 그래도 넘치면 블록 단위로 쪼갠다."""
    out: List[Segment] = []
    for s in segs:
        if s.tokens <= HARD_MAX:
            out.append(s)
            continue

        lines = s.body.splitlines()
        inner = parse_headings(s.body)
        pieces: List[tuple[str, List[str]]] = []

        deeper = [h for h in inner if h.level > (inner[0].level if inner else 0)]
        if deeper:
            lv = min(h.level for h in deeper)
            head_lines = lines[:min(h.line for h in inner if h.level == lv)]
            cuts = _cut(lines, inner, lv)
            if head_lines:
                pieces.append(("", head_lines))
            pieces += [(strip_lead_number(h.text), bl) for h, bl in cuts]
        else:
            pieces = [("", blk) for blk in _pack(lines, HARD_MAX - 200)]

        # 쪼갠 뒤에도 남는 초과분은 블록 단위로 한 번 더 처리
        flat: List[tuple[str, List[str]]] = []
        for label, bl in pieces:
            if est_tokens("\n".join(bl)) > HARD_MAX:
                flat += [(label, b) for b in _pack(bl, HARD_MAX - 200)]
            else:
                flat.append((label, bl))
        flat = [(lb, bl) for lb, bl in flat if "\n".join(bl).strip()]

        total = len(flat)
        for i, (label, bl) in enumerate(flat, 1):
            sub_title = f"{s.title} — {label}" if label else s.title
            out.append(Segment(
                domain=s.domain,
                path=s.path + ([label] if label else []),
                path_raw=s.path_raw + ([label] if label else []),
                title=sub_title if total > 1 else s.title,
                section_no=s.section_no,
                body="\n".join(bl).strip(),
                part=s.part,
                split_of=i if total > 1 else 0,
                split_total=total if total > 1 else 0,
            ))
    return out


# ── 메타 추출 (LLM 없이) ─────────────────────────────────────────────────

# 문서가 인용하는 내부 ID: `OI-D08-01`, `TECH-SKON-D04-001`, `COMP-SKON-001` …
REF_ID = re.compile(r"`([A-Z][A-Z0-9]{1,7}(?:-[A-Z0-9][A-Z0-9.]*){1,4})`")
DOMAIN_REF = re.compile(r"\bD(0\d|1[0-7])\b")

# 기존 Chunk YAML 블록 — 이미 사람이 정제해 둔 키워드/엔티티를 승계한다.
CHUNK_BLOCK = re.compile(r"```yaml\n(.*?)\n```", re.DOTALL)
YAML_LIST = re.compile(r"^(keywords|entities):\s*\n((?:\s+-\s+.*\n?)+)", re.MULTILINE)

# 과제 발굴 agent 가 직접 소비하는 구간(seeds 선반)의 판정은 회사별 패턴으로 한다
# (companies.py). 원본 DB 마다 절 제목 관례가 다르기 때문이다.
# 판정은 **자기 제목과 바로 위 헤딩까지만** 본다. 경로 전체로 보면 D17 파일은
# 최상위 H1 제목("… Opportunity Portfolio & AI Task Recommendation")에 걸려
# 13개 절이 통째로 seeds 로 빨려 들어간다 — 실제 후보 목록만 남겨야 한다.
#
# 계층 0 승격 후보 — 용어·ID·상태값 정의
CORE_MARKER = re.compile(r"Domain Boundary|Entity Master|ID Governance|Standard|Taxonomy|"
                         r"Classification Rules|Schema|명칭 및 별칭|Data Quality", re.I)
# 원본 집필 과정의 흔적(작업 로그·진행상태). 검색 우선순위만 낮추고 **버리지 않는다** —
# 어느 구간이 어디까지 검증됐는지가 여기에만 적혀 있어 근거 신뢰도 판단에 쓰인다.
LOG_TITLE = re.compile(r"이번 구간 완료|다음 시작점|Completion Check|진행상태|작업 로그", re.I)


def _yaml_lists(body: str) -> tuple[List[str], List[str]]:
    kw: List[str] = []
    ent: List[str] = []
    for block in CHUNK_BLOCK.findall(body):
        for key, items in YAML_LIST.findall(block + "\n"):
            vals = [re.sub(r"^\s*-\s+", "", ln).strip().strip('"')
                    for ln in items.splitlines() if ln.strip()]
            (kw if key == "keywords" else ent).extend(v for v in vals if v)
    return _dedup(kw), _dedup(ent)


def _dedup(xs: List[str]) -> List[str]:
    seen, out = set(), []
    for x in xs:
        if x and x not in seen:
            seen.add(x)
            out.append(x)
    return out


def enrich_meta(seg: Segment, company: Company) -> None:
    theme = company.theme(seg.domain)[0]
    tags = [seg.domain.lower(), theme]

    # 자기 제목 + 바로 위 헤딩까지만 본다. path[0] 은 파일 제목 H1 이라 제외한다
    # (D17 은 파일 제목부터 "Task Recommendation" 이라 전 구간이 seeds 로 빨려간다).
    scope = [seg.title]
    if len(seg.path) >= 3:
        scope.append(seg.path[-2])
    if company.seed_marker.search(" ".join(scope)):
        tags.append("oi-seed")
    if CORE_MARKER.search(seg.title):
        tags.append("core-candidate")
    if LOG_TITLE.search(seg.title):
        tags.append("build-log")
    if "```yaml" in seg.body:
        tags.append("schema")
    if seg.body.count("\n|") >= 6:
        tags.append("table")

    seg.tags = _dedup(tags)
    seg.keywords, seg.entities = _yaml_lists(seg.body)

    refs = _dedup(REF_ID.findall(seg.body))[:24]
    cross = _dedup("D" + m for m in DOMAIN_REF.findall(seg.body) if "D" + m != seg.domain)
    seg.refs = refs
    seg.entities = _dedup(seg.entities)
    seg.tags += [f"xref:{d.lower()}" for d in cross[:4]]


def _priority(tags: List[str]) -> str:
    """critical: 계층 0 승격 후보 · reference: 작업 로그 등 후순위 · normal: 그 외."""
    if "core-candidate" in tags:
        return "critical"
    if "build-log" in tags:
        return "reference"
    return "normal"


def make_id(seg: Segment, taken: set, company: Company) -> str:
    bits = [company.slug, seg.domain.lower()]
    if seg.section_no:
        bits.append(slugify(seg.section_no, 16))
    bits.append(slugify(seg.title, 40))
    base = "-".join(b for b in bits if b)
    if seg.split_of:
        base = f"{base}-{seg.split_of}"
    doc_id, n = base, 2
    while doc_id in taken:
        doc_id = f"{base}-{n}"
        n += 1
    taken.add(doc_id)
    return doc_id


def to_document(seg: Segment, doc_id: str, source_file: str, updated: str,
                company: Company) -> str:
    """frontmatter + 자기완결 헤더 + 본문."""
    breadcrumb = " > ".join(seg.path[:-1])
    meta = {
        "id": doc_id,
        "title": seg.title,
        # summary 는 S3 enrich 가 채운다. 비어 있으면 validate 가 경고한다.
        "summary": "",
        "tags": seg.tags,
        "keywords": seg.keywords,
        "related": seg.refs,
        "priority": _priority(seg.tags),
        "domain": seg.domain,
        "section": seg.section_no,
        "source": source_file,
        "breadcrumb": breadcrumb,
        "tokens": seg.tokens,
        "updated": updated,
    }
    # 전략 §3.3: 조각을 단독으로 읽어도 어느 기업·도메인·상위 절인지 알 수 있어야 한다.
    lead = (
        f"{company.lead_prefix} {seg.domain} {company.theme(seg.domain)[1]}"
        + (f" · {breadcrumb}" if breadcrumb else "")
    )
    return dump_frontmatter(meta) + "\n" + lead + "\n\n" + seg.body.strip() + "\n"


def disambiguate(segs: List[Segment]) -> None:
    """중복 제목에 상위 절을 덧붙여 단독으로 식별 가능하게 만든다.

    원본에는 `## OI Metadata` 가 51개, `## Domain Boundary` 가 11개 있다.
    인덱스에 그대로 실으면 에이전트가 어느 것을 열지 고를 수 없다 (전략 §3.4).
    """
    from collections import Counter

    base = {id(s): s.title for s in segs}
    # 상위 헤딩을 한 단계씩 더 붙여 나가며 유일해질 때까지 (최대 2단계).
    for depth in (1, 2):
        dup = {t for t, n in Counter(s.title for s in segs).items() if n > 1}
        if not dup:
            break
        for s in segs:
            if s.title not in dup:
                continue
            ancestors = [p for p in s.path[1:-1] if p and p != base[id(s)]]
            prefix = ancestors[-depth:] if ancestors else []
            if prefix:
                s.title = " — ".join(prefix + [base[id(s)]])
            elif s.section_no:
                s.title = f"{s.section_no} {base[id(s)]}"

    # 그래도 남는 중복(같은 절 안의 반복 헤딩)은 절 번호 + 순번으로 마무리한다.
    seen: dict = {}
    for s in segs:
        n = seen.get(s.title, 0) + 1
        seen[s.title] = n
        if n > 1:
            s.title = f"{s.title} ({n})"


# ── 실행 ─────────────────────────────────────────────────────────────────

def run(src: Path, out: Path, updated: str, company: Company) -> List[Dict]:
    reports = {r["file"]: r for r in prof.run(src)}
    taken: set = set()
    manifest: List[Dict] = []

    for name, report in reports.items():
        path = src / name
        segs = split_file(path, report, company)
        disambiguate(segs)
        for seg in segs:
            enrich_meta(seg, company)
            doc_id = make_id(seg, taken, company)
            shelf = "seeds" if "oi-seed" in seg.tags else "docs"
            rel = Path(shelf) / seg.domain / f"{doc_id}.md"
            write_text(out / rel, to_document(seg, doc_id, name, updated, company))
            manifest.append({
                "id": doc_id, "path": str(rel), "domain": seg.domain,
                "section": seg.section_no, "title": seg.title,
                "summary": "", "tags": seg.tags, "keywords": seg.keywords,
                "related": seg.refs, "tokens": seg.tokens, "shelf": shelf,
                "priority": _priority(seg.tags),
                "breadcrumb": " > ".join(seg.path[:-1]), "source": name,
            })
    write_text(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--src", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--updated", default=None)
    args = ap.parse_args()

    co = companies.get(args.company)
    man = run(args.src or co.src, args.out or Path("build/segments") / co.code,
              args.updated or co.updated, co)
    toks = [m["tokens"] for m in man]
    seeds = [m for m in man if m["shelf"] == "seeds"]
    print(f"문서 {len(man)}건  (seeds {len(seeds)} / docs {len(man) - len(seeds)})")
    print(f"토큰  합계 {sum(toks):,} · 중앙값 {sorted(toks)[len(toks) // 2]:,} · 최대 {max(toks):,}")
    print(f"상한(4,000) 초과 {sum(1 for t in toks if t > HARD_MAX)}건")
    print(f"→ {args.out}")


if __name__ == "__main__":
    main()
