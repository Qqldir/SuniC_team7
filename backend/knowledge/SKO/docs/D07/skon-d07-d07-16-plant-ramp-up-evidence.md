---
id: skon-d07-d07-16-plant-ramp-up-evidence
title: Plant Ramp-Up Evidence
summary: 배터리 공장의 증설 단계(R0-R7)와 세산·코마롬·얀청·테네시 등 주요 생산거점의 현재 가동 상황을 정의·추적하는 프레임워크.
tags: [d07, footprint, schema]
keywords: [배터리, 공장 현황, 생산개시, 용량 확대, 기술이전, 생산거점, SOP, 고객승인, GWh, 라인 가동, 공장 증설, ramp-up, 가동률, Seosan, Yancheng, Tennessee, capacity, 고객 승인]
related: []
priority: normal
domain: D07
section: D07-16.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 876
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-16. Plant Ramp-Up Evidence

## 16.1 Ramp Status Framework

```yaml
plant_ramp_status:

  R0_PRE_CONSTRUCTION:
    - Site and investment plan

  R1_CONSTRUCTION:
    - Building and equipment installation

  R2_COMPLETED_PRE_SOP:
    - Facility completed
    - Commercial production not started

  R3_SOP_STARTED:
    - Initial commercial production

  R4_CUSTOMER_RAMP:
    - Customer-approved output increasing

  R5_PARTIAL_CAPACITY:
    - Some design capacity is operational

  R6_STABLE_SERIAL_PRODUCTION:
    - Sustained qualified production

  R7_FULL_DESIGN_CAPACITY:
    - Full design capacity reached

  control:
    - SOP does not equal full capacity
    - Building completion does not equal customer qualification
```

---

## 16.2 Plant Ramp Snapshot

```yaml
plant_ramp_snapshot:

  Seosan:
    stage: R6_STABLE_SERIAL_PRODUCTION
    exact_utilization: NOT_DISCLOSED

  Komarom_1:
    stage: R6_STABLE_SERIAL_PRODUCTION
    exact_utilization: NOT_DISCLOSED

  Komarom_2:
    stage: R6_STABLE_SERIAL_PRODUCTION
    exact_utilization: NOT_DISCLOSED

  Ivancsa:
    stage: R5_PARTIAL_CAPACITY
    design_capacity_gwh: 30
    full_capacity_date: UNRESOLVED

  Yancheng_1_2:
    stage: R6_OR_R5_UNRESOLVED
    plant_level_utilization: NOT_DISCLOSED

  Yancheng_3:
    stage: R5_PARTIAL_CAPACITY
    full_capacity_date: UNRESOLVED

  SKBA_Commerce:
    stage: R6_WITH_PRODUCT_MIX_REVALIDATION
    current_customer_mix: UNRESOLVED

  HSBMA:
    stage: R3_SOP_STARTED_TO_R4_CUSTOMER_RAMP
    first_confirmed_vehicle: IONIQ_9

  Tennessee:
    stage: R2_PRE_SOP_PREPARATION
    target_sop: 2028
```

HSBMA의 상업생산 개시는 확인됐지만, 35GWh 전체 가동이나 정상수율은 공개되지 않았다. Tennessee는 운영체계와 인력을 준비 중이며 2028년 생산개시가 목표다. ([현대뉴스][8])

---

## 16.3 Ramp Evidence Record

```yaml
plant_ramp_evidence_schema:

  plant_id: required
  ramp_event_id: required

  event_type:
    - Construction start
    - Equipment installation
    - Completion
    - Trial production
    - Commercial production start
    - Customer approval
    - Partial capacity
    - Full capacity

  effective_date: required

  capacity:
    - Installed
    - Qualified
    - Available
    - Actual output

  quality:
    - FPY
    - Customer reject
    - Grade distribution
    - Safety qualification

  operations:
    - Workforce
    - Equipment availability
    - Material approval
    - Supplier localization

  source_ids:
    required: true
```

---

## 16.4 Ramp-Up Learning Priority

```yaml
ramp_learning_priority:

  source_plants:
    - Ivancsa
    - Yancheng_3
    - HSBMA

  target_plant:
    - SK_On_Tennessee

  transferable_knowledge:
    - Equipment installation issue
    - MES and genealogy commissioning
    - Initial material qualification
    - Formation bottleneck
    - Customer approval
    - Workforce certification

  non_transferable_without_validation:
    - Numeric recipe
    - Customer acceptance limit
    - Chemistry-specific formation
    - Equipment-specific control setting
```

---
