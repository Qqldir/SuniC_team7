---
id: skon-d00-d00-04-canonical-fact-claim-relationship-model
title: "Canonical Fact, Claim & Relationship Model"
summary: "사실과 관계 정보의 저장 구조, 신뢰도 분류, 그리고 AI가 해서는 안 될 자동 추론 규칙을 정의한다."
tags: [d00, governance, schema, table, "xref:d12", "xref:d13"]
keywords: [메타데이터 스키마, 엔티티 ID, 신뢰도 관리, 자동 추론 금지, 출처 추적, 데이터 분류, 파생 방법, 범위 관리, Triple 구조, 신뢰도, fact class, 자동 추론, entity ID, 추론 금지, derivation method, 정보 검증, 데이터 모델]
related: []
priority: normal
domain: D00
section: D00-04
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 855
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-04 Canonical Fact, Claim & Relationship Model

### 1. Fact/Claim Record

```yaml
claim_record:
  claim_id: CLM-D12-000001
  subject_entity_id: ORG-BOSK-000001
  predicate: HAS_LOAN_COMMITMENT_LIMIT
  object_value: 9630000000
  unit: USD
  scope_id: SCOPE-BOSK-DOE-LOAN
  valid_time:
    from: null
    to: null
  transaction_time:
    first_recorded_at: 2026-08-03
    last_updated_at: 2026-08-03
  fact_class: FACT|ANALYSIS|HYPOTHESIS|PROPOSAL
  status: ANNOUNCED|SIGNED|EFFECTIVE|OPERATING|SUPERSEDED|HISTORICAL|UNKNOWN
  confidence: CONFIRMED_MULTI|CONFIRMED_SINGLE|INDICATED|CONFLICTED
  source_ids: [SRC-CAN-000004]
  source_locator: "section/page/table"
  derivation_method: DIRECT_QUOTE_PARAPHRASE|CALCULATION|INFERENCE|SCENARIO
  assumptions: []
  owner_domain: D12
  reviewer_role: ""
  prohibited_inference: "commitment limit is not drawn balance or SK On standalone debt"
```

### 2. Fact Class

| Class | 정의 | AI 사용 규칙 |
|---|---|---|
| `FACT` | 원문이 직접 확인하는 사실 | Source·Scope·시점이 맞을 때 응답 가능 |
| `CALCULATED_FACT` | 공개 입력값과 명시된 수식으로 계산 | 입력·단위·범위·수식 동시 제시 |
| `ANALYSIS` | 여러 사실의 해석 | 사실처럼 단정하지 않고 해석임을 표시 |
| `HYPOTHESIS` | 검증할 가설 | 확정관계 생성 금지 |
| `PROPOSAL` | O/I 과제·운영모델 제안 | 현재 SK온 운영상태로 표현 금지 |
| `UNKNOWN` | 필요한 정보가 없거나 비공개 | 0·없음·미실행으로 변환 금지 |

### 3. Relationship Triple

```yaml
relationship:
  relationship_id: REL-000001
  subject_id: ORG-SKON-000001
  predicate: OWNS_EQUITY_IN
  object_id: ORG-HSBMA-000001
  value: 50
  unit: PERCENT
  valid_from: null
  valid_to: null
  status: CURRENT_AS_OF_DATE
  source_ids: []
  confidence: CONFIRMED_MULTI
  owner_domain: D13
  excluded_implications:
    - equal_cash_burden
    - equal_guarantee
    - unilateral_control
```

### 4. 금지되는 자동 추론

| 확인된 사실 | 자동으로 만들면 안 되는 결론 |
|---|---|
| JV 지분 50% | 자본·보증·손익·통제도 각각 50% |
| 공장 명목 Capacity | 실제 생산·고객승인·판매 가능한 Capacity |
| 계약 총 GWh | 연도별 Call-off·출하·매출 |
| MOU 최대 물량 | 확정 구매의무·매출 |
| 45X 단가 | 실제 인식·현금수령·SK온 귀속액 |
| DOE 대출 승인한도 | 실제 인출액·SK온 단독 차입금 |
| 제품 발표 | 양산·고객승인·상업매출 |
| R&D License | 상업생산 License·FTO 확보 |
| 단일 리콜 | 전사 불량률·현재 전체 품질수준 |
| 경쟁사 Case 성과 | SK온 예상 ROI |
| 내부데이터 미공개 | 값이 0 또는 제도가 없음 |

---
