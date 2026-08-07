---
id: skon-d09-d09-01-customer-relationship-data-model
title: Customer & Relationship Data Model
summary: "고객과 수주 관계 관리를 위한 10개 핵심 엔터티(Customer, Agreement, Program 등)의 구조와 관계상태, 수요량 분류 기준을 정의한 데이터 모델."
tags: [d09, customer, schema, table]
keywords: [고객, 데이터 모델, 엔터티, 관계상태, 계약, 예측, 수주, Call-off, OEM, PPAP, 공급계약, 차종, 수요예측, 배터리할당, ESS]
related: []
priority: normal
domain: D09
section: D09-01
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 632
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09-01 Customer & Relationship Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `Customer` | `customer_id` | 법인·그룹·브랜드·국가·고객유형·신용위험 |
| `Program` | `program_id` | 차종/ESS 프로젝트·플랫폼·SOP/EOP·지역·공장 |
| `Agreement` | `agreement_id + version` | 당사자·구속력·기간·총량·option·가격·해지조건 |
| `Forecast` | `forecast_id + snapshot_date` | 고객 Forecast·기간 Bucket·수량·신뢰도·변경이력 |
| `CallOff` | `calloff_id` | 확정 Release·납기·Cell Revision·인도지 |
| `Nomination` | `nomination_id` | 고객·Program·Cell·공장·Line·승인상태 |
| `Qualification` | `qualification_id` | PPAP/4M·시험·고객승인·유효 Revision |
| `Allocation` | `allocation_id` | Program별 연·월 GWh·공장·Line·제약조건 |
| `ClaimEvent` | `claim_id` | 품질·납기·Capacity·보상·책임·재발방지 |
| `ExternalSignal` | `signal_id` | EV 판매·공장 Shift·출시연기·정책·신용·뉴스 |

### 2. 관계 상태 Vocabulary

```yaml
relationship_status:
  CURRENT_CONFIRMED:
    meaning: 기준일과 가까운 당사자 또는 시장 설치자료로 고객관계 확인
  CURRENT_TRANSITION:
    meaning: 고객관계는 확인되나 차종 종료·JV 재편·물량조정이 진행 중
  FUTURE_BINDING:
    meaning: 미래 공급계약 체결, 실제 PO·출하 전
  FRAMEWORK_PARTLY_BINDING:
    meaning: 확정분과 option·우선협상 범위가 함께 존재
  HISTORICAL_CONFIRMED:
    meaning: 과거 차종·공급은 확인되나 현재 지속은 미확인
  MEDIA_OR_INVESTOR_INDICATED:
    meaning: 보조자료상 고객이나 당사자 최신 확인 부족
  WATCHLIST:
    meaning: 검증 전 후보, 확정 고객 집계 금지
```

### 3. 수요량 Vocabulary

```text
Announced Contract Total
≠ Option / Preferential Volume
≠ Customer Forecast
≠ Firm Call-off
≠ Shipped GWh
≠ Accepted GWh
≠ Revenue-Recognized GWh
```

---
