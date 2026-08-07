---
id: skes-d05-7-r-d-program-master
title: R&D Program Master
summary: "SK이노베이션 E&S의 CCS, CCUS, 도시가스 분야 R&D 프로젝트들을 프로그램 ID, 진행 상태, 참여자, 목표, 지적재산 현황으로 정리한 마스터 레지스트리."
tags: [d05, rnd, schema]
keywords: [CCS, CCUS, CO2포집, R&D프로젝트, 기술개발, 지적재산권, 특허, 도시가스, 프로그램관리, 연구개발]
related: [RDP-ENS-CCS-001, RDP-ENS-CCS-002, RDP-ENS-CCS-003, RDP-ENS-CCS-004, RDP-ENS-CG-001, RDP-ENS-CG-002, RDP-ENS-CG-003, RDP-ENS-ESS-001, RDP-ENS-ESS-002, RDP-ENS-EVC-001, RDP-ENS-EVC-002, RDP-ENS-H2-001, RDP-ENS-H2-002, RDP-ENS-LNG-001, RDP-ENS-PWR-001, RDP-ENS-REN-001]
priority: normal
domain: D05
section: 7
source: SK이노베이션E&S_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2336
updated: 2026-08-06
---

> SK이노베이션 E&S · D05 R&D·특허·지식재산

# 7. R&D Program Master

## 7.1 CCS·CCUS

### `RDP-ENS-CCS-001` — KIER·CE TECH CO₂ 포집 고도화

```yaml
program_id: RDP-ENS-CCS-001
status: PUBLIC_COLLABORATIVE_RND
start_evidence: 2021-06-16
participants:
  - SK_E&S
  - Korea_Institute_of_Energy_Research
  - CE_TECH
objective:
  - optimize_capture_for_large_scale_hydrogen
  - optimize_capture_for_LNG_power
  - demonstrate_and_commercialize_wet_capture
output_candidates:
  - process_design
  - solvent_and_operating_window
  - pilot_data
  - joint_or_separate_patents
ip_questions:
  - background_solvent_IP
  - process_improvement_ownership
  - field_of_use_and_region
  - scaleup_data_and_licensing
source_ids: [SRC-ENS-D05-0002, SRC-ENS-D05-0013, SRC-ENS-D05-0014]
```

### `RDP-ENS-CCS-002` — Honeywell ASCC 발전 배가스 실증

```yaml
program_id: RDP-ENS-CCS-002
status: PARTNER_TECH_DEMONSTRATION
participants: [SK_E&S, Honeywell_UOP]
technology: Advanced_Solvent_Carbon_Capture
target: natural_gas_power_plant_flue_gas
public_claim: greater_than_95_percent_capture_by_partner
ownership:
  core_technology: Honeywell
  site_data: contract_required
  integration_improvement: contract_required
  commercialization_rights: contract_required
gates:
  - guarantee_boundary
  - solvent_supply_and_license
  - energy_penalty
  - degradation_and_emission
  - derivative_and_improvement_IP
source_ids: [SRC-ENS-D05-0004]
```

### `RDP-ENS-CCS-003` — Barossa–Bayu-Undan CCS 공동연구

```yaml
program_id: RDP-ENS-CCS-003
status: PROJECT_FEASIBILITY_AND_DEVELOPMENT
participants: [SK_E&S, Santos, project_partners]
scope:
  - gas_field_CO2_management
  - cross_asset_transport_and_storage
  - depleted_field_storage
  - low_carbon_LNG_and_blue_hydrogen_link
ip_focus:
  - subsurface_models
  - monitoring_and_MRV_data
  - project_design_and_operating_knowhow
  - cross_border_data_and_liability
source_ids: [SRC-ENS-D05-0003]
```

### `RDP-ENS-CCS-004` — 흡수제 저장·고체화 방지

