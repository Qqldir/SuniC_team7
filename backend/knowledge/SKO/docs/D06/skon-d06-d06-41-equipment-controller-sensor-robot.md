---
id: skon-d06-d06-41-equipment-controller-sensor-robot
title: Equipment Controller·Sensor·Robot
summary: "공장 자동화 환경에서 제조 설비·센서·로봇의 데이터 스키마, 상태 분류 체계, 센서 품질 기준, 엣지 제어 정책을 규정하는 기술 명세다."
tags: [d06, process, schema]
keywords: [설비 상태 분류, 센서 데이터 품질, OPC UA, 엣지 처리, PLC, 캘리브레이션, 데이터 유효성, 히스토리안, 사이버보안, 제어 아키텍처, 제조공정, 설비 계층, 상태 분류, 센서 품질, 안전 제어, 공정 운영]
related: []
priority: normal
domain: D06
section: D06-41.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 873
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-41. Equipment Controller·Sensor·Robot

## 41.1 Equipment Entity Schema

```yaml
manufacturing_equipment_schema:

  equipment_id: required
  canonical_name: required
  equipment_class: required

  hierarchy:
    - Site
    - Area
    - Line
    - Cell
    - Equipment
    - Module
    - Sensor

  control_assets:
    - PLC
    - Motion controller
    - Robot controller
    - Safety PLC
    - Industrial PC
    - Edge gateway

  operational_attributes:
    - Current state
    - Product and recipe
    - Rated cycle time
    - Tool configuration
    - Maintenance state

  data_interfaces:
    - Industrial fieldbus
    - OPC UA or equivalent
    - Historian connector
    - MES interface
    - Time synchronization

  cybersecurity:
    - Asset owner
    - Firmware version
    - Network zone
    - Approved remote access
    - Backup status
    - Patch status
```

---

## 41.2 Equipment State Vocabulary

```yaml
equipment_state_vocabulary:

  productive:
    - RUNNING_GOOD
    - RUNNING_SCRAP
    - ENGINEERING_RUN

  planned_loss:
    - PLANNED_MAINTENANCE
    - CHANGEOVER
    - CLEANING
    - CALIBRATION
    - BREAK
    - NO_PRODUCTION_PLAN

  unplanned_loss:
    - EQUIPMENT_FAILURE
    - TOOL_FAILURE
    - SENSOR_FAILURE
    - QUALITY_HOLD
    - SAFETY_STOP
    - OT_SYSTEM_FAILURE

  flow_loss:
    - STARVED
    - BLOCKED
    - MATERIAL_WAIT
    - OPERATOR_WAIT
    - DOWNSTREAM_WAIT

  unknown:
    - UNCLASSIFIED
```

`STARVED`, `BLOCKED`와 설비고장을 구분해야 한 설비의 정지 원인을 상류·하류 물류병목과 기계고장으로 분리할 수 있다.

---

## 41.3 Sensor Data Quality Record

```yaml
sensor_quality_record:

  sensor_identity:
    - Sensor ID
    - Equipment ID
    - Measurement type
    - Range
    - Unit
    - Sampling rate

  metrology:
    - Calibration date
    - Calibration result
    - Accuracy
    - Resolution
    - Drift limit
    - Next calibration

  data_health:
    - Missing-data rate
    - Frozen-value detection
    - Outlier rate
    - Time synchronization
    - Communication latency
    - Signal-to-noise ratio

  process_context:
    - Product
    - Recipe
    - Equipment state
    - Process phase
    - Environmental condition

  decision:
    - Valid
    - Degraded
    - Advisory only
    - Invalid
```

---

## 41.4 Edge Processing Architecture

```text
Sensor·Vision·Controller
          ↓
Timestamp and Data Validation
          ↓
Local Feature Extraction
          ↓
Fast Safety or Quality Decision
          ↓
PLC / Line Controller
          ↓
Historian·MES·Model Platform
```

```yaml
edge_control_policy:

  safety_control:
    location: PLC_OR_SAFETY_PLC
    cloud_dependency: PROHIBITED

  deterministic_motion:
    location: LOCAL_CONTROLLER

  quality_inference:
    location:
      - Industrial PC
      - Edge server

  long_term_training:
    location:
      - Central data platform
      - Approved private cloud

  automatic_adjustment:
    requirements:
      - Validated operating window
      - Model confidence
      - Manual override
      - Audit log
      - Safe fallback recipe
```

---
