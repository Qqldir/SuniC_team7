---
id: skon-d00-d00-11-d17-lineage-recommendation-control
title: D17 Lineage & Recommendation Control
summary: "D17 과제의 데이터 출처 추적 체계, 최소 필수 필드 정의, 279개 Seed 상태 분류(SELECTED·MERGED·DEPENDENCY·DEFERRED·DUPLICATE·REJECTED_GATE·RETIRED), 의존성 정정 규칙을 설정한 가이드."
tags: [d00, governance, schema, table, "xref:d17"]
keywords: [Seed, 데이터 계보, Task 필드, Disposition, 의존성, 포트폴리오, 게이트, KPI, 우선순위, 보류, D17 과제, Lineage, Seed Disposition, Canonical Source, Hard Gate, 결정 권한자, 데이터 권리]
related: []
priority: normal
domain: D00
section: D00-11
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 615
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-11 D17 Lineage & Recommendation Control

### 1. 필수 Lineage

```text
Canonical Source
→ Claim
→ Entity / Event / Relationship
→ Pain Point
→ Domain OI Seed
→ Deduplication Group
→ D17 Final Task
→ Score / Hard Gate / Dependency
→ PoC Gate / KPI / Decision Evidence
→ Scale or Stop / Post-implementation Result
```

### 2. D17 Task 최소 필드

```yaml
d17_task_lineage:
  task_id: D17-OI-001
  task_name: ""
  portfolio_id: ""
  priority: P0|P1|P2
  source_seed_ids: []
  canonical_claim_ids: []
  canonical_source_ids: []
  affected_entity_ids: []
  owner_domain_ids: []
  decision_owner_role: ""
  required_internal_data: []
  data_and_ip_rights: []
  baseline_and_control: ""
  primary_kpi: ""
  value_scope_id: ""
  no_double_count_group: ""
  hard_gates: []
  dependencies: []
  first_gate: G0
  status: PROPOSED_FOR_VALIDATION
```

### 3. Seed Disposition

모든 279개 Seed는 다음 중 하나를 가져야 한다. v1.1 Ledger에서는 D17 과제표에 직접 연결된 166개를 `SELECTED`, 직접 연결이 없는 113개를 `DEFERRED`로 기록했다. 보류 Seed는 향후 승격 시 `MERGED·DEPENDENCY·DUPLICATE·REJECTED_GATE·RETIRED` 중 더 구체적인 상태로 재판정한다.

| Disposition | 의미 |
|---|---|
| `SELECTED` | D17 과제의 핵심 Seed |
| `MERGED` | 동일 원인·데이터·Owner 과제로 통합 |
| `DEPENDENCY` | 독립 과제가 아니라 선행 기반 |
| `DEFERRED` | 기술·시장·데이터 조건 대기 |
| `DUPLICATE` | 다른 Seed와 실질적으로 동일 |
| `REJECTED_GATE` | 권리·안전·경제성·근거 Gate 실패 |
| `RETIRED` | 전제 사실이 만료·취소·대체됨 |

### 4. D17 최신 정정 상태

```yaml
d17_dependency_correction:
  prior_value:
    D05_patent_IP_completeness: OPEN_GAP
  canonical_D00_value:
    D05_public_database: COMPLETE_V2
    official_register_status: REFRESH_AT_DECISION_DATE
    product_and_contract_rights: INTERNAL_VALIDATION_REQUIRED
    legal_FTO_opinion: REQUIRED_BEFORE_COMMERCIAL_COMMITMENT
  action: PATCHED_IN_D17_V1_1
```

---
