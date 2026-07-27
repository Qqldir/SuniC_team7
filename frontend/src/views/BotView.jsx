import { Bell, Check, Plus } from "lucide-react";
import { BOT_SEED } from "../data/botSeed.js";
import AffTag from "../components/AffTag.jsx";
import Formula from "../components/Formula.jsx";
import EvidenceChips from "../components/EvidenceChips.jsx";
import Row from "../components/Row.jsx";

export default function BotView({ botAdded, onAdd, openEvidence }) {
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>AI Reporting</h1>
          <p className="lede">매일 아침 과제 제안 Top N을 발송합니다. 아래는 오늘 발송분 시뮬레이션입니다.</p>
        </div>
      </div>

      <div className="chatwrap">
        <div className="chat-head">
          <Bell size={14} />
          <span>O/I 변경 검토 · #oi-과제발굴</span>
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
