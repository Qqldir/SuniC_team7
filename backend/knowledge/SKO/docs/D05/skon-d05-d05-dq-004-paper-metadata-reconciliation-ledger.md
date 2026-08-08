---
id: skon-d05-d05-dq-004-paper-metadata-reconciliation-ledger
title: 004. Paper Metadata Reconciliation Ledger
summary: SK온의 논문 메타데이터 정준 정책 및 LMRO·LLZO 연구성과 관련 메타데이터 불일치·미확정 이슈의 해결 기록이다.
tags: [d05, rnd, schema]
keywords: [메타데이터, 논문 데이터, 품질 관리, 저자 규칙, LMRO, LLZO, 전해질, 이온전도도, DOI, 불일치, 메타데이터 정책, 데이터 품질 이슈, 고체전해질, 논문 검증, 정준 메타데이터, 저자권 규칙]
related: []
priority: normal
domain: D05
section: D05-DQ
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 964
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 5. Paper·Research Output Master 및 Author Collaboration Network

**문서 버전:** D05 v1.4
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-28 Updated Patent Portfolio Snapshot`

---

# D05-DQ-004. Paper Metadata Reconciliation Ledger

```yaml
paper_metadata_policy:

  canonical_metadata_priority:
    1: Publisher journal page
    2: DOI registry
    3: University or research-institute publication record
    4: Official corporate article
    5: Secondary database

  source_grade_normalization:
    peer_reviewed_paper:
      source_grade: A
      evidence_level: THIRD_PARTY_VERIFIED

    official_company_article:
      source_grade: A
      evidence_level: DIRECT_OFFICIAL

  performance_boundary:
    required_fields:
      - Cell configuration
      - Electrode and electrolyte
      - Temperature
      - C-rate or current density
      - Cycle count
      - Comparison baseline
      - Research-cell or commercial-cell boundary

  authorship_rule:
    - Author and inventor are separate entities
    - Paper authorship does not establish patent inventorship
    - Corresponding author does not establish IP ownership
    - Joint publication does not establish equal patent ownership
```

## DQ-D05-PAPER-001 — LMRO 논문 링크 불일치

SK온 공식 기사에서는 LMRO 관련 연구가 `Advanced Energy Materials`에 게재됐다고 설명했지만, 해당 기사에 연결된 링크는 `Chemistry of Materials`의 LMRO 단결정 합성 논문으로 이어진다. 실제로 두 논문은 서로 다른 연구성과이므로 하나로 합치지 않는다. ([askinno.com][1])

```yaml
issue_id: DQ-D05-PAPER-001
issue: Corporate article journal statement and linked paper mismatch

corporate_statement:
  journal: Advanced Energy Materials
  research_topic:
    - LMRO degradation
    - Oxygen release
    - Sulfide electrolyte oxidation

linked_primary_paper:
  journal: Chemistry of Materials
  doi: 10.1021/acs.chemmater.4c01762
  research_topic:
    - Active-inactive molten salt synthesis
    - LMRO single-crystal particle formation

resolution:
  - Register the two papers separately
  - Use publisher metadata as canonical
  - Preserve the corporate-page mismatch
  - Do not transfer performance results between the papers

status: CONTROL_IMPLEMENTED
```

## DQ-D05-PAPER-002 — LLZO 논문 메타데이터 미확정

SK온은 단국대학교와 공동 개발한 LLZO계 고체전해질에 대해 `1.7mS/cm`의 이온전도도와 기존 대비 약 70% 개선 결과를 공개했다. 다만 현재 확보된 자료만으로는 이에 대응하는 학술논문의 제목·DOI·저자 전체를 확정하지 못했으므로 Paper Master에 정식 등재하지 않고 후보 레코드로 보존한다. ([askinno.com][1])

```yaml
issue_id: DQ-D05-PAPER-002
subject: LLZO oxide solid electrolyte paper

confirmed:
  - Joint research with Dankook University
  - Company-reported ionic conductivity result
  - Patent-family linkage exists

not_reconciled:
  - Canonical paper title
  - DOI
  - Journal
  - Full author list
  - Exact experimental boundary

handling:
  - Register as PAPER_CANDIDATE
  - Do not create paper-derived author edges
```

---
