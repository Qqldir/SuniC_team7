---
id: skon-d06-d06-58-manufacturing-graph-query-templates
title: Manufacturing Graph Query Templates
summary: "배터리 제조 과정에서 제품 추적, 불량 원인, 공정 변수, 설비 이력 등을 조회하는 그래프 쿼리 템플릿 11개"
tags: [d06, process, schema]
keywords: [배터리 제조, 공정추적, 불량분석, 설비정지, Cell 계보, 근인분석, 트레이서빌리티, 제조공정, 제품 추적, Cell Genealogy, 공정변수, 불량 원인, 설비 다운타임, OEE, 품질 특성, Graph Query]
related: []
priority: normal
domain: D06
section: D06-58.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1877
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-58. Manufacturing Graph Query Templates

## GQ-D06-001 — End-to-End Process Route

```yaml
query_id: GQ-D06-001
natural_language: 특정 배터리 제품의 전체 제조공정을 순서대로 보여줘.

start_nodes:
  - USER_SELECTED_PRODUCT

traversals:
  - USES_CELL_TECHNOLOGY
  - MANUFACTURED_BY_PROCESS
  - FOLLOWED_BY
  - PRODUCES_INTERMEDIATE
  - INSPECTED_BY
```

## GQ-D06-002 — Cell Genealogy

```yaml
query_id: GQ-D06-002
natural_language: 특정 Cell이 어떤 소재·Roll·설비를 거쳤는지 보여줘.

start_nodes:
  - CELL_SERIAL

traversals:
  - CREATED_FROM_STACK
  - CONTAINS_ELECTRODE
  - CUT_FROM_ROLL
  - COATED_FROM_SLURRY
  - USED_MATERIAL_LOT
  - PROCESSED_BY_EQUIPMENT
```

## GQ-D06-003 — Affected Population

```yaml
query_id: GQ-D06-003
natural_language: 특정 소재 Lot나 설비이상으로 영향받은 제품을 계산해줘.

start_nodes:
  - MATERIAL_LOT_OR_EQUIPMENT_EVENT

traversals:
  - CONSUMED_BY_BATCH
  - PRODUCED_ROLL
  - CUT_INTO_ELECTRODE
  - ASSEMBLED_INTO_CELL
  - INSTALLED_IN_MODULE_OR_PACK
```

## GQ-D06-004 — Process Parameters

```yaml
query_id: GQ-D06-004
natural_language: 특정 공정의 핵심 공정변수와 품질특성을 보여줘.

start_nodes:
  - USER_SELECTED_PROCESS

traversals:
  - HAS_CPP
  - CONTROLS_CQA
  - MAY_GENERATE_DEFECT
  - INSPECTED_BY
```

## GQ-D06-005 — Defect Origin

```yaml
query_id: GQ-D06-005
natural_language: 특정 불량의 발생공정과 검출공정을 구분해줘.

start_nodes:
  - USER_SELECTED_DEFECT

traversals:
  - POSSIBLY_ORIGINATED_AT
  - DETECTED_AT
  - HAS_OBSERVABLE_SIGNAL
  - HAS_POTENTIAL_EFFECT

answer_control:
  - Confirmed and suspected origins separated
```

## GQ-D06-006 — Formation Anomaly

```yaml
query_id: GQ-D06-006
natural_language: 특정 포메이션 이상곡선의 상류 원인후보를 보여줘.

start_nodes:
  - FORMATION_EVENT

traversals:
  - HAS_CURVE_FEATURE
  - RELATED_TO_WETTING
  - RELATED_TO_WELD
  - RELATED_TO_STACK
  - RELATED_TO_MATERIAL
```

## GQ-D06-007 — Aging Release

```yaml
query_id: GQ-D06-007
natural_language: 특정 셀이 에이징 연장 또는 Release된 근거를 보여줘.

start_nodes:
  - CELL_SERIAL

traversals:
  - HAS_AGING_RECORD
  - HAS_OCV_DECAY
  - HAS_SWELLING
  - HAS_RISK_SCORE
  - HAS_DISPOSITION
```

## GQ-D06-008 — Cell Grade Matching

```yaml
query_id: GQ-D06-008
natural_language: 특정 Module이나 Pack에 배정된 Cell의 매칭근거를 보여줘.

start_nodes:
  - MODULE_OR_PACK_SERIAL

traversals:
  - CONTAINS_CELL
  - HAS_CAPACITY_GRADE
  - HAS_RESISTANCE_GRADE
  - HAS_GENEALOGY
  - MATCHED_BY_RULE
```

## GQ-D06-009 — Coordinate Scrap

```yaml
query_id: GQ-D06-009
natural_language: 전극 Roll의 국부결함이 어떤 Cell에 들어갔는지 계산해줘.

start_nodes:
  - ROLL_DEFECT_COORDINATE

traversals:
  - TRANSFORMED_DURING_SLITTING
  - CUT_INTO_ELECTRODE
  - ASSEMBLED_INTO_STACK
  - ASSEMBLED_INTO_CELL
```

## GQ-D06-010 — Equipment Downtime

