---
id: skon-d06-d06-15-electrolyte-filling-wetting
title: Electrolyte Filling & Wetting
summary: "포우치 셀에 전해액을 주입해 전극·분리막에 균일하게 침투시키는 공정의 절차, 임계 파라미터, 품질 기준을 설명한다."
tags: [d06, process, schema, "xref:d04"]
keywords: [전해액, 함침, 포우치셀, 전극, 분리막, 캘린더링, 공극률, 진공압력, 도징, 습윤, 침투, 포로시티, 진공-압력, 점도, 토르투오시티, 표면에너지, 건조도]
related: []
priority: normal
domain: D06
section: D06-15.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1171
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-15. Electrolyte Filling & Wetting

## 15.1 Process Flow

```text
Dried and Assembled Pouch Cell
          ↓
Cell Weighing
          ↓
Vacuum Preparation
          ↓
Electrolyte Dosing
          ↓
Vacuum·Pressure-Assisted Infiltration
          ↓
Resting·Soaking
          ↓
Additional Dosing if Required
          ↓
Temporary Sealing
          ↓
Formation
```

전해액 주입은 셀 조립 이후 포메이션 이전에 위치하며, 전해액이 전극과 분리막 전체에 균일하게 침투하는 함침과정이 이어진다. 전극 공극률과 캘린더링 상태, 온도, 진공·압력조건 등이 함침거동에 영향을 줄 수 있다. ([OSTI][9])

---

## PROC-SKON-D06-014 — Electrolyte Filling and Wetting

```yaml
process_id: PROC-SKON-D06-014
canonical_name: Electrolyte Filling and Wetting
korean_name: 전해액 주입 및 함침
process_layer: CELL_ASSEMBLY
ownership_scope: INDUSTRY_BASELINE

input_objects:
  - Dry unfilled pouch cell
  - Electrolyte lot

output_object:
  - Electrolyte-filled pouch cell

equipment_classes:
  - Vacuum filling chamber
  - Precision dosing pump
  - Electrolyte reservoir
  - Vacuum-pressure cycling unit
  - Cell-weighing system
  - Resting or wetting rack

critical_process_parameters:
  - Electrolyte dose
  - Electrolyte temperature
  - Cell temperature
  - Vacuum level
  - Pressure profile
  - Vacuum and pressure cycle count
  - Dosing rate
  - Soaking time
  - Cell orientation
  - Electrode compression state

critical_quality_attributes:
  - Electrolyte quantity
  - Electrolyte distribution
  - Separator wetting
  - Electrode wetting
  - Absence of dry zones
  - Cell weight
  - Leakage absence
  - Moisture and contamination level

defect_modes:
  - Underfilling
  - Overfilling
  - Incomplete wetting
  - Trapped gas
  - Electrolyte contamination
  - Cell-to-cell dose variation
  - Seal-area contamination
  - Leakage

inspection_methods:
  - Pre-fill and post-fill weighing
  - Dosing-system mass balance
  - Pressure-decay monitoring
  - Ultrasound or acoustic imaging candidate
  - X-ray or neutron imaging for research
  - Electrical response during formation
  - Final cell-weight verification

technology_ids:
  - TECH-SKON-D04-057

source_ids:
  - SRC-BASE-D06-013
  - SRC-BASE-D06-014

evidence_level: THIRD_PARTY_VERIFIED
sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 15.2 Wetting Factors

```yaml
electrolyte_wetting_factors:

  electrode:
    - Porosity
    - Pore-size distribution
    - Tortuosity
    - Calendering density
    - Surface chemistry
    - Electrode thickness

  separator:
    - Porosity
    - Surface energy
    - Coating
    - Thickness
    - Compression

  electrolyte:
    - Viscosity
    - Surface tension
    - Temperature
    - Composition
    - Contamination

  cell_architecture:
    - Stack thickness
    - Stack pressure
    - Tab and pouch geometry
    - Gas-escape path

  process:
    - Vacuum
    - Pressure
    - Soaking time
    - Dosing sequence
    - Cell orientation
```

전해액 함침이 느리거나 불균일하면 제조 대기시간이 길어지고, 초기 셀 전기화학 특성의 분산으로 이어질 가능성이 있다. 연구에서는 캘린더링과 온도가 전해액 침투속도에 영향을 줄 수 있다고 보고하지만, 구체적인 영향은 전극구조와 시험조건에 의존한다. ([OSTI][9])

---

## 15.3 Electrolyte Lot–Cell Genealogy

```yaml
electrolyte_filling_record:

  electrolyte:
    - Electrolyte formulation ID
    - Supplier lot
    - Internal lot
    - Tank ID
    - Open timestamp
    - Moisture result
    - Temperature

  cell:
    - Cell serial number
    - Stack ID
    - Pouch ID
    - Pre-fill weight
    - Post-fill weight

  process:
    - Filling equipment ID
    - Nozzle ID
    - Recipe version
    - Actual dose
    - Vacuum profile
    - Pressure profile
    - Soaking duration

  quality:
    - Weight deviation
    - Leak result
    - Wetting-risk score
    - Formation anomaly
```

---
