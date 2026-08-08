---
id: skon-d07-d07-10-plant-line-entity-schema
title: Plant–Line Entity Schema
summary: 배터리 생산라인의 마스터 데이터 스키마 정의와 라인 ID 생성 규칙을 제시하는 기술 명세
tags: [d07, footprint, core-candidate, schema]
keywords: [라인ID, 용량, 운영상태, 생산라인, 물리적범위, 제품범위, 화학성분, 고객매핑, 라인 ID, 캐파시티, 배터리셀, 데이터스키마, 화학재료, 신뢰도]
related: []
priority: critical
domain: D07
section: D07-10.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 602
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-10. Plant–Line Entity Schema

## 10.1 Line Master Schema

```yaml
plant_line_schema:

  line_id:
    required: true

  plant_id:
    required: true

  line_name:
    required: true

  physical_scope:
    allowed_values:
      - BUILDING
      - ELECTRODE_LINE
      - CELL_ASSEMBLY_LINE
      - FORMATION_LINE
      - MODULE_LINE
      - PACK_LINE
      - INTEGRATED_LINE
      - UNRESOLVED

  operating_status:
    allowed_values:
      - OPERATIONAL
      - PARTIAL_OPERATION
      - RAMPING
      - RECONFIGURING
      - PRE_SOP
      - IDLE
      - TRANSFERRED
      - STATUS_UNRESOLVED

  capacity:
    - value_gwh
    - capacity_type
    - reference_date
    - qualification_status

  product_scope:
    - EV_CELL
    - ESS_CELL
    - MODULE
    - PACK
    - POUCH
    - CUSTOMER_SPECIFIC
    - UNRESOLVED

  chemistry:
    - HIGH_NICKEL_NCM
    - MID_NICKEL_NCM
    - LFP
    - OTHER
    - UNRESOLVED

  customer_mapping:
    - customer_id
    - vehicle_or_solution
    - mapping_level
    - effective_period
    - source_ids

  conversion_readiness:
    - current_product
    - target_product
    - equipment_compatibility
    - required_modification
    - qualification_status

  source_ids:
    required: true

  evidence_level:
    required: true

  confidence:
    - VERY_HIGH
    - HIGH
    - MEDIUM
    - LOW
```

---

## 10.2 Line ID 생성원칙

공개자료는 대부분 공장 또는 건물 단위 Capacity만 제시하며, 실제 전극·조립·포메이션 Line 수는 공개하지 않는다. 따라서 임의로 `Line 1`, `Line 2`를 생성하지 않는다.

```yaml
line_creation_rule:

  create_physical_line_when:
    - Official line number is disclosed
    - Regulatory filing identifies a line
    - A plant building is explicitly treated as a capacity unit

  otherwise:
    - Create plant-level aggregate line
    - Set physical_scope: UNRESOLVED
    - Set actual_line_count: NOT_DISCLOSED

  prohibited:
    - Derive line count from total GWh
    - Assume one building equals one integrated production line
    - Divide capacity evenly among undisclosed lines
```

---
