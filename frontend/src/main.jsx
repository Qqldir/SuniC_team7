import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import App from "./App.jsx";
import Login from "./views/Login.jsx";
import StyleBlock from "./styles.jsx";
import { initTheme } from "./lib/theme.js";

initTheme(); // 저장된 테마(기본 dark) 즉시 적용

createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <StyleBlock />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/*" element={<App />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
