---
id: skes-d03-part-3-application-customer-alternative-2
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Application Taxonomy
summary: "에너지·전력 도메인의 25개 AI/최적화 애플리케이션을 분류한 마스터 테이블로, 각 앱의 적용 장면과 사용자, 의사결정 영역을 정의한다."
tags: [d03, product, core-candidate, schema, table, "xref:d17"]
keywords: [마스터 테이블, LNG 화물, 재생에너지, 배터리 저장, 수소, 발전 최적화, 도시가스, 의사결정, 우선도, 에너지 도메인]
related: [APP-ENS-001, APP-ENS-002, APP-ENS-003, APP-ENS-004, APP-ENS-005, APP-ENS-006, APP-ENS-007, APP-ENS-008, APP-ENS-009, APP-ENS-010, APP-ENS-011, APP-ENS-012, APP-ENS-013, APP-ENS-014, APP-ENS-015, APP-ENS-016, APP-ENS-017, APP-ENS-018, APP-ENS-019, APP-ENS-020, APP-ENS-021, APP-ENS-022, APP-ENS-023, APP-ENS-024]
priority: critical
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 3774
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 22. Application Taxonomy

### 22.1 Application Master

| APP ID | 적용 장면 | 연결 PS | 핵심 사용자 | 대표 의사결정 | D17 우선도 |
|---|---|---|---|---|---|
| `APP-ENS-001` | LNG cargo portfolio planning | LNG-01/02/03 | 수급·트레이딩 | 도입·재판매·대체조달 | P0 |
| `APP-ENS-002` | LNG vessel–terminal scheduling | LNG-03/04 | 선박·터미널 관제 | ETA·berth·하역 | P0 |
| `APP-ENS-003` | LNG terminal inventory/BOG | LNG-04 | 터미널 운영 | 재고·BOG·send-out | P0 |
| `APP-ENS-004` | CCGT economic dispatch | PWR-01 | 발전운영·시장 | 출력·기동·정비 | P0 |
| `APP-ENS-005` | CHP electricity/heat co-optimization | PWR-02 | 열·발전운영 | 전기·열·축열 | P0 |
| `APP-ENS-006` | City gas demand forecasting | CG-01 | 수급·관제 | 권역별 송출·압력 | P0 |
| `APP-ENS-007` | Pipeline dynamic risk | CG-03 | 안전·정비 | 점검·보수 우선순위 | P0 |
| `APP-ENS-008` | Excavation/third-party damage prevention | CG-03 | 안전·현장 | 위험굴착 탐지·출동 | P0 |
| `APP-ENS-009` | Meter reading and billing | CG-02 | 고객·검침·청구 | 검침확정·오류처리 | P0 |
| `APP-ENS-010` | Customer move-in/out orchestration | CG-02 | 고객센터·기사 | 예약·배정·완료 | P0 |
| `APP-ENS-011` | Solar forecasting and loss analysis | REN-01 | 발전·O&M | 예측·세척·정비 | P0 |
| `APP-ENS-012` | Offshore wind weather-window O&M | REN-02/ES-06 | O&M·선박·인력 | 방문·수리·연기 | P0 |
| `APP-ENS-013` | Corporate direct PPA sales design | REN-03/04 | 영업·고객 | 자산매칭·가격제안 | P0 |
| `APP-ENS-014` | PPA settlement and evidence | REN-05 | 정산·고객 ESG | 대사·청구·증빙 | P0 |
| `APP-ENS-015` | Liquid hydrogen plant optimization | H2-01 | 생산·정비 | 생산·품질·정비 | P0 |
| `APP-ENS-016` | Hydrogen logistics and station replenishment | H2-02/03 | 물류·충전 | 배차·재고·출하 | P0 |
| `APP-ENS-017` | Industrial demand-management ESS | ES-01 | 공장·EMS 운영 | 충방전·peak reserve | P0 |
| `APP-ENS-018` | Renewable-coupled ESS | ES-02 | 재생발전·ESS | 예측오차·출력제한 | P0 |
| `APP-ENS-019` | Wholesale-market grid ESS bidding | ES-03 | KCE·트레이더 | day-ahead·5분 입찰 | P0 |
| `APP-ENS-020` | Distribution DER visibility/control | ES-04 | 배전·DER 운영 | 예측·제약·dispatch | P1 |
| `APP-ENS-021` | VPP resource aggregation | ES-05 | 중개·자원보유자 | 등록·입찰·정산 | P1 |
| `APP-ENS-022` | Renewable fleet O&M | ES-06 | O&M·자산주 | 이상·작업·예비품 | P0 |
| `APP-ENS-023` | Parking/fleet smart charging | ES-07 | 주차·fleet·운전자 | 전력배분·예약 | P0 |
| `APP-ENS-024` | Charging site BESS integration | ES-08 | 부지운영·전력관리 | ESS·충전·증설 | P0 |
| `APP-ENS-025` | CCS chain-of-custody MRV | CCS-01/02 | 탄소·공정·감사 | 배출·포집·저장 검증 | P1 |

