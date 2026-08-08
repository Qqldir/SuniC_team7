"""S4. 계층 0 · 계층 1 생성 — frontmatter 에서 자동 생성한다 (전략 §2.2).

**여기가 전략을 그대로 따를 수 없는 지점이다.** 전략 §2.2 는 "문서 하나당 한 줄"
인덱스를 상정하고 문서 200개 / 3~4천 토큰을 예시로 든다. SK온 DB 는 재구조화 후
문서가 742개라 같은 방식이면 인덱스만 1만 5천 토큰을 넘겨 계층 1 예산(1~4천)을
두 배 이상 초과한다.

그래서 인덱스를 두 단계로 나눈다.

    INDEX.md (항상 로드)   도메인 → 절(section) 단위 요약 + 과제 시드 전량
    list_docs(domain, …)   특정 절의 문서 목록을 온디맨드로 반환

시드(seeds/)만 문서 단위로 전부 싣는다. 과제 발굴 agent 가 실제로 소비하는
대상이고 수십 건뿐이라 비용이 감당되며, 이걸 빼면 "무엇이 있는지" 자체를 모른다.

    python -m tools.kb_build.build_index --company SKES
"""
from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from tools.kb_build import companies
from tools.kb_build.common import est_tokens, read_text, write_text
from tools.kb_build.companies import Company


def _section_key(doc: Dict) -> str:
    """`D08-12-3` → `D08-12`. 절 단위로 묶기 위한 키."""
    sec = (doc.get("section") or "").rstrip(".")
    parts = sec.split("-")
    return "-".join(parts[:2]) if len(parts) >= 2 else (sec or "—")


# ── 계층 1: INDEX.md ────────────────────────────────────────────────────

def build_index(manifest: List[Dict], company: Company) -> str:
    seeds = [d for d in manifest if d["shelf"] == "seeds"]
    docs = [d for d in manifest if d["shelf"] != "seeds"]

    out = [
        f"# {company.name} 지식 베이스 인덱스",
        "",
        "이 인덱스는 frontmatter 에서 자동 생성된다. 직접 편집하지 말 것.",
        "",
        f"- 총 {len(manifest)}건 · 시드 {len(seeds)}건 · 도메인 문서 {len(docs)}건",
        "- 본문은 `read_doc(id)` 로만 열린다. 아래 목록에 있는 id 만 유효하다.",
        "- `[build-log]` 은 원본 집필 로그다. 사실 근거로 인용하지 말 것.",
        "",
        "---",
        "",
        "## 과제 시드 (seeds/) — 과제 발굴 시 여기부터 본다",
        "",
        f"각 도메인이 D17 로 넘긴 O/I 과제 후보와 최종 포트폴리오. 전 {len(seeds)}건.",
        "",
    ]
    for d in sorted(seeds, key=lambda x: (x["domain"], x["id"])):
        summary = d.get("summary") or d["title"]
        out.append(f"- `{d['id']}` — {summary}")

    out += [
        "", "---", "", "## 도메인 지도 (docs/)", "",
        "도메인 → 절 → 문서 전량. 인덱스에 없는 문서는 존재하지 않는다.",
        "",
    ]

    by_domain: Dict[str, List[Dict]] = defaultdict(list)
    for d in docs:
        by_domain[d["domain"]].append(d)

    for domain in sorted(by_domain):
        theme, label = company.theme(domain)
        group = by_domain[domain]
        out += ["", f"### {domain} {label} · {len(group)}건 · `{theme}`", ""]

        by_section: Dict[str, List[Dict]] = defaultdict(list)
        for d in group:
            by_section[_section_key(d)].append(d)

        for sec in sorted(by_section):
            items = sorted(by_section[sec], key=lambda x: x["id"])
            # 절 제목은 가장 큰 문서에서 딴다 — 그 절을 가장 잘 대표한다.
            head = max(items, key=lambda x: x["tokens"])["title"].split(" — ")[0]
            out.append(f"**`{sec}` {head}**")
            for d in items:
                # summary 가 채워지기 전에는 제목이 그 자리를 대신한다.
                desc = d.get("summary") or d["title"]
                extra = [t for t in d["tags"]
                         if t in ("build-log", "schema", "table", "core-candidate")]
                suffix = f" · [{', '.join(extra)}]" if extra else ""
                out.append(f"- `{d['id']}` — {desc}{suffix}")
            out.append("")

    return "\n".join(out).rstrip() + "\n"


