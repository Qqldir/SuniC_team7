"""S0. 구조 프로파일링 — 파일별 분할 레벨을 자동 결정한다.

전략 §3.1 은 "기존 md 의 H2 단위"로 분할하라고 하지만, DB_SK_ON 은 파일마다
헤딩 사용법이 다릅니다.

    D08~D17 : H2 가 도메인 섹션 (파일당 11~17개)      → H2 가 주제 단위
    D03~D07 : H1 이 주제, H2 는 레코드 마커 (최대 356개) → H1 이 주제 단위

레벨을 고정하면 한쪽은 통째로 4,000 토큰을 넘고 다른 쪽은 파편화됩니다.
그래서 레벨별로 "목표 구간(500~2,000 토큰)에 얼마나 들어맞는가"를 채점해
파일마다 최적 레벨을 고릅니다.

    python -m tools.kb_build.profile [--src DIR] [--json OUT]
"""
from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path
from typing import Dict, List

from tools.kb_build.common import (
    Heading, domain_of, est_tokens, parse_headings, read_text,
)

TARGET_LO, TARGET_HI = 500, 2_000     # 전략 §3.1 목표 크기
HARD_MAX = 4_000                      # 전략 §3.1 최대 허용


def _sections_at(text: str, headings: List[Heading], level: int) -> List[int]:
    """지정 레벨로 잘랐을 때 각 구간의 추정 토큰 수."""
    lines = text.splitlines()
    starts = [h.line for h in headings if h.level == level]
    if not starts:
        return []
    bounds = starts + [len(lines)]
    return [
        est_tokens("\n".join(lines[bounds[i]:bounds[i + 1]]))
        for i in range(len(starts))
    ]


def _score(sizes: List[int]) -> float:
    """목표 구간 적합도 0~1. 상한 초과는 강하게 감점한다.

    상한 초과 섹션은 재분할로 구제할 수 있지만 그때 문맥이 상하므로,
    애초에 초과가 적은 레벨을 고르는 편이 낫습니다.
    """
    if not sizes:
        return 0.0
    in_target = sum(1 for s in sizes if TARGET_LO <= s <= TARGET_HI)
    over = sum(1 for s in sizes if s > HARD_MAX)
    tiny = sum(1 for s in sizes if s < 200)
    n = len(sizes)
    return (in_target - 1.5 * over - 0.5 * tiny) / n


def detect_parts(headings: List[Heading]) -> int:
    """이어붙은 구간 수. 같은 H1 제목이 반복되면 파일이 여러 파트다."""
    h1 = [h.text for h in headings if h.level == 1]
    if not h1:
        return 1
    return max(1, h1.count(h1[0]))


def profile_file(path: Path) -> Dict:
    text = read_text(path)
    headings = parse_headings(text)
    per_level = {}
    for lv in (1, 2, 3):
        sizes = _sections_at(text, headings, lv)
        if not sizes:
            continue
        per_level[lv] = {
            "count": len(sizes),
            "median": int(statistics.median(sizes)),
            "p90": int(sorted(sizes)[int(len(sizes) * 0.9)]) if sizes else 0,
            "over_hard_max": sum(1 for s in sizes if s > HARD_MAX),
            "score": round(_score(sizes), 3),
        }

    best = max(per_level, key=lambda lv: per_level[lv]["score"]) if per_level else 2
    return {
        "file": path.name,
        "domain": domain_of(path.name),
        "chars": len(text),
        "est_tokens": est_tokens(text),
        "parts": detect_parts(headings),
        "levels": per_level,
        "split_level": best,
        # 상한 초과분은 split 단계에서 한 단계 더 깊은 레벨로 재분할한다.
        "subsplit_level": best + 1 if (best + 1) in per_level else None,
    }


def run(src: Path) -> List[Dict]:
    files = sorted(p for p in src.glob("*.md") if not p.name.endswith(".docx"))
    return [profile_file(p) for p in files]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="../DB_SK_ON", type=Path)
    ap.add_argument("--json", type=Path, default=None)
    args = ap.parse_args()

    reports = run(args.src)
    total = sum(r["est_tokens"] for r in reports)

    print(f"{'file':<34} {'tok':>8} {'part':>4} {'lv':>3} {'n':>5} {'med':>6} {'>4k':>4}")
    print("-" * 70)
    for r in reports:
        lv = r["split_level"]
        info = r["levels"].get(lv, {})
        print(f"{r['domain'] + ' ' + r['file'][6:38]:<34} {r['est_tokens']:>8,} "
              f"{r['parts']:>4} {'H' + str(lv):>3} {info.get('count', 0):>5} "
              f"{info.get('median', 0):>6,} {info.get('over_hard_max', 0):>4}")
    print("-" * 70)
    print(f"{'TOTAL':<34} {total:>8,}")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n→ {args.json}")


if __name__ == "__main__":
    main()
