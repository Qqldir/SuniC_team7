---
id: skon-d06-d06-dq-007-canonical-registry-correction
title: 007. Canonical Registry Correction
summary: "SK온 D06 제조공정 Canonical Registry의 소스 등급 재정규화, 특허 증거 제어, ID 오류 정정 등 데이터 품질 기준 문서."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [source_grade, 데이터 품질, canonical registry, 특허공보, 정규화, entity, D06, patent_mirror, 근거, 오류정정, 소스 등급, Source Grade, DQ, 특허 미러]
related: [PROC-SKON-D06-018C, SRC-SKON-D06-023]
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 964
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 7. Chunk Library·Graph Query·Relationship Graph·Final Quality Audit

**문서 버전:** D06 v1.6
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-56 Manufacturing OI Prioritization`
**신규 외부조사:** 없음
**근거 범위:** 기존 D04·D05·D06 Canonical Registry

---

# D06-DQ-007. Canonical Registry Correction

## DQ-D06-007-001 — Source Grade 재정규화

```yaml
source_grade_policy:

  A_PLUS:
    - Patent publications and official patent registers
    - Government and regulatory publications
    - International standards
    - Annual and regulatory reports

  A:
    - Official company newsroom and technology pages
    - Peer-reviewed academic papers
    - Public research institutes
    - Official technology-vendor pages

  B_PLUS:
    - Reuters
    - Bloomberg
    - Financial Times
    - Wall Street Journal

  B:
    - Industry associations
    - Reputable consulting firms

  C:
    - General press used only for corroboration
```

따라서 D06에서 학술논문이라는 이유만으로 `source_grade: A_PLUS`를 부여한 레코드는 `A`로 변경한다. 정부기관이 직접 발행한 보고서와 국제표준은 `A_PLUS`를 유지한다.

```yaml
migration:

  peer_reviewed_sources_to_A:
    - SRC-BASE-D06-007
    - SRC-BASE-D06-008
    - SRC-BASE-D06-012
    - SRC-BASE-D06-013
    - SRC-BASE-D06-014
    - SRC-BASE-D06-015
    - SRC-BASE-D06-016
    - SRC-BASE-D06-017
    - SRC-BASE-D06-023

  government_reports_remain_A_PLUS:
    - SRC-BASE-D06-006
    - SRC-BASE-D06-009
    - SRC-BASE-D06-010
    - SRC-ANL-D06-037

  standards_remain_A_PLUS:
    - SRC-STD-D06-033
    - SRC-STD-D06-034
    - SRC-NIST-D06-035
    - SRC-NIST-D06-036
```

---

## DQ-D06-007-002 — 특허 미러와 특허공보 분리

```yaml
patent_evidence_control:

  underlying_document:
    type: OFFICIAL_PATENT_PUBLICATION
    source_grade: A_PLUS
    evidence_level: DIRECT_REGULATORY

  retrieval_channel:
    example: PATENT_MIRROR
    independent_source_grade: NOT_APPLICABLE

  document_content_allowed:
    - Published applicant
    - Published inventor
    - Specification
    - Claims
    - Publication metadata

  legal_status_not_allowed_without_register:
    - Current enforceability
    - Current owner
    - Maintenance-fee status
    - Exact expiration
    - National validation
```

---

## DQ-D06-007-003 — X-ray Source ID 오류

`PROC-SKON-D06-018C`에 포함됐던 `SRC-SKON-D06-023`은 D06 Source Registry에 정의되지 않은 ID다.

```yaml
correction:

  affected_process:
    - PROC-SKON-D06-018C

  remove:
    - SRC-SKON-D06-023

  corrected_source_ids:
    - SRC-SKON-D06-022
    - PF-SKON-D05-030
    - PF-SKON-D05-031

  interpretation:
    - Integrated inspection and sorting is supported by SRC-SKON-D06-022
    - Detailed X-ray architectures are supported by the two patent families
```

---

## DQ-D06-007-004 — 최종 Entity Count

```yaml
canonical_registry_count:

  source_records: 37

  process_entities:
    total_including_parent_aggregates: 42
    parent_aggregate_processes:
      - PROC-SKON-D06-019
      - PROC-SKON-D06-020
      - PROC-SKON-D06-021

  defect_entities: 20
  pain_point_entities: 22
  oi_seed_entities: 49

  actual_sk_on_operational_kpis:
    count: 0
    reason: NOT_PUBLICLY_DISCLOSED
```

---
