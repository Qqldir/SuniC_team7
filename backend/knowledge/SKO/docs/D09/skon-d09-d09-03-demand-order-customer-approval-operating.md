---
id: skon-d09-d09-03-demand-order-customer-approval-operating
title: "Demand, Order & Customer Approval Operating Model"
summary: 고객 수요 예측부터 출하·수락까지의 주문 관리 프로세스와 고객승인 기준을 통합적으로 다루는 운영 모델이다.
tags: [d09, customer, schema, table, "xref:d03", "xref:d04", "xref:d07"]
keywords: [고객 수요, Forecast Reconciliation, Firm Call-off, 공장 배정, 고객승인, BOM 변경, 출하·수락, Qualified Capacity, 통제점, 예측·주문 일치, 수요 예측, 주문 처리, Firm call-off, 내부 원장, Acceptance, 프로세스 인증]
related: []
priority: normal
domain: D09
section: D09-03
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 567
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09-03 Demand, Order & Customer Approval Operating Model

### 1. 내부 통합 원장

```yaml
customer_demand_record:
  customer_id: CUST-D09-...
  program_id: PRG-D09-...
  agreement_id: AGR-D09-...
  agreement_version: 1
  forecast_snapshot_date: YYYY-MM-DD
  forecast_bucket: MONTH
  forecast_gwh: null
  firm_calloff_gwh: null
  shipped_gwh: null
  accepted_gwh: null
  cell_product_id: PROD-D03-...
  chemistry_id: CHEM-D04-...
  plant_id: PLANT-D07-...
  line_id: LINE-D07-...
  qualification_id: QUAL-D09-...
  sop_date: null
  eop_date: null
  confidence: LOW|MEDIUM|HIGH
  source_ids: []
  last_updated_at: YYYY-MM-DDThh:mm:ssZ
```

### 2. Forecast Reconciliation

| 단계 | 질문 | 필수 통제 |
|---|---|---|
| 고객 Long-range Forecast | 12~24개월 Program 수요는 얼마인가? | Snapshot을 덮어쓰지 않고 Version 보존 |
| 계약 최소·최대량 | 법적 의무와 option은 무엇인가? | Base·option·우선협상량 분리 |
| Firm Call-off | 실제 Release된 물량은 얼마인가? | Forecast와 별도 Ledger |
| 공장·Line 배정 | 어느 Qualified Capacity가 대응하는가? | 고객승인 없는 Capacity 배정 금지 |
| 출하·수락 | 생산량 중 고객이 받은 합격량은 얼마인가? | Good output·Shipment·Acceptance 분리 |
| 매출·Claim | 가격조정·보상·Chargeback은 무엇인가? | 일회성 보상과 반복 Margin 분리 |

### 3. 고객승인 Key

```text
customer_legal_entity
+ program/platform
+ cell_product_revision
+ chemistry/BOM revision
+ plant
+ line
+ process revision
+ approval effective period
```

같은 Cell 제품이라도 공장·Line·BOM·공정이 바뀌면 고객승인이 자동 승계된다고 가정하지 않는다. 이 Key는 D07의 Qualified Capacity, D08의 소재 4M, D15의 품질·보증 정보와 연결한다.

---
