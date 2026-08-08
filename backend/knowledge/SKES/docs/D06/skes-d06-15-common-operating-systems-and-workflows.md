---
id: skes-d06-15-common-operating-systems-and-workflows
title: Common Operating Systems and Workflows
summary: "산업 설비 운영에서 제어층별 시스템 구조와 알람 대응, 작업 허가, 변경 관리 등 운영 프로세스 수립 방법을 다룬 문서"
tags: [d06, process, schema, table]
keywords: [제어층, SCADA, 알람 대응, PLC/DCS, 작업 허가, 변경 관리, EAM/CMMS, 안전 시스템, HMI, 운영 프로세스]
related: []
priority: normal
domain: D06
section: 15
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1244
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 15. Common Operating Systems and Workflows

## 15.1 Control-Layer Architecture

| Layer | Typical systems | Decision speed | External-AI rule |
|---|---|---|---|
| L0 field | sensor, transmitter, actuator, relay | milliseconds–seconds | read-only first; direct control prohibited without safety validation |
| L1 control | PLC/DCS/BMS/PCS/turbine control | subsecond–seconds | approved setpoint envelope only |
| L2 supervisory | HMI, SCADA, historian, alarm | seconds–minutes | advisory or constrained optimization |
| L3 operations | MES-like log, EAM/CMMS, LIMS, scheduling | hours–days | workflow integration with human approval |
| L4 enterprise/market | ERP, contract, trading, billing | days–years | commercial optimization with traceable version |
| L5 external ecosystem | market, weather, vendor cloud, regulator | variable | authenticated, quality-flagged ingestion |

## 15.2 Alarm-to-Action Workflow

```yaml
workflow:
  - alarm_generation
  - suppression_or_priority_rule
  - operator_acknowledgement
  - diagnosis and operating_context capture
  - immediate action or safe_state
  - work_request or incident creation
  - root_cause and corrective_action
  - effectiveness and recurrence review
minimum_metrics:
  - alarms_per_operator_hour
  - standing_alarm_count
  - chattering_alarm_count
  - acknowledgement_time
  - alarm_to_work_order_conversion
  - repeat_alarm_after_close
OI_candidate:
  - cross_asset alarm rationalization
  - event sequence mining
  - operator decision support
guardrails:
  - no automatic suppression of safety alarm by opaque model
  - safety instrumented alarms remain independently governed
```

## 15.3 Permit-to-Work and Isolation

```yaml
work_types:
  - hot_work
  - confined_space
  - electrical
  - excavation
  - lifting
  - line_breaking
  - cryogenic_or_hydrogen
minimum_record:
  - asset and location
  - scope hazard JSA and permit type
  - energy source and isolation point
  - lock_tag_try verification
  - gas test and atmospheric monitoring
  - simultaneous_operations conflict
  - issuer acceptor and validity
  - closeout and restoration
OI_candidate:
  - digital isolation graph
  - permit conflict detection
  - field verification via secure mobile device
```

## 15.4 Management of Change

```yaml
change_types:
  - process setpoint or control logic
  - equipment material or vendor
  - software firmware and model
  - operating procedure or staffing
  - temporary bypass and impairment
required_gate:
  - technical and safety review
  - process hazard and cyber review
  - document and training update
  - test and commissioning
  - time_limited temporary change expiry
  - post_implementation review
AI_model_change:
  - training_data and feature version
  - performance and bias test
  - operating envelope
  - rollback and kill_switch
  - accountable approver
```

## 15.5 EAM/CMMS Minimum Data Model

```yaml
functional_location:
  hierarchy: business_site_system_equipment_component
asset_master:
  fields: [asset_id, class, model, serial, criticality, commission_date, parent, status]
work_order:
  fields: [notification, symptom, priority, failure_mode, task, part, labor, downtime, as_found, as_left]
condition_record:
  fields: [measurement, unit, route, threshold, quality, observation]
spare_part:
  fields: [part_id, compatible_asset, lead_time, stock, criticality, shelf_life]
failure_taxonomy:
  fields: [symptom, mechanism, cause, remedy, recurrence]
data_quality_rules:
  - free_text_alone_is_not_root_cause
  - work_order_without_asset_id_is_incomplete
  - asset_status_and_historian_tag_must_share_effective_dates
```

## 15.6 E&S SHE Operating-System Link

E&S는 13개 SHE 운영요소를 규정과 절차에 적용한다고 공개한다. D06에서 직접 연결하는 요소는 SHE 사업관리, 감사, 비상대응, 환경관리, 변경관리, 교육, 사고관리, 협력사 관리, 법규, 공정설비 안전, 화학물질, 작업안전이다. IRR은 리스크 공유와 사고 대응 프로세스의 공식 확인 근거다.

```yaml
SHE_event_link:
  process_event_id: required
  hazard_and_barrier_id: required
  IRR_or_incident_id: optional_by_threshold
  permit_and_MOC_id: required_when_applicable
  contractor_id: optional
  immediate_cause_and_root_cause: separate
  corrective_action_owner_due_status: required
  learning_scope: site_affiliate_CIC
```

---
