import { Download, Trash2, FolderCheck } from "lucide-react";
import { AFF, BIZ } from "../data/affiliates.js";
import { md } from "../lib/utils.js";

export default function SavedView({
  tasks, checked, setChecked, allChecked, toggleAll, downloadCsv, removeChecked, goGen, goBot,
}) {
  const toggle = (id) => setChecked((c) => (c.includes(id) ? c.filter((x) => x !== id) : [...c, id]));
  return (
    <div>
      <div className="page-head">
        <div>
          <h1>저장된 과제</h1>
          <p className="lede">저장한 과제 인스턴스를 관리하고, 기존 과제 기록 DB와 같은 스키마의 CSV로 내려받습니다.</p>
        </div>
        <div className="head-actions">
          <button className="btn" onClick={downloadCsv} disabled={tasks.length === 0}>
            <Download size={15} /> CSV 내려받기{checked.length ? ` (${checked.length}건)` : " (전체)"}
          </button>
          <button className="btn btn-danger" onClick={removeChecked} disabled={checked.length === 0}>
            <Trash2 size={15} /> 선택 삭제
          </button>
        </div>
      </div>

      {tasks.length === 0 ? (
        <div className="card empty-lg">
          <FolderCheck size={20} className="dim" />
          <div>아직 저장된 과제가 없습니다.</div>
          <div className="empty-actions">
            <button className="btn btn-sm" onClick={goGen}>과제 생성하러 가기</button>
            <button className="btn btn-sm" onClick={goBot}>봇 제안 보기</button>
          </div>
        </div>
      ) : (
        <div className="card table-card">
          <table className="tbl">
            <thead>
              <tr>
                <th className="th-chk"><input type="checkbox" checked={allChecked} onChange={toggleAll} aria-label="전체 선택" /></th>
                <th>생성일</th><th>계열사</th><th>과제명</th><th>분류</th><th>KPI</th><th>상태</th><th>경로</th>
              </tr>
            </thead>
            <tbody>
              {tasks.map((t) => (
                <tr key={t.id}>
                  <td className="th-chk"><input type="checkbox" checked={checked.includes(t.id)} onChange={() => toggle(t.id)} aria-label={t.title + " 선택"} /></td>
                  <td className="mono dim">{md(t.createdAt)}</td>
                  <td><span className="tagchip tagchip-static" style={{ borderLeftColor: BIZ[AFF[t.aff]?.biz || "energy"].color }}>{t.aff}</span></td>
                  <td className="td-title">{t.title}</td>
                  <td className="dim">{t.category}</td>
                  <td className="mono td-kpi" title={t.kpiFormula}>{t.kpiName}</td>
                  <td><span className="status">{t.status}</span></td>
                  <td className="dim-xs">{t.origin}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
      <p className="foot-note">CSV 컬럼은 기존 과제 기록 DB 스키마 기준으로 고정 — 실제 DB 컬럼 확인 후 매핑만 교체합니다(기획안 6.3). 저장 데이터는 백엔드 SQLite(또는 미연결 시 브라우저)에 유지됩니다.</p>
    </div>
  );
}
