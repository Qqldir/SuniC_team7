import { Wand2, Loader2, AlertTriangle, Check, Plus } from "lucide-react";
import { AFFILIATES } from "../data/affiliates.js";
import AffTag from "../components/AffTag.jsx";
import Formula from "../components/Formula.jsx";
import EvidenceChips from "../components/EvidenceChips.jsx";
import Row from "../components/Row.jsx";

export default function GenView({
  genAff, setGenAff, genNote, setGenNote,
  loading, error, results, ctxCount, run, savedKeys, onSave, openEvidence,
}) {
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
            <select className="select" value={genAff} onChange={(e) => setGenAff(e.target.value)}>
              {AFFILIATES.map((a) => <option key={a.code} value={a.code}>{a.name}</option>)}
            </select>
          </div>
          <div className="field">
            <span className="field-label">내부 현황 (가정 입력)</span>
            <textarea
              className="textarea"
              rows={7}
              placeholder={"예) NCC 가동률 70%대, 8월 정기보수 예정. 전력비 부담 확대, 물류는 장기계약 만료 앞둠.\n비워두면 외부 동향만으로 제안합니다."}
              value={genNote}
              onChange={(e) => setGenNote(e.target.value)}
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
          {results.map((t) => (
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
