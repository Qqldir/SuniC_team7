---
id: skon-d05-d05-53-patent-research-chunk-library-d05-003-pa-6
title: Patent & Research Chunk Library — D05-003 — Patent Ownership Normalization
summary: "SK이노베이션 명의 특허를 SK온으로 소급 표기하지 않고, 최초 출원인·현재 권리자·양도 이벤트를 분리 관리하는 정규화 규칙."
tags: [d05, rnd, schema]
keywords: [출원인, 권리자, 양도, 배터리 특허, SK이노베이션, SK온, 소급표기, 명의변경, 이전이벤트, 양도 이벤트, 소급 표기, 특허 이전, applicant normalization, assignment]
related: []
priority: normal
domain: D05
section: D05-53.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: Patent & Research Chunk Library
tokens: 307
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산 · Patent & Research Chunk Library

## CH-SKON-D05-003 — Patent Ownership Normalization

```yaml
chunk_id: CH-SKON-D05-003
title: SK이노베이션·SK온 특허 권리자 정규화
information_type: GOVERNANCE_RULE

chunk_text: >
  SK온 출범 전 배터리 특허는 최초 출원인이 SK이노베이션으로
  표시되고 이후 SK온으로 이전된 사례가 존재한다. 데이터베이스에서는
  최초 출원인, 현재 권리자와 양도이벤트를 분리한다. SK이노베이션
  명의 출원을 출원시점부터 SK온 특허로 소급 표기하지 않는다.

organization_ids:
  - APP-SKI-001
  - APP-SKON-001

source_ids:
  - D05-APPLICANT-NORMALIZATION
  - D05-ASSIGNMENT-LEDGER

legal_status_scope: AUDIT_REQUIRED
claim_status: SOURCE_SUPPORTED_FACT
confidence: VERY_HIGH

retrieval_tags:
  - 출원인
  - 권리자
  - 양도
  - SK이노베이션
  - SK온

exclusions:
  - 특허 미러만으로 현재 권리자 최종확정 금지
```

---
