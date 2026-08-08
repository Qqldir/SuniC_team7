---
id: skon-d06-d06-14-pouch-forming-electrode-insertion
title: Pouch Forming & Electrode Insertion
summary: "파우치 필름을 성형하고 전극 적층체를 삽입하는 배터리 셀 제조 공정의 기술 명세로, 공정 변수·품질 기준·결함 원인을 정의한다."
tags: [d06, process, schema, "xref:d04"]
keywords: [파우치 셀, 전극 스택, 공정변수, 품질 검사, 불량 메커니즘, 코너 박리, 누액 위험, 소재 계보, PROC-SKON-D06-013, 파우치 성형, 전극 적층, 공정 변수, 품질 속성, 결함 모드, 비전 검사, 누설 위험, 셀 조립]
related: []
priority: normal
domain: D06
section: D06-14.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 881
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-14. Pouch Forming & Electrode Insertion

## PROC-SKON-D06-013 — Pouch Forming and Stack Insertion

```yaml
process_id: PROC-SKON-D06-013
canonical_name: Pouch Forming and Electrode-Stack Insertion
korean_name: 파우치 성형 및 전극 적층체 삽입
process_layer: CELL_ASSEMBLY
ownership_scope: SK_ON_CONFIRMED

input_objects:
  - Aluminum-laminate pouch film
  - Electrode-stack assembly
  - Lead tabs
  - Insulation and sealing components

output_object:
  - Unfilled pouch cell assembly

equipment_classes:
  - Pouch-forming press
  - Forming die
  - Film feeder
  - Stack insertion robot
  - Tab-position fixture
  - Vision inspection system
  - Pre-sealing unit

critical_process_parameters:
  - Forming depth
  - Forming pressure
  - Die geometry
  - Film position
  - Stack insertion position
  - Tab position
  - Pouch tension
  - Sealing-surface cleanliness

critical_quality_attributes:
  - Pouch-cavity dimensions
  - Corner thickness
  - Absence of crack or pinhole
  - Stack-to-pouch alignment
  - Tab position
  - Seal-area flatness
  - Wrinkle absence
  - Insulation clearance

defect_modes:
  - Pouch-film crack
  - Corner thinning
  - Wrinkle
  - Stack misplacement
  - Tab interference
  - Seal-area contamination
  - Film delamination
  - Electrode-stack damage during insertion

inspection_methods:
  - Vision inspection
  - Dimensional measurement
  - Pinhole or leak sampling
  - Stack-position verification
  - Tab-position verification
  - Surface-contamination inspection

technology_ids:
  - TECH-SKON-D04-056

source_ids:
  - SRC-BASE-D06-012
  - SRC-BASE-D06-016

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-012

sk_on_parameter_disclosure: NOT_DISCLOSED
```

SK온은 파우치 셀 생산과 Z-Folding 기술을 공식적으로 공개하지만, 파우치 성형깊이·성형압력·삽입속도 등의 실제 조건은 공개하지 않았다. 따라서 위 공정변수는 일반 파우치 제조 기준으로만 사용한다. ([SK On][8])

---

## 14.1 Pouch Material Genealogy

```yaml
pouch_assembly_record:

  pouch_material:
    - Pouch-film lot
    - Roll ID
    - Supplier ID
    - Material specification
    - Storage exposure

  forming:
    - Forming machine ID
    - Die ID
    - Recipe version
    - Cavity position
    - Forming timestamp

  inserted_stack:
    - Stack ID
    - Positive weld ID
    - Negative weld ID
    - Stack dimensions

  inspection:
    - Forming depth
    - Corner image
    - Wrinkle result
    - Tab-position result
    - Seal-surface result
```

---

## 14.2 Pouch Forming Failure Chain

```text
Pouch Film Property Variation
            ↓
Local Forming-Strain Increase
            ↓
Corner Thinning·Microcrack
            ↓
Leakage or Moisture Ingress Risk
```

```text
Stack or Tab Misposition
            ↓
Seal-Area Interference
            ↓
Incomplete Sealing
            ↓
Electrolyte Leakage·Gas Leakage Risk
```

두 연결은 일반적인 `POSSIBLE_CAUSE` 모델이며 SK온 제품불량 사실을 나타내지 않는다.

---
