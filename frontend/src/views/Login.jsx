import { useMemo, useState } from "react";

/* 로그인 랜딩 페이지 — login.dc.html(편집 환경 구축) 충실 이식.
 * 항상 다크(퍼플/블루 · 별 배경). 회원가입/로그인 버튼 → 대시보드(/) 이동. */

/* 별 배경 box-shadow 문자열 생성 (레이어별) */
function makeStars(n) {
  let s = "";
  for (let i = 0; i < n; i++) {
    const x = Math.floor(Math.random() * 2000);
    const y = Math.floor(Math.random() * 2000);
    s += `${x}px ${y}px #fff${i < n - 1 ? "," : ""}`;
  }
  return s;
}

export default function Login() {
  const [open, setOpen] = useState(false);
  const enter = () => { window.location.href = "/trendroom.html"; };
  const openModal = (e) => { e?.preventDefault?.(); setOpen(true); };

  const stars = useMemo(() => ({
    s1: makeStars(700),
    s2: makeStars(200),
    s3: makeStars(100),
  }), []);

  return (
    <div className="lp">
      <style>{LP_CSS}</style>

      {/* 별 배경 */}
      <div className="lp-stars" aria-hidden="true">
        <div className="stars s1" style={{ "--sh": stars.s1 }} />
        <div className="stars s2" style={{ "--sh": stars.s2 }} />
        <div className="stars s3" style={{ "--sh": stars.s3 }} />
      </div>

      {/* 헤더 */}
      <header className="lp-header">
        <div className="lp-wrap lp-header-in">
          <a href="#top" className="lp-logo">
            <span className="lp-mark">O/I</span>
            <span>
              <span className="lp-logo-t">O/I Spark Agent AI</span>
              <span className="lp-logo-s">@ski.com</span>
            </span>
          </a>
          <nav className="lp-nav">
            <a href="#work">개요</a>
            <a href="#services">사용 설명</a>
          </nav>
        </div>
      </header>

      <main id="top" className="lp-main">
        {/* 히어로 */}
        <section className="lp-hero lp-wrap">
          <h1 className="lp-h1">흩어진 외부 자료를<br />계열사 맞춤 혁신 과제로</h1>
          <p className="lp-hero-sub">O/I Spark agent is here to help all your research needs.</p>
          <div className="lp-cta-row">
            <button className="btn-grad" onClick={openModal}>Outlook으로 연결</button>
            <a className="btn-ghost" href="#work">See service overview</a>
          </div>
          <div className="lp-demo" role="img" aria-label="O/I Spark 미리보기">
            <span className="lp-demo-tag">3D · Retroactive glass material</span>
          </div>
        </section>

        {/* 서비스 개요 */}
        <section id="work" className="lp-section lp-wrap">
          <div className="lp-sec-head">
            <div className="lp-eyebrow">Service Overview</div>
            <h2 className="lp-h2">주요 기능과 외부자료 DB</h2>
          </div>
          <div className="ov-grid">
            {OVERVIEW.map((o) => (
              <div key={o.label} className="ov-card" style={{ background: o.bg }}>
                <span className="ov-label">{o.label}</span>
              </div>
            ))}
          </div>
        </section>

        {/* 서비스 상세 */}
        <section id="services" className="lp-section lp-wrap">
          <div className="lp-sec-head">
            <div className="lp-eyebrow">Service Detail</div>
            <h2 className="lp-h2">주요 기능 상세</h2>
          </div>
          <div className="sd-grid">
            {DETAIL.map((d) => (
              <div key={d.title} className="sd-card">
                <div className="sd-icon" style={{ background: d.iconBg, borderColor: d.iconBd }}>{d.icon}</div>
                <h3 className="sd-title">{d.title}</h3>
                <p className="sd-desc">{d.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Pricing / DB */}
        <section id="pricing" className="lp-section lp-wrap">
          <div className="lp-sec-head">
            <div className="lp-eyebrow">DB</div>
            <h2 className="lp-h2">수많은 외부 자료, 정리된 DB로</h2>
          </div>
          <div className="price-wrap">
            <div>
              <span className="price-badge">룰루</span>
              <h3 className="price-h3">n개의 외부 자료 종류</h3>
              <p className="price-p">다양한 곳에서 가져오는 외부 자료를<br />연결해서 DB만들고 어쩌구 저쩌구</p>
              <ul className="feat-list">
                {FEATURES.map((f) => (
                  <li key={f}><span className="feat-ico">✓</span>{f}</li>
                ))}
              </ul>
            </div>
            <div className="price-card">
              <div className="price-num">999<small>per 1 day</small></div>
              <div className="price-note">!</div>
              <button className="btn-grad btn-block" onClick={enter}>Go to main page</button>
            </div>
          </div>
        </section>

        {/* 하단 CTA */}
        <section className="lp-wrap" style={{ padding: "56px 24px" }}>
          <div className="cta-box">
            <h2 className="cta-h2">새로운 과제 아이디어를<br />생성할 준비가 됐나요?</h2>
            <p className="cta-p">Chill Guys 팀에 점수 많이 주시고 이 서비스 많이많이 활용해주세염~</p>
            <button className="btn-grad" onClick={openModal}>Outlook으로 연결</button>
          </div>
        </section>
      </main>

      {/* 푸터 */}
      <footer className="lp-footer">
        <div className="lp-wrap lp-footer-in">
          <a href="#top" className="lp-logo">
            <span className="lp-mark sm">O/I</span>
            <span><span className="lp-logo-t sm">O/I Spark</span><span className="lp-logo-s">@ski.com</span></span>
          </a>
          <div className="lp-foot-links">
            <a href="#top">Privacy Policy</a>
            <a href="#top">Terms and Conditions</a>
          </div>
          <div className="lp-copy">© 2026 SUNIC 5기 Chill Guys</div>
        </div>
      </footer>

      {/* 회원가입/로그인 모달 */}
      {open && (
        <div className="lp-overlay" onClick={() => setOpen(false)}>
          <div className="lp-modal" onClick={(e) => e.stopPropagation()}>
            <button className="lp-modal-x" onClick={() => setOpen(false)} aria-label="닫기">×</button>
            <h2 className="lp-modal-t">Sign Up</h2>
            <p className="lp-modal-d">Connect your Outlook mail to O/I Spark.</p>

            <form onSubmit={(e) => { e.preventDefault(); enter(); }}>
              <label className="lp-lbl">Email</label>
              <div className="lp-inp"><span className="lp-inp-i">✉</span>
                <input type="text" placeholder="Enter your Email" /></div>

              <label className="lp-lbl">Password</label>
              <div className="lp-inp"><span className="lp-inp-i">🔒</span>
                <input type="password" placeholder="Enter your Password" /></div>

              <div className="lp-row-between">
                <label className="lp-remember"><input type="checkbox" /> Remember me</label>
                <span className="lp-link">Forgot password?</span>
              </div>

              <button className="lp-signup" type="submit">Sign Up</button>
            </form>

            <p className="lp-modal-foot">Already have an account? <span className="lp-link" onClick={enter}>Sign In</span></p>
            <p className="lp-or">Or With</p>
            <div className="lp-social">
              <button type="button" onClick={enter}>Outlook</button>
              <button type="button" onClick={enter}>Google</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const OVERVIEW = [
  { label: "과제 제안", bg: "linear-gradient(140deg,#1b1436,#4c2fa8)" },
  { label: "커스텀 과제 제안", bg: "linear-gradient(140deg,#2a1b4d,#7c5cff)" },
  { label: "트렌드룸", bg: "linear-gradient(140deg,#101b3d,#3b6ef5)" },
  { label: "프롬프트 내보내기", bg: "linear-gradient(140deg,#0d1226,#2b4b8f)" },
  { label: "AI 리포팅", bg: "linear-gradient(140deg,#3a1160,#9b4dff)" },
  { label: "비지니스 DB", bg: "linear-gradient(140deg,#131320,#3d3d5c)" },
  { label: "과제 DB / 학습 Logic", bg: "linear-gradient(140deg,#1a2b8a,#6f8bff)" },
];

const P = { iconBg: "rgba(139,92,246,.14)", iconBd: "rgba(139,92,246,.28)" };
const B = { iconBg: "rgba(59,110,245,.16)", iconBd: "rgba(59,110,245,.3)" };
const DETAIL = [
  { icon: "🖥️", title: "과제 제안", desc: "과제 제안 잘하죠~", ...P },
  { icon: "📱", title: "커스텀 과제 제안", desc: "~~~~~~", ...P },
  { icon: "🧩", title: "최근 사업 동향", desc: "Biz별 최근 산업 시장을 키워드로 구분하고 업데이트. 새로운 키워드면 과거 자료까지 소급 적용", ...B },
  { icon: "✦", title: "외부자료 실시간 통합 DB", desc: "수많은 외부자료를 실시간으로 통합하고, 고정된 축으로 분리 및 정리", ...B },
  { icon: "📣", title: "사용자의 피드백 수용", desc: "생성된 과제에 피드백 한 줄이 주는 성능 개선 효과", ...P },
  { icon: "⚡", title: "내부자료 활용 용이", desc: "프롬프트 내보내기 쉽고, csv·pdf 파일로 서비스 DB와 내부 자료를 쉽게 통합", ...B },
];

const FEATURES = [
  "실시간 크롤링으로 어쩌구",
  "산업별 혁신 과제를 정리한 DB",
  "하루 평균 신규 추가되는 외부자료 n개",
  "내부자료나 새로운 소스 생기면 추가하삼",
  "n8n 어쩌구~",
  "관리자 기능에서 어쩌구",
];

const LP_CSS = `
.lp{--acc:#a855f7;--acc2:#38bdf8;--acc-glow:rgba(168,85,247,.6);
  min-height:100vh;position:relative;overflow-x:hidden;color:#edeaf7;line-height:1.5;
  background:radial-gradient(ellipse at bottom,#140f2b 0%,#07070c 70%);
  font-family:'Pretendard Variable',Pretendard,-apple-system,'Noto Sans KR',sans-serif}
.lp a{color:inherit;text-decoration:none}
.lp ::selection{background:#6d3bff;color:#fff}
.lp-wrap{max-width:1080px;margin:0 auto;padding-left:24px;padding-right:24px}

/* 별 배경 */
.lp-stars{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none}
.lp .stars{position:absolute;top:0;left:0;background:transparent;box-shadow:var(--sh)}
.lp .stars::after{content:" ";position:absolute;top:2000px;left:0;background:transparent;box-shadow:var(--sh)}
.lp .s1{width:1px;height:1px;animation:lpstar 50s linear infinite}
.lp .s1::after{width:1px;height:1px}
.lp .s2{width:2px;height:2px;animation:lpstar 100s linear infinite}
.lp .s2::after{width:2px;height:2px}
.lp .s3{width:3px;height:3px;animation:lpstar 150s linear infinite}
.lp .s3::after{width:3px;height:3px}
@keyframes lpstar{from{transform:translateY(0)}to{transform:translateY(-2000px)}}
@media (prefers-reduced-motion:reduce){.lp .stars{animation:none}}

/* 헤더 */
.lp-header{position:sticky;top:0;z-index:50;backdrop-filter:saturate(180%) blur(14px);
  background:rgba(9,9,16,.72);border-bottom:1px solid rgba(255,255,255,.08)}
.lp-header-in{display:flex;align-items:center;justify-content:space-between;height:74px}
.lp-logo{display:flex;align-items:center;gap:10px;font-weight:600}
.lp-mark{background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;font-weight:700;
  font-size:13px;padding:5px 8px;border-radius:8px;letter-spacing:.02em}
.lp-mark.sm{font-size:11px;padding:4px 7px}
.lp-logo-t{display:block;font-size:19px;letter-spacing:-.02em;
  background:linear-gradient(100deg,#f5f3ff,#a855f7 45%,#38bdf8);-webkit-background-clip:text;
  background-clip:text;color:transparent}
.lp-logo-t.sm{font-size:15px}
.lp-logo-s{display:block;color:#8b87a8;font-weight:400;font-size:12px}
.lp-nav{display:flex;gap:26px;font-size:14.5px;color:#8b87a8}
.lp-nav a:hover{color:#edeaf7}

.lp-main{position:relative;z-index:1}

/* 히어로 */
.lp-hero{padding:72px 24px 56px;text-align:center}
.lp-h1{font-size:clamp(38px,8vw,70px);line-height:1.02;letter-spacing:-.03em;font-weight:600;
  max-width:18ch;margin:0 auto 22px;color:#f6f4ff}
.lp-hero-sub{font-size:clamp(17px,2.4vw,21px);color:#8b87a8;max-width:46ch;margin:0 auto 34px}
.lp-cta-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-grad{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(135deg,var(--acc),var(--acc2));
  color:#fff;padding:11px 20px;border-radius:999px;font-size:14.5px;font-weight:500;
  border:1px solid rgba(255,255,255,.14);box-shadow:0 10px 30px -12px var(--acc-glow);
  cursor:pointer;transition:transform .15s ease}
.btn-grad:hover{transform:translateY(-1px)}
.btn-block{width:100%;justify-content:center}
.btn-ghost{display:inline-flex;align-items:center;gap:8px;background:transparent;color:#edeaf7;
  padding:11px 20px;border-radius:999px;font-size:14.5px;font-weight:500;
  border:1px solid rgba(255,255,255,.14);transition:background .15s ease}
.btn-ghost:hover{background:rgba(255,255,255,.06)}
.lp-demo{margin:56px auto 0;max-width:760px;height:280px;border-radius:28px;position:relative;overflow:hidden;
  background:radial-gradient(120% 140% at 20% 10%,rgba(168,85,247,.55) 0%,transparent 55%),
    radial-gradient(120% 120% at 90% 20%,rgba(56,189,248,.5) 0%,transparent 50%),
    radial-gradient(140% 140% at 50% 120%,rgba(56,189,248,.5) 0%,transparent 55%),
    linear-gradient(135deg,#141026,#0b1226);
  border:1px solid rgba(255,255,255,.1);
  box-shadow:0 40px 90px -40px rgba(109,59,255,.55),inset 0 1px 0 rgba(255,255,255,.12)}
.lp-demo-tag{position:absolute;left:50%;bottom:18px;transform:translateX(-50%);font-size:13px;
  color:rgba(237,234,247,.75);background:rgba(10,10,20,.5);padding:6px 12px;border-radius:999px;
  backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.08);white-space:nowrap}

/* 섹션 공통 */
.lp-section{padding:56px 24px}
.lp-sec-head{text-align:center;margin-bottom:40px}
.lp-eyebrow{font-size:13.5px;letter-spacing:.14em;text-transform:uppercase;color:#8b87a8;margin-bottom:14px}
.lp-h2{font-size:clamp(28px,4.4vw,42px);letter-spacing:-.02em;font-weight:600;color:#f6f4ff;margin:0}

/* 개요 카드 */
.ov-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.ov-card{border-radius:22px;aspect-ratio:4/3;border:1px solid rgba(255,255,255,.09);position:relative;
  overflow:hidden;box-shadow:0 24px 50px -34px rgba(0,0,0,.9)}
.ov-label{position:absolute;left:16px;bottom:14px;font-size:13.5px;color:rgba(255,255,255,.92);font-weight:500}

/* 상세 카드 */
.sd-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}
.sd-card{background:#0e0e18;border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:26px 24px;
  transition:transform .15s ease,border-color .15s ease}
.sd-card:hover{transform:translateY(-3px);border-color:rgba(139,92,246,.45)}
.sd-icon{width:42px;height:42px;border-radius:12px;border:1px solid;display:grid;place-items:center;
  margin-bottom:16px;font-size:20px}
.sd-title{font-size:18px;font-weight:600;letter-spacing:-.01em;margin:0 0 6px;color:#f6f4ff}
.sd-desc{font-size:14.5px;color:#8b87a8;margin:0}

/* Pricing */
.price-wrap{background:linear-gradient(150deg,#150f2e,#0b1024 60%,#0a0a14);
  border:1px solid rgba(139,92,246,.28);border-radius:28px;padding:44px;
  display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:40px;align-items:center;
  box-shadow:0 50px 100px -60px rgba(109,59,255,.7)}
.price-badge{display:inline-block;background:rgba(139,92,246,.18);border:1px solid rgba(139,92,246,.34);
  color:#c4b5fd;padding:6px 14px;border-radius:999px;font-size:13px;margin-bottom:18px}
.price-h3{font-size:clamp(24px,3.4vw,32px);font-weight:600;letter-spacing:-.02em;margin:0 0 8px;color:#f6f4ff}
.price-p{color:#9e9abb;margin:0 0 26px;max-width:34ch}
.feat-list{list-style:none;display:grid;gap:12px;padding:0;margin:0}
.feat-list li{display:flex;gap:10px;align-items:flex-start;font-size:15px;color:#d7d3ea}
.feat-ico{width:18px;height:18px;flex:0 0 18px;margin-top:2px;border-radius:50%;display:grid;place-items:center;
  background:linear-gradient(135deg,#8b5cf6,#3b6ef5);color:#fff;font-size:11px;font-weight:700}
.price-card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.12);border-radius:20px;
  padding:30px;text-align:center}
.price-num{font-size:44px;font-weight:600;letter-spacing:-.02em;color:#f6f4ff}
.price-num small{font-size:16px;color:#8b87a8;font-weight:400;margin-left:4px}
.price-note{font-size:13.5px;color:#8b87a8;margin:8px 0 22px}

/* CTA */
.cta-box{text-align:center;border:1px solid rgba(139,92,246,.24);border-radius:28px;padding:56px 32px;
  background:radial-gradient(120% 160% at 50% 0%,rgba(109,59,255,.35) 0%,transparent 60%),
    linear-gradient(160deg,#120e26,#0a0a14);box-shadow:0 50px 100px -60px rgba(109,59,255,.7)}
.cta-h2{font-size:clamp(28px,4.6vw,44px);letter-spacing:-.025em;font-weight:600;margin:0 auto 14px;
  max-width:18ch;color:#f6f4ff}
.cta-p{color:#9e9abb;margin:0 0 26px}

/* 푸터 */
.lp-footer{position:relative;z-index:1;padding:40px 0 60px;border-top:1px solid rgba(255,255,255,.08);margin-top:56px}
.lp-footer-in{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.lp-foot-links{display:flex;gap:22px;font-size:14px;color:#8b87a8}
.lp-foot-links a:hover{color:#edeaf7}
.lp-copy{font-size:13.5px;color:#6e6a88;width:100%;padding-top:20px;
  border-top:1px solid rgba(255,255,255,.08);margin-top:6px}

/* 모달 */
.lp-overlay{position:fixed;inset:0;z-index:60;display:flex;align-items:center;justify-content:center;
  padding:24px;background:rgba(4,4,10,.72);backdrop-filter:blur(8px)}
.lp-modal{position:relative;display:flex;flex-direction:column;gap:10px;width:100%;max-width:450px;padding:30px;
  border-radius:20px;background:linear-gradient(160deg,#161231,#0c0b1a);border:1px solid rgba(255,255,255,.12);
  box-shadow:0 40px 90px -30px rgba(109,59,255,.55),inset 0 1px 0 rgba(255,255,255,.1);max-height:88vh;overflow:auto}
.lp-modal-x{position:absolute;top:16px;right:16px;width:32px;height:32px;border-radius:50%;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);color:#9e9abb;font-size:16px;cursor:pointer}
.lp-modal-x:hover{background:rgba(255,255,255,.12);color:#edeaf7}
.lp-modal-t{margin:0;font-size:24px;font-weight:600;letter-spacing:-.02em;color:#f6f4ff}
.lp-modal-d{margin:0 0 12px;font-size:14px;color:#8b87a8}
.lp-lbl{color:#edeaf7;font-weight:600;font-size:14px;margin-top:6px}
.lp-inp{display:flex;align-items:center;gap:10px;height:50px;padding:0 14px;border-radius:10px;
  background:rgba(255,255,255,.04);border:1.5px solid rgba(255,255,255,.14)}
.lp-inp:focus-within{border-color:var(--acc)}
.lp-inp-i{font-size:15px;opacity:.7}
.lp-inp input{flex:1;height:100%;border:none;outline:none;background:transparent;color:#f6f4ff;font-size:14.5px}
.lp-row-between{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px}
.lp-remember{display:flex;align-items:center;gap:8px;font-size:14px;color:#9e9abb}
.lp-remember input{accent-color:var(--acc);width:16px;height:16px}
.lp-link{color:#a78bfa;font-weight:500;cursor:pointer}
.lp-signup{margin:18px 0 8px;height:50px;width:100%;border:none;border-radius:10px;
  background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;font-size:15px;font-weight:600;
  cursor:pointer;box-shadow:0 12px 30px -12px var(--acc-glow);transition:transform .15s ease}
.lp-signup:hover{transform:translateY(-1px)}
.lp-modal-foot{text-align:center;font-size:14px;color:#8b87a8;margin:4px 0}
.lp-or{text-align:center;font-size:13px;color:#6e6a88;margin:10px 0}
.lp-social{display:flex;gap:10px}
.lp-social button{flex:1;height:50px;border-radius:10px;font-size:14px;font-weight:500;color:#edeaf7;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);cursor:pointer;transition:.2s}
.lp-social button:hover{border-color:var(--acc);background:rgba(255,255,255,.09)}

@media (max-width:640px){.lp-header-in{height:64px}.lp-logo-t{font-size:16px}}
`;
