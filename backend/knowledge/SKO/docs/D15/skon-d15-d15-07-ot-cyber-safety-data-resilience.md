---
id: skon-d15-d15-07-ot-cyber-safety-data-resilience
title: OT Cyber–Safety & Data Resilience
summary: 운영기술(OT) 시스템의 사이버보안과 데이터 복원력 확보를 위한 핵심 통제(자산·접근·버전·백업)과 AI의사결정 가드레일을 규정한다.
tags: [d15, risk, schema]
keywords: [산업제어시스템, IEC 62443, Asset Inventory, 원격접근, PLC, Safety Interlock, 불변 백업, AI Guardrail, 변경통제, 사이버인시던트, 원격접속, Immutable Backup, AI 가드레일, Model Drift, 사이버 인시던트]
related: []
priority: normal
domain: D15
section: D15-07
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 461
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-07 OT Cyber–Safety & Data Resilience

### 1. 핵심 통제

- IT–OT Zone·Conduit와 생산 Cell/Line별 Asset Inventory
- Vendor Remote Access의 시간제한·승인·Session Recording
- PLC·Robot·Recipe·Inspection Model·BMS Calibration의 Signed Version과 Change Control
- Safety PLC·Hardwired Interlock을 최적화 AI와 독립 유지
- Patch 불가 Asset의 Compensating Control과 만료일
- MES·Historian·Genealogy의 Immutable Backup, Restore Test, 시간동기화
- Model Drift·False Negative·Training Data Lineage와 Rollback
- Cyber Incident 시 안전정지·품질 Hold·수동운전의 사전 승인절차

IEC 62443은 산업제어시스템을 Lifecycle 전체에서 다루고, Product Secure Development에는 요구사항·설계·구현·검증·결함·Patch·EOL 관리가 포함된다. D15는 인증 보유 여부보다 실제 Line Asset·변경·복구 Evidence를 관리한다. ([IEC 62443](https://www.iec.ch/blog/understanding-iec-62443))

### 2. AI Decision Guardrail

```yaml
AI_safety_guardrail:
  allowed:
    - anomaly_ranking
    - suspected_population_draft
    - evidence_gap_detection
    - scenario_simulation
    - CAPA_similarity_search
  prohibited_without_human_approval:
    - safety_interlock_bypass
    - shipment_or_product_release
    - recall_scope_finalization
    - regulatory_or_customer_notification
    - root_cause_final_determination
    - employee_discipline_or_supplier_blocking
  mandatory_lineage:
    - model_version_input_snapshot_threshold_output_reviewer_and_action
```

---
