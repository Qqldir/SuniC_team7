---
id: skes-d06-7-lng-terminal-operations
title: LNG Terminal Operations
summary: "LNG 터미널의 선박 하역부터 저장·가스 처리까지 운영 전 단계의 절차, 점검 항목, 위험 요소를 정의한 프로세스 명세이다."
tags: [d06, process, schema]
keywords: [하역, 선박정박, 재고조정, 보일오프가스, BOG, 저온저장, 압축기, 재액화, ESD, 탱크]
related: [PROC-ENS-D06-LNG-008, PROC-ENS-D06-LNG-009, PROC-ENS-D06-LNG-010, PROC-ENS-D06-LNG-011]
priority: normal
domain: D06
section: 7
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1278
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 7. LNG Terminal Operations

## 7.1 `PROC-ENS-D06-LNG-008` — Berthing and Unloading

```yaml
public_confirmation: Boryeong terminal unloads stores regasifies and transmits imported LNG
pre_arrival:
  - ship terminal compatibility
  - berth window and weather
  - tank space and receiving plan
  - cargo documents and quality
  - tug pilot and marine coordination
ship_shore:
  - communication link
  - mooring status
  - loading arm connection
  - ESD link and emergency release test
unloading:
  - line cooldown
  - ramp up
  - steady transfer
  - tank allocation and pressure control
  - ramp down drain purge disconnect
critical_data:
  - arm movement and connection status
  - flow pressure temperature density
  - ship and shore tank levels
  - return gas flow
  - ESD permissive and trip sequence
KPIs:
  - berth_turnaround
  - unloading_rate_stability
  - transfer_difference
  - delay_by_reason
  - safety_interlock_test_success
failure_modes:
  - weather excursion
  - arm leak or excessive movement
  - ESD activation
  - receiving tank pressure rise
  - meter discrepancy
OI_seeds: [SEED-ENS-D06-009, SEED-ENS-D06-010]
```

## 7.2 `PROC-ENS-D06-LNG-009` — Storage and Inventory Reconciliation

```yaml
process_objective: 안전한 cryogenic storage와 상업·물리 재고의 일치
inventory_equation:
  closing_inventory: opening_inventory + receipts - sendout - fuel - measured_losses - adjustments
state_variables:
  - tank level and liquid volume
  - density composition and heating_value
  - liquid and vapor temperature profile
  - tank pressure
  - stratification indicator
  - heel and usable inventory
commercial_dimensions:
  - owner and title
  - contract source
  - receipt batch
  - allocation to power city_gas third_party
  - measurement uncertainty and adjustment approval
failure_modes:
  - level or density bias
  - unrecognized stratification
  - tank capacity conflict
  - inventory ownership mismatch
  - unexplained gain_or_loss
KPIs:
  - inventory_reconciliation_error
  - usable_days_of_supply
  - tank_capacity_utilization
  - quality_blend_compliance
  - adjustment_frequency
OI_seeds: [SEED-ENS-D06-011, SEED-ENS-D06-012]
```

## 7.3 `PROC-ENS-D06-LNG-010` — Boil-Off Gas Management

```yaml
evidence_note: BOG process is industry baseline; Boryeong actual equipment and routing require internal validation
BOG_sources:
  - steady tank heat ingress
  - ship unloading displacement and flash
  - pump and pipe heat ingress
  - pressure reduction and recirculation
  - tank cooldown or operational transient
possible_routes:
  - compressor to fuel gas
  - recondenser or reliquefaction
  - sendout blend
  - controlled flare_or_vent as last barrier subject to design
critical_data:
  - BOG flow composition pressure temperature
  - compressor status suction discharge and vibration
  - recondenser liquid flow and duty
  - tank pressure and sendout demand
  - flare_or_vent event and reason
failure_modes:
  - compressor trip
  - low sendout and high BOG coincidence
  - recondenser capacity limit
  - tank pressure escalation
  - sensor or mass_balance inconsistency
KPIs:
  - BOG_generated_per_throughput
  - BOG_recovered_ratio
  - compressor_availability
  - flare_or_vent_quantity
  - tank_pressure_excursion
OI_seeds: [SEED-ENS-D06-013, SEED-ENS-D06-014]
```

## 7.4 `PROC-ENS-D06-LNG-011` — Regasification and Sendout

```yaml
sequence:
  - LNG in_tank pump
  - high_pressure sendout pump
  - vaporizer heat exchange
  - gas heating or conditioning if required
  - quality and custody measurement
  - pipeline sendout
control_variables:
  - pump staging
  - vaporizer allocation and heat input
  - outlet pressure temperature and flow
  - gas quality and heating_value
  - sendout nomination and downstream pressure
failure_modes:
  - pump cavitation or trip
  - vaporizer fouling icing or heat_source constraint
  - low outlet temperature
  - quality excursion
  - pipeline pressure or demand constraint
KPIs:
  - sendout_availability
  - specific_regas_energy_or_heat
  - nomination_accuracy
  - pump_and_vaporizer_efficiency
  - unplanned_constraint_hours
OI_seeds: [SEED-ENS-D06-015]
```

## 7.5 Terminal Digital Thread

```yaml
cargo_to_consumption_trace:
  - cargo_id
  - unloading_event_id
  - receiving_tank_id
  - inventory_layer_or_batch_id
  - BOG_allocation_id
  - sendout_stream_id
  - custody_meter_record_id
  - consuming_plant_or_network_id
required_reconciliation:
  physical_mass: required
  energy_content: required
  commercial_title: required
  measurement_uncertainty: required
  timestamp_and_timezone: required
```

---
