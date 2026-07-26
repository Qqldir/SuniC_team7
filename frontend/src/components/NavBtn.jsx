export default function NavBtn({ on, onClick, icon, label, count }) {
  return (
    <button className={`navbtn ${on ? "navbtn-on" : ""}`} onClick={onClick}>
      {icon}
      <span>{label}</span>
      {count > 0 && <span className="navcount mono">{count}</span>}
    </button>
  );
}
