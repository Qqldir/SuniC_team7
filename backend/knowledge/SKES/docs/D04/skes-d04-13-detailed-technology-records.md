---
id: skes-d04-13-detailed-technology-records
title: Detailed Technology Records
summary: "SK이노베이션 E&S의 LNG 최적화, BOG 예측, 발전소 디스패치, 파이프라인 위험도, PPA 정산 등 5개 핵심 기술의 입출력, 메트릭, 적용 방식을 정의하는 기술 명세서."
tags: [d04, technology, schema, "xref:d03"]
keywords: [LNG 터미널, ETA 예측, BOG 관리, 파이프라인 RBMS, 발전소 디스패치, 위험도 평가, PPA 정산, 기술 명세]
related: [TECH-ENS-LNG-ETA, TECH-ENS-LNG-BOG-HYBRID, TECH-ENS-PWR-HEALTH-DISPATCH, TECH-ENS-CG-DYNAMIC-RBMS, TECH-ENS-PPA-LINEAGE, TECH-ENS-LH2-PLANT-ADVISORY, TECH-ENS-H2-SUPPLY-TWIN, TECH-ENS-KCE-MARKET-AI, TECH-ENS-EVERCHARGE-SMARTPOWER, TECH-ENS-CCS-MRV-LINEAGE]
priority: normal
domain: D04
section: 13
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 1597
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 13. Detailed Technology Records

### 13.1 `TECH-ENS-LNG-ETA` — LNG ETA and Berth Optimization

```yaml
technology_id: TECH-ENS-LNG-ETA
linked_apps: [APP-ENS-002]
linked_seeds: [SEED-ENS-D03-001, SEED-ENS-D03-023]
layer: model_analytics_and_optimization
inputs:
  - AIS_position_speed_heading
  - marine_weather_current
  - berth_and_unloading_schedule
  - terminal_tank_and_sendout
outputs:
  - probabilistic_ETA
  - conflict_and_inventory_risk
  - berth_speed_or_schedule_recommendation
technical_metrics:
  - ETA_MAE
  - calibration
  - schedule_feasibility
business_metrics:
  - vessel_waiting_hours
  - rescheduling_count
  - inventory_violation
deployment: advisory_first
```

### 13.2 `TECH-ENS-LNG-BOG-HYBRID` — Hybrid BOG Model

```yaml
technology_id: TECH-ENS-LNG-BOG-HYBRID
linked_apps: [APP-ENS-003]
linked_seeds: [SEED-ENS-D03-002, SEED-ENS-D03-024]
method:
  - mass_energy_balance
  - machine_learning_residual
  - constraint_aware_optimization
inputs:
  - tank_thermal_pressure_level
  - LNG_composition_and_unloading
  - ambient_and_sendout
  - compressor_and_reliquefaction_state
outputs:
  - BOG_forecast
  - cause_attribution
  - operating_recommendation
gate:
  - no_direct_SIS_override
  - operator_approval
  - sensor_calibration
```

### 13.3 `TECH-ENS-PWR-HEALTH-DISPATCH` — Health-aware Dispatch

```yaml
technology_id: TECH-ENS-PWR-HEALTH-DISPATCH
linked_apps: [APP-ENS-004]
linked_seeds: [SEED-ENS-D03-003, SEED-ENS-D03-026, SEED-ENS-D03-027]
components:
  - price_and_demand_forecast
  - heat_rate_baseline
  - start_stop_degradation_cost
  - asset_failure_risk
  - constrained_dispatch_optimizer
business_metric:
  - net_margin_after_expected_degradation_and_outage
gate:
  - LTSA_and_OEM
  - operator_override
  - change_management
```

### 13.4 `TECH-ENS-CG-DYNAMIC-RBMS` — Dynamic Pipeline RBMS

```yaml
technology_id: TECH-ENS-CG-DYNAMIC-RBMS
linked_apps: [APP-ENS-007, APP-ENS-008]
linked_seeds: [SEED-ENS-D03-005, SEED-ENS-D03-030, SEED-ENS-D03-031]
features:
  static:
    - material_age_diameter_pressure
    - location_population_consequence
  dynamic:
    - excavation_permit
    - corrosion_and_CP
    - weather_flood_landslide
    - leak_alarm_complaint
  output:
    - segment_risk_with_reason
    - inspection_repair_priority
model_controls:
  - high_consequence_recall_first
  - missing_data_uncertainty
  - legal_inspection_floor
```