```yaml
query_id: GQ-D06-010
natural_language: 설비정지의 직접원인과 최종 Root Cause를 보여줘.

start_nodes:
  - DOWNTIME_EVENT

traversals:
  - HAS_INITIAL_REASON
  - CAUSED_BY_FAILURE
  - AFFECTED_WIP
  - CREATED_SCRAP
  - RESOLVED_BY_ACTION
```

## GQ-D06-011 — OEE Loss

```yaml
query_id: GQ-D06-011
natural_language: 특정 라인의 OEE 손실을 가동·속도·품질로 분해해줘.

start_nodes:
  - LINE_AND_PERIOD

traversals:
  - HAS_AVAILABILITY_LOSS
  - HAS_PERFORMANCE_LOSS
  - HAS_QUALITY_LOSS
  - HAS_CHANGEOVER_LOSS
```

## GQ-D06-012 — Yield Waterfall

```yaml
query_id: GQ-D06-012
natural_language: 원료부터 Pack까지의 수율 Waterfall을 보여줘.

start_nodes:
  - PRODUCT_LINE_AND_PERIOD

traversals:
  - HAS_PROCESS_INPUT
  - HAS_FIRST_PASS_GOOD
  - HAS_REWORK
  - HAS_SCRAP
  - CALCULATES_RTY
```

## GQ-D06-013 — Value-Added Scrap

```yaml
query_id: GQ-D06-013
natural_language: 누적가치가 가장 큰 Scrap의 발생·검출공정을 보여줘.

filters:
  - HIGH_ACCUMULATED_VALUE
  - LATE_DETECTION

traversals:
  - ORIGINATED_AT
  - DETECTED_AT
  - ACCUMULATED_PROCESS_COST
  - HAS_CONTAINMENT_POPULATION
```

## GQ-D06-014 — Bottleneck·WIP

```yaml
query_id: GQ-D06-014
natural_language: 현재와 향후 병목공정을 보여줘.

start_nodes:
  - PLANT_OR_LINE

traversals:
  - HAS_WIP
  - HAS_QUEUE_GROWTH
  - HAS_CAPACITY
  - HAS_FAILURE_RISK
  - HAS_QUALITY_HOLD
```

## GQ-D06-015 — Energy

```yaml
query_id: GQ-D06-015
natural_language: 공정별 합격품당 에너지와 손실원인을 보여줘.

start_nodes:
  - PLANT_LINE_PROCESS

traversals:
  - CONSUMES_UTILITY
  - ALLOCATED_TO_PRODUCT
  - ALLOCATED_TO_SCRAP
  - HAS_IDLE_LOSS
  - HAS_PEAK_DEMAND
```

## GQ-D06-016 — Digital Twin

```yaml
query_id: GQ-D06-016
natural_language: 특정 Twin의 모델범위와 검증상태를 보여줘.

start_nodes:
  - DIGITAL_TWIN_ID

traversals:
  - REPRESENTS_PROCESS
  - USES_ACTUAL_DATA
  - HAS_MODEL_VERSION
  - VALIDATED_AGAINST
  - APPROVED_FOR_USE_CASE
```

## GQ-D06-017 — Ramp-Up Learning

```yaml
query_id: GQ-D06-017
natural_language: 신규 라인의 반복문제와 검증된 해결책을 보여줘.

start_nodes:
  - RAMP_UP_LINE

traversals:
  - EXPERIENCED_PROBLEM
  - HAS_CONFIRMED_CAUSE
  - RESOLVED_BY
  - VALIDATED_BY
  - REUSED_AT_OTHER_LINE
```

## GQ-D06-018 — Cross-Plant Transfer

```yaml
query_id: GQ-D06-018
natural_language: 기준공장 Recipe를 대상공장으로 이전하기 위한 차이를 보여줘.

start_nodes:
  - SOURCE_RECIPE
  - TARGET_LINE

traversals:
  - HAS_PROCESS_INTENT
  - DIFFERS_IN_EQUIPMENT
  - DIFFERS_IN_MATERIAL
  - REQUIRES_NORMALIZATION
  - REQUIRES_QUALIFICATION
```

## GQ-D06-019 — OT·AI Governance

```yaml
query_id: GQ-D06-019
natural_language: 제조 AI나 OT 변경이 승인된 상태인지 보여줘.

start_nodes:
  - MODEL_OR_CONTROLLER_CHANGE

traversals:
  - HAS_VERSION
  - APPROVED_BY
  - VALIDATED_FOR_PRODUCT
  - HAS_ROLLBACK
  - HAS_CYBERSECURITY_SIGNATURE
```

## GQ-D06-020 — OI Recommendation

```yaml
query_id: GQ-D06-020
natural_language: 특정 제조 Pain Point에 적합한 외부기술과 협력방식을 추천해줘.

start_nodes:
  - USER_SELECTED_PAIN_POINT

traversals:
  - REQUIRES_CAPABILITY
  - MATCHED_TO_EXTERNAL_TECHNOLOGY
  - MATCHED_TO_PARTNER_TYPE
  - GENERATES_OI_SEED
  - HAS_EXPECTED_KPI
```

---
