---
id: skon-d07-d07-15-customer-linked-capacity
title: Customer-Linked Capacity
summary: "고객별 배터리 캐파 배정 현황, 생산거점별 배치, 고객의존도 위험도를 추적하는 데이터 기록"
tags: [d07, footprint, schema]
keywords: [고객별 용량 배정, 차종별 납품 계약, D07 생산거점, 공장 의존도, OEM 계약, 배터리 GWh, HSBMA GA, 용량 할당 스키마, 고객집중도지표, 고객배정, 공장캐파, GWh, 고객집중도, 고객의존도, 생산거점, OEM, 대체공장]
related: []
priority: normal
domain: D07
section: D07-15.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 897
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-15. Customer-Linked Capacity

## 15.1 Customer Capacity Record

```yaml
customer_linked_capacity_schema:

  mapping_id: required
  plant_id: required
  customer_id: required

  product:
    - Vehicle model
    - Vehicle platform
    - ESS solution
    - Generic OEM program
    - Unresolved

  capacity:
    - Dedicated capacity
    - Shared capacity
    - Maximum contract volume
    - Customer-qualified capacity
    - Unresolved

  mapping_level:
    - DIRECT_SITE_MODEL
    - DIRECT_SITE_OEM
    - DIRECT_COMPANY_MODEL
    - ANALYST_INFERENCE
    - UNRESOLVED

  effective_period:
    required: true

  exclusivity:
    - EXCLUSIVE
    - PREFERRED
    - SHARED
    - UNRESOLVED

  alternative_site:
    - Qualified
    - Qualification required
    - Contractually restricted
    - Unresolved

  source_ids:
    required: true
```

---

## 15.2 Confirmed Customer-Linked Records

```yaml
confirmed_customer_linked_records:

  - mapping_id: MAP-D07-US-001
    plant_id: PLANT-D07-US-GA1_GA2
    customer: Ford
    vehicle: F_150_Lightning
    mapping_level: DIRECT_SITE_MODEL
    status: HISTORICAL_CONFIRMED_CURRENT_REVALIDATION_REQUIRED
    dedicated_capacity_gwh: UNRESOLVED
    source_ids:
      - SRC-GOV-D07-008

  - mapping_id: MAP-D07-US-002
    plant_id: PLANT-D07-US-GA1_GA2
    customer: Volkswagen
    vehicle: ID_4
    mapping_level: DIRECT_SITE_MODEL
    status: HISTORICAL_CONFIRMED_CURRENT_REVALIDATION_REQUIRED
    dedicated_capacity_gwh: UNRESOLVED
    source_ids:
      - SRC-GOV-D07-008

  - mapping_id: MAP-D07-US-003
    plant_id: PLANT-D07-US-HSBMA
    customer: Hyundai_Motor_Group
    product_scope:
      - Hyundai_EV
      - Kia_EV
      - Genesis_EV
    mapping_level: DIRECT_SITE_OEM
    status: CURRENT_CONFIRMED
    dedicated_capacity_gwh: UNRESOLVED
    gross_plant_capacity_gwh: 35
    source_ids:
      - SRC-OFF-D07-005
      - SRC-OFF-D07-009

  - mapping_id: MAP-D07-US-004
    plant_id: PLANT-D07-US-HSBMA
    customer: Hyundai
    vehicle: IONIQ_9
    mapping_level: DIRECT_SITE_MODEL
    status: INITIAL_PRODUCTION_CONFIRMED
    dedicated_capacity_gwh: UNRESOLVED
    source_ids:
      - SRC-OFF-D07-009
```

SKBA의 약 22GWh와 HSBMA의 35GWh는 공장 총 Capacity이지, 각 차종에 배정된 계약 Capacity가 아니다. ([켐프 주지사 사무실][3])

---

## 15.3 Customer Concentration Metrics

```yaml
customer_concentration_metrics:

  plant_customer_share:
    formula: customer_allocated_capacity / qualified_plant_capacity

  plant_top_customer_dependency:
    formula: largest_customer_output / plant_total_output

  customer_single_site_dependency:
    formula: customer_volume_from_largest_site / total_customer_volume

  alternative_qualified_capacity:
    definition: >
      다른 공장에서 고객승인을 받아 실제 전환 가능한 Capacity

  customer_requalification_lead_time:
    definition: >
      대체공장에서 해당 제품을 생산하기 위해 필요한 검증기간

  unavailable_public_fields:
    - Contract allocation
    - Minimum purchase commitment
    - Customer-specific line capacity
    - Exclusivity
    - Requalification time
```

---
