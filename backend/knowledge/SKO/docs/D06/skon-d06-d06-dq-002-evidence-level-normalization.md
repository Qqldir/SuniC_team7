---
id: skon-d06-d06-dq-002-evidence-level-normalization
title: 002. Evidence-Level Normalization
summary: SK온 D06의 기존 임시 증거등급을 프로젝트 표준 어휘로 정규화하는 변환 규칙 및 허용 증거등급을 정의한다.
tags: [d06, process, schema]
keywords: [증거 분류, DIRECT_OFFICIAL, THIRD_PARTY_VERIFIED, ANALYST_INFERENCE, vocabulary 표준화, 제조공정 표준, INDUSTRY_BASELINE, 매핑 규칙, D06-DQ, 증거등급 변환, 증거등급, 정규화, 메타데이터, 데이터 마이그레이션, Evidence-Level, 표준화, 제조공정, D06, 데이터 거버넌스, 변환 규칙]
related: []
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 289
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 2. Dry-Room·Cell Assembly·Electrolyte Filling·Assembly Defect Graph

**문서 버전:** D06 v1.1
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-10 Initial Manufacturing OI Seeds`

---

# D06-DQ-002. Evidence-Level Normalization

이전 D06 레코드에서 사용한 일부 임시 증거등급을 프로젝트 공통 Vocabulary에 맞춰 정규화한다.

```yaml
evidence_level_migration:

  INDUSTRY_BASELINE:
    corrected_to: THIRD_PARTY_VERIFIED
    applies_to:
      - Peer-reviewed manufacturing review
      - Government-laboratory technical study
      - General lithium-ion manufacturing process

  DIRECT_CORPORATE_COMMUNICATION:
    corrected_to: DIRECT_OFFICIAL

  MIXED:
    corrected_to: ANALYST_INFERENCE
    requirement:
      - basis_source_ids
      - basis_edge_ids

allowed_evidence_levels:
  - DIRECT_REGULATORY
  - DIRECT_OFFICIAL
  - THIRD_PARTY_VERIFIED
  - ANALYST_INFERENCE
  - HYPOTHESIS
```

---
