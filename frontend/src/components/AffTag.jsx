import { AFF, BIZ } from "../data/affiliates.js";

export default function AffTag({ code, onClick }) {
  const a = AFF[code];
  if (!a) return null;
  return (
    <button
      className="tagchip"
      style={{ borderLeftColor: BIZ[a.biz].color }}
      onClick={onClick}
      title={BIZ[a.biz].label}
    >
      {a.label || a.code}
    </button>
  );
}
