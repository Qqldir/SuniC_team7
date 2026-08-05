import { useState } from "react";
import { Moon, Sun } from "lucide-react";
import { getTheme, applyTheme } from "../lib/theme.js";

/* 다크/라이트 전환 버튼 */
export default function ThemeToggle() {
  const [theme, setTheme] = useState(getTheme());
  const dark = theme === "dark";
  const toggle = () => setTheme(applyTheme(dark ? "light" : "dark"));
  return (
    <button
      className="theme-btn"
      type="button"
      onClick={toggle}
      title={dark ? "라이트 모드로 전환" : "다크 모드로 전환"}
      aria-label="테마 전환"
    >
      {dark ? <Moon size={15} /> : <Sun size={15} />}
    </button>
  );
}
