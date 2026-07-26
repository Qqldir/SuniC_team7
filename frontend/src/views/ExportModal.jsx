import { useMemo, useState } from "react";
import { X, Copy, Check, Download } from "lucide-react";
import { TODAY } from "../data/affiliates.js";
import { buildPrompt } from "../lib/prompt.js";
import { copyText, downloadText } from "../lib/utils.js";

export default function ExportModal({ affSel, period, onClose }) {
  const [copied, setCopied] = useState(false);
  const text = useMemo(() => buildPrompt(affSel, period), [affSel, period]);
  const scope = affSel.length ? affSel.join(", ") : "전체 계열사";
  return (
    <div className="overlay" onClick={onClose}>
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <div className="modal-head">
          <div>
            <div className="eyebrow">프롬프트 내보내기</div>
            <div className="dim-xs">범위: {scope} · 최근 {period}일 — 증권사 리서치 PDF와 함께 사내 LLM에 붙여넣는 용도</div>
          </div>
          <button className="iconbtn" onClick={onClose} aria-label="닫기"><X size={16} /></button>
        </div>
        <textarea className="export-area mono" readOnly value={text} />
        <div className="modal-actions">
          <button
            className="btn btn-primary"
            onClick={async () => { const ok = await copyText(text); setCopied(ok); setTimeout(() => setCopied(false), 2000); }}
          >
            {copied ? <Check size={15} /> : <Copy size={15} />} {copied ? "복사됨" : "템플릿 복사"}
          </button>
          <button className="btn" onClick={() => downloadText(`외부환경브리핑_${TODAY}.md`, text, "text/markdown")}><Download size={15} /> .md</button>
          <button className="btn" onClick={() => downloadText(`외부환경브리핑_${TODAY}.txt`, text)}><Download size={15} /> .txt</button>
        </div>
      </div>
    </div>
  );
}
