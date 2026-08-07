---
id: skes-d00-d00-04-claim-time-status-control
title: "Claim, Time & Status Control"
summary: "데이터 클레임의 스키마, 사실 상태 코드, 신뢰도, 5가지 시점의 정의와 규칙을 명시한 메타데이터 표준"
tags: [d00, governance, schema, table, "xref:d07"]
keywords: [상태 코드, 사실 상태, 신뢰도, 시점 구분, 스키마, event_time, knowledge_time, 유효 기간, 출처, 클레임 검증, fact_status, PUBLIC_CONFIRMED, 시점 관리, 메타데이터, COMPANY_CLAIM, 데이터 품질]
related: []
priority: normal
domain: D00
section: D00-04
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 457
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-04 Claim, Time & Status Control

### Claim Schema

```yaml
claim_record:
  claim_id: CLM-ENS-D07-000001
  subject_entity_id: ""
  predicate: ""
  object_value: null
  unit: null
  geography: ""
  scope: ""
  event_time: null
  valid_from: null
  valid_to: null
  knowledge_time: null
  fact_status: PUBLIC_CONFIRMED|COMPANY_CLAIM|EXTERNAL_SIGNAL|INTERNAL_REQUIRED|HYPOTHESIS|PROPOSAL
  confidence: HIGH|MEDIUM|LOW|NOT_SCORED
  source_ids: []
  conflict_set_id: null
```

### 상태 코드

| 코드 | 의미 |
|---|---|
| PUBLIC_CONFIRMED | 공개 근거로 해당 범위의 사실 확인 |
| COMPANY_CLAIM | 기업이 발표했으나 독립 검증과 구분 필요 |
| EXTERNAL_SIGNAL | 외부 시장·기술·위협 신호이며 E&S 사건을 뜻하지 않음 |
| INTERNAL_REQUIRED | 공개자료만으로 확정 불가 |
| HYPOTHESIS | 검증 전 분석 가설 |
| PROPOSAL | O/I·PoC 제안 |
| SUPERSEDED | 후속 Source/Event가 대체 |
| CANCELLED | 계획·입찰·프로젝트가 취소됨 |
| ENACTED_FUTURE | 확정됐으나 기준일 현재 미시행 |
| EXPIRED | 종료일 경과 |

### 시점 규칙

- `event_time`: 사건이 실제 발생한 때
- `valid_from/to`: 사실·규칙이 유효한 기간
- `knowledge_time`: DB가 해당 사실을 알게 된 때
- `publication_date`: 출처가 공개된 때
- `effective_date`: 법·계약·정책 효력이 발생한 때

위 다섯 날짜는 서로 대체하지 않는다.

---
