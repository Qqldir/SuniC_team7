import { FileText } from "lucide-react";
import { AFFILIATES, BIZ } from "../data/affiliates.js";
import { md } from "../lib/utils.js";
import AffTag from "../components/AffTag.jsx";
import KindBadge from "../components/KindBadge.jsx";

export default function DashView({
  affSel, toggleAff, clearAff, kindSel, setKindSel,
  period, setPeriod, events, news, highlight, onOpenExport, onTagClick,
}) {
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
          {AFFILIATES.map((a) => (
            <button
              key={a.code}
              className={`chip ${affSel.includes(a.code) ? "chip-on" : ""}`}
              style={affSel.includes(a.code) ? { borderColor: BIZ[a.biz].color, color: BIZ[a.biz].color } : {}}
              onClick={() => toggleAff(a.code)}
            >
              {a.label || a.code}
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
          {[7, 14, 30].map((d) => (
            <button key={d} className={`chip ${period === d ? "chip-on" : ""}`} onClick={() => setPeriod(d)}>최근 {d}일</button>
          ))}
        </div>
      </div>

      {/* 이벤트 / 뉴스 */}
      <div className="grid-2">
        <FeedSection title="주요 이벤트" note="경쟁사 수시·정기 공시" items={events} highlight={highlight} onTagClick={onTagClick} clamp />
        <FeedSection title="주요 뉴스" note="산업·정책·시황" items={news} highlight={highlight} onTagClick={onTagClick} clamp />
      </div>

      <p className="foot-note">피드는 데모용 샘플입니다. 실서비스는 DART OpenAPI · SEC EDGAR · 뉴스 API 수집으로 대체 — 기획안 6장.</p>
    </div>
  );
}

function FeedSection({ title, note, items, highlight, onTagClick, clamp }) {
  return (
    <div className="card">
      <div className="card-head">
        <span className="eyebrow">{title}</span>
        <span className="dim-xs">{note} · {items.length}건</span>
      </div>
      {items.length === 0 && <div className="empty-sm">선택한 조건에 해당하는 항목이 없습니다. 필터를 넓혀보세요.</div>}
      {items.map((f) => (
        <div key={f.id} id={"feed-" + f.id} className={`feed-item ${highlight === f.id ? "feed-hl" : ""}`}>
          <div className="feed-meta">
            <span className="mono dim">{md(f.d)}</span>
            <KindBadge kind={f.kind} />
            <span className="feed-src">{f.src}</span>
          </div>
          <div className="feed-title">{f.title}</div>
          <div className={`feed-sum ${clamp ? "feed-clamp" : ""}`}>{f.sum}</div>
          <div className="feed-tags">
            {f.tags.map((t) => <AffTag key={t} code={t} onClick={() => onTagClick(t)} />)}
          </div>
        </div>
      ))}
    </div>
  );
}
