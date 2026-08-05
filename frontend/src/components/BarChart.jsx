import { useState } from "react";

/* 일별 생성 건수 — 단일 시리즈 세로 막대. 막대 호버 시 툴팁. */
function ticks(max) {
  const step = Math.max(1, Math.ceil(max / 4));
  return { top: step * 4, arr: [4, 3, 2, 1, 0].map((i) => i * step) };
}

export default function BarChart({ data, total }) {
  const [hover, setHover] = useState(null);
  const max = Math.max(1, ...data.map((d) => d.n));
  const t = ticks(max);

  return (
    <div className="card chart-card">
      <div className="card-h">
        <h2>일별 생성 건수</h2>
        <span className="note">총 {total ?? data.reduce((a, b) => a + b.n, 0)}건</span>
      </div>
      <div className="cwrap">
        <div className="crow crow-plot">
          <div className="cyax">
            {t.arr.map((v, i) => <span key={i}>{v}</span>)}
          </div>
          <div className="cplot">
            <div className="cgrid">
              {[0, 1, 2, 3, 4].map((i) => <span key={i} />)}
            </div>
            <div className="cbars">
              {data.map((d, i) => (
                <button
                  key={i}
                  className="cb"
                  onMouseEnter={() => setHover(i)}
                  onMouseLeave={() => setHover((h) => (h === i ? null : h))}
                >
                  {hover === i && (
                    <span className="ctip">
                      <span className="ctip-d">{d.label}</span>
                      <span className="ctip-r">생성<span className="ctip-v">{d.n}건</span></span>
                    </span>
                  )}
                  <span
                    className="cbar"
                    style={{ height: `${((d.n / t.top) * 100).toFixed(2)}%` }}
                  />
                </button>
              ))}
            </div>
          </div>
        </div>
        <div className="crow">
          <div className="cyax sp" />
          <div className="cxax">
            {data.map((d, i) => (
              <span key={i} className="cx">{d.label.slice(5)}</span>
            ))}
          </div>
        </div>
      </div>
      <div className="clg">
        <span className="note">막대에 마우스를 올리면 해당 날짜 생성 건수를 볼 수 있습니다</span>
      </div>
    </div>
  );
}
