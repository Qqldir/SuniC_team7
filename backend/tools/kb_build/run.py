"""KB 빌드 오케스트레이터 — 전 단계를 순서대로 실행한다.

    S0 profile      파일별 분할 레벨 결정 (H1/H2/H3 자동 선택)
    S1 restructure  분할 + 결정적 frontmatter → build/segments/<회사>
    S2 build_index  계층 0(core/) · 계층 1(INDEX.md) 생성 → knowledge/<회사>
    S3 enrich       summary · keywords LLM 보강 (선택, 폴백 있음)
    S4 validate     원문 커버리지 + 전략 §3.6 점검

`--skip-enrich` 로 LLM 없이 끝까지 돌릴 수 있다. 그때 summary 는 빈 값으로 남고
validate 가 WARN 으로 보고한다 — 실패가 아니라 다음에 할 일이다.

대상 회사는 코드 하나로 고른다. 원본 경로·id 접두사·계층 0 스텁은
`companies.py` 의 프로파일에서 온다 (계열사 추가 시 손대는 유일한 파일).

    python -m tools.kb_build.run --company SKO      # SK온
    python -m tools.kb_build.run --company SKES     # SK E&S
    python -m tools.kb_build.run --company SKES --skip-enrich   # LLM 없이
"""
from __future__ import annotations

import argparse
from pathlib import Path

from tools.kb_build import (
    build_index, companies, enrich, profile, restructure, validate,
)
from tools.kb_build.common import est_tokens


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--src", type=Path, default=None, help="기본: 회사 프로파일의 원본 경로")
    ap.add_argument("--work", type=Path, default=None, help="기본: build/segments/<코드>")
    ap.add_argument("--out", type=Path, default=None, help="기본: knowledge/<코드>")
    ap.add_argument("--updated", default=None, help="기본: 회사 프로파일의 원본 기준일")
    ap.add_argument("--skip-enrich", action="store_true")
    ap.add_argument("--enrich-limit", type=int, default=None)
    args = ap.parse_args()

    company = companies.get(args.company)
    # 산출물은 회사별로 완전히 분리한다. 중간 산출(build/segments)까지 나누지 않으면
    # build_index 의 copytree 가 다른 회사 문서를 그대로 옮겨 담는다.
    args.src = args.src or company.src
    args.work = args.work or Path("build/segments") / company.code
    args.out = args.out or Path("knowledge") / company.code
    args.updated = args.updated or company.updated
    print(f"대상: {company.name} ({company.code}) · {args.src} → {args.out}\n")

    print("── S0 구조 프로파일링 ─────────────────────────────")
    reports = profile.run(args.src)
    for r in reports:
        lv = r["split_level"]
        print(f"  {r['domain']}  H{lv}  {r['levels'].get(lv, {}).get('count', 0):>3}절  "
              f"{r['est_tokens']:>7,} 토큰" + (f"  파트 {r['parts']}" if r["parts"] > 1 else ""))

    print("\n── S1 분할 + 메타 추출 ────────────────────────────")
    manifest = restructure.run(args.src, args.work, args.updated, company)
    toks = [m["tokens"] for m in manifest]
    seeds = sum(1 for m in manifest if m["shelf"] == "seeds")
    print(f"  문서 {len(manifest)}건 (seeds {seeds} / docs {len(manifest) - seeds})")
    print(f"  토큰 중앙값 {sorted(toks)[len(toks) // 2]:,} · 최대 {max(toks):,}")

    print("\n── S2 계층 0/1 생성 ───────────────────────────────")
    r = build_index.run(args.work, args.out, company)
    print(f"  INDEX.md   {r['index_tokens']:>7,} 토큰")
    print(f"  core/      {r['core_total']:>7,} 토큰")
    print(f"  docs+seeds {r['body_tokens']:>7,} 토큰 (온디맨드)")

    if args.skip_enrich:
        print("\n── S3 LLM 보강 ────────────────────────────────────\n  건너뜀 (--skip-enrich)")
    else:
        print("\n── S3 LLM 보강 ────────────────────────────────────")
        e = enrich.run(args.out, args.enrich_limit, company)
        print(f"  보강 {e['done']}/{e['targets']}건 · 실패 {e['failed']}건")
        if e["done"]:
            # summary 가 인덱스에 실려야 검색 판단이 가능해진다.
            # reindex 는 산출물을 복사하지 않는다 — run() 을 다시 부르면
            # 방금 보강한 문서를 segments 원본으로 덮어쓰게 된다.
            r = build_index.reindex(args.out, company)
            print(f"  INDEX.md 재생성 {r['index_tokens']:,} 토큰")

    print("\n── S4 검증 ────────────────────────────────────────")
    findings = validate.check(args.src, args.out, company)
    errors = [m for s, m in findings if s == "ERROR"]
    warns = [m for s, m in findings if s == "WARN"]
    for m in errors[:20]:
        print(f"  ERROR  {m}")
    for m in warns[:8]:
        print(f"  WARN   {m}")
    if len(warns) > 8:
        print(f"  WARN   … 외 {len(warns) - 8}건")
    print(f"\n  ERROR {len(errors)} · WARN {len(warns)}")
    print(f"\n완료 → {args.out}")


if __name__ == "__main__":
    main()
