---
id: skon-d07-d07-33-plant-capacity-graph-query-templates
title: Plant·Capacity Graph Query Templates
summary: "공장별 생산능력, 고객 공급 계약, 양산 준비 상황을 조회하는 SK온 그래프 쿼리 템플릿 12종."
tags: [d07, footprint, schema]
keywords: [공장, 생산능력, 캐파, 고객계약, JV, 생산거점, 고객 공급, 설계능력, 양산, HSBMA, 그래프쿼리, 고객할당, 계약관리, EV·ESS, 양산준비]
related: []
priority: normal
domain: D07
section: D07-33.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1589
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-33. Plant·Capacity Graph Query Templates

```yaml
graph_query_status:
  query_design: ACCEPTED
  source_binding: PARTIAL
  plant_level_operational_data: PENDING
```

## GQ-D07-001 — 현재 공장 목록

```yaml
query_id: GQ-D07-001
natural_language: 현재 SK온이 보유·운영하거나 지분을 가진 생산거점을 보여줘.

filters:
  - reference_date
  - ownership_status
  - transferred_assets_excluded

traversals:
  - COMPANY_OWNS
  - COMPANY_CONTROLS
  - COMPANY_PARTICIPATES_IN_JV
```

## GQ-D07-002 — Capacity 유형별 합계

```yaml
query_id: GQ-D07-002
natural_language: 생산능력을 연결·JV Gross·미래설계·양도자산으로 나눠 보여줘.

traversals:
  - HAS_CAPACITY_RECORD
  - HAS_CAPACITY_TYPE
  - INCLUDED_IN_SCOPE
```

## GQ-D07-003 — Capacity 시점 비교

```yaml
query_id: GQ-D07-003
natural_language: 2024년부터 현재까지 Capacity 변화를 Event별로 설명해줘.

traversals:
  - HAS_CAPACITY_EVENT
  - EFFECTIVE_FROM
  - INCREASED_BY
  - DECREASED_BY
  - TRANSFERRED_TO
```

## GQ-D07-004 — 공식값과 분석값

```yaml
query_id: GQ-D07-004
natural_language: 공식 공시 Capacity와 Analyst Pro Forma를 분리해줘.

traversals:
  - REPORTED_IN
  - DERIVED_FROM
  - HAS_EVIDENCE_LEVEL
```

## GQ-D07-005 — 공장별 고객

```yaml
query_id: GQ-D07-005
natural_language: 특정 공장에 직접 연결된 고객·차종을 보여줘.

traversals:
  - SUPPLIES_CUSTOMER
  - SUPPLIES_MODEL
  - HAS_MAPPING_LEVEL
  - VALID_DURING

answer_control:
  - Historical and current mappings separated
```

## GQ-D07-006 — 고객계약의 생산공장

```yaml
query_id: GQ-D07-006
natural_language: Nissan 또는 Slate 계약이 어느 공장에 배정됐는지 보여줘.

traversals:
  - CUSTOMER_HAS_SUPPLY_AGREEMENT
  - REQUIRES_US_PRODUCTION
  - NOMINATED_TO_PLANT

answer_control:
  - Return UNRESOLVED when no plant nomination exists
```

## GQ-D07-007 — HSBMA Capacity

```yaml
query_id: GQ-D07-007
natural_language: HSBMA의 총설계능력·지분·고객과 Ramp 상태를 보여줘.

start_nodes:
  - PLANT-D07-US-HSBMA

traversals:
  - HAS_JV_OWNER
  - HAS_GROSS_CAPACITY
  - SUPPLIES_CUSTOMER
  - HAS_RAMP_STAGE
```

## GQ-D07-008 — Tennessee 준비상태

```yaml
query_id: GQ-D07-008
natural_language: Tennessee가 2028년 양산 전까지 해결해야 할 과제를 보여줘.

traversals:
  - HAS_PRE_SOP_GAP
  - REQUIRES_PRODUCT_NOMINATION
  - REQUIRES_CUSTOMER_QUALIFICATION
  - REQUIRES_RESOURCE
```

## GQ-D07-009 — Qualified Capacity

