---
id: skes-d06-6-lng-upstream-liquefaction-cargo-operatio
title: LNG Upstream·Liquefaction·Cargo Operations
summary: "LNG 포트폴리오 수요 계획, 상류 생산 nomination, 가스 정제의 운영 프로세스를 정의하며, 공급 계약 권리와 액화 터미널을 맞추는 방법을 설명한다."
tags: [d06, process, schema]
keywords: [LNG, 포트폴리오계획, nomination, 액화슬롯, 계약권리, 터미널운영, 생산예측, Barossa, take-or-pay, 가스정제]
related: [PROC-ENS-D06-LNG-001, PROC-ENS-D06-LNG-002, PROC-ENS-D06-LNG-003, PROC-ENS-D06-LNG-004, PROC-ENS-D06-LNG-005, PROC-ENS-D06-LNG-006, PROC-ENS-D06-LNG-007]
priority: normal
domain: D06
section: 6
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 2019
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 6. LNG Upstream·Liquefaction·Cargo Operations

## 6.1 `PROC-ENS-D06-LNG-001` — Portfolio Demand and Entitlement Planning

```yaml
process_id: PROC-ENS-D06-LNG-001
objective: 발전 도시가스 판매 수요와 계약 LNG 권리를 기간별로 정합화
inputs:
  - power and heat demand scenarios
  - city_gas demand forecast
  - contract entitlement and destination flexibility
  - liquefaction slot and terminal capacity
  - vessel availability and voyage duration
  - opening inventory and minimum stock policy
outputs:
  - annual monthly cargo plan
  - source allocation and diversion decision
  - terminal tank target trajectory
  - fuel supply risk scenario
control_variables:
  - cargo timing volume quality and source
  - storage buffer
  - spot purchase or sale
  - plant fuel switching or dispatch coordination
KPIs:
  - supply_shortfall_risk
  - terminal_stockout_or_overfill_risk
  - portfolio_landed_cost
  - cargo_reschedule_count
  - take_or_pay_and_use_or_pay_exposure
failure_modes:
  - forecast error
  - correlated plant and cargo disruption
  - incompatible quality or terminal window
  - fragmented contract physical data
internal_data_required:
  - contract abstraction
  - cargo and terminal slot book
  - demand forecast versions
  - scenario approval log
OI_seeds: [SEED-ENS-D06-001, SEED-ENS-D06-002]
evidence_level: E1_DIRECT_OFFICIAL_PLUS_E4_MODEL
```

핵심은 최저가 LNG를 단순 선택하는 것이 아니라 공급권리·액화슬롯·선박·터미널 탱크·발전기의 기동계획을 함께 만족시키는 것이다. E&S의 Barossa, Woodford/Freeport, Tangguh 등은 권리형태와 운영주체가 다르므로 하나의 재고처럼 합산하기 전에 계약별 nomination·title·destination·품질 조건을 분리해야 한다.

## 6.2 `PROC-ENS-D06-LNG-002` — Upstream Production and Nomination Interface

```yaml
process_id: PROC-ENS-D06-LNG-002
public_confirmation:
  - Barossa gas field participation with Santos
  - Woodford joint development
  - Tangguh LNG introduction
process_boundary: E&S commercial_and_JV_interface_not_assumed_field_operator
inputs:
  - well and facility availability notice
  - forecast production and gas composition
  - entitlement and nomination window
  - planned maintenance and force_majeure notice
outputs:
  - confirmed feed_gas nomination
  - entitlement production record
  - variance and shortfall notice
  - liquefaction feed outlook
critical_data:
  - gross production vs equity entitlement
  - forecast vs actual
  - water CO2 H2S N2 heavy_hydrocarbon composition
  - pressure and delivery point
  - downtime reason and recovery estimate
failure_modes:
  - well decline or facility trip
  - feed off_spec
  - pipeline constraint
  - allocation disagreement
OI_seeds: [SEED-ENS-D06-003]
```

## 6.3 `PROC-ENS-D06-LNG-003` — Feed-Gas Conditioning

이 프로세스는 LNG 산업 baseline이며 E&S가 직접 운전하는 설비구성을 뜻하지 않는다.

