---
id: skon-d12-d12-05-capex-stage-gate-real-options-logic
title: CAPEX Stage Gate & Real-Options Logic
summary: 자본투자 프로젝트를 전략 적합성부터 운영 성과까지 8단계 게이트와 실옵션 분석으로 평가하는 의사결정 프레임워크
tags: [d12, capex, schema, table, "xref:d03", "xref:d09", "xref:d10", "xref:d11"]
keywords: [게이트, 투자의사결정, Scenario 분석, 실옵션, NPV, Greenfield, Financial Close, 현금흐름, MOTHBALL, 위험조정, Stage Gate, Real Option, CAPEX 의사결정, NPV 범위 분석, 투자 평가, 자본배분, Risk-adjusted Value]
related: []
priority: normal
domain: D12
section: D12-05
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 756
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-05 CAPEX Stage Gate & Real-Options Logic

### 1. 표준 Gate

| Gate | 핵심 질문 | 필수 증거 | 가능한 결정 |
|---|---|---|---|
| `G0 Strategic Fit` | 제품·지역·고객·정책 방향과 맞는가? | D03·D09·D10 Scenario | 탐색/종료 |
| `G1 Concept` | Greenfield·Brownfield·전환·외주 중 최적안은? | 범위·Capacity·기술·대안 | 설계/보류 |
| `G2 Qualification` | 고객승인과 Product Freeze가 충분한가? | 계약상태·샘플·인증 Plan | 조건부 승인 |
| `G3 Funding` | 자금과 Incentive가 법적으로 확보됐는가? | Term Sheet·Covenant·Guarantee | Financial Close/보류 |
| `G4 Commit` | 수요 Downside에도 계약 발주가 타당한가? | NPV Range·Exit Cost·Stage Budget | 발주/축소 |
| `G5 Build` | Schedule·EAC·Change Order가 허용범위인가? | 물리진척·EAC·Critical Path | 계속/재설계 |
| `G6 Ramp` | 합격 kWh와 고객인수가 계획대로 늘어나는가? | FPY·승인·가동·Cash Burn | Ramp/전환/휴지 |
| `G7 Operate` | 반복 Cash ROIC가 기준을 충족하는가? | D11 Unit Economics | 확장/유지/개조 |
| `G8 Exit` | 추가투자보다 매각·휴지·철수가 유리한가? | 처분가·복구·계약·Clawback | Exit/보존 |

### 2. Real Option 비교

```yaml
asset_option_set:
  EXPAND:
    value_driver: qualified_demand_and_positive_incremental_cash
  HOLD:
    value_driver: preserve_option_until_customer_or_policy_uncertainty_resolves
  CONVERT_EV_TO_ESS:
    value_driver: reuse_building_utility_and_selected_equipment
  CONVERT_FORMAT_OR_CHEMISTRY:
    value_driver: capture_LFP_prismatic_or_new_platform_demand
  MOTHBALL:
    value_driver: avoid_variable_and_selected_fixed_cost_while_preserving_restart
  SELL_OR_TRANSFER:
    value_driver: release_cash_and_obligations
  EXIT_AND_REMEDIATE:
    value_driver: stop_structural_cash_loss_after_exit_cost
```

```text
Risk-adjusted Incremental Value
= Operating Cash Flow under Scenario
+ Policy Support with Probability and Clawback
+ Residual / Reuse / Option Value
− Remaining CAPEX and Working Capital
− Financing and Guarantee Cost
− Qualification Delay and Ramp Loss
− Exit, Restoration and Contract Cost
```

NPV를 단일 숫자로 만들기보다 수요·SOP·수율·원료·가격·Credit·환율·공사비 Scenario별 범위와 `중단 Trigger`를 함께 제시한다. 이미 쓴 CAPEX가 크다는 이유만으로 추가투자를 승인하지 않는다.

---
