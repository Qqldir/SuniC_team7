---
id: skon-d07-d07-35-capacity-data-quality-audit
title: Capacity Data Quality Audit
summary: "D07 생산거점의 용량 데이터에 어떤 품질 이슈가 있으며, 각 이슈의 심각도와 미해결 항목이 무엇인지 파악할 수 있는 감시 보고서."
tags: [d07, footprint, core-candidate, schema, "xref:d11", "xref:d12", "xref:d08", "xref:d09"]
keywords: [D07, 배터리 생산용량, 데이터 품질, 라인 가시성, 고객 매핑, JV 제약, 가동률, 플랜트 캐패시티, 적격용량, 생산 거점, Registry Audit, 생산라인 가시성, 고객자격용량, JV 펀지빌리티, D07 생산거점, HSBMA, 플랜트 용량]
related: []
priority: critical
domain: D07
section: D07-35.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1361
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-35. Capacity Data Quality Audit

## 35.1 Registry Audit

```yaml
d07_registry_audit:

  source_records:
    canonical_total: 19
    deprecated_aliases:
      - SRC-OFF-D07-009

  plant_entities:
    current_or_pending_total: 13
    historical_transferred_total: 2
    total: 15

  site_cluster_entities:
    total: 1
    entities:
      - SITE-D07-US-COMMERCE

  ownership_events:
    total: 3

  capacity_events:
    total: 8

  confirmed_customer_mappings:
    total: 4

  risk_entities:
    total: 6

  pain_point_entities:
    total: 10

  oi_seed_entities:
    total: 21

  chunks:
    total: 20

  graph_queries:
    total: 18

  core_relationship_triples:
    total: 32
```

---

## DQ-D07-FINAL-001 — 현재 공식 연결 Capacity

```yaml
issue_id: DQ-D07-FINAL-001
issue: Post-restructuring official consolidated capacity is unavailable

known:
  q1_2026_official_gwh: 97.4
  kentucky_transfer: confirmed
  hsbma_commercial_production: confirmed

unknown:
  - Q2 normalized plant capacity table
  - Post-Q1 Ivancsa ramp
  - Post-Q1 Yancheng 3 ramp
  - Restated consolidated total

severity: CRITICAL

current_handling:
  official_current_total: UNRESOLVED
  analyst_pro_forma_gwh: 94.3
```

---

## DQ-D07-FINAL-002 — Plant·Line Visibility

```yaml
issue_id: DQ-D07-FINAL-002
issue: Physical line count and line-level capacity are not disclosed

missing:
  - Electrode line count
  - Cell assembly line count
  - Formation channel capacity
  - Module and pack lines
  - Customer allocation by line
  - EV and ESS line designation

severity: CRITICAL

control:
  - Do not invent line IDs
  - Use plant or site-cluster aggregate
```

---

## DQ-D07-FINAL-003 — Customer-Qualified Capacity

```yaml
issue_id: DQ-D07-FINAL-003
issue: Plant gross capacity cannot be converted to customer-qualified capacity

affected:
  - HSBMA
  - Ivancsa
  - Yancheng 3
  - SKBA Commerce
  - Tennessee

missing:
  - Customer approval
  - Qualified product revision
  - Good-output capacity
  - Annual customer allocation

severity: CRITICAL
```

---

## DQ-D07-FINAL-004 — Customer Mapping

```yaml
issue_id: DQ-D07-FINAL-004
issue: Most Europe, China and U.S. contract volumes lack plant nomination

confirmed:
  - Commerce historical F-150 Lightning
  - Commerce historical ID.4
  - HSBMA Hyundai Motor Group
  - HSBMA initial IONIQ 9

unresolved:
  - Nissan production plant
  - Slate production plant
  - GRIDON production plant
  - Europe customer by site
  - China customer by site

severity: VERY_HIGH
```

---

## DQ-D07-FINAL-005 — JV Fungibility

```yaml
issue_id: DQ-D07-FINAL-005
issue: JV physical capacity is not freely allocable SK On capacity

affected:
  - HSBMA
  - Changzhou
  - Huizhou

constraints:
  - Partner rights
  - Customer commitments
  - Accounting scope
  - Contract approval
  - Product qualification

severity: VERY_HIGH
```

---

## DQ-D07-FINAL-006 — 가동률

```yaml
issue_id: DQ-D07-FINAL-006
issue: Only consolidated average utilization is disclosed

available:
  - 2024: 43.8 percent
  - 2025: 48.7 percent
  - 2026 Q1: 36.5 percent

missing:
  - Plant utilization
  - Line utilization
  - Product utilization
  - Good-output utilization

severity: CRITICAL
```

---

## DQ-D07-FINAL-007 — Economics

```yaml
issue_id: DQ-D07-FINAL-007
issue: Plant-level cost and profitability are unavailable

missing:
  - Depreciation by plant
  - Fixed manufacturing cost
  - Utility cost
  - Yield-adjusted variable cost
  - Incentive-eligible output
  - JV attributable economics

severity: VERY_HIGH

dependency:
  - D11 Cost
  - D12 Investment
```

---

## DQ-D07-FINAL-008 — Policy Eligibility

```yaml
issue_id: DQ-D07-FINAL-008
issue: U.S. physical output and policy-eligible output are not reconciled

missing:
  - Material origin
  - Supplier ownership
  - PFE cost ratio
  - Cell and module tax-credit records
  - OEM battery-ledger linkage

severity: VERY_HIGH

dependency:
  - D08 Supply Chain
  - D09 Customer Programs
```

---

## DQ-D07-FINAL-009 — Resource Constraints

```yaml
issue_id: DQ-D07-FINAL-009
issue: Plant resource headroom is unavailable

missing:
  - Electricity capacity
  - Water allocation
  - Dry-room utility limit
  - Critical workforce availability
  - Permit headroom

severity: HIGH
```

---

## 35.2 Release Suitability

```yaml
release_suitability:

  suitable_for:
    - Global footprint understanding
    - Ownership and JV analysis
    - Capacity-definition governance
    - Capacity scenario construction
    - Customer concentration analysis
    - Ramp and resilience planning
    - OI opportunity generation

  not_suitable_for:
    - Claiming current official consolidated capacity
    - Claiming plant-level utilization
    - Calculating plant profitability
    - Assigning contracts to unnamed plants
    - Treating JV capacity as SK On-controlled capacity
    - Certifying alternative-site supply capability
```

---
