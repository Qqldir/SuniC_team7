---
id: skes-d00-d00-03-entity-time-slice-master
title: Entity & Time-Slice Master
summary: SK이노베이션 2024년 합병 전후 법인·사업조직·자산을 분류하고 메타데이터로 관리하는 엔티티 마스터 구조 및 처리 규칙
tags: [d00, governance, schema, table]
keywords: [SK이노베이션, 합병 전후, 법인명 구분, SK Innovation Co., Ltd., SK E&S Co., E&S CIC, 사내회사, Canonical Entity, 유효기간, 자산·계약·허가, 엔티티 분류, 조직 구조, 합병 규칙, SK Innovation, CIC, 메타데이터 스키마, 자산 관리, 법인 별칭, canonical entity, 2024-11-01]
related: []
priority: normal
domain: D00
section: D00-03
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 508
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-03 Entity & Time-Slice Master

### 최상위 Entity 구분

| Canonical Entity | 유효기간/상태 | 사용 규칙 |
|---|---|---|
| SK E&S Co., Ltd. | 2024-10-31까지 역사 법인·브랜드 문맥 | 당시 발표·계약·자산의 Event 주체 보존 |
| SK Innovation Co., Ltd. | 합병 존속법인 | 공시·법적 의무·연결재무 범위의 주체 |
| SK Innovation E&S CIC | 2024-11-01 이후 사내회사/사업조직 문맥 | 현재 사업 포트폴리오·운영 주체 표기 |
| Subsidiary/JV/SPV | 각 법인별 | 모회사와 자산·부채·계약·허가를 합치지 않음 |

### Entity Record Schema

```yaml
entity_record:
  canonical_entity_id: ENT-ENS-000001
  legal_name: ""
  display_name: ""
  entity_type: LEGAL_ENTITY|CIC|JV|SPV|ASSET|PROJECT|REGULATOR|VENDOR
  jurisdiction: ""
  aliases: []
  parent_entity_id: null
  ownership_pct: null
  valid_from: null
  valid_to: null
  status: ACTIVE|HISTORICAL|PLANNED|DISSOLVED|UNKNOWN
  source_ids: []
```

### 합병 전후 처리

- 2024-11-01 이전 자료의 회사명은 원문을 보존하고 현재 명칭으로 소급 치환하지 않는다.
- 합병 이전 계약·허가·채무가 자동으로 CIC 소유라고 단정하지 않는다.
- 재무수치는 별도·연결·CIC 관리손익의 Scope를 반드시 표시한다.
- 프로젝트 지분과 운영권, Offtake 권리, 자산 소유권을 각각 분리한다.
- `KCE`, `EverCharge`, `Barossa`, `Darwin LNG`, `Quynh Lap`, 인천 액화수소 등은 프로젝트·법인·자산 Alias를 혼합하지 않는다.

---
