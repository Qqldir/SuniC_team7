---
id: skon-d06-d06-51-process-defect-kpi-integration
title: Process–Defect–KPI Integration
summary: 배터리 제조에서 공정 결함이 KPI에 미치는 영향을 추적하고 실시간부터 전술적 단계까지의 운영 의사결정을 지원하는 제어탑 구조
tags: [d06, process, schema, table]
keywords: [제조운영 제어탑, 공정-불량-KPI 통합, ISA-95, 배터리 제조, 불량 추적성, 의사결정 시간대, 수율, 근본원인, 실시간 모니터링, CAPA, 공정결함, 제어탑, 운영 의사결정, 설비 상태, 품질관리, WIP]
related: []
priority: normal
domain: D06
section: D06-51.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1489
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-51. Process–Defect–KPI Integration

## 51.1 Operations Control Tower Objective

```text
Customer Demand·Production Plan
              ↓
Material Availability·Quality Release
              ↓
Equipment Capacity·Maintenance Condition
              ↓
Process Execution·WIP Flow
              ↓
Inline Quality·Defect Detection
              ↓
Yield·Scrap·Energy·Delivery Prediction
              ↓
Recommended Action
              ↓
Production·Quality·Maintenance Decision
```

ISA-95는 기업계층과 제조운영계층 사이의 정보교환, 제조운영 활동과 객체모델을 정의한다. D06 Control Tower는 이를 배터리 제조의 공정·설비·품질·물류 객체에 적용한 분석구조다. ([isa.org][3])

---

## 51.2 Control Tower Entity Model

```yaml
operations_control_tower:

  control_tower_id: OCT-SKON-D06-001
  canonical_name: Battery Manufacturing Operations Control Tower
  ownership_scope: ANALYTICAL_TARGET

  decision_horizons:

    real_time:
      range: seconds_to_minutes
      decisions:
        - Equipment alarm response
        - Quality hold
        - Buffer routing
        - Safe process adjustment
        - Utility excursion response

    shift:
      range: hours
      decisions:
        - Bottleneck response
        - Operator and maintenance allocation
        - Product sequence
        - Retest and rework queue

    daily:
      range: one_to_several_days
      decisions:
        - Production schedule
        - Grade inventory allocation
        - Material release
        - Formation and aging capacity
        - Maintenance window

    tactical:
      range: weeks_to_months
      decisions:
        - Ramp-up target
        - Recipe transfer
        - Equipment modification
        - Supplier and material qualification
        - Capacity investment

  principal_data_domains:
    - Demand and production plan
    - Material and supplier lot
    - Process and recipe
    - Equipment state
    - Quality and defect
    - Genealogy
    - WIP and logistics
    - Energy and utility
    - Maintenance
    - Cost and value-added scrap
```

---

## 51.3 Process–Defect–KPI Bridge Schema

```yaml
process_defect_kpi_bridge:

  bridge_id: required

  process:
    process_id: required
    process_revision: required

  defect:
    defect_id: required
    relationship:
      - ORIGIN_CONFIRMED
      - ORIGIN_SUSPECTED
      - CONTRIBUTING_FACTOR
      - DETECTED_HERE
      - ESCAPED_FROM_UPSTREAM

  kpi_impact:
    - First-pass yield
    - Scrap
    - Rework
    - Cycle time
    - Downtime
    - Energy
    - WIP
    - Delivery
    - Quality escape

  evidence:
    source_ids: required
    experiment_ids: optional
    capa_ids: optional
    model_ids: optional

  evidence_level:
    - THIRD_PARTY_VERIFIED
    - ANALYST_INFERENCE
    - HYPOTHESIS

  confidence:
    - LOW
    - MEDIUM
    - HIGH
    - VERY_HIGH
```

---

## 51.4 KPI Layer Map

| KPI Layer | 핵심 KPI                           | 질문                      |
| --------- | -------------------------------- | ----------------------- |
| 설비        | Availability, MTBF, MTTR         | 설비 때문에 얼마만큼 생산을 잃었는가    |
| 공정        | Cycle Time, Cpk, FPY             | 공정이 안정적으로 합격품을 만드는가     |
| 품질        | Defect Escape, Rework, Scrap     | 불량이 어디서 발생하고 어디서 검출됐는가  |
| 흐름        | WIP, Queue Time, Starved·Blocked | 실제 병목이 어느 공정인가          |
| 에너지       | Energy/Good Cell, Peak Demand    | 합격품 한 개에 에너지가 얼마나 투입되는가 |
| Ramp-Up   | Stable Output, Yield Learning    | 목표 속도와 품질에 얼마나 가까워졌는가   |
| 납기        | Schedule Adherence, OTIF         | 생산계획을 고객납기로 연결했는가       |

ISO 22400은 제조운영 KPI의 산식·구성요소·시간 특성과 적용대상을 정의하는 틀을 제공한다. D06에서는 같은 명칭의 KPI라도 산식과 데이터 경계가 다르면 별도 버전으로 저장한다. ([ISO][2])

---

## 51.5 Control Tower Decision Record

```yaml
control_tower_decision_record:

  decision_id: required
  timestamp: required
  decision_horizon: required

  detected_condition:
    - KPI deviation
    - Predicted bottleneck
    - Material shortage
    - Quality excursion
    - Equipment failure risk
    - Energy peak risk

  affected_scope:
    - Plant
    - Area
    - Line
    - Equipment
    - Material lot
    - WIP population
    - Product

  recommended_actions:
    - Schedule change
    - WIP rerouting
    - Maintenance
    - Quality hold
    - Recipe advisory
    - Additional inspection
    - Material substitution review

  expected_effect:
    - Yield
    - Throughput
    - Delivery
    - Energy
    - Scrap
    - Risk

  execution:
    status:
      - ACCEPTED
      - MODIFIED
      - REJECTED
      - AUTO_EXECUTED
    approver: required
    actual_action: required

  result:
    - KPI before
    - KPI after
    - Side effects
    - Learning record
```

---
