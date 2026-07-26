import React, { useState, useEffect, useMemo, useRef } from "react";
import {
  LayoutDashboard, Wand2, FolderCheck, MessageSquare, Download, Copy, Check,
  X, Bell, ChevronRight, Trash2, Loader2, FileText, AlertTriangle, Plus
} from "lucide-react";

/* ─────────────────────────── 데이터 (데모용 샘플) ─────────────────────────── */

const TODAY = "2026-07-22";

const BIZ = {
  energy:  { label: "에너지·화학", color: "#B0522C" },
  battery: { label: "배터리·소재", color: "#2E6B57" },
  lng:     { label: "LNG·전력",   color: "#3A5E8C" },
};

const AFFILIATES = [
  { code: "SKE",   name: "SK에너지",             biz: "energy"  },
  { code: "SKGC",  name: "SK지오센트릭",         biz: "energy"  },
  { code: "SKEN",  name: "SK엔무브",             biz: "energy"  },
  { code: "SKIPC", name: "SK인천석유화학",       biz: "energy"  },
  { code: "SKTI",  name: "SK트레이딩인터내셔널", biz: "energy"  },
  { code: "SKEO",  name: "SK어스온",             biz: "energy"  },
  { code: "SKO",   name: "SK온",                 biz: "battery" },
  { code: "SKIET", name: "SK아이이테크놀로지",   biz: "battery" },
  { code: "SKES",  name: "SK E&S",               biz: "lng"     },
];
const AFF = Object.fromEntries(AFFILIATES.map(a => [a.code, a]));

const KIND = {
  adhoc:    { label: "DART 수시", cls: "badge-adhoc" },
  periodic: { label: "DART 정기", cls: "badge-periodic" },
  sec:      { label: "SEC",      cls: "badge-sec" },
  news:     { label: "뉴스",     cls: "badge-news" },
};

// 데모용 샘플 피드 — 실서비스에선 DART OpenAPI / SEC EDGAR / 뉴스 API 수집으로 대체
const FEED = [
  { id: "e01", d: "2026-07-21", kind: "adhoc",    src: "롯데케미칼",       title: "여수 NCC 일부 라인 가동 조정 결정", sum: "수요 부진에 따른 가동률 조정 공시. 고정비 흡수 구조 변화로 원가 경쟁 심화 예상.", tags: ["SKGC", "SKIPC"] },
  { id: "e02", d: "2026-07-20", kind: "news",     src: "에너지 정책",      title: "산업용 전기요금 추가 인상안 논의", sum: "요금 인상 시 전력 다소비 공정의 원단위 관리 중요성 확대.", tags: ["SKE", "SKGC", "SKIPC"] },
  { id: "e03", d: "2026-07-18", kind: "sec",      src: "Dow",              title: "10-Q — 연 10억 달러 비용절감 프로그램 진척 공시", sum: "물류·구매·정비 영역별 절감 실적과 잔여 목표 공개.", tags: ["SKGC"] },
  { id: "e04", d: "2026-07-17", kind: "news",     src: "미쓰이화학",       title: "정기보수(TA) 공정 개선으로 기간 단축 발표", sum: "결산설명회에서 TA 표준화·병렬화 사례와 기회손실 축소 효과 언급.", tags: ["SKGC", "SKE"] },
  { id: "e05", d: "2026-07-15", kind: "adhoc",    src: "LG에너지솔루션",   title: "신규 시설투자 집행 속도 조절 공시", sum: "수요 성장 둔화 구간의 CapEx 페이싱. 기존 라인 효율화로 무게중심 이동.", tags: ["SKO"] },
  { id: "e06", d: "2026-07-14", kind: "news",     src: "CATL",             title: "검사 자동화 확대로 셀 수율 개선 보도", sum: "머신비전 기반 전수검사 전환. 수율·검사 인건비 동시 개선 사례.", tags: ["SKO"] },
  { id: "e07", d: "2026-07-11", kind: "sec",      src: "LyondellBasell",   title: "유럽 자산 전략 검토 관련 공시", sum: "저수익 설비 매각·전환 검토. 다운사이클 포트폴리오 조정의 대표 사례.", tags: ["SKGC"] },
  { id: "e08", d: "2026-07-09", kind: "news",     src: "해운 시황",        title: "컨테이너 해상운임 지수 하락세 지속", sum: "장기 운송계약 재협상 여지. 물류비 원단위 절감 타이밍.", tags: ["SKTI", "SKE", "SKO"] },
  { id: "e09", d: "2026-07-08", kind: "periodic", src: "에쓰오일",         title: "반기보고서 — 정기보수 계획·원가 동향", sum: "하반기 TA 일정과 정비비 추이 공시. 동종사 대비 정비비율 비교 가능.", tags: ["SKE"] },
  { id: "e10", d: "2026-07-06", kind: "news",     src: "아사히카세이",     title: "분리막 라인 재편으로 수익성 개선 추진", sum: "저가동 라인 통합 운영. 가동률 방어형 원가 구조 전환 사례.", tags: ["SKIET"] },
  { id: "e11", d: "2026-07-03", kind: "adhoc",    src: "GS칼텍스",         title: "자가발전·유틸리티 설비 투자 결정 공시", sum: "전력비 부담 대응형 투자. 에너지 자립도와 원단위 개선 목적.", tags: ["SKE"] },
  { id: "e12", d: "2026-07-01", kind: "news",     src: "산업부",           title: "석화 콤비나트 경쟁력 방안 — 설비 공동활용 논의", sum: "단지 내 유틸리티·물류 공동화가 의제로. 인접사 협력형 과제 여지.", tags: ["SKGC", "SKIPC"] },
  { id: "e13", d: "2026-06-29", kind: "sec",      src: "Cheniere",         title: "운영비 가이던스 및 장기계약 업데이트", sum: "터미널 운영비 효율화 지표 공개. LNG 운영 벤치마크로 참고 가능.", tags: ["SKES"] },
  { id: "e14", d: "2026-06-27", kind: "news",     src: "Valero",           title: "정제마진 약세 구간 오펙스 절감 목표 제시", sum: "정기보수 최적화·에너지 효율 중심의 비용 대응 발표.", tags: ["SKE"] },
  { id: "e15", d: "2026-06-25", kind: "periodic", src: "삼성SDI",          title: "반기보고서 — 가동률 조정·재고 관리 동향", sum: "재고자산 회전과 가동 전략 공시. 운전자본 관리 비교 지표.", tags: ["SKO"] },
  { id: "e16", d: "2026-06-24", kind: "news",     src: "포스코인터내셔널", title: "E&P 운영 효율화·생산비 절감 계획 보도", sum: "해외 광구 운영비 구조 개선. 생산 단가 관리 사례.", tags: ["SKEO"] },
];
const FEED_BY_ID = Object.fromEntries(FEED.map(f => [f.id, f]));

