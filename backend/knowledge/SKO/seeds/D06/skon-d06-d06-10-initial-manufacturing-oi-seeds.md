---
id: skon-d06-d06-10-initial-manufacturing-oi-seeds
title: Initial Manufacturing OI Seeds
summary: "배터리 전극 제조 공정에서 원재료 편차, 슬러리 특성, 코팅 결함, 건조, 캘린더링, 엣지 결함 등 6가지 개선 필요 과제를 정의한다."
tags: [d06, process, oi-seed, schema]
keywords: [배터리 극판, 제조공정 혁신, AI 기반 제어, 디지털 트윈, 품질 센서, 슬러리 분석, 결함 검출, 폐루프, 공정 자동화, 최적화, 배터리 전극, 원재료 편차, 슬러리 특성, 코팅 결함, 건조 최적화, 캘린더링, 폐루프 제어]
related: []
priority: normal
domain: D06
section: D06-10.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1125
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-10. Initial Manufacturing OI Seeds

## OI-SEED-D06-001 — Material Variability Compensation

```yaml
seed_id: OI-SEED-D06-001
title: Raw Material Variability-to-Recipe Compensation

strategy:
  objective: 공급사·Lot 편차에 강한 생산체계

current_state:
  - Material properties are inspected by lot
  - Actual SK On compensation method is not disclosed

gap:
  - Incoming material data and process recipe are disconnected

needed_capability:
  - Material fingerprint
  - Lot clustering
  - Recipe recommendation
  - Downstream performance feedback

external_partner_type:
  - Powder characterization company
  - Process AI startup
  - Laboratory automation company

expected_kpi:
  - Batch variability
  - Coating loading variation
  - First-pass yield

priority: VERY_HIGH
```

---

## OI-SEED-D06-002 — Slurry Digital Fingerprint

```yaml
seed_id: OI-SEED-D06-002
title: Inline Slurry Digital Fingerprint

gap:
  - Offline viscosity sample cannot represent the full mixing and transfer history

needed_capability:
  - Inline rheology
  - Acoustic or ultrasonic dispersion measurement
  - Torque and power signature analysis
  - Agglomerate detection
  - Coating-quality prediction

expected_kpi:
  - Slurry release time
  - Coating defect rate
  - Mixer downtime

priority: VERY_HIGH
```

---

## OI-SEED-D06-003 — Coating Defect Digital Map

```yaml
seed_id: OI-SEED-D06-003
title: Coordinate-Based Electrode Defect Map

gap:
  - Defects are detected but may not remain linked to downstream cells

needed_capability:
  - Machine-direction coordinate tracking
  - Cross-web defect location
  - Roll-to-cell genealogy
  - Automatic local cut-out
  - Defect-to-performance correlation

expected_kpi:
  - False reject rate
  - Defect escape
  - Scrap reduction

priority: VERY_HIGH
```

---

## OI-SEED-D06-004 — Intelligent Drying Optimization

```yaml
seed_id: OI-SEED-D06-004
title: Energy–Quality Co-Optimized Electrode Drying

gap:
  - Drying speed, energy, adhesion and microstructure are optimized separately

needed_capability:
  - Electrode surface-temperature imaging
  - Solvent concentration measurement
  - Drying digital twin
  - Binder-migration prediction
  - Adaptive zone control

expected_kpi:
  - Energy per square meter
  - Residual solvent
  - Electrode adhesion
  - Line speed

priority: VERY_HIGH
```

---

## OI-SEED-D06-005 — AI Calendering Closed Loop

```yaml
seed_id: OI-SEED-D06-005
title: AI Calendering Closed-Loop Validation

sk_on_asset:
  - AI-based calendering process-control concept
  - Process data
  - Electrode quality data

gap:
  - Public evidence of closed-loop production deployment is unavailable

needed_capability:
  - Thickness and porosity soft sensor
  - Roll-deflection model
  - Model uncertainty
  - Safe automatic adjustment
  - Recipe transfer between lines

expected_kpi:
  - Thickness Cpk
  - Density variation
  - Electrode crack rate
  - Changeover loss

priority: VERY_HIGH
```

---

## OI-SEED-D06-006 — Edge Defect Prevention

```yaml
seed_id: OI-SEED-D06-006
title: Predictive Slitter·Notcher Quality

gap:
  - Burr and particle shedding may be detected after defects are generated

needed_capability:
  - Tool-wear monitoring
  - Acoustic and vibration sensing
  - Burr-height prediction
  - Automatic blade-change recommendation
  - Electrode-specific cutting recipe

expected_kpi:
  - Burr defect rate
  - Tool life
  - Edge scrap
  - Internal-short escape risk

priority: HIGH
```

---

## OI-SEED-D06-007 — Electrode Manufacturing Digital Thread

```yaml
seed_id: OI-SEED-D06-007
title: Material-to-Cell Manufacturing Digital Thread

gap:
  - Material, process and quality data may exist in separate systems

needed_capability:
  - Common manufacturing ontology
  - Lot and roll genealogy
  - Time-series linkage
  - Defect coordinate linkage
  - Cell serial connection
  - Root-cause graph query

expected_kpi:
  - Root-cause analysis time
  - Affected-lot containment time
  - Scrap localization
  - Warranty traceability

priority: VERY_HIGH
```

---