```yaml
generic_sequence:
  - inlet separation
  - acid gas removal
  - dehydration
  - mercury removal
  - heavy hydrocarbon and NGL control
  - treated gas quality verification
critical_variables:
  - CO2 H2S water mercury nitrogen and hydrocarbon dewpoint
  - absorber differential pressure
  - solvent condition
  - molecular_sieve bed temperature profile
  - breakthrough indicators
failure_modes:
  - contaminant breakthrough
  - hydrate or freeze risk
  - corrosion
  - adsorbent degradation
  - analyzer drift
downstream_impact:
  - liquefaction exchanger restriction
  - off_spec LNG
  - train trip and cargo delay
internal_validation: operator_and_actual_process_configuration
```

## 6.4 `PROC-ENS-D06-LNG-004` — Gas Liquefaction Entitlement Operation

```yaml
process_id: PROC-ENS-D06-LNG-004
E&S_role:
  Darwin: equity_or_project_participation_interface
  Freeport: liquefaction_use_agreement_interface
physical_baseline:
  - treated gas precooling
  - staged refrigeration and liquefaction
  - end_flash and LNG rundown
  - refrigerant compression and heat rejection
critical_data:
  - feed gas flow and composition
  - train availability and run rate
  - compressor power and suction discharge state
  - refrigerant inventory and composition
  - exchanger temperature approach and pressure drop
  - LNG production rate and quality
commercial_data:
  - nominated feed vs accepted feed
  - scheduled vs produced LNG
  - fuel gas and retainage
  - outage allocation and make_up rights
failure_modes:
  - compressor trip or surge
  - exchanger restriction
  - refrigerant imbalance
  - utility or cooling limitation
  - feed quality excursion
KPIs:
  - entitlement_realization
  - train_availability
  - specific_energy_industry_field
  - production_variance
  - unplanned_outage_hours
OI_seeds: [SEED-ENS-D06-004, SEED-ENS-D06-005]
```

## 6.5 `PROC-ENS-D06-LNG-005` — Export Storage and Loading

```yaml
inputs: [LNG_rundown, tank_capacity, carrier_arrival, loading_plan]
activities:
  - tank receipt and stratification monitoring
  - inventory quality reconciliation
  - loading line cooldown
  - custody transfer metering
  - ship shore communication and ESD test
  - loading and heel management
outputs: [loaded_cargo, quality_certificate, bill_of_lading, tank_balance]
critical_data:
  - tank level density temperature pressure
  - composition heating_value Wobbe_index
  - loading flow and totalized mass_or_energy
  - ship tank state and heel
  - ESD and loading_arm status
failure_modes:
  - berth delay
  - tank stratification rollover risk
  - loading arm or meter fault
  - quality mismatch
  - documentation discrepancy
OI_seeds: [SEED-ENS-D06-006]
```

## 6.6 `PROC-ENS-D06-LNG-006` — Cargo and Vessel Scheduling

```yaml
decision_horizons: [annual, monthly, week_ahead, day_of_operation]
inputs:
  - loading window and terminal slot
  - vessel position speed fuel and compatibility
  - weather port congestion canal and route constraints
  - destination tank space and sendout forecast
  - commercial diversion value
outputs:
  - voyage order and ETA
  - speed and boil_off strategy
  - berth nomination
  - diversion or swap decision
KPIs:
  - on_time_arrival
  - demurrage
  - voyage_fuel_and_BOG_use
  - terminal_waiting_time
  - schedule_change_stability
OI_seeds: [SEED-ENS-D06-007]
```

## 6.7 `PROC-ENS-D06-LNG-007` — LNG Carrier Voyage and Cargo Management

```yaml
public_confirmation: E&S secured dedicated LNG carriers and began private fleet transport in 2019
operating_record:
  - vessel_id and voyage_id
  - cargo_source destination and title
  - departure ETA arrival and route
  - cargo tank pressure temperature level
  - generated and consumed boil_off
  - propulsion and fuel mode
  - weather and navigation restriction
failure_modes:
  - propulsion or equipment fault
  - excessive BOR or cargo pressure
  - weather route delay
  - port incompatibility or berth unavailability
  - communication and documentation mismatch
OI_focus:
  - ETA uncertainty propagation to terminal inventory
  - cargo loss and propulsion optimization
  - vessel equipment condition prediction
OI_seeds: [SEED-ENS-D06-008]
```

---
