---
id: skon-d06-d06-52-end-to-end-yield-waterfall
title: End-to-End Yield Waterfall
summary: "배터리 제조 공정에서 각 단계의 수율을 추적하고 최종 수율을 계산하는 방법과, 불량 발생·검출 단계별 비용 특성을 분석하는 프레임워크를 설명한다."
tags: [d06, process, schema, table, "xref:d11"]
keywords: [yield waterfall, 첫 통과 수율, FPY, 불량 발생·검출, 배터리 제조공정, 부가가치 스크랩, 공정 경계, 롤드 스루풋 수율, 원인 추적, 다단계 공정, 배터리, 불량, 공정, 검출, 재작업, 폐기물비용, RTY, 품질관리]
related: []
priority: normal
domain: D06
section: D06-52.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1237
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-52. End-to-End Yield Waterfall

## 52.1 Yield Waterfall Structure

```text
Material Release Yield
          ×
Electrode FPY
          ×
Cell Assembly FPY
          ×
Formation FPY
          ×
Aging·Grading FPY
          ×
Cell EoL FPY
          ×
Module·CTP FPY
          ×
Pack EoL FPY
          =
End-to-End Rolled Throughput Yield
```

```yaml
yield_waterfall_formula:

  process_first_pass_yield:
    formula: first_pass_good_output / process_input

  rolled_throughput_yield:
    formula: product_of_each_process_first_pass_yield

  final_yield:
    formula: accepted_output_after_rework / original_input

  good_output_yield:
    formula: customer_releasable_output / original_input

  required_boundary:
    - Process start and end
    - Rework treatment
    - Retest treatment
    - Engineering sample treatment
    - Product revision
    - Time period
```

---

## 52.2 Yield Waterfall Record

```yaml
yield_waterfall_record:

  waterfall_id: required

  boundary:
    - Plant
    - Line
    - Product
    - Product revision
    - Chemistry
    - Time period

  stages:

    material:
      input: null
      first_pass_good: null
      rejected: null

    electrode:
      input: null
      first_pass_good: null
      reworked: null
      scrapped: null

    cell_assembly:
      input: null
      first_pass_good: null
      reworked: null
      scrapped: null

    cell_finishing:
      input: null
      first_pass_good: null
      retested: null
      scrapped: null

    module_pack:
      input: null
      first_pass_good: null
      reworked: null
      scrapped: null

  calculated:
    - Process FPY
    - RTY
    - Final yield
    - Rework-adjusted yield
    - Value-added scrap

  sk_on_actual_values:
    status: NOT_DISCLOSED
```

---

## 52.3 Origin–Detection Matrix

| 불량 발생 공정          | 실제 검출 공정                    | 비용·위험 특성           |
| ----------------- | --------------------------- | ------------------ |
| Mixing·Coating    | Inline Electrode Inspection | 낮은 단계에서 격리 가능      |
| Mixing·Coating    | Formation·Grading           | 소재·조립비가 누적됨        |
| Slitting·Stacking | X-ray EoL                   | 완성 셀 단계의 고부가 Scrap |
| Welding           | Formation·Module EoL        | 원인구분이 어려울 수 있음     |
| Filling·Wetting   | Formation·Aging             | 긴 WIP와 설비점유 발생     |
| Cell Matching     | Pack EoL                    | Pack 재분해·재조립 가능성   |
| Thermal Interface | Pack Thermal Test           | 고가 부품과 조립비 누적      |

배터리는 다단계 공정의 작은 변동이 셀 성능·안전 문제로 이어질 수 있고, 하나의 최종 불량에 여러 잠재 원인이 존재할 수 있다. 따라서 최종 불량률만으로는 생산품질을 충분히 관리하기 어렵다. ([Nature][4])

---

## 52.4 Value-Added Scrap Index

```yaml
value_added_scrap_index:

  objective:
    - Prioritize defects by accumulated economic loss
    - Move detection closer to the origin process

  conceptual_formula: >
    scrap_quantity
    × accumulated_material_cost
    + accumulated_conversion_cost
    + accumulated_energy_cost
    + disposal_or_recycling_cost

  classification:

    low_value_stage:
      - Incoming material
      - Mixing batch
      - Early electrode roll

    medium_value_stage:
      - Slitted electrode
      - Unformed cell
      - Early formation cell

    high_value_stage:
      - Graded cell
      - Module
      - CTP assembly
      - Completed pack

  warning:
    - Actual cost requires D11 cost-domain linkage
```

---

## 52.5 Yield-Causal Query

```yaml
query_id: GQ-D06-001
natural_language: >
  Pack EoL에서 발생한 특정 불량이 어느 공정·소재 Lot·설비에서
  시작됐을 가능성이 높은지 보여줘.

traversal:
  - PACK_DEFECT
  - DETECTED_AT
  - CONTAINS_MODULE_OR_CELLS
  - PRODUCED_BY_PROCESS
  - USED_MATERIAL_LOT
  - PROCESSED_BY_EQUIPMENT
  - CORRELATED_WITH_PARAMETER
  - VALIDATED_BY_EXPERIMENT

answer_requirements:
  - Confirmed and suspected causes separated
  - Confidence shown
  - Affected population calculated
  - Missing genealogy reported
```

---
