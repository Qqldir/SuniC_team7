---
id: skon-d06-d06-26-cell-finishing-oi-seeds
title: Cell Finishing OI Seeds
summary: 배터리 완성공정의 충방전 단계에서 효율 개선과 품질 향상을 위한 세 가지 AI 기술 도입 전략을 소개한다.
tags: [d06, process, oi-seed, schema, "xref:d05"]
keywords: [Formation, 적응형 프로토콜, 이상 진단, 근본 원인 분석, 에너지 회수, Rack Scheduling, 공정 최적화, 배터리 제조, AI/ML, 충방전, 셀 결함 진단, 랙 스케줄링, 적응형 제어, 생산 효율화, 품질 진단, 전력 관리, 초기 활성화]
related: []
priority: normal
domain: D06
section: D06-26.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 3075
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-26. Cell Finishing OI Seeds

## OI-SEED-D06-016 — Adaptive Formation Protocol

```yaml
seed_id: OI-SEED-D06-016
title: Cell-Specific Adaptive Formation Protocol

strategy:
  - Reduce formation time while preserving interphase quality

target:
  - Initial charging and activation

current_state:
  - Formation follows a predefined recipe
  - SK On has filed formation-stage defect-detection technology
  - Actual adaptive control is not publicly confirmed

desired_state:
  - Protocol is adjusted within validated limits using early cell response

gap:
  - Fixed recipes may overprocess normal cells and under-diagnose abnormal cells

needed_capability:
  - Early curve-feature extraction
  - Interphase-quality proxy
  - Safe protocol optimization
  - Chemistry-specific control limits
  - Model uncertainty estimation

external_technology:
  - Physics-informed machine learning
  - High-precision formation hardware
  - Battery electrochemistry modeling

partner_type:
  - Formation-equipment company
  - Battery-modeling startup
  - National laboratory

collaboration_model:
  - Shadow-mode validation
  - Controlled pilot
  - Joint foreground patent

expected_kpi:
  - Formation time
  - Energy per accepted cell
  - First-pass yield
  - Early-life quality
  - Protocol-induced scrap

priority: VERY_HIGH
```

---

## OI-SEED-D06-017 — Formation Anomaly Root-Cause AI

```yaml
seed_id: OI-SEED-D06-017
title: Formation Anomaly Root-Cause AI

strategy:
  - Convert formation curves into upstream process feedback

target:
  - Formation abnormality diagnosis

current_state:
  - Voltage-pattern defect detection is disclosed in an SK On patent application

desired_state:
  - The system distinguishes wetting, welding, internal short and channel faults

gap:
  - Similar voltage anomalies may have different causes

needed_capability:
  - Multimodal formation data
  - Upstream genealogy
  - Causal feature library
  - Explainable defect classification

external_technology:
  - Time-series foundation model
  - Causal AI
  - Knowledge graph

partner_type:
  - Industrial AI company
  - Electrochemical diagnostics laboratory
  - Graph-data company

collaboration_model:
  - SK On-owned defect ontology
  - Joint algorithm development

expected_kpi:
  - Root-cause precision
  - Diagnosis time
  - Repeated-defect rate
  - Containment population

priority: VERY_HIGH
```

---

## OI-SEED-D06-018 — Formation Energy Recovery & Rack Scheduling

```yaml
seed_id: OI-SEED-D06-018
title: Formation Energy Recovery and Dynamic Rack Scheduling

strategy:
  - Reduce electricity use and increase channel utilization

target:
  - Formation racks and power conversion

desired_state:
  - Discharge energy is reused where technically feasible
  - Tray assignment minimizes idle and peak load

gap:
  - Energy flow and production scheduling may be optimized separately

needed_capability:
  - Bidirectional power conversion
  - Rack-level energy balancing
  - Dynamic tray scheduling
  - Peak-load prediction
  - Maintenance-aware dispatch

external_technology:
  - Regenerative cycler
  - Microgrid controller
  - Optimization software

partner_type:
  - Power-electronics company
  - Energy-management company
  - Scheduling-optimization startup

collaboration_model:
  - Line-level energy PoC
  - Performance-based contract

expected_kpi:
  - Net energy per accepted cell
  - Peak demand
  - Channel utilization
  - Tray wait time
  - Formation throughput

priority: VERY_HIGH
```

