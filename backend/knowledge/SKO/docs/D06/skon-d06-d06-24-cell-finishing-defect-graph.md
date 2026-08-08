---
id: skon-d06-d06-24-cell-finishing-defect-graph
title: Cell Finishing Defect Graph
summary: "배터리 셀 완성 공정에서 발생 가능한 5가지 결함(포메이션 곡선 이상, 과다 가스, 실링 누설, 자가방전, 용량·저항 등급 이상)의 원인, 검출 신호, 검출 방법을 정의한 매핑 문서."
tags: [d06, process, schema]
keywords: [포메이션 곡선, 실링 미세누설, 자가방전, 과다 가스, 용량 저항 등급, 누설 탐지, 이상 탐지, 배터리 불량, OCV 감소, 공정 진단, 배터리 셀 결함, 포메이션 곡선 이상, 실링 누설, 결함 검출, 완성 공정, 용량 저항 이상, D06 공정]
related: []
priority: normal
domain: D06
section: D06-24.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1735
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-24. Cell Finishing Defect Graph

## DEF-D06-006 — Formation Curve Abnormality

```yaml
defect_id: DEF-D06-006
canonical_name: Formation Curve Abnormality
korean_name: 포메이션 곡선 이상

detected_process_id:
  - PROC-SKON-D06-015

possible_origin_process_ids:
  - PROC-SKON-D06-011
  - PROC-SKON-D06-012
  - PROC-SKON-D06-014
  - PROC-SKON-D06-015

possible_causes:
  - Incomplete wetting
  - Weld resistance
  - Internal leakage
  - Formation-channel contact error
  - Material variation

observable_signals:
  - Abnormal voltage rise
  - Abnormal voltage drop
  - Capacity deviation
  - Temperature anomaly
  - Pressure-response anomaly

detection_methods:
  - Curve comparison
  - Relative cell comparison
  - Multivariate anomaly model

source_ids:
  - SRC-SKON-D06-018
  - SRC-BASE-D06-016

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-007 — Excessive Formation Gas

```yaml
defect_id: DEF-D06-007
canonical_name: Excessive Formation Gas or Swelling
korean_name: 포메이션 과다 가스·팽창

detected_process_id:
  - PROC-SKON-D06-015
  - PROC-SKON-D06-016

possible_causes:
  - Electrolyte side reaction
  - Residual moisture
  - Formation-protocol mismatch
  - Contamination
  - Incomplete wetting

observable_signals:
  - Thickness increase
  - Pressure increase
  - High extracted-gas volume
  - Abnormal cell mass change

potential_effects:
  - Degassing overload
  - Final thickness variation
  - Seal contamination
  - Cell rejection

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-016
```

---

## DEF-D06-008 — Final Seal Microleak

```yaml
defect_id: DEF-D06-008
canonical_name: Final Seal Microleak
korean_name: 최종 실링 미세누설

detected_process_id:
  - PROC-SKON-D06-016
  - PROC-SKON-D06-018B

possible_causes:
  - Electrolyte contamination in seal
  - Seal-temperature variation
  - Nonuniform seal pressure
  - Pouch wrinkle
  - Pouch material damage

observable_signals:
  - Pressure-decay failure
  - Tracer-gas signal
  - Cell weight change
  - Delayed swelling or drying

source_ids:
  - SRC-SKON-D06-021

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-009 — Excessive Self-Discharge

```yaml
defect_id: DEF-D06-009
canonical_name: Excessive Self-Discharge
korean_name: 과도한 자가방전

detected_process_id:
  - PROC-SKON-D06-017

possible_causes:
  - Internal leakage path
  - Micro-short
  - Contamination
  - Electrochemical instability
  - Measurement error

observable_signals:
  - Excessive OCV decay
  - Abnormal relaxation curve
  - Peer-group outlier
  - Delayed temperature anomaly

potential_effects:
  - Aging extension
  - Cell rejection
  - Pack imbalance risk if undetected

evidence_level: THIRD_PARTY_VERIFIED
source_ids:
  - SRC-BASE-D06-016
  - SRC-BASE-D06-017
```

