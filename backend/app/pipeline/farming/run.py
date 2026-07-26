"""파밍 실행 CLI.

    python -m app.pipeline.farming.run                 # 전체 소스 크롤 → DB 적재
    python -m app.pipeline.farming.run --days 14        # 최근 14일
    python -m app.pipeline.farming.run --dry            # 적재 없이 수집 결과만 출력
    python -m app.pipeline.farming.run --source news    # 특정 소스만 (dart|sec|news)
"""
import argparse

from app.config import CRAWL_SINCE_DAYS
from app.pipeline.farming import crawler, ingest, dart, sec, news


def _crawl(source: str, days: int):
    if source == "dart":
        return dart.crawl(days)
    if source == "sec":
        return sec.crawl(days)
    if source == "news":
        return news.crawl(days)
    return crawler.crawl_all(days)


def main():
    ap = argparse.ArgumentParser(description="O/I Scout 지식 파밍 크롤러")
    ap.add_argument("--days", type=int, default=CRAWL_SINCE_DAYS, help="크롤 대상 기간(일)")
    ap.add_argument("--source", choices=["all", "dart", "sec", "news"], default="all")
    ap.add_argument("--dry", action="store_true", help="DB 적재 없이 수집만")
    ap.add_argument("--limit", type=int, default=10, help="--dry 시 출력 개수")
    args = ap.parse_args()

    docs = _crawl(args.source, args.days)
    docs = crawler._dedup(docs)
    print(f"\n총 {len(docs)}건 수집 (최근 {args.days}일)\n")

    if args.dry:
        for d in docs[: args.limit]:
            print(f"  [{d.published_on} · {d.kind} · {d.source}] {d.title[:60]}")
            print(f"     tags={d.tags} url={d.url[:70]}")
        if len(docs) > args.limit:
            print(f"  ... 외 {len(docs) - args.limit}건")
        return

    stats = ingest.store(docs)
    print(f"적재 완료: feed_item {stats['written']}건 · 태그 {stats['tags']}건")


if __name__ == "__main__":
    main()
