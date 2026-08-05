import { useState, useEffect, useMemo } from "react";
import { NavLink, Routes, Route, useNavigate } from "react-router-dom";

import { TODAY, AFFILIATES, AFF } from "./data/affiliates.js";
import { FEED } from "./data/feed.js";
import { inPeriod } from "./lib/utils.js";
import { tasksToCsv } from "./lib/csv.js";
import { downloadText } from "./lib/utils.js";
import { generateTasks, fetchTasks, createTask, deleteTasks } from "./lib/api.js";

import ThemeToggle from "./components/ThemeToggle.jsx";
import DashView from "./views/DashView.jsx";
import GenView from "./views/GenView.jsx";
import SavedView from "./views/SavedView.jsx";
import BotView from "./views/BotView.jsx";
import CasesView from "./views/CasesView.jsx";
import TrendView from "./views/TrendView.jsx";
import Placeholder from "./views/Placeholder.jsx";
import ExportModal from "./views/ExportModal.jsx";

/* 사이드바 네비 링크 (trendroom.html NAV 구조: 글리프 아이콘 + 카운트) */
function Nav({ to, glyph, label, count, end }) {
  return (
    <NavLink to={to} end={end} className={({ isActive }) => "nav-b" + (isActive ? " on" : "")}>
      <span className="nav-i">{glyph}</span>
      <span>{label}</span>
      {count != null && <span className="nav-c num">{count}</span>}
    </NavLink>
  );
}

