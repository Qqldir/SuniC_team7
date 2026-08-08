---
id: skes-d06-20-d06-o-i-seed-portfolio
title: D06 O/I Seed Portfolio
summary: "D06 운영 프로세스에서 추진할 O/I 시드 과제들의 포트폴리오로, LNG와 전력 분야의 68개 후보 과제와 각 과제의 우선순위 평가 기준을 제시한다."
tags: [d06, process, oi-seed, schema, table, "xref:d16", "xref:d05"]
keywords: [시드 우선순위 지정, LNG 공급망 최적화, 전력 발전 운영, 데이터 준비도, Prioritization Rule, KPI 성과지표, 구현 가능성 평가, 과제 마스터, 운영 효율화, 안전 규제 이점]
related: [SEED-ENS-D06-001, SEED-ENS-D06-002, SEED-ENS-D06-003, SEED-ENS-D06-004, SEED-ENS-D06-005, SEED-ENS-D06-006, SEED-ENS-D06-007, SEED-ENS-D06-008, SEED-ENS-D06-009, SEED-ENS-D06-010, SEED-ENS-D06-011, SEED-ENS-D06-012, SEED-ENS-D06-013, SEED-ENS-D06-014, SEED-ENS-D06-015, SEED-ENS-D06-016, SEED-ENS-D06-017, SEED-ENS-D06-018, SEED-ENS-D06-019, SEED-ENS-D06-020, SEED-ENS-D06-021, SEED-ENS-D06-022, SEED-ENS-D06-023, SEED-ENS-D06-024]
priority: normal
domain: D06
section: 20
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 2638
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 20. D06 O/I Seed Portfolio

## 20.1 Seed Prioritization Rule

```yaml
priority_score:
  strategic_relevance: 0_to_5
  measurable_value: 0_to_5
  data_readiness: 0_to_5
  implementation_feasibility: 0_to_5
  safety_and_regulatory_benefit: 0_to_5
  affiliate_reuse: 0_to_5
  penalty:
    safety_autonomy_risk: 0_to_minus5
    data_rights_or_cyber_gap: 0_to_minus5
    planned_business_uncertainty: 0_to_minus5
rule:
  P0: high_value_and_operating_data_available
  P1: data foundation or pilot required
  P2: planned business or high dependency
```

## 20.2 Seed Master — 68 Candidates

