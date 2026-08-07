---
id: skon-d00-d00-05-scope-time-unit-status-standard
title: "Scope, Time, Unit & Status Standard"
summary: SK온 데이터 관리를 위해 범위·시간·단위를 정의하고 미공개·미확인 데이터를 구분하는 필수 표준 가이드. 용량·계약량·생산량 등 데이터유형별 단위·필드·금지사항 표 포함.
tags: [d00, governance, core-candidate, schema, table]
keywords: [consolidation_scope, GWh, effective_date, NOT_DISCLOSED, 계약량, transaction_time, 불확실성, 원가, 지분, Scope ID, 범위 정의, Time Standard, 시간 기준, Unit Standard, 데이터 단위, Capacity]
related: []
priority: critical
domain: D00
section: D00-05
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 894
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-05 Scope, Time, Unit & Status Standard

### 1. Scope ID

```yaml
scope:
  scope_id: SCOPE-000001
  consolidation_scope: SKI_CONSOLIDATED|BATTERY_SEGMENT|SKON_CONSOLIDATED|LEGAL_ENTITY|JV_GROSS
  legal_entity_id: null
  plant_id: null
  line_id: null
  product_id: null
  product_revision_id: null
  customer_id: null
  customer_program_id: null
  supplier_id: null
  material_grade_id: null
  geography: null
  period: null
  currency_basis: null
  gross_or_attributable: GROSS|ATTRIBUTABLE|UNKNOWN
```

### 2. Time Standard

| Field | 의미 |
|---|---|
| `publication_date` | 원문 발행일 |
| `effective_date` | 법령·계약·정책 효력일 |
| `event_date` | 생산개시·거래종결·사고 등 사건일 |
| `period_start/end` | 실적·전망의 대상기간 |
| `valid_from/to` | 사실관계가 유효한 기간 |
| `access_date` | 원문을 확인한 날짜 |
| `transaction_time` | KB에 기록·변경한 시점 |
| `decision_date` | 투자·FTO·계약 판단을 실제 수행하는 시점 |

미래 계획은 `target_date`, 완료 사실은 `actual_date`로 분리한다. 계획일이 지났다고 자동으로 완료 처리하지 않는다.

### 3. 단위·범위 Standard

| 데이터 | 필수 단위·필드 | 금지사항 |
|---|---|---|
| Capacity | GWh/year, nominal/installed/qualified/actual | 서로 다른 Capacity 단순합산 |
| 계약량 | GWh 또는 tonne, total/annual/option | Option 포함 총량을 Firm으로 표기 |
| 생산량 | GWh, 기간, accepted/scrap 포함 여부 | 출하량·판매량과 혼용 |
| 금액 | 통화, 명목/현재가치, gross/net, 기간 | 환율·기준일 없는 합산 |
| 지분 | %, 기준일, 의결권/경제권 | 지분율로 통제 추정 |
| 세액공제 | rate, eligible basis, claimed/recognized/cash | 명목 Capacity 곱셈으로 현금 추정 |
| 원가 | KRW/USD per accepted kWh, 범위·기간 | Pack/Cell, gross/net 혼용 |
| 품질 | 분모·Population·기간·검사 Gate | 단일 사건을 전사율로 환산 |
| 탄소 | kgCO2e/kWh, system boundary, method version | 서로 다른 LCA 경계 비교 |

### 4. Unknown Standard

| Code | 의미 |
|---|---|
| `NOT_DISCLOSED` | 존재 가능성은 있으나 공개되지 않음 |
| `NOT_PUBLICLY_CONFIRMED` | 공개 1차 자료로 확인되지 않음 |
| `NOT_APPLICABLE` | 해당 범위에 적용되지 않음 |
| `NOT_YET_EFFECTIVE` | 제정·발표됐으나 효력 전 |
| `PENDING_SECONDARY_RULE` | 위임·시행 규칙 대기 |
| `PENDING_INTERNAL_DATA` | 내부 원장·실적 필요 |
| `PENDING_LEGAL_REVIEW` | 법률해석·FTO 의견 필요 |
| `CONFLICTED` | 출처 간 충돌 미해결 |
| `STALE` | 갱신주기를 넘음 |
| `UNKNOWN` | 위 범주로도 세분할 수 없음 |

`UNKNOWN`, `NOT_DISCLOSED`, 빈칸, 0은 서로 다른 값이다.

---
