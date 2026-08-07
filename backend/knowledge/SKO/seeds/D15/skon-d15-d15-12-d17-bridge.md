---
id: skon-d15-d15-12-d17-bridge
title: D17 Bridge
summary: "SK온 D15 도메인의 리스크·품질·안전 정보를 D17로 전달하기 위한 cross-domain 연결 체계, 필수 필드, 검증 게이트를 정의한 문서입니다."
tags: [d15, risk, oi-seed, schema, table, "xref:d17", "xref:d01", "xref:d03", "xref:d04"]
keywords: [도메인 매핑, Cross-domain, 전달 규칙, 필수 필드, 검증 게이트, 리스크 정보, CAPA, genealogy, OI_seed_id, 우선순위, D15, D17, cross-domain, 리스크 관리, 품질, 안전, 회복탄력성, Failure Mode]
related: []
priority: normal
domain: D15
section: D15-12
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1624
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-12 D17 Bridge

### 1. Cross-domain 연결

| D15 정보 | 연결 도메인 | D17에서 사용할 질문 |
|---|---|---|
| 법인·위원회·Owner | D01 | 누가 위험을 소유·도전·승인·감사하는가? |
| 제품·화학계·안전기술 | D03·D04 | 어떤 Failure Mode·Barrier·사용조건에 노출되는가? |
| R&D·IP·변경 | D05 | 설계변경·License·Data 권리가 CAPA를 막거나 촉진하는가? |
| 공정·검사·설비 | D06 | 어느 공정변수·검사·Change가 Field Failure와 연결되는가? |
| 공장·용량·대체 Site | D07 | 어느 Site가 Single Point이고 대체 Qualification에 얼마나 걸리는가? |
| 원료·공급망 | D08 | 공통 Supplier·Lot·원산지 Risk가 여러 제품에 전파되는가? |
| 고객·Program | D09 | 어떤 OEM·VIN·ESS Site·계약 Population이 노출되는가? |
| 시장·경쟁 | D10 | 수요·가격·기술 변화가 Risk Appetite와 Recovery Option을 바꾸는가? |
| 원가·보증·현금 | D11 | 품질손실·Downtime·Remedy가 반복이익과 Cash에 미치는 범위는? |
| CAPEX·Funding | D12 | 복원력 투자와 미투자 Tail Loss·Covenant를 어떻게 비교할 것인가? |
| 계약·JV | D13 | 통지·보증·보험·Data·Recall·Exit 의무는 누구에게 있는가? |
| 정책·규제 | D14 | 어떤 사건이 신고·시장접근·세액공제·Clawback을 촉발하는가? |
| 외부 Solution | D16 | RiskTech·QualityTech·SafetyTech·CyberTech의 빈칸을 누가 채우는가? |

### 2. D17 전달 규칙

```yaml
d17_handoff_rule:
  mandatory_fields:
    - oi_seed_id_and_risk_event_or_failure_mode
    - affected_entity_plant_line_product_lot_serial_customer_and_period
    - trigger_signal_denominator_and_detection_latency
    - hazard_issue_incident_loss_and_cause_confidence
    - preventive_detective_corrective_and_recovery_controls
    - genealogy_population_inclusion_exclusion_and_unknown_tail
    - containment_root_cause_CAPA_effectiveness_and_horizontal_deployment
    - residual_risk_tail_scenario_and_acceptance_owner
    - required_internal_data_access_rights_and_current_gap
    - partner_type_PoC_duration_shadow_mode_and_control_group
    - KPI_in_hours_days_percent_population_kWh_KRW_USD_and_safety_outcome
    - source_ids_and_human_approvers
  gates:
    - never_generalize_one_incident_to_enterprise_quality
    - never_use_small_recall_population_as_a_safety_success_metric
    - require_population_denominator_genealogy_and_unknown_tail
    - keep_correlation_mechanism_reproduction_and_verified_cause_separate
    - include_low_frequency_high_severity_and_common_cause_scenarios
    - require_quality_SHE_cyber_legal_customer_and_plant_approval
    - prohibit_autonomous_release_recall_notification_root_cause_or_safety_bypass
```

### 3. D17 우선 전달 레코드

```yaml
d15_priority_handoff:
  - oi_seed_id: OI-D15-02
    title: Process-to-Field Quality Digital Thread
    problem_proxy: material_process_inspection_pack_vehicle_field_and_CAPA_are_fragmented
    owner: quality_manufacturing_customer_quality_IT_data
    partner_type: industrial_data_fabric_qualitytech_connected_vehicle
    poc_duration: 6_to_9_months
    success_kpi: complete_genealogy_and_faster_verified_root_cause_for_one_program
    source_ids: [SRC-D15-005, SRC-D15-008, SRC-D15-009]

  - oi_seed_id: OI-D15-03
    title: Defect Population and Recall Scope Engine
    problem_proxy: inclusion_exclusion_and_unknown_tail_are_manually_reconstructed
    owner: product_quality_legal_customer_quality_manufacturing
    partner_type: graph_analytics_reliability_AI_evidence_workflow
    poc_duration: 4_to_6_months
    success_kpi: reproducible_population_with_no_known_defective_serial_excluded
    source_ids: [SRC-D15-005, SRC-D15-006, SRC-D15-007]

  - oi_seed_id: OI-D15-04
    title: Early Field Failure Signal Fusion
    problem_proxy: telemetry_DTC_complaint_warranty_and_return_signals_are_reviewed_separately
    owner: field_quality_BMS_OEM_interface_warranty_data
    partner_type: anomaly_AI_NLP_connected_vehicle_analytics
    poc_duration: 6_to_9_months
    success_kpi: earlier_detection_with_controlled_false_alarm_and_valid_denominator
    source_ids: [SRC-D15-008, SRC-D15-009]

  - oi_seed_id: OI-D15-10
    title: OT Cyber-Safety Guardrail
    problem_proxy: enterprise_ISMS_does_not_prove_line_level_OT_and_safety_control_health
    owner: plant_OT_cyber_SHE_quality_engineering
    partner_type: OT_security_IEC62443_integrator_configuration_management
    poc_duration: 6_to_9_months
    success_kpi: critical_asset_access_change_backup_restore_and_safe_mode_validation
    source_ids: [SRC-D15-002, SRC-D15-016]

  - oi_seed_id: OI-D15-08
    title: Plant SHE Barrier Health Monitor
    problem_proxy: lagging_incident_rate_does_not_show_degraded_barriers_or_high_potential_near_misses
    owner: plant_SHE_operations_maintenance_emergency_response
    partner_type: EHStech_sensor_analytics_process_safety
    poc_duration: 4_to_6_months
    success_kpi: lower_barrier_impairment_hours_and_faster_HiPo_action_closure
    source_ids: [SRC-D15-003, SRC-D15-004, SRC-D15-015]
```

D15가 D17에 넘기는 핵심은 `AI로 Risk를 예측하자`는 일반론이 아니다. **제품·공정·공장·고객·계약·현금에 흩어진 Signal과 Exposure를 Serial·Lot·Event 단위로 연결하고, 영향범위·통제·CAPA·복구를 사람의 안전판정 아래 더 빠르고 재현 가능하게 만드는 것**이 과제다.

---
