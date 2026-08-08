---
id: skon-d06-d06-49-smart-factory-oi-seeds
title: Smart Factory OI Seeds
summary: "배터리 제조의 스마트팩토리화를 위한 데이터 통합, 기계상태 분류, 예측유지보수, 가상커미셔닝 등 4대 혁신 과제의 전략, 필요역량, 파트너 유형을 정의한다."
tags: [d06, process, oi-seed, schema]
keywords: [데이터 통합, 장비 상태 분류, 예측유지보수, 가상 commissioning, OI Seeds, MES, OEE, 다운타임 분석, Virtual Commissioning, Predictive Maintenance, 배터리 제조, 예측 유지보수, ISA-95, 가상 커미셔닝, 프로세스 마이닝, 엣지 AI, 계보 추적, 기계상태 분류]
related: []
priority: normal
domain: D06
section: D06-49.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1748
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-49. Smart Factory OI Seeds

## OI-SEED-D06-034 — Battery Manufacturing Data Backbone

```yaml
seed_id: OI-SEED-D06-034
title: Battery Manufacturing Data Backbone

strategy:
  - Connect material, equipment, quality and genealogy data

target:
  - MES, historian, QMS and laboratory integration

gap:
  - High-frequency signals and production objects may use different identifiers

needed_capability:
  - ISA-95-aligned ontology
  - Common equipment hierarchy
  - Event-time synchronization
  - Roll-to-cell-to-pack genealogy
  - Data-quality monitoring

partner_type:
  - Industrial data-platform company
  - Knowledge-graph company
  - Manufacturing integration specialist

collaboration_model:
  - SK On-owned ontology
  - Platform integration PoC

expected_kpi:
  - Data completeness
  - Root-cause analysis time
  - Genealogy coverage
  - Manual data-preparation time

priority: VERY_HIGH
```

---

## OI-SEED-D06-035 — Automatic Machine-State Classification

```yaml
seed_id: OI-SEED-D06-035
title: Automatic Machine-State and Downtime Classification

strategy:
  - Establish reliable OEE and bottleneck data

target:
  - Equipment-state and downtime records

gap:
  - Operator-entered downtime causes may be delayed or inconsistent

needed_capability:
  - PLC and sensor event interpretation
  - Starved·blocked classification
  - Cause-chain analysis
  - Operator confirmation workflow

external_technology:
  - Industrial event analytics
  - Process mining
  - Edge AI

expected_kpi:
  - Unclassified downtime
  - Downtime-label accuracy
  - Mean time to classify
  - Repeated stop rate

priority: VERY_HIGH
```

---

## OI-SEED-D06-036 — Critical Equipment Predictive Maintenance

```yaml
seed_id: OI-SEED-D06-036
title: Battery Line Critical-Asset Predictive Maintenance

strategy:
  - Prevent unplanned line stops and quality drift

priority_assets:
  - Coater pump and tension system
  - Dryer fan and solvent-recovery unit
  - Calender
  - Slitter and notcher
  - Stacking robot
  - Welding optics or horn
  - Formation channel
  - X-ray source and detector

needed_capability:
  - Operating-condition-normalized anomaly detection
  - Remaining-useful-life estimate
  - Quality-impact prediction
  - Maintenance work-order integration

expected_kpi:
  - Unplanned downtime
  - Maintenance lead time
  - Quality loss before failure
  - Spare-parts use

priority: VERY_HIGH
```

---

## OI-SEED-D06-037 — Virtual Commissioning Standard

```yaml
seed_id: OI-SEED-D06-037
title: Global Line Virtual Commissioning Standard

strategy:
  - Reduce new-line and equipment-modification risk

sk_on_asset:
  - Siemens DISW cooperation
  - Global battery manufacturing network

gap:
  - Equipment models and acceptance criteria may differ by supplier and plant

needed_capability:
  - Standard equipment simulation interface
  - PLC and robot software-in-the-loop
  - Cycle-time validation
  - Failure and recovery scenario
  - Common virtual-FAT protocol

partner_type:
  - Siemens DISW
  - Automation supplier
  - Equipment manufacturer

expected_kpi:
  - Commissioning issue count
  - On-site debug time
  - Ramp-up time
  - Engineering change cost

priority: VERY_HIGH
```

---

## OI-SEED-D06-038 — Yield Causal Knowledge Graph

```yaml
seed_id: OI-SEED-D06-038
title: Material-to-Pack Yield Causal Knowledge Graph

strategy:
  - Find cross-process causes of late defects

target:
  - Electrode, cell, finishing and pack quality

needed_capability:
  - Defect ontology
  - Process genealogy
  - Causal hypothesis ranking
  - Experiment and CAPA linkage
  - Evidence-backed relationship confidence

expected_kpi:
  - Root-cause resolution time
  - Repeat defect
  - Containment population
  - Value-added scrap

priority: VERY_HIGH
```

---

## OI-SEED-D06-039 — Coordinate-Level Scrap Localization

```yaml
seed_id: OI-SEED-D06-039
title: Roll-to-Cell Coordinate Scrap Localization

strategy:
  - Scrap only the material affected by a local defect

target:
  - Coating, calendering, slitting and cell genealogy

needed_capability:
  - Machine- and cross-direction coordinates
  - Roll transformation tracking
  - Electrode-to-cell mapping
  - Automatic affected-cell calculation

expected_kpi:
  - Scrap area
  - Quarantine population
  - Defect containment accuracy
  - Manual genealogy time

priority: VERY_HIGH
```

---

## OI-SEED-D06-040 — Utility and Production Energy Orchestration

```yaml
seed_id: OI-SEED-D06-040
title: Utility–Production Energy Orchestration

strategy:
  - Reduce energy per accepted battery without shifting quality risk

target:
  - Dry room, electrode drying and formation

needed_capability:
  - Meter hierarchy
  - Production-context energy allocation
  - Outdoor-humidity forecasting
  - Formation energy recovery
  - Peak-demand-aware scheduling

expected_kpi:
  - Energy per accepted cell
  - Dry-room energy
  - Formation net energy
  - Peak demand
  - Energy applied to scrap

priority: VERY_HIGH
```

---

## OI-SEED-D06-041 — OT Cyber Range for Battery Factories

```yaml
seed_id: OI-SEED-D06-041
title: Battery Factory OT Cyber Range

strategy:
  - Validate recovery without disrupting production

target:
  - PLC, robot, MES, historian and inspection systems

needed_capability:
  - Virtual OT network
  - Controller and equipment emulator
  - Ransomware and data-integrity scenario
  - Backup restoration exercise
  - Quality-impact simulation

partner_type:
  - OT cybersecurity company
  - Automation supplier
  - Digital-twin provider

expected_kpi:
  - Recovery time
  - Backup success
  - Unapproved communication
  - Incident containment time

priority: HIGH
```

---

## OI-SEED-D06-042 — Manufacturing AI Model Governance

```yaml
seed_id: OI-SEED-D06-042
title: Manufacturing AI Model Governance Platform

strategy:
  - Safely scale quality and control models across factories

target:
  - Calendering, welding, formation, grading and inspection AI

needed_capability:
  - Dataset lineage
  - Model registry
  - Product and recipe applicability
  - Drift monitoring
  - Approval and rollback
  - Human override
  - Cybersecurity signature

expected_kpi:
  - Model-validation time
  - Drift detection
  - Unapproved-model deployment
  - Cross-line transfer performance
  - AI-related quality deviation

priority: VERY_HIGH
```

---
