---
id: skes-d06-13-liquid-hydrogen-operations
title: Liquid-Hydrogen Operations
summary: "부생수소 정제에서 액화, 극저온 저장, 탱커 배송까지 전체 공급체계의 운영기준과 관리지표를 정의한다."
tags: [d06, process, schema]
keywords: [부생수소, 수소액화, 정제기술, 극저온저장, 보일오프, 직교파라전환, 탱커배송, 냉동압축]
related: [PROC-ENS-D06-H2-001, PROC-ENS-D06-H2-002, PROC-ENS-D06-H2-003]
priority: normal
domain: D06
section: 13
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1318
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 13. Liquid-Hydrogen Operations

## 13.1 Evidence Boundary

E&S는 인천 SK인천석유화학 부지에서 발생하는 부생수소를 액화해 2024년부터 수도권을 포함한 전국에 공급한다고 공개했고, 플랜트 명목 연간 능력을 3만 톤으로 제시한다. 그러나 정제기술, 액화 사이클, 공급사, train 구성, 실제 가동률, specific energy, 순도, boil-off rate는 공개되지 않았다.

## 13.2 `PROC-ENS-D06-H2-001` — Byproduct Hydrogen Intake and Purification

```yaml
public_confirmation: byproduct_hydrogen_source_from_SK_Incheon_Petrochemical
operator_boundary: source_plant_to_IGE_plus_or_operating_entity_interface_requires_validation
inputs:
  - source hydrogen flow pressure temperature
  - composition and contaminant analysis
  - source unit operating state
activities_industry_baseline:
  - buffer and compression as required
  - contaminant removal and purification
  - product quality verification
  - feed balancing to liquefier
outputs:
  - purified hydrogen feed
  - offgas or purge
  - quality certificate and lot
critical_data:
  - H2 purity
  - moisture oxygen nitrogen hydrocarbons and specified contaminants
  - flow pressure temperature
  - purification bed or unit state
  - source interruption notice
failure_modes:
  - source variability
  - impurity breakthrough
  - analyzer drift
  - compressor trip
  - source and liquefier imbalance
KPIs:
  - feed_acceptance_rate
  - purification_recovery
  - off_spec_events
  - feed_availability
OI_seeds: [SEED-ENS-D06-061]
```

## 13.3 `PROC-ENS-D06-H2-002` — Liquefaction and Cryogenic Storage

```yaml
physical_baseline:
  - feed compression and precooling
  - staged cryogenic cooling
  - ortho_para conversion management
  - final liquefaction near minus_253_C
  - rundown to cryogenic storage
  - boil_off handling
critical_data:
  - temperature pressure flow and purity by stage
  - compressor expander and cold_box state
  - electrical power and cooling duty
  - storage tank P/T/level
  - generated recovered vented_or_consumed BOG
  - product mass and quality
failure_modes:
  - cold_box or compressor trip
  - impurity freeze or restriction
  - insufficient ortho_para conversion
  - tank pressure rise and boil_off
  - hydrogen detector or ventilation impairment
  - vacuum insulation degradation
KPIs:
  - liquid_hydrogen_output
  - specific_electricity_consumption
  - product_recovery
  - plant_availability
  - storage_BOR
  - safety_barrier_availability
OI_seeds: [SEED-ENS-D06-062, SEED-ENS-D06-063]
evidence_level: E1_EXISTENCE_PLUS_E3_PROCESS_BASELINE
```

## 13.4 `PROC-ENS-D06-H2-003` — Tanker Loading·Delivery·Station Receiving

```yaml
loading:
  - order and tanker compatibility
  - pre_cooling_and_connection
  - mass transfer and pressure control
  - quality and quantity certificate
  - safe disconnect and dispatch
transport:
  - route schedule driver and vehicle readiness
  - tank pressure temperature and location
  - delay and emergency management
station_receiving:
  - delivery acceptance
  - connection and transfer
  - station storage and boil_off management
  - inventory and settlement
loss_points:
  - line and hose cooldown
  - tanker heat ingress
  - waiting time
  - station transfer and storage
critical_data:
  - source_batch tanker_load station_delivery genealogy
  - gross loaded delivered and accepted mass
  - pressure temperature and vent record
  - turnaround and waiting
  - safety interlock gas detection and grounding
failure_modes:
  - incompatible connection or procedure
  - excessive pressure or boil_off
  - delayed delivery and inventory shortage
  - mass balance discrepancy
  - leak detector alarm or ESD
KPIs:
  - loading_and_delivery_turnaround
  - delivered_to_loaded_ratio
  - on_time_in_full
  - station_stockout
  - transfer_loss
OI_seeds: [SEED-ENS-D06-064, SEED-ENS-D06-065]
```

## 13.5 Hydrogen Safety Barrier Record

```yaml
barrier_record:
  detection:
    - hydrogen detector coverage and proof_test
    - flame detector where applicable
    - oxygen deficiency and ventilation status
  containment:
    - vacuum insulated vessel and piping
    - isolation valve and breakaway coupling
    - pressure relief routing
  ignition_control:
    - classified electrical equipment
    - grounding and bonding
    - permit and hot_work control
  response:
    - ESD cause_and_effect
    - ventilation and safe vent
    - exclusion zone and emergency coordination
data_requirements:
  - barrier_id status bypass impairment and restoration
  - detector calibration and alarm test
  - relief or vent event
  - emergency drill and response time
```

---
