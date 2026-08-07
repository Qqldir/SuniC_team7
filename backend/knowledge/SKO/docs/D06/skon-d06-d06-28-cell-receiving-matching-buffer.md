---
id: skon-d06-d06-28-cell-receiving-matching-buffer
title: Cell Receiving·Matching·Buffer
summary: 셀 용량과 저항 등급의 성능 매칭과 제조 배치의 Genealogy 분산을 동시에 고려하는 모듈·팩 입고·매칭·버퍼 프로세스를 정의한다.
tags: [d06, process, schema]
keywords: [셀 입고, 등급 매칭, 용량 등급, OCV, Formation Batch, 계보 분산, 공통원인, 버퍼, 배터리 조립, 저항 등급, 제조 Genealogy, 셀 분류, 성능 균형, EoL 검사]
related: []
priority: normal
domain: D06
section: D06-28.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 810
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-28. Cell Receiving·Matching·Buffer

## PROC-SKON-D06-019A — Module/Pack Cell Receiving

```yaml
process_id: PROC-SKON-D06-019A
canonical_name: Graded Cell Receiving and Matching
korean_name: 등급 셀 입고·매칭·버퍼
process_layer: MODULE_PACK
ownership_scope: INDUSTRY_BASELINE

input_objects:
  - Accepted graded cells
  - Cell matching-group assignment
  - Cell EoL record

output_objects:
  - Released module cell set
  - Released CTP cell-assembly set
  - Held or reinspection cell

critical_input_attributes:
  - Cell model
  - Capacity class
  - DC resistance class
  - OCV
  - Thickness
  - Weight
  - Formation batch
  - Aging result
  - Manufacturing genealogy
  - Storage exposure

process_functions:
  - Identity verification
  - Polarity and orientation verification
  - Matching-group validation
  - Visual damage inspection
  - OCV or resistance reconfirmation
  - Buffer assignment
  - FIFO or controlled allocation

defect_modes:
  - Wrong cell model
  - Mixed capacity grade
  - Mixed resistance grade
  - Reversed orientation
  - Serial-number mismatch
  - Storage-related voltage drift
  - Cell surface damage
  - Unapproved cell substitution

inspection_methods:
  - Barcode or data-matrix scan
  - OCV measurement
  - Resistance check
  - Dimension and thickness check
  - Vision inspection
  - Genealogy validation

sk_on_parameter_disclosure: NOT_DISCLOSED
evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-SKON-D06-024
  - SRC-PAT-D06-027
```

---

## 28.1 Cell Matching Record

```yaml
module_cell_matching_record:

  assembly_order:
    - Module or pack build ID
    - Product configuration
    - Electrical series-parallel configuration
    - Matching-rule version

  cells:
    - Cell serial number
    - Capacity grade
    - Resistance grade
    - OCV
    - Formation batch
    - Aging batch
    - EoL result

  matching_metrics:
    - Capacity range
    - Resistance range
    - OCV range
    - Thickness range
    - Genealogy concentration
    - Predicted degradation similarity

  decision:
    - Release
    - Re-match
    - Electrical retest
    - Engineering hold
```

---

## 28.2 Buffer Pain Points

```yaml
cell_buffer_pain_points:

  - Grade-specific inventory imbalance
  - Aged-cell voltage drift
  - Cell serial and physical-position mismatch
  - Excessive buffer time
  - Reinspection congestion
  - Module build interruption caused by one missing grade
  - Excessive genealogy concentration in one pack
```

동일 등급 셀만 묶는 방식은 초기 편차를 줄일 수 있지만, 특정 소재 Lot나 Formation Batch가 하나의 팩에 과도하게 집중되면 잠재적 공통원인 위험이 함께 집중될 수 있다. 따라서 성능 매칭과 제조 Genealogy 분산을 동시에 고려하는 것이 D06의 분석 목표다.

---
