---
id: skon-d06-d06-18-cell-assembly-oi-seeds
title: Cell Assembly OI Seeds
summary: 셀 조립 공정의 생산성·품질 향상을 위해 필요한 외부 기술과 파트너 협력 모델을 제시하는 오픈 이노베이션 이니셔티브
tags: [d06, process, oi-seed, schema]
keywords: [셀 조립, Dry-room, 건조실, 전극 정렬, Z-Folding, 용접, RFID 추적, 머신 비전, 디지털 트윈, 기술 협력, 건조실 관리, 정렬 제어, 용접 검증, 오픈 이노베이션, 공정 개선, 기술 파트너, 배터리 공정, IoT 센서]
related: []
priority: normal
domain: D06
section: D06-18.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2914
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-18. Cell Assembly OI Seeds

각 OI Seed는 다음 의사결정 체계를 따른다.

```text
Strategy
→ Target
→ Current State
→ Desired State
→ Gap
→ Cause
→ Needed Capability
→ External Technology
→ Partner
→ Collaboration Model
→ Expected KPI
```

---

## OI-SEED-D06-008 — Dry-Room Exposure Intelligence

```yaml
seed_id: OI-SEED-D06-008
title: Dry-Room Material Exposure Intelligence

strategy:
  - Reduce moisture-related process variation
  - Reduce dry-room energy and quarantine loss

target:
  - Electrode and cell-component exposure tracking

current_state:
  - Dry-room environment is controlled
  - SK On object-level exposure genealogy is not publicly confirmed

desired_state:
  - Every material and cell stack has an environmental exposure history
  - Local excursions are automatically linked to affected cells

gap:
  - Room-level sensor data may not be connected to material movement

possible_causes:
  - Disconnected facility and MES data
  - Manual logistics
  - Insufficient local sensing

needed_capability:
  - Mobile dew-point sensing
  - RFID material tracking
  - Exposure digital passport
  - Excursion impact model

external_technology:
  - Industrial IoT sensor
  - Indoor positioning
  - Environmental digital twin

partner_type:
  - Industrial sensor company
  - Smart logistics company
  - Facility energy-management company

collaboration_model:
  - Pilot deployment
  - Data-integration JDA

expected_kpi:
  - Moisture excursion detection time
  - Quarantine lot size
  - Dry-room energy per cell
  - Material exposure time

priority: VERY_HIGH
```

---

## OI-SEED-D06-009 — High-Speed Z-Folding Alignment Control

```yaml
seed_id: OI-SEED-D06-009
title: High-Speed Z-Folding Alignment Control

strategy:
  - Increase stacking productivity without reducing safety margin

target:
  - Electrode placement and separator-overhang control

current_state:
  - SK On operates Z-Folding technology
  - Actual alignment-control performance is not disclosed

desired_state:
  - Placement error is predicted and corrected before stack completion

gap:
  - Vision inspection may detect error after placement
  - Material curl and separator tension change dynamically

possible_causes:
  - Camera latency
  - Robot drift
  - Static charge
  - Electrode dimensional variation

needed_capability:
  - High-speed multi-camera vision
  - Edge and overhang measurement
  - Robot drift compensation
  - Separator-tension soft sensor
  - Predictive placement control

external_technology:
  - High-speed machine vision
  - Motion-control AI
  - Digital servo twin

partner_type:
  - Vision company
  - Robotics company
  - Precision-motion startup

collaboration_model:
  - Equipment retrofit PoC
  - Joint foreground patent

expected_kpi:
  - Alignment Cpk
  - Placement correction rate
  - Stack takt time
  - Defect escape rate

priority: VERY_HIGH
```

---

## OI-SEED-D06-010 — Weld Signature Intelligence

```yaml
seed_id: OI-SEED-D06-010
title: Electrode Tab Weld Signature Intelligence

strategy:
  - Prevent hidden high-resistance joints

target:
  - Tab and current-collector welding

current_state:
  - SK On actual joining process and inline inspection are not disclosed

desired_state:
  - Every weld receives a quality probability and traceable signature

gap:
  - Destructive sampling cannot inspect every joint
  - Single process threshold may not capture material variation

possible_causes:
  - Tool wear
  - Surface contamination
  - Foil-thickness variation
  - Alignment variation

needed_capability:
  - Multi-signal welding monitoring
  - Resistance prediction
  - Tool-health estimation
  - Adaptive parameter window

external_technology:
  - Acoustic emission
  - Optical emission sensing
  - Edge AI
  - Ultrasonic NDI

partner_type:
  - Welding-equipment company
  - NDI company
  - Industrial AI startup

collaboration_model:
  - Joint development agreement
  - Battery-specific foreground IP

expected_kpi:
  - Weld defect escape
  - False reject
  - Tool life
  - Destructive-test reduction
  - Joint resistance variation

priority: VERY_HIGH
```

---

## OI-SEED-D06-011 — Pouch Forming Digital Twin

```yaml
seed_id: OI-SEED-D06-011
title: Pouch Forming and Corner-Thinning Digital Twin

strategy:
  - Reduce leakage risk and material scrap

target:
  - Aluminum-laminate pouch forming

current_state:
  - Pouch-cell manufacturing is confirmed
  - Forming-condition and defect data are not disclosed

desired_state:
  - Forming strain and corner thickness are predicted before production

gap:
  - Film-lot variation may require different process windows

possible_causes:
  - Material anisotropy
  - Die wear
  - Forming-depth change
  - Lubrication or friction variation

needed_capability:
  - Forming simulation
  - Film material fingerprint
  - Inline 3D shape measurement
  - Corner-thickness soft sensor

external_technology:
  - Finite-element simulation
  - 3D optical metrology
  - Material property AI

partner_type:
  - Packaging-material company
  - Forming-equipment company
  - Simulation software company

collaboration_model:
  - Material–process joint optimization
  - Shared foreground patent

expected_kpi:
  - Pouch crack rate
  - Corner-thickness variation
  - Forming scrap
  - Changeover time

priority: HIGH
```

