/* 원본 데모의 StyleBlock — 전역 스타일 (IBM Plex + O/I Scout 테마) */
export default function StyleBlock() {
  return (
    <style>{`
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

      .app {
        --paper:#F3F5F8; --panel:#FFFFFF; --ink:#17202E; --steel:#5C6B82;
        --line:#DFE5EC; --accent:#E4002B; --accent-soft:#FCE8EC;
        min-height:100vh; background:var(--paper); color:var(--ink);
        font-family:'IBM Plex Sans KR',-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;
        font-size:14px; line-height:1.55; -webkit-font-smoothing:antialiased;
      }
      .app *, .app *::before, .app *::after { box-sizing:border-box; }
      .mono { font-family:'IBM Plex Mono',ui-monospace,monospace; font-size:0.86em; letter-spacing:-0.01em; }
      .dim { color:var(--steel); }
      .dim-xs { color:var(--steel); font-size:12px; }
      button { font-family:inherit; cursor:pointer; }
      .app :focus-visible { outline:2px solid var(--accent); outline-offset:2px; border-radius:3px; }
      @media (prefers-reduced-motion: reduce) { .app * { transition:none !important; animation:none !important; } }

      /* 상단 바 */
      .topbar { display:flex; justify-content:space-between; align-items:center; padding:14px 22px;
        background:var(--panel); border-bottom:1px solid var(--line); position:sticky; top:0; z-index:20; }
      .brand { display:flex; align-items:baseline; gap:8px; }
      .brand-mark { background:var(--accent); color:#fff; font-weight:700; font-size:12px;
        padding:3px 7px; letter-spacing:0.02em; }
      .brand-name { font-weight:700; font-size:17px; letter-spacing:-0.01em; }
      .brand-sub { color:var(--steel); font-size:12px; }
      .topbar-right { display:flex; align-items:center; gap:10px; font-size:12px; }
      .sample-pill { border:1px solid var(--line); color:var(--steel); padding:2px 8px; border-radius:99px; font-size:11px; }

      /* 프레임 */
      .frame { display:flex; max-width:1180px; margin:0 auto; }
      .rail { width:168px; flex:none; padding:18px 10px; display:flex; flex-direction:column; gap:4px; }
      .navbtn { display:flex; align-items:center; gap:9px; width:100%; padding:9px 11px;
        background:transparent; border:none; border-left:2px solid transparent; color:var(--steel);
        font-size:13.5px; text-align:left; transition:color .12s; }
      .navbtn:hover { color:var(--ink); }
      .navbtn-on { color:var(--ink); font-weight:600; border-left-color:var(--accent); background:var(--panel); }
      .navcount { margin-left:auto; background:var(--accent-soft); color:var(--accent);
        font-size:11px; padding:1px 6px; border-radius:99px; }
      .main { flex:1; min-width:0; padding:26px 22px 60px; }
      @media (max-width:820px) {
        .frame { flex-direction:column; }
        .rail { width:100%; flex-direction:row; overflow-x:auto; padding:10px 12px; border-bottom:1px solid var(--line); background:var(--panel); }
        .navbtn { border-left:none; border-bottom:2px solid transparent; white-space:nowrap; width:auto; }
        .navbtn-on { border-bottom-color:var(--accent); background:transparent; }
      }

      .page-head { display:flex; justify-content:space-between; align-items:flex-end; gap:14px; margin-bottom:18px; flex-wrap:wrap; }
      .page-head h1 { font-size:19px; font-weight:700; margin:0 0 4px; letter-spacing:-0.01em; }
      .lede { margin:0; color:var(--steel); font-size:13px; max-width:520px; }
      .head-actions { display:flex; gap:8px; }

      /* 카드/피드 */
      .card { background:var(--panel); border:1px solid var(--line); padding:16px 18px; margin-bottom:16px; }
      .card-head { display:flex; justify-content:space-between; align-items:baseline; margin-bottom:10px; }
      .eyebrow { font-size:11.5px; font-weight:700; letter-spacing:0.08em; color:var(--ink); text-transform:uppercase; }
      .grid-2 { display:grid; grid-template-columns:1fr; gap:16px; }
      @media (min-width:900px) { .grid-2 { grid-template-columns:1fr 1fr; align-items:start; } }

      .feed-item { padding:11px 10px; border-top:1px solid var(--line); transition:background .15s; }
      .feed-item:hover { background:#FAFBFD; }
      .feed-hl { background:var(--accent-soft); box-shadow:inset 2px 0 0 var(--accent); }
      .feed-meta { display:flex; align-items:center; gap:8px; margin-bottom:3px; }
      .feed-src { font-size:12px; font-weight:600; }
      .feed-title { font-weight:600; font-size:13.5px; margin-bottom:2px; }
      .feed-sum { color:var(--steel); font-size:12.5px; margin-bottom:6px; }
      .feed-tags { display:flex; gap:5px; flex-wrap:wrap; }

      .badge { font-size:10.5px; font-weight:600; padding:1px 6px; border-radius:2px; letter-spacing:0.02em; }
      .badge-adhoc { background:#FDF3E3; color:#9A6413; }
      .badge-periodic { background:#E8EEF7; color:#3A5E8C; }
      .badge-sec { background:#EFEAF7; color:#5E4A9E; }
      .badge-news { background:#E7F1EC; color:#2E6B57; }

      .tagchip { font-family:'IBM Plex Mono',monospace; font-size:11px; color:var(--steel);
        background:#F7F8FA; border:1px solid var(--line); border-left:3px solid var(--steel);
        padding:1px 7px; transition:color .12s; }
      .tagchip:hover { color:var(--ink); }
      .tagchip-static { pointer-events:none; }

      /* 필터 */
      .filterbar { background:var(--panel); border:1px solid var(--line); padding:12px 16px; margin-bottom:16px;
        display:flex; flex-direction:column; gap:8px; }
      .filter-row { display:flex; align-items:center; gap:6px; flex-wrap:wrap; }
      .filter-label { font-size:11.5px; color:var(--steel); font-weight:600; margin-right:4px; min-width:36px; }
      .filter-sep { width:1px; height:16px; background:var(--line); margin:0 8px; }
      .chip { font-size:12px; padding:3px 10px; background:transparent; border:1px solid var(--line);
        border-radius:99px; color:var(--steel); transition:all .12s; }
      .chip:hover { border-color:var(--steel); color:var(--ink); }
      .chip-on { border-color:var(--ink); color:var(--ink); font-weight:600; }

      /* 버튼 */
      .btn { display:inline-flex; align-items:center; gap:6px; font-size:13px; padding:8px 14px;
        background:var(--panel); border:1px solid var(--line); color:var(--ink); transition:all .12s; }
      .btn:hover:not(:disabled) { border-color:var(--steel); }
      .btn:disabled { opacity:.5; cursor:default; }
      .btn-primary { background:var(--accent); border-color:var(--accent); color:#fff; font-weight:600; }
      .btn-primary:hover:not(:disabled) { background:#C50026; border-color:#C50026; }
      .btn-danger:hover:not(:disabled) { border-color:var(--accent); color:var(--accent); }
      .btn-sm { padding:5px 10px; font-size:12px; }
      .btn-wide { width:100%; justify-content:center; margin-top:4px; }
      .iconbtn { background:transparent; border:none; color:var(--steel); padding:4px; }
      .iconbtn:hover { color:var(--ink); }
      .spin { animation:oispin 0.9s linear infinite; }
      @keyframes oispin { to { transform:rotate(360deg); } }

      /* 폼 */
      .field { margin-bottom:12px; }
      .field-label { display:block; font-size:12px; font-weight:600; color:var(--steel); margin-bottom:5px; }
      .input, .select, .textarea { width:100%; font-family:inherit; font-size:13.5px; color:var(--ink);
        background:#FAFBFD; border:1px solid var(--line); padding:9px 11px; }
      .textarea { resize:vertical; line-height:1.55; }
      .input:focus, .select:focus, .textarea:focus { outline:none; border-color:var(--steel); }
      .field-2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
      .aff-pick { display:flex; flex-wrap:wrap; gap:5px; }
      .case-badges { display:flex; gap:6px; align-items:center; flex-wrap:wrap; }
      .badge-pending { background:#FDF3E3; color:#9A6413; }
      .badge-approved { background:#E7F1EC; color:#2E6B57; }
      .badge-rejected { background:#F0F3F7; color:var(--steel); }
      .badge-src { background:#EFEAF7; color:#5E4A9E; }
      .case-actions { display:flex; gap:6px; margin-top:8px; align-items:center; }
      .case-actions .spacer { flex:1; }
      .ctx-note { font-size:11.5px; color:var(--steel); background:#F7F8FA; border:1px dashed var(--line);
        padding:7px 10px; margin-bottom:10px; }
      .errbox { display:flex; align-items:center; gap:7px; margin-top:10px; padding:9px 11px;
        background:var(--accent-soft); color:#A3001F; font-size:12.5px; }

      /* 과제 카드 */
      .task-card { padding:15px 16px; }
      .task-head { display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom:8px; }
      .task-title { font-weight:700; font-size:14.5px; margin-bottom:5px; }
      .task-meta { display:flex; align-items:center; gap:7px; }
      .cat { font-size:11.5px; color:var(--steel); border:1px solid var(--line); padding:1px 7px; border-radius:99px; }
      .row { display:flex; gap:10px; padding:4px 0; font-size:13px; }
      .rk { flex:none; width:52px; color:var(--steel); font-size:12px; padding-top:1px; }
      .rv { flex:1; }
      .formula { display:flex; align-items:baseline; gap:8px; flex-wrap:wrap; margin:9px 0;
        border:1px solid var(--line); border-left:3px solid var(--ink); background:#FAFBFD; padding:8px 12px; }
      .formula-name { font-size:12px; font-weight:700; }
      .formula-eq { font-family:'IBM Plex Mono',monospace; font-size:12.5px; color:var(--ink); }
      .task-evd { display:flex; gap:10px; align-items:center; margin:6px 0 10px; }
      .evd-wrap { display:flex; gap:6px; flex-wrap:wrap; }
      .evd { display:inline-flex; align-items:center; gap:2px; font-size:11.5px; color:var(--steel);
        background:transparent; border:1px solid var(--line); padding:2px 8px; border-radius:99px; transition:all .12s; }
      .evd:hover { color:var(--accent); border-color:var(--accent); }

      /* 테이블 */
      .table-card { padding:0; overflow-x:auto; }
      .tbl { width:100%; border-collapse:collapse; font-size:13px; }
      .tbl th { text-align:left; font-size:11.5px; color:var(--steel); font-weight:600;
        padding:10px 12px; border-bottom:1px solid var(--line); white-space:nowrap; }
      .tbl td { padding:10px 12px; border-bottom:1px solid var(--line); vertical-align:top; }
      .tbl tr:last-child td { border-bottom:none; }
      .th-chk { width:34px; }
      .td-title { font-weight:600; min-width:180px; }
      .td-kpi { font-size:12px; }
      .status { font-size:11.5px; background:#F0F3F7; color:var(--steel); padding:2px 8px; border-radius:99px; }

      /* 모달 */
      .overlay { position:fixed; inset:0; background:rgba(23,32,46,0.45); z-index:50;
        display:flex; align-items:center; justify-content:center; padding:20px; }
      .modal { background:var(--panel); width:100%; max-width:680px; max-height:86vh;
        display:flex; flex-direction:column; border:1px solid var(--line); }
      .modal-head { display:flex; justify-content:space-between; align-items:flex-start;
        padding:16px 18px 10px; gap:10px; }
      .export-area { flex:1; min-height:300px; margin:0 18px; padding:12px; font-size:11.5px;
        line-height:1.6; border:1px solid var(--line); background:#FAFBFD; color:var(--ink); resize:none; }
      .modal-actions { display:flex; gap:8px; padding:14px 18px; }

      /* 봇 */
      .chatwrap { max-width:640px; background:var(--panel); border:1px solid var(--line); }
      .chat-head { display:flex; align-items:center; gap:8px; padding:11px 15px;
        border-bottom:1px solid var(--line); font-size:13px; font-weight:600; }
      .chat-note { margin-left:auto; font-weight:400; }
      .chat-body { background:#EEF1F5; padding:16px 14px 22px; }
      .chat-day { text-align:center; font-size:11px; color:var(--steel); margin-bottom:12px; }
      .bubble { background:var(--panel); border:1px solid var(--line); padding:13px 14px;
        max-width:560px; box-shadow:0 1px 2px rgba(23,32,46,0.05); }
      .bubble-intro { font-size:13.5px; margin-bottom:10px; }
      .bot-card { display:flex; gap:11px; border-top:1px solid var(--line); padding:12px 2px; }
      .bot-rank { flex:none; color:var(--accent); font-weight:600; font-size:13px; padding-top:2px; }
      .bot-main { flex:1; min-width:0; }
      .bot-title { font-weight:700; font-size:13.5px; margin-bottom:5px; }

      /* 기타 */
      .empty-sm { color:var(--steel); font-size:12.5px; padding:14px 6px; }
      .empty-lg { display:flex; flex-direction:column; align-items:center; gap:8px;
        padding:44px 20px; text-align:center; color:var(--steel); font-size:13.5px; }
      .empty-actions { display:flex; gap:8px; margin-top:4px; }
      .foot-note { color:var(--steel); font-size:11.5px; margin-top:4px; }
    `}</style>
  );
}
