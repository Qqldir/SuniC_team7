"""이미 정제된 feed_item 에 brief(트렌드룸 데일리 브리핑)만 채우는 백필.

    python -m app.db.backfill_brief --dry-run     # 대상 건수·프롬프트만 확인
    python -m app.db.backfill_brief --limit 5     # 5건만 (시험)
    python -m app.db.backfill_brief               # 대상 전량

왜 전량 재정제(farming.run)가 아니라 이 좁은 백필인가
    ① **원본 body 가 DB 에 없다.** feed_item 에 body 컬럼이 없어 재정제하려면 원문을
       다시 크롤해야 하고, 뉴스는 Google News 토큰·페이월 때문에 그때 확보된다는 보장이 없다.
    ② 전량 재정제는 **이미 확보한 값을 깎는다.** 실측(dart-20260515002934):
       metrics 3개 → 2개로 줄고, LLM keywords("품목별가동률"·"가동률격차"·"석화제품")가
       ingest._sync_keywords 에서 **사전 키워드보다 앞자리**를 차지한다.
       현재 DB 의 distinct 키워드 54종은 전부 사전어라 트렌드룸 키워드 카드·트리맵 라벨·
       필터가 한 어휘 체계로 서 있는데, 재정제는 그것을 1회성 조어로 흩뜨린다.
    ③ brief 는 summary(사실 재진술)를 재료로 한 **시사점 한 겹**이라 저장된 summary 만으로
       충분히 만들 수 있다. 화면에서 brief 바로 옆에 summary 가 붙어 검증도 가능하다.

무엇을 쓰나
    feed_item.brief 한 컬럼뿐이다. summary·metrics·keywords·importance 는 건드리지 않는다.

대상
    enriched=1 AND brief 가 빈 값 AND summary <> ''.
    summary 가 빈 자료(원문 미확보 12건)는 **대상이 아니다** — 재료가 없는데 지어내면
    근거 없는 문장이 박힌다. 그 행은 화면이 '원문 미확보' 로 남는 것이 정직하다.
"""
import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor

from app import llm_client
from app.config import OI_LLM_CONCURRENCY, OI_LLM_MODEL, OI_LLM_PROVIDER
from app.db.database import get_connection

BRIEF_CHARS = 200  # farming.llm.BRIEF_CHARS 와 같은 규격

SYSTEM = (
    "당신은 SK이노베이션 계열의 O/I(운영개선) 과제 발굴을 지원하는 외부 동향 분석가다. "
    "모든 출력은 한국어로 쓰고, 지정된 JSON 객체 하나만 출력한다. "
    "주어진 [자료 요약]에 없는 사실·수치를 만들어 내지 않는다."
)

PROMPT = """아래 [자료 요약]은 외부 기업의 공시·보고서·뉴스를 이미 정제해 둔 결과다.
이것만 근거로 트렌드룸 '데일리 브리핑' 카드에 실을 brief 를 쓰라.

brief 규칙
- **무슨 일이 있었고 그것이 SK 계열사에게 무슨 의미인지** 1~2문장.
- 개조식 종결(…했습니다. / …입니다.). 전체 40~90자.
- [자료 요약]에 있는 사실·수치만 쓴다. 배경지식으로 보충하지 마라.
- 요약을 그대로 옮겨 적지 마라. 요약은 사실 재진술이고 brief 는 **시사점**이다.
- 자료의 쓸모를 깎는 평가문("사례성은 제한적임")을 쓰지 마라. 그건 brief 가 아니다.
- 회사명·매체명을 반복하지 마라. 화면에 따로 표시된다.
- ★ [자료 요약]이 비어 있거나 시사점을 말할 근거가 없으면 **빈 문자열**을 낸다.
  억지로 지어내지 마라 — 화면이 요약으로 폴백한다.

[자료 요약]
제목: {title}
발표 주체: {source}
자료 종류: {kind_label}
발행일: {published_on}
테마: {theme}
레버: {levers}
요약: {summary}
지표: {metrics}
"""

