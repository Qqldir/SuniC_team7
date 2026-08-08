---
id: skon-d06-d06-29-module-cell-stacking-compression
title: Module Cell Stacking·Compression
summary: "배터리 모듈 제조의 셀 적층·압축 공정에서 프로세스 정의, 임계 파라미터, 품질 기준, 결함 모드, 검사 방법을 설명하는 문서다."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [배터리 모듈 조립, 셀 배향, 압축력, 열차단재, 품질속성, compression pad, 불량모드, assembly flow, 셀 적층, 압축, 모듈 조립, 프로세스 파라미터, 품질 기준, 결함 모드, 검사 방법, 배터리 제조]
related: []
priority: normal
domain: D06
section: D06-29.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 928
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-29. Module Cell Stacking·Compression

## 29.1 Conventional Module Assembly Flow

```text
Matched Cells
      ↓
Cell Orientation and Polarity Check
      ↓
Compression Pad·Thermal Barrier Placement
      ↓
Cell Stacking
      ↓
Temporary Stack Compression
      ↓
End Plate·Side Plate Installation
      ↓
Stack-Dimension Inspection
      ↓
Busbar and Sensing Integration
      ↓
Housing Closure
```

---

## PROC-SKON-D06-019B — Cell Stacking and Compression

```yaml
process_id: PROC-SKON-D06-019B
canonical_name: Module Cell Stacking and Compression
korean_name: 모듈 셀 적층·압축
process_layer: MODULE_PACK
ownership_scope: SK_ON_CONFIRMED

input_objects:
  - Matched battery cells
  - Compression pads
  - Thermal barriers
  - Insulation sheets
  - End plates
  - Side structures

output_object:
  - Mechanically constrained cell stack

equipment_classes:
  - Cell feeding robot
  - Orientation inspection
  - Stacking jig
  - Compression fixture
  - Force and displacement sensor
  - Pad or barrier insertion unit
  - Dimensional inspection unit

critical_process_parameters:
  - Cell sequence
  - Cell orientation
  - Pad or barrier position
  - Compression force
  - Compression displacement
  - Stack length
  - Stack parallelism
  - Alignment reference
  - Holding time

critical_quality_attributes:
  - Stack length
  - Compression distribution
  - Cell-to-cell alignment
  - Pad and barrier location
  - End-plate parallelism
  - Cell surface damage absence
  - Swelling accommodation
  - Electrical isolation

defect_modes:
  - Cell orientation error
  - Missing compression pad
  - Missing thermal barrier
  - Excess compression
  - Insufficient compression
  - Nonuniform pressure
  - Cell edge damage
  - Stack tilt
  - Foreign material inclusion

inspection_methods:
  - Force–displacement curve
  - Stack-height measurement
  - Vision inspection
  - Barrier-height measurement
  - Pressure-film sampling
  - Electrical isolation check

technology_ids:
  - TECH-SKON-D04-002
  - TECH-SKON-D04-021
  - TECH-SKON-D04-026
  - TECH-SKON-D04-062

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-009

source_ids:
  - SRC-PAT-D06-029

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-PAT-D06-029

sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

SK온 출원에는 셀 정렬부재, 열차단부재 삽입장치, 삽입압력센서와 높이검사가 포함된다. 다만 이를 SK온의 모든 모듈 라인에 적용된 표준공정으로 확대해석하지 않는다. ([구글 특허][6])

---

## 29.2 Compression Record

```yaml
cell_stack_compression_record:

  stack_identity:
    - Stack ID
    - Cell serial sequence
    - Module build ID
    - Stack fixture ID

  inserted_components:
    - Compression-pad lot
    - Thermal-barrier lot
    - Insulation-sheet lot
    - Component position

  process_time_series:
    - Compression force
    - Displacement
    - Fixture position
    - Hold time
    - Release response

  calculated_features:
    - Stack stiffness
    - Force relaxation
    - Cell-to-cell thickness variation
    - Suspected missing-component signal
    - Pressure-uniformity score

  inspection:
    - Final stack length
    - Parallelism
    - Barrier height
    - Vision result
```

---
