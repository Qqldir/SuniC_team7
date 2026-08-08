---
id: skes-d11-15-scenario-and-sensitivity-engine
title: Scenario and Sensitivity Engine
summary: "LNG·발전·도시가스 등 에너지사업의 18개 핵심 시나리오(가격·공급·환율 충격)와 각 시나리오별 영향범위·핵심산출물, 그리고 4개 카테고리(가격·수량·비용·재무)의 민감도분석 항목을 규정한 위험평가 프레임워크입니다."
tags: [d11, cost, schema, table]
keywords: [스트레스테스트, LNG, 발전, 도시가스, 환율충격, 위험시나리오, BESS, 재생에너지, 수소, 금리]
related: [SCN-ENS-D11-001, SCN-ENS-D11-002, SCN-ENS-D11-003, SCN-ENS-D11-004, SCN-ENS-D11-005, SCN-ENS-D11-006, SCN-ENS-D11-007, SCN-ENS-D11-008, SCN-ENS-D11-009, SCN-ENS-D11-010, SCN-ENS-D11-011, SCN-ENS-D11-012, SCN-ENS-D11-013, SCN-ENS-D11-014, SCN-ENS-D11-015, SCN-ENS-D11-016, SCN-ENS-D11-017, SCN-ENS-D11-018]
priority: normal
domain: D11
section: 15
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 782
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 15. Scenario and Sensitivity Engine

## 15.1 Scenario Master

| Scenario ID | Scenario | 핵심 충격 | 영향 사업 | 필수 출력 |
|---|---|---|---|---|
| `SCN-ENS-D11-001` | LNG_PRICE_SPIKE | JKM/HH/oil-linked 가격 상승 | LNG·발전·도시가스 | Margin-at-Risk·Cash·담보 |
| `SCN-ENS-D11-002` | LNG_SUPPLY_DISRUPTION | 생산·액화·항로 중단 | LNG·발전 | 대체 Cargo·Lost Margin |
| `SCN-ENS-D11-003` | LNG_SUPPLY_WAVE | 공급확대·가격하락 | Upstream·발전 | Portfolio rebalance |
| `SCN-ENS-D11-004` | FX_SHOCK | KRW/USD 변동 | 전 사업 | Hedge 후 EBIT·Cash |
| `SCN-ENS-D11-005` | LOW_SMP | 전력가격 하락 | 발전·CHP | Clean spark·정비 선택 |
| `SCN-ENS-D11-006` | PEAK_POWER_STRESS | 폭염·예비력 부족 | 발전·BESS | Availability value |
| `SCN-ENS-D11-007` | FORCED_OUTAGE | 핵심발전기 고장 | 발전·CHP | Lost Margin·복구 NPV |
| `SCN-ENS-D11-008` | WARM_WINTER | HDD 하락 | 도시가스 | Weather-normalized EBIT |
| `SCN-ENS-D11-009` | GAS_ELECTRIFICATION | 고객 전기화 | 도시가스 | Cohort churn·network cost |
| `SCN-ENS-D11-010` | RENEWABLE_CURTAILMENT | 계통제약 | 재생·PPA | Lost MWh·BESS option |
| `SCN-ENS-D11-011` | PPA_SHAPE_GAP | 부하-발전 불일치 | PPA | Hourly hedge cost |
| `SCN-ENS-D11-012` | BESS_SPREAD_COMPRESSION | 경쟁증가 | KCE | Degradation-adjusted NPV |
| `SCN-ENS-D11-013` | BESS_VOLATILITY | Scarcity 증가 | KCE | Risk-adjusted revenue |
| `SCN-ENS-D11-014` | CHARGING_LOW_UTILIZATION | EV 채택 지연 | EverCharge | Site breakeven |
| `SCN-ENS-D11-015` | H2_DEMAND_DELAY | 차량·충전소 지연 | 액화수소 | Cash burn·minimum offtake |
| `SCN-ENS-D11-016` | H2_CLUSTER_RAMP | 버스 Fleet 집중 | 액화수소 | Route·plant utilization |
| `SCN-ENS-D11-017` | CCS_VOLUME_GAP | Emitter FID 지연 | CCS | Stranded-infra NPV |
| `SCN-ENS-D11-018` | HIGH_RATE_DELAY | 금리상승·COD 지연 | 재생·BESS·H2·CCS | IDC·DSCR·Equity IRR |

## 15.2 Sensitivity Fields

```yaml
minimum_sensitivity:
  prices:
    - LNG_indices_and_basis
    - FX
    - SMP_and_heat_tariff
    - REC_and_carbon_value
    - ancillary_and_capacity_price
  volume:
    - demand_and_nominations
    - availability_and_utilization
    - curtailment_and_dispatch
    - firm_offtake_probability
  cost:
    - fuel_and_heat_rate
    - shipping_and_terminal
    - O&M_and_labor
    - degradation_and_augmentation
    - liquefaction_energy_and_BOG
    - MRV_and_long_tail_liability
  finance:
    - CAPEX_overrun
    - COD_delay
    - interest_rate_and_WACC
    - working_capital_and_collateral
    - residual_value_and_decommissioning
```

---
