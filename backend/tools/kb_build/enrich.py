"""S6. LLM 보강 — summary · keywords 를 채운다.

`summary` 는 인덱스와 검색 결과에 그대로 노출된다. 에이전트가 **이 한 줄만 보고
문서를 열지 말지 판단**하므로 (전략 §3.2) 제목 복사본이면 검색 단계가 무의미해진다.
`keywords` 는 동의어·영문·약어를 담아 키워드 검색 재현율을 올린다.

app/pipeline/farming/llm.py 와 같은 규약을 따른다:

- provider 미설정·네트워크·파싱 실패는 전부 **원문 보존 폴백**으로 떨어지고
  예외를 올리지 않는다. 설정이 없어도 빌드는 끝까지 돈다.
- 형식 오류는 1회 재시도한다.
- 항목 단위로 격리한다. 한 건 실패가 전체를 중단시키지 않는다.

**본문은 절대 수정하지 않는다.** frontmatter 의 두 필드만 덮어쓴다.

    python -m tools.kb_build.enrich --company SKES --limit 40
    python -m tools.kb_build.enrich --company SKES          # 전량
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app import llm_client                                        # noqa: E402
from app.config import OI_LLM_CONCURRENCY, OI_LLM_MODEL, OI_LLM_PROVIDER  # noqa: E402
from tools.kb_build import companies                              # noqa: E402
from tools.kb_build.common import (                               # noqa: E402
    dump_frontmatter, load_frontmatter, read_text, split_frontmatter, write_text,
)
from tools.kb_build.companies import Company                      # noqa: E402

BODY_CHARS = 3_000        # 앞부분만으로 요약이 가능한 구조다 (리드 문장 + 표 헤더)
SUMMARY_CHARS = 160

SYSTEM = (
    "당신은 {company} 지식 베이스의 색인 담당자다. 주어진 문서 조각을 읽고 "
    "JSON 객체 하나만 출력한다. 설명·코드펜스 금지."
)

PROMPT = """아래는 {company} AI 지식 베이스의 문서 한 건이다.

출력 스키마:
{{"summary": "이 문서에 무엇이 들어 있는지 한 문장(80자 내외). 제목을 그대로 옮기지 말고,
              '어떤 질문에 답할 수 있는 문서인가'가 드러나게 쓴다. 표가 핵심이면 무슨 표인지 밝힌다.",
  "keywords": [검색어 5~10개. 본문에 등장하는 한국어 용어, 영문 표기, 약어,
               사용자가 쓸 법한 동의어를 섞는다. 문서 제목의 단어를 그대로 반복하지 않는다.]}}

[문서]
id: {doc_id}
제목: {title}
위치: {breadcrumb}
본문:
{body}
"""


def _parse(raw: str, title: str) -> Dict:
    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    start, end = clean.find("{"), clean.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"JSON 을 찾지 못했습니다: {clean[:160]!r}")
    data = json.loads(clean[start:end + 1])

    summary = str(data.get("summary") or "").strip().replace("\n", " ")[:SUMMARY_CHARS]
    if summary == title.strip():
        raise ValueError("summary 가 제목 복사본입니다")
    keywords = [
        str(k).strip() for k in (data.get("keywords") or [])
        if str(k).strip()
    ][:10]
    if not summary:
        raise ValueError("summary 가 비어 있습니다")
    return {"summary": summary, "keywords": keywords}


def enrich_one(entry: Dict, out: Path, company: Company) -> Dict:
    path = out / entry["path"]
    _, body = split_frontmatter(read_text(path))
    prompt = PROMPT.format(
        company=company.name,
        doc_id=entry["id"], title=entry["title"],
        breadcrumb=entry.get("breadcrumb") or "-",
        body=body.strip()[:BODY_CHARS],
    )
    system = SYSTEM.format(company=company.name)

    def ask(text: str) -> str:
        return llm_client.call(text, system, OI_LLM_MODEL, OI_LLM_PROVIDER)

    try:
        return _parse(ask(prompt), entry["title"])
    except (ValueError, json.JSONDecodeError):
        return _parse(ask(prompt + "\n\n반드시 JSON 객체 하나만 출력하라."), entry["title"])


def apply(entry: Dict, data: Dict, out: Path) -> None:
    """frontmatter 의 summary·keywords 만 덮어쓴다. 본문은 손대지 않는다."""
    path = out / entry["path"]
    text = read_text(path)
    meta = load_frontmatter(text)
    _, body = split_frontmatter(text)

    meta["summary"] = data["summary"]
    # 원문 Chunk 블록에서 승계한 키워드가 있으면 합친다 (중복 제거, 순서 유지).
    merged, seen = [], set()
    for k in list(meta.get("keywords") or []) + data["keywords"]:
        if k and k not in seen:
            seen.add(k)
            merged.append(k)
    meta["keywords"] = merged

    write_text(path, dump_frontmatter(meta) + body)
    entry["summary"] = data["summary"]
    entry["keywords"] = merged


def run(out: Path, limit: int | None, company: Company,
        only_missing: bool = True) -> Dict:
    manifest: List[Dict] = json.loads(read_text(out / "manifest.json"))
    targets = [e for e in manifest if not (e.get("summary") or "").strip()] \
        if only_missing else list(manifest)
    if limit:
        # 큰 문서를 먼저 — 요약이 없을 때 손실이 가장 큰 쪽이다.
        targets = sorted(targets, key=lambda e: -e["tokens"])[:limit]

    ready, why = llm_client.ready(OI_LLM_PROVIDER)
    if not ready:
        print(f"[kb] {why} — 보강을 건너뜁니다 (summary 는 빈 값 유지)")
        return {"done": 0, "failed": 0, "targets": len(targets)}

    print(f"[kb] {OI_LLM_PROVIDER}/{OI_LLM_MODEL} — {len(targets)}건 보강 "
          f"(동시 {OI_LLM_CONCURRENCY})")
    done = failed = 0
    with ThreadPoolExecutor(max_workers=max(1, OI_LLM_CONCURRENCY)) as pool:
        futures = {pool.submit(enrich_one, e, out, company): e for e in targets}
        for future, entry in futures.items():
            try:
                data = future.result()
            except Exception as e:                    # 항목 단위 격리
                failed += 1
                print(f"[kb] ✗ {entry['id'][:52]} — {type(e).__name__}: {str(e)[:90]}")
                continue
            apply(entry, data, out)
            done += 1
            print(f"[kb] ✓ {entry['id'][:52]} — {data['summary'][:60]}")

    write_text(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    return {"done": done, "failed": failed, "targets": len(targets)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--limit", type=int, default=None, help="상위 N건만 (미지정 시 전량)")
    ap.add_argument("--all", action="store_true", help="summary 가 이미 있어도 다시 생성")
    args = ap.parse_args()

    co = companies.get(args.company)
    r = run(args.out or Path("knowledge") / co.code, args.limit, co,
            only_missing=not args.all)
    print(f"\n보강 {r['done']}/{r['targets']}건 · 실패 {r['failed']}건")
    print("INDEX.md 를 갱신하려면 build_index 를 다시 실행하세요.")


if __name__ == "__main__":
    main()
