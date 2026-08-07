---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-024-cros-26
title: Manufacturing Chunk Library — D06-024 — Cross-Plant Recipe Transfer
summary: 기준공장의 레시피를 다른 공장에 이전할 때 설비·원료·환경 차이를 정규화하고 재검증해야 한다는 제조 공정 거버넌스 규칙
tags: [d06, process, schema]
keywords: [공장 간 레시피 이전, Recipe 이전, Cross-Plant, 설정값 복사 금지, 정규화, 재검증, Golden Batch, 설비 차이, 기준공장, 크로스플랜트, 레시피 정규화, 설정값 복사, 열응답, 원료 표준화, 센서 캘리브레이션, 공정 재검증]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 234
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-024 — Cross-Plant Recipe Transfer

```yaml
chunk_id: CH-SKON-D06-024
title: 공장 간 Recipe·모델 이전
information_type: GOVERNANCE_RULE

chunk_text: >
  기준공장의 숫자 설정값을 다른 공장에 그대로 복사해서는 안 된다.
  동일 품질목표를 기준으로 설비크기·열응답·센서·원료·환경 차이를
  정규화하고 대상라인에서 재검증해야 한다. Golden Batch는 참조점일
  뿐 공정창 전체를 대신하지 않는다.

oi_seed_ids:
  - OI-SEED-D06-047
  - OI-SEED-D06-048
  - OI-SEED-D06-049

source_ids:
  - SRC-SIEMENS-D06-032
  - SRC-STD-D06-033

evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
