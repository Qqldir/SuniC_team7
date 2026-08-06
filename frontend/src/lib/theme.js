/* 테마(다크/라이트) 유틸 — data-theme 속성 + localStorage */
const KEY = "oi-theme";

export function getTheme() {
  try {
    return localStorage.getItem(KEY) === "light" ? "light" : "dark";
  } catch {
    return "dark";
  }
}

export function applyTheme(theme) {
  const t = theme === "light" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", t);
  try {
    localStorage.setItem(KEY, t);
  } catch {
    /* ignore */
  }
  return t;
}

/* 앱 로드 시 저장된 테마(기본 dark)를 즉시 적용 */
export function initTheme() {
  return applyTheme(getTheme());
}
