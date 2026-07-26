/*
 * 백엔드(FastAPI) 클라이언트.
 * VITE_API_BASE 가 있으면 절대 URL, 없으면 Vite 프록시(/api)를 사용합니다.
 * 과제 CRUD 는 백엔드가 응답하지 않으면 localStorage 로 폴백합니다.
 */
import { localStore } from "./storage.js";

const BASE = import.meta.env.VITE_API_BASE || "";

async function req(path, opts) {
  const res = await fetch(`${BASE}/api${path}`, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) throw new Error(`API 응답 오류 (${res.status})`);
  return res.json();
}

/* ── 과제 발굴 (과제 생성) ── */
export async function generateTasks(affCode, userNote) {
  const data = await req("/discovery/generate", {
    method: "POST",
    body: JSON.stringify({ aff: affCode, note: userNote || "" }),
  });
  const arr = data.tasks || [];
  if (!arr.length) throw new Error("생성된 과제가 없습니다.");
  return arr.map((t, i) => ({
    key: `gen-${i}-${t.title}`,
    aff: affCode,
    title: t.title || "무제 과제",
    category: t.category || "기타",
    background: t.background || "",
    plan: t.plan || "",
    risk: t.risk || "",
    effect: t.effect || "",
    kpi: { name: t.kpi?.name || "-", formula: t.kpi?.formula || "-" },
    evidence: t.evidence || [],
  }));
}

/* ── 저장된 과제 CRUD (백엔드 우선, localStorage 폴백) ── */
export async function fetchTasks() {
  try {
    const data = await req("/tasks");
    return data.tasks || [];
  } catch {
    return localStore.load();
  }
}

export async function createTask(task) {
  try {
    const data = await req("/tasks", { method: "POST", body: JSON.stringify(task) });
    return data.task;
  } catch {
    const tasks = localStore.load();
    const saved = { ...task, id: task.id || "OI-" + String(Date.now()).slice(-6) };
    localStore.save([saved, ...tasks]);
    return saved;
  }
}

export async function deleteTasks(ids) {
  try {
    await req("/tasks", { method: "DELETE", body: JSON.stringify({ ids }) });
  } catch {
    localStore.save(localStore.load().filter((t) => !ids.includes(t.id)));
  }
}

/* ── 혁신 사례 (지식 기반, 백엔드 필요 — localStorage 폴백 없음) ── */
export async function fetchCases(params = {}) {
  const qs = new URLSearchParams(
    Object.entries(params).filter(([, v]) => v)
  ).toString();
  try {
    const data = await req(`/cases${qs ? "?" + qs : ""}`);
    return data.cases || [];
  } catch {
    return [];
  }
}

export async function createCase(payload) {
  const data = await req("/cases", { method: "POST", body: JSON.stringify(payload) });
  return data.case;
}

export async function updateCaseStatus(id, status) {
  await req(`/cases/${id}/status`, { method: "PATCH", body: JSON.stringify({ status }) });
}

export async function deleteCase(id) {
  await req(`/cases/${id}`, { method: "DELETE" });
}
