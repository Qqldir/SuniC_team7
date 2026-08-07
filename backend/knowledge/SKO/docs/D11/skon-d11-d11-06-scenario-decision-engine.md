---
id: skon-d11-d11-06-scenario-decision-engine
title: Scenario & Decision Engine
summary: "사업 경제성 평가에 필요한 8가지 핵심 시나리오(원가, 정책, 수요, 수율, 환율, 전환, 지연, 현지화)와 검증 체크리스트를 제공한다."
tags: [d11, cost, schema, table]
keywords: [경제성 평가, 시나리오 분석, EBIT, NPV, 현금흐름, 정책신용, 운전자본, 공정 수율, 가동률, 현지화, 수익성 분석, 정책 신용, 타당성 판단, 원가 구조]
related: []
priority: normal
domain: D11
section: D11-06
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 453
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-06 Scenario & Decision Engine

### 1. 최소 Scenario

| Scenario | 핵심 가정 | 필수 출력 |
|---|---|---|
| `BASE_RECURRING` | 현재 승인·물량·원가, 비반복 보상 제외 | recurring EBIT/kWh·Cash |
| `POLICY_OFF` | 신규 AMPC 인식 0 또는 적격성 상실 | Plant/Program 손익·BCP |
| `LOW_UTILIZATION` | 고객 Call-off 하락·Ramp 지연 | 고정비 미흡수·현금 Burn |
| `YIELD_RECOVERY` | 공정별 FPY 개선 | 재료·Capacity·Margin 효과 |
| `METAL_FX_SHOCK` | 원료·환율 충격과 Pass-through 시차 | Margin at Risk·운전자본 |
| `EV_TO_ESS_CONVERSION` | 전환 CAPEX·승인기간·ESS 가격 | NPV·회수기간·Opportunity Cost |
| `CUSTOMER_PROGRAM_DELAY` | SOP/Shutdown/종료 | 재고·가동률·손상 Trigger |
| `LOCALIZE_OR_IMPORT` | 현지조달·물류·관세·Credit 적격 | Landed cost·Risk-adjusted NPV |

### 2. 경제성 Gate

```yaml
economics_decision_gate:
  mandatory:
    - same_scope_period_currency_and_volume_denominator
    - price_pass_through_and_contract_limit
    - customer_qualification_and_ramp_schedule
    - policy_credit_eligibility_probability
    - warranty_and_end_of_program_cost
    - working_capital_and_cash_timing
    - downside_and_exit_cost
  prohibit:
    - using_nameplate_capacity_as_sales_volume
    - treating_company_compensation_as_recurring_price
    - treating_announced_credit_rate_as_realized_cash
    - excluding_bad_one_offs_while_retaining_good_one_offs
    - autonomous_bid_or_shutdown_decision
```

---