```yaml
program_id: RDP-ENS-CCS-004
status: PATENTED_ENGINEERING_SOLUTION
owned_direct_patent_families:
  - PF-ENS-CCS-001
  - PF-ENS-CCS-002
problem:
  - amine_solvent_solidification_in_storage
solutions:
  - use_process_waste_heat
  - use_captured_CO2_to_reduce_free_amine
potential_KPI:
  - heater_energy
  - solvent_availability
  - downtime_and_clogging
  - freeze_or_solidification_event
```

## 7.2 도시가스

### `RDP-ENS-CG-001` — 정압기 압력조절·시험기술

```yaml
program_id: RDP-ENS-CG-001
status: PATENT_EVIDENCED
participants:
  - SK_E&S
  - Busan_City_Gas
  - Chungcheong_Energy_Service
problems:
  - pressure_setpoint_accuracy
  - regulator_testing
  - safe_maintenance
linked_families:
  - PF-ENS-CG-001
  - PF-ENS-CG-005
linked_tech:
  - TECH-ENS-CG-01
  - TECH-ENS-CG-04
```

### `RDP-ENS-CG-002` — 계량·온압보정·열량변화 대응

```yaml
program_id: RDP-ENS-CG-002
status: PATENT_EVIDENCED
problems:
  - portable_volume_corrector_test
  - remote_metering
  - temperature_pressure_correction
  - calorific_value_change
  - customer_usage_and_billing_data
linked_families:
  - PF-ENS-CG-002
  - PF-ENS-CG-003
  - PF-ENS-CG-004
OI_extension:
  - AMI_data_quality
  - anomaly_detection
  - device_identity_and_security
  - calibration_lineage
```

### `RDP-ENS-CG-003` — 배관 응급보수·작업자 안전

```yaml
program_id: RDP-ENS-CG-003
status: AFFILIATE_PATENT_EVIDENCED
owner: Busan_City_Gas
problem:
  - repair_damaged_gas_pipeline_without_direct_exposure
  - prevent_secondary_accident
linked_family: PF-ENS-CG-006
OI_extension:
  - robotic_repair
  - digital_work_instruction
  - gas_isolation_verification
  - incident_evidence_capture
```

## 7.3 ESS·시장·분산자원

### `RDP-ENS-ESS-001` — KCE MarketCapture

```yaml
program_id: RDP-ENS-ESS-001
status: OPERATING_PROPRIETARY_SOFTWARE
owner: Key_Capture_Energy
development_evidence:
  technology_team_focus_years: 2
  release_date: 2022-12-13
functions:
  - autonomous_energy_trading
  - day_ahead_and_real_time_optimization
  - standalone_storage_revenue_optimization
  - ERCOT_operation_and_third_party_use
ip_form_hypothesis:
  primary: software_copyright_trade_secret_data_model
  patent: not_confirmed_in_initial_public_search
rights_questions:
  - source_code_owner
  - market_data_license
  - model_training_and_backtest_data
  - Korean_market_reuse_right
  - affiliate_internal_license
  - trader_override_and_liability
source_ids: [SRC-ENS-D05-0009]
```

### `RDP-ENS-ESS-002` — KCE WattBot·운영지식

```yaml
program_id: RDP-ENS-ESS-002
status: PUBLICLY_NAMED_CAPABILITY_REQUIRES_INTERNAL_DETAIL
owner: Key_Capture_Energy
scope_hypothesis:
  - market_or_asset_analytics
  - interaction_with_MarketCapture
evidence_rule:
  - no_architecture_or_performance_claim_without_internal_document
OI_extension:
  - explainable_bid_recommendation
  - degradation_aware_dispatch
  - multi_market_portfolio_risk
```

## 7.4 EV 충전

### `RDP-ENS-EVC-001` — SmartPower 동적 부하관리

```yaml
program_id: RDP-ENS-EVC-001
status: OPERATING_PATENTED_AFFILIATE_TECH
owner: EverCharge
core_functions:
  - real_time_building_load_awareness
  - dynamic_EVSE_power_allocation
  - multi_circuit_management
  - charger_mesh_communication
value:
  - increase_charger_count_with_existing_capacity
  - defer_electrical_upgrade
linked_families:
  - PF-ENS-EVC-001
  - PF-ENS-EVC-002
linked_tech: TECH-ENS-EVERCHARGE-SMARTPOWER
source_ids: [SRC-ENS-D05-0011, SRC-ENS-D05-0012, SRC-ENS-D05-0021, SRC-ENS-D05-0022]
```

