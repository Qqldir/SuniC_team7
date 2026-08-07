"""자료 손실 검증 — 원문의 모든 줄이 산출물에 남아 있는지 대조한다.

재구조화에서 가장 위험한 실패는 조용한 누락이다. 분할 기준 헤딩보다 앞에 있는
서두, 필터에 걸린 구간, 재분할 과정에서 흘린 블록은 전부 오류 없이 사라진다.
그래서 토큰 수가 아니라 **줄 단위 커버리지**를 신뢰의 기준으로 삼는다.

원문 줄을 정규화해 멀티셋으로 만들고, 산출 문서 전체의 줄 멀티셋과 비교한다.
(분할 시 헤딩·리드 문장이 추가되므로 '추가'는 정상, '누락'만 문제다.)

    python -m tools.kb_build.coverage --company SKES
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
from typing import Dict, List

from tools.kb_build import companies
from tools.kb_build.common import domain_of, read_text, split_frontmatter
from tools.kb_build.companies import Company


def _norm(line: str) -> str:
    return " ".join(line.split())


def _lines(text: str) -> Counter:
    """의미 있는 줄만 남긴 멀티셋. 공백 차이는 무시한다."""
    return Counter(n for n in (_norm(x) for x in text.splitlines()) if n)


def _built_lines(root: Path, domain: str, lead_prefix: str) -> Counter:
    total: Counter = Counter()
    for path in root.rglob(f"*{domain.lower()}-*.md"):
        _, body = split_frontmatter(read_text(path))
        # 빌드가 덧붙인 리드 인용문은 대조 대상에서 뺀다.
        body = "\n".join(l for l in body.splitlines() if not l.startswith(lead_prefix))
        total += _lines(body)
    return total


def audit(src: Path, out: Path, company: Company) -> List[Dict]:
    rows = []
    for path in sorted(p for p in src.glob("*.md") if not p.name.endswith(".docx")):
        domain = domain_of(path.name)
        original = _lines(read_text(path))
        built = _built_lines(out, domain, company.lead_prefix)

        missing = original - built          # 원문에 있는데 산출물에 없는 줄
        n_orig = sum(original.values())
        n_miss = sum(missing.values())
        rows.append({
            "file": path.name,
            "domain": domain,
            "lines": n_orig,
            "missing": n_miss,
            "coverage": (n_orig - n_miss) / n_orig if n_orig else 1.0,
            "samples": [l for l, _ in missing.most_common(6)],
        })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--src", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None,
                    help="대조할 산출물 (기본: knowledge/<코드>)")
    ap.add_argument("--show", type=int, default=6, help="누락 줄 예시 출력 개수")
    args = ap.parse_args()

    co = companies.get(args.company)
    rows = audit(args.src or co.src, args.out or Path("knowledge") / co.code, co)
    print(f"{'domain':<7} {'lines':>7} {'missing':>8} {'coverage':>9}")
    print("-" * 36)
    for r in rows:
        flag = "" if r["missing"] == 0 else "  ←"
        print(f"{r['domain']:<7} {r['lines']:>7,} {r['missing']:>8,} "
              f"{r['coverage'] * 100:>8.2f}%{flag}")

    total = sum(r["lines"] for r in rows)
    miss = sum(r["missing"] for r in rows)
    print("-" * 36)
    print(f"{'TOTAL':<7} {total:>7,} {miss:>8,} {(total - miss) / total * 100:>8.2f}%")

    if miss:
        print("\n누락 예시:")
        for r in rows:
            if not r["missing"]:
                continue
            print(f"\n[{r['domain']}] {r['missing']:,}줄 누락")
            for s in r["samples"][:args.show]:
                print(f"    {s[:110]}")


if __name__ == "__main__":
    main()
