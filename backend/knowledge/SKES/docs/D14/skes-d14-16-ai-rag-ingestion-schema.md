---
id: skes-d14-16-ai-rag-ingestion-schema
title: AI/RAG Ingestion Schema
summary: "규제 정보를 AI/RAG 시스템에 수집할 때 사용하는 JSON 스키마, 쿼리 처리 방식, 필수 메타데이터를 정의한다."
tags: [d14, policy, core-candidate, "xref:d07"]
keywords: [규제 데이터 모델, 메타데이터, 쿼리 가드레일, Regulation, 컴플라이언스, 의무, 관할권, 규제 유효기간, 탄소배출권거래제]
related: []
priority: critical
domain: D14
section: 16
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 355
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 16. AI/RAG Ingestion Schema

## 16.1 Regulation JSON

```json
{
  "reg_id": "REG-ENS-D14-0001",
  "jurisdiction": "KR",
  "rule_name": "K-ETS Phase 4",
  "state": "IN_FORCE",
  "publication_date": "2025-11-11",
  "effective_from": "2026-01-01",
  "effective_to": "2030-12-31",
  "applicability": ["covered_generation_entity"],
  "asset_ids": ["AST-ENS-D07-0020", "AST-ENS-D07-0021", "AST-ENS-D07-0022"],
  "obligation_ids": ["OBL-ENS-D14-0001", "OBL-ENS-D14-0002", "OBL-ENS-D14-0003"],
  "economic_driver": "carbon_compliance_cost",
  "source_id": "SRC-ENS-D14-0001",
  "reviewer": "Legal/ESG"
}
```

## 16.2 Query Guardrail

```text
Question
→ identify jurisdiction
→ identify legal entity / asset / activity
→ retrieve only rules effective on requested date
→ evaluate applicability conditions
→ retrieve obligation + evidence + deadline
→ show official source
→ label uncertainty/internal-data gap
→ Legal/Tax/EHS reviewer for action
```

## 16.3 Mandatory Metadata

- `jurisdiction`
- `regulator`
- `rule_version`
- `publication_date`
- `effective_from`
- `effective_to`
- `state`
- `legal_entity`
- `asset_id`
- `activity`
- `threshold`
- `obligation`
- `deadline`
- `evidence`
- `penalty_or_loss`
- `incentive_state`
- `source_url`
- `last_verified_at`
- `human_owner`

---