| Seed ID | O/I 과제 | Process | 핵심 데이터 | KPI | 우선도 |
|---|---|---|---|---|---|
| `SEED-ENS-D06-001` | LNG 수요–계약–재고 통합 시나리오 엔진 | LNG-001 | contract, demand, cargo, tank | supply risk, landed cost | P0 |
| `SEED-ENS-D06-002` | 다중 제약 cargo portfolio optimizer | LNG-001 | slot, vessel, quality, rights | demurrage, shortfall | P1 |
| `SEED-ENS-D06-003` | upstream entitlement shortfall early warning | LNG-002 | production forecast, outage | realization | P1 |
| `SEED-ENS-D06-004` | liquefaction entitlement performance cockpit | LNG-004 | feed, production, outage | realization, variance | P1 |
| `SEED-ENS-D06-005` | partner outage impact simulation | LNG-004 | outage, cargo, inventory | recovery time | P1 |
| `SEED-ENS-D06-006` | export loading quality/document anomaly check | LNG-005 | quality, meter, document | exception rate | P2 |
| `SEED-ENS-D06-007` | vessel ETA·speed·BOG optimization | LNG-006 | AIS, weather, cargo, berth | ETA, fuel, BOR | P0 |
| `SEED-ENS-D06-008` | carrier machinery condition analytics | LNG-007 | vibration, alarm, work | availability | P1 |
| `SEED-ENS-D06-009` | berth turnaround digital twin | LNG-008 | marine, arm, transfer | turnaround | P1 |
| `SEED-ENS-D06-010` | unloading transfer-difference diagnostics | LNG-008 | ship/shore meter, tank | discrepancy | P0 |
| `SEED-ENS-D06-011` | tank inventory reconciliation engine | LNG-009 | level, density, receipts/use | inventory error | P0 |
| `SEED-ENS-D06-012` | LNG quality blending and tank allocation | LNG-009 | composition, tank, demand | quality compliance | P1 |
| `SEED-ENS-D06-013` | BOG generation forecast | LNG-010 | tank, unloading, ambient | generated BOG | P0 |
| `SEED-ENS-D06-014` | BOG compressor predictive maintenance | LNG-010 | vibration, process, work | availability/recovery | P0 |
| `SEED-ENS-D06-015` | vaporizer·pump efficiency and fouling analytics | LNG-011 | flow, P/T, energy | sendout efficiency | P1 |
| `SEED-ENS-D06-016` | power dispatch–gas nomination co-optimizer | PWR-001 | market, unit, gas | imbalance, margin | P0 |
| `SEED-ENS-D06-017` | startup probability and time predictor | PWR-001/2 | sequence, condition, history | start reliability | P0 |
| `SEED-ENS-D06-018` | startup fuel·emissions·life minimizer | PWR-002 | fuel, CEMS, thermal | start fuel/time | P1 |
| `SEED-ENS-D06-019` | gas-turbine corrected performance monitor | PWR-003 | ambient, fuel, output | heat rate | P0 |
| `SEED-ENS-D06-020` | combustion anomaly early warning | PWR-003 | dynamics, T spread, NOx | trip/emission | P0 |
| `SEED-ENS-D06-021` | HRSG tube-leak and fatigue risk model | PWR-004 | chemistry, T, acoustics | outage | P1 |
| `SEED-ENS-D06-022` | condenser vacuum loss root-cause AI | PWR-005 | vacuum, CW, chemistry | heat rate | P0 |
| `SEED-ENS-D06-023` | efficiency–ramp–life multi-objective dispatch | PWR-006 | load, heat rate, starts | margin/life | P1 |
| `SEED-ENS-D06-024` | CEMS data-quality and emission anomaly monitor | PWR-007 | CEMS, fuel, mode | valid data/emission | P0 |
| `SEED-ENS-D06-025` | water chemistry and cooling reuse optimizer | PWR-007 | water, chemistry, load | water/use/outage | P1 |
| `SEED-ENS-D06-026` | historian–EAM failure digital thread | PWR-008 | tags, alarm, work | MTBF/recurrence | P0 |
| `SEED-ENS-D06-027` | outage scope·part·crew optimizer | PWR-008 | asset, work, parts | outage duration | P1 |
| `SEED-ENS-D06-028` | CHP heat-demand probabilistic forecast | CHP-001 | weather, calendar, meter | forecast error | P0 |
| `SEED-ENS-D06-029` | electricity–heat co-dispatch optimizer | CHP-001/2 | power, heat, plant | margin/service | P0 |
| `SEED-ENS-D06-030` | city-gate mass/energy balance | CG-001 | custody meter, quality | imbalance | P0 |
| `SEED-ENS-D06-031` | regulator hunting early detection | CG-002 | pressure, position, flow | pressure stability | P0 |
| `SEED-ENS-D06-032` | odorant injection and inventory intelligence | CG-002 | flow, injection, inventory | compliance | P1 |
| `SEED-ENS-D06-033` | city-gas network state estimation | CG-003 | pressure, flow, topology | compliance/residual | P1 |
| `SEED-ENS-D06-034` | explainable RBMS risk scoring | CG-004 | pipe, environment, history | risk capture | P0 |
| `SEED-ENS-D06-035` | RBMS inspection-plan optimizer | CG-004 | risk, crew, access, cost | risk reduction | P0 |
| `SEED-ENS-D06-036` | drone inspection asset geolocation | CG-005 | image, GNSS, GIS | mapping accuracy | P0 |
| `SEED-ENS-D06-037` | multimodal gas-leak anomaly detection | CG-005 | detector, image, pressure | confirmation time | P0 |
| `SEED-ENS-D06-038` | excavation–pipeline conflict alert | CG-006 | permit, GIS, schedule | damage prevention | P0 |
| `SEED-ENS-D06-039` | regulator/valve condition-based maintenance | CG-007 | test, pressure, work | failure/maintenance | P1 |
| `SEED-ENS-D06-040` | smart-meter anomaly and failure prediction | CG-008 | interval, battery, comm | read rate | P0 |
| `SEED-ENS-D06-041` | unaccounted-for-gas decomposition | CG-008 | custody, meter, event | UFG | P0 |
| `SEED-ENS-D06-042` | customer move·inspection workflow automation | CG-009 | customer, meter, work | lead time | P1 |
| `SEED-ENS-D06-043` | gas emergency dispatch decision support | CG-010 | call, GIS, crew, valve | safe-state time | P0-safety |
| `SEED-ENS-D06-044` | solar/wind ensemble forecasting | REN-001 | NWP, local, SCADA | forecast error | P0 |
| `SEED-ENS-D06-045` | forecast uncertainty-to-bid decision | REN-001 | forecast distribution, price | imbalance cost | P1 |
| `SEED-ENS-D06-046` | PV string/inverter loss classifier | REN-002 | electrical, weather, alarm | lost energy | P0 |
| `SEED-ENS-D06-047` | wind drivetrain condition analytics | REN-003 | vibration, oil, SCADA | downtime | P0 |
| `SEED-ENS-D06-048` | offshore access and maintenance scheduler | REN-003/4 | weather, vessel, part | repair time | P1 |
| `SEED-ENS-D06-049` | renewable lost-energy root-cause engine | REN-004 | expected, SCADA, work | availability | P0 |
| `SEED-ENS-D06-050` | PPA interval allocation and exception automation | REN-005 | meter, contract, REC | cycle/exception | P0 |
| `SEED-ENS-D06-051` | RE100 evidence ledger | REN-005 | meter, REC, contract | audit completeness | P1 |
| `SEED-ENS-D06-052` | ESS price/award forecast model ensemble | ESS-001 | market history, fundamentals | revenue forecast | P0 |
| `SEED-ENS-D06-053` | ESS bid optimizer with degradation cost | ESS-001 | price, SOC/SOH, warranty | revenue/cycle | P0 |
| `SEED-ENS-D06-054` | award-to-dispatch feasibility guard | ESS-002 | award, telemetry, limit | tracking/penalty | P0 |
| `SEED-ENS-D06-055` | SOC/SOH confidence-aware estimator | ESS-003 | cell/rack, throughput | usable energy | P0 |
| `SEED-ENS-D06-056` | battery thermal precursor fusion | ESS-003 | T, gas, voltage, insulation | early warning | P0-safety |
| `SEED-ENS-D06-057` | DER flexibility onboarding and baseline engine | DERMS/VPP | meter, device, contract | eligible MW | P1 |
| `SEED-ENS-D06-058` | EV site dynamic power allocation | EVC-001 | site load, sessions | delivered energy/peak | P0 |
| `SEED-ENS-D06-059` | departure-aware charging queue optimizer | EVC-001 | request, priority, load | satisfaction | P1 |
| `SEED-ENS-D06-060` | charger failure triage and recurrence AI | EVC-002 | fault, firmware, work | uptime/MTTR | P0 |
| `SEED-ENS-D06-061` | hydrogen feed purity breakthrough prediction | H2-001 | analyzer, bed, flow | off-spec/availability | P1 |
| `SEED-ENS-D06-062` | liquefier specific-energy optimizer | H2-002 | process, ambient, power | kWh/kg | P0 |
| `SEED-ENS-D06-063` | LH₂ storage boil-off forecast and recovery | H2-002 | tank P/T/level, dwell | BOR/loss | P0 |
| `SEED-ENS-D06-064` | tanker route·inventory·dwell optimizer | H2-003 | order, route, tank, station | OTIF/BOR | P0 |
| `SEED-ENS-D06-065` | LH₂ transfer mass-balance diagnostics | H2-003 | load/delivery meter, P/T | transfer loss | P0 |
| `SEED-ENS-D06-066` | capture process solvent-health analytics | CCS-001 | loading, chemistry, DP | capture/solvent | P2 |
| `SEED-ENS-D06-067` | power–capture integrated dynamic optimizer | CCS-001 | unit, steam, capture | net avoided/margin | P2 |
| `SEED-ENS-D06-068` | CCS chain MRV and mass-balance platform | CCS-001 | capture/transport/injection | MRV completeness | P1 |

## 20.3 Seed Card Template

```yaml
seed_card:
  seed_id: required
  process_ids: []
  pain_id: required
  decision_to_improve: required
  current_workflow: required
  proposed_capability: required
  minimum_data: []
  baseline_KPI: required
  target_KPI: internal_gate
  pilot_asset_scope: internal_gate
  data_owner: required
  business_owner: required
  safety_owner: conditional
  cyber_zone: required
  build_buy_partner: D16
  evidence_and_IP: D05
  benefits_and_cost: D11_D12
  regulatory_gate: D14_D15
  stop_conditions: []
```

---
