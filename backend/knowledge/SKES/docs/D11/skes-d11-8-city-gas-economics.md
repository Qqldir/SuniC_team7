---
id: skes-d11-8-city-gas-economics
title: City-Gas Economics
summary: 도시가스 사업의 수익성을 결정하는 요금·손실·수요 변동 등 8대 드라이버와 이를 추적하는 성과 지표 체계
tags: [d11, cost, table]
keywords: [요금 패스-스루, 청구누수, 기상수요, 계량기, 현장출동, 수금, 고객이탈, 마진율, DMA, DSO]
related: [CST-ENS-D11-023, CST-ENS-D11-024, CST-ENS-D11-025, CST-ENS-D11-026, CST-ENS-D11-027, CST-ENS-D11-028, CST-ENS-D11-029, CST-ENS-D11-030, KPI-ENS-D11-017, KPI-ENS-D11-018, KPI-ENS-D11-019, KPI-ENS-D11-020, KPI-ENS-D11-021, KPI-ENS-D11-022]
priority: normal
domain: D11
section: 8
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 502
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 8. City-Gas Economics

## 8.1 Customer and Network Waterfall

```text
Purchased gas
→ network input
→ pressure regulation and metering
→ billed volume
→ collected revenue
→ commodity pass-through + regulated/service margin
− network O&M − safety − meter − service − bad debt
```

## 8.2 City-Gas Driver Record

| ID | Driver | 손익·현금 영향 | 필요한 세분화 |
|---|---|---|---|
| `CST-ENS-D11-023` | Weather demand | 물량·수입·재고 | 고객군·HDD/CDD·지역 |
| `CST-ENS-D11-024` | Tariff/pass-through | 매출·Margin lag | 요금항목·적용시점 |
| `CST-ENS-D11-025` | Unaccounted-for gas | 구매량 대비 청구누수 | DMA·압력·계량기 |
| `CST-ENS-D11-026` | Leak and emergency | 손실·안전·복구비 | 배관구간·원인 |
| `CST-ENS-D11-027` | Meter accuracy | 매출누락·민원 | 형식·연령·고객군 |
| `CST-ENS-D11-028` | Field service | 출장·콜센터·재방문 | 요청유형·지역 |
| `CST-ENS-D11-029` | Bad debt | 현금회수·충당금 | 고객군·연체기간 |
| `CST-ENS-D11-030` | Customer churn | 장기 물량 감소 | 전기화·연료전환 Cohort |

## 8.3 City-Gas KPI

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-017` | Weather-normalized Volume | 실제−기상효과 |
| `KPI-ENS-D11-018` | Margin per Billed Nm³ | 순매출−변동원가/청구량 |
| `KPI-ENS-D11-019` | Unaccounted-for Gas | input−billed−known operations |
| `KPI-ENS-D11-020` | Cost-to-Serve/Customer | network+meter+call+visit/customer |
| `KPI-ENS-D11-021` | First-time Fix Rate | 1회 해결/현장출동 |
| `KPI-ENS-D11-022` | DSO and Bad-debt Rate | 채권회수일·미회수율 |

---
