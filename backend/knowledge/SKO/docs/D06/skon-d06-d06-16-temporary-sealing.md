---
id: skon-d06-d06-16-temporary-sealing
title: Temporary Sealing
summary: "파우치 셀 임시 실링 공정의 설비, 파라미터, 품질 특성, 결함 및 검사 방법을 정의하는 기술 표준"
tags: [d06, process, schema]
keywords: [파우치 셀, 전해질 보존, Heat-sealing, 누설 저항성, Peel-strength test, PROC-SKON-D06-014A, 실링 강도, 결함 모드, Thermal-seal signature, 품질 검사, 열 실링, 전해질, 공정 파라미터, 품질 관리, 누수 검사, 셀 조립]
related: []
priority: normal
domain: D06
section: D06-16.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 466
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-16. Temporary Sealing

## PROC-SKON-D06-014A — Temporary Pouch Sealing

```yaml
process_id: PROC-SKON-D06-014A
canonical_name: Temporary Pouch Sealing
korean_name: 파우치 임시 실링
process_layer: CELL_ASSEMBLY
ownership_scope: INDUSTRY_BASELINE

purpose:
  - Retain electrolyte
  - Limit environmental exposure
  - Prepare cell for wetting and formation
  - Preserve gas pocket for later degassing where applicable

equipment_classes:
  - Heat-sealing unit
  - Seal-bar temperature controller
  - Pressure actuator
  - Vision system
  - Seal-surface cleaner

critical_process_parameters:
  - Seal temperature
  - Seal pressure
  - Seal time
  - Seal width
  - Pouch alignment
  - Tab alignment
  - Cooling time

critical_quality_attributes:
  - Seal continuity
  - Seal strength
  - Seal width
  - Absence of wrinkle
  - Absence of electrolyte contamination
  - Tab-area integrity
  - Leakage resistance

defect_modes:
  - Weak seal
  - Overheated seal
  - Seal wrinkle
  - Pouch-layer damage
  - Electrolyte in seal area
  - Tab-seal interference
  - Microleak

inspection_methods:
  - Vision inspection
  - Seal-width measurement
  - Leak test
  - Peel-strength sampling
  - Thermal-seal signature
  - Pressure-decay test

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-014

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-014
```

임시 실링의 정확한 순서·가스 포켓 구조·실링 방식은 셀 설계와 제조사에 따라 달라질 수 있다. SK온 파우치 셀의 구체적 임시 실링 Recipe는 공개되지 않았다.

---
