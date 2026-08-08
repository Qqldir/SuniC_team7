"""S5. 빌드 검증 — 전략 §3.6 점검 항목 + 자료 손실 검사.

가장 무거운 항목을 맨 앞에 둔다: **원문 커버리지**. 나머지 검사가 모두 통과해도
원문이 빠져 있으면 지식 베이스로서 실패다.

    python -m tools.kb_build.validate --company SKES
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import List, Tuple

from tools.kb_build import companies, coverage as cov
from tools.kb_build.common import (
    est_tokens, load_frontmatter, read_text, split_frontmatter,
)
from tools.kb_build.companies import Company

REQUIRED_FIELDS = ("id", "title", "tags", "updated")
MAX_DOC_TOKENS = 4_000

Finding = Tuple[str, str]          # (severity, message)  severity: ERROR | WARN


def check(src: Path, out: Path, company: Company) -> List[Finding]:
    findings: List[Finding] = []
    manifest = json.loads(read_text(out / "manifest.json"))
    by_id = {d["id"]: d for d in manifest}

    # ── 1. 원문 커버리지 (가장 중요) ────────────────────────────────────
    rows = cov.audit(src, out, company)
    missing = sum(r["missing"] for r in rows)
    if missing:
        for r in rows:
            if r["missing"]:
                findings.append((
                    "ERROR",
                    f"{r['domain']} 원문 {r['missing']:,}줄 누락 "
                    f"(커버리지 {r['coverage'] * 100:.2f}%)",
                ))
    total_lines = sum(r["lines"] for r in rows)

    # ── 2. frontmatter · id ────────────────────────────────────────────
    ids = Counter()
    for entry in manifest:
        path = out / entry["path"]
        if not path.exists():
            findings.append(("ERROR", f"{entry['id']}: 파일 없음 ({entry['path']})"))
            continue
        raw, body = split_frontmatter(read_text(path))
        if not raw:
            findings.append(("ERROR", f"{entry['id']}: frontmatter 없음"))
            continue
        meta = load_frontmatter(read_text(path))
        for field in REQUIRED_FIELDS:
            if not meta.get(field):
                findings.append(("ERROR", f"{entry['id']}: 필수 필드 누락 — {field}"))
        if meta.get("id") != path.stem:
            findings.append((
                "ERROR", f"{entry['id']}: id 와 파일명 불일치 ({path.stem})"))
        ids[entry["id"]] += 1

        # 3. 문서 크기 상한
        tokens = est_tokens(body)
        if tokens > MAX_DOC_TOKENS:
            findings.append((
                "WARN", f"{entry['id']}: {tokens:,} 토큰 — 상한 {MAX_DOC_TOKENS:,} 초과"))

        # 4. summary 품질
        summary = (meta.get("summary") or "").strip()
        if not summary:
            findings.append(("WARN", f"{entry['id']}: summary 비어 있음 (S6 enrich 대상)"))
        elif summary == meta.get("title"):
            findings.append(("WARN", f"{entry['id']}: summary 가 제목 복사본"))

    for doc_id, n in ids.items():
        if n > 1:
            findings.append(("ERROR", f"{doc_id}: id 중복 {n}건"))

    # ── 5. related 끊어진 링크 ─────────────────────────────────────────
    # related 는 원문의 내부 코드(`OI-D08-01`, `TECH-SKON-D04-001`)라 문서 id 와 다르다.
    # 코드에 박힌 도메인이 실제 도메인 집합에 없으면 그 참조는 해석 불가능하다.
    import re as _re

    domains = {d["domain"] for d in manifest}
    ref_domain = _re.compile(r"\b(D\d{2})\b")
    dangling: Counter = Counter()
    for entry in manifest:
        for ref in entry.get("related", []):
            m = ref_domain.search(ref)
            if m and m.group(1) not in domains:
                dangling[ref] += 1
    for ref, n in dangling.most_common(20):
        findings.append(("WARN", f"참조 `{ref}` 의 도메인이 존재하지 않음 ({n}건에서 인용)"))

    # ── 6. 계층 0 / 계층 1 존재 ────────────────────────────────────────
    for required in ("INDEX.md", "core/schema.md", "core/rules.md", "core/glossary.md"):
        if not (out / required).exists():
            findings.append(("ERROR", f"{required} 없음"))

    # ── 7. 시드 선반 ───────────────────────────────────────────────────
    seeds = [d for d in manifest if d["shelf"] == "seeds"]
    if not seeds:
        findings.append(("ERROR", "seeds/ 선반이 비어 있음 — 과제 발굴이 동작하지 않는다"))

    print(f"검사 대상: 문서 {len(manifest):,}건 · 원문 {total_lines:,}줄 · 시드 {len(seeds)}건")
    return findings


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--src", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--max-warn", type=int, default=12, help="WARN 출력 상한")
    args = ap.parse_args()

    co = companies.get(args.company)
    findings = check(args.src or co.src, args.out or Path("knowledge") / co.code, co)
    errors = [m for s, m in findings if s == "ERROR"]
    warns = [m for s, m in findings if s == "WARN"]

    for m in errors:
        print(f"  ERROR  {m}")
    for m in warns[:args.max_warn]:
        print(f"  WARN   {m}")
    if len(warns) > args.max_warn:
        print(f"  WARN   … 외 {len(warns) - args.max_warn}건")

    print(f"\nERROR {len(errors)} · WARN {len(warns)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
