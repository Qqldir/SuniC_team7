---
id: skes-d06-11-ess-derms-vpp-operations
title: ESS·DERMS·VPP Operations
summary: "에너지저장장치와 분산전원 시스템의 운영 상태 정의, 시장 입찰 최적화, 실시간 지령 처리 및 안전성 제어 프로세스"
tags: [d06, process, schema, table, "xref:d07"]
keywords: [에너지저장, 분산에너지, 전력중개, 입찰 최적화, MarketCapture, 배터리 운영, SOC, 실시간 지령, 제어 계층, 성능 저하]
related: [PROC-ENS-D06-ESS-001, PROC-ENS-D06-ESS-002, PROC-ENS-D06-ESS-003]
priority: normal
domain: D06
section: 11
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1465
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 11. ESS·DERMS·VPP Operations

## 11.1 Operating-State Boundary

| Capability | 공개 상태 | D06 처리 |
|---|---|---|
| KCE utility-scale ESS | 개발·운영 공개 | 자회사 운영역량으로 상세화 |
| MarketCapture | AI 기반 입찰 최적화 소프트웨어 공개 | 기능은 직접근거, 모델 내부는 Gap |
| 국내 수요관리/재생연계 ESS | 사업모델 공개 | 사업운영 프로세스 상세화, 자산별 실적은 D07 |
| DERMS | Ensolve 기반 추진 계획 공개 | `DEVELOPING`, 실시간 대규모 운영 단정 금지 |
| VPP | 소규모 전력중개 진입 검토 공개 | `PLANNED`, 상용운영 KPI 단정 금지 |

## 11.2 `PROC-ENS-D06-ESS-001` — Market Forecasting and Bid Optimization

```yaml
process_id: PROC-ENS-D06-ESS-001
operator_boundary: KCE_affiliate_capability
public_confirmation: MarketCapture is described as AI-driven energy bidding optimization
inputs:
  - day_ahead and real_time price forecast
  - ancillary service price and requirement
  - asset power energy efficiency and availability
  - SOC SOH temperature and warranty constraints
  - interconnection and market participation rules
  - outage maintenance and derating
decisions:
  - market product
  - bid price and quantity
  - charge discharge schedule
  - reserve SOC and headroom
  - cycling and degradation budget
outputs:
  - bid package
  - scenario value and risk
  - approved operating envelope
  - model version and decision log
model_controls:
  - forecast vintage
  - feature and training window
  - constraint version
  - human override and reason
  - backtest vs realized outcome
failure_modes:
  - price forecast error
  - stale availability or SOC
  - market rule change
  - degradation cost omitted
  - infeasible stacked service schedule
  - opaque model override
KPIs:
  - awarded_vs_offered
  - realized_vs_forecast_revenue
  - dispatch_feasibility
  - revenue_per_equivalent_cycle
  - forecast_error_by_market
OI_seeds: [SEED-ENS-D06-052, SEED-ENS-D06-053]
```

## 11.3 `PROC-ENS-D06-ESS-002` — Award-to-Dispatch Translation

```yaml
inputs:
  - award and dispatch instruction
  - current SOC SOH power limit and temperature
  - site meter and grid state
  - planned subsequent obligations
activities:
  - validate instruction and market timestamp
  - calculate asset setpoint
  - enforce power energy and safety constraints
  - issue PCS command
  - confirm telemetry and performance
  - record deviation and settlement impact
control_hierarchy:
  market_layer: bid_award_dispatch
  fleet_layer: asset allocation
  site_layer: EMS setpoint and interconnection
  equipment_layer: PCS BMS HVAC fire_system
safety_override: always_higher_priority_than_market_dispatch
failure_modes:
  - telemetry latency or time skew
  - dispatch instruction conflict
  - SOC estimate error
  - PCS or communication trip
  - site limit breach
KPIs:
  - response_time
  - dispatch_tracking_error
  - unavailable_MW
  - settlement_penalty
  - override_frequency
OI_seeds: [SEED-ENS-D06-054]
```

## 11.4 `PROC-ENS-D06-ESS-003` — Battery Operation·Thermal Safety·Degradation

```yaml
operating_state:
  electrical:
    - cell module rack voltage
    - current power and energy
    - SOC and SOH
    - imbalance and insulation
  thermal:
    - cell module rack and room temperature
    - cooling command and HVAC state
    - temperature gradient and rate_of_change
  safety:
    - gas smoke and fire detection
    - contactor breaker and emergency_stop
    - suppression and ventilation state
  commercial:
    - cycle depth C_rate dwell and throughput
    - warranty limit and degradation budget
failure_modes:
  - cell imbalance
  - SOC drift
  - accelerated degradation
  - cooling failure
  - isolation or ground fault
  - thermal propagation precursor
  - nuisance trip or unavailable safety device
maintenance:
  - alarm review and remote reset governance
  - rack balancing or replacement
  - thermal system inspection
  - fire and gas detector proof test
  - firmware and cybersecurity change control
KPIs:
  - round_trip_efficiency
  - usable_energy_and_power
  - availability
  - degradation_per_throughput
  - temperature_excursion
  - safety_system_impairment_time
OI_seeds: [SEED-ENS-D06-055, SEED-ENS-D06-056]
```

## 11.5 DERMS/VPP Operating Model — Planned Gate

```yaml
status: DEVELOPING_OR_PLANNED_NOT_CONFIRMED_FULL_SCALE_OPERATION
resource_onboarding:
  - identity owner location and market eligibility
  - device capability and telemetry
  - customer consent and contract
  - baseline and measurement method
  - cyber certificate and control test
forecast_and_dispatch:
  - load renewable and flexibility forecast
  - portfolio optimization
  - constraint-aware dispatch
  - customer and safety override
settlement:
  - interval performance
  - baseline adjustment
  - incentive penalty and allocation
  - REC or environmental attribute separation
gates:
  - no control without authenticated resource
  - no settlement without meter lineage
  - no AI autonomous dispatch outside approved envelope
  - distribution constraint must override portfolio value
OI_seeds: [SEED-ENS-D06-057]
```

---
