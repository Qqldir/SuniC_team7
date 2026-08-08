---
id: skon-d06-d06-57-manufacturing-chunk-library-d06-025-ot-m-27
title: Manufacturing Chunk Library — D06-025 — OT·Manufacturing AI Governance
summary: PLC·로봇 등 제조 시스템 연결 환경에서 OT 보안 격리와 제조 AI 모델의 버전·드리프트·롤백을 관리하기 위한 필수 통제 및 기록 요구사항
tags: [d06, process, schema]
keywords: [PLC, 로봇 보안, MES, OT Zone, 원격접속 승인, 모델 버전, Drift 모니터링, Rollback, OT 보안, Zone 격리, 제조 AI 모델, 데이터셋 버전, 드리프트 감시, 변경 통제, 롤백 복구, Recipe 관리, PLC·로봇]
related: []
priority: normal
domain: D06
section: D06-57.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: Manufacturing Chunk Library
tokens: 225
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영 · Manufacturing Chunk Library

## CH-SKON-D06-025 — OT·Manufacturing AI Governance

```yaml
chunk_id: CH-SKON-D06-025
title: OT 보안과 제조 AI 관리
information_type: GOVERNANCE_RULE

chunk_text: >
  PLC·Robot·Inspection·MES 연결에서는 OT Zone 분리, 승인된
  원격접속, Logic·Recipe·Model 변경관리와 복구 가능한 백업이
  필요하다. 제조 AI는 Dataset·Model Version, 적용가능 제품과
  Recipe, Drift, Override와 Rollback을 기록해야 한다.

process_ids:
  - PROC-SKON-D06-022
  - PROC-SKON-D06-023
  - PROC-SKON-D06-024

oi_seed_ids:
  - OI-SEED-D06-041
  - OI-SEED-D06-042

source_ids:
  - SRC-NIST-D06-035
  - SRC-NIST-D06-036

evidence_level: ANALYST_INFERENCE
confidence: VERY_HIGH
sk_on_disclosure_scope: NOT_DISCLOSED
```

---
