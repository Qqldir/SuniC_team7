---
id: skon-d06-d06-17-cell-assembly-defect-graph
title: Cell Assembly Defect Graph
summary: "배터리 셀 조립 공정에서 발생하는 전극 정렬, 용접, 파우치 성형 등 결함의 원인, 검출 방법, 영향을 분류·정의한 결함 맵핑 자료."
tags: [d06, process, schema]
keywords: [전극 정렬불량, 용접불량, 파우치 성형불량, 배터리 제조공정, 공정 결함, 검출 방법, Electrode Misalignment, D06, 불량 원인 분석, 품질 관리, 셀 조립 결함, 파우치 성형, 결함 검출, 공정 원인, 품질 기준, D06 공정, 불량 판정, 결함 데이터]
related: []
priority: normal
domain: D06
section: D06-17.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1785
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-17. Cell Assembly Defect Graph

## 17.1 Canonical Defect Entity Schema

```yaml
cell_assembly_defect_schema:

  defect_id: required
  canonical_name: required

  detected_process_id: required

  possible_origin_process_ids:
    type: array

  possible_causes:
    type: array

  observable_signals:
    type: array

  potential_effects:
    type: array

  detection_methods:
    type: array

  containment_action:
    type: array

  evidence_level:
    allowed_values:
      - DIRECT_OFFICIAL
      - THIRD_PARTY_VERIFIED
      - ANALYST_INFERENCE
      - HYPOTHESIS

  source_ids:
    required: true
```

---

## DEF-D06-001 — Electrode Misalignment

```yaml
defect_id: DEF-D06-001
canonical_name: Electrode Stack Misalignment
korean_name: 전극 적층 정렬불량

detected_process_id:
  - PROC-SKON-D06-011

possible_origin_process_ids:
  - PROC-SKON-D06-009
  - PROC-SKON-D06-011

possible_causes:
  - Electrode dimension variation
  - Vision calibration drift
  - Robot placement error
  - Separator tension variation
  - Electrode curl

observable_signals:
  - X or Y offset
  - Rotation angle
  - Separator-overhang reduction
  - Stack edge irregularity

potential_effects:
  - Reduced design margin
  - Potential separator damage
  - Potential local current-density variation

detection_methods:
  - Vision inspection
  - X-ray inspection
  - Stack-dimension measurement

source_ids:
  - SRC-SKON-D06-011
  - SRC-BASE-D06-012

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-002 — Weld Defect

```yaml
defect_id: DEF-D06-002
canonical_name: Electrode Tab Weld Defect
korean_name: 전극 탭 용접불량

detected_process_id:
  - PROC-SKON-D06-012

possible_causes:
  - Surface contamination
  - Incorrect weld energy
  - Tab misalignment
  - Tool wear
  - Material-thickness variation

observable_signals:
  - Abnormal weld signature
  - High electrical resistance
  - Low mechanical strength
  - Spatter
  - Foil tearing

potential_effects:
  - Local heat generation
  - Voltage loss
  - Intermittent electrical connection
  - Cell rejection

detection_methods:
  - Resistance measurement
  - Vision
  - Signature analysis
  - Pull-test sampling
  - X-ray or ultrasound

source_ids:
  - SRC-BASE-D06-015

evidence_level: THIRD_PARTY_VERIFIED
```

---

## DEF-D06-003 — Pouch Forming Defect

```yaml
defect_id: DEF-D06-003
canonical_name: Pouch Forming Defect
korean_name: 파우치 성형불량

detected_process_id:
  - PROC-SKON-D06-013

possible_causes:
  - Excessive forming depth
  - Material variation
  - Die wear
  - Film misalignment
  - Foreign particle

observable_signals:
  - Corner thinning
  - Wrinkle
  - Crack
  - Pinhole
  - Cavity-dimension deviation

potential_effects:
  - Leakage risk
  - Moisture-ingress risk
  - Stack-compression variation

detection_methods:
  - Vision
  - Dimensional measurement
  - Leak testing
  - Thickness sampling

source_ids:
  - SRC-BASE-D06-012

