---
id: skes-d06-18-data-architecture-and-digital-thread
title: Data Architecture and Digital Thread
summary: "운영 데이터 정규화와 품질 보증을 위한 정준ID, 타임스탐프, 품질기준, PoC 데이터 패키지 규격"
tags: [d06, process, schema, table]
keywords: [정준ID, canonical_tag_id, 타임스탐프, UTC, 데이터품질, 데이터거버넌스, PoC, 시계열, work_order, 센서태그]
related: []
priority: normal
domain: D06
section: 18
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 793
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 18. Data Architecture and Digital Thread

## 18.1 Canonical IDs

| Object | Canonical ID | Required joins |
|---|---|---|
| Physical asset | `asset_id` | site, system, equipment class, operator, effective date |
| Sensor/tag | `canonical_tag_id` | asset, measurement, unit, historian, quality, cyber zone |
| Process | `process_id` | upstream/downstream, product, technology, owner |
| Operating event | `event_id` | asset, process, mode, time, alarm, work order |
| Work order | `work_order_id` | asset, event, failure, part, labor, close evidence |
| Material/energy batch | `flow_lot_id` | source, quantity, quality, title, destination |
| Commercial obligation | `contract_obligation_id` | contract, process, meter, settlement |
| Model | `model_id` | version, data, feature, approval, performance, retirement |
| O/I experiment | `poc_id` | Seed, process, asset, data, baseline, result, gate |

## 18.2 Timestamp Rules

```yaml
time_rules:
  storage: UTC_plus_original_timezone
  market_and_billing: official_market_timezone
  historian: source_timestamp_plus_ingestion_timestamp
  daylight_saving: explicit_fold_and_gap_handling
  clock_sync: monitored
  event_alignment:
    - control millisecond_or_second
    - market and meter interval
    - work_order hours_or_days
    - contract effective period
```

## 18.3 Data-Quality Dimensions

| Dimension | Test | Operational consequence |
|---|---|---|
| Completeness | expected vs received records | blind spot and biased model |
| Validity | range/state/quality flag | false alarm or missed deviation |
| Consistency | mass/energy/topology reconciliation | inventory, settlement, MRV error |
| Timeliness | event-to-availability latency | late decision and unsafe automation |
| Traceability | source→transform→decision lineage | audit and root-cause failure |
| Uniqueness | duplicate tag/event/meter check | double count and conflicting action |
| Accuracy | calibration/reference comparison | systematic KPI bias |
| Context | operating mode and maintenance state | wrong normal/abnormal label |

## 18.4 Minimum PoC Data Package

```yaml
minimum_PoC_package:
  business:
    - problem_statement and current_decision
    - KPI definition and economic/safety impact
  process:
    - process map and operating modes
    - asset hierarchy and critical equipment
  time_series:
    - tag dictionary unit sampling quality
    - at least representative normal abnormal and seasonal periods
  event:
    - alarms trips starts stops maintenance and inspection
  outcome:
    - confirmed failure or loss label
    - action and effectiveness
  governance:
    - data owner and lawful purpose
    - OT cyber zone and access method
    - model approval and rollback
  experiment:
    - baseline comparator
    - train validation test split by time_or_asset
    - value and safety acceptance criteria
```

---
