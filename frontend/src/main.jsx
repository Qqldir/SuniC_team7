import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Login from "./views/Login.jsx";
import StyleBlock from "./styles.jsx";
import { initTheme } from "./lib/theme.js";

initTheme(); // 저장된 테마(기본 dark) 즉시 적용

/* 진입 = 로그인 랜딩(React) → 로그인 시 정적 앱(/trendroom.html)으로 이동.
 * 실제 앱 화면(과제 제안·트렌드룸·관리자 등)은 public/trendroom.html 이 전부 담고 있음. */
createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <StyleBlock />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
