---
id: skon-d06-d06-43-manufacturing-digital-twin
title: Manufacturing Digital Twin
summary: "제조 디지털 트윈의 모델 타입, 성숙도 단계, SK온의 구현 수준과 검증 방법을 설명한다."
tags: [d06, process, schema]
keywords: [성숙도 모델, 가상공장, Virtual Commissioning, 폐루프 제어, Siemens Xcelerator, 공정 시뮬레이션, 모델 검증, 공정 자동화, 생산 효율화, 성숙도, 제조공정, 시뮬레이션, 가상팩토리, Siemens, 폐루프, 예측, 트윈타입, 모델검증]
related: []
priority: normal
domain: D06
section: D06-43.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 999
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-43. Manufacturing Digital Twin

## 43.1 Twin Type Master

```yaml
manufacturing_digital_twin_types:

  product_twin:
    represents:
      - Cell
      - Module
      - Pack
      - Product tolerance
      - Thermal and mechanical behavior

  process_twin:
    represents:
      - Mixing
      - Coating
      - Drying
      - Calendering
      - Formation
      - Assembly

  equipment_twin:
    represents:
      - Machine kinematics
      - Controller behavior
      - Tool condition
      - Cycle time
      - Failure behavior

  line_twin:
    represents:
      - Buffers
      - Material flow
      - Equipment interaction
      - Starvation and blocking
      - Changeover

  factory_twin:
    represents:
      - Plant layout
      - Logistics
      - Utility demand
      - WIP
      - Labor
      - Production scheduling

  performance_twin:
    represents:
      - Actual operating data
      - Model residual
      - Quality outcome
      - Energy
      - Maintenance
```

---

## 43.2 Digital Twin Maturity

```yaml
digital_twin_maturity:

  level_0_static_model:
    capability:
      - Layout and design visualization
    physical_connection: false

  level_1_virtual_simulation:
    capability:
      - Offline capacity and process simulation
    physical_connection: false

  level_2_connected_twin:
    capability:
      - Actual production data updates model
    physical_connection: one_way

  level_3_predictive_twin:
    capability:
      - Forecast bottleneck, quality or failure
    physical_connection: one_way_with_prediction

  level_4_prescriptive_twin:
    capability:
      - Recommend operating or scheduling changes
    control: ADVISORY

  level_5_closed_loop_twin:
    capability:
      - Automatically adjust validated controls
    control: AUTOMATIC
    sk_on_public_status: NOT_CONFIRMED
```

---

## 43.3 SK온 Digital Twin 적용범위 판정

```yaml
sk_on_digital_twin_status:

  confirmed:
    - Siemens DISW partnership
    - Planned Xcelerator use
    - Virtual factory and process-simulation objective

  evidence_supported_maturity:
    minimum: LEVEL_1_VIRTUAL_SIMULATION
    maximum_publicly_confirmed: UNRESOLVED

  prohibited_assumption:
    - Real-time connected twin is deployed globally
    - Prescriptive control is operational
    - Closed-loop factory control is operational

  evidence_level: DIRECT_OFFICIAL
  confidence: HIGH
```

Siemens는 디지털 트윈을 통해 제조공정의 사전 시뮬레이션, Virtual Commissioning과 실제 성능데이터의 피드백을 지원할 수 있다고 설명한다. SK온 공개자료가 확인하는 것은 협력과 활용계획이며, 연결형·폐루프 Twin의 실제 도입수준은 별도 검증 대상이다. ([Siemens][2])

---

## 43.4 Twin Validation Record

```yaml
digital_twin_validation:

  model_identity:
    - Twin ID
    - Model version
    - Equipment or line scope
    - Software version

  input_validation:
    - Cycle-time distribution
    - Failure distribution
    - Buffer capacity
    - Material routing
    - Quality loss
    - Maintenance schedule

  comparison:
    - Simulated throughput
    - Actual throughput
    - Simulated WIP
    - Actual WIP
    - Simulated downtime
    - Actual downtime
    - Simulated energy
    - Actual energy

  acceptance:
    - Error threshold
    - Approved use case
    - Valid product family
    - Valid operating range

  status:
    - Draft
    - Calibrated
    - Validated
    - Degraded
    - Retired
```

---