### 13.5 `TECH-ENS-PPA-LINEAGE` — PPA Settlement Data Lineage

```yaml
technology_id: TECH-ENS-PPA-LINEAGE
linked_apps: [APP-ENS-013, APP-ENS-014]
linked_seeds: [SEED-ENS-D03-010, SEED-ENS-D03-011, SEED-ENS-D03-036, SEED-ENS-D03-037]
data_objects:
  - customer_load_meter_version
  - renewable_generation_meter_version
  - contract_formula_and_amendment
  - market_grid_charge
  - certificate_allocation
functions:
  - validation_and_reconciliation
  - exception_workflow
  - invoice_and_evidence_generation
  - audit_trace
gate:
  - legal_approved_rules
  - accounting_control
  - immutable_versioning
```

### 13.6 `TECH-ENS-LH2-PLANT-ADVISORY` — LH2 Plant Advisory AI

```yaml
technology_id: TECH-ENS-LH2-PLANT-ADVISORY
linked_apps: [APP-ENS-015]
linked_seeds: [SEED-ENS-D03-012, SEED-ENS-D03-038, SEED-ENS-D03-039]
inputs:
  - feed_quality_flow
  - process_sensor_setpoint
  - power_and_ambient
  - rotating_equipment_condition
outputs:
  - energy_yield_baseline
  - anomaly_and_failure_risk
  - advisory_setpoint_or_maintenance
kpi:
  - kWh_per_kg
  - yield_offspec
  - lead_time_precision
gate:
  - cryogenic_process_safety
  - OEM_and_control_boundary
```

### 13.7 `TECH-ENS-H2-SUPPLY-TWIN` — Hydrogen Supply-chain Twin

```yaml
technology_id: TECH-ENS-H2-SUPPLY-TWIN
linked_apps: [APP-ENS-016]
linked_seeds: [SEED-ENS-D03-013, SEED-ENS-D03-014, SEED-ENS-D03-040]
nodes:
  - plant_production_and_storage
  - tank_lorry
  - station_storage_and_dispenser
events:
  - production_change
  - shipment_loading_delivery
  - demand_and_stockout
  - boiloff_and_equipment_outage
output:
  - production_inventory_delivery_plan
  - resilience_scenario
```

### 13.8 `TECH-ENS-KCE-MARKET-AI` — MarketCapture Capability

```yaml
technology_id: TECH-ENS-KCE-MARKET-AI
linked_apps: [APP-ENS-019]
linked_seeds: [SEED-ENS-D03-016, SEED-ENS-D03-043, SEED-ENS-D03-044]
capability_status: disclosed_owned_or_subsidiary
disclosed:
  - day_ahead_bidding
  - real_time_5_minute_optimization
  - autonomous_platform
  - performance_reporting
undisclosed:
  - model_architecture
  - revenue_uplift
  - API_and_IP_boundary
reuse_assessment:
  - target_market_rule_gap
  - data_feature_gap
  - battery_warranty_and_degradation
  - trader_control_and_explainability
```

### 13.9 `TECH-ENS-EVERCHARGE-SMARTPOWER` — SmartPower

```yaml
technology_id: TECH-ENS-EVERCHARGE-SMARTPOWER
linked_apps: [APP-ENS-023, APP-ENS-024]
linked_seeds: [SEED-ENS-D03-048, SEED-ENS-D03-049]
capability_status: disclosed_owned_or_subsidiary
functions:
  - dynamic_load_management
  - charging_pattern_analysis
  - vehicle_need_based_power_allocation
  - mesh_network_connectivity
value:
  - more_chargers_with_existing_electrical_capacity
  - avoid_or_defer_utility_upgrade
validation:
  - site_specific_capacity_ratio
  - charging_success_and_departure_target
  - cyber_and_payment_compliance
```

### 13.10 `TECH-ENS-CCS-MRV-LINEAGE` — CCS MRV Lineage

```yaml
technology_id: TECH-ENS-CCS-MRV-LINEAGE
linked_apps: [APP-ENS-025]
linked_seeds: [SEED-ENS-D03-021, SEED-ENS-D03-051, SEED-ENS-D03-052]
functions:
  - meter_and_lab_QA_QC
  - custody_transfer
  - mass_balance_reconciliation
  - storage_monitoring_and_anomaly
  - lifecycle_carbon_intensity
  - third_party_verification_package
gate:
  - cross_border_regulation
  - long_term_liability
  - methodology_and_boundary
  - anti_greenwashing_control
```
