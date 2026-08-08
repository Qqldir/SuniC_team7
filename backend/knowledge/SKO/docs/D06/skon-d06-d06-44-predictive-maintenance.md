---
id: skon-d06-d06-44-predictive-maintenance
title: Predictive Maintenance
summary: "배터리 제조 공정의 핵심 설비별 모니터링 신호, 고장 기록 구조, 예측 유지보수 의사결정 프로세스를 정의한 가이드 문서"
tags: [d06, process, schema, table]
keywords: [설비모니터링, 상태신호, 이상탐지, 고장예측, 잔존수명, 센서신호, 유지보수의사결정, Asset Criticality, 공정안정성, 다운타임, 설비 모니터링, 상태 신호, Asset Criticality Map, 고장 모드, 이상 탐지, 의사결정 프로세스, 센서 데이터, RUL, 배터리 제조공정, 고장 기록]
related: []
priority: normal
domain: D06
section: D06-44.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 825
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-44. Predictive Maintenance

## 44.1 Asset Criticality Map

| 공정    | 핵심 설비                  | 대표 상태신호                         | 정지 영향            |
| ----- | ---------------------- | ------------------------------- | ---------------- |
| 혼합    | Mixer·Pump             | Torque·Vibration·Pressure       | Batch·Coating 대기 |
| 코팅    | Coater·Pump·Unwinder   | Die pressure·Tension·Motor      | Roll Scrap       |
| 건조    | Oven·Fan·Recovery      | Temperature·Flow·Concentration  | Line 정지·에너지      |
| 압연    | Calender               | Force·Gap·Vibration·Temperature | 두께·밀도 불량         |
| 절단    | Slitter·Notcher        | Vibration·Acoustic·Tool count   | Burr·Dust        |
| 적층    | Stacker·Robot          | Position·Vision·Servo current   | Cell assembly 정지 |
| 접합    | Welder                 | Power·Force·Optical signal      | 전기접합 불량          |
| 주액    | Filling system         | Dose·Pressure·Nozzle condition  | 함침 편차            |
| 포메이션  | Rack·Channel           | Voltage·Current·Contact         | 대량 WIP 정체        |
| X-ray | Source·Detector·Stage  | Image quality·Dose·Position     | EoL 병목           |
| 팩 조립  | Robot·Dispenser·Tester | Position·Mass·Torque            | 고부가 Scrap        |

---

## 44.2 Maintenance Failure Record

```yaml
equipment_failure_record:

  failure_identity:
    - Failure ID
    - Equipment ID
    - Component ID
    - Failure mode

  occurrence:
    - Start time
    - Detection time
    - Stop time
    - Recovery time

  operating_context:
    - Product
    - Recipe
    - Equipment load
    - Tool age
    - Recent maintenance

  signals:
    - Alarm
    - Vibration
    - Temperature
    - Motor current
    - Pressure
    - Image-quality score

  impact:
    - Downtime
    - Lost production
    - Affected WIP
    - Suspected quality impact
    - Scrap

  resolution:
    - Root cause
    - Repair action
    - Replaced part
    - Verification
```

---

## 44.3 Predictive-Maintenance Decision Flow

```text
Asset Criticality
       ↓
Failure Mode and Signal Selection
       ↓
Baseline·Operating-Condition Normalization
       ↓
Anomaly Detection
       ↓
Remaining Useful Life / Failure Probability
       ↓
Maintenance Window Recommendation
       ↓
Work Order
       ↓
Post-Maintenance Validation
```

```yaml
predictive_maintenance_governance:

  mandatory:
    - Failure-mode definition
    - Sensor-quality validation
    - Product and load normalization
    - False-alarm measurement
    - Missed-failure measurement
    - Maintenance-action feedback

  prohibited:
    - Treat every anomaly as failure
    - Train only on normal data and claim cause classification
    - Trigger automatic shutdown without safety validation
    - Ignore maintenance-induced model drift
```

---
