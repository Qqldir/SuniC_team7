import { useState, useEffect } from "react";
import { Lightbulb, Plus, Check, X, Trash2, ExternalLink } from "lucide-react";
import { AFFILIATES } from "../data/affiliates.js";
import { fetchCases, createCase, updateCaseStatus, deleteCase } from "../lib/api.js";
import AffTag from "../components/AffTag.jsx";
import Formula from "../components/Formula.jsx";
import Row from "../components/Row.jsx";

// 자주 쓰는 레버 분류 (입력 자동완성용)
const LEVERS = ["에너지비", "정비/TA", "물류비", "수율", "구매", "간접비", "운전자본", "가동률"];

const EMPTY = {
  title: "", category: "", background: "", effect: "",
  kpiName: "", kpiFormula: "", sourceOrg: "", sourceRef: "", affiliates: [],
};

const STATUS = {
  pending:  { label: "검토대기", cls: "badge-pending" },
  approved: { label: "승인됨",   cls: "badge-approved" },
  rejected: { label: "반려",     cls: "badge-rejected" },
};
const SRC = { manual: "수기입력", ai: "AI추출", auto: "자동수집" };

export default function CasesView() {
  const [cases, setCases] = useState([]);
  const [filter, setFilter] = useState("pending");
  const [form, setForm] = useState(EMPTY);
  const [saving, setSaving] = useState(false);
  const [msg, setMsg] = useState(null);

  const load = async () => setCases(await fetchCases());
  useEffect(() => { load(); }, []);

  const counts = {
    all: cases.length,
    pending: cases.filter((c) => c.status === "pending").length,
    approved: cases.filter((c) => c.status === "approved").length,
  };
  const shown = cases.filter((c) => (filter === "all" ? true : c.status === filter));

  const setField = (k, v) => setForm((f) => ({ ...f, [k]: v }));
  const toggleAff = (code) =>
    setForm((f) => ({
      ...f,
      affiliates: f.affiliates.includes(code)
        ? f.affiliates.filter((x) => x !== code)
        : [...f.affiliates, code],
    }));

  const submit = async () => {
    if (!form.title.trim()) { setMsg("사례명을 입력하세요."); return; }
    setSaving(true); setMsg(null);
    try {
      await createCase({
        ...form,
        kpiName: form.kpiName || "-",
        kpiFormula: form.kpiFormula || "-",
        sourceType: "manual",
        status: "approved",
      });
      setForm(EMPTY);
      setMsg("저장되었습니다.");
      await load();
    } catch {
      setMsg("저장 실패 — 백엔드가 실행 중인지 확인하세요.");
    } finally {
      setSaving(false);
    }
  };

  const changeStatus = async (id, status) => { await updateCaseStatus(id, status); await load(); };
  const remove = async (id) => { await deleteCase(id); await load(); };

  return (
    <div>
      <div className="page-head">
        <div>
          <h1>혁신 사례 모음</h1>
          <p className="lede">경쟁사·업계의 개선 사례를 쌓아 과제 발굴의 근거로 씁니다. 직접 입력한 사례는 바로 승인되고, AI가 추출한 사례는 검토 후 승인하세요.</p>
        </div>
      </div>

      <div className="grid-2">
        {/* ── 입력 폼 ── */}
        <div className="card">
          <div className="card-head"><span className="eyebrow">새 사례 입력</span></div>

          <div className="field">
            <span className="field-label">사례명 *</span>
            <input className="input" value={form.title} onChange={(e) => setField("title", e.target.value)}
              placeholder="예) 폐열 회수로 스팀 사용량 절감" />
          </div>

          <div className="field-2">
            <div className="field">
              <span className="field-label">레버 분류</span>
              <input className="input" list="lever-list" value={form.category}
                onChange={(e) => setField("category", e.target.value)} placeholder="예) 에너지비" />
              <datalist id="lever-list">
                {LEVERS.map((l) => <option key={l} value={l} />)}
              </datalist>
            </div>
            <div className="field">
              <span className="field-label">사례 주체</span>
              <input className="input" value={form.sourceOrg}
                onChange={(e) => setField("sourceOrg", e.target.value)} placeholder="예) BASF" />
            </div>
          </div>

          <div className="field">
            <span className="field-label">배경·내용</span>
            <textarea className="textarea" rows={3} value={form.background}
              onChange={(e) => setField("background", e.target.value)}
              placeholder="어떤 회사가 무엇을 했는지 1~2문장" />
          </div>

          <div className="field">
            <span className="field-label">기대효과</span>
            <input className="input" value={form.effect}
              onChange={(e) => setField("effect", e.target.value)}
              placeholder="정량 방향성 포함 1문장" />
          </div>

          <div className="field-2">
            <div className="field">
              <span className="field-label">KPI 지표명</span>
              <input className="input" value={form.kpiName}
                onChange={(e) => setField("kpiName", e.target.value)} placeholder="예) 스팀 원단위" />
            </div>
            <div className="field">
              <span className="field-label">KPI 산출식</span>
              <input className="input" value={form.kpiFormula}
                onChange={(e) => setField("kpiFormula", e.target.value)} placeholder="예) 스팀사용량 ÷ 생산량" />
            </div>
          </div>

          <div className="field">
            <span className="field-label">근거 (링크 또는 크롤 id, 선택)</span>
            <input className="input" value={form.sourceRef}
              onChange={(e) => setField("sourceRef", e.target.value)} placeholder="예) https://... 또는 e03" />
          </div>

          <div className="field">
            <span className="field-label">적용 계열사</span>
            <div className="aff-pick">
              {AFFILIATES.map((a) => (
                <button key={a.code} type="button"
                  className={`chip ${form.affiliates.includes(a.code) ? "chip-on" : ""}`}
                  onClick={() => toggleAff(a.code)}>
                  {a.label || a.code}
                </button>
              ))}
            </div>
          </div>

          <button className="btn btn-primary btn-wide" onClick={submit} disabled={saving}>
            <Plus size={15} /> {saving ? "저장 중…" : "사례 저장"}
          </button>
          {msg && <div className="ctx-note mono" style={{ marginTop: 10, marginBottom: 0 }}>{msg}</div>}
        </div>

        {/* ── 목록 + 검토 ── */}
        <div>
          <div className="filter-row" style={{ marginBottom: 12 }}>
            {[
              ["pending", `검토대기 ${counts.pending}`],
              ["approved", `승인됨 ${counts.approved}`],
              ["all", `전체 ${counts.all}`],
            ].map(([k, l]) => (
              <button key={k} className={`chip ${filter === k ? "chip-on" : ""}`} onClick={() => setFilter(k)}>{l}</button>
            ))}
          </div>

          {shown.length === 0 ? (
            <div className="card empty-lg">
              <Lightbulb size={20} className="dim" />
              <div>{filter === "pending" ? "검토할 사례가 없습니다." : "표시할 사례가 없습니다."}</div>
              <div className="dim-xs">왼쪽에서 새 사례를 입력하거나 필터를 바꿔보세요.</div>
            </div>
          ) : (
            shown.map((c) => (
              <CaseCard key={c.id} c={c} onStatus={changeStatus} onDelete={remove} />
            ))
          )}
        </div>
      </div>
    </div>
  );
}