export default function App() {
  const navigate = useNavigate();

  const [tasks, setTasks] = useState([]);
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

  /* 영속 저장 — 백엔드 SQLite (미연결 시 localStorage 폴백, lib/api.js) */
  useEffect(() => {
    (async () => {
      const loaded = await fetchTasks();
      setTasks(loaded);
    })();
  }, []);

  /* 파생 데이터 */
  const filtered = useMemo(
    () =>
      FEED.filter((f) => {
        if (!inPeriod(f, period)) return false;
        if (kindSel !== "all" && f.kind !== kindSel) return false;
        if (affSel.length && !f.tags.some((t) => affSel.includes(t))) return false;
        return true;
      }),
    [affSel, kindSel, period]
  );
  const events = filtered.filter((f) => f.kind !== "news");
  const news = filtered.filter((f) => f.kind === "news");

  /* 액션 */
  const openEvidence = (id) => {
    navigate("/");
    setHighlight(id);
    setTimeout(() => {
      document.getElementById("feed-" + id)?.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 80);
    setTimeout(() => setHighlight((h) => (h === id ? null : h)), 3500);
  };

  const saveTask = async (t, origin) => {
    const draft = {
      createdAt: TODAY, aff: t.aff, title: t.title, category: t.category,
      background: t.background || "", plan: t.plan || "",
      risk: t.risk, effect: t.effect,
      kpiName: t.kpi.name, kpiFormula: t.kpi.formula,
      evidence: t.evidence || [], status: "검토중", origin,
    };
    const saved = await createTask(draft);
    setTasks((prev) => [saved, ...prev]);
  };

  const toggleAff = (code) =>
    setAffSel((s) => (s.includes(code) ? s.filter((c) => c !== code) : [...s, code]));

  const runGenerate = async () => {
    setGenLoading(true);
    setGenError(null);
    setGenResults([]);
    try {
      const out = await generateTasks(genAff, genNote);
      setGenResults(out);
    } catch (e) {
      setGenError(e.message || "생성 중 오류가 발생했습니다.");
    } finally {
      setGenLoading(false);
    }
  };

  const ctxCount = useMemo(
    () => FEED.filter((f) => inPeriod(f, 30) && f.tags.includes(genAff)).length,
    [genAff]
  );

  const allChecked = tasks.length > 0 && checked.length === tasks.length;
  const toggleAll = () => setChecked(allChecked ? [] : tasks.map((t) => t.id));
  const downloadCsv = () => {
    const sel = tasks.filter((t) => checked.includes(t.id));
    const rows = sel.length ? sel : tasks;
    downloadText(`OI_과제_${TODAY}.csv`, tasksToCsv(rows), "text/csv");
  };
  const removeChecked = async () => {
    await deleteTasks(checked);
    setTasks((ts) => ts.filter((t) => !checked.includes(t.id)));
    setChecked([]);
  };

  /* 라우트 공용 엘리먼트 */
  const dashEl = (
    <DashView
      affSel={affSel} toggleAff={toggleAff} clearAff={() => setAffSel([])}
      kindSel={kindSel} setKindSel={setKindSel}
      period={period} setPeriod={setPeriod}
      events={events} news={news} highlight={highlight}
      onOpenExport={() => setExportOpen(true)}
      onTagClick={(c) => setAffSel([c])}
    />
  );
  const genEl = (
    <GenView
      genAff={genAff} setGenAff={setGenAff}
      genNote={genNote} setGenNote={setGenNote}
      loading={genLoading} error={genError} results={genResults}
      ctxCount={ctxCount} run={runGenerate}
      savedKeys={savedKeys}
      onSave={(t) => { saveTask(t, "생성"); setSavedKeys((k) => [...k, t.key]); }}
      openEvidence={openEvidence}
    />
  );
  const savedEl = (
    <SavedView
      tasks={tasks} checked={checked} setChecked={setChecked}
      allChecked={allChecked} toggleAll={toggleAll}
      downloadCsv={downloadCsv}
      removeChecked={removeChecked}
      goGen={() => navigate("/custom")} goBot={() => navigate("/reporting")}
    />
  );
  const botEl = (
    <BotView
      botAdded={botAdded}
      onAdd={(p) => { saveTask(p, "봇"); setBotAdded((a) => [...a, p.id]); }}
      openEvidence={openEvidence}
    />
  );

  /* ───────── 렌더 ───────── */
  return (
    <div className="app">
      {/* 좌측 사이드바 (trendroom.html 구조) */}
      <aside className="side">
        <div className="brand">
          <span className="brand-mark">O/I</span>
          <div>
            <div className="brand-name">O/I Spark</div>
            <div className="brand-sub">SK이노베이션 O/I추진단</div>
          </div>
          <ThemeToggle />
        </div>

        <nav className="nav">
          <div className="nav-g">
            <div className="nav-t">발굴</div>
            <Nav to="/" end glyph="≡" label="과제 제안" count={tasks.length} />
            <Nav to="/custom" glyph="+" label="커스텀 생성" />
          </div>
          <div className="nav-g">
            <div className="nav-t">활용</div>
            <Nav to="/trend" glyph="T" label="트렌드룸" />
            <Nav to="/export" glyph="›" label="프롬프트 내보내기" />
            <Nav to="/reporting" glyph="↗" label="AI Reporting" />
          </div>
          <div className="nav-g">
            <div className="nav-t">관리</div>
            <Nav to="/admin" glyph="⚙" label="관리자" />
          </div>

          <div className="pipe">
            <div className="pipe-h">
              <span className="pipe-t">수집 파이프라인</span>
              <span className="pipe-ok">정상</span>
            </div>
            <div className="pipe-r"><span className="dot" style={{ background: "var(--ok)" }} />크롤링 · 오늘 08:00 완료</div>
            <div className="pipe-r"><span className="dot" style={{ background: "var(--warn)" }} />유료 매체 4건 · 계정 필요</div>
            <div className="pipe-r"><span className="dot" style={{ background: "var(--steel)" }} />수집 주기 · 4시간</div>
          </div>
        </nav>
      </aside>

      {/* 본문 */}
      <div className="body">
        <main className="main">
          <Routes>
            <Route index element={dashEl} />
            <Route path="custom" element={genEl} />
            <Route path="trend" element={<TrendView />} />
            <Route path="export" element={<Placeholder title="프롬프트 내보내기" />} />
            <Route path="reporting" element={botEl} />
            <Route path="admin" element={<Placeholder title="관리자" />} />
            {/* 레거시/보조 라우트 (사이드바 외) */}
            <Route path="gen" element={genEl} />
            <Route path="cases" element={<CasesView />} />
            <Route path="saved" element={savedEl} />
            <Route path="*" element={dashEl} />
          </Routes>
        </main>
      </div>

      {exportOpen && <ExportModal affSel={affSel} period={period} onClose={() => setExportOpen(false)} />}
    </div>
  );
}
