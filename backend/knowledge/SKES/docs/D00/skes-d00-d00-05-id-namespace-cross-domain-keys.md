---
id: skes-d00-d00-05-id-namespace-cross-domain-keys
title: ID Namespace & Cross-Domain Keys
summary: "SK이노베이션 E&S의 각 엔티티 유형별 ID 형식, 불변성 원칙, 데이터 충돌 우선순위 판정 기준을 명시한 마스터 가이드"
tags: [d00, governance, schema, table, "xref:d14", "xref:d17"]
keywords: [ID 네임스페이스, ID 불변성, Canonical ID, Alias, 충돌 처리, Change Event, Supersession, Entity Master, 엔티티 ID, Canonical Source, 불변성, 소스 우선순위, 거버넌스]
related: [SRC-ENS-CAN-000001, ENT-ENS-000001, AST-ENS-000001, PRJ-ENS-000001, AGR-ENS-000001, REG-ENS-000001, CLM-ENS-D14-000001, RSK-ENS-000001, EVD-ENS-000001, OI-ENS-SEED-001, OI-ENS-TASK-001]
priority: normal
domain: D00
section: D00-05
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 585
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-05 ID Namespace & Cross-Domain Keys

| 유형 | 형식 | 예시 |
|---|---|---|
| Canonical Source | `SRC-ENS-CAN-######` | `SRC-ENS-CAN-000001` |
| Entity | `ENT-ENS-######` | `ENT-ENS-000001` |
| Asset | `AST-ENS-######` | `AST-ENS-000001` |
| Project | `PRJ-ENS-######` | `PRJ-ENS-000001` |
| Agreement | `AGR-ENS-######` | `AGR-ENS-000001` |
| Rule | `REG-ENS-######` | `REG-ENS-000001` |
| Claim | `CLM-ENS-D##-######` | `CLM-ENS-D14-000001` |
| Risk | `RSK-ENS-######` | `RSK-ENS-000001` |
| Evidence | `EVD-ENS-######` | `EVD-ENS-000001` |
| O/I Seed | `OI-ENS-SEED-###` | `OI-ENS-SEED-001` |
| Final Task | `OI-ENS-TASK-###` | `OI-ENS-TASK-001` |

### ID 불변성

1. 이름이 바뀌어도 동일 개체면 ID를 유지하고 Alias를 추가한다.
2. 합병·분할·신설처럼 법적 개체가 달라지면 새 ID와 관계 Event를 만든다.
3. 삭제 대신 `status`, `valid_to`, `superseded_by`를 사용한다.
4. Domain 로컬 ID는 보존하되 Canonical ID에 매핑한다.
5. ID 재사용은 금지한다.

---

## D00-06 Conflict, Supersession & Change Log

### 충돌 처리 순서

1. Scope·단위·법인·기간·Gross/Net·계획/실적 차이를 먼저 확인한다.
2. 동일 주장일 때 S1A → S1B → S2 → S3 → S4 → S5 순으로 우선한다.
3. 최신 Source가 과거 Source를 무조건 삭제하지 않고 유효기간을 닫는다.
4. 해결되지 않으면 `CONFLICT_OPEN`으로 유지하고 D17 Hard Gate로 전달한다.
5. 숫자를 평균하거나 임의 선택하지 않는다.

### Change Event Schema

```yaml
change_event:
  change_id: CHG-ENS-YYYYMMDD-###
  changed_at: ""
  actor: HUMAN|PIPELINE|AI_ASSISTED
  object_type: SOURCE|ENTITY|CLAIM|DOMAIN|OI_TASK
  object_id: ""
  change_type: CREATE|UPDATE|SUPERSEDE|MERGE_ALIAS|STATUS_CHANGE|CORRECTION
  before_hash: null
  after_hash: null
  reason: ""
  evidence_source_ids: []
  reviewer: null
```

---
