---
id: skon-d12-d12-06-cost-to-complete-cash-impairment-control
title: "Cost-to-Complete, Cash & Impairment Control"
summary: "프로젝트의 최종 비용 추정(EAC), 유동성 관리 체계, 자산손상 위험 신호와 대응 체크리스트를 담은 CAPEX 통제 가이드."
tags: [d12, capex, schema, table]
keywords: [EAC, 최종완료비용, 유동성 워터폴, 손상징후, 공사비 관리, 우발비, 현금흐름 예측, 자본지출, Change Order, 조기경보, 자산손상 조기경보, 비용진척 대 물리진척, Liquidity Runway, 손상 Trigger, 게이트 재심사, 현금 버퍼, Contingency 조정, Policy-off Scenario]
related: []
priority: normal
domain: D12
section: D12-06
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 558
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-06 Cost-to-Complete, Cash & Impairment Control

### 1. Cost-to-Complete

```text
Approved Budget
− Actual Cash Paid
− Certified but Unpaid Invoice
− Remaining Contract Commitment
+ Approved and Probable Change Orders
+ Schedule Delay Cost
+ Commissioning / Ramp / Qualification Cost
+ Contingency at Current Risk Level
= Estimate at Completion and Remaining Funding Need
```

`percent complete`는 비용진척과 물리진척을 함께 저장한다. 선급금·고가설비 조기발주로 비용진척만 높아질 수 있고, 건물 완공률이 높아도 Utility·MES·검사·고객승인이 Critical Path일 수 있다.

### 2. Liquidity Waterfall

```yaml
liquidity_waterfall:
  opening_unrestricted_cash: INTERNAL_REQUIRED
  operating_cash_generation: INTERNAL_REQUIRED
  committed_equity_calls: INTERNAL_REQUIRED
  available_undrawn_debt: INTERNAL_REQUIRED
  grants_and_tax_cash_timing: INTERNAL_REQUIRED
  mandatory_capex_and_debt_service: INTERNAL_REQUIRED
  working_capital_peak: INTERNAL_REQUIRED
  guarantee_or_clawback_stress: INTERNAL_REQUIRED
  minimum_cash_buffer: BOARD_POLICY_REQUIRED
  result: base_downside_severe_monthly_liquidity_runway
```

### 3. 손상 Early Warning

| 선행 Trigger | 내부 KPI | D12 행동 |
|---|---|---|
| 고객 SOP·Call-off 지연 | approved demand / planned capacity | Gate 재심사·발주 동결 |
| 가동률·FPY Ramp 지연 | accepted kWh / nameplate kWh | Cost-to-Complete 재산정 |
| 반복 Margin 악화 | recurring cash contribution/kWh | CGU Cash Flow 갱신 |
| 정책지원 감소·부적격 | eligible-to-cash gap | Policy-off Scenario |
| 공사비·일정 초과 | EAC/budget, months late | Contingency·Claim·Scope 조정 |
| 고객·제품 전환 | requalification lead time | 전환 NPV·Exit Cost 비교 |
| 금리·환율 변화 | debt service and FX-at-risk | Funding Mix·Hedge 검토 |

---
