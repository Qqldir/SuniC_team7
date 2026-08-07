---
id: skon-d11-d11-04-qualified-kwh-unit-economics
title: Qualified-kWh Unit Economics
summary: 배터리 생산의 손실 단계(Volume Waterfall)와 kWh당 원가 구성(재료·전환·물류비)으로 수익성을 측정하는 단위경제 관리 체계를 설명한다.
tags: [d11, cost, schema, table]
keywords: [배터리, kWh, 원가분석, 생산 손실, 합격률, OEE, 비용-서빙, 수익성, 경제성, 원가구조, 배터리 원가, 손실 추적, 수율, 현금화, 재료비, 전환비, 물류비]
related: []
priority: normal
domain: D11
section: D11-04
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 737
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-04 Qualified-kWh Unit Economics

### 1. Volume Waterfall

```text
Nameplate kWh
→ Scheduled kWh
→ Produced kWh
→ First-pass Good kWh
→ Final Good kWh after Rework
→ Shipped kWh
→ Customer-accepted kWh
→ Paid kWh
```

| 단계 | 경제적 질문 | 대표 손실 |
|---|---|---|
| Nameplate→Scheduled | 수요·승인·정비를 반영한 가동계획인가? | 유휴 Capacity·고정비 미흡수 |
| Scheduled→Produced | 설비가 계획대로 가동됐는가? | Downtime·속도손실·인력제약 |
| Produced→First-pass Good | 한 번에 합격했는가? | Scrap·재료손실·병목 |
| Good→Shipped | 고객 Call-off와 물류가 연결됐는가? | 완제품 재고·보관비 |
| Shipped→Accepted | 고객검사·Claim을 통과했는가? | 반품·가격차감·재작업 |
| Accepted→Paid | 계약조건대로 현금화됐는가? | 매출채권·분쟁·환율 |

### 2. Cost per Accepted kWh

```text
Material Cost / Accepted kWh
= Cathode + Anode + Separator + Electrolyte
 + Cu/Al Foil + Binder/CNT + Pack/Module Components
 + Inbound Freight/Duty − Scrap Recovery Value

Conversion Cost / Accepted kWh
= Direct Labor + Energy + Utility + Consumables
 + Maintenance + Quality/Inspection + Factory Overhead
 + Depreciation + Ramp/Downtime Loss + Rework

Cost-to-Serve / Accepted kWh
= Outbound Logistics + Expedite + Inventory Carry
 + Engineering Change + Customer Quality Support
 + Warranty/Recall Expected Loss + Service/Project Execution

Recurring Contribution / Accepted kWh
= Realized Net Price
 − Material Cost − Conversion Cost − Cost-to-Serve
 + Recurring Policy Support Scenario
```

### 3. 필수 관리 필드

```yaml
qualified_kwh_economics_record:
  dimensions:
    - period
    - legal_entity
    - plant_and_line
    - customer_and_program
    - product_and_chemistry
    - form_factor_and_application
  volume:
    - produced_kWh
    - first_pass_good_kWh
    - final_good_kWh
    - shipped_kWh
    - customer_accepted_kWh
  operational_driver:
    - OEE
    - first_pass_yield
    - final_yield
    - scrap_and_rework
    - energy_kWh_per_accepted_kWh
    - labor_hours_per_accepted_kWh
  economics:
    - realized_price_per_kWh
    - material_cost_per_kWh
    - conversion_cost_per_kWh
    - logistics_and_cost_to_serve_per_kWh
    - warranty_expected_loss_per_kWh
    - AMPC_recognized_and_cash_per_kWh
    - recurring_contribution_per_kWh
  controls:
    - currency_and_fx_rate
    - standard_vs_actual
    - data_lineage
    - close_status
    - owner_and_approval
```

---
