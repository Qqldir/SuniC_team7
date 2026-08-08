---
id: skon-d06-d06-08-electrode-manufacturing-digital-genealog
title: Electrode Manufacturing Digital Genealogy
summary: 전극 제조 과정에서 원재료부터 최종 배터리 셀까지의 계보를 추적하기 위한 디지털 데이터 구조와 프로세스 관계를 정의한 문서이다.
tags: [d06, process, schema, "xref:d04"]
keywords: [재료추적, Slurry, 코팅, 캘린더링, 품질검사, 배터리셀, 공정관계, Parameter, Traceability, 전극 제조, 제조 족보, 추적성, 슬러리 배합, 코팅 공정, 품질 검사, 원재료 로트, 프로세스 계보, 배터리 셀]
related: []
priority: normal
domain: D06
section: D06-08.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 738
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-08. Electrode Manufacturing Digital Genealogy

## 08.1 Genealogy Chain

```text
Supplier Material Lot
        ↓
Incoming Inspection Lot
        ↓
Dispensing Event
        ↓
Mixing Batch
        ↓
Slurry Tank
        ↓
Coating Run
        ↓
Master Electrode Roll
        ↓
Calender Run
        ↓
Slitted Roll
        ↓
Notched Electrode Lot
        ↓
Z-Folding Stack
        ↓
Cell Serial Number
```

```yaml
manufacturing_genealogy_minimum_keys:

  material:
    - Supplier ID
    - Supplier lot
    - Internal lot
    - Material specification version

  process:
    - Process ID
    - Equipment ID
    - Recipe version
    - Start and end time
    - Parameter time series

  intermediate_product:
    - Slurry batch ID
    - Coated-roll ID
    - Calendered-roll ID
    - Slitted-roll ID
    - Electrode lot ID

  quality:
    - Inspection result
    - Defect location
    - Disposition
    - Deviation approval

  final_link:
    - Cell serial
    - Module serial
    - Pack serial
```

---

## 08.2 Canonical Process Relationships

```yaml
process_relationship_triples:

  - edge_id: EDGE-D06-001
    subject: PROC-SKON-D06-003
    predicate: FEEDS
    object: PROC-SKON-D06-004
    source_ids:
      - SRC-BASE-D06-006
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-002
    subject: PROC-SKON-D06-004
    predicate: FEEDS
    object: PROC-SKON-D06-006
    source_ids:
      - SRC-BASE-D06-006
      - SRC-BASE-D06-007
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-003
    subject: PROC-SKON-D06-006
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-007
    source_ids:
      - SRC-BASE-D06-006
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-004
    subject: PROC-SKON-D06-007
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-008
    source_ids:
      - SRC-BASE-D06-006
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-005
    subject: PROC-SKON-D06-008
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-009
    source_ids:
      - SRC-BASE-D06-006
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-006
    subject: PROC-SKON-D06-008
    predicate: OPTIMIZED_BY
    object: TECH-SKON-D04-039
    source_ids:
      - SRC-SKON-D06-001
    evidence_level: DIRECT_OFFICIAL

  - edge_id: EDGE-D06-007
    subject: PROC-SKON-D06-009
    predicate: FOLLOWED_BY
    object: PROC-SKON-D06-010
    source_ids:
      - SRC-BASE-D06-006
    evidence_level: INDUSTRY_BASELINE

  - edge_id: EDGE-D06-008
    subject: PROC-SKON-D06-010
    predicate: FEEDS
    object: PROC-SKON-D06-011
    source_ids:
      - SRC-BASE-D06-006
      - SRC-SKON-D06-002
    evidence_level: MIXED
```

---