### 22.2 Application Record Detail

#### `APP-ENS-001` — LNG cargo portfolio planning

```yaml
problem_statement: >
  장기계약·지분가스·spot·발전/도시가스 수요·선박/터미널 제약을 함께 고려해
  cargo의 도입·교환·재판매·대체조달 결정을 지원한다.
minimum_data:
  - anonymized_contract_flexibility
  - demand_scenarios
  - price_fx_freight
  - cargo_and_terminal_schedule
decision_user: human trader and supply planner
success_metrics:
  - avoided_emergency_purchase
  - inventory_violation
  - recommendation_adoption
  - explainability_and_audit_completion
non_goals:
  - autonomous_trade_execution
  - exposure_of_contract_terms_to_public_models
```

#### `APP-ENS-002` — LNG vessel–terminal scheduling

```yaml
problem_statement: >
  선박 ETA 변동과 berth·탱크·send-out 제약 때문에 발생하는 대기·재고·운전변경을 줄인다.
minimum_data:
  - AIS_and_weather
  - berth_and_unloading_rate
  - tank_inventory_and_quality
  - sendout_and_demand
baseline:
  - planner_manual_schedule
  - deterministic_eta
success_metrics:
  - waiting_hours
  - rescheduling_count
  - inventory_safety_violation
  - operator_override_reason
```

#### `APP-ENS-003` — LNG terminal inventory/BOG

```yaml
problem_statement: >
  탱크 열유입·하역·송출·조성·압력 조건을 이용해 BOG 발생과 처리부하를 예측하고
  안전제약 안에서 운전계획을 지원한다.
minimum_data:
  - tank_level_temperature_pressure
  - composition_and_unloading_event
  - bog_flow_compressor_state
  - sendout_and_ambient
success_metrics:
  - forecast_error
  - compressor_specific_energy
  - alarm_lead_time
  - avoided_flare_or_loss
```

#### `APP-ENS-004` — CCGT economic dispatch

```yaml
problem_statement: >
  시장가격·연료비·효율곡선·기동비·설비상태를 결합해 경제성과 신뢰도를 함께 높인다.
minimum_data:
  - market_and_fuel_price
  - heat_rate_curve
  - start_stop_and_ramp_cost
  - equipment_health_and_outage
success_metrics:
  - margin_after_fuel_and_start_cost
  - heat_rate_improvement
  - forced_outage
  - emissions_constraint_compliance
```

#### `APP-ENS-005` — CHP electricity/heat co-optimization

```yaml
problem_statement: >
  기온·열수요·전력가격·축열·발전제약을 고려해 전력과 열을 동시 최적화한다.
minimum_data:
  - hourly_heat_load_weather
  - power_price_and_generation_curve
  - thermal_storage_state
  - network_supply_return_temperature
success_metrics:
  - total_fuel_per_joint_output
  - heat_supply_violation
  - heat_loss
  - contribution_margin
```

