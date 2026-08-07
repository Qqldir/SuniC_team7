---
id: skon-d06-d06-22-cell-grading-sorting
title: Cell Grading & Sorting
summary: 셀의 충방전 특성 측정을 통해 불량을 제거하고 용도별으로 분류하며 모듈·팩 매칭 그룹을 생성하는 등급화 프로세스
tags: [d06, process, schema]
keywords: [셀 등급분류, 배터리 선별, 용량·저항·전압, 셀 매칭 그룹, 내부저항, 쿨롱 효율, 이상탐지, 기계학습, 용량·저항 분류, 모듈 매칭, DCIR, OCV, 불량 제거, 초기곡선 예측, 팩 할당]
related: []
priority: normal
domain: D06
section: D06-22.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1041
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-22. Cell Grading & Sorting

## 22.1 Grading Objective

```text
Formation and Aging Data
        ↓
Capacity·Resistance·Efficiency Calculation
        ↓
Outlier and Stability Screening
        ↓
Product-Specific Grade Rules
        ↓
Cell Matching Group Generation
        ↓
Module·Pack Assembly Assignment
```

셀 Grading은 불량품 제거와 함께 용량·저항·전압 특성이 유사한 셀을 묶어 모듈과 팩의 편차를 줄이는 역할을 한다. 최근 연구는 전체 충방전시험을 완료하기 전에 초기 곡선으로 용량을 예측해 Grading 시간을 줄이는 방식을 검토한다. ([ScienceDirect][10])

---

## PROC-SKON-D06-018 — Cell Grading and Sorting

```yaml
process_id: PROC-SKON-D06-018
canonical_name: Cell Grading and Sorting
korean_name: 셀 등급분류 및 선별
process_layer: CELL_FINISHING
ownership_scope: INDUSTRY_BASELINE

input_object:
  - Formed and aged battery cell

output_objects:
  - Accepted graded cell
  - Rework or retest cell
  - Rejected cell
  - Matched cell group

grading_features:
  - Discharge capacity
  - Charge capacity
  - Initial coulombic efficiency
  - DC internal resistance
  - OCV
  - Self-discharge indicator
  - Cell thickness
  - Cell weight
  - Temperature response
  - Curve-derived features

grade_dimensions:
  quality:
    - Accept
    - Conditional
    - Retest
    - Reject

  performance:
    - Capacity class
    - Resistance class
    - Power class

  matching:
    - Module-matching group
    - Pack-matching group
    - Product or customer allocation

equipment_classes:
  - Electrical tester
  - Automated sorter
  - Barcode or data reader
  - Cell-handling robot
  - Buffer and binning system

defect_modes:
  - Misclassification
  - Tester calibration error
  - Data-ID mismatch
  - Grade boundary instability
  - Overly conservative rejection
  - Weak cells entering accepted group

inspection_methods:
  - Full capacity test
  - Partial-curve prediction
  - Resistance test
  - Statistical outlier detection
  - Multi-feature machine-learning classification

source_ids:
  - SRC-BASE-D06-017
  - SRC-BASE-D06-023
  - SRC-SKON-D06-022

evidence_level: THIRD_PARTY_VERIFIED
sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 22.2 Grading Decision Model

```yaml
cell_grade_record:

  identity:
    - Cell serial number
    - Product type
    - Formation recipe
    - Tester ID
    - Model version

  measured_features:
    - Capacity
    - DCIR
    - OCV
    - Coulombic efficiency
    - Voltage relaxation
    - Temperature rise
    - Thickness
    - Weight

  predicted_features:
    - Predicted full capacity
    - Predicted resistance class
    - Predicted early-life stability
    - Prediction confidence

  decision:
    - Grade
    - Matching group
    - Customer or product allocation
    - Retest requirement
    - Reject reason

  governance:
    - Acceptance-limit version
    - Model approval ID
    - Manual override
    - Override reason
```

---

## 22.3 Grading Model Controls

```yaml
grading_ai_governance:

  required_validation:
    - Chemistry-specific validation
    - Product-format validation
    - Factory and line validation
    - Equipment-change validation
    - Seasonal and temperature validation
    - New material-lot validation

  drift_signals:
    - Prediction residual
    - Grade-distribution shift
    - Tester-to-tester bias
    - Upstream material change
    - New formation recipe

  prohibited_use:
    - Remove full testing before validation
    - Use low-confidence prediction as final disposition
    - Mix training and validation cells from the same genealogy without control
```

---
