---
id: skon-d07-d07-09-initial-manufacturing-footprint-oi-seeds
title: Initial Manufacturing Footprint OI Seeds
summary: "SK온 배터리 생산 거점의 용량 최적화를 위한 5가지 핵심 전략(Digital Twin, JV 거버넌스, 라인 전환, 수요 배분, 경험 이전)과 각각의 필요 역량 및 성과지표를 정의한 문서."
tags: [d07, footprint, oi-seed, schema]
keywords: [배터리용량, 디지털트윈, 공장최적화, EV/ESS, 합작투자, 수요배분, 신공장, 생산효율, 캐파계획, 기술로드맵, 생산용량, Digital Twin, 배터리, 합작회사, 라인 전환, 수요 배분, 가동률, JV, HSBMA, 이차전지]
related: []
priority: normal
domain: D07
section: D07-09.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 789
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-09. Initial Manufacturing Footprint OI Seeds

## OI-SEED-D07-001 — Global Capacity Digital Twin

```yaml
seed_id: OI-SEED-D07-001
title: Global Battery Capacity Digital Twin

strategy:
  - Replace static GWh tables with line-level qualified capacity

needed_capability:
  - Design capacity
  - Installed capacity
  - Customer-qualified capacity
  - Available capacity
  - Actual production
  - Utilization and yield
  - Maintenance and conversion status

expected_kpi:
  - Capacity forecast error
  - Demand–capacity mismatch
  - Idle capacity
  - Customer allocation time

priority: VERY_HIGH
```

---

## OI-SEED-D07-002 — JV Capacity Governance

```yaml
seed_id: OI-SEED-D07-002
title: Joint-Venture Capacity and Ownership Governance

target:
  - HSBMA
  - China joint ventures
  - Future customer JVs

needed_capability:
  - Gross and attributable capacity separation
  - Consolidation-status history
  - Ownership effective dates
  - Partner approval rights
  - Customer-linked production constraints

expected_kpi:
  - Capacity-report reconciliation time
  - Double-counted capacity
  - Ownership-data error

priority: HIGH
```

---

## OI-SEED-D07-003 — EV·ESS Line Conversion Readiness

```yaml
seed_id: OI-SEED-D07-003
title: EV-to-ESS Line Conversion Readiness Map

strategy:
  - Use underutilized EV capacity for growing ESS demand

needed_capability:
  - Equipment compatibility
  - Chemistry conversion requirement
  - Customer and regulatory qualification
  - Tooling and formation changes
  - Conversion CAPEX and downtime
  - Local-content eligibility

expected_kpi:
  - Conversion lead time
  - Reused equipment ratio
  - Capacity utilization
  - Conversion investment

priority: VERY_HIGH
```

---

## OI-SEED-D07-004 — Cross-Plant Demand Allocation

```yaml
seed_id: OI-SEED-D07-004
title: Customer Demand–Plant Allocation Optimizer

needed_capability:
  - Customer qualification constraints
  - Logistics cost
  - Local-content rules
  - Capacity and yield
  - Tariff and currency
  - Product-switching cost
  - Supply disruption probability

expected_kpi:
  - On-time delivery
  - Capacity utilization
  - Logistics cost
  - Unserved demand
  - Customer concentration risk

priority: VERY_HIGH
```

---

## OI-SEED-D07-005 — Ramp-Up Learning Transfer

```yaml
seed_id: OI-SEED-D07-005
title: Iváncsa·Yancheng·HSBMA Ramp-Up Learning Transfer

strategy:
  - Reuse verified ramp-up solutions across new factories

target_plants:
  - Ivancsa
  - Yancheng 3
  - HSBMA
  - SK On Tennessee

needed_capability:
  - Problem–cause–action–validation database
  - Equipment normalization
  - Product and material context
  - Local workforce learning
  - Supplier qualification history

expected_kpi:
  - Time to stable output
  - Ramp FPY
  - Repeated launch defects
  - Engineering response time

priority: VERY_HIGH
```

---
