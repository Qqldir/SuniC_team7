---
id: skes-d09-10-kce-bess-market-and-utility-relationship
title: KCE BESS Market and Utility Relationships
summary: "BESS 운영의 ISO/RTO·유틸리티·지역사회·ITC 매수자 등 6층 이해관계자 관계와 각층의 의무·데이터를 정의하고, 입찰부터 정산까지의 실패 모드(가용성 지연, SOC 오류, 규칙 불일치 등)별 제어 요구사항을 제시하는 운영 프레임워크."
tags: [d09, customer, table]
keywords: [ERCOT, NYISO, 입찰-정산, 도매 시장, 유틸리티 계약, 상호 연결, 이해관계자, 계약 구조, 가용성 관리]
related: []
priority: normal
domain: D09
section: 10
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 512
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 10. KCE BESS Market and Utility Relationships

## 10.1 Relationship Layers

| Layer | Counterparty | Revenue/obligation | Data |
|---|---|---|---|
| wholesale market | ERCOT·NYISO | energy·ancillary·capacity settlement | bid·award·LMP·telemetry |
| utility contract | Orange & Rockland 등 | NWA·availability·performance | feeder need·SLA |
| interconnection | utility/ISO | operating permission·limits | queue·study·curtailment |
| tax-credit buyer | undisclosed third party | ITC transfer consideration | eligibility·transfer |
| land/community | landowner·local government | lease·tax·permit | milestones·complaints |
| optimizer user | internal trading/ops | dispatch recommendation | forecast·SOC·degradation |

## 10.2 Bid-to-Settlement Event Model

`price forecast → asset availability → warranty/degradation constraint → bid submission → award → dispatch instruction → telemetry response → meter validation → settlement → dispute/true-up`

| Failure mode | Customer/market impact | Required control |
|---|---|---|
| stale availability | non-performance | real-time asset state |
| SOC forecast error | missed dispatch | uncertainty reserve |
| telemetry mismatch | penalty/dispute | redundant validation |
| rule version mismatch | invalid bid | rule registry |
| degradation omitted | short-term gain, long-term loss | warranty-aware optimizer |
| price spike miss | opportunity loss | ensemble forecast |
| settlement data mismatch | revenue leakage | bid-to-meter lineage |

## 10.3 KCE Customer Definition Rule

ERCOT와 NYISO의 최종 수혜자는 광범위한 전력소비자지만 D09 customer master에는 ISO/RTO를 `MARKET_OPERATOR`로 저장한다. 시장 참가자·utility·지역사회·ITC buyer의 관계를 한 고객 레코드로 합치지 않는다.

---
