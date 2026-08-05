import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Mail, Lock } from "lucide-react";

/* 로그인 화면 — login.dc.html 디자인 이식.
 * 데모 단계: 실제 인증 없이 로그인 시 대시보드(/)로 이동. */
export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");

  const signIn = (e) => {
    e.preventDefault();
    // TODO: 백엔드 인증 연동 (현재는 데모 통과)
    navigate("/");
  };

  return (
    <div className="login-wrap">
      <form className="login-card" onSubmit={signIn}>
        <div className="login-brand">
          <span className="brand-mark">O/I</span>
          <div>
            <div className="brand-name">O/I Spark</div>
            <div className="brand-sub">SK이노베이션 O/I추진단</div>
          </div>
        </div>

        <h1 className="login-title">로그인</h1>
        <p className="login-desc">Outlook 계정으로 O/I Spark에 연결하세요.</p>

        <div className="field">
          <label className="field-label">이메일</label>
          <div style={{ position: "relative" }}>
            <Mail size={16} style={iconStyle} />
            <input
              className="input"
              style={{ paddingLeft: 34 }}
              type="text"
              placeholder="이메일을 입력하세요"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
        </div>

        <div className="field">
          <label className="field-label">비밀번호</label>
          <div style={{ position: "relative" }}>
            <Lock size={16} style={iconStyle} />
            <input
              className="input"
              style={{ paddingLeft: 34 }}
              type="password"
              placeholder="비밀번호를 입력하세요"
              value={pw}
              onChange={(e) => setPw(e.target.value)}
            />
          </div>
        </div>

        <button className="login-btn" type="submit">로그인</button>

        <div className="login-or">또는</div>
        <div className="login-social">
          <button className="btn" type="button" onClick={signIn}>Outlook</button>
          <button className="btn" type="button" onClick={signIn}>Google</button>
        </div>

        <p className="login-foot">
          계정이 없으신가요? <span className="login-link" onClick={signIn} style={{ cursor: "pointer" }}>회원가입</span>
        </p>
      </form>
    </div>
  );
}

const iconStyle = {
  position: "absolute",
  left: 11,
  top: "50%",
  transform: "translateY(-50%)",
  color: "var(--steel)",
  pointerEvents: "none",
};
