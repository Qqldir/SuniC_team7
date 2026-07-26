export default function Row({ k, v }) {
  if (!v) return null;
  return (
    <div className="row">
      <span className="rk">{k}</span>
      <span className="rv">{v}</span>
    </div>
  );
}
