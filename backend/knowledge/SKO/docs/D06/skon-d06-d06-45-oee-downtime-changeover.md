---
id: skon-d06-d06-45-oee-downtime-changeover
title: OEE·Downtime·Changeover
summary: "배터리 제조 공정의 설비효율(OEE)과 가동 중단 원인, 생산 전환 손실을 ISO 22400 표준으로 정의하고 분류한 KPI 모델."
tags: [d06, process, schema]
keywords: [OEE, 설비 가용성, 다운타임, Downtime taxonomy, 설비 변경, Changeover loss, 배터리 제조, ISO 22400, 종합설비효율, 다운타임 분류, 배터리 제조 KPI, 생산 전환 손실, 공정 성능 지표, 장비 고장]
related: []
priority: normal
domain: D06
section: D06-45.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 823
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-45. OEE·Downtime·Changeover

ISO 22400은 제조 KPI를 일관되게 정의하고 사용하는 프레임워크를 제공한다. 아래 OEE·수율·Changeover 지표는 해당 원칙을 배터리 제조에 적용한 내부 분석모델이며, SK온의 실제 KPI 정의는 공개되지 않았다. ([ISO][4])

## 45.1 OEE Model

```yaml
oee_model:

  availability:
    formula: operating_time / planned_production_time

  performance:
    formula: ideal_cycle_time * total_count / operating_time

  quality:
    formula: good_count / total_count

  oee:
    formula: availability * performance * quality

  boundary_requirements:
    - Equipment or line scope
    - Product
    - Time period
    - Planned-production definition
    - Good-product definition
    - Ideal-cycle-time version
```

---

## 45.2 Downtime Taxonomy

```yaml
downtime_taxonomy:

  planned:
    - Preventive maintenance
    - Changeover
    - Cleaning
    - Calibration
    - Planned engineering trial

  equipment:
    - Mechanical failure
    - Electrical failure
    - Sensor failure
    - Robot or motion failure
    - Tool failure

  material:
    - Material shortage
    - Material-quality hold
    - Wrong material
    - Delayed internal logistics

  quality:
    - Process deviation
    - Inspection hold
    - Excessive scrap
    - Engineering review

  utility:
    - Electricity
    - Compressed air
    - Vacuum
    - Dry-room condition
    - Cooling water
    - Network or system outage

  flow:
    - Starved
    - Blocked
    - Downstream buffer full
    - Upstream buffer empty

  organization:
    - Operator unavailable
    - Work instruction
    - Approval wait
```

---

## 45.3 Downtime Event Record

```yaml
downtime_event:

  equipment_id: required
  start_time: required
  end_time: required

  initial_reason:
    source:
      - Controller
      - Operator
      - MES
      - Maintenance

  normalized_reason:
    - Planned
    - Equipment
    - Material
    - Quality
    - Utility
    - Flow
    - Organization

  causal_chain:
    - Trigger
    - Immediate cause
    - Root cause

  impact:
    - Lost time
    - Lost output
    - Affected WIP
    - Scrap
    - Energy during downtime

  validation:
    - Supervisor approval
    - Maintenance confirmation
    - Quality confirmation
```

---

## 45.4 Changeover Loss

```yaml
changeover_record:

  from:
    - Product
    - Recipe
    - Material
    - Tool

  to:
    - Product
    - Recipe
    - Material
    - Tool

  changeover_phases:
    - Stop and clear
    - Cleaning
    - Tool change
    - Recipe loading
    - Material verification
    - First-piece setup
    - Quality approval
    - Stable production

  losses:
    - Time
    - Material purge
    - Start-up scrap
    - Energy
    - Inspection delay

  kpi:
    - Changeover duration
    - First-good-piece time
    - Start-up scrap
    - Time to stable Cpk
```

---