---

## OI-SEED-D06-012 — Electrolyte Wetting Acceleration

```yaml
seed_id: OI-SEED-D06-012
title: Electrolyte Wetting Acceleration and Verification

strategy:
  - Shorten cell assembly and finishing lead time

target:
  - Electrolyte filling and wetting

current_state:
  - Electrolyte filling and wetting are general quality-critical processes
  - SK On recipe and wetting time are not disclosed

desired_state:
  - Minimum complete-wetting time is predicted for each cell
  - Incomplete wetting is detected before formation

gap:
  - Wetting is difficult to observe inside a sealed cell
  - Fixed soaking time may overprocess or underprocess cells

possible_causes:
  - Electrode porosity variation
  - Stack compression
  - Electrolyte viscosity
  - Trapped gas
  - Dose variation

needed_capability:
  - Non-invasive wetting sensor
  - Filling digital twin
  - Cell-specific soaking prediction
  - Vacuum-pressure optimization

external_technology:
  - Ultrasound imaging
  - Acoustic spectroscopy
  - Physics-informed simulation
  - Precision fluid dosing

partner_type:
  - Acoustic sensor company
  - Fluid-control company
  - University imaging laboratory

collaboration_model:
  - Joint PoC
  - Battery-specific inspection patent

expected_kpi:
  - Wetting time
  - Incomplete-wetting detection rate
  - Formation anomaly rate
  - Electrolyte consumption
  - Cell lead time

priority: VERY_HIGH
```

---

## OI-SEED-D06-013 — Cell Assembly Contamination Map

```yaml
seed_id: OI-SEED-D06-013
title: Cell Assembly Contamination Source Map

strategy:
  - Reduce foreign-particle-related safety risk

target:
  - Dry-room and cell-assembly equipment

current_state:
  - Cleanliness control is necessary
  - SK On contamination genealogy is not publicly confirmed

desired_state:
  - Particle source, movement and affected cell population are traceable

gap:
  - Particle measurement is often zone-based rather than object-based

possible_causes:
  - Tool wear
  - Electrode cutting dust
  - Packaging material
  - Personnel movement
  - Airflow

needed_capability:
  - Particle composition identification
  - Local particle sensing
  - Airflow simulation
  - Cell genealogy integration

external_technology:
  - Automated microscopy
  - Particle spectroscopy
  - Cleanroom digital twin

partner_type:
  - Contamination-analysis institute
  - Cleanroom engineering company
  - Sensor startup

collaboration_model:
  - Root-cause pilot
  - Analysis-service contract
  - Joint process patent where applicable

expected_kpi:
  - Particle excursion containment time
  - Affected cell population
  - Repeat contamination incidents
  - Cell assembly scrap

priority: VERY_HIGH
```

---

## OI-SEED-D06-014 — Seal Integrity Prediction

```yaml
seed_id: OI-SEED-D06-014
title: Pouch Seal Integrity Prediction

strategy:
  - Prevent microleak and electrolyte loss

target:
  - Temporary and final pouch sealing

current_state:
  - Seal quality can be evaluated by visual, leak and sampling tests
  - SK On inspection configuration is not disclosed

desired_state:
  - Seal quality is predicted from thermal and mechanical process signatures

gap:
  - Microleak may not be apparent in visual inspection

possible_causes:
  - Seal contamination
  - Temperature drift
  - Pressure nonuniformity
  - Pouch wrinkle
  - Tab interference

needed_capability:
  - Seal-bar pressure mapping
  - Thermal imaging
  - Seal-signature model
  - Rapid microleak test

external_technology:
  - Thin-film pressure sensor
  - Infrared inspection
  - Helium or alternative high-speed leak detection

partner_type:
  - Packaging inspection company
  - Leak-test equipment company
  - Sensor company

collaboration_model:
  - Equipment validation
  - Joint algorithm development

expected_kpi:
  - Microleak escape
  - Seal false reject
  - Seal rework
  - Inspection takt time

priority: HIGH
```

---

## OI-SEED-D06-015 — Assembly-to-Formation Genealogy

```yaml
seed_id: OI-SEED-D06-015
title: Assembly-to-Formation Root-Cause Graph

strategy:
  - Convert formation anomalies into upstream process learning

target:
  - Z-Folding, welding, pouch forming, filling and sealing

current_state:
  - Each process can generate equipment and quality data
  - Cross-process graph implementation is not publicly confirmed

desired_state:
  - A formation anomaly can be traced to affected material, position and process event

gap:
  - Cell-level electrical data and roll·stack·weld data may remain separated

possible_causes:
  - Different identifiers
  - Time-series misalignment
  - Missing coordinate genealogy
  - Inconsistent defect taxonomy

needed_capability:
  - Common manufacturing ontology
  - Event-based graph
  - Time-series synchronization
  - Probabilistic root-cause model

external_technology:
  - Knowledge graph
  - Manufacturing data platform
  - Causal AI

partner_type:
  - Industrial data-platform company
  - Graph AI startup
  - Digital-twin company

collaboration_model:
  - Data-platform PoC
  - SK On-owned manufacturing ontology

expected_kpi:
  - Root-cause analysis time
  - Containment time
  - Repeated defect rate
  - Scrap localization accuracy

priority: VERY_HIGH
```

---
