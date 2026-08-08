---
id: skon-d06-d06-21-aging-charge-retention-test
title: Aging & Charge-Retention Test
summary: "배터리 셀의 안정성 검증을 위한 에이징 및 충전유지 검사 프로세스와 측정 기준, 기록 내용을 정의한 문서."
tags: [d06, process, schema, "xref:d04"]
keywords: [에이징, 자가방전, OCV, 온도 제어, 전압강하, 셀 안정성, SOC, 누수, 마이크로숏, 팽창, 재공품, PROC-SKON-D06-017]
related: []
priority: normal
domain: D06
section: D06-21.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1018
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-21. Aging & Charge-Retention Test

## 21.1 Process Role

```text
Final-Sealed Cell
        ↓
Controlled-Temperature Storage
        ↓
Open-Circuit Voltage Measurement
        ↓
Rest or Calendar-Aging Interval
        ↓
Repeated OCV·Thickness·Temperature Check
        ↓
Charge-Retention or Self-Discharge Decision
        ↓
Release to Grading / Hold / Reject
```

에이징은 셀을 일정 조건에서 보관하며 전압강하, 자가방전, 두께 변화와 초기 안정성을 확인하는 단계다. 장시간 에이징은 잠재결함 검출에 유리할 수 있지만, 재공품과 공장면적을 증가시키므로 검사 민감도와 리드타임 사이의 균형이 필요하다. ([ScienceDirect][9])

---

## PROC-SKON-D06-017 — Cell Aging and Retention Testing

```yaml
process_id: PROC-SKON-D06-017
canonical_name: Cell Aging and Charge-Retention Testing
korean_name: 셀 에이징 및 충전유지 검사
process_layer: CELL_FINISHING
ownership_scope: INDUSTRY_BASELINE

input_object:
  - Formed and final-sealed cell

output_object:
  - Stability-screened cell

equipment_classes:
  - Aging rack
  - Temperature-controlled chamber
  - OCV measurement system
  - Thickness gauge
  - Cell logistics system
  - Safety monitoring system

critical_process_parameters:
  - Initial SOC
  - Aging temperature
  - Aging duration
  - Measurement interval
  - Storage orientation
  - Mechanical compression
  - Temperature uniformity

critical_quality_attributes:
  - OCV retention
  - Voltage-decay rate
  - Self-discharge indicator
  - Thickness change
  - Gas or swelling behavior
  - Temperature stability
  - Leakage absence

defect_modes:
  - Excessive voltage decay
  - Internal leakage current
  - Micro-short indication
  - Delayed gas generation
  - Microleak
  - Abnormal swelling
  - Measurement-contact error

inspection_methods:
  - Repeated OCV measurement
  - Thickness measurement
  - Thermal monitoring
  - Statistical peer comparison
  - Model-based self-discharge prediction
  - Leak retest for suspected cells

technology_ids:
  - TECH-SKON-D04-058
  - TECH-SKON-D04-035

source_ids:
  - SRC-BASE-D06-016
  - SRC-BASE-D06-017

evidence_level: THIRD_PARTY_VERIFIED
sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 21.2 Aging Record

```yaml
aging_retention_record:

  cell_identity:
    - Cell serial number
    - Formation batch
    - Final-seal record

  aging_location:
    - Warehouse or chamber ID
    - Rack ID
    - Position ID

  conditions:
    - Target temperature
    - Actual temperature time series
    - Start SOC
    - Start timestamp
    - End timestamp

  measurements:
    - OCV at each interval
    - Thickness
    - Cell temperature
    - Weight where applicable
    - Visual condition

  calculated_features:
    - Voltage-decay slope
    - Nonlinear relaxation feature
    - Peer-group deviation
    - Swelling rate
    - Suspected self-discharge score

  disposition:
    - Release
    - Extend aging
    - Electrical retest
    - Leak retest
    - Hold
    - Scrap
```

---

## 21.3 Aging Inventory Risk

```text
Long Aging Duration
        ↓
High Work-in-Process Inventory
        ↓
Large Rack·Warehouse Requirement
        ↓
Long Feedback Delay to Upstream Process
        ↓
More Material Produced Before Root Cause Is Found
```

따라서 에이징 단축의 가치는 단순 보관시간 감소뿐 아니라 조립·함침·포메이션 결함을 상류공정에 더 빠르게 피드백한다는 점에 있다.

---
