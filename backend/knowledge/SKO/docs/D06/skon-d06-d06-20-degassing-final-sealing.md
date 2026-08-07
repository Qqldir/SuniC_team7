---
id: skon-d06-d06-20-degassing-final-sealing
title: Degassing & Final Sealing
summary: "배터리 파우치 셀의 형성 후 발생한 가스를 제거하고 최종 밀봉하는 공정의 절차, 설비, 공정 파라미터, 검사 방법을 설명하는 제조 프로세스 문서."
tags: [d06, process, schema, "xref:d05"]
keywords: [디개싱, 가스 제거, 파우치 셀, 최종 실링, 진공, 열 실링, 공정 파라미터, 누설 검사, 결함 모드, PROC-SKON-D06-016, 진공 디개싱, 가스 포켓, 밀봉 강도, 전해액 분해, 셀 완성, 압력 감쇠 시험]
related: []
priority: normal
domain: D06
section: D06-20.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 978
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-20. Degassing & Final Sealing

## 20.1 Process Flow

```text
Initial Formation Cell
        ↓
Gas-Pocket Positioning
        ↓
Vacuum Degassing
        ↓
Gas-Pocket Removal or Extraction
        ↓
Seal-Surface Preparation
        ↓
Final Heat Sealing
        ↓
Edge Trimming
        ↓
Leak and Seal Inspection
```

최초 충전에서는 전해액 분해와 계면형성 반응에 따라 가스가 발생할 수 있다. 파우치 셀은 이를 제거한 뒤 최종 실링하는 공정이 필요할 수 있지만, 정확한 가스포켓 구조와 반복횟수는 셀 설계별로 다르다.

---

## PROC-SKON-D06-016 — Degassing and Final Sealing

```yaml
process_id: PROC-SKON-D06-016
canonical_name: Cell Degassing and Final Pouch Sealing
korean_name: 셀 디개싱 및 최종 파우치 실링
process_layer: CELL_FINISHING
ownership_scope: INDUSTRY_BASELINE

input_object:
  - Partially formed pouch cell

output_object:
  - Degassed and permanently sealed cell

equipment_classes:
  - Vacuum chamber
  - Degassing fixture
  - Pouch cutting unit
  - Heat-sealing unit
  - Seal-pressure controller
  - Edge trimming unit
  - Leak-inspection equipment

critical_process_parameters:
  - Chamber vacuum
  - Degassing duration
  - Cell orientation
  - Cell compression
  - Seal temperature
  - Seal pressure
  - Seal duration
  - Seal width
  - Cooling time
  - Trim location

critical_quality_attributes:
  - Residual gas volume
  - Cell thickness
  - Seal continuity
  - Seal strength
  - Seal width
  - Pouch alignment
  - Leakage resistance
  - Electrolyte retention

defect_modes:
  - Incomplete gas removal
  - Electrolyte loss
  - Seal contamination
  - Weak seal
  - Overheated seal
  - Pouch wrinkle
  - Microleak
  - Cell thickness variation

inspection_methods:
  - Cell-weight comparison
  - Thickness measurement
  - Vision inspection
  - Pressure-decay test
  - Tracer-gas test
  - Seal-strength sampling
  - Thermographic inspection candidate

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-008

source_ids:
  - SRC-BASE-D06-016
  - SRC-SKON-D06-021

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-016
  - SRC-SKON-D06-021

sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 20.2 Degassing Record

```yaml
degassing_sealing_record:

  cell:
    - Cell serial number
    - Pre-degassing weight
    - Pre-degassing thickness
    - Formation batch ID

  degassing:
    - Chamber ID
    - Fixture position
    - Vacuum profile
    - Duration
    - Compression profile
    - Extracted gas estimate

  sealing:
    - Sealer ID
    - Recipe version
    - Bar temperature
    - Pressure
    - Time
    - Seal position
    - Trim position

  post_process:
    - Post-seal weight
    - Post-seal thickness
    - Vision result
    - Leak-test result
    - Seal-strength sample link
```

---

## 20.3 Gas as Manufacturing Signal

```yaml
formation_gas_signal:

  possible_information:
    - Electrolyte reaction intensity
    - Residual moisture response
    - Formation-protocol suitability
    - Cell-to-cell process variation
    - Potential contamination

  measurement_candidates:
    - Thickness change
    - Pressure change
    - Extracted gas volume
    - Gas composition sampling
    - Cell mass change

  interpretation_warning:
    - Gas volume alone cannot uniquely identify a root cause
    - Chemistry and cell design strongly affect baseline gas generation
```

---