---

## DEF-D06-010 — Capacity or Resistance Outlier

```yaml
defect_id: DEF-D06-010
canonical_name: Capacity or Resistance Grade Outlier
korean_name: 용량·저항 등급 이상

detected_process_id:
  - PROC-SKON-D06-018

possible_origin_process_ids:
  - PROC-SKON-D06-004
  - PROC-SKON-D06-006
  - PROC-SKON-D06-008
  - PROC-SKON-D06-014
  - PROC-SKON-D06-015

possible_causes:
  - Electrode loading variation
  - Calendering variation
  - Electrolyte wetting variation
  - Material-lot variation
  - Formation-protocol deviation
  - Tester calibration error

observable_signals:
  - Low capacity
  - High DCIR
  - Low efficiency
  - Abnormal thermal response

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-017
  - SRC-BASE-D06-023
```

---

## DEF-D06-011 — Internal Structural Defect

```yaml
defect_id: DEF-D06-011
canonical_name: Internal Cell Structural Defect
korean_name: 셀 내부 구조결함

detected_process_id:
  - PROC-SKON-D06-018C

possible_origin_process_ids:
  - PROC-SKON-D06-009
  - PROC-SKON-D06-011
  - PROC-SKON-D06-012
  - PROC-SKON-D06-013

possible_causes:
  - Electrode misalignment
  - Fold error
  - Tab displacement
  - Burr or foreign particle
  - Stack insertion damage

observable_signals:
  - X-ray geometry deviation
  - Abnormal edge position
  - Suspected foreign object
  - Tab-region anomaly

source_ids:
  - SRC-SKON-D06-022

evidence_level: DIRECT_OFFICIAL
```

---

## 24.1 Cross-Process Defect Graph

```text
Coating·Calendering Variation
            ↓
Electrode Capacity·Porosity Variation
            ↓
Wetting and Formation Variation
            ↓
Capacity·Resistance Grade Outlier
```

```text
Z-Folding·Tab Joining Defect
            ↓
Internal Geometry or Resistance Anomaly
            ↓
Formation·X-Ray·Thermal Signal
            ↓
Hold / Retest / Reject
```

```text
Formation Side Reaction
            ↓
Gas Generation and Swelling
            ↓
Degassing·Seal Burden
            ↓
Thickness or Leakage Defect
```

```text
Final Seal Microdefect
            ↓
Electrolyte or Moisture Exchange
            ↓
Delayed OCV·Weight·Swelling Change
            ↓
Aging or EoL Detection
```

---

## 24.2 Defect Relationship Triples

```yaml
cell_finishing_defect_edges:

  - edge_id: EDGE-D06-014
    subject: PROC-SKON-D06-014
    predicate: MAY_CONTRIBUTE_TO
    object: DEF-D06-006
    source_ids:
      - SRC-BASE-D06-014
      - SRC-SKON-D06-018
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-015
    subject: PROC-SKON-D06-015
    predicate: MAY_GENERATE
    object: DEF-D06-007
    source_ids:
      - SRC-BASE-D06-016
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-016
    subject: PROC-SKON-D06-016
    predicate: MAY_GENERATE
    object: DEF-D06-008
    source_ids:
      - SRC-SKON-D06-021
    evidence_level: ANALYST_INFERENCE

  - edge_id: EDGE-D06-017
    subject: PROC-SKON-D06-017
    predicate: DETECTS
    object: DEF-D06-009
    source_ids:
      - SRC-BASE-D06-017
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-018
    subject: PROC-SKON-D06-018
    predicate: DETECTS
    object: DEF-D06-010
    source_ids:
      - SRC-BASE-D06-023
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-019
    subject: PROC-SKON-D06-018C
    predicate: DETECTS
    object: DEF-D06-011
    source_ids:
      - SRC-SKON-D06-022
    evidence_level: DIRECT_OFFICIAL
```

---