# codex --output-schema 용. 최상위 object · 전 키 required · additionalProperties:false.
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["brief"],
    "properties": {
        "brief": {
            "type": "string",
            "description": "1~2문장 40~90자, 개조식 종결. 무슨 일이 있었고 우리에게 무슨"
                           " 의미인지. 근거가 없으면 빈 문자열",
        }
    },
}

_SELECT = """
SELECT id,
       COALESCE(NULLIF(title_label, ''), title) AS title,
       COALESCE(NULLIF(source_label, ''), source) AS source,
       kind_label, published_on, theme, levers, summary, metrics
  FROM feed_item
 WHERE enriched = 1 AND (brief IS NULL OR brief = '') AND summary <> ''
 ORDER BY id
"""


def _one_paragraph(text: str) -> str:
    s = " ".join(str(text or "").split())
    for b in ("- ", "· ", "• ", "* "):
        if s.startswith(b):
            s = s[len(b):]
    return s.strip()


def build_prompt(row) -> str:
    return PROMPT.format(
        title=row["title"], source=row["source"], kind_label=row["kind_label"] or "",
        published_on=row["published_on"], theme=row["theme"] or "",
        levers=row["levers"] or "(없음)", summary=row["summary"],
        metrics=row["metrics"] or "[]",
    )


def ask(row) -> tuple:
    """(id, brief, 오류) — 항목 단위로 격리한다. 한 건 실패가 배치를 멈추지 않는다."""
    try:
        raw = llm_client.call(
            build_prompt(row), SYSTEM, OI_LLM_MODEL, OI_LLM_PROVIDER, schema=SCHEMA,
        )
        clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        s, e = clean.find("{"), clean.rfind("}")
        if s == -1 or e == -1:
            return row["id"], None, f"JSON 없음: {clean[:120]!r}"
        brief = _one_paragraph(json.loads(clean[s:e + 1]).get("brief"))[:BRIEF_CHARS]
        return row["id"], brief, None
    except Exception as exc:                       # noqa: BLE001 — 항목 격리가 목적
        return row["id"], None, f"{type(exc).__name__}: {str(exc)[:160]}"


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description="feed_item.brief 백필")
    ap.add_argument("--limit", type=int, default=0, help="처리 건수 상한 (0=전량)")
    ap.add_argument("--dry-run", action="store_true", help="호출·기록 없이 대상만 출력")
    args = ap.parse_args(argv if argv is not None else sys.argv[1:])

    ready, why = llm_client.ready(OI_LLM_PROVIDER)
    if not ready and not args.dry_run:
        print(f"[brief] {why} — 중단합니다 (brief 는 LLM 만 만들 수 있습니다)")
        raise SystemExit(1)

    conn = get_connection()
    try:
        rows = conn.execute(_SELECT).fetchall()
        if args.limit:
            rows = rows[:args.limit]
        print(f"[brief] 대상 {len(rows)}건 · provider={OI_LLM_PROVIDER} "
              f"· 동시 {OI_LLM_CONCURRENCY}")
        if args.dry_run:
            for r in rows[:3]:
                print(f"\n── {r['id']}\n{build_prompt(r)}")
            print(f"\n[dry-run] {len(rows)}건 대상. 호출·기록 없음.")
            return

        t0 = time.time()
        done = blank = failed = 0
        # ★ 커밋을 건별로 한다. 중간에 끊겨도 여기까지 채운 brief 는 남고,
        #   다시 실행하면 남은 건만 대상이 된다(대상 조건이 brief 빈 값이므로 자동 재개).
        with ThreadPoolExecutor(max_workers=max(1, OI_LLM_CONCURRENCY)) as pool:
            for fid, brief, err in pool.map(ask, rows):
                if err:
                    failed += 1
                    print(f"[brief] ✗ {fid} {err}")
                    continue
                if not brief:
                    blank += 1
                    print(f"[brief] – {fid} 근거 없음(빈 값) — 화면은 요약으로 폴백")
                    continue
                conn.execute("UPDATE feed_item SET brief = ? WHERE id = ?", (brief, fid))
                conn.commit()
                done += 1
                print(f"[brief] ✓ {fid} {brief[:60]}")
        print(f"\n[brief] 기록 {done}건 · 빈 값 {blank}건 · 실패 {failed}건 "
              f"· {time.time() - t0:.0f}초")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
