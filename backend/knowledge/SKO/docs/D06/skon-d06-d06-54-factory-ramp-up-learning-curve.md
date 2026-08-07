---
id: skon-d06-d06-54-factory-ramp-up-learning-curve
title: Factory Ramp-Up & Learning Curve
summary: "배터리 생산 능력 확대 시 필요한 8단계 공정 검증 프로세스, 각 단계의 종료 기준과 품질 성과 지표를 설명한다."
tags: [d06, process, schema]
keywords: [기가팩토리, 양산 전환, 배터리, 공정 단계, 설비 검수, 고객 검증, 생산 수율, FPY, Gigafactory, 공정 검증, 생산 능력, SAT, 품질 지표]
related: []
priority: normal
domain: D06
section: D06-54.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1797
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-54. Factory Ramp-Up & Learning Curve

## 54.1 Ramp-Up Evidence Boundary

Fraunhofer FFB는 배터리 Gigafactory Ramp-Up이 제품·공정 복잡성, 높은 자동화 수준, 기술·조직 문제와 지식 부족 때문에 이상적인 직선형 증가와 다르게 전개될 수 있다고 설명한다. 연구기관은 경험 데이터베이스, 디지털화와 체계적인 원인분석을 Ramp-Up 관리의 핵심 요소로 제시한다. ([Fraunhofer FFB][6])

```yaml
ramp_up_boundary:

  publicly_confirmed_sk_on_metrics:
    status: NOT_DISCLOSED

  analytical_use:
    - Define ramp-up gates
    - Track process stability
    - Separate capacity from qualified good output
    - Capture lessons for future plants

  prohibited:
    - Insert generic ramp-up duration as SK On target
    - Infer plant yield from nameplate capacity
    - Treat equipment SAT as production qualification
```

---

## 54.2 Ramp-Up Stage Model

```text
R0 Product·Process Design Freeze
            ↓
R1 Equipment Installation·SAT
            ↓
R2 Dry Run·Utility Qualification
            ↓
R3 Material and Process Trial
            ↓
R4 Cell Build and Process Qualification
            ↓
R5 Customer Qualification
            ↓
R6 Controlled Volume Ramp
            ↓
R7 Stable Serial Production
            ↓
R8 Continuous Improvement
```

```yaml
ramp_up_stage_master:

  R0:
    name: Product and Process Design Freeze
    exit_criteria:
      - Product revision controlled
      - Process route approved
      - Critical parameters identified
      - Measurement system planned

  R1:
    name: Equipment Installation and SAT
    exit_criteria:
      - Safety acceptance
      - Mechanical and electrical completion
      - Basic cycle test
      - Backup and software baseline

  R2:
    name: Dry Run and Utility Qualification
    exit_criteria:
      - Equipment interaction verified
      - Material flow verified
      - Utility stability
      - MES and genealogy transaction verified

  R3:
    name: Material and Process Trial
    exit_criteria:
      - Approved material lots
      - Process window established
      - Measurement system acceptable
      - Initial defect taxonomy

  R4:
    name: Cell and Process Qualification
    exit_criteria:
      - Product performance
      - Safety tests
      - Process capability
      - Repeatability across lots

  R5:
    name: Customer Qualification
    exit_criteria:
      - Customer test completion
      - Change-control agreement
      - Approved production configuration

  R6:
    name: Controlled Volume Ramp
    exit_criteria:
      - Stable good output
      - FPY trend
      - Equipment availability
      - Containment effectiveness

  R7:
    name: Stable Serial Production
    exit_criteria:
      - Sustained qualified throughput
      - Stable quality distribution
      - Predictable delivery
      - Controlled change management
```

---

## 54.3 Ramp-Up KPI Scorecard

```yaml
ramp_up_scorecard:

  output:
    - Total output
    - First-pass good output
    - Customer-releasable output
    - Output versus plan

  quality:
    - Process FPY
    - RTY
    - Defect escape
    - Value-added scrap
    - Repeat defect

  process:
    - Critical parameter Cpk
    - Recipe adherence
    - Measurement-system capability
    - Process-window coverage

  equipment:
    - Availability
    - Unplanned downtime
    - Cycle-time attainment
    - Unclassified downtime

  people:
    - Qualified operator coverage
    - Maintenance-response capability
    - Engineering action closure
    - Training completion

  supply:
    - Approved supplier coverage
    - Material-lot stability
    - Incoming quality
    - Material shortage

  digital:
    - Genealogy completeness
    - Sensor-data completeness
    - Model-validation status
    - Cybersecurity readiness
```

생산량만 증가시키면 불량·재검·고부가 Scrap이 함께 늘 수 있으므로, Ramp-Up은 총생산량보다 **고객 출하 가능한 합격 생산량**을 기준으로 관리해야 한다. 대규모 배터리 생산은 작은 제조편차에도 민감하므로 품질과 처리량을 동시에 보아야 한다. ([Nature][4])

---

## 54.4 Learning Record

```yaml
ramp_up_learning_record:

  learning_id: required

  problem:
    - Symptom
    - Affected process
    - Affected product
    - Affected population

  evidence:
    - Equipment event
    - Process time series
    - Inspection data
    - Laboratory analysis
    - Experiment result

  cause:
    classification:
      - Confirmed
      - Probable
      - Rejected
    causal_chain: required

  resolution:
    - Recipe change
    - Equipment modification
    - Material specification
    - Inspection change
    - Training
    - Maintenance

  validation:
    - Before-after result
    - Replication
    - Applicable product range
    - Applicable equipment range

  reuse:
    - Future line
    - Future plant
    - Supplier specification
    - Virtual commissioning scenario
```

---

## 54.5 Learning-Curve Boundary

```yaml
manufacturing_learning_curve:

  unit_of_learning:
    - Cumulative qualified cells
    - Cumulative qualified electrode area
    - Cumulative accepted capacity
    - Repeated production lots

  outcome_variables:
    - Cycle time
    - First-pass yield
    - Scrap
    - Downtime
    - Energy
    - Engineering intervention

  controls:
    - Product revision must be stable
    - Major equipment change creates a new curve segment
    - Material chemistry change creates a new curve segment
    - Learning must not be confused with demand or utilization change

  sk_on_learning_rate:
    status: NOT_DISCLOSED
```

---

## 54.6 Ramp-Up OI Seeds

```yaml
ramp_up_oi_seeds:

  - seed_id: OI-SEED-D06-044
    title: Ramp-Up Knowledge Graph
    objective:
      - Reuse validated cause–effect knowledge across new lines
    priority: VERY_HIGH

  - seed_id: OI-SEED-D06-045
    title: Virtual SAT and Ramp-Up Scenario Library
    objective:
      - Test failure, recovery, buffer and takt scenarios before installation
    priority: VERY_HIGH

  - seed_id: OI-SEED-D06-046
    title: Qualified-Good-Output Ramp Dashboard
    objective:
      - Separate total output from releasable output
    priority: VERY_HIGH
```

---