#### `APP-ENS-006` — City gas demand forecasting

```yaml
problem_statement: >
  권역·고객군별 수요를 예측해 송출·압력·인력계획을 개선한다.
minimum_data:
  - historical_sendout
  - weather_and_calendar
  - customer_segment_and_major_industry_schedule
  - pressure_and_operating_event
success_metrics:
  - forecast_error_by_horizon
  - pressure_violation
  - imbalance_or_emergency_adjustment
fairness_privacy:
  - 개인고객 식별정보 없이 집계수요 우선
```

#### `APP-ENS-007` — Pipeline dynamic risk

```yaml
problem_statement: >
  정적 배관속성과 최신 굴착·기상·점검·누출 데이터를 결합해 점검·보수 우선순위를 갱신한다.
minimum_data:
  - geospatial_pipe_segment
  - material_age_pressure
  - inspection_corrosion_cp
  - excavation_weather_incident
success_metrics:
  - high_risk_detection_recall
  - inspection_yield
  - leak_and_near_miss
  - false_alarm_workload
safety_rule:
  - 모델이 법정점검을 축소하는 근거로 단독 사용되지 않음
```

#### `APP-ENS-008` — Excavation damage prevention

```yaml
problem_statement: >
  허가굴착·현장영상·배관 GIS를 비교해 무단 또는 근접 굴착 위험을 빠르게 식별한다.
minimum_data:
  - excavation_permit_polygon_and_time
  - pipe_buffer_zone
  - drone_or_vehicle_image
  - field_dispatch_result
success_metrics:
  - confirmed_risk_precision
  - detection_to_dispatch_time
  - prevented_damage_or_near_miss
```

#### `APP-ENS-009` — Meter reading and billing

```yaml
problem_statement: >
  계량기 이미지와 과거 사용량을 사용해 자가검침 값을 보조 판독하고 비정상·오입력을 분류한다.
minimum_data:
  - consented_meter_image
  - meter_type_and_digits
  - previous_reading_and_usage_range
  - human_correction_label
success_metrics:
  - exact_read_accuracy
  - auto_accept_rate_at_safe_threshold
  - billing_correction
  - privacy_incident
```

#### `APP-ENS-010` — Move-in/out orchestration

```yaml
problem_statement: >
  전출입 예약·주소·계량기·기사 위치·작업시간을 연결해 재방문과 고객대기를 줄인다.
minimum_data:
  - request_and_service_window
  - address_meter_mapping
  - technician_skill_location
  - historical_duration_no_show
success_metrics:
  - on_time_completion
  - first_visit_completion
  - travel_time
  - customer_waiting
```

#### `APP-ENS-011` — Solar forecasting and loss analysis

```yaml
problem_statement: >
  기상·발전·인버터·현장정보를 이용해 예상발전량과 실제발전량의 차이를 원인별로 분해한다.
minimum_data:
  - irradiance_weather
  - meter_inverter_scada
  - curtailment_and_outage
  - cleaning_soiling_inspection
success_metrics:
  - forecast_error
  - unexplained_loss
  - recovered_generation
  - maintenance_roi
```

#### `APP-ENS-012` — Offshore wind weather-window O&M

```yaml
problem_statement: >
  고장위험과 해상 접근가능 시간·선박·인력·부품을 결합해 정비시점을 최적화한다.
minimum_data:
  - turbine_condition_alarm
  - wave_wind_visibility_forecast
  - vessel_crew_parts
  - generation_price_and_failure_cost
success_metrics:
  - downtime
  - vessel_day
  - first_time_fix
  - safety_and_aborted_visit
```

#### `APP-ENS-013` — Corporate PPA sales design

