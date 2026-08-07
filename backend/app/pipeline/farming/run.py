"""파밍 실행 CLI.

    python -m app.pipeline.farming.run                      # 전체 소스 크롤 → DB 적재
    python -m app.pipeline.farming.run --days 14            # 최근 14일
    python -m app.pipeline.farming.run --dry                # 적재 없이 수집 결과만 출력
    python -m app.pipeline.farming.run --source news        # 특정 소스만 (dart|sec|news)
    python -m app.pipeline.farming.run --with-docs 0        # 목록만 (원문 확보 없이)
    python -m app.pipeline.farming.run --no-llm             # LLM 정제 없이 naive 요약

크롤 끝에 소스별 요약표를 찍습니다 — 수집 / 원문 확보 / 정제 / 미확보 사유별 건수.
'한도밖' 으로 빠진 물량은 --with-docs 를 올리면 그대로 회수됩니다.

전문검색(watchlist 밖 기업의 사례 역방향 발굴):
    python -m app.pipeline.farming.run --search "cost reduction program"
"""
import argparse
import time

from app.config import CRAWL_SINCE_DAYS
from app.pipeline.farming import classify, crawler, ingest, sec


def _search(query: str, days: int, limit: int) -> None:
    hits = sec.full_text_search(query, days=days, size=limit)
    print(f"\nEDGAR 전문검색 '{query}' — {len(hits)}건\n")
    for h in hits:
        print(f"  [{h['date']} · {h['form']}] {h['company']}")
        print(f"     {h['id']}")