### `RDP-ENS-EVC-002` — EVSE 보호·다중전압·과금

```yaml
program_id: RDP-ENS-EVC-002
status: PATENTED_AFFILIATE_TECH
owner: EverCharge
functions:
  - charging_and_automated_billing
  - mixed_level_EVSE
  - internal_current_overage_protection
linked_families:
  - PF-ENS-EVC-003
  - PF-ENS-EVC-004
  - PF-ENS-EVC-005
OI_extension:
  - fleet_priority_and_departure_SLA
  - charger_BESS_joint_dispatch
  - cybersecure_offline_operation
  - predictive_maintenance
```

## 7.5 수소

### `RDP-ENS-H2-001` — SK Plug HyVerse PEM 현지화·실증

```yaml
program_id: RDP-ENS-H2-001
status: JV_TECH_TRANSFER_LOCALIZATION_AND_DEMONSTRATION
participants: [SK_E&S, Plug_Power, SK_Plug_HyVerse]
scope:
  - PEM_electrolyzer
  - fuel_cell_system
  - hydrogen_refueling
  - local_manufacturing_and_research_base
ownership_rule:
  - Plug_core_technology_is_not_E&S_owned_by_default
  - JV_product_and_improvement_rights_require_contract
  - certification_does_not_equal_patent_ownership
source_ids: [SRC-ENS-D05-0005, SRC-ENS-D05-0006, SRC-ENS-D05-0027]
```

### `RDP-ENS-H2-002` — 액화수소드론 생태계 R&D

```yaml
program_id: RDP-ENS-H2-002
status: STARTUP_RND_SUPPORT_AND_EARLY_COMMERCIALIZATION
participants:
  - SK_E&S
  - seven_publicly_referenced_drone_companies
support:
  - R&D_funding
  - exhibition_and_ecosystem
  - commercialization_cooperation
ip_focus:
  - cryogenic_tank_and_supply
  - drone_fuel_system
  - flight_data
  - safety_certification
  - foreground_IP_and_market_rights
source_ids: [SRC-ENS-D05-0007]
```

## 7.6 LNG·발전·재생에너지

### `RDP-ENS-LNG-001` — LNG 밸류체인 통합운영 연구후보

```yaml
program_id: RDP-ENS-LNG-001
status: OI_RESEARCH_CANDIDATE_NOT_PUBLICLY_CONFIRMED_AS_FORMAL_PROGRAM
scope:
  - vessel_terminal_inventory_schedule
  - BOG_prediction_and_recovery
  - sendout_and_power_dispatch
  - methane_LDAR
ip_priority:
  - optimizer_and_event_graph
  - data_interface_and_operating_constraints
  - trade_secret_for_commercial_terms
```

### `RDP-ENS-PWR-001` — 가스발전 성능·포집 통합

```yaml
program_id: RDP-ENS-PWR-001
status: OI_EXTENSION_FROM_CAPTURE_DEMO
scope:
  - gas_turbine_and_HRSG_performance
  - capture_energy_penalty
  - steam_heat_and_capture_integration
  - flexible_operation_with_renewables
rights:
  - OEM_background_IP
  - Honeywell_capture_IP
  - E&S_site_data
  - integration_improvement_IP
```

### `RDP-ENS-REN-001` — 발전예측·PPA 정산 연구후보

```yaml
program_id: RDP-ENS-REN-001
status: OPERATING_CAPABILITY_WITH_IP_DETAILS_UNDISCLOSED
scope:
  - renewable_forecast
  - customer_load_simulation
  - PPA_settlement_and_exception
  - certificate_lineage
protection:
  - software_and_database_right
  - commercial_logic_trade_secret
  - customer_data_contract
```

---
