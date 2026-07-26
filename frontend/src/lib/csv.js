import { AFF } from "../data/affiliates.js";
import { FEED_BY_ID } from "../data/feed.js";

/* 기존 과제 기록 DB 스키마 기준 고정 컬럼 (기획안 6.3) */
export const CSV_HEADERS = [
  "과제ID", "생성일", "계열사", "과제명", "분류", "배경", "실행방안",
  "리스크", "기대효과", "KPI지표", "KPI산출식", "근거출처", "상태", "작성경로",
];

function csvEscape(v) {
  const s = String(v ?? "").replace(/\r?\n/g, " / ");
  return '"' + s.replace(/"/g, '""') + '"';
}

export function tasksToCsv(tasks) {
  const rows = tasks.map((t) =>
    [
      t.id, t.createdAt, AFF[t.aff]?.name || t.aff, t.title, t.category,
      t.background || "", t.plan || "", t.risk, t.effect,
      t.kpiName, t.kpiFormula,
      (t.evidence || [])
        .map((id) => { const f = FEED_BY_ID[id]; return f ? `${f.src}(${f.d})` : id; })
        .join("; "),
      t.status, t.origin,
    ].map(csvEscape).join(",")
  );
  return CSV_HEADERS.map(csvEscape).join(",") + "\n" + rows.join("\n");
}