---

## OI-SEED-D06-019 — Formation Gas Prediction

```yaml
seed_id: OI-SEED-D06-019
title: Formation Gas and Degassing Prediction

strategy:
  - Stabilize cell thickness and reduce unnecessary degassing time

target:
  - Formation gas generation and vacuum degassing

desired_state:
  - Gas-generation risk and required degassing duration are predicted per cell

gap:
  - Gas is difficult to measure non-destructively during formation

needed_capability:
  - Thickness or pressure sensing
  - Gas-volume soft sensor
  - Electrolyte-lot linkage
  - Degassing endpoint prediction

external_technology:
  - Thin pressure sensor
  - Optical thickness measurement
  - Gas-analysis sampling
  - Physics-informed gas model

partner_type:
  - Sensor company
  - Vacuum-equipment company
  - Gas-analysis institute

collaboration_model:
  - Sensor integration pilot
  - Joint process patent

expected_kpi:
  - Degassing time
  - Residual gas variation
  - Cell thickness distribution
  - Electrolyte loss
  - Seal contamination rate

priority: HIGH
```

---

## OI-SEED-D06-020 — Multimodal Seal Integrity

```yaml
seed_id: OI-SEED-D06-020
title: Multimodal Pouch Seal Integrity Inspection

strategy:
  - Detect microleaks without excessive false rejection

target:
  - Final sealing and leak inspection

sk_on_asset:
  - Seal-inspection patent application
  - Pouch insulation and thermography patent application

desired_state:
  - Pressure, tracer gas, seal image and thermal signals produce one decision

gap:
  - A single method may miss small leaks or generate false rejects

needed_capability:
  - High-speed tracer-gas detection
  - Pressure-decay compensation
  - Seal-image AI
  - Sensor-fusion confidence score

external_technology:
  - Helium or alternative tracer detection
  - Thermal imaging
  - Edge inference

partner_type:
  - Leak-test equipment company
  - Packaging inspection company
  - Sensor-fusion startup

collaboration_model:
  - Joint equipment validation
  - Battery-specific foreground IP

expected_kpi:
  - Microleak detection sensitivity
  - False reject
  - Test takt time
  - Retest share

priority: VERY_HIGH
```

---

## OI-SEED-D06-021 — Accelerated Aging Decision

```yaml
seed_id: OI-SEED-D06-021
title: Accelerated Aging and Self-Discharge Prediction

strategy:
  - Reduce aging inventory and feedback delay

target:
  - OCV retention and latent-defect screening

desired_state:
  - Cells unlikely to fail extended aging are released earlier
  - High-risk cells receive extended observation

gap:
  - Fixed aging time treats all cells equally

needed_capability:
  - Early OCV-relaxation model
  - Temperature-normalized voltage features
  - Self-discharge probability
  - Risk-based hold duration
  - Conservative safety guardrail

external_technology:
  - Probabilistic machine learning
  - Precision OCV measurement
  - Digital inventory control

partner_type:
  - Battery analytics company
  - Measurement-equipment company
  - University statistics laboratory

collaboration_model:
  - Retrospective validation
  - Parallel shadow operation
  - Gradual release-gate approval

expected_kpi:
  - Average aging time
  - WIP inventory
  - Latent-defect escape
  - Rack-space requirement
  - Upstream feedback time

priority: VERY_HIGH
```

---

## OI-SEED-D06-022 — AI Capacity Grading

