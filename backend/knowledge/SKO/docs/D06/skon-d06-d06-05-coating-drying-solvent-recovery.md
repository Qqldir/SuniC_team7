---
id: skon-d06-d06-05-coating-drying-solvent-recovery
title: Coating·Drying·Solvent Recovery
summary: "배터리 극판의 습식 코팅·건조·용매 회수 공정에서 사용되는 장비, 공정 파라미터, 품질 지표, 결함 모드를 정의한 명세"
tags: [d06, process, schema]
keywords: [습식 코팅, 전극 건조, NMP 회수, 슬릿 다이, 다중존 건조기, 코팅 결함, 집전체, 활물질, 습식 전극, 슬롯 다이 코터, 코팅 속도, 다층 건조기, 잔류 용매, 바인더 이동, 극판 접착, 공정 파라미터]
related: []
priority: normal
domain: D06
section: D06-05.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1323
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-05. Coating·Drying·Solvent Recovery

## 05.1 Wet Coating Process

```text
Released Slurry
        ↓
Coating Head
        ↓
Current Collector
        ↓
Wet-Coating Formation
        ↓
Multi-Zone Dryer
        ↓
Solvent Recovery / Exhaust Treatment
        ↓
Dry Electrode Roll
```

Argonne 기준모델은 집전체의 한 면을 코팅·건조한 뒤 반대편을 코팅·건조하는 양면공정을 예시로 제시한다. 양극 용매로 설정된 NMP는 응축·회수하며, 공정비는 코팅면적뿐 아니라 증발시켜야 할 용매량과도 연결된다. 이는 공개 기준모델의 가정이지 SK온의 실제 라인구성은 아니다. ([ANL Publications][6])

---

## PROC-SKON-D06-006 — Wet Electrode Coating

```yaml
process_id: PROC-SKON-D06-006
canonical_name: Wet Electrode Coating
korean_name: 습식 전극 코팅
process_layer: ELECTRODE
ownership_scope: INDUSTRY_BASELINE

input:
  - Released slurry
  - Aluminum or copper current collector

equipment_classes:
  - Slot-die coater
  - Gravure or comma coater
  - Unwinder
  - Tension controller
  - Thickness gauge
  - Edge-position controller

critical_process_parameters:
  - Coating speed
  - Slurry flow rate
  - Die gap
  - Web tension
  - Slurry temperature
  - Coating width
  - Intermittent-coating timing
  - Edge position

critical_quality_attributes:
  - Areal loading
  - Wet thickness
  - Dry thickness
  - Width
  - Edge profile
  - Surface uniformity
  - Uncoated tab position

defect_modes:
  - Streak
  - Pin hole
  - Ribbing
  - Edge bead
  - Missing coating
  - Loading variation
  - Particle agglomerate
  - Foil wrinkle

inspection_methods:
  - Beta or X-ray thickness gauge
  - Optical line scan
  - Surface inspection
  - Edge-position measurement
  - Mass-loading sample test

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-006
  - SRC-BASE-D06-007
  - SRC-BASE-D06-008
```

비균일 양극 코팅은 국부적인 활물질 균형을 깨뜨려 셀 열화를 유발할 수 있다는 연구결과가 있어, 결함의 크기뿐 아니라 위치와 상대전극과의 정렬을 함께 추적할 필요가 있다. ([오크리지국립연구소][11])

---

## PROC-SKON-D06-007 — Drying & Solvent Recovery

```yaml
process_id: PROC-SKON-D06-007
canonical_name: Electrode Drying and Solvent Recovery
korean_name: 전극 건조 및 용매 회수
process_layer: ELECTRODE
ownership_scope: INDUSTRY_BASELINE

equipment_classes:
  - Multi-zone convection dryer
  - Air-handling unit
  - Solvent condenser
  - Solvent recovery unit
  - Thermal oxidizer
  - Exhaust monitoring system

critical_process_parameters:
  - Zone temperature
  - Air velocity
  - Exhaust rate
  - Web speed
  - Residence time
  - Solvent concentration
  - Surface temperature
  - Drying-rate profile

critical_quality_attributes:
  - Residual solvent
  - Moisture
  - Binder distribution
  - Electrode adhesion
  - Crack density
  - Porosity gradient
  - Electrode curl

defect_modes:
  - Incomplete drying
  - Binder migration
  - Surface skin formation
  - Electrode cracking
  - Delamination
  - Nonuniform porosity
  - Solvent-recovery loss

operational_pain_points:
  - Large oven footprint
  - High thermal-energy demand
  - NMP recovery and purification
  - Start-up and shutdown loss
  - Fire and exposure control

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-006
  - SRC-BASE-D06-008
  - SRC-BASE-D06-009
```

습식전극의 건조와 용매회수는 설비면적·에너지·환경관리 부담이 큰 공정이며, 건조조건은 바인더 이동·균열·접착과 같은 전극 미세구조 결함에 영향을 줄 수 있다. ([OSTI][8])

---

## 05.2 Coating–Drying Integrated Data Record

```yaml
electrode_roll_record:

  roll_identity:
    - Electrode roll ID
    - Current-collector coil ID
    - Slurry batch ID
    - Coater ID
    - Recipe version

  coating_time_series:
    - Line speed
    - Web tension
    - Pump flow
    - Die pressure
    - Coating gap
    - Edge position

  dryer_time_series:
    - Zone temperature
    - Air velocity
    - Exhaust
    - Solvent concentration
    - Surface temperature

  inline_quality_map:
    coordinate_system:
      - Machine direction
      - Cross-web direction

    signals:
      - Thickness
      - Loading
      - Surface defect
      - Edge position
      - Width
      - Moisture

  disposition:
    - Release
    - Local cut-out
    - Rework
    - Scrap
```

---
