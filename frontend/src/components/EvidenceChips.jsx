import { ChevronRight } from "lucide-react";
import { FEED_BY_ID } from "../data/feed.js";

export default function EvidenceChips({ ids, onOpen }) {
  if (!ids?.length) return <span className="dim-xs">근거 없음</span>;
  return (
    <span className="evd-wrap">
      {ids.map((id) => {
        const f = FEED_BY_ID[id];
        if (!f) return null;
        return (
          <button key={id} className="evd" onClick={() => onOpen(id)} title={f.title}>
            {f.src} <ChevronRight size={11} strokeWidth={2.5} />
          </button>
        );
      })}
    </span>
  );
}