```yaml
problem_statement: >
  고객부하·RE100 목표와 개발/운영 자산을 매칭해 가격·기간·위험 시나리오를 빠르게 비교한다.
minimum_data:
  - interval_customer_load
  - renewable_asset_profile_status
  - price_grid_and_certificate_cost
  - credit_and_contract_constraints
success_metrics:
  - proposal_cycle_time
  - scenario_accuracy
  - contract_conversion
  - post_contract_variance
```

#### `APP-ENS-014` — PPA settlement and evidence

```yaml
problem_statement: >
  계량·발전·사용·계약·시장·인증 데이터를 연결해 정산오류와 증빙작성 시간을 줄인다.
minimum_data:
  - meter_interval_and_version
  - contract_formula
  - market_and_grid_charge
  - certificate_and_allocation
success_metrics:
  - settlement_cycle_time
  - exception_rate
  - audit_rework
  - customer_dispute
```

#### `APP-ENS-015` — Liquid hydrogen plant optimization

```yaml
problem_statement: >
  원료수소 품질·생산계획·전력·설비상태를 결합해 안전한 생산량과 에너지 원단위를 개선한다.
minimum_data:
  - feed_flow_quality
  - process_sensor_and_control
  - power_consumption
  - equipment_condition_and_trip
success_metrics:
  - kWh_per_kg
  - yield_and_offspec
  - availability
  - safety_limit_violation
```

#### `APP-ENS-016` — Hydrogen logistics and replenishment

```yaml
problem_statement: >
  생산·탱크·탱크로리·충전소 수요와 재고를 함께 계획해 품절·BOG·배송비를 줄인다.
minimum_data:
  - production_and_plant_inventory
  - station_inventory_and_demand
  - vehicle_capacity_location
  - route_weather_and_service_window
success_metrics:
  - stockout
  - on_time_in_full
  - logistics_cost_per_kg
  - boiloff_loss
```

#### `APP-ENS-017` — Demand-management ESS

```yaml
problem_statement: >
  생산부하·요금·ESS 상태를 예측해 peak를 줄이되 열화·안전·생산제약을 준수한다.
minimum_data:
  - interval_load_and_production
  - tariff_and_demand_charge
  - battery_soc_soh_temperature
  - warranty_and_operating_limit
success_metrics:
  - net_saving_after_degradation
  - peak_reduction
  - availability
  - safety_event
```

#### `APP-ENS-018` — Renewable-coupled ESS

```yaml
problem_statement: >
  발전예측·출력제한·PPA/시장가치를 반영해 ESS 충방전을 결정한다.
minimum_data:
  - renewable_forecast_actual
  - curtailment_and_grid_limit
  - market_or_ppa_settlement
  - battery_state_degradation
success_metrics:
  - recovered_energy
  - settlement_improvement
  - net_revenue_after_degradation
```

#### `APP-ENS-019` — Wholesale-market grid ESS bidding

```yaml
problem_statement: >
  시장가격·규칙·배터리 제약을 반영해 day-ahead와 실시간 입찰·dispatch를 자동화 또는 지원한다.
minimum_data:
  - market_prices_and_rules
  - battery_bidirectional_limit
  - availability_and_outage
  - degradation_cost
success_metrics:
  - realized_revenue
  - benchmark_regret
  - rule_violation
  - human_override_and_explanation
owned_capability:
  - KCE MarketCapture is a disclosed internal/subsidiary capability
```

#### `APP-ENS-020` — Distribution DER visibility/control

```yaml
problem_statement: >
  분산자원과 배전망 상태를 표준화해 가시화하고 전압·혼잡 제약 안에서 제어 가능성을 검증한다.
minimum_data:
  - network_topology_limit
  - smart_meter_scada
  - inverter_ess_ev_interface
  - weather_forecast
success_metrics:
  - telemetry_coverage_quality
  - constraint_prediction
  - dispatch_success
  - cyber_security_compliance
```

#### `APP-ENS-021` — VPP resource aggregation
