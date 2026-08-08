---
id: skes-d06-4-process-entity-schema
title: Process Entity Schema
summary: "SK이노베이션 E&S의 운영 데이터를 표준화된 구조로 기록하는 프로세스, 이벤트, 센서 태그, 고장 모드 4가지 레코드 스키마를 정의한다."
tags: [d06, process, core-candidate, schema]
keywords: [운영 데이터 표준화, 이벤트 레코드, 시계열 태그, 고장 모드, 센서 측정, 제어 계층, 메타데이터 정의, 데이터 모델, 밸류체인 운전]
related: []
priority: critical
domain: D06
section: 4
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 632
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 4. Process Entity Schema

## 4.1 Canonical Process Record

```yaml
process_record:
  process_id: required
  canonical_name: required
  korean_name: required
  chain_id: required
  lifecycle_status: OPERATING|DEVELOPING|PLANNED|PILOT|INDUSTRY_BASELINE
  operator_entity_id: required_or_gap
  asset_class_ids: []
  upstream_process_ids: []
  downstream_process_ids: []
  input_entities: []
  output_entities: []
  physical_objective: required
  commercial_objective: optional
  control_layer:
    planning_systems: []
    supervisory_systems: []
    basic_control: []
    safety_systems: []
  data_inputs: []
  control_variables: []
  state_variables: []
  quality_attributes: []
  KPI_ids: []
  failure_mode_ids: []
  inspection_methods: []
  maintenance_strategy: []
  source_ids: []
  evidence_level: required
  public_confirmation: required
  internal_validation_required: []
  OI_seed_ids: []
```

## 4.2 Event Record

```yaml
event_record:
  event_id: required
  process_id: required
  asset_id: required_or_gap
  event_type: START|STOP|TRIP|ALARM|DEVIATION|INSPECTION|MAINTENANCE|TRANSFER|SETTLEMENT
  start_time: required
  end_time: optional
  operating_mode: required
  trigger: required
  precondition_snapshot_id: optional
  alarm_ids: []
  work_order_ids: []
  material_or_energy_quantity: optional
  quality_snapshot_id: optional
  safety_barrier_status: []
  financial_impact: internal_optional
  root_cause_status: OPEN|HYPOTHESIS|CONFIRMED|CLOSED
```

## 4.3 Time-Series Tag Record

```yaml
tag_record:
  canonical_tag_id: required
  source_system_tag: restricted
  process_id: required
  equipment_id: required
  measurement: required
  unit: required
  sampling_interval: required
  historian: required
  valid_range: internal
  quality_flag: required
  calibration_due: optional
  timezone: required
  data_owner: required
  cyber_zone: required
  external_use_allowed: required
```

## 4.4 Failure Mode Record

```yaml
failure_mode_record:
  failure_mode_id: required
  process_id: required
  affected_equipment_class_ids: []
  deviation: required
  initiating_causes: []
  leading_indicators: []
  consequences: []
  existing_barriers: []
  detection_methods: []
  response: []
  KPI_impact: []
  OI_candidate: yes_or_no
  evidence_level: required
```

---
