import { TODAY, AFF, AFFILIATES, KIND } from "../data/affiliates.js";
import { FEED } from "../data/feed.js";
import { md, inPeriod } from "./utils.js";

/* 대시보드 범위를 사내 LLM용 '외부 환경 브리핑' 프롬프트로 직렬화 */
export function buildPrompt(affCodes, periodDays) {
  const affs = affCodes.length ? affCodes : AFFILIATES.map((a) => a.code);
  const items = FEED.filter((f) => inPeriod(f, periodDays) && f.tags.some((t) => affs.includes(t)));
  const events = items.filter((f) => f.kind !== "news");
  const news = items.filter((f) => f.kind === "news");
  const line = (f) =>
    `- [${md(f.d)} · ${KIND[f.kind].label} · ${f.src}] ${f.title} — ${f.sum} (관련: ${f.tags.join(", ")})`;
  const affNames = affs.map((c) => AFF[c].name).join(", ");
  return [
    `# 외부 환경 브리핑 — ${affNames} (최근 ${periodDays}일)`,
    `기준일: ${TODAY} · 출처: DART/SEC/뉴스 (O/I 변경 검토)`,
    ``,
    `## 공시 이벤트`,
    events.length ? events.map(line).join("\n") : "- (해당 기간 없음)",
    ``,
    `## 뉴스`,
    news.length ? news.map(line).join("\n") : "- (해당 기간 없음)",
    ``,
    `---`,
    `## 지시문`,
    `당신은 SK이노베이션 O/I추진단 애널리스트입니다. 위 외부 동향과 아래에 붙여넣는 증권사 리서치 내용을 근거로, ${affNames}에 적용 가능한 O/I(Operation Improvement) 과제 후보 3건을 제안하세요. 각 과제는 과제명 / 배경 / 실행방안 / 리스크 / 기대효과 / KPI(산출식) / 근거를 포함해야 하며, 확장 투자형보다 비용·효율·수익성 개선 과제를 우선하세요.`,
    ``,
    `[▼ 여기에 증권사 리서치 본문·주요 페이지 텍스트를 붙여넣으세요]`,
  ].join("\n");
}
