---
id: skes-d06-9-city-gas-operations
title: City-Gas Operations
summary: "도시가스 도매 수령, 가취화, 배분 관리, 무결성 평가 등 운영 프로세스별 절차, 임계 변수, 장애 모드, KPI를 정의하는 문서."
tags: [d06, process, schema]
keywords: [도매 수령, 거래 이전, 가취화, 압력 조절, 배분, 라인팩, RBMS, 무결성 평가]
related: [PROC-ENS-D06-CG-001, PROC-ENS-D06-CG-002, PROC-ENS-D06-CG-003, PROC-ENS-D06-CG-004, PROC-ENS-D06-CG-005, PROC-ENS-D06-CG-006, PROC-ENS-D06-CG-007, PROC-ENS-D06-CG-008]
priority: normal
domain: D06
section: 9
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 2156
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 9. City-Gas Operations

## 9.1 Operating Context

E&S는 공개 기준 7개 도시가스 자회사로 8개 권역에 공급하고, RBMS와 드론 안전점검을 공개했다. D06은 자회사별 상세 설비가 동일하다고 가정하지 않고 공통 프로세스 표준과 법인별 현장차이를 분리한다.

## 9.2 `PROC-ENS-D06-CG-001` — Wholesale Receipt and Custody Transfer

```yaml
inputs:
  - wholesale gas nomination
  - delivery pressure and quality
  - customer demand forecast
activities:
  - city_gate receipt
  - custody flow and quality measurement
  - daily allocation and imbalance reconciliation
outputs:
  - accepted gas volume and energy
  - network injection schedule
  - custody and billing record
critical_data:
  - flow pressure temperature compressibility
  - heating_value and composition
  - meter factor calibration and quality flag
  - nomination actual and imbalance
failure_modes:
  - meter bias
  - pressure or quality deviation
  - forecast imbalance
  - timestamp and standard_condition mismatch
OI_seeds: [SEED-ENS-D06-030]
```

## 9.3 `PROC-ENS-D06-CG-002` — Odorization and Pressure Regulation

```yaml
sequence:
  - inlet filtering and isolation
  - pressure reduction and control
  - overpressure protection
  - gas heating if required by design
  - odorant injection and verification
  - outlet monitoring
critical_variables:
  - inlet outlet and differential pressure
  - flow and regulator position
  - gas temperature
  - odorant injection rate and inventory
  - slam_shut relief and bypass status
failure_modes:
  - regulator hunting or lockup
  - underpressure or overpressure
  - filter restriction
  - hydrate or freezing
  - under_or_over odorization
  - unauthorized bypass state
OI_seeds: [SEED-ENS-D06-031, SEED-ENS-D06-032]
```

## 9.4 `PROC-ENS-D06-CG-003` — Distribution Pressure and Linepack

```yaml
inputs: [gate_supply, hourly_demand, weather, network_topology, regulator_status]
decisions:
  - pressure_zone target
  - regulator and valve operation
  - supply source allocation
  - contingency isolation plan
state_variables:
  - pressure at critical nodes
  - estimated flow and linepack
  - customer demand by segment
  - valve and regulator state
failure_modes:
  - low pressure during peak
  - high pressure after demand drop
  - telemetry blind spot
  - topology model not synchronized with field
  - local restriction or leak
KPIs:
  - pressure_compliance
  - forecast_error
  - unserved_or_low_pressure_events
  - regulator_movement_and_stability
  - model_measurement_residual
OI_seeds: [SEED-ENS-D06-033]
```

## 9.5 `PROC-ENS-D06-CG-004` — RBMS Integrity Risk Assessment

```yaml
public_confirmation: E&S introduced Risk Based Management System for city gas pipes
risk_unit: pipe_segment_or_asset_cluster
risk_inputs:
  - material diameter age and joint type
  - coating cathodic_protection and corrosion history
  - pressure class and operating history
  - leak failure repair and inspection history
  - soil groundwater road and seismic attributes
  - excavation density and third_party exposure
  - population consequence and critical customer
  - data completeness and uncertainty
outputs:
  - likelihood_score
  - consequence_score
  - composite_risk_rank
  - inspection rehabilitation replacement plan
model_controls:
  - version and approved weights
  - explainable contribution
  - backtest against incidents
  - missing_data penalty
  - expert override reason
failure_modes:
  - stale GIS or asset attributes
  - inspection bias
  - low frequency event underlearning
  - score not connected to work execution
  - legal or safety accountability ambiguity
OI_seeds: [SEED-ENS-D06-034, SEED-ENS-D06-035]
```

