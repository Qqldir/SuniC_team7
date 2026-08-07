---
id: skes-d06-17-failure-mode-and-deviation-register
title: Failure-Mode and Deviation Register
summary: "LNG 밸류체인의 액화, 운송, 재기화, 발전 등 공정별 주요 실패 모드, 선행지표, 결과, 제어조치를 정의한 위험 등록 표"
tags: [d06, process, schema, table]
keywords: [액화, 운송, 재기화, 위험 등록, BOG, 터미널, 선행지표, RBMS, HRSG, 제어 조치]
related: [FM-ENS-D06-001, FM-ENS-D06-002, FM-ENS-D06-003, FM-ENS-D06-004, FM-ENS-D06-005, FM-ENS-D06-006, FM-ENS-D06-007, FM-ENS-D06-008, FM-ENS-D06-009, FM-ENS-D06-010, FM-ENS-D06-011, FM-ENS-D06-012, FM-ENS-D06-013, FM-ENS-D06-014, FM-ENS-D06-015, FM-ENS-D06-016, FM-ENS-D06-017, FM-ENS-D06-018, FM-ENS-D06-019, FM-ENS-D06-020, FM-ENS-D06-021, FM-ENS-D06-022, FM-ENS-D06-023, FM-ENS-D06-024]
priority: normal
domain: D06
section: 17
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1693
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 17. Failure-Mode and Deviation Register

## 17.1 Critical Failure Modes

