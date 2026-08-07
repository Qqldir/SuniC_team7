---
id: skon-d06-d06-40-manufacturing-system-architecture
title: Manufacturing System Architecture
summary: SK온의 배터리 제조 시스템이 ISA-95 기반 4계층(기업·운영·제어·장비)으로 설계되고 제조 정보가 흐르는 방식을 설명하는 문서
tags: [d06, process, schema]
keywords: [ISA-95, MES, SCADA, ERP, PLC, 제조 정보 흐름, 다층 아키텍처, BOM, 생산 계획, 엣지 분석, 4계층 모델, 정보 흐름, 마스터 데이터]
related: []
priority: normal
domain: D06
section: D06-40.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 917
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-40. Manufacturing System Architecture

## 40.1 ISA-95 기반 분석 아키텍처

```text
LEVEL 4 — Enterprise
ERP · SCM · Finance · PLM · Customer Order
                      ↓
LEVEL 3 — Manufacturing Operations
MES · QMS · LIMS · WMS · APS · Maintenance
                      ↓
LEVEL 2 — Supervisory Control
SCADA · Historian · Line Controller · Edge Analytics
                      ↓
LEVEL 1 — Basic Control
PLC · Motion Controller · Robot Controller · Safety PLC
                      ↓
LEVEL 0 — Physical Process
Sensor · Actuator · Motor · Valve · Welder · Formation Channel
```

ISA-95는 기업과 제조 제어 사이의 인터페이스·정보모델을 정의하는 표준이다. 위 시스템 배치는 그 원칙을 배터리 제조에 적용한 D06 분석구조이며 SK온의 실제 시스템 제품구성을 의미하지 않는다. ([isa.org][3])

---

## 40.2 SK온 제조 시스템 목표모델

```yaml
manufacturing_system_target_architecture:

  enterprise_layer:
    systems:
      - ERP
      - Supply-chain planning
      - Customer-order management
      - Product lifecycle management
      - Cost and finance

    principal_objects:
      - Customer order
      - Product BOM
      - Material requirement
      - Approved supplier
      - Plant capacity

  operations_layer:
    systems:
      - MES
      - QMS
      - LIMS
      - WMS
      - Maintenance management
      - Advanced planning and scheduling

    principal_objects:
      - Production order
      - Recipe
      - Material lot
      - Equipment
      - Work instruction
      - Inspection result
      - Nonconformance
      - Maintenance order

  control_layer:
    systems:
      - SCADA
      - Line controller
      - Historian
      - Edge analytics
      - Machine vision server

    principal_objects:
      - Machine state
      - Alarm
      - Process parameter
      - Equipment event
      - Sensor time series
      - Defect coordinate

  equipment_layer:
    systems:
      - PLC
      - Motion controller
      - Robot
      - Safety controller
      - Intelligent sensor

    principal_objects:
      - Actuator state
      - Tool position
      - Motor current
      - Pressure
      - Temperature
      - Speed
      - Force
      - Image
```

---

## 40.3 Manufacturing Information Flow

```text
Engineering BOM
      ↓
Manufacturing BOM
      ↓
Process Plan
      ↓
Equipment Recipe
      ↓
Production Order
      ↓
Material Consumption
      ↓
Process Event·Inspection
      ↓
Cell·Module·Pack Genealogy
      ↓
Release·Shipment·Field Feedback
```

```yaml
manufacturing_information_controls:

  master_data:
    - Product revision
    - Material specification
    - Process route
    - Recipe version
    - Equipment capability
    - Inspection specification

  transactional_data:
    - Production order
    - Material consumption
    - Equipment use
    - Inspection result
    - Nonconformance
    - Rework

  time_series:
    - Process parameters
    - Equipment condition
    - Environment
    - Energy
    - Quality signal

  relationship_data:
    - Material-to-roll
    - Roll-to-electrode
    - Electrode-to-cell
    - Cell-to-module
    - Cell or module-to-pack
```

---