```yaml
seed_id: OI-SEED-D06-022
title: Confidence-Aware AI Capacity Grading

strategy:
  - Reduce full-capacity test time and grading congestion

target:
  - Cell grading and sorting

desired_state:
  - High-confidence cells are graded from partial curves
  - Uncertain cells receive full testing

gap:
  - Full testing is slow
  - Pure prediction can create misclassification risk

needed_capability:
  - Partial-curve capacity prediction
  - Uncertainty quantification
  - Tester-drift correction
  - Grade-boundary optimization
  - Cross-line model transfer

external_technology:
  - Time-series ML
  - Bayesian uncertainty
  - Automated model monitoring

partner_type:
  - Battery analytics startup
  - Formation-equipment supplier
  - Metrology institute

collaboration_model:
  - Shadow-mode comparison
  - Product-specific qualification

expected_kpi:
  - Grading cycle time
  - Capacity-prediction error
  - Grade misclassification
  - Tester capacity requirement

priority: VERY_HIGH
```

---

## OI-SEED-D06-023 — Multimodal EoL Decision Engine

```yaml
seed_id: OI-SEED-D06-023
title: Multimodal Cell EoL Decision Engine

strategy:
  - Improve defect detection while reducing redundant inspection

target:
  - Electrical, leak, X-ray, vision and thermal inspection

sk_on_asset:
  - Multiple inspection patent applications
  - Battery-specific defect definitions
  - Formation and grading data

desired_state:
  - Inspection sequence adapts according to each cell's risk

gap:
  - Inspection systems may operate independently
  - Repeated full inspection can increase takt time

needed_capability:
  - Cross-modal data fusion
  - Risk-based inspection routing
  - False-reject analysis
  - Defect-location consistency
  - Traceable decision explanation

external_technology:
  - Multimodal AI
  - Edge computing
  - Inspection orchestration software

partner_type:
  - X-ray equipment company
  - Leak-test company
  - Industrial AI company

collaboration_model:
  - Multi-vendor integration consortium
  - SK On-owned inspection ontology

expected_kpi:
  - Defect escape
  - False reject
  - EoL takt time
  - Retest rate
  - Inspection cost per cell

priority: VERY_HIGH
```

---

## OI-SEED-D06-024 — Cell Finishing Digital Twin

```yaml
seed_id: OI-SEED-D06-024
title: Formation–Aging–Inspection WIP Digital Twin

strategy:
  - Optimize inventory, equipment and energy as one system

target:
  - Cell finishing operations

desired_state:
  - Formation racks, aging positions, inspection equipment and retest queues are jointly scheduled

gap:
  - Local equipment optimization may shift bottlenecks downstream

needed_capability:
  - Discrete-event simulation
  - Real-time WIP location
  - Dynamic bottleneck prediction
  - Energy-aware scheduling
  - Maintenance and failure simulation

external_technology:
  - Factory digital twin
  - Operations-research optimizer
  - Indoor asset tracking

partner_type:
  - Siemens DISW
  - Scheduling software company
  - Industrial simulation specialist

collaboration_model:
  - Virtual commissioning
  - Brownfield line optimization

expected_kpi:
  - Cell-finishing lead time
  - WIP
  - Rack utilization
  - Inspection queue
  - Peak electricity demand

priority: VERY_HIGH
```

---

# D06-27. D05 Patent Backlog Update

```yaml
d05_candidate_patent_backlog_update:

  - candidate_id: PF-CAND-SKON-D05-005
    title: Formation-Stage Battery Defect Detection
    representative_publication:
      - US20250290992A1
    status: FAMILY_RECONCILIATION_REQUIRED

  - candidate_id: PF-CAND-SKON-D05-006
    title: High-Density Battery Activation and Inspection System
    representative_publication:
      - EP4509851A1
    status: FAMILY_RECONCILIATION_REQUIRED

  - candidate_id: PF-CAND-SKON-D05-007
    title: Pouch Insulation and Thermographic Inspection
    representative_publication:
      - US20250349916A1
    status: FAMILY_RECONCILIATION_REQUIRED

  - candidate_id: PF-CAND-SKON-D05-008
    title: Battery Cell Seal Inspection
    representative_publication:
      - US20260126338A1
    status: FAMILY_RECONCILIATION_REQUIRED

governance:
  - Do not add to confirmed D05 family count before priority audit
  - Do not label as active or granted
  - Use as manufacturing technology evidence only
```

---
