---
id: skon-d00-d00-07-change-version-control
title: Change & Version Control
summary: "2026년 8월 초 SK온 지식 베이스의 12건 변경이력 기록과 변경 이벤트 스키마, 의미론적 버전 관리(Patch/Minor/Major) 규칙을 정의한 마스터 문서."
tags: [d00, governance, schema, table, "xref:d05", "xref:d17", "xref:d01", "xref:d02"]
keywords: [변경 추적, 버전 관리, Change Event Schema, 변경 로그, Semantic Versioning, 데이터 거버넌스, Crosswalk, 도메인 영향도, 스냅샷, 변경이력 관리, Change Event, 버전 관리 규칙, 도메인 감사, CHG, D00 마스터, Canonical Crosswalk, SKON-KB]
related: [CHG-20260803-000001, CHG-20260802-000002, CHG-20260803-000003, CHG-20260803-000004, CHG-20260803-000005, CHG-20260803-000006, CHG-20260803-000007, CHG-20260803-000008, CHG-20260803-000009, CHG-20260803-000010, CHG-20260803-000011, CHG-20260803-000012]
priority: normal
domain: D00
section: D00-07
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 795
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-07 Change & Version Control

### 1. Change Event Schema

```yaml
change_event:
  change_id: CHG-20260803-000001
  changed_at: 2026-08-03T00:00:00+09:00
  changed_by: AI_RESEARCH_WORKFLOW
  object_type: DOMAIN|SOURCE|ENTITY|CLAIM|RELATIONSHIP|TASK
  object_id: D05
  change_type: CREATE|CORRECT|UPDATE|SUPERSEDE|MERGE|SPLIT|RETIRE|REFRESH
  prior_version: v1.8
  new_version: v2.0
  reason: "Public DB completion and decision-date rights/FTO gate separation"
  evidence_ids: []
  affected_domains: [D00, D05, D17]
  downstream_actions:
    - update_D17_D05_gap_status
  approval_status: DOCUMENTED
```

### 2. Initial Change Log

| Change ID | 대상 | 변경 | 영향 |
|---|---|---|---|
| `CHG-20260803-000001` | D00 | 통합 Source·Entity·ID·변경이력 Control Plane 생성 | D01~D17 공통 |
| `CHG-20260802-000002` | D05 | 공개자료 DB를 v2.0 완료로 재판정 | D17의 기존 Open Gap 수정 필요 |
| `CHG-20260803-000003` | D01·D02 | 번호형 링크를 Legacy Source로 등록하도록 결정 | 출처 Lineage 보강 필요 |
| `CHG-20260803-000004` | D08 | `S02/S03/S04/S05/S08X`를 D08 Legacy Namespace로 보존 | Canonical Crosswalk 필요 |
| `CHG-20260803-000005` | D03~D07 | Header Version과 완료부 Version 불일치 확인 | 통합검수 Patch 필요 |
| `CHG-20260803-000006` | D17 | `D05_patent_IP_completeness: OPEN_GAP`이 최신 D05와 불일치 | `PUBLIC_COMPLETE_INTERNAL_GATE_REQUIRED`로 변경 예정 |
| `CHG-20260803-000007` | D01~D17 | D00 Cross-Domain Audit Patch 적용 | Version·Alias·상태·Lineage 정합화 |
| `CHG-20260803-000008` | Source·Entity | 511개 Canonical URL·1,491개 ID Crosswalk 생성 | 전역 Alias·중복·도메인 출현 추적 |
| `CHG-20260803-000009` | D17 | D05 v2.0의 O/I Seed 18개 추가 반영 | 원천 Seed 261→279, 직접참조 148→166 |
| `CHG-20260803-000010` | D17 | D05 Gap을 공개 DB 완료·내부/법률 Gate로 재분류 | 과대표시 해소, 통제는 유지 |
| `CHG-20260803-000011` | D00~D17 | `SKON-KB-20260803-v1.0` 공개자료 Snapshot Freeze | SHA-256·크기·행 수 기준 재현 가능 상태 고정 |
| `CHG-20260803-000012` | 제출·시연 Package | 통합본·요약본·PDF·Archive 생성 | AI 원장과 사람용 의사결정 문서를 분리 제공 |

### 3. Semantic Versioning

| 변경 | Version |
|---|---|
| 오탈자·링크·표기·Crosswalk | Patch `x.y.z` |
| Source·Entity·Schema·분석 보강 | Minor `x.y` |
| 도메인 경계·ID 체계·핵심 판정 변경 | Major `x.0` |

도메인 파일의 문서 Version과 개별 Claim/Source Version은 별도로 관리한다.

---
