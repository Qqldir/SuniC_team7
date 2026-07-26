export default function Formula({ name, formula }) {
  return (
    <div className="formula">
      <span className="formula-name">{name}</span>
      <span className="formula-eq">= {formula}</span>
    </div>
  );
}
