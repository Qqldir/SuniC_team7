---
id: skon-d15-d15-14-machine-readable-summary
title: Machine-readable Summary
summary: "SK온의 엔터프라이즈 리스크·품질·안전을 정의한 YAML 명세로, 위험 분류체계와 폐쇄형 루프 운영 모델을 구조화한 문서."
tags: [d15, risk, schema, "xref:d16", "xref:d03", "xref:d04", "xref:d06"]
keywords: [D15, 리스크 분류체계, 품질 안전, CAPA, 폐루프, 회복탄력성, 의사결정 가드레일, 공개 신호, 리스크 분류, 폐쇄형 루프, 근본원인 분석, 필드 품질, 공급망 리스크, OT 사이버, SHE 관리, 회상 범위]
related: []
priority: normal
domain: D15
section: D15-14
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1478
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-14 Machine-readable Summary

```yaml
domain:
  id: D15
  name: Enterprise_Risk_Quality_Safety_and_Resilience
  version: v1.0
  as_of: 2026-08-03_KST
  previous_domain: D14_Policy_Regulation_Incentives_and_Compliance_v1.0

public_confirmed_signals:
  SKBA_F150_recall_23V168:
    status: HISTORICAL_PUBLIC_RECALL
    affected_vehicles: 18
    supplier: SK_Battery_America
    failure_mode: cell_manufacturing_deviation_internal_short_at_high_SOC_fire_risk
    positive_control_pattern: supplier_process_records_plus_pack_to_vehicle_traceability
    prohibition: do_not_generalize_to_enterprise_defect_rate
  SK_innovation_SHE:
    status: GROUP_LEVEL_PUBLIC_CONTROL_BASELINE
    disclosed: CSO_safety_committee_site_SHE_and_2022_emergency_drills
    warning: do_not_copy_group_or_2022_metrics_to_current_SK_On_sites
  information_security:
    status: GROUP_LEVEL_ISMS_PUBLIC_BASELINE
    disclosed: ISO_IEC_27001_27701_and_PDCA
    gap: plant_line_OT_coverage_not_publicly_verified

risk_taxonomy:
  total: 12
  categories:
    - product_quality_and_field_safety
    - manufacturing_quality_and_ramp
    - plant_SHE
    - supply_chain_and_origin
    - customer_demand_and_concentration
    - utilization_cost_cash
    - contract_JV_counterparty
    - policy_regulation_market_access
    - IT_OT_data_IP
    - climate_natural_hazard_utility
    - people_organization_safety_culture
    - reputation_stakeholder

operating_model:
  closed_loop:
    - signal
    - triage
    - affected_population
    - containment
    - investigation
    - root_cause_confidence
    - CAPA
    - effectiveness_validation
    - recovery
    - residual_risk_and_learning
  cause_confidence:
    - observed_association
    - plausible_mechanism
    - reproduced
    - verified_cause
  decision_guardrails:
    - no_autonomous_safety_bypass
    - no_autonomous_product_release
    - no_autonomous_recall_scope_or_notification
    - no_autonomous_root_cause_finalization

counts:
  public_signal_events: 8
  enterprise_risk_categories: 12
  priority_scenarios: 8
  pain_points: 14
  external_cases: 7
  OI_opportunities: 15
  priority_POCs: 5
  sources: 18

priority_OI:
  - OI-D15-02_Process_to_Field_Quality_Digital_Thread
  - OI-D15-03_Defect_Population_and_Recall_Scope_Engine
  - OI-D15-04_Early_Field_Failure_Signal_Fusion
  - OI-D15-10_OT_Cyber_Safety_Guardrail
  - OI-D15-08_Plant_SHE_Barrier_Health_Monitor

critical_internal_data:
  - material_roll_cell_module_pack_vehicle_or_ESS_genealogy
  - inspection_formation_BMS_DTC_telemetry_complaint_warranty_and_return
  - affected_population_inclusion_exclusion_and_denominator
  - incident_near_miss_barrier_impairment_and_emergency_drill
  - CAPA_change_effectiveness_recurrence_and_horizontal_deployment
  - OT_asset_access_patch_backup_restore_and_safety_independence
  - RTO_RPO_alternative_site_insurance_contract_and_regulatory_notifications

data_quality:
  strong:
    - official_SKBA_recall_event_and_population
    - industry_recall_and_battery_fire_failure_patterns
    - public_group_level_SHE_security_and_governance_baselines
    - standards_based_risk_SHE_OT_and_transport_framework
  weak_or_not_disclosed:
    - current_SK_On_enterprise_risk_register
    - plant_product_customer_specific_defect_and_warranty_rates
    - warranty_provision_recall_cost_insurance_limit_and_recovery
    - site_level_SHE_incident_near_miss_and_barrier_health
    - OT_asset_and_control_coverage
    - climate_physical_risk_and_BCP_test_results
  release_suitability:
    suitable_for:
      - risk_data_model_and_cross_domain_linkage
      - public_signal_based_pain_point_and_OI_generation
      - internal_data_request_and_POC_design
    not_suitable_for:
      - claiming_actual_SK_On_defect_accident_or_warranty_performance
      - regulatory_recall_safety_or_insurance_decisions
      - autonomous_operational_control

completion:
  domain_boundary: COMPLETE
  risk_data_model: COMPLETE
  public_signal_register: COMPLETE
  quality_warranty_closed_loop: COMPLETE
  plant_SHE: COMPLETE
  aggregation_and_scenarios: COMPLETE
  BCP_and_crisis: COMPLETE
  OT_cyber_safety: COMPLETE
  governance_and_KPI: COMPLETE
  pain_points: COMPLETE
  external_cases: COMPLETE
  OI_portfolio: COMPLETE
  D17_bridge: COMPLETE
  source_registry: COMPLETE
  final_quality_audit: COMPLETE

next_domain:
  id: D16
  name: External_Solutions_Startups_Vendors_and_Open_Innovation_Ecosystem
```

---

## D15 완료 전 검증 체크포인트

- [x] F-150 23V-168의 18대·SKBA·내부단락·화재위험·Pack 교체·추적성 범위를 NHTSA 원문과 일치시킴
- [x] 단일 공개사건을 SK온 전체 불량률·현재 품질수준으로 일반화하지 않음
- [x] 공개되지 않은 Warranty·Recall Cost·보험·사고율·OT Coverage를 `NOT_DISCLOSED`로 유지
- [x] D03·D04 제품기술, D06 공정, D07 공장, D08~D14 원장을 중복 생성하지 않고 Risk Event로 연결
- [x] 품질·SHE·Cyber·BCP에 사람 승인과 독립 Safety Barrier를 적용
- [x] Pain Point 14개·외부사례 7개·O/I 15개·우선 PoC 5개·출처 18개 구성

**다음 작업 지점:** `D16 External Solutions, Startups, Vendors & Open-Innovation Ecosystem`
