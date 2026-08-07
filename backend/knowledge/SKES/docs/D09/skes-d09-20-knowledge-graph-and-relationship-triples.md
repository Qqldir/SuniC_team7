---
id: skes-d09-20-knowledge-graph-and-relationship-triples
title: Knowledge Graph and Relationship Triples
summary: "에너지 공급 계약의 고객, 계량, 시설 등을 그래프로 모델링하기 위한 노드·엣지 타입과 실제 거래 사례의 관계 삼중조를 정의한 문서"
tags: [d09, customer]
keywords: [그래프 데이터베이스, 노드·엣지, 관계 삼중조, 계약·PPA, 에너지 수매, 고객 관계, 계량 체계, 공급망 모델링]
related: []
priority: normal
domain: D09
section: 20
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 490
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 20. Knowledge Graph and Relationship Triples

## 20.1 Node Types

`Customer`, `LegalEntity`, `Contract`, `DemandVersion`, `Meter`, `ServicePoint`, `Asset`, `Product`, `Market`, `Site`, `Fleet`, `Vehicle`, `Station`, `Invoice`, `Incident`, `Evidence`, `O/ISeed`.

## 20.2 Edge Types

`OFFTAKES`, `SUPPLIES`, `PARTICIPATES_IN`, `OPERATES`, `HOSTS`, `METERS`, `SETTLES`, `SERVES`, `USES`, `CONSTRAINS`, `EVIDENCES`, `AMENDS`, `TRIGGERS`, `EXPOSES_TO`, `REQUIRES_DATA_FROM`.

## 20.3 Core Triples

```text
Amorepacific --OFFTAKES--> Renewable electricity
PPA-ENS-D09-001 --HAS_TERM--> 20 years
PPA-ENS-D09-001 --HAS_CONTRACTED_CAPACITY--> 5MW
SK Specialty --OFFTAKES--> Renewable electricity
KCE TX19 --PARTICIPATES_IN--> ERCOT
KCE NY3 --SERVES--> Orange & Rockland NWA
Avis IAH --USES--> EverCharge charging solution
SK hynix commute fleet --USES--> Icheon liquid-hydrogen station
Cheonan MOU --IS_NOT_EQUAL_TO--> Firm hydrogen offtake
City-gas meter --METERS--> Service point
Contract --CONSTRAINS--> Demand plan
Metered delivery --SETTLES--> Invoice
```

## 20.4 Retrieval Queries

1. 공개된 PPA 고객 중 계약기간과 규모가 함께 확인된 사례는?
2. MOU이지만 확정수요로 집계하면 안 되는 수소 관계는?
3. KCE 시장운영에서 고객이 아닌 시장운영기관은?
4. EverCharge fleet 고객의 departure-SOC 개선에 필요한 데이터는?
5. 도시가스 긴급신고와 연결되는 자산·출동·고객 Journey는?
6. 계약량과 실제 계량량이 불일치한 계약의 손익 영향은?
7. 데이터 권리가 불명확하여 즉시 PoC할 수 없는 Seed는?

---
