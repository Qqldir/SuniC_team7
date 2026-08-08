---
id: skes-d10-7-city-gas-market-and-electrification
title: City-Gas Market and Electrification
summary: "도시가스의 주거·산업·상업 수요를 세분화하고, 열펌프 등 대체재로 인한 고객 이탈 및 수요 변화를 코호트 모델로 예측하는 방법을 다룬다."
tags: [d10, market, schema, table]
keywords: [난방, 열펌프, 코호트 분석, churn, 산업열, 연료 전환, 이탈률, 수요 드라이버, 대체재, ESG]
related: []
priority: normal
domain: D10
section: 7
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 478
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 7. City-Gas Market and Electrification

## 7.1 Demand Segments

| Segment | 주요 수요 driver | 대체재 | 위험 signal | E&S response |
|---|---|---|---|---|
| residential heating | HDD·가구·보일러 stock | heat pump·district heat | 전기요금·보조금·신축규정 | cohort forecast |
| cooking | 가구·상업시설 | induction·electric kitchen | 신축 all-electric | 서비스 bundle |
| commercial building | 면적·운영시간 | heat pump·electric boiler | ESG·효율규제 | efficiency service |
| industrial heat | production·temperature | electricity·hydrogen·biomass | carbon price·fuel spread | fuel-switch solution |
| CHP/cogen | power·steam demand | grid+boiler·ESS | SMP·gas price | integrated dispatch |
| transport gas | vehicle stock | EV·hydrogen | fleet conversion | asset repurpose |

## 7.2 Market Interpretation

도시가스는 고객 510만 가구라는 stock만으로 성장성을 판단하면 안 된다. 핵심은 고객 수보다 `weather-normalized volume`, `connection churn`, `usage per account`, `service cost`, `electrification probability`, `industrial fuel-switch economics`다.

## 7.3 Electrification Cohort Model

```yaml
cohort_features:
  - building_type_and_age
  - heating_equipment_age
  - annual_and_peak_gas_use
  - electricity_capacity
  - renovation_event
  - local_subsidy_and_code
  - complaint_and_service_history
  - weather_normalized_load
outputs:
  - 12m_churn_probability
  - 5y_volume_decline
  - retention_offer
  - heat_pump_or_hybrid_opportunity
guardrails:
  - no_automated_discrimination
  - privacy_minimization
  - explainable_segment_action
```

---
