---
id: skes-d09-14-crm-contract-meter-and-settlement-archit
title: "CRM, Contract, Meter and Settlement Architecture"
summary: "고객·계약·계량·정산을 담당하는 CRM, CLM, 빌링, AMI 등 11개 시스템의 마스터 데이터와 이벤트의 조인 구조, legal_customer_id 등 7가지 골든 키, 그리고 고객명 매칭·미터 귀속·시간대·단위 관리 등 데이터 품질 규칙을 정의한다."
tags: [d09, customer, table]
keywords: [데이터통합, 고객마스터, 계약관리, 계량정산, 식별자, 빌링, 시스템맵, AMI]
related: []
priority: normal
domain: D09
section: 14
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 571
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 14. CRM, Contract, Meter and Settlement Architecture

## 14.1 Minimum System Map

| System | Master | Event | Join key |
|---|---|---|---|
| CRM | account·contact·opportunity | meeting·stage | customer_id |
| CLM | contract·obligation | amendment·renewal | contract_id |
| billing | account·tariff | invoice·payment | billing_account_id |
| metering/AMI | meter·service point | read·quality flag | meter_id |
| ETRM | commodity·book·position | trade·nomination | deal_id |
| EMS/SCADA | asset·tag | dispatch·alarm | asset_id/tag_id |
| contact center | case·reason | call/chat/field | service_event_id |
| PPA platform | offtaker·plant | meter match·REC | ppa_id |
| KCE MarketCapture | asset·market | bid·award | market_asset_id |
| EverCharge | site·EVSE·driver | session·payment | site_id/evse_id |
| hydrogen logistics | station·trailer | load·delivery·dispense | shipment_id |

## 14.2 Golden Keys

1. `legal_customer_id`: 계약·신용·회계 단위.
2. `service_point_id`: 물리 공급 위치.
3. `contract_id`: 권리·의무 단위.
4. `meter_id`: 계량·정산 단위.
5. `asset_id`: 공급능력·고장 단위.
6. `relationship_id`: 고객·시장·파트너 역할 단위.
7. `demand_version_id`: 예상·확정·실적 이력 단위.

## 14.3 Data-Quality Rules

- 하나의 고객이 여러 법인·사이트·계약을 가질 수 있다.
- 하나의 meter가 계약변경으로 다른 account에 귀속될 수 있으므로 유효기간을 저장한다.
- 고객명 fuzzy match는 자동 병합하지 않고 후보와 근거를 제시한다.
- 익명 EverCharge 사례와 공개 고객사를 이름 유사성으로 연결하지 않는다.
- market settlement interval의 시간대·DST·timezone을 원본대로 보존한다.
- 가스·전력·열·수소의 단위변환에는 발열량·온압·효율 가정을 명시한다.

---
