/*
 * 백엔드(SQLite)가 없을 때의 과제 저장 폴백.
 * 원본 데모의 window.storage 역할을 브라우저 localStorage로 대체합니다.
 */
const KEY = "oi-scout:tasks";

export const localStore = {
  load() {
    try {
      const raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  },
  save(tasks) {
    try {
      localStorage.setItem(KEY, JSON.stringify(tasks));
    } catch {
      /* 저장 실패 시 세션 내 유지 */
    }
  },
};
