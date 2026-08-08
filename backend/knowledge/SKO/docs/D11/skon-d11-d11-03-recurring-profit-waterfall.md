---
id: skon-d11-d11-03-recurring-profit-waterfall
title: Recurring Profit Waterfall
summary: 일회성 항목을 제거하고 정상화된 반복 이익을 산정하는 워터폴 프로세스와 항목별 반복성 판정 기준
tags: [d11, cost, schema, table]
keywords: [반복성이익, 정상화 EBIT, EBITDA, 일회성조정, CAPEX, AMPC, 고객보상, 현금기여, 원가정상화, 비반복비용, 반복성 이익, EBIT 정상화, Recurring EBIT, 일회성 항목, Waterfall, IRA 세액공제]
related: []
priority: normal
domain: D11
section: D11-03
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 813
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-03 Recurring Profit Waterfall

### 1. 표준 Waterfall

```text
Reported Operating Profit
− Customer Compensation and Claim Settlements judged non-recurring
− Asset Sale / Liability Release / Provision Reversal
− Incremental or Policy-dependent Production Credit chosen for Stress Case
− Temporary Inventory Valuation / FX / Metal Lag Gain
+ Temporary Ramp / Shutdown / Restructuring Cost normalized only with evidence
= Normalized Recurring EBIT Range

Recurring EBIT
+ Depreciation and Amortization
= Recurring EBITDA

Recurring EBITDA
− Maintenance CAPEX
− Growth CAPEX attributable to the program
− Increase in Working Capital
− Cash Tax / Interest / JV settlement
= Cash Contribution
```

정상화 과정은 좋은 항목만 제거하는 방식이 아니다. 일회성 이익과 일회성 비용을 같은 기준으로 분류하고, 제거 근거·금액·현금영향·재발가능성을 `OneOffAdjustment`에 남겨야 한다.

### 2. 2026 Q2 공개자료 Bridge

```yaml
sk_on_q2_2026_profit_bridge:
  scope: battery_segment
  reported_operating_profit_krw_bn: 821.8
  disclosed_drivers:
    - customer_compensation_amount_NOT_DISCLOSED
    - increased_IRA_tax_credit_amount_NOT_DISCLOSED
    - expanded_Asia_sales
    - cost_reduction_efforts
  recurring_ebit:
    value: NOT_CALCULABLE_FROM_PUBLIC_DATA
    reason: adjustment_amounts_and_volume_denominator_not_disclosed
  required_internal_evidence:
    - compensation_contract_and_accounting_entry
    - AMPC_eligible_produced_and_sold_kWh_by_facility
    - recognized_and_cash_collected_credit
    - accepted_sales_GWh_and_realized_price
    - plant_product_customer_cost_ledger
```

### 3. 반복성 판정표

| 항목 | 보고 EBIT 포함 | 반복 EBIT 처리 | Cash 별도 확인 |
|---|---|---|---|
| 정상 Cell 판매 Margin | 포함 | 포함 | 매출채권 회수 확인 |
| 45X AMPC | 포함 가능 | Base/Policy-on/Policy-off Scenario로 병렬 관리 | 신청·양도·환급 시점 |
| 고객보상 | 포함 가능 | 계약상 반복조건 없으면 비반복 | 수취·상계 방식 |
| Metal/FX Lag | 포함 | 정상 Pass-through 시차와 투기적 변동 분리 | 재고·Hedge 정산 |
| Ramp·초기가동 비용 | 포함 | 객관적 Ramp Curve가 있을 때만 정상화 | 현금비용·감가상각 |
| Warranty/Recall 충당금 | 포함 | 제품 Lifetime Economics에는 포함 | 지급시점 장기 추적 |
| 자산손상차손 | 영업외 또는 별도 | 반복 EBIT 제외 가능 | 비현금이나 ROIC에는 반영 |
| 자산매각이익 | 범위별 상이 | 핵심 영업 반복이익에서 제외 | 매각 현금은 별도 |

---