// 봇 데일리 발송분 (데모 샘플)
const BOT_SEED = [
  {
    id: "b1", aff: "SKGC", title: "NCC 정기보수(TA) 기간 단축 벤치마킹", category: "정비/TA",
    risk: "공기 단축에 따른 안전·품질 검증 부담 증가",
    effect: "TA 1일 단축 시 기회손실·고정비 부담 축소",
    kpi: { name: "TA 기간 단축률", formula: "(기준 TA일수 − 실제 TA일수) ÷ 기준 TA일수" },
    evidence: ["e04", "e01"],
  },
  {
    id: "b2", aff: "SKE", title: "전력 다소비 공정 요금제·피크 관리 최적화", category: "에너지비",
    risk: "부하 이동 시 생산 계획과의 충돌 가능성",
    effect: "요금 인상분 흡수 및 전력비 원단위 개선",
    kpi: { name: "전력 원단위", formula: "전력사용량(kWh) ÷ 생산량(t)" },
    evidence: ["e02", "e11"],
  },
  {
    id: "b3", aff: "SKO", title: "검사 자동화 확대를 통한 셀 수율 개선", category: "수율",
    risk: "설비 투자 대비 효과 검증에 기간 소요",
    effect: "불량 유출 감소와 검사 인건비 절감 동시 달성",
    kpi: { name: "공정 수율", formula: "양품 수 ÷ 투입 수 × 100(%)" },
    evidence: ["e06", "e05"],
  },
];

const CSV_HEADERS = ["과제ID", "생성일", "계열사", "과제명", "분류", "배경", "실행방안", "리스크", "기대효과", "KPI지표", "KPI산출식", "근거출처", "상태", "작성경로"];

/* ─────────────────────────── 유틸 ─────────────────────────── */

const md = (s) => s.slice(5); // '2026-07-21' → '07-21'
const daysBetween = (a, b) => Math.round((new Date(a) - new Date(b)) / 86400000);
const inPeriod = (item, days) => daysBetween(TODAY, item.d) <= days;

