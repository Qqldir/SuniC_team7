---
id: skon-d06-d06-36-module-pack-defect-graph
title: Module·Pack Defect Graph
summary: "배터리 모듈·팩 제조 공정에서 발생하는 셀 매칭오류, 압축 불균일, 열차단재 조립불량, 버스바 접합불량 등 주요 불량의 원인, 증상, 영향을 체계적으로 정의한 결함 카탈로그."
tags: [d06, process, schema]
keywords: [결함 분류, DEF-D06, 셀 매칭오류, 압축 불균일, 열차단재, 버스바 접합, 열전도계면, 모듈 팩, 제조불량, D06 공정, 버스바 접합불량, 열차단재 조립, 열계면 공극, 불량 원인, 공정 이상, Cell matching, Busbar joint, 품질 검사]
related: []
priority: normal
domain: D06
section: D06-36.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2042
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-36. Module·Pack Defect Graph

## DEF-D06-012 — Cell Matching Error

```yaml
defect_id: DEF-D06-012
canonical_name: Module or Pack Cell Matching Error
korean_name: 셀 매칭오류

detected_process_ids:
  - PROC-SKON-D06-019A
  - PROC-SKON-D06-021D

possible_causes:
  - Grade-data mismatch
  - Serial-scan failure
  - Wrong buffer bin
  - Manual substitution
  - Outdated matching rule

observable_signals:
  - Capacity-class mismatch
  - Resistance-class mismatch
  - OCV deviation
  - Serial-position inconsistency

potential_effects:
  - Pack imbalance
  - Reduced usable capacity
  - Increased balancing burden

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-SKON-D06-024
```

---

## DEF-D06-013 — Compression Nonuniformity

```yaml
defect_id: DEF-D06-013
canonical_name: Cell-Stack Compression Nonuniformity
korean_name: 셀 적층 압축 불균일

detected_process_ids:
  - PROC-SKON-D06-019B
  - PROC-SKON-D06-020E

possible_causes:
  - Cell-thickness variation
  - Missing or wrong pad
  - Fixture misalignment
  - Uneven case dimensions
  - Excessive or insufficient compression

observable_signals:
  - Force–displacement anomaly
  - Stack tilt
  - Local pressure difference
  - Unit dimension deviation

potential_effects:
  - Uneven swelling constraint
  - Uneven thermal contact
  - Mechanical cell damage

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-PAT-D06-029
  - SRC-SKON-D06-026
```

---

## DEF-D06-014 — Thermal Barrier Installation Defect

```yaml
defect_id: DEF-D06-014
canonical_name: Thermal-Barrier Installation Defect
korean_name: 열차단재 조립불량

detected_process_ids:
  - PROC-SKON-D06-019B
  - PROC-SKON-D06-020D

possible_causes:
  - Missing barrier
  - Incomplete insertion
  - Barrier damage
  - Wrong position
  - Excessive insertion force

observable_signals:
  - Height deviation
  - Pressure-signature anomaly
  - Vision failure
  - Material-presence error

potential_effects:
  - Reduced thermal-isolation performance
  - Cell compression variation
  - Gas-path interference

source_ids:
  - SRC-PAT-D06-029

evidence_level: DIRECT_REGULATORY
```

---

## DEF-D06-015 — Busbar Joint Defect

```yaml
defect_id: DEF-D06-015
canonical_name: Module or Pack Busbar Joint Defect
korean_name: 버스바 접합불량

detected_process_ids:
  - PROC-SKON-D06-019C
  - PROC-SKON-D06-020C
  - PROC-SKON-D06-021D

possible_causes:
  - Lead misalignment
  - Surface contamination
  - Joining-energy drift
  - Insufficient overlap
  - Tool or optical-head drift

observable_signals:
  - High joint resistance
  - Weld-signature anomaly
  - Spatter
  - Lead tearing
  - Thermal hotspot

potential_effects:
  - Local heat generation
  - Voltage loss
  - Open-circuit or intermittent connection
  - Pack reject

source_ids:
  - SRC-PAT-D06-028

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-016 — Thermal Interface Void

```yaml
defect_id: DEF-D06-016
canonical_name: Thermal-Interface Void or Incomplete Contact
korean_name: 열전도계면 공극·접촉불량

detected_process_ids:
  - PROC-SKON-D06-019D
  - PROC-SKON-D06-020B
  - PROC-SKON-D06-020E