# ── 계층 0: core/ ───────────────────────────────────────────────────────

def build_schema(manifest: List[Dict], company: Company) -> str:
    """도메인 지도 · id 규칙 · 태그 어휘. 전부 결정적으로 생성된다."""
    counts: Dict[str, int] = defaultdict(int)
    for d in manifest:
        counts[d["domain"]] += 1

    lines = [
        f"# {company.name} 지식 베이스 스키마",
        "",
        "## 도메인 코드",
        "",
        "| 코드 | 주제 | 태그 | 문서 |",
        "|---|---|---|---|",
    ]
    for code in sorted(counts):
        theme, label = company.theme(code)
        lines.append(f"| `{code}` | {label} | `{theme}` | {counts[code]} |")

    seeds = [d for d in manifest if d["shelf"] == "seeds"]
    # id 규칙은 실제 문서로 보여준다 — 절번호 자리가 드러나는 것 중 가장 짧은 것.
    example = min((d for d in manifest if d.get("section")),
                  key=lambda d: (len(d["id"]), d["id"]), default=manifest[0])
    tags = sorted({t for d in manifest for t in d["tags"] if not t.startswith("xref:")})
    lines += [
        "",
        "## 문서 id 규칙",
        "",
        f"`{company.slug}-{{도메인}}-{{절번호}}-{{제목슬러그}}` — 예: `{example['id']}`.",
        "id 는 파일명과 일치하며, 인덱스나 검색 결과에 없는 id 는 존재하지 않는다.",
        "",
        "## 선반",
        "",
        "| 선반 | 내용 | 언제 |",
        "|---|---|---|",
        f"| `seeds/` | 도메인별 O/I 과제 후보 · D17 포트폴리오 — 문서 {len(seeds)}건 | 과제 발굴 |",
        "| `docs/` | 도메인 본문 (사업·운영·원가·계약·규제 등) | 근거 확인 |",
        "",
        "## 태그 어휘",
        "",
        " ".join(f"`{t}`" for t in tags),
        "",
        "`xref:d##` 태그는 그 문서가 다른 도메인을 참조한다는 뜻이다.",
    ]
    return "\n".join(lines) + "\n"


def build_core(manifest: List[Dict], out: Path, company: Company) -> Dict[str, int]:
    """core/ 를 만든다. schema.md 는 자동 생성, 나머지는 최초 1회 스텁만 깐다.

    용어집·규칙 스텁은 companies.py 가 회사별로 들고 있다. 여기 있던 SK온 표를
    그대로 다른 계열사에 깔면 **틀린 계층 0**(합병 시점·fact_status enum 이 다르다)이
    항상 로드되므로, 비어 있는 것보다 나쁘다.
    """
    core = out / "core"
    written = {}

    write_text(core / "schema.md", build_schema(manifest, company))
    written["schema.md"] = est_tokens(read_text(core / "schema.md"))

    for name, stub in (("glossary.md", company.glossary), ("rules.md", company.rules)):
        path = core / name
        if not path.exists():          # 사람이 고친 내용을 덮어쓰지 않는다
            write_text(path, stub)
        written[name] = est_tokens(read_text(path))
    return written


# ── 실행 ─────────────────────────────────────────────────────────────────

def _restore_frontmatter(manifest: List[Dict], out: Path) -> None:
    """승계한 summary·keywords 를 새로 복사된 문서 frontmatter 에 되써 넣는다."""
    from tools.kb_build.common import (
        dump_frontmatter, load_frontmatter, split_frontmatter,
    )

    for entry in manifest:
        if not (entry.get("summary") or "").strip():
            continue
        path = out / entry["path"]
        if not path.exists():
            continue
        text = read_text(path)
        meta = load_frontmatter(text)
        _, body = split_frontmatter(text)
        meta["summary"] = entry["summary"]
        meta["keywords"] = entry.get("keywords") or []
        write_text(path, dump_frontmatter(meta) + body)


