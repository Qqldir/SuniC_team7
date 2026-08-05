/* 전역 스타일 — 토큰 기반 테마 (다크 기본 + 라이트) · trendroom(O/I Spark) 룩 이식
 * 색상은 전부 CSS 변수(토큰)로 관리. data-theme 속성으로 다크/라이트 전환.
 * 기존 뷰들이 쓰는 클래스 이름은 그대로 보존.
 */
export default function StyleBlock() {
  return (
    <style>{`
      @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css');
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap');

      /* ===== 다크 테마 (기본값) ===== */
      :root{
        --paper:#0a0912; --panel:#14121f; --panel-sub:#1a1730; --fill:#1d1a30;
        --ink:#edeaf7; --steel:#9791b4; --line:#2a2542;
        --accent:#a855f7; --accent-hover:#9333ea; --accent-soft:#251b40;
        --ok:#34d399; --ok-bg:#12281f;
        --warn:#fbbf24; --warn-bg:#2a2113;
        --info:#60a5fa; --info-bg:#14233b;
        --violet:#c4b5fd; --violet-bg:#231d3d;
        --danger:#f87171; --danger-bg:#2a1618;
        --bar:#6ea8ff;
        --shadow:rgba(0,0,0,.45);
        color-scheme:dark;
      }
      /* ===== 라이트 테마 (trendroom 라이트: 틸/슬레이트) ===== */
      :root[data-theme="light"]{
        --paper:#eef2f4; --panel:#ffffff; --panel-sub:#f7f9fa; --fill:#f1f4f6;
        --ink:#12202a; --steel:#5c6a78; --line:#e2e7ec;
        --accent:#2f4a57; --accent-hover:#213640; --accent-soft:#e6eef1;
        --ok:#1f8f5f; --ok-bg:#e7f3ec;
        --warn:#9a6413; --warn-bg:#fbf1e0;
        --info:#3a5e8c; --info-bg:#e8eef7;
        --violet:#5e4a9e; --violet-bg:#efeaf7;
        --danger:#c8102e; --danger-bg:#fcebee;
        --bar:#2f6df0;
        --shadow:rgba(16,24,40,.07);
        color-scheme:light;
      }

      html{background:var(--paper);transition:background-color .22s ease}
      body{margin:0;background:var(--paper);color:var(--ink);
        font-family:'Pretendard Variable',Pretendard,-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;
        font-size:14px;line-height:1.55;-webkit-font-smoothing:antialiased;
        transition:background-color .22s ease,color .22s ease}
      *,*::before,*::after{box-sizing:border-box}
      button{font-family:inherit;cursor:pointer}
      a{color:inherit;text-decoration:none}
      :focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:3px}
      ::-webkit-scrollbar{width:10px;height:10px}
      ::-webkit-scrollbar-thumb{background:var(--line);border-radius:8px;border:3px solid transparent;background-clip:content-box}
      @media (prefers-reduced-motion: reduce){*{transition:none !important;animation:none !important}}
      .mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:0.86em;letter-spacing:-0.01em}
      .dim{color:var(--steel)}
      .dim-xs{color:var(--steel);font-size:12px}

      /* ===== 레이아웃 셸 (좌측 사이드바) ===== */
      .app{display:flex;min-height:100vh;background:var(--paper);color:var(--ink)}
      .side{width:236px;flex:none;background:var(--panel);border-right:1px solid var(--line);
        display:flex;flex-direction:column;position:sticky;top:0;height:100vh}
      .brand{height:60px;flex:none;display:flex;align-items:center;gap:10px;padding:0 16px;
        border-bottom:1px solid var(--line)}
      .brand-mark{background:var(--accent);color:#fff;font-weight:700;font-size:11px;
        padding:4px 7px;border-radius:6px;letter-spacing:.02em}
      .brand-name{font-weight:700;font-size:14px;letter-spacing:-.01em}
      .brand-sub{color:var(--steel);font-size:10.5px}
      .theme-btn{margin-left:auto;width:30px;height:30px;flex:none;display:flex;align-items:center;
        justify-content:center;border:1px solid var(--line);border-radius:8px;background:var(--panel-sub);
        color:var(--ink);font-size:14px;line-height:1}
      .theme-btn:hover{border-color:var(--accent)}

      .nav{flex:1;overflow-y:auto;padding:14px 10px;display:flex;flex-direction:column;gap:16px}
      .nav-group{display:flex;flex-direction:column;gap:2px}
      .nav-title{font-size:10.5px;font-weight:600;color:var(--steel);letter-spacing:.4px;padding:0 10px 6px}
      .navbtn{display:flex;align-items:center;gap:9px;width:100%;padding:9px 11px;background:transparent;
        border:none;border-radius:8px;color:var(--steel);font-size:13px;font-weight:500;text-align:left;
        transition:background .12s,color .12s}
      .navbtn:hover{background:var(--fill);color:var(--ink)}
      .navbtn-on{background:var(--accent-soft);color:var(--ink);font-weight:600}
      .navcount{margin-left:auto;background:var(--accent-soft);color:var(--accent);font-size:11px;
        font-weight:600;padding:1px 7px;border-radius:99px}

      .body{flex:1;min-width:0}
      .main{padding:24px 26px 60px;max-width:1200px}

      @media (max-width:860px){
        .app{flex-direction:column}
        .side{width:100%;height:auto;position:static;flex-direction:column}
        .nav{flex-direction:row;overflow-x:auto;gap:10px;padding:10px 12px}
        .nav-group{flex-direction:row;align-items:center;gap:4px}
        .nav-title{display:none}
        .navbtn{width:auto;white-space:nowrap}
        .main{padding:20px 16px 48px}
      }

      /* ===== 페이지 헤더 ===== */
      .page-head{display:flex;justify-content:space-between;align-items:flex-end;gap:14px;margin-bottom:18px;flex-wrap:wrap}
      .page-head h1{font-size:20px;font-weight:700;margin:0 0 4px;letter-spacing:-.01em}
      .lede{margin:0;color:var(--steel);font-size:13px;max-width:560px}
      .head-actions{display:flex;gap:8px}

      /* ===== 카드/피드 ===== */
      .card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:16px}
      .card-head{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px}
      .eyebrow{font-size:11.5px;font-weight:700;letter-spacing:.08em;color:var(--ink);text-transform:uppercase}
      .grid-2{display:grid;grid-template-columns:1fr;gap:16px}
      @media (min-width:900px){.grid-2{grid-template-columns:1fr 1fr;align-items:start}}

      .feed-item{padding:11px 10px;border-top:1px solid var(--line);transition:background .15s}
      .feed-item:hover{background:var(--panel-sub)}
      .feed-hl{background:var(--accent-soft);box-shadow:inset 2px 0 0 var(--accent)}
      .feed-meta{display:flex;align-items:center;gap:8px;margin-bottom:3px}
      .feed-src{font-size:12px;font-weight:600}
      .feed-title{font-weight:600;font-size:13.5px;margin-bottom:2px}
      .feed-sum{color:var(--steel);font-size:12.5px;margin-bottom:6px}
      .feed-sum.feed-clamp{display:-webkit-box;-webkit-line-clamp:3;line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
      .feed-tags{display:flex;gap:5px;flex-wrap:wrap}

      .badge{font-size:10.5px;font-weight:600;padding:1px 6px;border-radius:4px;letter-spacing:.02em}
      .badge-adhoc{background:var(--warn-bg);color:var(--warn)}
      .badge-periodic{background:var(--info-bg);color:var(--info)}
      .badge-sec{background:var(--violet-bg);color:var(--violet)}
      .badge-news{background:var(--ok-bg);color:var(--ok)}

      .tagchip{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--steel);
        background:var(--fill);border:1px solid var(--line);border-left:3px solid var(--steel);
        padding:1px 7px;border-radius:3px;transition:color .12s}
      .tagchip:hover{color:var(--ink)}
      .tagchip-static{pointer-events:none}

      /* ===== 필터 ===== */
      .filterbar{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 16px;
        margin-bottom:16px;display:flex;flex-direction:column;gap:8px}
      .filter-row{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
      .filter-label{font-size:11.5px;color:var(--steel);font-weight:600;margin-right:4px;min-width:36px}
      .filter-sep{width:1px;height:16px;background:var(--line);margin:0 8px}
      .chip{font-size:12px;padding:4px 11px;background:transparent;border:1px solid var(--line);
        border-radius:99px;color:var(--steel);transition:all .12s}
      .chip:hover{border-color:var(--steel);color:var(--ink)}
      .chip-on{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}

      /* ===== 버튼 ===== */
      .btn{display:inline-flex;align-items:center;gap:6px;font-size:13px;padding:8px 14px;border-radius:9px;
        background:var(--panel);border:1px solid var(--line);color:var(--ink);transition:all .12s}
      .btn:hover:not(:disabled){border-color:var(--accent)}
      .btn:disabled{opacity:.5;cursor:default}
      .btn-primary{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
      .btn-primary:hover:not(:disabled){background:var(--accent-hover);border-color:var(--accent-hover)}
      .btn-danger:hover:not(:disabled){border-color:var(--danger);color:var(--danger)}
      .btn-sm{padding:5px 10px;font-size:12px;border-radius:7px}
      .btn-wide{width:100%;justify-content:center;margin-top:4px}
      .iconbtn{background:transparent;border:none;color:var(--steel);padding:4px;border-radius:6px}
      .iconbtn:hover{color:var(--ink)}
      .spin{animation:oispin 0.9s linear infinite}
      @keyframes oispin{to{transform:rotate(360deg)}}

      /* ===== 폼 ===== */
      .field{margin-bottom:12px}
      .field-label{display:block;font-size:12px;font-weight:600;color:var(--steel);margin-bottom:5px}
      .input,.select,.textarea{width:100%;font-family:inherit;font-size:13.5px;color:var(--ink);
        background:var(--panel-sub);border:1px solid var(--line);border-radius:8px;padding:9px 11px}
      .textarea{resize:vertical;line-height:1.55}
      .input:focus,.select:focus,.textarea:focus{outline:none;border-color:var(--accent)}
      .select option{background:var(--panel);color:var(--ink)}
      .field-2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
      .aff-pick{display:flex;flex-wrap:wrap;gap:5px}
      .case-badges{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
      .badge-pending{background:var(--warn-bg);color:var(--warn)}
      .badge-approved{background:var(--ok-bg);color:var(--ok)}
      .badge-rejected{background:var(--fill);color:var(--steel)}
      .badge-src{background:var(--violet-bg);color:var(--violet)}
      .case-actions{display:flex;gap:6px;margin-top:8px;align-items:center}
      .case-actions .spacer{flex:1}
      .ctx-note{font-size:11.5px;color:var(--steel);background:var(--fill);border:1px dashed var(--line);
        border-radius:8px;padding:7px 10px;margin-bottom:10px}
      .errbox{display:flex;align-items:center;gap:7px;margin-top:10px;padding:9px 11px;border-radius:8px;
        background:var(--danger-bg);color:var(--danger);font-size:12.5px}

      /* ===== 과제 카드 ===== */
      .task-card{padding:15px 16px}
      .task-head{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:8px}
      .task-title{font-weight:700;font-size:14.5px;margin-bottom:5px}
      .task-meta{display:flex;align-items:center;gap:7px}
      .cat{font-size:11.5px;color:var(--steel);border:1px solid var(--line);padding:1px 7px;border-radius:99px}
      .row{display:flex;gap:10px;padding:4px 0;font-size:13px}
      .rk{flex:none;width:52px;color:var(--steel);font-size:12px;padding-top:1px}
      .rv{flex:1}
      .formula{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap;margin:9px 0;border-radius:8px;
        border:1px solid var(--line);border-left:3px solid var(--accent);background:var(--panel-sub);padding:8px 12px}
      .formula-name{font-size:12px;font-weight:700}
      .formula-eq{font-family:'IBM Plex Mono',monospace;font-size:12.5px;color:var(--ink)}
      .task-evd{display:flex;gap:10px;align-items:center;margin:6px 0 10px}
      .evd-wrap{display:flex;gap:6px;flex-wrap:wrap}
      .evd{display:inline-flex;align-items:center;gap:2px;font-size:11.5px;color:var(--steel);
        background:transparent;border:1px solid var(--line);padding:2px 8px;border-radius:99px;transition:all .12s}
      .evd:hover{color:var(--accent);border-color:var(--accent)}

      /* ===== 테이블 ===== */
      .table-card{padding:0;overflow-x:auto}
      .tbl{width:100%;border-collapse:collapse;font-size:13px}
      .tbl th{text-align:left;font-size:11.5px;color:var(--steel);font-weight:600;padding:10px 12px;
        border-bottom:1px solid var(--line);white-space:nowrap}
      .tbl td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
      .tbl tr:last-child td{border-bottom:none}
      .th-chk{width:34px}
      .td-title{font-weight:600;min-width:180px}
      .td-kpi{font-size:12px}
      .status{font-size:11.5px;background:var(--fill);color:var(--steel);padding:2px 8px;border-radius:99px}

      /* ===== 모달 ===== */
      .overlay{position:fixed;inset:0;background:rgba(4,4,10,.6);z-index:50;display:flex;align-items:center;
        justify-content:center;padding:20px;backdrop-filter:blur(4px)}
      .modal{background:var(--panel);width:100%;max-width:680px;max-height:86vh;border-radius:14px;
        display:flex;flex-direction:column;border:1px solid var(--line)}
      .modal-head{display:flex;justify-content:space-between;align-items:flex-start;padding:16px 18px 10px;gap:10px}
      .export-area{flex:1;min-height:300px;margin:0 18px;padding:12px;font-size:11.5px;line-height:1.6;
        border:1px solid var(--line);border-radius:8px;background:var(--panel-sub);color:var(--ink);resize:none}
      .modal-actions{display:flex;gap:8px;padding:14px 18px}

      /* ===== 봇 ===== */
      .chatwrap{max-width:640px;background:var(--panel);border:1px solid var(--line);border-radius:12px}
      .chat-head{display:flex;align-items:center;gap:8px;padding:11px 15px;border-bottom:1px solid var(--line);
        font-size:13px;font-weight:600}
      .chat-note{margin-left:auto;font-weight:400}
      .chat-body{background:var(--fill);padding:16px 14px 22px}
      .chat-day{text-align:center;font-size:11px;color:var(--steel);margin-bottom:12px}
      .bubble{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:13px 14px;
        max-width:560px;box-shadow:0 1px 2px var(--shadow)}
      .bubble-intro{font-size:13.5px;margin-bottom:10px}
      .bot-card{display:flex;gap:11px;border-top:1px solid var(--line);padding:12px 2px}
      .bot-rank{flex:none;color:var(--accent);font-weight:600;font-size:13px;padding-top:2px}
      .bot-main{flex:1;min-width:0}
      .bot-title{font-weight:700;font-size:13.5px;margin-bottom:5px}

      /* ===== 기타 ===== */
      .empty-sm{color:var(--steel);font-size:12.5px;padding:14px 6px}
      .empty-lg{display:flex;flex-direction:column;align-items:center;gap:8px;padding:44px 20px;
        text-align:center;color:var(--steel);font-size:13.5px}
      .empty-actions{display:flex;gap:8px;margin-top:4px}
      .foot-note{color:var(--steel);font-size:11.5px;margin-top:4px}

      /* ===== 트렌드룸 차트 ===== */
      .num{font-variant-numeric:tabular-nums}
      .note{font-size:11.5px;color:var(--steel);line-height:1.5}
      .grid-c{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:stretch;margin-bottom:16px}
      .grid-c > .card{margin-bottom:0}
      @media (max-width:1180px){.grid-c{grid-template-columns:minmax(0,1fr)}}
      .chart-card{display:flex;flex-direction:column;min-width:0}
      .chart-card .card-h{display:flex;align-items:center;gap:10px;padding-bottom:12px;
        border-bottom:1px solid var(--line);margin-bottom:0}
      .chart-card .card-h h2{font-size:14px;font-weight:700}

      .cnav{flex:none;width:26px;height:26px;border:1px solid var(--line);border-radius:7px;
        background:var(--panel);color:var(--steel);display:inline-flex;align-items:center;justify-content:center}
      .cnav:hover:not(:disabled){background:var(--fill);color:var(--ink)}
      .cnav:disabled{opacity:.35;cursor:default}

      .cwrap{padding:14px 2px 4px;flex:1;display:flex;flex-direction:column;min-height:0}
      .crow{display:flex;align-items:stretch;gap:0}
      .crow-plot{flex:1;min-height:0}
      .cyax{flex:none;width:26px;display:flex;flex-direction:column;justify-content:space-between;
        align-items:flex-end;padding-right:8px;font-size:10.5px;color:var(--steel);font-variant-numeric:tabular-nums}
      .cyax.sp{height:auto;padding:0}
      .cplot{flex:1;min-width:0;position:relative;min-height:180px;max-height:250px}
      .cgrid{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:space-between}
      .cgrid span{height:1px;background:var(--line);opacity:.85}
      .cgrid span:last-child{background:var(--steel);opacity:.5}
      .cbars{position:absolute;inset:0;display:flex;align-items:flex-end;gap:10px;padding:0 4px}
      .cb{flex:1;min-width:0;height:100%;display:flex;flex-direction:column;justify-content:flex-end;position:relative;
        background:transparent;border:none;padding:0;cursor:pointer}
      .cbar{width:100%;background:var(--bar);min-height:3px;border-radius:5px 5px 0 0;transition:opacity .12s}
      .cbars:hover .cbar{opacity:.4}
      .cb:hover .cbar{opacity:1}
      .ctip{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);z-index:40;
        display:flex;flex-direction:column;gap:3px;min-width:110px;padding:8px 10px;border-radius:8px;
        background:var(--ink);color:var(--paper);pointer-events:none;box-shadow:0 4px 14px var(--shadow)}
      .ctip-d{font-size:10.5px;opacity:.75;font-variant-numeric:tabular-nums}
      .ctip-r{display:flex;align-items:center;gap:10px;font-size:12px;white-space:nowrap}
      .ctip-v{margin-left:auto;font-weight:700;font-variant-numeric:tabular-nums}
      .cxax{flex:1;min-width:0;display:flex;gap:10px;padding:7px 4px 0}
      .cx{flex:1;min-width:0;text-align:center;font-size:10.5px;color:var(--steel);
        font-variant-numeric:tabular-nums;white-space:nowrap}
      .clg{display:flex;gap:14px;align-items:center;padding:8px 2px 2px}

      .empty{padding:52px 20px;display:flex;flex-direction:column;align-items:center;gap:9px;text-align:center;
        color:var(--steel);font-size:14px;font-weight:600;flex:1;justify-content:center}

      .pie-wrap{display:flex;flex-direction:column;justify-content:center;padding:16px 2px;min-width:0;flex:1}
      .pie-top{display:flex;align-items:center;gap:22px;min-width:0}
      .pie{width:180px;height:180px;flex:none;position:relative}
      .pie svg{width:100%;height:100%;transform:rotate(-90deg)}
      .psl{cursor:pointer;transition:opacity .12s}
      .pie-c{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
        pointer-events:none}
      .pie-n{font-size:32px;font-weight:700;letter-spacing:-1.2px;line-height:1}
      .pie-u{font-size:11px;color:var(--steel);margin-top:6px;font-weight:600}
      .pie-lg{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:1px}
      .pl{display:flex;align-items:center;gap:8px;padding:0 4px;cursor:pointer;border:0;background:none;
        width:100%;text-align:left;border-radius:6px;height:26px;flex:none}
      .pl:hover,.pl.sel{background:var(--fill)}
      .pl-d{width:9px;height:9px;border-radius:2px;flex:none}
      .pl-n{font-size:11.5px;line-height:1;color:var(--ink);flex:none;width:118px;overflow:hidden;
        text-overflow:ellipsis;white-space:nowrap}
      .pl-tr{flex:1;min-width:24px;height:7px;background:var(--fill);border-radius:4px;overflow:hidden;display:block}
      .pl-fl{display:block;height:100%;border-radius:4px}
      .pl-v{font-size:11.5px;line-height:1;font-weight:700;width:20px;text-align:right;flex:none}
      .pl-p{font-size:10.5px;line-height:1;color:var(--steel);width:34px;text-align:right;flex:none}

      /* ===== 시황 티커 ===== */
      .ticker{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;
        height:46px;display:flex;margin-bottom:16px}
      .tk-view{flex:1;min-width:0;overflow:hidden;position:relative;display:flex;align-items:center}
      .tk-view::before,.tk-view::after{content:'';position:absolute;top:0;bottom:0;width:40px;pointer-events:none;z-index:2}
      .tk-view::before{left:0;background:linear-gradient(to left,transparent,var(--panel))}
      .tk-view::after{right:0;background:linear-gradient(to right,transparent,var(--panel))}
      .tk-track{display:flex;align-items:center;white-space:nowrap;animation:tkroll 44s linear infinite;will-change:transform}
      .tk-view:hover .tk-track{animation-play-state:paused}
      @keyframes tkroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
      .tk-i{display:inline-flex;align-items:center;gap:7px;padding:0 17px;position:relative;height:44px}
      .tk-i+.tk-i::before{content:'';position:absolute;left:0;top:50%;transform:translateY(-50%);
        width:1px;height:13px;background:var(--line)}
      .tk-nm{font-size:12px;color:var(--steel)}
      .tk-i.sk .tk-nm{color:var(--ink);font-weight:700}
      .tk-p{font-size:12px;font-weight:700;color:var(--ink)}
      .tk-c{font-size:11px;font-weight:600}
      .tk-c.up{color:var(--danger)}
      .tk-c.dn{color:var(--info)}
      .tk-go{font-size:9.5px;color:var(--steel);opacity:0;transition:opacity .12s}
      .tk-i:hover .tk-nm{color:var(--accent);text-decoration:underline;text-underline-offset:3px}
      .tk-i:hover .tk-go{opacity:1;color:var(--accent)}
      .tk-btn{flex:none;display:flex;align-items:center;justify-content:center;padding:0 22px;border:0;
        background:var(--accent);cursor:pointer;font-size:12.5px;font-weight:700;color:#fff;white-space:nowrap}
      .tk-btn:hover{background:var(--accent-hover)}
      @media (prefers-reduced-motion: reduce){.tk-track{animation:none}}

      /* ===== 로그인 ===== */
      .login-wrap{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;
        background:
          radial-gradient(120% 120% at 15% 10%, color-mix(in srgb, var(--accent) 22%, transparent) 0%, transparent 55%),
          radial-gradient(120% 120% at 90% 100%, color-mix(in srgb, var(--info) 20%, transparent) 0%, transparent 55%),
          var(--paper)}
      .login-card{width:100%;max-width:410px;background:var(--panel);border:1px solid var(--line);
        border-radius:18px;padding:32px 30px;box-shadow:0 30px 80px -40px var(--shadow)}
      .login-brand{display:flex;align-items:center;gap:10px;margin-bottom:22px}
      .login-title{font-size:22px;font-weight:700;letter-spacing:-.02em;margin:0 0 4px}
      .login-desc{font-size:13px;color:var(--steel);margin:0 0 22px}
      .login-btn{width:100%;height:48px;margin-top:6px;border:none;border-radius:10px;background:var(--accent);
        color:#fff;font-size:15px;font-weight:600;transition:background .15s}
      .login-btn:hover{background:var(--accent-hover)}
      .login-or{text-align:center;font-size:12px;color:var(--steel);margin:16px 0 10px}
      .login-social{display:flex;gap:10px}
      .login-social .btn{flex:1;justify-content:center;height:46px}
      .login-foot{text-align:center;font-size:12.5px;color:var(--steel);margin-top:18px}
      .login-link{color:var(--accent);font-weight:600}
    `}</style>
  );
}