function downloadText(filename, content, mime = "text/plain") {
  const blob = new Blob(["\uFEFF" + content], { type: mime + ";charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename; a.click();
  URL.revokeObjectURL(url);
}

function csvEscape(v) {
  const s = String(v ?? "").replace(/\r?\n/g, " / ");
  return '"' + s.replace(/"/g, '""') + '"';
}

function tasksToCsv(tasks) {
  const rows = tasks.map(t => [
    t.id, t.createdAt, AFF[t.aff]?.name || t.aff, t.title, t.category,
    t.background || "", t.plan || "", t.risk, t.effect,
    t.kpiName, t.kpiFormula,
    (t.evidence || []).map(id => { const f = FEED_BY_ID[id]; return f ? `${f.src}(${f.d})` : id; }).join("; "),
    t.status, t.origin,
  ].map(csvEscape).join(","));
  return CSV_HEADERS.map(csvEscape).join(",") + "\n" + rows.join("\n");
}

function buildPrompt(affCodes, periodDays) {
  const affs = affCodes.length ? affCodes : AFFILIATES.map(a => a.code);
  const items = FEED.filter(f => inPeriod(f, periodDays) && f.tags.some(t => affs.includes(t)));
  const events = items.filter(f => f.kind !== "news");
  const news = items.filter(f => f.kind === "news");
  const line = (f) => `- [${md(f.d)} · ${KIND[f.kind].label} · ${f.src}] ${f.title} — ${f.sum} (관련: ${f.tags.join(", ")})`;
  const affNames = affs.map(c => AFF[c].name).join(", ");
  return [
    `# 외부 환경 브리핑 — ${affNames} (최근 ${periodDays}일)`,
    `기준일: ${TODAY} · 출처: DART/SEC/뉴스 (O/I Scout)`,
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

async function copyText(text) {
  try { await navigator.clipboard.writeText(text); return true; }
  catch {
    try {
      const ta = document.createElement("textarea");
      ta.value = text; document.body.appendChild(ta);
      ta.select(); document.execCommand("copy"); document.body.removeChild(ta);
      return true;
    } catch { return false; }
  }
}

/* ─────────────────────────── 과제 생성 (Claude API) ─────────────────────────── */

async function generateTasks(affCode, userNote) {
  const aff = AFF[affCode];
  const items = FEED.filter(f => inPeriod(f, 30) && f.tags.includes(affCode)).slice(0, 8);
  const ctx = items.map(f => `- (id:${f.id}) [${md(f.d)} · ${KIND[f.kind].label} · ${f.src}] ${f.title} — ${f.sum}`).join("\n");

  const system = [
    `너는 SK이노베이션 O/I추진단의 과제 발굴 애널리스트다. [외부 동향]과 [내부 현황]을 근거로 ${aff.name}에 적용 가능한 O/I(Operation Improvement) 과제 2건을 제안한다.`,
    `규칙:`,
    `- 출력은 JSON 배열만. 코드펜스·설명·주석 금지.`,
    `- 원소 스키마: {"title":"과제명","category":"레버 분류(에너지비/정비·TA/물류비/수율/구매/간접비/운전자본 중 택1 또는 유사)","background":"배경 1~2문장","plan":"실행방안 1~2문장","risk":"핵심 리스크 1문장","effect":"기대효과 1문장(정량 방향성 포함)","kpi":{"name":"지표명","formula":"산출식"},"evidence":["근거로 쓴 외부 동향 id"]}`,
    `- evidence는 [외부 동향]의 id에서만 고른다. 없으면 빈 배열.`,
    `- 확장 투자형보다 비용·효율·수익성 개선 과제를 우선한다. 문장은 짧고 구체적으로.`,
  ].join("\n");

  const user = [
    `[외부 동향] (최근 30일, ${aff.name} 관련)`,
    ctx || "- (해당 없음)",
    ``,
    `[내부 현황]`,
    userNote?.trim() || "(제공되지 않음 — 외부 동향만으로 제안)",
  ].join("\n");

  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-6",
      max_tokens: 1000,
      system,
      messages: [{ role: "user", content: user }],
    }),
  });
  if (!res.ok) throw new Error(`API 응답 오류 (${res.status})`);
  const data = await res.json();
  const text = (data.content || []).filter(b => b.type === "text").map(b => b.text).join("\n");
  const clean = text.replace(/```json|```/g, "").trim();
  const start = clean.indexOf("["), end = clean.lastIndexOf("]");
  if (start === -1 || end === -1) throw new Error("응답 형식을 해석하지 못했습니다.");
  const arr = JSON.parse(clean.slice(start, end + 1));
  if (!Array.isArray(arr) || !arr.length) throw new Error("생성된 과제가 없습니다.");
  return arr.map((t, i) => ({
    key: `gen-${Date.now()}-${i}`,
    aff: affCode,
    title: t.title || "무제 과제",
    category: t.category || "기타",
    background: t.background || "",
    plan: t.plan || "",
    risk: t.risk || "",
    effect: t.effect || "",
    kpi: { name: t.kpi?.name || "-", formula: t.kpi?.formula || "-" },
    evidence: (t.evidence || []).filter(id => FEED_BY_ID[id]),
  }));
}

/* ─────────────────────────── 공용 소품 ─────────────────────────── */

function AffTag({ code, onClick }) {
  const a = AFF[code]; if (!a) return null;
  return (
    <button className="tagchip" style={{ borderLeftColor: BIZ[a.biz].color }} onClick={onClick} title={BIZ[a.biz].label}>
      {a.code}
    </button>
  );
}

function KindBadge({ kind }) {
  return <span className={`badge ${KIND[kind].cls}`}>{KIND[kind].label}</span>;
}

function Formula({ name, formula }) {
  return (
    <div className="formula">
      <span className="formula-name">{name}</span>
      <span className="formula-eq">= {formula}</span>
    </div>
  );
}

function EvidenceChips({ ids, onOpen }) {
  if (!ids?.length) return <span className="dim-xs">근거 없음</span>;
  return (
    <span className="evd-wrap">
      {ids.map(id => {
        const f = FEED_BY_ID[id]; if (!f) return null;
        return (
          <button key={id} className="evd" onClick={() => onOpen(id)} title={f.title}>
            {f.src} <ChevronRight size={11} strokeWidth={2.5} />
          </button>
        );
      })}
    </span>
  );
}

/* ─────────────────────────── 메인 앱 ─────────────────────────── */

export default function App() {
  const [view, setView] = useState("dash");
  const [tasks, setTasks] = useState([]);
  const [loaded, setLoaded] = useState(false);
  const [highlight, setHighlight] = useState(null);

  // 대시보드 필터
  const [affSel, setAffSel] = useState([]);
  const [kindSel, setKindSel] = useState("all");
  const [period, setPeriod] = useState(30);
  const [exportOpen, setExportOpen] = useState(false);

  // 과제 생성
  const [genAff, setGenAff] = useState("SKGC");
  const [genNote, setGenNote] = useState("");
  const [genLoading, setGenLoading] = useState(false);
  const [genError, setGenError] = useState(null);
  const [genResults, setGenResults] = useState([]);
  const [savedKeys, setSavedKeys] = useState([]);

  // 저장 목록 선택
  const [checked, setChecked] = useState([]);

  // 봇 추가 상태
  const [botAdded, setBotAdded] = useState([]);

  /* 영속 저장 (artifact storage) */
  useEffect(() => {
    (async () => {
      try {
        const r = await window.storage.get("oi-scout:tasks");
        if (r?.value) setTasks(JSON.parse(r.value));
      } catch { /* 최초 실행 — 저장된 과제 없음 */ }
      setLoaded(true);
    })();
  }, []);
  useEffect(() => {
    if (!loaded) return;
    (async () => {
      try { await window.storage.set("oi-scout:tasks", JSON.stringify(tasks)); } catch { /* 저장 실패 시 세션 내 유지 */ }
    })();
  }, [tasks, loaded]);

  /* 파생 데이터 */
  const filtered = useMemo(() => FEED.filter(f => {
    if (!inPeriod(f, period)) return false;
    if (kindSel !== "all" && f.kind !== kindSel) return false;
    if (affSel.length && !f.tags.some(t => affSel.includes(t))) return false;
    return true;
  }), [affSel, kindSel, period]);
  const events = filtered.filter(f => f.kind !== "news");
  const news = filtered.filter(f => f.kind === "news");

  /* 액션 */
  const openEvidence = (id) => {
    setView("dash"); setHighlight(id);
    setTimeout(() => {
      document.getElementById("feed-" + id)?.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 60);
    setTimeout(() => setHighlight(h => (h === id ? null : h)), 3500);
  };

  const saveTask = (t, origin) => {
    const id = "OI-" + String(Date.now()).slice(-6);
    setTasks(prev => [{
      id, createdAt: TODAY, aff: t.aff, title: t.title, category: t.category,
      background: t.background || "", plan: t.plan || "",
      risk: t.risk, effect: t.effect,
      kpiName: t.kpi.name, kpiFormula: t.kpi.formula,
      evidence: t.evidence || [], status: "검토중", origin,
    }, ...prev]);
  };

  const toggleAff = (code) => setAffSel(s => s.includes(code) ? s.filter(c => c !== code) : [...s, code]);

  const runGenerate = async () => {
    setGenLoading(true); setGenError(null); setGenResults([]);
    try {
      const out = await generateTasks(genAff, genNote);
      setGenResults(out);
    } catch (e) {
      setGenError(e.message || "생성 중 오류가 발생했습니다.");
    } finally {
      setGenLoading(false);
    }
  };

  const ctxCount = useMemo(() => FEED.filter(f => inPeriod(f, 30) && f.tags.includes(genAff)).length, [genAff]);

  const allChecked = tasks.length > 0 && checked.length === tasks.length;
  const toggleAll = () => setChecked(allChecked ? [] : tasks.map(t => t.id));
  const downloadCsv = () => {
    const sel = tasks.filter(t => checked.includes(t.id));
    const rows = sel.length ? sel : tasks;
    downloadText(`OI_과제_${TODAY}.csv`, tasksToCsv(rows), "text/csv");
  };

  /* ───────── 렌더 ───────── */
  return (
    <div className="app">
      <StyleBlock />

      {/* 상단 바 */}
      <div className="topbar">
        <div className="brand">
          <span className="brand-mark">O/I</span>
          <span className="brand-name">Scout</span>
          <span className="brand-sub">신규 과제 발굴 · 데모</span>
        </div>
        <div className="topbar-right">
          <span className="mono dim">기준일 {TODAY}</span>
          <span className="sample-pill">샘플 데이터</span>
        </div>
      </div>

      <div className="frame">
        {/* 좌측 내비 */}
        <div className="rail">
          <NavBtn on={view === "dash"} onClick={() => setView("dash")} icon={<LayoutDashboard size={16} />} label="대시보드" />
          <NavBtn on={view === "gen"} onClick={() => setView("gen")} icon={<Wand2 size={16} />} label="과제 생성" />
          <NavBtn on={view === "saved"} onClick={() => setView("saved")} icon={<FolderCheck size={16} />} label="저장된 과제" count={tasks.length} />
          <NavBtn on={view === "bot"} onClick={() => setView("bot")} icon={<MessageSquare size={16} />} label="메신저 봇" />
        </div>

        {/* 본문 */}
        <div className="main">
          {view === "dash" && (
            <DashView
              affSel={affSel} toggleAff={toggleAff} clearAff={() => setAffSel([])}
              kindSel={kindSel} setKindSel={setKindSel}
              period={period} setPeriod={setPeriod}
              events={events} news={news} highlight={highlight}
              onOpenExport={() => setExportOpen(true)}
              onTagClick={(c) => { setAffSel([c]); }}
            />
          )}
          {view === "gen" && (
            <GenView
              genAff={genAff} setGenAff={setGenAff}
              genNote={genNote} setGenNote={setGenNote}
              loading={genLoading} error={genError} results={genResults}
              ctxCount={ctxCount} run={runGenerate}
              savedKeys={savedKeys}
              onSave={(t) => { saveTask(t, "생성"); setSavedKeys(k => [...k, t.key]); }}
              openEvidence={openEvidence}
            />
          )}
          {view === "saved" && (
            <SavedView
              tasks={tasks} checked={checked} setChecked={setChecked}
              allChecked={allChecked} toggleAll={toggleAll}
              downloadCsv={downloadCsv}
              removeChecked={() => { setTasks(ts => ts.filter(t => !checked.includes(t.id))); setChecked([]); }}
              goGen={() => setView("gen")} goBot={() => setView("bot")}
            />
          )}
          {view === "bot" && (
            <BotView
              botAdded={botAdded}
              onAdd={(p) => { saveTask(p, "봇"); setBotAdded(a => [...a, p.id]); }}
              openEvidence={openEvidence}
            />
          )}
        </div>
      </div>

      {exportOpen && (
        <ExportModal affSel={affSel} period={period} onClose={() => setExportOpen(false)} />
      )}
    </div>
  );
}

function NavBtn({ on, onClick, icon, label, count }) {
  return (
    <button className={`navbtn ${on ? "navbtn-on" : ""}`} onClick={onClick}>
      {icon}
      <span>{label}</span>
      {count > 0 && <span className="navcount mono">{count}</span>}
    </button>
  );
}

/* ─────────────────────────── 대시보드 ─────────────────────────── */

function DashView({ affSel, toggleAff, clearAff, kindSel, setKindSel, period, setPeriod, events, news, highlight, onOpenExport, onTagClick }) {
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>외부자료 대시보드</h1>
          <p className="lede">DART·SEC 공시와 뉴스를 계열사 태그로 정리합니다. 필요한 범위를 골라 LLM 프롬프트로 내보내세요.</p>
        </div>
        <button className="btn btn-primary" onClick={onOpenExport}>
          <FileText size={15} /> 프롬프트 내보내기
        </button>
      </div>

      {/* 필터 */}
      <div className="filterbar">
        <div className="filter-row">
          <span className="filter-label">계열사</span>
          <button className={`chip ${affSel.length === 0 ? "chip-on" : ""}`} onClick={clearAff}>전체</button>
          {AFFILIATES.map(a => (
            <button key={a.code} className={`chip ${affSel.includes(a.code) ? "chip-on" : ""}`}
              style={affSel.includes(a.code) ? { borderColor: BIZ[a.biz].color, color: BIZ[a.biz].color } : {}}
              onClick={() => toggleAff(a.code)}>
              {a.code}
            </button>
          ))}
        </div>
        <div className="filter-row">
          <span className="filter-label">유형</span>
          {[["all", "전체"], ["adhoc", "수시공시"], ["periodic", "정기공시"], ["sec", "SEC"], ["news", "뉴스"]].map(([k, l]) => (
            <button key={k} className={`chip ${kindSel === k ? "chip-on" : ""}`} onClick={() => setKindSel(k)}>{l}</button>
          ))}
          <span className="filter-sep" />
          <span className="filter-label">기간</span>
          {[7, 14, 30].map(d => (
            <button key={d} className={`chip ${period === d ? "chip-on" : ""}`} onClick={() => setPeriod(d)}>최근 {d}일</button>
          ))}
        </div>
      </div>

      {/* 이벤트 / 뉴스 */}
      <div className="grid-2">
        <FeedSection title="주요 이벤트" note="경쟁사 수시·정기 공시" items={events} highlight={highlight} onTagClick={onTagClick} />
        <FeedSection title="주요 뉴스" note="산업·정책·시황" items={news} highlight={highlight} onTagClick={onTagClick} />
      </div>

      <p className="foot-note">피드는 데모용 샘플입니다. 실서비스는 DART OpenAPI · SEC EDGAR · 뉴스 API 수집으로 대체 — 기획안 6장.</p>
    </div>
  );
}

function FeedSection({ title, note, items, highlight, onTagClick }) {
  return (
    <div className="card">
      <div className="card-head">
        <span className="eyebrow">{title}</span>
        <span className="dim-xs">{note} · {items.length}건</span>
      </div>
      {items.length === 0 && <div className="empty-sm">선택한 조건에 해당하는 항목이 없습니다. 필터를 넓혀보세요.</div>}
      {items.map(f => (
        <div key={f.id} id={"feed-" + f.id} className={`feed-item ${highlight === f.id ? "feed-hl" : ""}`}>
          <div className="feed-meta">
            <span className="mono dim">{md(f.d)}</span>
            <KindBadge kind={f.kind} />
            <span className="feed-src">{f.src}</span>
          </div>
          <div className="feed-title">{f.title}</div>
          <div className="feed-sum">{f.sum}</div>
          <div className="feed-tags">
            {f.tags.map(t => <AffTag key={t} code={t} onClick={() => onTagClick(t)} />)}
          </div>
        </div>
      ))}
    </div>
  );
}

/* ─────────────────────────── 프롬프트 내보내기 ─────────────────────────── */

function ExportModal({ affSel, period, onClose }) {
  const [copied, setCopied] = useState(false);
  const text = useMemo(() => buildPrompt(affSel, period), [affSel, period]);
  const scope = affSel.length ? affSel.join(", ") : "전체 계열사";
  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div className="modal-head">
          <div>
            <div className="eyebrow">프롬프트 내보내기</div>
            <div className="dim-xs">범위: {scope} · 최근 {period}일 — 증권사 리서치 PDF와 함께 사내 LLM에 붙여넣는 용도</div>
          </div>
          <button className="iconbtn" onClick={onClose} aria-label="닫기"><X size={16} /></button>
        </div>
        <textarea className="export-area mono" readOnly value={text} />
        <div className="modal-actions">
          <button className="btn btn-primary" onClick={async () => { const ok = await copyText(text); setCopied(ok); setTimeout(() => setCopied(false), 2000); }}>
            {copied ? <Check size={15} /> : <Copy size={15} />} {copied ? "복사됨" : "템플릿 복사"}
          </button>
          <button className="btn" onClick={() => downloadText(`외부환경브리핑_${TODAY}.md`, text, "text/markdown")}><Download size={15} /> .md</button>
          <button className="btn" onClick={() => downloadText(`외부환경브리핑_${TODAY}.txt`, text)}><Download size={15} /> .txt</button>
        </div>
      </div>
    </div>
  );
}