def _carry_forward(manifest: List[Dict], out: Path) -> int:
    """이전 빌드의 summary·keywords 를 새 manifest 로 옮긴다.

    S6 보강은 LLM 호출 수백 건이 든다. 재빌드할 때마다 날아가면 아무도 빌드를
    다시 돌리지 않게 된다. id 가 같으면 사람이 쓴 값으로 간주해 물려받는다.
    """
    old_path = out / "manifest.json"
    if not old_path.exists():
        return 0
    old = {d["id"]: d for d in json.loads(read_text(old_path))}
    kept = 0
    for entry in manifest:
        prev = old.get(entry["id"])
        if not prev:
            continue
        if (prev.get("summary") or "").strip():
            entry["summary"] = prev["summary"]
            kept += 1
        if prev.get("keywords"):
            merged, seen = [], set()
            for k in list(entry.get("keywords") or []) + list(prev["keywords"]):
                if k and k not in seen:
                    seen.add(k)
                    merged.append(k)
            entry["keywords"] = merged
    return kept


def resync(out: Path) -> int:
    """문서 frontmatter → manifest 로 summary·keywords 를 되읽는다.

    S6 보강은 문서를 한 건씩 저장하지만 manifest 는 마지막에 한 번 쓴다.
    배치가 중간에 끊기면 문서에는 요약이 있는데 manifest 에는 없는 상태가 된다.
    이 함수가 그 격차를 메워, 끊긴 배치를 처음부터 다시 돌리지 않게 한다.
    """
    from tools.kb_build.common import load_frontmatter

    path = out / "manifest.json"
    manifest = json.loads(read_text(path))
    synced = 0
    for entry in manifest:
        doc = out / entry["path"]
        if not doc.exists():
            continue
        meta = load_frontmatter(read_text(doc))
        summary = (meta.get("summary") or "").strip()
        if summary and summary != (entry.get("summary") or "").strip():
            entry["summary"] = summary
            entry["keywords"] = meta.get("keywords") or entry.get("keywords") or []
            synced += 1
    if synced:
        write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2))
    return synced


def reindex(out: Path, company: Company) -> Dict:
    """복사 없이 INDEX.md · core/schema.md 만 현재 manifest 로 다시 만든다.

    S6 보강 직후처럼 **산출물을 건드리면 안 되는** 상황에서 쓴다.
    """
    resync(out)                     # 끊긴 보강 배치의 결과까지 반영한다
    manifest = json.loads(read_text(out / "manifest.json"))
    index = build_index(manifest, company)
    write_text(out / "INDEX.md", index)
    core = build_core(manifest, out, company)
    return {
        "docs": len(manifest),
        "index_tokens": est_tokens(index),
        "core_tokens": core,
        "core_total": sum(core.values()),
        "body_tokens": sum(d["tokens"] for d in manifest),
    }


def run(segments: Path, out: Path, company: Company) -> Dict:
    manifest = json.loads(read_text(segments / "manifest.json"))
    kept = _carry_forward(manifest, out)
    if kept:
        print(f"  이전 빌드에서 summary {kept}건 승계")

    for shelf in ("docs", "seeds"):
        src, dst = segments / shelf, out / shelf
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

    # 승계한 summary·keywords 를 문서 frontmatter 에도 다시 써 넣는다.
    _restore_frontmatter(manifest, out)

    index = build_index(manifest, company)
    write_text(out / "INDEX.md", index)
    write_text(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    core = build_core(manifest, out, company)

    return {
        "docs": len(manifest),
        "index_tokens": est_tokens(index),
        "core_tokens": core,
        "core_total": sum(core.values()),
        "body_tokens": sum(d["tokens"] for d in manifest),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default=companies.DEFAULT_CODE,
                    help=f"회사 코드 ({'/'.join(companies.codes())})")
    ap.add_argument("--segments", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    co = companies.get(args.company)
    r = run(args.segments or Path("build/segments") / co.code,
            args.out or Path("knowledge") / co.code, co)
    print(f"문서            {r['docs']:>7,}건")
    print(f"계층 2 본문     {r['body_tokens']:>7,} 토큰 (온디맨드)")
    print(f"계층 1 INDEX    {r['index_tokens']:>7,} 토큰 (전량 수록)")
    for name, tok in r["core_tokens"].items():
        print(f"  core/{name:<14} {tok:>5,} 토큰")
    print(f"계층 0 합계     {r['core_total']:>7,} 토큰")
    print(f"→ {args.out}")


if __name__ == "__main__":
    main()