```yaml
query_id: GQ-D07-009
natural_language: 특정 공장의 설계 Capacity가 고객출하 Capacity로 줄어드는 과정을 보여줘.

traversals:
  - HAS_DESIGN_CAPACITY
  - HAS_INSTALLED_CAPACITY
  - HAS_AVAILABLE_CAPACITY
  - HAS_CUSTOMER_QUALIFIED_CAPACITY
  - HAS_GOOD_OUTPUT_CAPACITY
```

## GQ-D07-010 — EV→ESS 전환

```yaml
query_id: GQ-D07-010
natural_language: EV Line을 ESS로 전환할 때 필요한 변경사항을 보여줘.

traversals:
  - HAS_CURRENT_PRODUCT
  - TARGETS_NEW_PRODUCT
  - REQUIRES_EQUIPMENT_CHANGE
  - REQUIRES_REQUALIFICATION
  - REQUIRES_POLICY_CHECK
```

## GQ-D07-011 — 대체공장

```yaml
query_id: GQ-D07-011
natural_language: 특정 고객제품의 대체 생산공장을 보여줘.

traversals:
  - TECHNICALLY_COMPATIBLE_WITH
  - CUSTOMER_QUALIFIED_FOR
  - COMMERCIALLY_AVAILABLE_FOR
  - COMPLIANT_WITH_ORIGIN_RULE
```

## GQ-D07-012 — 고객집중도

```yaml
query_id: GQ-D07-012
natural_language: 공장별 주요 고객의존도와 단일 Site 위험을 보여줘.

traversals:
  - PLANT_ALLOCATED_TO_CUSTOMER
  - CUSTOMER_VOLUME_SHARE
  - HAS_ALTERNATIVE_SITE
```

## GQ-D07-013 — Ramp-Up

```yaml
query_id: GQ-D07-013
natural_language: 부분가동·SOP·정상양산 단계에 있는 공장을 분류해줘.

traversals:
  - HAS_RAMP_EVENT
  - HAS_RAMP_STAGE
  - HAS_QUALIFIED_CAPACITY
```

## GQ-D07-014 — 정책적격 Capacity

```yaml
query_id: GQ-D07-014
natural_language: 미국 생산량 중 정책·세액공제 적격 가능 Capacity를 보여줘.

traversals:
  - PRODUCED_IN_COUNTRY
  - USES_MATERIAL_ORIGIN
  - SUBJECT_TO_PFE_TEST
  - ELIGIBLE_FOR_INCENTIVE
```

## GQ-D07-015 — 공장 Economics

```yaml
query_id: GQ-D07-015
natural_language: 공장별 고정비 흡수와 Break-Even 생산량을 비교해줘.

traversals:
  - HAS_FIXED_COST
  - HAS_GOOD_OUTPUT
  - RECEIVES_INCENTIVE
  - INCURS_LOGISTICS_COST
  - HAS_BREAK_EVEN_UTILIZATION
```

## GQ-D07-016 — Resource Constraint

```yaml
query_id: GQ-D07-016
natural_language: Utility·인력·인허가로 제한되는 Capacity를 보여줘.

traversals:
  - REQUIRES_ELECTRICITY
  - REQUIRES_WATER
  - REQUIRES_QUALIFIED_WORKFORCE
  - LIMITED_BY_PERMIT
```

## GQ-D07-017 — 공급차질 Stress Test

```yaml
query_id: GQ-D07-017
natural_language: 특정 공장 중단 시 복구 가능한 고객수요를 계산해줘.

traversals:
  - DISRUPTION_AFFECTS
  - HAS_ALTERNATIVE_SITE
  - HAS_AVAILABLE_CAPACITY
  - REQUIRES_REQUALIFICATION
  - RECOVERS_DEMAND
```

## GQ-D07-018 — OI 추천

```yaml
query_id: GQ-D07-018
natural_language: 특정 Footprint Pain Point에 맞는 OI 과제를 추천해줘.

traversals:
  - PLANT_HAS_PAIN_POINT
  - PAIN_POINT_REQUIRES_CAPABILITY
  - CAPABILITY_GENERATES_OI_SEED
  - OI_SEED_HAS_EXPECTED_KPI
```

---