/* ─────────────────────────── 과제 생성 ─────────────────────────── */

function GenView({ genAff, setGenAff, genNote, setGenNote, loading, error, results, ctxCount, run, savedKeys, onSave, openEvidence }) {
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>과제 생성</h1>
          <p className="lede">내부 현황을 입력하면 최근 외부 동향과 결합해 과제 초안을 만듭니다. 마음에 들면 저장하세요.</p>
        </div>
      </div>

      <div className="grid-2">
        <div className="card">
          <div className="field">
            <span className="field-label">대상 계열사</span>
            <select className="select" value={genAff} onChange={e => setGenAff(e.target.value)}>
              {AFFILIATES.map(a => <option key={a.code} value={a.code}>{a.name} ({a.code})</option>)}
            </select>
          </div>
          <div className="field">
            <span className="field-label">내부 현황 (가정 입력)</span>
            <textarea
              className="textarea"
              rows={7}
              placeholder={"예) NCC 가동률 70%대, 8월 정기보수 예정. 전력비 부담 확대, 물류는 장기계약 만료 앞둠.\n비워두면 외부 동향만으로 제안합니다."}
              value={genNote}
              onChange={e => setGenNote(e.target.value)}
            />
          </div>
          <div className="ctx-note mono">컨텍스트: 최근 30일 {genAff} 관련 외부 동향 {ctxCount}건 자동 포함</div>
          <button className="btn btn-primary btn-wide" onClick={run} disabled={loading}>
            {loading ? <Loader2 size={15} className="spin" /> : <Wand2 size={15} />}
            {loading ? "생성 중…" : "과제 생성"}
          </button>
          {error && <div className="errbox"><AlertTriangle size={14} /> {error} — 잠시 후 다시 시도하세요.</div>}
        </div>

        <div>
          {results.length === 0 && !loading && (
            <div className="card empty-lg">
              <Wand2 size={20} className="dim" />
              <div>생성된 과제 초안이 여기에 표시됩니다.</div>
              <div className="dim-xs">계열사를 고르고 과제 생성을 누르세요.</div>
            </div>
          )}
          {results.map(t => (
            <div key={t.key} className="card task-card">
              <div className="task-head">
                <div>
                  <div className="task-title">{t.title}</div>
                  <div className="task-meta">
                    <AffTag code={t.aff} onClick={() => {}} />
                    <span className="cat">{t.category}</span>
                  </div>
                </div>
                <button className="btn btn-sm" disabled={savedKeys.includes(t.key)} onClick={() => onSave(t)}>
                  {savedKeys.includes(t.key) ? <><Check size={14} /> 저장됨</> : <><Plus size={14} /> 저장</>}
                </button>
              </div>
              <Row k="배경" v={t.background} />
              <Row k="실행방안" v={t.plan} />
              <Row k="리스크" v={t.risk} />
              <Row k="기대효과" v={t.effect} />
              <Formula name={t.kpi.name} formula={t.kpi.formula} />
              <div className="task-evd"><span className="rk">근거</span><EvidenceChips ids={t.evidence} onOpen={openEvidence} /></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function Row({ k, v }) {
  if (!v) return null;
  return <div className="row"><span className="rk">{k}</span><span className="rv">{v}</span></div>;
}

/* ─────────────────────────── 저장된 과제 ─────────────────────────── */

function SavedView({ tasks, checked, setChecked, allChecked, toggleAll, downloadCsv, removeChecked, goGen, goBot }) {
  const toggle = (id) => setChecked(c => c.includes(id) ? c.filter(x => x !== id) : [...c, id]);
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>저장된 과제</h1>
          <p className="lede">저장한 과제 인스턴스를 관리하고, 기존 과제 기록 DB와 같은 스키마의 CSV로 내려받습니다.</p>
        </div>
        <div className="head-actions">
          <button className="btn" onClick={downloadCsv} disabled={tasks.length === 0}>
            <Download size={15} /> CSV 내려받기{checked.length ? ` (${checked.length}건)` : " (전체)"}
          </button>
          <button className="btn btn-danger" onClick={removeChecked} disabled={checked.length === 0}>
            <Trash2 size={15} /> 선택 삭제
          </button>
        </div>
      </div>

      {tasks.length === 0 ? (
        <div className="card empty-lg">
          <FolderCheck size={20} className="dim" />
          <div>아직 저장된 과제가 없습니다.</div>
          <div className="empty-actions">
            <button className="btn btn-sm" onClick={goGen}>과제 생성하러 가기</button>
            <button className="btn btn-sm" onClick={goBot}>봇 제안 보기</button>
          </div>
        </div>
      ) : (
        <div className="card table-card">
          <table className="tbl">
            <thead>
              <tr>
                <th className="th-chk"><input type="checkbox" checked={allChecked} onChange={toggleAll} aria-label="전체 선택" /></th>
                <th>생성일</th><th>계열사</th><th>과제명</th><th>분류</th><th>KPI</th><th>상태</th><th>경로</th>
              </tr>
            </thead>
            <tbody>
              {tasks.map(t => (
                <tr key={t.id}>
                  <td className="th-chk"><input type="checkbox" checked={checked.includes(t.id)} onChange={() => toggle(t.id)} aria-label={t.title + " 선택"} /></td>
                  <td className="mono dim">{md(t.createdAt)}</td>
                  <td><span className="tagchip tagchip-static" style={{ borderLeftColor: BIZ[AFF[t.aff]?.biz || "energy"].color }}>{t.aff}</span></td>
                  <td className="td-title">{t.title}</td>
                  <td className="dim">{t.category}</td>
                  <td className="mono td-kpi" title={t.kpiFormula}>{t.kpiName}</td>
                  <td><span className="status">{t.status}</span></td>
                  <td className="dim-xs">{t.origin}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <p className="foot-note">CSV 컬럼은 기존 과제 기록 DB 스키마 기준으로 고정 — 실제 DB 컬럼 확인 후 매핑만 교체합니다(기획안 6.3). 저장 데이터는 이 기기의 아티팩트 저장소에 유지됩니다.</p>
    </div>
  );
}

/* ─────────────────────────── 메신저 봇 ─────────────────────────── */

function BotView({ botAdded, onAdd, openEvidence }) {
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>메신저 봇</h1>
          <p className="lede">매일 아침 과제 제안 Top N을 발송합니다. 아래는 오늘 발송분 시뮬레이션입니다.</p>
        </div>
      </div>

      <div className="chatwrap">
        <div className="chat-head">
          <Bell size={14} />
          <span>O/I Scout 봇 · #oi-과제발굴</span>
          <span className="dim-xs chat-note">매일 09:00 자동 발송 · 데모</span>
        </div>
        <div className="chat-body">
          <div className="chat-day mono">7월 22일 (수) 09:00</div>
          <div className="bubble">
            <div className="bubble-intro">오늘의 신규 과제 제안 <b>Top 3</b> — 최근 7일 외부 동향 기준</div>
            {BOT_SEED.map((p, i) => (
              <div key={p.id} className="bot-card">
                <div className="bot-rank mono">{String(i + 1).padStart(2, "0")}</div>
                <div className="bot-main">
                  <div className="bot-title">{p.title}</div>
                  <div className="task-meta">
                    <AffTag code={p.aff} onClick={() => {}} />
                    <span className="cat">{p.category}</span>
                  </div>
                  <Row k="리스크" v={p.risk} />
                  <Row k="기대효과" v={p.effect} />
                  <Formula name={p.kpi.name} formula={p.kpi.formula} />
                  <div className="task-evd">
                    <span className="rk">근거</span>
                    <EvidenceChips ids={p.evidence} onOpen={openEvidence} />
                  </div>
                  <button className="btn btn-sm" disabled={botAdded.includes(p.id)} onClick={() => onAdd(p)}>
                    {botAdded.includes(p.id) ? <><Check size={14} /> 추가됨</> : <><Plus size={14} /> 저장된 과제에 추가</>}
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <p className="foot-note">실서비스는 사내 메신저(Teams·카카오워크 등) 웹훅 발송으로 연결 — 기획안 5.2. 근거 버튼은 대시보드의 해당 항목으로 이동합니다.</p>
    </div>
  );
}

/* ─────────────────────────── 스타일 ─────────────────────────── */

function StyleBlock() {
  return (
    <style>{`
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

      .app {
        --paper:#F3F5F8; --panel:#FFFFFF; --ink:#17202E; --steel:#5C6B82;
        --line:#DFE5EC; --accent:#E4002B; --accent-soft:#FCE8EC;
        min-height:100vh; background:var(--paper); color:var(--ink);
        font-family:'IBM Plex Sans KR',-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;
        font-size:14px; line-height:1.55; -webkit-font-smoothing:antialiased;
      }
      .app *, .app *::before, .app *::after { box-sizing:border-box; }
      .mono { font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:0.86em; letter-spacing:-0.01em; }
      .dim { color:var(--steel); }
      .dim-xs { color:var(--steel); font-size:12px; }
      button { font-family:inherit; cursor:pointer; }
      .app :focus-visible { outline:2px solid var(--accent); outline-offset:2px; border-radius:3px; }
      @media (prefers-reduced-motion: reduce) { .app * { transition:none !important; animation:none !important; } }

      /* 상단 바 */
      .topbar { display:flex; justify-content:space-between; align-items:center; padding:14px 22px;
        background:var(--panel); border-bottom:1px solid var(--line); position:sticky; top:0; z-index:20; }
      .brand { display:flex; align-items:baseline; gap:8px; }
      .brand-mark { background:var(--accent); color:#fff; font-weight:700; font-size:12px;
        padding:3px 7px; letter-spacing:0.02em; }
      .brand-name { font-weight:700; font-size:17px; letter-spacing:-0.01em; }
      .brand-sub { color:var(--steel); font-size:12px; }
      .topbar-right { display:flex; align-items:center; gap:10px; font-size:12px; }
      .sample-pill { border:1px solid var(--line); color:var(--steel); padding:2px 8px; border-radius:99px; font-size:11px; }

      /* 프레임 */
      .frame { display:flex; max-width:1180px; margin:0 auto; }
      .rail { width:168px; flex:none; padding:18px 10px; display:flex; flex-direction:column; gap:4px; }
      .navbtn { display:flex; align-items:center; gap:9px; width:100%; padding:9px 11px;
        background:transparent; border:none; border-left:2px solid transparent; color:var(--steel);
        font-size:13.5px; text-align:left; transition:color .12s; }
      .navbtn:hover { color:var(--ink); }
      .navbtn-on { color:var(--ink); font-weight:600; border-left-color:var(--accent); background:var(--panel); }
      .navcount { margin-left:auto; background:var(--accent-soft); color:var(--accent);
        font-size:11px; padding:1px 6px; border-radius:99px; }
      .main { flex:1; min-width:0; padding:26px 22px 60px; }
      @media (max-width:820px) {
        .frame { flex-direction:column; }
        .rail { width:100%; flex-direction:row; overflow-x:auto; padding:10px 12px; border-bottom:1px solid var(--line); background:var(--panel); }
        .navbtn { border-left:none; border-bottom:2px solid transparent; white-space:nowrap; width:auto; }
        .navbtn-on { border-bottom-color:var(--accent); background:transparent; }
      }

      .page-head { display:flex; justify-content:space-between; align-items:flex-end; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
      .page-head h1 { font-size:19px; font-weight:700; margin:0 0 4px; letter-spacing:-0.01em; }
      .lede { margin:0; color:var(--steel); font-size:13px; max-width:520px; }
      .head-actions { display:flex; gap:8px; }

      /* 카드/피드 */
      .card { background:var(--panel); border:1px solid var(--line); padding:16px 18px; margin-bottom:16px; }
      .card-head { display:flex; justify-content:space-between; align-items:baseline; margin-bottom:10px; }
      .eyebrow { font-size:11.5px; font-weight:700; letter-spacing:0.08em; color:var(--ink); text-transform:uppercase; }
      .grid-2 { display:grid; grid-template-columns:1fr; gap:16px; }
      @media (min-width:900px) { .grid-2 { grid-template-columns:1fr 1fr; align-items:start; } }

      .feed-item { padding:11px 10px; border-top:1px solid var(--line); transition:background .15s; }
      .feed-item:hover { background:#FAFBFD; }
      .feed-hl { background:var(--accent-soft); box-shadow:inset 2px 0 0 var(--accent); }
      .feed-meta { display:flex; align-items:center; gap:8px; margin-bottom:3px; }
      .feed-src { font-size:12px; font-weight:600; }
      .feed-title { font-weight:600; font-size:13.5px; margin-bottom:2px; }
      .feed-sum { color:var(--steel); font-size:12.5px; margin-bottom:6px; }
      .feed-tags { display:flex; gap:5px; flex-wrap:wrap; }

      .badge { font-size:10.5px; font-weight:600; padding:1px 6px; border-radius:2px; letter-spacing:0.02em; }
      .badge-adhoc { background:#FDF3E3; color:#9A6413; }
      .badge-periodic { background:#E8EEF7; color:#3A5E8C; }
      .badge-sec { background:#EFEAF7; color:#5E4A9E; }
      .badge-news { background:#E7F1EC; color:#2E6B57; }

      .tagchip { font-family:'IBM Plex Mono',monospace; font-size:11px; color:var(--steel);
        background:#F7F8FA; border:1px solid var(--line); border-left:3px solid var(--steel);
        padding:1px 7px; transition:color .12s; }
      .tagchip:hover { color:var(--ink); }
      .tagchip-static { pointer-events:none; }

      /* 필터 */
      .filterbar { background:var(--panel); border:1px solid var(--line); padding:12px 16px; margin-bottom:16px;
        display:flex; flex-direction:column; gap:8px; }
      .filter-row { display:flex; align-items:center; gap:6px; flex-wrap:wrap; }
      .filter-label { font-size:11.5px; color:var(--steel); font-weight:600; margin-right:4px; min-width:36px; }
      .filter-sep { width:1px; height:16px; background:var(--line); margin:0 8px; }
      .chip { font-size:12px; padding:3px 10px; background:transparent; border:1px solid var(--line);
        border-radius:99px; color:var(--steel); transition:all .12s; }
      .chip:hover { border-color:var(--steel); color:var(--ink); }
      .chip-on { border-color:var(--ink); color:var(--ink); font-weight:600; }

      /* 버튼 */
      .btn { display:inline-flex; align-items:center; gap:6px; font-size:13px; padding:8px 14px;
        background:var(--panel); border:1px solid var(--line); color:var(--ink); transition:all .12s; }
      .btn:hover:not(:disabled) { border-color:var(--steel); }
      .btn:disabled { opacity:.5; cursor:default; }
      .btn-primary { background:var(--accent); border-color:var(--accent); color:#fff; font-weight:600; }
      .btn-primary:hover:not(:disabled) { background:#C50026; border-color:#C50026; }
      .btn-danger:hover:not(:disabled) { border-color:var(--accent); color:var(--accent); }
      .btn-sm { padding:5px 10px; font-size:12px; }
      .btn-wide { width:100%; justify-content:center; margin-top:4px; }
      .iconbtn { background:transparent; border:none; color:var(--steel); padding:4px; }
      .iconbtn:hover { color:var(--ink); }
      .spin { animation:oispin 0.9s linear infinite; }
      @keyframes oispin { to { transform:rotate(360deg); } }

      /* 폼 */
      .field { margin-bottom:12px; }
      .field-label { display:block; font-size:12px; font-weight:600; color:var(--steel); margin-bottom:5px; }
      .select, .textarea { width:100%; font-family:inherit; font-size:13.5px; color:var(--ink);
        background:#FAFBFD; border:1px solid var(--line); padding:9px 11px; }
      .textarea { resize:vertical; line-height:1.55; }
      .select:focus, .textarea:focus { outline:none; border-color:var(--steel); }
      .ctx-note { font-size:11.5px; color:var(--steel); background:#F7F8FA; border:1px dashed var(--line);
        padding:7px 10px; margin-bottom:10px; }
      .errbox { display:flex; align-items:center; gap:7px; margin-top:10px; padding:9px 11px;
        background:var(--accent-soft); color:#A3001F; font-size:12.5px; }

      /* 과제 카드 */
      .task-card { padding:15px 16px; }
      .task-head { display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom:8px; }
      .task-title { font-weight:700; font-size:14.5px; margin-bottom:5px; }
      .task-meta { display:flex; align-items:center; gap:7px; }
      .cat { font-size:11.5px; color:var(--steel); border:1px solid var(--line); padding:1px 7px; border-radius:99px; }
      .row { display:flex; gap:10px; padding:4px 0; font-size:13px; }
      .rk { flex:none; width:52px; color:var(--steel); font-size:12px; padding-top:1px; }
      .rv { flex:1; }
      .formula { display:flex; align-items:baseline; gap:8px; flex-wrap:wrap; margin:9px 0;
        border:1px solid var(--line); border-left:3px solid var(--ink); background:#FAFBFD; padding:8px 12px; }
      .formula-name { font-size:12px; font-weight:700; }
      .formula-eq { font-family:'IBM Plex Mono',monospace; font-size:12.5px; color:var(--ink); }
      .task-evd { display:flex; gap:10px; align-items:center; margin:6px 0 10px; }
      .evd-wrap { display:flex; gap:6px; flex-wrap:wrap; }
      .evd { display:inline-flex; align-items:center; gap:2px; font-size:11.5px; color:var(--steel);
        background:transparent; border:1px solid var(--line); padding:2px 8px; border-radius:99px; transition:all .12s; }
      .evd:hover { color:var(--accent); border-color:var(--accent); }

      /* 테이블 */
      .table-card { padding:0; overflow-x:auto; }
      .tbl { width:100%; border-collapse:collapse; font-size:13px; }
      .tbl th { text-align:left; font-size:11.5px; color:var(--steel); font-weight:600;
        padding:10px 12px; border-bottom:1px solid var(--line); white-space:nowrap; }
      .tbl td { padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top; }
      .tbl tr:last-child td { border-bottom:none; }
      .th-chk { width:34px; }
      .td-title { font-weight:600; min-width:180px; }
      .td-kpi { font-size:12px; }
      .status { font-size:11.5px; background:#F0F3F7; color:var(--steel); padding:2px 8px; border-radius:99px; }

      /* 모달 */
      .overlay { position:fixed; inset:0; background:rgba(23,32,46,0.45); z-index:50;
        display:flex; align-items:center; justify-content:center; padding:20px; }
      .modal { background:var(--panel); width:100%; max-width:680px; max-height:86vh;
        display:flex; flex-direction:column; border:1px solid var(--line); }
      .modal-head { display:flex; justify-content:space-between; align-items:flex-start;
        padding:16px 18px 10px; gap:10px; }
      .export-area { flex:1; min-height:300px; margin:0 18px; padding:12px; font-size:11.5px;
        line-height:1.6; border:1px solid var(--line); background:#FAFBFD; color:var(--ink); resize:none; }
      .modal-actions { display:flex; gap:8px; padding:14px 18px; }

      /* 봇 */
      .chatwrap { max-width:640px; background:var(--panel); border:1px solid var(--line); }
      .chat-head { display:flex; align-items:center; gap:8px; padding:11px 15px;
        border-bottom:1px solid var(--line); font-size:13px; font-weight:600; }
      .chat-note { margin-left:auto; font-weight:400; }
      .chat-body { background:#EEF1F5; padding:16px 14px 22px; }
      .chat-day { text-align:center; font-size:11px; color:var(--steel); margin-bottom:12px; }
      .bubble { background:var(--panel); border:1px solid var(--line); padding:13px 14px;
        max-width:560px; box-shadow:0 1px 2px rgba(23,32,46,0.05); }
      .bubble-intro { font-size:13.5px; margin-bottom:10px; }
      .bot-card { display:flex; gap:11px; border-top:1px solid var(--line); padding:12px 2px; }
      .bot-rank { flex:none; color:var(--accent); font-weight:600; font-size:13px; padding-top:2px; }
      .bot-main { flex:1; min-width:0; }
      .bot-title { font-weight:700; font-size:13.5px; margin-bottom:5px; }

      /* 기타 */
      .empty-sm { color:var(--steel); font-size:12.5px; padding:14px 6px; }
      .empty-lg { display:flex; flex-direction:column; align-items:center; gap:8px;
        padding:44px 20px; text-align:center; color:var(--steel); font-size:13.5px; }
      .empty-actions { display:flex; gap:8px; margin-top:4px; }
      .foot-note { color:var(--steel); font-size:11.5px; margin-top:4px; }
    `}</style>
  );
}
