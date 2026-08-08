---
id: skon-d13-d13-04-commercial-agreement-obligation-hierarch
title: Commercial Agreement & Obligation Hierarchy
summary: "계약 체결부터 배송까지의 계층적 단계, 가격·용량·품질 등 8가지 핵심 계약조항의 분류 및 추출기준, 옵션·ROFO 등 선택권의 통제 방안을 제시한다."
tags: [d13, contract, schema, table]
keywords: [공급계약, 의향서, MOU, 선매권, ROFO, 옵션, 용량예약, 가격조정, Incoterms, 계약 계층, 상용 조건, 용량 예약, 가격 조정, 배송 조건, 신용 조건, 계약 변경, 계약 종료]
related: []
priority: normal
domain: D13
section: D13-04
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 518
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-04 Commercial Agreement & Obligation Hierarchy

### 1. 문서와 수요의 계층

```text
Non-binding MoU / Strategic Intent
→ Term Sheet / Nomination / Preferred Supplier
→ Definitive Supply Agreement
→ Annual Capacity Reservation / Forecast
→ Firm Call-off / Release
→ Purchase Order
→ Shipment / Delivery
→ Customer Acceptance
→ Invoice / Price Adjustment / Claim
```

이 계층에서 `약 100GWh 계약`, `약 20GWh + Option`, `1GWh + 6.2GWh ROFO`, `최대 10만t MOU`를 같은 수주잔고 필드에 넣지 않는다.

### 2. 핵심 Commercial Clause Map

| Clause Family | 최소 추출 항목 | 연결 KPI |
|---|---|---|
| Volume | minimum/maximum·option·forecast·call-off·cancellation | firm demand / reserved capacity |
| Price | index·FX·raw-material pass-through·rebate·true-up | recurring margin / accepted kWh |
| Capacity | plant·line·allocation·priority·reservation fee | qualified capacity utilization |
| Quality | specification·PPAP·acceptance·warranty·recall | claim rate / warranty exposure |
| Delivery | Incoterms·lead time·buffer·expedite·LD | OTIF / premium freight |
| Change | engineering change·4M·price review·law change | change lead time / margin leakage |
| Credit | payment term·security·parent guarantee·set-off | DSO / counterparty exposure |
| Termination | convenience·cause·volume drop·insolvency·transition | stranded asset / exit cost |

### 3. Option·ROFO·우선협상권 통제

```yaml
optional_volume_record:
  base_binding_volume: null
  option_volume: null
  right_type: OPTION|ROFO|ROFR|PREFERENTIAL_NEGOTIATION
  exercise_window: null
  exercise_conditions: []
  price_determined: UNKNOWN
  capacity_reserved: UNKNOWN
  customer_financing_condition: UNKNOWN
  status: UNEXERCISED
  prohibited_use: firm_order_revenue_or_utilization_commitment
```

---
