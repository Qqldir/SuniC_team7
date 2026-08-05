import { useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { pctRound } from "../data/trend.js";

/* OC별 구성 — SVG 도넛(stroke-dasharray) + 순위 범례.
 * 색상은 사업부문 램프이지만 범례에 이름·건수·비율을 함께 표기해
 * 식별을 색상 단독에 의존하지 않음. 조각 호버 시 나머지를 흐리게.
 * 헤더의 ‹ › 로 월 이동. */
export default function Donut({ rows, names, colors, monthLabel, onPrev, onNext, prevDisabled, nextDisabled }) {
  const [hover, setHover] = useState(null);
  const tot = rows.reduce((a, b) => a + b.c, 0);

  const header = (
    <div className="card-h">
      <h2>OC별 구성</h2>
      <div className="head-actions" style={{ marginLeft: "auto" }}>
        <button className="cnav" disabled={prevDisabled} onClick={onPrev} title="이전 달">
          <ChevronLeft size={15} />
        </button>
        <button className="cnav" disabled={nextDisabled} onClick={onNext} title="다음 달">
          <ChevronRight size={15} />
        </button>
      </div>
    </div>
  );

  if (!tot) {
    return (
      <div className="card chart-card">
        {header}
        <div className="empty">해당 월 생성분이 없습니다</div>
      </div>
    );
  }

  const pr = pctRound(rows.map((r) => r.c), tot);
  const maxC = rows[0].c;

  let acc = 0;
  const slices = rows.map((r) => {
    const pct = (r.c / tot) * 100;
    const el = (
      <circle
        key={r.oc}
        className="psl"
        r="15.915"
        cx="21"
        cy="21"
        fill="transparent"
        stroke={colors[r.oc]}
        strokeWidth="6"
        strokeDasharray={`${pct.toFixed(3)} ${(100 - pct).toFixed(3)}`}
        strokeDashoffset={`${(-acc).toFixed(3)}`}
        style={{ opacity: hover && hover !== r.oc ? 0.28 : 1 }}
        onMouseEnter={() => setHover(r.oc)}
        onMouseLeave={() => setHover((h) => (h === r.oc ? null : h))}
      />
    );
    acc += pct;
    return el;
  });

  return (
    <div className="card chart-card">
      {header}
      <div className="pie-wrap">
        <div className="pie-top">
          <div className="pie">
            <svg viewBox="0 0 42 42">{slices}</svg>
            <div className="pie-c">
              <span className="pie-n num">{tot}</span>
              <span className="pie-u num">{monthLabel}</span>
            </div>
          </div>
          <div className="pie-lg">
            {rows.map((r, i) => (
              <button
                key={r.oc}
                className={"pl" + (hover === r.oc ? " sel" : "")}
                title={`${names[r.oc]} ${r.c}건 (${pr[i]}%)`}
                onMouseEnter={() => setHover(r.oc)}
                onMouseLeave={() => setHover((h) => (h === r.oc ? null : h))}
              >
                <span className="pl-d" style={{ background: colors[r.oc] }} />
                <span className="pl-n">{names[r.oc]}</span>
                <span className="pl-tr">
                  <span className="pl-fl" style={{ width: `${((r.c / maxC) * 100).toFixed(1)}%`, background: colors[r.oc] }} />
                </span>
                <span className="pl-v num">{r.c}</span>
                <span className="pl-p num">{pr[i]}%</span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
