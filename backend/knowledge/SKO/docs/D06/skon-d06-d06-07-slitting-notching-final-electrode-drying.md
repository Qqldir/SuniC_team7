---
id: skon-d06-d06-07-slitting-notching-final-electrode-drying
title: Slitting·Notching·Final Electrode Drying
summary: "코팅된 전극을 슬리팅과 노칭으로 절단하고 진공건조한 후 건조실로 이송하는 공정의 임계 파라미터, 품질 기준, 결함 모드를 정의하는 기술 사양서"
tags: [d06, process, schema, "xref:d04"]
keywords: [전극 절단, 슬리팅, 노칭, 진공건조, 공정 파라미터, 결함 모드, 엣지 결함, 수분 제거, 드라이룸 이송, 코팅 박리, 전극절단, 엣지검사, 버높이, 코팅박리, 진공, 건조실, 수분제거, 블레이드, 먼지제거, 레이저노칭]
related: []
priority: normal
domain: D06
section: D06-07.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1084
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-07. Slitting·Notching·Final Electrode Drying

## 07.1 Process Flow

```text
Calendered Master Roll
        ↓
Slitting into Narrow Rolls
        ↓
Edge Inspection
        ↓
Notching / Electrode Cutting
        ↓
Dust Removal
        ↓
Stacking by Polarity
        ↓
Final Vacuum Drying
        ↓
Dry-Room Transfer
```

Argonne 기준모델은 코팅된 전극 Foil을 스트립과 개별 전극으로 절단하고, 절단된 전극을 진공건조한 뒤 드라이룸으로 이송하는 흐름을 사용한다. 모델상 절단 스크랩 수치는 현재 SK온 수율이 아닌 역사적 가정값이므로 D06의 회사 데이터에는 저장하지 않는다. ([ANL Publications][6])

---

## PROC-SKON-D06-009 — Electrode Slitting & Notching

```yaml
process_id: PROC-SKON-D06-009
canonical_name: Electrode Slitting and Notching
korean_name: 전극 슬리팅 및 노칭
process_layer: ELECTRODE
ownership_scope: INDUSTRY_BASELINE

equipment_classes:
  - Rotary slitter
  - Mechanical notcher
  - Laser notcher
  - Web-tension controller
  - Dust-extraction system
  - Edge-inspection camera

critical_process_parameters:
  - Blade clearance
  - Blade overlap
  - Cutting speed
  - Web tension
  - Tool wear
  - Laser power where applicable
  - Laser speed
  - Focal position
  - Dust-extraction flow

critical_quality_attributes:
  - Electrode width
  - Tab geometry
  - Edge straightness
  - Burr height
  - Particle shedding
  - Coating delamination
  - Dimensional accuracy
  - Surface contamination

defect_modes:
  - Metal burr
  - Electrode chipping
  - Coating peel-off
  - Tab deformation
  - Width deviation
  - Dust contamination
  - Heat-affected zone
  - Incorrect electrode orientation

inspection_methods:
  - Optical edge inspection
  - Burr-height measurement
  - Dimensional metrology
  - Surface particle inspection
  - Tool-condition monitoring
  - Dust-particle monitoring

sk_on_parameter_disclosure: NOT_DISCLOSED

technology_ids:
  - TECH-SKON-D04-053
  - TECH-SKON-D04-061

source_ids:
  - SRC-BASE-D06-006
  - SRC-BASE-D06-007
  - SRC-BASE-D06-010
```

---

## PROC-SKON-D06-010 — Final Electrode Drying

```yaml
process_id: PROC-SKON-D06-010
canonical_name: Final Electrode Vacuum Drying
korean_name: 최종 전극 진공건조
process_layer: ELECTRODE
ownership_scope: INDUSTRY_BASELINE

purpose:
  - Remove residual moisture
  - Remove residual volatile species
  - Prepare electrode for dry-room assembly

critical_process_parameters:
  - Vacuum level
  - Temperature
  - Drying time
  - Electrode stack loading
  - Cooling condition
  - Transfer exposure time

critical_quality_attributes:
  - Residual moisture
  - Residual solvent
  - Electrode adhesion
  - Electrode deformation

defect_modes:
  - Incomplete drying
  - Re-absorption during transfer
  - Excess heating
  - Electrode curl
  - Lot mixing

required_genealogy:
  - Electrode roll ID
  - Cut-electrode lot
  - Dryer ID
  - Dryer recipe
  - Rack position
  - Dry-room transfer time

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-006
```

---

## 07.2 Edge-Defect Traceability Model

```yaml
edge_defect_record:

  defect_identity:
    - Defect ID
    - Electrode ID
    - Machine-direction coordinate
    - Cross-web coordinate
    - Defect type

  upstream_context:
    - Master-roll ID
    - Coater ID
    - Calender ID
    - Slitter or notcher ID
    - Blade or laser-tool ID

  defect_measurement:
    - Burr height
    - Delamination area
    - Particle count
    - Edge roughness
    - Dimensional deviation

  downstream_risk:
    - Separator damage
    - Internal-short risk
    - Stacking misalignment
    - Tab-welding defect
    - Local current-density increase

  disposition:
    - Accept
    - Cut out
    - Rework
    - Scrap
```

---
