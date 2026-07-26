import { TODAY } from "../data/affiliates.js";

/* 날짜/기간 유틸 */
export const md = (s) => s.slice(5); // '2026-07-21' → '07-21'
export const daysBetween = (a, b) => Math.round((new Date(a) - new Date(b)) / 86400000);
export const inPeriod = (item, days) => daysBetween(TODAY, item.d) <= days;

/* 파일 다운로드 (BOM 포함 — 엑셀 한글 깨짐 방지) */
export function downloadText(filename, content, mime = "text/plain") {
  const blob = new Blob(["﻿" + content], { type: mime + ";charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

/* 클립보드 복사 (execCommand 폴백 포함) */
export async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    try {
      const ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
      return true;
    } catch {
      return false;
    }
  }
}
