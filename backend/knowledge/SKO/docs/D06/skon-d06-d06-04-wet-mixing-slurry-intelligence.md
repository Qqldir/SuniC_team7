---
id: skon-d06-d06-04-wet-mixing-slurry-intelligence
title: Wet Mixing & Slurry Intelligence
summary: "배터리 전극 슬러리의 습식 혼합 공정에서 사용하는 혼합 흐름도, 장비, 중요 공정 파라미터, 품질 속성, 데이터 관리 체계 및 발생 가능한 결함을 정리한 기술 문서."
tags: [d06, process, schema, table]
keywords: [전극 슬러리, 습식 혼합, 입자분산, 점도, 응집체, 고형분 함량, 혼합에너지, 유변학, 공정 매개변수, 결함 모드, 슬러리, 전극 제조, 점도 관리, 입자 분산, 활물질, 혼합 에너지, 공정 파라미터, 배치 기록]
related: []
priority: normal
domain: D06
section: D06-04.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1137
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-04. Wet Mixing & Slurry Intelligence

## 04.1 Generic Wet Mixing Flow

```text
Active Material
+ Conductive Additive
+ Binder
+ Solvent
        ↓
Pre-Mixing
        ↓
High-Shear Mixing / Kneading
        ↓
Solvent Adjustment
        ↓
Vacuum Defoaming
        ↓
Filtration
        ↓
Slurry Storage·Transfer
        ↓
Coating
```

전극 슬러리의 입자분산, 고형분, 점도와 유변특성은 코팅 균일성과 전극 미세구조에 영향을 준다. 습식전극 제조 리뷰는 혼합·슬러리 특성과 건조 중 미세구조 변화가 후속 성능과 결함에 연결된다고 설명한다. ([OSTI][8])

---

## PROC-SKON-D06-004 — Wet Electrode Mixing

```yaml
process_id: PROC-SKON-D06-004
canonical_name: Wet Electrode Mixing
korean_name: 습식 전극 혼합
process_layer: ELECTRODE
ownership_scope: INDUSTRY_BASELINE

input_materials:
  cathode:
    - Cathode active material
    - Conductive additive
    - Binder
    - Solvent

  anode:
    - Graphite or silicon composite
    - Conductive additive
    - Binder
    - Solvent or water-based medium

equipment_classes:
  - Planetary mixer
  - High-shear mixer
  - Kneader
  - Continuous mixer
  - Vacuum mixing tank
  - Filter
  - Transfer pump

critical_process_parameters:
  - Addition sequence
  - Mixing speed
  - Mixing time
  - Mixing energy
  - Temperature
  - Vacuum level
  - Solids content
  - Solvent addition
  - Rest time

critical_quality_attributes:
  - Viscosity
  - Yield stress
  - Thixotropy
  - Particle dispersion
  - Agglomerate size
  - Solid-content uniformity
  - Bubble content
  - Slurry temperature

defect_modes:
  - Agglomeration
  - Conductive-additive segregation
  - Binder nonuniformity
  - Air entrapment
  - Excessive shear damage
  - Sedimentation
  - Filter blockage

inspection_methods:
  - Rheology
  - Solid-content measurement
  - Particle-size analysis
  - Density measurement
  - Microscopy
  - Filter-pressure monitoring

sk_on_parameter_disclosure: NOT_DISCLOSED

source_ids:
  - SRC-BASE-D06-006
  - SRC-BASE-D06-007
  - SRC-BASE-D06-008
```

Argonne의 기준모델은 활물질·카본·바인더·용매를 혼합해 코팅공정으로 공급하는 구조를 사용하지만, 탱크 크기나 혼합량은 특정 가상공장의 경제성 가정이므로 SK온 데이터에 이식하지 않는다. ([ANL Publications][6])

---

## 04.2 Wet Mixing Data Model

```yaml
mixing_batch_record:

  batch_identity:
    - Mixing batch ID
    - Recipe version
    - Production order
    - Mixer ID
    - Operator or automation ID
    - Start and end timestamp

  material_genealogy:
    - Material ID
    - Supplier lot
    - Internal lot
    - Actual dispensed mass
    - Container ID

  process_time_series:
    - Impeller speed
    - Torque
    - Power
    - Temperature
    - Vacuum
    - Pressure
    - Addition event

  quality_results:
    - Viscosity
    - Solid content
    - Density
    - Particle dispersion
    - Filter result
    - Release decision

  downstream_links:
    - Slurry tank ID
    - Coater roll ID
    - Electrode roll ID
    - Cell lot ID
```

---

## 04.3 Wet Mixing Pain Points

| Pain Point | 가능한 원인              | 후속 영향       |
| ---------- | ------------------- | ----------- |
| 점도 편차      | 수분·온도·투입순서·혼합에너지    | 코팅두께 편차     |
| 응집체        | 분산 부족·원료 응집         | 핀홀·줄무늬·국부저항 |
| 기포         | 진공·이송조건 불량          | 코팅 공극·미도포   |
| 침강         | 저장시간·분산 안정성         | Roll 전후 조성차 |
| Batch 간 편차 | 설비·원료 Lot·Recipe 차이 | 셀 성능 분산     |
| 필터 막힘      | 대형 응집체·이물           | 압력상승·가동중단   |

---
