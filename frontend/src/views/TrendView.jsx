import { useState, useRef } from "react";
import {
  EV, TH2, BIZ_C, evKind, TR_KINDS, TR_BIZS, TR_PERIODS,
  trPd, trIso, trDot, trMD, trShift, trMon, trRange, trScope,
} from "../data/evidence.js";

/* 트렌드룸 — 수집 외부자료를 테마별로 요약하고 주차별 목록으로 보여준다.
 * 좌: 상위 테마 + 자료 목록 / 우: AI 동향 요약. (trendroom.html viewTrend 이식) */
export default function TrendView() {
  const [S, setS] = useState({
    trBiz: "전체", trPeriod: "1m", trFrom: "2026-06-30", trTo: "2026-07-30",
    trTheme: null, trQ: "", trKind: "전체", trSort: "date",
    trNew: false, trUnl: false, trMethod: false, trGenAt: "오늘 08:12",
  });
  const [aiDim, setAiDim] = useState(false);
  const bumpT = useRef(null);
  const set = (patch) => setS((s) => ({ ...s, ...patch }));

  /* AI 요약 다시 생성(페이드) */
  const bump = () => {
    setAiDim(true);
    clearTimeout(bumpT.current);
    bumpT.current = setTimeout(() => { setAiDim(false); set({ trGenAt: "방금" }); }, 420);
  };

  const scope = trScope(S);
  const [f, t] = trRange(S);
  const pLabel = (TR_PERIODS.find((p) => p.k === S.trPeriod) || TR_PERIODS[1]).l;
  const scopeSpan = S.trPeriod === "all" ? `수집 전 기간 · ~${trDot(t)}` : `${trDot(f)} – ${trDot(t)}`;
  const bizLabel = S.trBiz === "전체" ? "전 분야" : S.trBiz;

  /* 테마 집계 */
  const cnt = {};
  scope.forEach((k) => { const th = EV[k].theme; cnt[th] = (cnt[th] || 0) + 1; });
  const ranked = Object.keys(cnt).sort((a, b) => cnt[b] - cnt[a] || a.localeCompare(b));
  const maxC = ranked.length ? cnt[ranked[0]] : 1;

  /* 요약 헤드라인 */
  let headline = "선택한 기간에 수집된 자료가 없습니다. 기간을 넓혀 보세요.";
  if (ranked.length === 1)
    headline = `${bizLabel} 자료 ${scope.length}건은 모두 ${ranked[0]} 축에 모였습니다.`;
  else if (ranked.length > 1)
    headline = `${bizLabel} 자료 ${scope.length}건이 ${ranked.length}개 테마에 걸쳐 있고, `
      + `${ranked[0]}(${cnt[ranked[0]]}건)과 ${ranked[1]}(${cnt[ranked[1]]}건)에 언급이 집중됐습니다. `
      + `공통 논조는 비용 항목을 개별로 깎기보다 운영 순서·계약 구조를 다시 짜는 쪽입니다.`;

  const bullets = ranked.slice(0, 3).map((th) => {
    const T = TH2[th];
    const srcs = scope.filter((k) => EV[k].theme === th).slice(0, 3).map((k) => EV[k].src).join(" · ");
    return { th, T, srcs, count: cnt[th] };
  });

  /* 목록 필터 */
  const q = (S.trQ || "").trim().toLowerCase();
  let rows = scope.filter((k) => {
    const e = EV[k];
    if (S.trTheme && e.theme !== S.trTheme) return false;
    if (S.trKind !== "전체" && evKind(k) !== S.trKind) return false;
    if (S.trNew && !e.new) return false;
    if (S.trUnl && e.refs > 0) return false;
    if (q && !(e.title + e.sum + e.src).toLowerCase().includes(q)) return false;
    return true;
  });
  rows.sort((a, b) => S.trSort === "cite"
    ? (EV[b].refs - EV[a].refs) || (trPd(EV[b].date) - trPd(EV[a].date))
    : trPd(EV[b].date) - trPd(EV[a].date));

  /* 주차 그룹핑 */
  const groups = [];
  rows.forEach((k) => {
    const d = trPd(EV[k].date), m0 = trMon(d), key = trIso(m0);
    let g = groups.find((x) => x.key === key);
    if (!g) {
      const nth = Math.floor((m0.getDate() - 1) / 7) + 1;
      g = { key, label: `${m0.getMonth() + 1}월 ${nth}주`, sub: `${trMD(m0)} – ${trMD(trShift(m0, -6))}`, rows: [] };
      groups.push(g);
    }
    g.rows.push(k);
  });

  const newN = scope.filter((k) => EV[k].new).length;
  const unlN = scope.filter((k) => EV[k].refs === 0).length;
  const hasF = !!(S.trTheme || q || S.trKind !== "전체" || S.trNew || S.trUnl);
  const srcCount = new Set(scope.map((k) => EV[k].src)).size;

  const chip = (on, onClick, label, key) => (
    <button key={key} className={"chip" + (on ? " on" : "")} onClick={onClick}>{label}</button>
  );

  const Row = ({ k }) => {
    const e = EV[k], T = TH2[e.theme], n = e.refs;
    const bz = e.biz[0];
    return (
      <div className="tr2-row">
        <div className="tr2-d">
          <span className="tr2-dd">{trMD(trPd(e.date))}</span>
          {e.new && <span className="nb">NEW</span>}
        </div>
        <div className="tr2-m">
          <div className="row-f" style={{ gap: 7 }}>
            <span className="bizdot" style={{ background: BIZ_C[bz] || "var(--steel)" }} />
            <span style={{ fontSize: 11.5, fontWeight: 700 }}>{e.src}</span>
            <span style={{ fontSize: 11, color: "var(--steel)" }}>·</span>
            <span style={{ fontSize: 11, color: "var(--steel)" }}>{evKind(k)}</span>
            <span className="thtag" style={{ background: T.bg, color: T.c }}>{e.theme}</span>
          </div>
          <div className="tr2-t">{e.title}</div>
          <div className="tr2-s">{e.sum}</div>
        </div>
        <div className="tr2-a">
          <button
            className="citep"
            style={n
              ? { background: "var(--accent-soft)", color: "var(--accent)" }
              : { background: "var(--warn-bg)", color: "var(--warn)" }}
            onClick={n ? () => set({ trQ: e.src, trTheme: null }) : undefined}
          >
            {n ? `인용 과제 ${n}건` : "미연결"}
          </button>
          <a className="tr-lk" href={e.url} target="_blank" rel="noopener noreferrer">원문 ↗</a>
        </div>
      </div>
    );
  };

  return (
    <div className="tr-screen">
      <div className="page-head">
        <div>
          <h1>트렌드룸</h1>
          <p className="lede">수집된 외부 자료를 기간·분야 단위로 요약해 산업 동향으로 보여줍니다. 여기 실린 자료들은 과제 생성의 근거로 사용됩니다.</p>
        </div>
        <div className="row-f">
          <span className="note">수집 {Object.keys(EV).length}건 · 오늘 08:00 갱신</span>
        </div>
      </div>

      <div className="tr2">
        {/* 좌측 */}
        <div className="tr2-l">
          {/* 상위 테마 */}
          <div className="card">
            <div className="card-h">
              <h2 style={{ whiteSpace: "nowrap" }}>상위 테마</h2>
              <span className="note">선택한 기간 내 자료를 테마 축에 배정한 결과 · 클릭하면 아래 목록이 좁혀집니다</span>
              <button className="btn sm" style={{ marginLeft: "auto" }} onClick={() => set({ trMethod: !S.trMethod })}>
                테마 선정 기준 {S.trMethod ? "▴" : "▾"}
              </button>
            </div>
            <div className="thg">
              {ranked.length ? ranked.map((th) => {
                const T = TH2[th], on = S.trTheme === th;
                return (
                  <button
                    key={th}
                    className="thc"
                    style={on ? { background: T.bg, borderColor: T.c } : undefined}
                    onClick={() => set({ trTheme: S.trTheme === th ? null : th })}
                  >
                    <span className="thc-t">
                      <span className="thc-n" style={on ? { color: T.c } : undefined}>{th}</span>
                      <span className="thc-c" style={{ color: T.c }}>{cnt[th]}</span>
                    </span>
                    <span className="thc-bar"><i style={{ background: T.c, width: `${Math.round(cnt[th] / maxC * 100)}%` }} /></span>
                  </button>
                );
              }) : <span className="note">해당 기간에 자료가 없습니다.</span>}
            </div>
            {S.trMethod && (
              <div className="method">
                <b>테마는 이렇게 정해집니다</b>
                <p>① <strong>고정 축</strong> — 과제 레버 체계(정비·에너지·구매·수율·물류·간접비·운전자본)를 그대로 테마 축으로 씁니다. 축이 고정이라 기간을 바꿔도 증감 비교가 가능합니다.<br />
                ② <strong>배정</strong> — LLM이 자료 1건을 축 1개에 배정하고, 배정 근거 문장을 함께 남깁니다.<br />
                ③ <strong>미배정 처리</strong> — 배정 확신도가 낮은 자료는 축에 넣지 않고 '미배정 풀'로 보냅니다. 이때 <strong>"이 자료의 핵심 동인" 한 문장</strong>을 함께 생성해 둡니다.<br />
                ④ <strong>신규 테마 승격</strong> — 미배정 자료끼리 그 동인 문장의 유사도로 묶고, <strong>같은 묶음이 3건 이상</strong>이 되면 LLM이 이름·정의·기존 축과의 경계를 제안해 관리자 승인 대기열에 올립니다. 승인 시 과거 자료까지 재배정합니다.<br />
                ⑤ <strong>접힘</strong> — 어디에도 묶이지 않은 잔여 자료와 기간 내 1건뿐인 테마는 '기타'로 묶습니다.</p>
              </div>
            )}
          </div>

          {/* 자료 목록 */}
          <div className="card">
            <div className="ctlbar">
              <input className="inp" style={{ width: 230 }} placeholder="제목·요약·출처 검색"
                value={S.trQ} onChange={(e) => set({ trQ: e.target.value })} />
              <select className="sel" value={S.trKind === "전체" ? "자료 종류 전체" : S.trKind}
                onChange={(e) => set({ trKind: e.target.value === "자료 종류 전체" ? "전체" : e.target.value })}>
                {TR_KINDS.map((k) => <option key={k}>{k === "전체" ? "자료 종류 전체" : k}</option>)}
              </select>
              <select className="sel" value={S.trSort} onChange={(e) => set({ trSort: e.target.value })}>
                <option value="date">최신순</option>
                <option value="cite">인용 많은 순</option>
              </select>
              <span className="ctl-sep" />
              {chip(S.trNew, () => set({ trNew: !S.trNew }), `신규 ${newN}`)}
              {chip(S.trUnl, () => set({ trUnl: !S.trUnl }), `미연결 ${unlN}`)}
              {hasF && (
                <button className="chip" style={{ border: 0, textDecoration: "underline", textUnderlineOffset: 3 }}
                  onClick={() => set({ trTheme: null, trQ: "", trKind: "전체", trNew: false, trUnl: false })}>
                  필터 해제
                </button>
              )}
              <span className="note num" style={{ marginLeft: "auto" }}>{rows.length}건 표시</span>
            </div>

            {rows.length ? (
              S.trSort === "cite"
                ? rows.map((k) => <Row key={k} k={k} />)
                : groups.map((g) => (
                  <div key={g.key}>
                    <div className="g-h">
                      <span className="g-l">{g.label}</span>
                      <span className="g-s">{g.sub}</span>
                      <span className="g-s" style={{ marginLeft: "auto" }}>{g.rows.length}건</span>
                    </div>
                    {g.rows.map((k) => <Row key={k} k={k} />)}
                  </div>
                ))
            ) : (
              <div className="empty2">
                <span style={{ fontSize: 14, fontWeight: 700 }}>조건에 맞는 자료가 없습니다</span>
                <span className="note">기간을 넓히거나 필터를 해제해 보세요.</span>
              </div>
            )}
          </div>
        </div>

        {/* 우측 — AI 동향 요약 */}
        <div className="tr2-r">
          <div className="card">
            <div className="card-h" style={{ padding: "13px 15px" }}>
              <span className="ai-mk">AI</span>
              <h2>동향 요약</h2>
              <span className="note" style={{ fontSize: 11 }}>{pLabel} · {scopeSpan} · {bizLabel}</span>
              <button className="btn sm" style={{ marginLeft: "auto" }} onClick={bump}>↻ 다시 생성</button>
            </div>
            <div className="ai-ctl">
              <div className="ai-row">
                <span className="ai-k">분야</span>
                {TR_BIZS.map((x) => chip(S.trBiz === x, () => { set({ trBiz: x }); bump(); }, x, x))}
              </div>
              <div className="ai-row">
                <span className="ai-k">기간</span>
                {TR_PERIODS.map((p) => chip(S.trPeriod === p.k, () => { set({ trPeriod: p.k }); bump(); }, p.l, p.k))}
              </div>
              {S.trPeriod === "custom" && (
                <div className="ai-row">
                  <span className="ai-k" />
                  <input type="date" className="dinp" value={S.trFrom} onChange={(e) => { set({ trFrom: e.target.value }); bump(); }} />
                  <span className="note">–</span>
                  <input type="date" className="dinp" value={S.trTo} onChange={(e) => { set({ trTo: e.target.value }); bump(); }} />
                </div>
              )}
            </div>
            <div className="ai-b" style={{ opacity: aiDim ? 0.35 : 1 }}>
              <p className="ai-hl">{headline}</p>
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {bullets.map((b) => (
                  <div className="ai-i" key={b.th}>
                    <span style={{ background: b.T.c }} />
                    <div className="ai-i-b">
                      <div className="row-f" style={{ gap: 8 }}>
                        <button className="ai-tag" style={{ background: b.T.c }} onClick={() => set({ trTheme: S.trTheme === b.th ? null : b.th })}>{b.th}</button>
                        <span className="num" style={{ fontSize: 11, fontWeight: 600, color: "var(--steel)" }}>자료 {b.count}건</span>
                        <span style={{ fontSize: 11, color: "var(--steel)" }}>{b.srcs}</span>
                      </div>
                      <div className="ai-h">{b.T.head}</div>
                      <div className="ai-p">{b.T.body}</div>
                    </div>
                  </div>
                ))}
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 3 }}>
                <span className="ai-f">근거 {scope.length}건 · 출처 {srcCount}곳 · {S.trGenAt} 생성</span>
                <span className="ai-f" style={{ opacity: 0.7 }}>요약은 기간·분야 선택에만 반응합니다 (왼쪽 검색·필터와 무관)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
