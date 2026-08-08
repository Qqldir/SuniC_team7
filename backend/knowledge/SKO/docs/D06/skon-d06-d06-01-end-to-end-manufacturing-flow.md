---
id: skon-d06-d06-01-end-to-end-manufacturing-flow
title: End-to-End Manufacturing Flow
summary: 배터리 셀 제조의 원료 준비부터 배송까지 전체 공정 단계와 L1-L6 레이어별 프로세스 분류 체계를 정의한다.
tags: [d06, process, schema]
keywords: [배터리 제조공정, 셀 어셈블리, 전극 코팅, 슬리팅, 포메이션, 드라이룸, 전해액 주입, 모듈 팩 조립, 공정 레이어, EOL 테스트, 배터리 제조 공정, 양극·음극 코팅, 품질 검사]
related: []
priority: normal
domain: D06
section: D06-01.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 590
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-01. End-to-End Manufacturing Flow

## 01.1 Canonical Cell Manufacturing Flow

```text
Raw Material Receiving
        ↓
Material Storage & Environmental Control
        ↓
Weighing·Dispensing·Lot Identification
        ↓
Cathode / Anode Mixing
        ↓
Slurry Filtration·Defoaming·Transfer
        ↓
Electrode Coating
        ↓
Drying & Solvent Recovery
        ↓
Calendering
        ↓
Slitting·Notching
        ↓
Final Electrode Drying
        ↓
Dry-Room Material Transfer
        ↓
Z-Folding / Stacking
        ↓
Tab Joining·Current-Collector Welding
        ↓
Pouch Forming & Electrode Insertion
        ↓
Electrolyte Filling·Wetting
        ↓
Temporary Sealing
        ↓
Formation Cycling
        ↓
Degassing·Final Sealing
        ↓
Aging·Charge-Retention Test
        ↓
Grading·Sorting
        ↓
Module / CTP Assembly
        ↓
Pack Assembly
        ↓
End-of-Line Test
        ↓
Shipping
```

Argonne의 공개 기준공장 역시 원료 준비, 코팅, 캘린더링, 슬리팅, 진공건조, 드라이룸 셀 조립, 전해액 주입, 포메이션·검사, 모듈·팩 조립의 흐름을 사용한다. ([ANL Publications][6])

---

## 01.2 Process Layer Classification

```yaml
manufacturing_layers:

  L1_material:
    process_ids:
      - PROC-SKON-D06-001
      - PROC-SKON-D06-002
      - PROC-SKON-D06-003

  L2_electrode:
    process_ids:
      - PROC-SKON-D06-004
      - PROC-SKON-D06-005
      - PROC-SKON-D06-006
      - PROC-SKON-D06-007
      - PROC-SKON-D06-008
      - PROC-SKON-D06-009

  L3_cell_assembly:
    process_ids:
      - PROC-SKON-D06-010
      - PROC-SKON-D06-011
      - PROC-SKON-D06-012
      - PROC-SKON-D06-013
      - PROC-SKON-D06-014

  L4_cell_finishing:
    process_ids:
      - PROC-SKON-D06-015
      - PROC-SKON-D06-016
      - PROC-SKON-D06-017
      - PROC-SKON-D06-018

  L5_module_pack:
    process_ids:
      - PROC-SKON-D06-019
      - PROC-SKON-D06-020
      - PROC-SKON-D06-021

  L6_digital_quality:
    process_ids:
      - PROC-SKON-D06-022
      - PROC-SKON-D06-023
      - PROC-SKON-D06-024
```

---