## 9.6 `PROC-ENS-D06-CG-005` — Patrol·Drone·Leak Survey

```yaml
public_confirmation: drone safety inspections are used in city gas operations
inspection_modes:
  - walking_or_vehicle patrol
  - fixed_or_mobile gas detector
  - drone visual_or_sensor inspection where applicable
  - pressure trend and customer report
  - valve regulator and exposed crossing inspection
record_fields:
  - route geometry and coverage
  - timestamp operator weather and sensor
  - observation image video and gas concentration
  - location confidence
  - anomaly classification severity and confidence
  - follow_up work order and closure evidence
failure_modes:
  - uninspected gap
  - false positive or false negative
  - poor geolocation
  - imagery disconnected from asset ID
  - anomaly not converted to work order
KPIs:
  - planned_coverage_completion
  - anomaly_confirmation_rate
  - time_to_field_verification
  - leak_found_per_distance_risk_adjusted
  - closure_lead_time
OI_seeds: [SEED-ENS-D06-036, SEED-ENS-D06-037]
```

## 9.7 `PROC-ENS-D06-CG-006` — Excavation and Third-Party Damage Prevention

```yaml
inputs:
  - excavation request and permit
  - GIS pipe location and depth
  - contractor and work schedule
  - field marking and locate result
activities:
  - conflict detection
  - locate and mark
  - high_risk attendance
  - work monitoring
  - completion and asset update
failure_modes:
  - incomplete or inaccurate map
  - unreported excavation
  - permit schedule change
  - contractor noncompliance
  - field change not reflected in GIS
OI_seeds: [SEED-ENS-D06-038]
```

## 9.8 `PROC-ENS-D06-CG-007` — Regulator·Valve Maintenance

```yaml
maintenance_inputs:
  - operating hours and cycles
  - pressure deviation and hunting index
  - inspection and overhaul history
  - manufacturer recommendation
  - criticality and redundancy
as_found_data:
  - inlet outlet lockup pressure
  - setpoint and response
  - filter differential pressure
  - valve stroke and leakage
  - relief and slam_shut test
outputs:
  - adjusted setpoint
  - replaced components
  - test certificate
  - updated risk and next due date
OI_seeds: [SEED-ENS-D06-039]
```

## 9.9 `PROC-ENS-D06-CG-008` — Metering·Volume Correction·Billing

```yaml
inputs:
  - raw meter index or interval volume
  - temperature pressure and compressibility where applicable
  - gas heating_value
  - tariff customer class and billing period
  - move_in move_out and meter exchange events
outputs:
  - corrected volume and energy
  - bill and tax
  - exception and estimated reading
  - revenue and unaccounted_for_gas input
failure_modes:
  - communication failure
  - meter drift battery or tamper
  - incorrect correction factor
  - estimated reading persistence
  - meter event and customer master mismatch
  - tariff version error
KPIs:
  - actual_read_rate
  - billing_exception_rate
  - rebill_and_complaint_rate
  - meter_failure_rate
  - unaccounted_for_gas
OI_seeds: [SEED-ENS-D06-040, SEED-ENS-D06-041]
```

## 9.10 `PROC-ENS-D06-CG-009/010` — Customer Event and Emergency Response

```yaml
normal_customer_events:
  - new_service feasibility and construction
  - meter installation or exchange
  - move_in and safety check
  - move_out shutoff and final reading
  - payment delinquency and restoration
emergency_inputs:
  - odor or leak call
  - detector alarm
  - pressure anomaly
  - excavation strike or fire
emergency_sequence:
  - call triage and location confirmation
  - dispatch and hazard zone setup
  - gas measurement and source isolation
  - evacuation and authority coordination
  - repair pressure_test restoration
  - incident investigation and learning
critical_timestamps:
  - call_received
  - dispatch
  - arrival
  - isolation
  - safe_state
  - restoration
failure_modes:
  - wrong location or asset
  - alarm duplication not recognized
  - delayed isolation resource
  - customer communication gap
  - incident learning not propagated
OI_seeds: [SEED-ENS-D06-042, SEED-ENS-D06-043]
```

---
