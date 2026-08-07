---
id: skon-d05-d05-dq-005-patent-evidence-source-grade-correct
title: 005. Patent Evidence & Source Grade Correction Ledger
summary: Google Patents 기반 특허 레코드의 신뢰도 등급을 정정하고 각 정보원별 사용 가능한 증거 범위를 규정한 지침.
tags: [d05, rnd, schema]
keywords: [출처 등급, 신뢰도, source_grade, 공식 등록부, 법적 상태, 특허 미러, Google Patents, KIPRIS, 존속판단, 증거 수준, 특허정보원, 법적상태, USPTO, EPO, 특허미러, 신뢰도등급, 마이그레이션]
related: []
priority: normal
domain: D05
section: D05-DQ
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 730
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 7. Legal-Status Audit Batch 2·Claim-Scope Mapping·IP White Space

**문서 버전:** D05 v1.6
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-42 Integrated Gap Register Update`

---

# D05-DQ-005. Patent Evidence & Source Grade Correction Ledger

기존 D05 일부 레코드에서 Google Patents를 통해 확인한 문서에 `source_grade: A_PLUS`, `evidence_level: DIRECT_REGULATORY`를 부여했으나, 이를 아래와 같이 정정한다.

```yaml
patent_source_correction:

  official_register:
    examples:
      - KIPRIS
      - USPTO Patent Center
      - European Patent Register
      - WIPO PATENTSCOPE
    source_grade: A_PLUS
    permitted_evidence:
      - Official procedural status
      - Official ownership record
      - Grant or lapse status
      - Official application history

  official_patent_publication:
    examples:
      - EPO Publication Server PDF
      - USPTO Patent Gazette
      - WIPO publication document
      - KIPO publication document
    source_grade: A_PLUS
    permitted_evidence:
      - Bibliographic data
      - Specification
      - Claims
      - Applicant and inventor as published

  patent_document_mirror:
    examples:
      - Google Patents
    retrieval_source_grade: A
    document_nature: PATENT_PUBLICATION_REPRODUCTION
    evidence_level: DOCUMENT_TEXT_REPRODUCTION
    permitted_evidence:
      - Claim and specification discovery
      - Family navigation
      - Preliminary event history
    prohibited_evidence:
      - Final legal-status determination
      - Definitive current ownership determination
      - Definitive expiration determination

migration_actions:
  - Google Patents 기반 A_PLUS 레코드를 retrieval_source_grade A로 변경
  - legal_status_source를 AGGREGATOR_SNAPSHOT으로 변경
  - 특허문서의 기술내용과 법적 상태의 증거필드를 분리
  - 공식 등록부 확인 전 GRANTED_ACTIVE 대신 GRANT_DOCUMENT_IDENTIFIED 사용
```

EPO는 European Patent Register를 유럽 출원의 절차상태를 확인하는 공식 정보원으로 설명하고 있으며, 미국은 USPTO Patent Public Search와 Patent Center, 한국은 KIPRIS를 통해 공식 기록을 확인해야 한다. 따라서 특허 미러의 이벤트 기록은 탐색에는 활용하되 최종 존속판단에는 사용하지 않는다. ([미국 특허청][1])

---