| Failure ID | Process | Deviation | Leading indicators | Consequence | Existing/required barriers | O/I |
|---|---|---|---|---|---|---|
| `FM-ENS-D06-001` | LNG portfolio | cargo/terminal/plant schedule mismatch | ETA drift, tank trajectory conflict | stockout, demurrage, lost dispatch | integrated planning, scenario approval | Yes |
| `FM-ENS-D06-002` | liquefaction | train performance degradation | power rise, temperature approach, vibration | reduced entitlement, delay | operator/OEM controls | Yes-interface |
| `FM-ENS-D06-003` | carrier | excessive cargo pressure/BOG | tank P rise, BOR deviation | loss, delay, safety response | cargo control, voyage procedure | Yes |
| `FM-ENS-D06-004` | unloading | ESD or arm abnormality | movement, leak, comm fault | transfer stop, marine risk | ESD, emergency release, exclusion | Limited |
| `FM-ENS-D06-005` | terminal tank | stratification/rollover precursor | density/temp layers, pressure trend | rapid vapor generation | monitoring, inventory control | Yes |
| `FM-ENS-D06-006` | BOG | compressor/recovery unavailable | suction P, vibration, trip | tank pressure, loss | redundancy, safe routing | Yes |
| `FM-ENS-D06-007` | regas | sendout constraint | pump/vaporizer performance | downstream fuel shortage | equipment staging, inventory | Yes |
| `FM-ENS-D06-008` | power startup | failed/delayed start | permissive, alarm sequence | dispatch loss, fuel/emission | procedure, automation, operator | Yes |
| `FM-ENS-D06-009` | gas turbine | combustion instability/degradation | dynamics, T spread, heat rate | trip, emission, efficiency | OEM limits, inspection | Yes |
| `FM-ENS-D06-010` | HRSG | tube leak/thermal fatigue | chemistry, make-up, acoustic/temp | outage, safety | inspection, chemistry control | Yes |
| `FM-ENS-D06-011` | condenser | vacuum degradation | backpressure, CW delta, air ingress | heat-rate/output loss | cleaning, leak test | Yes |
| `FM-ENS-D06-012` | power CEMS | invalid or drifting data | calibration flags, residual | compliance uncertainty | QA/QC, redundancy, calibration | Yes |
| `FM-ENS-D06-013` | CHP | heat shortfall | weather error, return T, asset state | customer service failure | reserve/auxiliary plan | Yes |
| `FM-ENS-D06-014` | city regulator | over/underpressure | hunting, setpoint drift | service/safety risk | slam-shut, relief, inspection | Yes |
| `FM-ENS-D06-015` | gas pipe | leak/corrosion/third party damage | survey, CP, excavation | fire, supply interruption | RBMS, patrol, isolation | Yes-high |
| `FM-ENS-D06-016` | RBMS | wrong risk prioritization | missing GIS, model drift | missed high-risk segment | governance, expert review | Yes |
| `FM-ENS-D06-017` | metering | systematic bias/comm failure | residual, read exception | revenue loss, complaint | calibration, exception workflow | Yes |
| `FM-ENS-D06-018` | solar | underperformance | PR residual, string/inverter alarms | lost generation/PPA gap | monitoring, inspection | Yes |
| `FM-ENS-D06-019` | offshore wind | condition fault plus access delay | vibration/oil/weather | long outage | CBM, spares, vessel plan | Yes-high |
| `FM-ENS-D06-020` | PPA | meter-allocation mismatch | missing intervals, residual | dispute, RE100 integrity | lineage, approval, audit | Yes |
| `FM-ENS-D06-021` | ESS bid | infeasible or low-value schedule | SOC/warranty/price residual | penalty/degradation | constraint engine, human approval | Yes |
| `FM-ENS-D06-022` | ESS safety | thermal/electrical precursor | T rise, gas, imbalance, insulation | fire, outage | BMS, HVAC, detection, E-stop | Yes-safety gated |
| `FM-ENS-D06-023` | EV charging | site overload/offline fleet | site demand, heartbeat | trip, failed sessions | dynamic control, local fallback | Yes |
| `FM-ENS-D06-024` | H2 purity | contaminant breakthrough | analyzer trend, bed state | liquefier restriction/off-spec | purification, analyzer, isolation | Yes |
| `FM-ENS-D06-025` | LH2 | excessive boil-off/transfer loss | tank P/T, dwell, mass residual | product loss, vent, shortage | insulation, recovery, scheduling | Yes-high |
| `FM-ENS-D06-026` | hydrogen safety | leak/ignition precursor | detector, pressure decay | major safety event | ESD, ventilation, exclusion | Yes-detection only |
| `FM-ENS-D06-027` | CCS absorber | solvent degradation/foaming | loading, DP, analysis | lower capture, corrosion | chemistry control, reclaiming | Yes |
| `FM-ENS-D06-028` | CCS chain | source-sink availability mismatch | capture/transport/injection state | vent/bypass, lost capture | buffer, chain scheduler | Yes |
| `FM-ENS-D06-029` | MRV | mass-balance/data gap | invalid meter, time mismatch | credit/compliance loss | calibration, substitution governance | Yes |
| `FM-ENS-D06-030` | common OT | time sync/data quality/cyber incident | timestamp drift, quality flag, network | unsafe/false optimization | segmentation, auth, historian QA | Yes-gated |

## 17.2 Failure Propagation Graph

```yaml
propagation_examples:
  - cause: vessel_ETA_delay
    path: terminal_receipt_delay -> low_tank_inventory -> sendout_constraint -> power_fuel_risk -> dispatch_loss
  - cause: BOG_compressor_trip
    path: tank_pressure_rise -> recovery_limit -> unloading_constraint -> berth_delay -> demurrage
  - cause: gas_turbine_fouling
    path: compressor_efficiency_loss -> heat_rate_increase -> marginal_cost_increase -> dispatch_competitiveness_loss
  - cause: city_gas_GIS_error
    path: wrong_excavation_clearance -> pipe_damage -> leak -> isolation -> customer_outage
  - cause: renewable_forecast_bias
    path: schedule_error -> imbalance -> ESS_re_dispatch -> extra_cycles -> degradation_and_margin_loss
  - cause: ESS_SOC_bias
    path: infeasible_bid -> dispatch_shortfall -> penalty -> warranty_stress
  - cause: LH2_delivery_delay
    path: station_low_inventory -> customer_supply_shortage -> tanker_reprioritization -> longer_dwell_and_BOG
  - cause: CCS_compressor_trip
    path: capture_backpressure -> absorber_constraint -> capture_bypass -> net_avoided_CO2_loss
```

---
