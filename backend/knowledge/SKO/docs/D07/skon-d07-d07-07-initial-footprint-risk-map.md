---
id: skon-d07-d07-07-initial-footprint-risk-map
title: Initial Footprint Risk Map
summary: "생산거점 용량 정의 일관성, 미국·중국 지역 전환, 고객 집중, 제품 유연성 등 운영 리스크 6건의 식별 및 통제 체크리스트"
tags: [d07, footprint, schema]
keywords: [생산능력 정의, 고정비용, 부분 가동, 미국 생산망, 중국 JV, 고객 집중, HSBMA, EV·ESS, 유연성, D07, 용량 정의, 미국 풋프린트, 중국 지분, 고객 집중도, 제품 유연성, 부분 운영, JV 지분]
related: []
priority: normal
domain: D07
section: D07-07.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 704
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-07. Initial Footprint Risk Map

## RISK-D07-001 — Capacity Definition Risk

```yaml
risk_id: RISK-D07-001
title: Capacity Definition Inconsistency

risk:
  - IR design capacity and regulatory normalized capacity differ
  - JV gross capacity can be double-counted
  - Future target can be mistaken for current capacity

control:
  - Capacity type mandatory
  - Reference date mandatory
  - Consolidation scope mandatory

priority: VERY_HIGH
```

---

## RISK-D07-002 — Partial-Operation Fixed-Cost Risk

```yaml
risk_id: RISK-D07-002
title: Partial-Operation and Ramp-Up Burden

affected_plants:
  - Ivancsa
  - Yancheng 3

risk:
  - Depreciation and labor begin before full output
  - Low utilization increases unit fixed cost
  - Customer and product concentration slows ramp

priority: VERY_HIGH
```

---

## RISK-D07-003 — U.S. Footprint Transition Risk

```yaml
risk_id: RISK-D07-003
title: United States Footprint Transition

risk:
  - Kentucky capacity exited SK On footprint
  - Tennessee mass production is deferred to 2028
  - HSBMA is customer-linked JV capacity
  - Georgia standalone plants may require EV–ESS flexibility

priority: VERY_HIGH
```

---

## RISK-D07-004 — China Ownership Transition

```yaml
risk_id: RISK-D07-004
title: China JV Stake-Swap Completion

risk:
  - Huizhou disposal and Jiangsu acquisition remain pending
  - Operating authority and financial consolidation may change at closing
  - Capacity histories can be double-counted during transition

priority: HIGH
```

---

## RISK-D07-005 — Customer Concentration by Plant

```yaml
risk_id: RISK-D07-005
title: Customer-Linked Capacity Concentration

known_example:
  - HSBMA supplies Hyundai Motor Group's U.S. plants

missing:
  - Customer allocation by line
  - Contracted volume
  - Alternative-customer qualification
  - Product-switching time

priority: VERY_HIGH
```

HSBMA의 생산 Cell은 현대·기아·제네시스의 미국 생산거점에 공급되며 첫 생산물량은 IONIQ 9에 사용될 예정이라고 JV가 밝혔다. 이는 고객과 공장이 밀접하게 연결된 사례다. ([HSAGP ENERGY LLC][5])

---

## RISK-D07-006 — Capacity Flexibility

```yaml
risk_id: RISK-D07-006
title: EV·ESS Product Conversion Flexibility

missing:
  - Plants capable of producing both EV and ESS cells
  - LFP and NCM conversion scope
  - Conversion CAPEX
  - Customer requalification
  - Changeover duration
  - Local-content eligibility

priority: VERY_HIGH
```

---
