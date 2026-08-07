---
id: skon-d07-d07-30-new-footprint-oi-seeds
title: New Footprint OI Seeds
summary: "D07 거점의 용량 추적, 세금공제, 관세 준수, 계약-생산 연결, 물류 효율화를 위한 6가지 전략 과제"
tags: [d07, footprint, oi-seed, schema]
keywords: [OI-SEED, 용량 이벤트, 배터리 세금공제, 45X credit, 관세 규칙, 계약-용량 대응, 물류 최적화, 공급망, D07, 용량 계획, 세금공제 자격, 관세·현지화, 계약-수급 연결, 배터리 생산, Capacity Event]
related: []
priority: normal
domain: D07
section: D07-30.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1227
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-30. New Footprint OI Seeds

## OI-SEED-D07-014 — Capacity Event Ledger

```yaml
seed_id: OI-SEED-D07-014
title: Real-Time Capacity Event Ledger

strategy:
  - Keep ownership, ramp and capacity snapshots synchronized

needed_capability:
  - Effective-date capacity events
  - Consolidation history
  - Design and normalized capacity separation
  - JV and transferred-asset ledger
  - Regulatory filing reconciliation

expected_kpi:
  - Capacity-report discrepancy
  - Data update latency
  - Double-counted GWh
  - Manual reconciliation time

priority: CRITICAL
```

---

## OI-SEED-D07-015 — 45X·PFE Eligibility Twin

```yaml
seed_id: OI-SEED-D07-015
title: U.S. Battery Tax-Credit Eligibility Twin

strategy:
  - Predict credit-eligible output before production allocation

needed_capability:
  - Cell and module production records
  - Capacity substantiation
  - Supplier ownership
  - Material origin
  - PFE material-assistance ratio
  - Sale and taxpayer structure

expected_kpi:
  - Credit-eligible output
  - Disallowed credit risk
  - Supplier remediation time
  - Audit response time

priority: CRITICAL
```

---

## OI-SEED-D07-016 — Tariff·Local-Content Rules Engine

```yaml
seed_id: OI-SEED-D07-016
title: Battery Tariff and Local-Content Rules Engine

strategy:
  - Select plants and suppliers based on current trade rules

needed_capability:
  - HTS classification
  - Product and material origin
  - Section 301 tariff
  - Vehicle battery ledger
  - EU battery compliance
  - Effective-date rule history

expected_kpi:
  - Tariff exposure
  - Compliance exception
  - Origin-data completeness
  - Allocation decision time

priority: VERY_HIGH
```

---

## OI-SEED-D07-017 — Contract-to-Capacity Demand Bridge

```yaml
seed_id: OI-SEED-D07-017
title: Customer Contract-to-Capacity Bridge

strategy:
  - Convert contract totals into time-phased plant requirements

target_programs:
  - Hyundai_Motor_Group
  - Slate
  - Nissan
  - GRIDON

needed_capability:
  - Annual delivery profile
  - Cell specification
  - Plant nomination
  - Customer approval
  - Option volume
  - Program delay and cancellation scenario

expected_kpi:
  - Unallocated contract demand
  - Contract coverage
  - Capacity shortfall
  - Excess committed capacity

priority: CRITICAL
```

---

## OI-SEED-D07-018 — Logistics Proximity Optimizer

```yaml
seed_id: OI-SEED-D07-018
title: Cell-to-Customer Logistics Proximity Optimizer

strategy:
  - Reduce inventory while preserving supply resilience

needed_capability:
  - Plant and customer schedules
  - Transit lane
  - Safety stock
  - Hazardous-goods constraints
  - Alternative route
  - Emergency freight

expected_kpi:
  - Transit time
  - Inventory days
  - Freight cost
  - Expedite frequency
  - Delivery disruption

priority: HIGH
```

---

## OI-SEED-D07-019 — Utility·Labor Constraint Twin

```yaml
seed_id: OI-SEED-D07-019
title: Plant Utility and Workforce Constraint Twin

strategy:
  - Prevent nominal GWh from exceeding site resources

needed_capability:
  - Power and water contract
  - Dry-room base load
  - Workforce qualification
  - Maintenance coverage
  - Environmental permit limit
  - Ramp production plan

expected_kpi:
  - Resource-constrained GWh
  - Utility excursion
  - Unfilled critical role
  - Production loss
  - Environmental-capacity headroom

priority: VERY_HIGH
```

---

## OI-SEED-D07-020 — Incentive Covenant Tracker

```yaml
seed_id: OI-SEED-D07-020
title: Manufacturing Incentive Covenant Tracker

strategy:
  - Protect incentives and prevent clawback

needed_capability:
  - Investment commitment
  - Employment commitment
  - Production milestone
  - Compliance period
  - Guarantee and support agreement
  - Evidence package

expected_kpi:
  - Covenant compliance
  - Incentive at risk
  - Missing evidence
  - Potential clawback

priority: HIGH
```

---

## OI-SEED-D07-021 — Footprint Economics Scenario Engine

```yaml
seed_id: OI-SEED-D07-021
title: Global Footprint Economics Scenario Engine

strategy:
  - Allocate demand based on true economic capacity

needed_capability:
  - Qualified good output
  - Fixed and variable cost
  - 45X and incentive eligibility
  - Tariff and logistics
  - Conversion CAPEX
  - JV attribution
  - Customer constraints

expected_kpi:
  - Contribution margin by plant
  - Break-even utilization
  - Fixed-cost exposure
  - Allocation value
  - Revenue at risk

priority: CRITICAL
```

---
