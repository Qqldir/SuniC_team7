import { KIND } from "../data/affiliates.js";

export default function KindBadge({ kind }) {
  return <span className={`badge ${KIND[kind].cls}`}>{KIND[kind].label}</span>;
}