evidence_level: ANALYST_INFERENCE
```

---

## DEF-D06-004 — Incomplete Electrolyte Wetting

```yaml
defect_id: DEF-D06-004
canonical_name: Incomplete Electrolyte Wetting
korean_name: 전해액 불완전 함침

detected_process_id:
  - PROC-SKON-D06-014
  - PROC-SKON-D06-015

possible_origin_process_ids:
  - PROC-SKON-D06-008
  - PROC-SKON-D06-011
  - PROC-SKON-D06-014

possible_causes:
  - Low electrode porosity
  - Nonuniform compression
  - Insufficient dose
  - Insufficient vacuum or pressure
  - Insufficient soaking time
  - Trapped gas

observable_signals:
  - Cell-weight deviation
  - Formation-voltage anomaly
  - Resistance variation
  - Local dry zone in research imaging

potential_effects:
  - Initial capacity variation
  - Resistance variation
  - Extended formation or aging time
  - Cell rejection

detection_methods:
  - Weight verification
  - Formation-curve analysis
  - Acoustic or ultrasound candidate
  - Research imaging

source_ids:
  - SRC-BASE-D06-013
  - SRC-BASE-D06-014

evidence_level: THIRD_PARTY_VERIFIED
```

---

## DEF-D06-005 — Temporary Seal Leak

```yaml
defect_id: DEF-D06-005
canonical_name: Temporary Seal Leakage
korean_name: 임시 실링 누설

detected_process_id:
  - PROC-SKON-D06-014A

possible_causes:
  - Electrolyte contamination
  - Seal wrinkle
  - Insufficient heat or pressure
  - Tab-position interference
  - Pouch-film damage

observable_signals:
  - Pressure-decay failure
  - Weight loss
  - Visible electrolyte
  - Seal-width anomaly

potential_effects:
  - Electrolyte loss
  - Environmental contamination
  - Formation inconsistency
  - Cell scrap

source_ids:
  - SRC-BASE-D06-014

evidence_level: ANALYST_INFERENCE
```

---

## 17.2 Cross-Process Defect Graph

```text
Electrode Coating·Calendering
          ↓
Porosity and Thickness Distribution
          ↓
Z-Folding Stack Compression
          ↓
Electrolyte Wetting Distribution
          ↓
Formation Resistance and Capacity Distribution
```

```text
Slitting·Notching
          ↓
Electrode Edge Burr·Particle
          ↓
Z-Folding and Stack Insertion
          ↓
Potential Separator Damage
          ↓
Potential Electrical Isolation Defect
```

```text
Tab Joining
          ↓
Weld Resistance·Mechanical Strength
          ↓
Formation and End-of-Line Electrical Result
          ↓
Cell Grade or Scrap Decision
```

---

## 17.3 Defect–Cause Relationship Triples

```yaml
cell_assembly_defect_edges:

  - edge_id: EDGE-D06-009
    subject: PROC-SKON-D06-011
    predicate: MAY_GENERATE
    object: DEF-D06-001
    evidence_level: ANALYST_INFERENCE
    basis_source_ids:
      - SRC-SKON-D06-011
      - SRC-BASE-D06-012

  - edge_id: EDGE-D06-010
    subject: PROC-SKON-D06-012
    predicate: MAY_GENERATE
    object: DEF-D06-002
    source_ids:
      - SRC-BASE-D06-015
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-011
    subject: PROC-SKON-D06-013
    predicate: MAY_GENERATE
    object: DEF-D06-003
    evidence_level: ANALYST_INFERENCE
    basis_source_ids:
      - SRC-BASE-D06-012

  - edge_id: EDGE-D06-012
    subject: PROC-SKON-D06-008
    predicate: MAY_CONTRIBUTE_TO
    object: DEF-D06-004
    source_ids:
      - SRC-BASE-D06-013
      - SRC-BASE-D06-014
    evidence_level: THIRD_PARTY_VERIFIED

  - edge_id: EDGE-D06-013
    subject: PROC-SKON-D06-014A
    predicate: MAY_GENERATE
    object: DEF-D06-005
    evidence_level: ANALYST_INFERENCE
    basis_source_ids:
      - SRC-BASE-D06-014
```

---
