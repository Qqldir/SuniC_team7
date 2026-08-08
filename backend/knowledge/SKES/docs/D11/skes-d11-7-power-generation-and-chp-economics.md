---
id: skes-d11-7-power-generation-and-chp-economics
title: Power Generation and CHP Economics
summary: "발전소의 운영 마진 구조와 전력/CHP 수익성을 좌우하는 10대 드라이버, 8개 성과지표(KPI)를 체계적으로 정의한 경제성 분석 프레임워크"
tags: [d11, cost, table]
keywords: [LNG 발전소, Dispatch 마진, 연료 효율, 가동률, SMP, 강제정지, HRSG 성능, 성과지표, 탄소비용]
related: [CST-ENS-D11-013, CST-ENS-D11-014, CST-ENS-D11-015, CST-ENS-D11-016, CST-ENS-D11-017, CST-ENS-D11-018, CST-ENS-D11-019, CST-ENS-D11-020, CST-ENS-D11-021, CST-ENS-D11-022, KPI-ENS-D11-009, KPI-ENS-D11-010, KPI-ENS-D11-011, KPI-ENS-D11-012, KPI-ENS-D11-013, KPI-ENS-D11-014, KPI-ENS-D11-015, KPI-ENS-D11-016]
priority: normal
domain: D11
section: 7
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 719
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 7. Power Generation and CHP Economics

## 7.1 Dispatch Margin

```text
Clean operating margin per MWh
= realized energy and ancillary-service revenue
− LNG fuel cost × actual heat rate
− variable O&M and start cost
− emission and environmental cost
− imbalance and settlement adjustment

Plant recurring EBIT
= margin per net MWh × settled net MWh
− fixed O&M − labor − insurance − depreciation
− expected outage cost − allocated terminal/access cost
```

## 7.2 Power·CHP Driver Record

| ID | Driver | 필요한 데이터 | 손익 효과 | 주요 Lever |
|---|---|---|---|---|
| `CST-ENS-D11-013` | SMP | interval price·node/region | 매출 | Dispatch·정비시점 |
| `CST-ENS-D11-014` | Fuel cost | delivered LNG·allocation | 변동원가 | Cargo·Hedge |
| `CST-ENS-D11-015` | Heat rate | fuel input/net MWh | 연료효율 | Cleaning·tuning |
| `CST-ENS-D11-016` | Availability | available/period hours | 판매기회 | 정비·Spare |
| `CST-ENS-D11-017` | Forced outage | event·duration·price | Lost Margin | Predictive maintenance |
| `CST-ENS-D11-018` | Start/ramp cost | fuel·wear·time | 유연성 비용 | Commitment |
| `CST-ENS-D11-019` | Auxiliary load | gross vs net MWh | 순판매량 | Pump/fan optimization |
| `CST-ENS-D11-020` | HRSG/ST performance | temp·pressure·efficiency | 복합효율 | Fouling·inspection |
| `CST-ENS-D11-021` | Emission cost | NOx/CO2·permit·reagent | 환경원가 | Combustion control |
| `CST-ENS-D11-022` | Heat demand | steam/heat load·tariff | CHP 공동수익 | Co-optimization |

## 7.3 KPI and Controls

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-009` | Clean Spark Spread | SMP−fuel−variable O&M−carbon |
| `KPI-ENS-D11-010` | Net Heat Rate | fuel energy/net settled MWh |
| `KPI-ENS-D11-011` | Equivalent Availability | available time adjusted for derating |
| `KPI-ENS-D11-012` | Forced Outage Rate | forced outage/required hours |
| `KPI-ENS-D11-013` | Lost Margin from Outage | counterfactual dispatch margin−actual |
| `KPI-ENS-D11-014` | Start Cost per Start | fuel+wear+labor/start |
| `KPI-ENS-D11-015` | Auxiliary Load Ratio | internal consumption/gross generation |
| `KPI-ENS-D11-016` | CHP Joint Margin | power+heat revenue−joint cost |

CHP에서는 연료비를 전력과 열 중 한쪽에 임의 배분하지 않는다. 에너지·Exergy·시장가치 등 승인된 원가배부 정책을 고정하고, 전력·열 공동 최적화의 증분 Margin을 별도 계산한다.

---
