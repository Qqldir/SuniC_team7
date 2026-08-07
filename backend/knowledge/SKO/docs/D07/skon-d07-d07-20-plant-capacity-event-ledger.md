---
id: skon-d07-d07-20-plant-capacity-event-ledger
title: Plant Capacity Event Ledger
summary: "SK온 생산시설의 캐파시티 변화 이벤트(설계 발표, 가동 시작, 소유권 이전 등)를 연대순으로 기록하고 각 사건의 영향 범위를 추적하는 원장이다."
tags: [d07, footprint, schema]
keywords: [정규화 용량, 양산 개시, 소유권 이전, GWh, SK온, 미래 목표, 지분법, 배터리 공장, 설계 공시, 정규화용량, 용량갱신, 소유권이전, 상용생산, 생산거점, 설비가동, 공시이벤트, 캐파시티변화]
related: []
priority: normal
domain: D07
section: D07-20.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1005
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-20. Plant Capacity Event Ledger

## 20.1 Capacity Event Schema

```yaml
capacity_event_schema:

  capacity_event_id: required
  plant_id: required

  event_type:
    - DESIGN_ANNOUNCED
    - CONSTRUCTION_STARTED
    - EQUIPMENT_INSTALLED
    - PARTIAL_OPERATION_STARTED
    - COMMERCIAL_PRODUCTION_STARTED
    - NORMALIZED_CAPACITY_UPDATED
    - CAPACITY_RECONFIGURED
    - OWNERSHIP_TRANSFERRED
    - DEFERRED
    - TARGET_ANNOUNCED

  capacity:
    value_gwh: optional
    capacity_type: required

  effective_date: required

  inclusion_scope:
    - CONSOLIDATED
    - JV_GROSS
    - EQUITY_METHOD
    - EXCLUDED
    - TRANSFERRED
    - FUTURE_TARGET

  source_ids: required
  evidence_level: required
```

---

## 20.2 Canonical Capacity Events

```yaml
capacity_event_ledger:

  - capacity_event_id: CAPEV-D07-001
    effective_date: 2024-12-31
    subject: SK_On_consolidated
    event_type: NORMALIZED_CAPACITY_UPDATED
    capacity:
      value_gwh: 71.5
      capacity_type: REPORTED_NORMALIZED_CAPACITY
    inclusion_scope: CONSOLIDATED
    source_ids:
      - SRC-REG-D07-001

  - capacity_event_id: CAPEV-D07-002
    effective_date: 2025-12-31
    subject: SK_On_consolidated
    event_type: NORMALIZED_CAPACITY_UPDATED
    capacity:
      value_gwh: 94.6
      capacity_type: REPORTED_NORMALIZED_CAPACITY
    inclusion_scope: CONSOLIDATED
    source_ids:
      - SRC-REG-D07-001

  - capacity_event_id: CAPEV-D07-003
    effective_date: 2026-03-31
    subject: SK_On_consolidated
    event_type: NORMALIZED_CAPACITY_UPDATED
    capacity:
      value_gwh: 97.4
      capacity_type: REPORTED_NORMALIZED_CAPACITY
    inclusion_scope: CONSOLIDATED
    source_ids:
      - SRC-REG-D07-001

  - capacity_event_id: CAPEV-D07-004
    effective_date: 2026-05-20
    subject:
      - Kentucky_1
      - Kentucky_2
    event_type: OWNERSHIP_TRANSFERRED
    capacity:
      q1_included_capacity_removed_gwh: 3.1
      capacity_type: REPORTED_NORMALIZED_CAPACITY_ADJUSTMENT
    inclusion_scope: TRANSFERRED
    source_ids:
      - SRC-REG-D07-003

  - capacity_event_id: CAPEV-D07-005
    effective_date: 2026-06-01
    subject: HSBMA
    event_type: COMMERCIAL_PRODUCTION_STARTED
    capacity:
      value_gwh: 35
      capacity_type: JV_GROSS_DESIGN_CAPACITY
    inclusion_scope: JV_GROSS
    source_ids:
      - SRC-OFF-D07-005

  - capacity_event_id: CAPEV-D07-006
    effective_date: 2026
    subject: GRIDON_Gen_1
    event_type: TARGET_ANNOUNCED
    capacity:
      value_gwh: UNDISCLOSED
      capacity_type: CORPORATE_TARGET
    inclusion_scope: FUTURE_TARGET
    source_ids:
      - SRC-OFF-D07-020

  - capacity_event_id: CAPEV-D07-007
    effective_date: 2028
    subject: SK_On_Tennessee
    event_type: COMMERCIAL_PRODUCTION_TARGET
    capacity:
      legacy_design_reference_gwh: 45
      commissioned_capacity_gwh: UNRESOLVED
    inclusion_scope: FUTURE_TARGET
    source_ids:
      - SRC-OFF-D07-004
      - SRC-REG-D07-019

  - capacity_event_id: CAPEV-D07-008
    effective_date: 2028
    subject: Nissan_supply_program
    event_type: CUSTOMER_SUPPLY_START_TARGET
    capacity:
      contract_total_gwh: nearly_100
      delivery_period: 2028_to_2033
      dedicated_plant_capacity: UNRESOLVED
    inclusion_scope: CUSTOMER_DEMAND
    source_ids:
      - SRC-OFF-D07-017
```

2026년 Capacity Event에서 가장 중요한 점은 HSBMA의 35GWh가 새로 상업생산을 시작했지만 JV Gross라는 점과, Q1 연결 Capacity에 들어 있던 Kentucky 1의 3.1GWh가 5월 이후 SK온에서 제외됐다는 점이다. ([KIND][11])

---
