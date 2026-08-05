/* 아직 trendroom.html 기준으로 구현 전인 화면용 임시 플레이스홀더 */
export default function Placeholder({ title, note }) {
  return (
    <>
      <div className="page-head">
        <div>
          <h1>{title}</h1>
          <p className="lede">{note || "이 화면은 다음 단계에서 trendroom.html 기준으로 구현됩니다."}</p>
        </div>
      </div>
      <div className="card" style={{ padding: 0 }}>
        <div className="empty2" style={{ padding: "64px 20px" }}>
          <span style={{ fontSize: 15, fontWeight: 700 }}>🚧 준비 중</span>
          <span className="note">{title} 화면은 곧 이어서 만들어 드릴게요.</span>
        </div>
      </div>
    </>
  );
}