possible_causes:
  - Under-dispensing
  - Trapped air
  - Uneven cell surface
  - Insufficient compression
  - Premature adhesive curing

observable_signals:
  - Dispense-mass deviation
  - Thermal-response nonuniformity
  - Ultrasound or X-ray void
  - Local temperature rise

potential_effects:
  - Uneven cooling
  - Local cell aging
  - Reduced fast-charge capability

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-SKON-D06-025
  - SRC-SKON-D06-026
  - SRC-PAT-D06-027
```

---

## DEF-D06-017 — Cooling-Circuit Leak or Flow Defect

```yaml
defect_id: DEF-D06-017
canonical_name: Cooling-Circuit Leak or Flow Defect
korean_name: 냉각회로 누설·유량불량

detected_process_ids:
  - PROC-SKON-D06-019D
  - PROC-SKON-D06-021C
  - PROC-SKON-D06-021D

possible_causes:
  - Connector assembly error
  - Gasket damage
  - Channel blockage
  - Welding or brazing defect
  - Air pocket

observable_signals:
  - Pressure decay
  - Low flow
  - High pressure drop
  - Coolant trace
  - Thermal-response deviation

potential_effects:
  - Insufficient cooling
  - Electrical-isolation risk
  - Pack leakage
  - Pack reject

source_ids:
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-018 — Sensing·Harness Connection Defect

```yaml
defect_id: DEF-D06-018
canonical_name: Sensing and Harness Connection Defect
korean_name: 센싱·하네스 연결불량

detected_process_ids:
  - PROC-SKON-D06-019E
  - PROC-SKON-D06-021B
  - PROC-SKON-D06-021D

possible_causes:
  - Connector not seated
  - Pin damage
  - Wrong channel mapping
  - FPCB damage
  - Harness pinching

observable_signals:
  - Open voltage channel
  - Implausible temperature
  - Communication fault
  - Intermittent signal

potential_effects:
  - Incorrect BMS decision
  - Pack EoL failure
  - Reduced diagnostic coverage

source_ids:
  - SRC-PAT-D06-028

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-019 — CTP Placement Defect

```yaml
defect_id: DEF-D06-019
canonical_name: CTP Direct-Installation Defect
korean_name: CTP 직접 탑재불량

detected_process_ids:
  - PROC-SKON-D06-020B
  - PROC-SKON-D06-021D

possible_causes:
  - Housing dimensional variation
  - Robot-position error
  - Thermal-interface displacement
  - Side-cover interference
  - Excessive insertion force

observable_signals:
  - Force–position anomaly
  - Assembly-coordinate deviation
  - Insulation failure
  - Thermal-contact deviation

potential_effects:
  - Cell damage
  - Cooling degradation
  - Structural weakness
  - Difficult rework

source_ids:
  - SRC-PAT-D06-027

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-020 — Pack Configuration or Software Error

```yaml
defect_id: DEF-D06-020
canonical_name: Pack Configuration or Software Error
korean_name: 팩 구성·소프트웨어 오류

detected_process_id:
  - PROC-SKON-D06-021D

possible_causes:
  - Incorrect firmware
  - Wrong calibration
  - Serial genealogy mismatch
  - Incorrect electrical configuration
  - Unapproved component revision

observable_signals:
  - Checksum mismatch
  - Sensor plausibility error
  - Unexpected topology
  - Diagnostic-code failure

potential_effects:
  - Incorrect BMS operation
  - Customer-interface failure
  - Shipping hold

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-PAT-D06-028
```

---

## 36.1 Cross-Process Defect Graph

```text
Cell Grading and Matching
        ↓
Module / CTP Cell Assignment
        ↓
Electrical and Aging Imbalance
        ↓
Pack Balancing Burden
```

```text
Cell Thickness·Pad Variation
        ↓
Compression Nonuniformity
        ↓
Thermal Contact Variation
        ↓
Local Temperature and Aging Difference
```

```text
Thermal Adhesive Dispensing
        ↓
Void or Uneven Bond Line
        ↓
Cooling Nonuniformity
        ↓
Local Cell Temperature Rise
```

```text
Busbar Joining·Sensing Connection
        ↓
Resistance or Channel Defect
        ↓
Pack EoL Electrical Failure
        ↓
Rework / Scrap / Engineering Hold
```

```text
CTP Direct Installation
        ↓
Pack-Level Integrated Defect
        ↓
Difficult Module-Level Replacement
        ↓
High Rework Cost
```

---
