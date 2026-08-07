---
id: skes-d11-11-ev-charging-economics-evercharge
title: EV Charging Economics — EverCharge
summary: EV 충전소의 수익·원가 구조 계산식과 운영 효율성을 측정하는 6개 경영 드라이버 및 KPI 6개를 정의한 경제성 분석 프레임워크 문서.
tags: [d11, cost, table]
keywords: [충전소 경제성, 포트 활용률, 수익 모델, 전력 수요 요금, 현장 서비스 비용, 가동률, 설치 원가, KPI, 마진율, 수익성 분석]
related: [CST-ENS-D11-049, CST-ENS-D11-050, CST-ENS-D11-051, CST-ENS-D11-052, CST-ENS-D11-053, CST-ENS-D11-054, KPI-ENS-D11-035, KPI-ENS-D11-036, KPI-ENS-D11-037, KPI-ENS-D11-038, KPI-ENS-D11-039, KPI-ENS-D11-040]
priority: normal
domain: D11
section: 11
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 406
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 11. EV Charging Economics — EverCharge

## 11.1 Site Economics

```text
Site net revenue
= charging energy margin + software/service fee + installation/service revenue
− purchased electricity − demand charge
− payment/network fee − maintenance and truck roll
− host revenue share − warranty − bad debt

Site cash return
= net revenue
− charger/panel/network CAPEX
− working capital
+ incentives actually received
```

## 11.2 Charging Driver and KPI

| ID | Driver | 주요 영향 |
|---|---|---|
| `CST-ENS-D11-049` | Port utilization | 매출·CAPEX 흡수 |
| `CST-ENS-D11-050` | Power-sharing efficiency | 제한된 kW당 서비스 차량 |
| `CST-ENS-D11-051` | Demand charge | Peak 전력비 |
| `CST-ENS-D11-052` | Uptime | 세션손실·SLA |
| `CST-ENS-D11-053` | Truck roll | 서비스 원가 |
| `CST-ENS-D11-054` | Installation variance | 프로젝트 Margin |

| KPI ID | KPI | 정의 |
|---|---|---|
| `KPI-ENS-D11-035` | Session/Port/Day | 실제 세션/가용 Port/일 |
| `KPI-ENS-D11-036` | Served EV per Constrained kW | 연결전력 활용도 |
| `KPI-ENS-D11-037` | Net Margin/Port-Month | 모든 변동비 차감 후 |
| `KPI-ENS-D11-038` | Uptime and Lost Session | 가용성·추정 미판매 세션 |
| `KPI-ENS-D11-039` | Truck Roll/100 Ports | 현장서비스 효율 |
| `KPI-ENS-D11-040` | Install Gross Margin | Quote→Actual 설치수익성 |

---
