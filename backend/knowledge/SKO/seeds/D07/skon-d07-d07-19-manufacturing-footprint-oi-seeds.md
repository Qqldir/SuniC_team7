---
id: skon-d07-d07-19-manufacturing-footprint-oi-seeds
title: Manufacturing Footprint OI Seeds
summary: "배터리 제조 거점의 용량 활용 최적화, 고객 집중도 관리, 리스크 조기 감지를 위해 필요한 5가지 운영 시스템의 설계 전략을 제시하는 문서다."
tags: [d07, footprint, oi-seed, schema]
keywords: [생산 용량 최적화, 고객 집중도 리스크, 설비 전환 평가, 대체 거점 자격화, EV ESS 전환, 캐파시티 계층화, 고객 자격화, 설비 호환성 분석, 배터리, 캐파시티, 생산능력, 고객할당, 고객집중도, ESS, EV, 라인전환, 조기경보, 대체거점]
related: []
priority: normal
domain: D07
section: D07-19.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1394
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-19. Manufacturing Footprint OI Seeds

## OI-SEED-D07-006 — Plant–Line–Customer Knowledge Graph

```yaml
seed_id: OI-SEED-D07-006
title: Plant–Line–Product–Customer Knowledge Graph

strategy:
  - Create a single source of truth for global manufacturing allocation

needed_capability:
  - Plant and line hierarchy
  - Product and chemistry revision
  - Customer qualification
  - Contract-capacity link
  - Effective-date history
  - Ownership and JV constraints

expected_kpi:
  - Unmapped capacity
  - Capacity-report reconciliation time
  - Customer exposure analysis time
  - Allocation-data error

priority: CRITICAL
```

---

## OI-SEED-D07-007 — Qualified Capacity Ledger

```yaml
seed_id: OI-SEED-D07-007
title: Design-to-Qualified Capacity Ledger

strategy:
  - Replace nameplate GWh with decision-ready capacity

capacity_layers:
  - Design capacity
  - Installed capacity
  - Mechanically available capacity
  - Customer-qualified capacity
  - Scheduled capacity
  - Good-output capacity
  - Commercially allocable capacity

expected_kpi:
  - Capacity forecast error
  - Unused qualified capacity
  - Unqualified installed capacity
  - Demand shortfall

priority: CRITICAL
```

---

## OI-SEED-D07-008 — Customer Concentration Early Warning

```yaml
seed_id: OI-SEED-D07-008
title: Customer–Plant Concentration Early Warning

strategy:
  - Detect demand and customer-program risk before utilization drops

needed_capability:
  - Vehicle production forecast
  - Customer order and nomination
  - Plant allocation
  - Program end-of-life
  - Scenario stress test
  - Alternative-customer pipeline

expected_kpi:
  - Top-customer dependence
  - Idle capacity forecast
  - Unallocated capacity
  - Response lead time

priority: VERY_HIGH
```

---

## OI-SEED-D07-009 — Alternative Site Qualification Engine

```yaml
seed_id: OI-SEED-D07-009
title: Alternative Site Qualification Engine

strategy:
  - Convert physical redundancy into customer-qualified redundancy

needed_capability:
  - Product similarity
  - Equipment equivalence
  - Material qualification
  - Customer validation package
  - Regulatory and local-content check
  - Transfer lead-time estimate

expected_kpi:
  - Qualified alternative capacity
  - Requalification lead time
  - Disruption recovery time
  - Single-site customer exposure

priority: VERY_HIGH
```

---

## OI-SEED-D07-010 — EV·ESS Conversion Digital Assessment

```yaml
seed_id: OI-SEED-D07-010
title: EV–ESS Line Conversion Digital Assessment

strategy:
  - Evaluate underutilized capacity without overstating compatibility

needed_capability:
  - Equipment compatibility matrix
  - Chemistry and cell-format difference
  - Formation and inspection modification
  - Customer qualification
  - CAPEX and downtime estimate
  - Incentive and local-content analysis

expected_kpi:
  - Conversion feasibility assessment time
  - Reusable equipment ratio
  - Conversion lead time
  - Converted qualified capacity
  - Conversion CAPEX

priority: VERY_HIGH
```

---

## OI-SEED-D07-011 — HSBMA Ramp Control Tower

```yaml
seed_id: OI-SEED-D07-011
title: HSBMA Customer Ramp Control Tower

strategy:
  - Stabilize new JV production against HMG vehicle demand

target:
  - HSBMA
  - Hyundai, Kia and Genesis U.S. programs

needed_capability:
  - Vehicle build schedule
  - Cell production and yield
  - Customer qualification gate
  - Cell inventory
  - Pack and vehicle-plant logistics
  - Quality containment

expected_kpi:
  - Qualified output
  - HMG delivery adherence
  - Ramp FPY
  - Cell inventory
  - Vehicle production disruption

priority: VERY_HIGH
```

---

## OI-SEED-D07-012 — Tennessee Pre-SOP Readiness Twin

```yaml
seed_id: OI-SEED-D07-012
title: SK On Tennessee Pre-SOP Readiness Twin

strategy:
  - Use the 2026–2028 preparation window to reduce launch risk

needed_capability:
  - Equipment and software baseline
  - Product-scenario comparison
  - EV and ESS market scenarios
  - Utility and workforce readiness
  - Virtual commissioning
  - HSBMA·Ivancsa·Yancheng learning transfer
  - Customer qualification roadmap

expected_kpi:
  - Open launch issue
  - Virtual versus physical commissioning defect
  - Workforce qualification
  - Time to customer-approved output
  - Ramp first-pass yield

priority: VERY_HIGH
```

---

## OI-SEED-D07-013 — Global Footprint Stress Test

```yaml
seed_id: OI-SEED-D07-013
title: Global Battery Footprint Stress Test

strategy:
  - Quantify recoverable supply under disruption

scenarios:
  - Plant shutdown
  - Utility shortage
  - Customer demand cancellation
  - Tariff or local-content change
  - Material embargo
  - JV restriction
  - Shipping disruption
  - Delayed ramp-up

needed_capability:
  - Effective qualified capacity
  - Customer and product mapping
  - Alternative-site status
  - Material and logistics constraints
  - Financial impact

expected_kpi:
  - Recoverable capacity
  - Unserved customer demand
  - Recovery lead time
  - Revenue-at-risk
  - Concentration exposure

priority: VERY_HIGH
```

---
