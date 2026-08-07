---
id: skon-d06-d06-42-mes-historian-quality-system
title: MES·Historian·Quality System
summary: "배터리 제조의 생산 이벤트 데이터 구조, 시스템별 역할, 시계열 데이터 문맥화, 데이터 무결성 관리 기준을 정의한다."
tags: [d06, process, schema]
keywords: [제조 이벤트, 시계열, 시스템 경계, 데이터 맥락화, 무결성 제어, 공정 추적성, 센서, QMS, 제조이벤트, 시계열데이터, 설비계보, 센서신호, 부적합, 데이터무결성, 역할분리, 레시피, 공정추적, WIP]
related: []
priority: normal
domain: D06
section: D06-42.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 845
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-42. MES·Historian·Quality System

## 42.1 Manufacturing Event Schema

```yaml
manufacturing_event:

  event_id: required
  event_type: required

  object:
    object_type:
      - Material lot
      - Roll
      - Electrode
      - Cell
      - Module
      - Pack
      - Equipment
      - Tool

    object_id: required

  process:
    process_id: required
    equipment_id: required
    recipe_version: required

  time:
    event_time: required
    ingestion_time: required
    timezone: required

  result:
    - Process value
    - Quality status
    - Material consumption
    - Output quantity
    - Defect
    - Disposition

  evidence:
    - Sensor record
    - Image
    - Operator input
    - Laboratory result
    - Automated inspection

  genealogy:
    - Parent object ID
    - Child object ID
```

---

## 42.2 MES–Historian 역할분리

```yaml
system_role_boundary:

  mes:
    primary_role:
      - Execute production order
      - Enforce routing
      - Verify material
      - Record genealogy
      - Manage WIP
      - Record disposition

  historian:
    primary_role:
      - Store high-frequency time series
      - Preserve equipment and process signals
      - Support trend and event analysis

  qms:
    primary_role:
      - Inspection specification
      - Nonconformance
      - Deviation
      - Corrective action
      - Release decision

  lims:
    primary_role:
      - Laboratory sample
      - Analytical method
      - Test result
      - Material and process qualification

  maintenance_system:
    primary_role:
      - Asset hierarchy
      - Work order
      - Spare part
      - Failure record
      - Preventive-maintenance plan
```

---

## 42.3 Time-Series Contextualization

```text
Raw Tag: PLC_17_AI_004
           ↓
Equipment: Calender No.2
           ↓
Signal: Upper Roll Force
           ↓
Process Phase: Cathode Calendering
           ↓
Product·Recipe·Roll ID
           ↓
Quality Outcome: Thickness·Porosity·Defect
```

```yaml
contextualization_minimum_fields:

  tag_identity:
    - Source system
    - Raw tag name
    - Engineering unit

  equipment_context:
    - Equipment ID
    - Component
    - Sensor location

  production_context:
    - Product
    - Recipe
    - Production order
    - Material or intermediate ID

  phase_context:
    - Process phase
    - Machine state
    - Start and stop event

  quality_context:
    - Inspection result
    - Defect
    - Disposition
```

---

## 42.4 Data Integrity Controls

```yaml
manufacturing_data_integrity:

  identity:
    - Unique object ID
    - Duplicate-ID prevention
    - Serial-position verification

  time:
    - Common time source
    - Clock-drift monitoring
    - Event-time preservation

  version:
    - Recipe version
    - Model version
    - Software version
    - Specification version

  correction:
    - Original-value retention
    - Correction reason
    - Approver
    - Timestamp

  access:
    - Role-based permission
    - Electronic signature
    - Privileged-action logging
```

---