def main():
    ap = argparse.ArgumentParser(description="O/I Scout 지식 파밍 크롤러")
    ap.add_argument("--days", type=int, default=CRAWL_SINCE_DAYS, help="크롤 대상 기간(일)")
    ap.add_argument("--source", choices=["all", "dart", "sec", "news"], default="all")
    ap.add_argument("--dry", action="store_true", help="DB 적재 없이 수집만")
    ap.add_argument("--limit", type=int, default=10, help="--dry 출력 개수 / 전문검색 결과 개수")
    # 기본값 5 — 원문이 없으면 요약이 제목 복사로 떨어지므로 '평소 크롤' 이 목록만 받는 건
    # 의미가 없다(실측: 56건 중 45건이 요약==제목).
    #
    # 실제 상한은 이 값 × 소스별 BODY_FACTOR 다. 소스마다 원문 확보 비용이 자릿수 단위로
    # 달라서 하나의 숫자에 묶으면 가장 비싼 소스(뉴스)에 맞춰 공시가 통째로 잘린다 —
    # 실제로 --with-docs 6 으로 돌린 프로덕션에서 '제목만' 43건 중 15건이 DART·SEC 였고,
    # 그건 페이월 때문이 아니라 순전히 상한 때문이었다.
    # 기본값 5 에서 실효 상한:  dart 20(×4) · sec 20(×4) · 뉴스 45(×9)
    #   → 실측 목록 크기(dart 14 · sec 12 · 뉴스 43)를 소스마다 전량 덮는다.
    # 근거 수치는 각 모듈의 BODY_FACTOR 주석에 있다.
    #
    # 크롤 1회 소요(2026-08-07 실측, 목록 69건 기준):
    #   목록 조회 17초 + 원문 확보 99초(dart 6.6 · sec 6.3 · 뉴스 약 86) = **1.9분**
    #   여기에 LLM 정제 62건이 붙어 전체 **10.0분**. 정제가 소요의 8할이다(아래 참고).
    #   --with-docs 0 으로 목록만 받으면 0.3분.
    ap.add_argument("--with-docs", type=int, default=5, metavar="N",
                    help="소스별 원문 확보 상한의 기준값 (0=목록만). "
                         "실효 상한은 소스별 배수가 곱해집니다 (dart ×4 · sec ×4 · news ×9)")
    # 기본값 70 — --with-docs 5 가 덮는 목록 전량(실측 69건)보다 커야 한다.
    #
    # 이 값이 확보한 본문 수보다 작으면 **받아 놓고 안 쓴 본문**이 생긴다. 뉴스 본문은
    # 저작물이라 naive_summary 가 저장을 거부하므로(meta['body_restricted']), 정제되지 못한
    # 건은 요약이 비고 ingest 가 근거 등급을 '제목만' 으로 매긴다 — 사실과 맞지만,
    # 상대 서버에 요청까지 해 놓고 결과를 버리는 셈이다.
    # 즉 --with-docs 를 올릴 때는 이 값을 같이 올려야 그 요청이 헛되지 않는다.
    # llm.enrich 는 본문 있는 문서만 정제하므로 이 값이 본문 수를 덮어도 낭비는 없다.
    # 비용 실측: 62건 정제에 8.1분 (codex 호출당 약 23초 · OI_LLM_CONCURRENCY 기본 3 동시).
    # 급할 때는 이 값을 낮추는 것이 --with-docs 를 낮추는 것보다 낫다 — 확보한 본문은
    # 다음 크롤에서 재사용되지 않지만, 이미 정제된 행은 UPSERT 가드가 지켜 준다.
    ap.add_argument("--enrich-limit", type=int, default=70, metavar="N",
                    help="LLM 정제 최대 건수 (비용 통제). --with-docs 로 받은 본문 수 이상이어야 합니다")
    ap.add_argument("--no-llm", action="store_true", help="LLM 정제 없이 naive 요약만")
    ap.add_argument("--search", type=str, default="", metavar="QUERY",
                    help="EDGAR 전문검색만 수행하고 종료")
    args = ap.parse_args()

    if args.search:
        _search(args.search, args.days, args.limit)
        return

    sources = None if args.source == "all" else [args.source]
    started = time.monotonic()
    docs = crawler.crawl_all(args.days, sources=sources)
    listed = time.monotonic() - started
    print(f"\n총 {len(docs)}건 수집 (최근 {args.days}일, 목록 조회 {listed:.0f}초)")

    body_stats = crawler.fetch_bodies(docs, per_source=args.with_docs)
    filled = sum(st.filled for st in body_stats.values())
    print(f"원문 확보 {filled}건 (누적 {time.monotonic() - started:.0f}초)")

    if args.dry:
        print()
        for d in docs[: args.limit]:
            label, axis = classify.kind_of(d)
            print(f"  [{d.published_on} · {d.kind} · {d.source}] {d.title[:60]}")
            print(f"     publisher={d.publisher!r} kind_label={label!r}({axis}) "
                  f"grade={classify.evidence_grade_of(len(d.body))}")
            print(f"     tags={d.tags} body={len(d.body):,}자 url={d.url[:60]}")
        if len(docs) > args.limit:
            print(f"  ... 외 {len(docs) - args.limit}건")
        print("\n■ 원문 확보 요약")
        print(crawler.format_report(body_stats))
        return

    stats = ingest.store(docs, use_llm=not args.no_llm, enrich_limit=args.enrich_limit)
    print(
        f"적재 완료: feed_item {stats['written']}건 · 태그 {stats['tags']}건 "
        f"· LLM 정제 {stats['enriched']}건 · 테마 규칙폴백 {stats['theme_default']}건"
    )
    _summary(body_stats, stats, time.monotonic() - started)

    if stats["written"] and stats["theme_default"] * 2 > stats["written"]:
        # 제목만으로는 키워드 규칙이 절반도 못 맞춘다. 본문(--with-docs)이나 정제가 필요하다는 신호.
        print("  ⚠ 테마 절반 이상이 규칙 기본값입니다 — --with-docs / --enrich-limit 를 늘려 보세요")
    # --no-llm 은 정제하지 않는 것이 의도이므로 경고하지 않는다.
    unenriched = 0 if args.no_llm else _bodies_without_enrich(body_stats, stats)
    if unenriched:
        # 확보한 본문이 정제되지 못하면 그 행은 '원문 확보' 배지에 요약이 빈 채로 남는다
        # (llm.naive_summary 가 저작권 규약 때문에 뉴스 본문을 요약 자리에 쓰지 않는다).
        # --with-docs 만 올리고 이 값을 그대로 두면 없던 고장이 새로 생긴다.
        print(f"  ⚠ 본문을 받았지만 정제되지 못한 자료가 {unenriched}건 있습니다 "
              f"— --enrich-limit 를 {stats['enriched'] + unenriched} 이상으로 올리세요")


def _bodies_without_enrich(body_stats, stats) -> int:
    """원문은 확보했는데 LLM 정제까지 가지 못한 건수 (--enrich-limit 부족의 신호)."""
    got = sum(st.with_body for st in body_stats.values())
    return max(0, got - stats["enriched"])


def _summary(body_stats, stats, elapsed: float) -> None:
    """운영자용 최종 요약표.

    성공만 찍히는 로그로는 무엇이 왜 빠졌는지 알 수 없다. 소스별로
    (수집 / 원문 확보 / 정제 / 등급 / 미확보 사유)를 한 화면에 모은다.
    """
    print("\n■ 소스별 요약")
    print(crawler.format_report(body_stats))

    by_source = stats.get("by_source") or {}
    if by_source:
        print(f"\n  {'소스':<6}{'적재':>6}{'정제':>6}{'원문확보':>8}{'요약문':>7}{'제목만':>7}")
        for name in sorted(by_source):
            s = by_source[name]
            print(f"  {name:<6}{s.get('written', 0):>6}{s.get('enriched', 0):>6}"
                  f"{s.get(classify.GRADE_FULL, 0):>8}{s.get(classify.GRADE_SUMMARY, 0):>7}"
                  f"{s.get(classify.GRADE_TITLE, 0):>7}")
    print(f"\n  총 소요 {elapsed / 60:.1f}분")


if __name__ == "__main__":
    main()
