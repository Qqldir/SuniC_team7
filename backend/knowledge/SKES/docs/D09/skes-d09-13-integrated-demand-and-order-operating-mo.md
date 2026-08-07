---
id: skes-d09-13-integrated-demand-and-order-operating-mo
title: Integrated Demand and Order Operating Model
summary: "고객 요청 수요를 상태별로 분류하고, 각 상태에서 조달·매출 처리 방식과 S&OP 의사결정 시점, 그리고 다층적 예측 관리 방식을 안내한다."
tags: [d09, customer, table]
keywords: [수요 상태, Procurement, 매출인식, S&OP, Nomination, 예측, Settlement, 계약, Dispatch]
related: []
priority: normal
domain: D09
section: 13
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 501
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 13. Integrated Demand and Order Operating Model

## 13.1 Common Demand State

| State | Definition | Can drive procurement? | Can recognize revenue? |
|---|---|---:|---:|
| opportunity | 잠재 고객·시장 | no | no |
| MOU/plan | 비구속 협력·목표 | no | no |
| contracted maximum | 계약상 상한·기준 | scenario | no |
| forecast | 예상 사용·발전·세션 | planning | no |
| nomination | 고객·시장 제출 수요 | conditional | no |
| firm order/award | 취소 제한 주문·시장낙찰 | yes | no |
| dispatched | 운영명령 | yes | no |
| delivered/metered | 물리 공급 | reconciliation | conditional |
| accepted/settled | 검수·정산 확정 | history | yes per accounting |
| adjusted | true-up·claim·refund | history | revised |

## 13.2 S&OP Cadence

| Horizon | Decision | Inputs | Output |
|---|---|---|---|
| intraday | dispatch·재고·충전배분 | telemetry·시장·기상 | operating setpoint |
| day-ahead | LNG/gas/power/hydrogen nomination | forecast·outage·contract | firm plan |
| week | cargo·maintenance·station logistics | demand range·inventory | constrained schedule |
| month | billing·PPA matching·sales plan | meter·price·contract | settlement and variance |
| quarter | customer portfolio·credit·renewal | churn·margin·risk | account action |
| year+ | PPA·asset·fleet·CCS development | scenario·policy·CAPEX | investment case |

## 13.3 Forecast Hierarchy

`portfolio → business → region/market → legal customer → contract → delivery point/site → meter/asset → interval`

Forecast reconciliation must preserve both top-down management scenario and bottom-up customer/site forecast. Forced overwrite is prohibited; variance is stored as an explainable bridge.

---