function CaseCard({ c, onStatus, onDelete }) {
  const st = STATUS[c.status] || STATUS.approved;
  return (
    <div className="card task-card">
      <div className="task-head">
        <div>
          <div className="task-title">{c.title}</div>
          <div className="case-badges">
            <span className={`badge ${st.cls}`}>{st.label}</span>
            <span className="badge badge-src">{SRC[c.sourceType] || c.sourceType}</span>
            {c.category && <span className="cat">{c.category}</span>}
          </div>
        </div>
      </div>

      <div className="task-meta" style={{ margin: "8px 0" }}>
        {c.affiliates.map((code) => <AffTag key={code} code={code} onClick={() => {}} />)}
      </div>

      <Row k="배경" v={c.background} />
      <Row k="효과" v={c.effect} />
      {c.kpi && c.kpi.name !== "-" && <Formula name={c.kpi.name} formula={c.kpi.formula} />}
      <div className="row">
        <span className="rk">출처</span>
        <span className="rv dim">
          {c.sourceOrg || "-"}
          {c.sourceRef && (
            /^https?:\/\//.test(c.sourceRef)
              ? <a href={c.sourceRef} target="_blank" rel="noreferrer" style={{ marginLeft: 6 }}>
                  링크 <ExternalLink size={11} />
                </a>
              : <span className="mono" style={{ marginLeft: 6 }}>({c.sourceRef})</span>
          )}
        </span>
      </div>

      <div className="case-actions">
        {c.status === "pending" && (
          <>
            <button className="btn btn-primary btn-sm" onClick={() => onStatus(c.id, "approved")}>
              <Check size={14} /> 승인
            </button>
            <button className="btn btn-sm" onClick={() => onStatus(c.id, "rejected")}>
              <X size={14} /> 반려
            </button>
          </>
        )}
        {c.status === "rejected" && (
          <button className="btn btn-sm" onClick={() => onStatus(c.id, "approved")}>
            <Check size={14} /> 되살리기
          </button>
        )}
        <span className="spacer" />
        <button className="btn btn-sm btn-danger" onClick={() => onDelete(c.id)} title="삭제">
          <Trash2 size={14} />
        </button>
      </div>
    </div>
  );
}
