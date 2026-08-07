---
id: skon-d06-d06-55-cross-plant-recipe-transfer
title: Cross-Plant Recipe Transfer
summary: 한 공장의 배터리 제조 공정 레시피를 다른 공장으로 이전할 때 설비 차이를 고려하여 검증하고 파라미터를 적응시키는 방법론을 설명한다.
tags: [d06, process, schema, table]
keywords: [공정조건 이전, 설비 정규화, 파라미터 분류, 공장 간 검증, Transfer Learning, 공정 의도, 셀 설계, 적응 파라미터, Golden Batch, 배터리 제조, 공정이전, Recipe Transfer, 파라미터 적응, Process Intent, Qualification]
related: []
priority: normal
domain: D06
section: D06-55.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1623
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-55. Cross-Plant Recipe Transfer

## 55.1 Recipe Transfer Principle

배터리 제조의 공정조건은 설비규모, 공정종류와 셀 설계가 바뀌면 동일하게 작동하지 않을 수 있다. 배터리 제조 Transfer Learning 연구도 생산규모, 제조공정과 셀 설계를 지식이전의 주요 차원으로 구분한다. ([ScienceDirect][7])

```yaml
recipe_transfer_policy:

  source_recipe:
    definition: >
      기준공장에서 검증된 공정조건과 품질결과

  target_recipe:
    definition: >
      대상공장의 설비·환경·소재 차이를 반영해 재검증된 공정조건

  prohibited:
    - Copy numeric settings without equipment normalization
    - Transfer model without product and sensor validation
    - Treat same equipment vendor as identical process
    - Remove local qualification

  required:
    - Equivalent process intent
    - Equipment capability mapping
    - Material equivalence
    - Sensor and measurement equivalence
    - Target-line validation
```

---

## 55.2 Transfer Package

```yaml
cross_plant_transfer_package:

  transfer_id: required

  source:
    - Plant
    - Line
    - Equipment
    - Product
    - Product revision
    - Recipe version

  target:
    - Plant
    - Line
    - Equipment
    - Product
    - Product revision

  process_intent:
    - Target intermediate quality
    - Critical quality attributes
    - Critical failure modes
    - Allowed operating window

  source_conditions:
    - Material properties
    - Equipment dimensions
    - Sensor configuration
    - Environmental conditions
    - Process parameters
    - Quality distribution

  target_differences:
    - Equipment geometry
    - Tool and actuator
    - Heating and cooling response
    - Material supplier
    - Local environment
    - Measurement method

  transfer_method:
    - Direct equivalence
    - Physics-based scaling
    - DoE
    - Bayesian transfer
    - Transfer learning
    - Digital-twin simulation

  qualification:
    - Engineering trial
    - Multi-lot validation
    - Capability test
    - Cell performance
    - Safety validation
    - Customer approval
```

---

## 55.3 Invariant vs Adaptable Parameters

```yaml
recipe_transfer_parameter_classes:

  product_invariants:
    examples:
      - Electrode loading target
      - Cell capacity target
      - Safety margin
      - Final dimensions
      - Acceptance specification

  process_intent_invariants:
    examples:
      - Required dispersion
      - Required residual moisture
      - Required weld resistance
      - Required seal integrity
      - Required formation outcome

  equipment_normalized_parameters:
    examples:
      - Energy per material mass
      - Shear exposure
      - Drying rate
      - Calender line pressure
      - Weld energy density

  locally_adaptable_parameters:
    examples:
      - Motor speed
      - Oven zone setpoint
      - Roll gap
      - Robot coordinate
      - Formation channel compensation
```

---

## 55.4 Golden Batch Model

```yaml
golden_batch:

  golden_batch_id: required

  eligibility:
    - Released customer-quality product
    - Complete genealogy
    - Stable equipment condition
    - No deviation or rework
    - Representative material lots

  stored_features:
    - Material fingerprint
    - Process trajectories
    - Intermediate quality
    - Formation curves
    - Final cell performance
    - Pack EoL result

  use:
    - Target-line comparison
    - Model calibration
    - Ramp-up reference
    - Drift detection

  warning:
    - One batch is not sufficient for process-window definition
    - Golden batch is a reference, not an immutable recipe
```

---

## 55.5 Transfer Validation Matrix

| 검증축 | 확인내용                              |
| --- | --------------------------------- |
| 소재  | 공급사·입도·수분·유변·전해액 차이               |
| 설비  | 크기·열관성·롤 변형·센서·제어응답               |
| 공정  | Parameter가 아니라 동일한 품질목표 달성 여부     |
| 측정  | 측정기 교정·Bias·Sampling·이미지 조건       |
| 제품  | 셀 설계·전극면적·두께·폼팩터                  |
| 결과  | 중간품질·Formation·수명·안전              |
| 운영  | 작업자·Changeover·Maintenance·물류     |
| 디지털 | Tag·Recipe·Model·Ontology Version |

ISO 23247은 제조 Digital Twin의 일반원칙, 참조 아키텍처, 제조요소의 디지털 표현과 정보교환을 규정하며, 2026년에는 Digital Thread와 Twin Composition 관련 Part 5·6이 추가됐다. 이는 공장 간 제품·공정·설비 Twin을 구성하고 연결하는 기준으로 활용할 수 있다. ([ISO][8])

---

## 55.6 Cross-Plant Transfer OI Seeds

```yaml
cross_plant_oi_seeds:

  - seed_id: OI-SEED-D06-047
    title: Cross-Plant Recipe Transfer Assistant
    needed_capability:
      - Equipment normalization
      - Material similarity
      - Transfer-learning model
      - Qualification workflow
    priority: VERY_HIGH

  - seed_id: OI-SEED-D06-048
    title: Golden Batch and Process-Trajectory Library
    needed_capability:
      - Common data model
      - Complete genealogy
      - Reference batch search
      - Drift comparison
    priority: VERY_HIGH

  - seed_id: OI-SEED-D06-049
    title: Global Measurement-System Equivalence
    needed_capability:
      - Gauge correlation
      - Image-system normalization
      - Cross-plant reference samples
    priority: VERY_HIGH
```

---
