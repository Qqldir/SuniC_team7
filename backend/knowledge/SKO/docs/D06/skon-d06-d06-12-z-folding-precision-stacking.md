---
id: skon-d06-d06-12-z-folding-precision-stacking
title: Z-Folding & Precision Stacking
summary: "배터리 전극의 Z-Folding 적층 공정에서 정렬 오류를 방지하기 위한 장비, 관리변수, 품질기준, 결함 모드, 정렬 모니터링 시스템을 정의한 공정 표준서."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [전극 정렬, 분리막, 공정 변수, 품질 속성, 결함 모드, 셀 조립, 오버행, alignment, electrode assembly, inspection, 전극 정렬 오차, 세퍼레이터 장력, 픽 앤 플레이스, 정렬 좌표 모델, 품질 검사 기준, 로봇 캘리브레이션, 정전기, 공정 관리 변수, 원인 분석]
related: []
priority: normal
domain: D06
section: D06-12.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1043
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-12. Z-Folding & Precision Stacking

## PROC-SKON-D06-011 — Z-Folding Electrode Assembly

```yaml
process_id: PROC-SKON-D06-011
canonical_name: Z-Folding Electrode Assembly
korean_name: Z-Folding 전극 적층
process_layer: CELL_ASSEMBLY
ownership_scope: SK_ON_CONFIRMED

input_objects:
  - Dried cathode plates
  - Dried anode plates
  - Continuous separator roll

output_object:
  - Electrode stack assembly

equipment_classes:
  - Separator unwinder
  - Electrode pick-and-place system
  - Stacking table
  - Vision-alignment camera
  - Separator tension controller
  - Stack compression fixture
  - Dust-removal unit

critical_process_parameters:
  - Electrode placement position
  - Separator feeding length
  - Separator tension
  - Folding position
  - Stacking speed
  - Electrode orientation
  - Stack compression
  - Static-charge control

critical_quality_attributes:
  - Cathode–anode alignment
  - Separator overhang
  - Electrode sequence
  - Stack height
  - Stack flatness
  - Electrode count
  - Wrinkle absence
  - Particle contamination

defect_modes:
  - Electrode misalignment
  - Missing electrode
  - Duplicate electrode
  - Separator wrinkle
  - Insufficient separator overhang
  - Fold-position error
  - Electrode rotation
  - Edge damage
  - Foreign particle inclusion

inspection_methods:
  - Top-view vision
  - Side-view vision
  - Electrode-count verification
  - Stack-height measurement
  - Weight verification
  - X-ray inspection
  - Electrical isolation test

technology_ids:
  - TECH-SKON-D04-022

patent_family_ids:
  - PF-SKON-D05-001
  - PF-SKON-D05-024

source_ids:
  - SRC-SKON-D06-011
  - SRC-BASE-D06-012

evidence_level: DIRECT_OFFICIAL
sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

Z-Folding의 존재와 기본 원리는 SK온 공식자료로 확인되지만, 위 설비유형과 세부 관리변수는 일반 적층공정 기준이다. SK온의 현재 장비 구성·속도·정렬공차는 공개되지 않았다. ([ASK Inno][1])

---

## 12.1 Alignment Coordinate Model

```yaml
stack_alignment_record:

  stack_identity:
    - Stack ID
    - Product type
    - Recipe version
    - Stacking equipment ID

  electrode_identity:
    - Electrode ID
    - Polarity
    - Electrode-lot ID
    - Sequence number

  coordinates:
    - Cathode X offset
    - Cathode Y offset
    - Cathode rotation
    - Anode X offset
    - Anode Y offset
    - Anode rotation
    - Separator overhang
    - Fold-position deviation

  images:
    - Pre-placement image
    - Post-placement image
    - Final-stack image

  disposition:
    - Accept
    - Automatic correction
    - Manual rework
    - Scrap
```

---

## 12.2 Z-Folding Root-Cause Graph

```text
Electrode Dimensional Variation
          ┐
Separator Tension Variation
          ├──→ Placement Error
Robot Calibration Drift
          ┤          ↓
Static Electricity
          ┘   Electrode Misalignment
                     ↓
       Separator Overhang Reduction
                     ↓
       Potential Edge Contact·Damage
```

```yaml
z_folding_possible_causes:

  material:
    - Electrode curl
    - Electrode dimensional variation
    - Separator-width variation
    - Static charge

  equipment:
    - Camera calibration drift
    - Pick-up tool wear
    - Robot-position drift
    - Separator-tension variation

  environment:
    - Particle contamination
    - Temperature variation
    - Airflow disturbance

  operation:
    - Incorrect recipe
    - Product changeover error
    - Electrode-lot mix-up
```

`POSSIBLE_CAUSE` 관계는 일반 제조원리를 나타내며 실제 SK온 불량원인으로 단정하지 않는다.

---
