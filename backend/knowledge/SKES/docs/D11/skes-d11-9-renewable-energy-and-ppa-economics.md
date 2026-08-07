---
id: skes-d11-9-renewable-energy-and-ppa-economics
title: Renewable Energy and PPA Economics
summary: "재생에너지 PPA 계약의 실질 수익을 계산하는 비용 구조와 경제성 분석 방법을 제시하며, 8가지 주요 경제적 누수 요인과 6개 KPI를 통해 사업 리스크를 관리하는 방법을 다룬다."
tags: [d11, cost, table]
keywords: [PPA, 신재생에너지, 수익-비용 워터폴, 경제적 누수, 드라이버, DSCR, Curtailment loss, 발전-부하 매칭, REC, COD]
related: [CST-ENS-D11-031, CST-ENS-D11-032, CST-ENS-D11-033, CST-ENS-D11-034, CST-ENS-D11-035, CST-ENS-D11-036, CST-ENS-D11-037, CST-ENS-D11-038, KPI-ENS-D11-023, KPI-ENS-D11-024, KPI-ENS-D11-025, KPI-ENS-D11-026, KPI-ENS-D11-027, KPI-ENS-D11-028]
priority: normal
domain: D11
section: 9
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 552
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 9. Renewable Energy and PPA Economics

## 9.1 Revenue and Cost Waterfall

```text
Gross renewable generation
− auxiliary and electrical loss
− curtailment
= metered delivered MWh

Realized PPA contribution
= contracted energy revenue + REC/environmental value
− asset O&M − lease − insurance − network charge
− imbalance/shape/balancing cost
− curtailment and availability LD
− credit and settlement cost
```

## 9.2 Renewable·PPA Driver Record

| ID | Driver | Economic leakage | Decision |
|---|---|---|---|
| `CST-ENS-D11-031` | Resource forecast | day-ahead error·imbalance | forecast ensemble |
| `CST-ENS-D11-032` | Availability | lost generation | predictive O&M |
| `CST-ENS-D11-033` | Curtailment | lost MWh·REC | site·storage·contract |
| `CST-ENS-D11-034` | Shape mismatch | hourly purchase/sale gap | asset-load matching |
| `CST-ENS-D11-035` | Grid/COD delay | IDC·LD·lost revenue | milestone control |
| `CST-ENS-D11-036` | PPA credit | default·collateral | customer limit |
| `CST-ENS-D11-037` | REC treatment | price·eligibility·retirement | product design |
| `CST-ENS-D11-038` | O&M and vessel/weather | downtime·repair | maintenance window |

## 9.3 PPA KPI

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-023` | Captured Price | net market/PPA revenue ÷ delivered MWh |
| `KPI-ENS-D11-024` | Shape-adjusted Margin | energy+REC−shape−imbalance−O&M |
| `KPI-ENS-D11-025` | Curtailment Loss | curtailed MWh×counterfactual value |
| `KPI-ENS-D11-026` | P50/P90 DSCR | project cash/debt service |
| `KPI-ENS-D11-027` | COD Schedule Variance | actual vs finance model |
| `KPI-ENS-D11-028` | Hourly CFE Match | matched clean MWh/load MWh |

계약 MW를 실제 공급 MWh로, 발전량을 고객의 시간대별 탄소무배출 전력 충족률로 대체해서는 안 된다. PPA 경제성은 발전 Profile과 고객 Load Profile, 정산·망·REC·불균형 비용을 함께 계산한다.

---
