import { useState } from "react";
import BarChart from "../components/BarChart.jsx";
import Donut from "../components/Donut.jsx";
import Ticker from "../components/Ticker.jsx";
import { DAILY, OC_MONTHLY, OC_NAME, OC_COLOR } from "../data/trend.js";

/* 트렌드룸 대시보드 — 일별 생성 막대 + OC별 도넛 + 시황 티커. */
export default function TrendView() {
  const months = Object.keys(OC_MONTHLY).sort().reverse();
  const [moIdx, setMoIdx] = useState(0);
  const ym = months[moIdx];
  const rows = OC_MONTHLY[ym] || [];
  const total = DAILY.reduce((a, b) => a + b.n, 0);

  return (
    <>
      <div className="page-head">
        <div>
          <h1>트렌드룸</h1>
          <p className="lede">
            과제 생성 추이와 계열사(OC)별 구성, 실시간 시황을 한눈에 봅니다.
            수집된 외부 자료가 과제 생성의 근거로 이어집니다.
          </p>
        </div>
        <div className="head-actions">
          <span className="dim-xs">수집 · 오늘 08:00 갱신</span>
        </div>
      </div>

      <div className="grid-c">
        <BarChart data={DAILY} total={total} />
        <Donut
          rows={rows}
          names={OC_NAME}
          colors={OC_COLOR}
          monthLabel={ym.replace("-", ".")}
          onPrev={() => setMoIdx((i) => Math.min(months.length - 1, i + 1))}
          onNext={() => setMoIdx((i) => Math.max(0, i - 1))}
          prevDisabled={moIdx >= months.length - 1}
          nextDisabled={moIdx <= 0}
        />
      </div>

      <Ticker />
    </>
  );
}
