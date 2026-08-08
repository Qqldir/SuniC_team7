---
id: skon-d06-d06-46-yield-scrap-rework-model
title: Yield·Scrap·Rework Model
summary: "배터리 셀과 팩 제조에서 수율 손실, 불량품, 재작업을 계층별·인과적으로 분석하고 추적하는 데이터 모델 및 측정 체계."
tags: [d06, process, schema]
keywords: [수율관리, 폐기추적, FPY, 재작업, 공정손실, 품질KPI, 결함원인, 스크랩회수, 인과관계모델, 배터리제조, First Pass Yield (FPY), Defect escape, 불량품 추적, 누적 가치, Formation, EoL 검사, 인과관계 분석, 원인 확정, 셀 등급]
related: []
priority: normal
domain: D06
section: D06-46.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 875
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-46. Yield·Scrap·Rework Model

## 46.1 Yield Hierarchy

```text
Raw Material Release
        ↓
Electrode FPY
        ↓
Cell Assembly FPY
        ↓
Formation FPY
        ↓
Cell EoL FPY
        ↓
Module / CTP FPY
        ↓
Pack EoL FPY
        ↓
Final Good Pack
```

```yaml
yield_kpis:

  first_pass_yield:
    formula: units_passing_without_rework / units_entering_process

  final_yield:
    formula: accepted_units_after_rework / units_entering_process

  rolled_throughput_yield:
    formula: product_of_process_first_pass_yields

  defect_escape:
    formula: downstream_detected_origin_defects / upstream_processed_units

  rework_rate:
    formula: reworked_units / processed_units

  scrap_rate:
    formula: scrapped_units / processed_units

  value_added_scrap:
    definition: >
      투입된 소재·가공·검사비가 누적된 상태에서 폐기된 제품
```

---

## 46.2 Scrap Genealogy

```yaml
scrap_record:

  scrap_id: required

  object:
    - Material
    - Electrode roll
    - Electrode plate
    - Cell
    - Module
    - Pack

  origin:
    - Suspected origin process
    - Detection process
    - Defect type
    - Equipment
    - Recipe
    - Material lot

  quantity:
    - Unit count
    - Mass
    - Area
    - Energy capacity where applicable

  accumulated_value:
    - Material
    - Conversion
    - Energy
    - Labor
    - Inspection
    - Disposal

  recovery:
    - Rework
    - Internal recycling
    - External recycling
    - Disposal

  containment:
    - Related object population
    - Quarantined population
    - Release decision
```

---

## 46.3 Yield Loss Tree

```yaml
yield_loss_tree:

  material_loss:
    - Incoming rejection
    - Expiration
    - Contamination
    - Wrong dispensing

  electrode_loss:
    - Coating edge trim
    - Coating defect
    - Start-up and shutdown
    - Calender crack
    - Slitting and notching scrap

  cell_assembly_loss:
    - Stacking misalignment
    - Weld defect
    - Pouch defect
    - Filling and sealing defect

  cell_finishing_loss:
    - Formation anomaly
    - Excessive self-discharge
    - Capacity or resistance outlier
    - X-ray or leak reject

  module_pack_loss:
    - Cell matching failure
    - Busbar defect
    - Thermal-interface defect
    - Cooling leak
    - BMS or software configuration
```

---

## 46.4 Causal Yield Graph

```text
Material Property
      ↓
Process Parameter
      ↓
Intermediate Quality
      ↓
Cell Formation Signal
      ↓
Cell Grade
      ↓
Pack EoL
      ↓
Field Performance
```

```yaml
yield_causal_edge:

  subject: required
  predicate:
    - POSSIBLE_CAUSE
    - CONFIRMED_CAUSE
    - CONTRIBUTING_FACTOR
    - DETECTED_BY
    - CORRELATED_WITH

  object: required

  evidence:
    - Source ID
    - Experiment ID
    - Statistical model
    - Engineering validation

  confidence:
    - LOW
    - MEDIUM
    - HIGH
    - VERY_HIGH
```

상관관계 모델만으로 `CONFIRMED_CAUSE`를 생성하지 않고, 공정시험·DoE·원인 제거 후 재현시험이 있는 경우에만 확정 원인으로 승격한다.

---
