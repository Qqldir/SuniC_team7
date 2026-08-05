import { QUOTES, quoteUrl } from "../data/trend.js";

/* 시황 티커 — 좌우로 흐르는 종목 시세. 호버 시 멈춤. */
export default function Ticker({ onTrend }) {
  const items = QUOTES.map((q, i) => {
    const up = q.c > 0;
    return (
      <a
        key={i}
        className={"tk-i" + (q.sk ? " sk" : "")}
        href={quoteUrl(q.cd)}
        target="_blank"
        rel="noopener noreferrer"
        title={`${q.n} 시세·트렌드 보기`}
      >
        <span className="tk-nm">{q.n}</span>
        <span className="tk-p num">{q.p}</span>
        <span className={"tk-c num " + (up ? "up" : "dn")}>
          {up ? "▲" : "▼"} {Math.abs(q.c).toFixed(2)}%
        </span>
        <span className="tk-go">↗</span>
      </a>
    );
  });

  return (
    <div className="ticker">
      <div className="tk-view">
        <div className="tk-track">{items}{items}</div>
      </div>
      {onTrend && (
        <button className="tk-btn" onClick={onTrend}>트렌드룸</button>
      )}
    </div>
  );
}
