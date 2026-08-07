---
id: skon-d00-d00-06-id-governance
title: ID Governance
summary: "SK온 데이터의 ID를 형식, 생명주기, 충돌 검사로 관리하는 거버넌스 규칙. Canonical 구분, 중복 처리, 정합성 검증의 원칙을 정의한다."
tags: [d00, governance, core-candidate, table, "xref:d14", "xref:d13", "xref:d07", "xref:d17"]
keywords: [ID 형식, ID Lifecycle, Collision Check, Canonical ID, ID 충돌, Entity Identity, Referential Integrity, 데이터 마스터, ID 관리, ID 검증, Lifecycle, Canonical Source, 중복 제거, MERGED_INTO, Referential integrity, 데이터 정합성]
related: []
priority: critical
domain: D00
section: D00-06
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 497
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-06 ID Governance

### 1. ID 형식

```text
Canonical Source: SRC-CAN-000001
Domain Source:    SRC-D14-000001
Canonical Entity: ORG-SKON-000001
Claim:            CLM-D14-000001
Relationship:     REL-D13-000001
Event:            EVT-D07-000001
Gap:              GAP-D17-000001
Change:           CHG-20260803-000001
Validation:       VAL-D00-000001
Final OI Task:    D17-OI-001
```

### 2. ID Lifecycle

1. ID는 의미가 바뀌어도 재사용하지 않는다.
2. 오탈자 정정은 같은 ID의 Patch Version으로 처리한다.
3. 범위·당사자·제품 Revision·효력기간이 바뀌면 새 ID를 발급한다.
4. 합쳐진 중복은 하나를 Canonical로 정하고 나머지는 `MERGED_INTO` Alias로 유지한다.
5. 잘못 생성된 ID도 삭제하지 않고 `RETIRED_INVALID`로 남긴다.
6. D17 과제 ID `001~060`은 고정하며 이름 변경은 Change Log로 관리한다.
7. Source ID와 Entity ID를 같은 Namespace에서 사용하지 않는다.

### 3. Collision Check

| Check | 실패조건 |
|---|---|
| ID uniqueness | 동일 ID가 서로 다른 정의를 가짐 |
| Entity identity | 같은 법인·공장·제품이 여러 Canonical ID로 존재 |
| Source identity | 같은 원문·Version이 여러 Canonical Source로 존재 |
| Temporal overlap | 배타적인 상태가 같은 기간에 동시에 Active |
| Referential integrity | 참조 ID가 Owner Domain에 없음 |
| Circular dependency | 근거가 없는 Claim이 서로를 근거로 참조 |
| Orphan task | D17 과제에 Pain Point·Source·Owner Domain이 없음 |

---
