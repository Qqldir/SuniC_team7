---
id: skon-d12-d12-04-funding-structure-obligation-ledger
title: Funding Structure & Obligation Ledger
summary: "SK온의 펀딩 이벤트(FI, PRS, 증자), 자본·채무·보증 구조, 회계 Scope와 실제 현금 노출의 차이를 정의하는 추적 원장."
tags: [d12, capex, schema, table]
keywords: [투자유치, FI, 증자, PRS, 자본, 채무보증, 자금흐름, Green Financing, 자금조달 이벤트, 자본 증자, Funding Stack, Scope 차이, 현금 노출]
related: [FUND-D12-2023-FI, FUND-D12-2023-HMG, FUND-D12-2025-SKON, FUND-D12-2025-FI-EXIT, FUND-D12-2025-MERGER, FUND-D12-GREEN]
priority: normal
domain: D12
section: D12-04
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 981
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-04 Funding Structure & Obligation Ledger

### 1. 공개 자금조달 Event

| Event ID | 시점 | 공개 내용 | 상태·해석 |
|---|---|---|---|
| `FUND-D12-2023-FI` | 2023-05 | FI·SNB 관련 최대 1.24조원, 기존 1.2조원 FI와 모회사 2조원 포함 최대 4.44조원 확보 발표 | 당시 투자유치 Event; 2025 FI 회수구조와 연결 필요 |
| `FUND-D12-2023-HMG` | 2023-05 | 현대차·기아의 SK온 차입 2조원, SK이노베이션 채무보증 발표 | 고객연계 Debt·Guarantee; 잔액·만기 재검증 필요 |
| `FUND-D12-2025-SKON` | 2025-07 | SK온 제3자배정 증자 2조원, SK이노베이션 PRS 구조 참여 발표 | 이사회 승인·운영자금 목적; PRS 정산 Exposure 별도 |
| `FUND-D12-2025-FI-EXIT` | 2025-07 | SK이노베이션이 SK온 FI 전환우선주 전량을 3.588조원에 매입 결정 | 자본유입이 아니라 FI Exit·모회사 Cash Obligation |
| `FUND-D12-2025-MERGER` | 2025-11 | SK온–SK엔무브 합병 완료 | 자본·EBITDA Scope 변화; 발표 당시 기대효과와 실제효과 분리 |
| `FUND-D12-GREEN` | 현재 | SK온·SK Battery America Green Financing Framework 공개 | 적격 Use-of-Proceeds 기반; 실제 잔액·배분·성과 별도 원장 필요 |

SK이노베이션은 2025년 7월 그룹 전체 8조원 자본확충 계획을 발표했다. 이 가운데 SK온 직접 항목은 2조원 제3자배정 증자였고, SK이노베이션 2조원 증자·영구채 0.7조원·SKIET 0.3조원·추가 3조원 계획은 모두 SK온 유입액이 아니다. 같은 발표의 SK온 FI 지분 3.588조원 매입도 SK온 신규자금과 상계해서는 안 된다. ([2025 Capital Expansion](https://askinno.com/global/archives/21782))

2023년 투자유치는 SK온이 최대 4.44조원을 확보했다고 발표했지만 이후 FI Exit와 PRS 자금이 등장했다. D12 원장은 `누적 발표액`을 더하는 방식 대신 투자자·증권종류·발행법인·납입일·상환/매입·PRS Reference Price·정산조건을 연결해야 한다. ([SK On 2023 Funding](https://askinno.com/global/archives/14491))

### 2. 표준 Funding Stack

```yaml
funding_stack_required_fields:
  equity:
    - issuer_and_investor
    - security_class_and_ownership
    - committed_paid_and_refunded_amount
    - dilution_redemption_exit_rights
  debt:
    - borrower_lender_facility_limit_drawn_balance
    - interest_maturity_amortization_currency
    - security_covenant_and_events_of_default
  guarantee:
    - guarantor_beneficiary_underlying_obligation
    - maximum_exposure_and_release_condition
  policy_support:
    - grant_tax_credit_interest_free_loan_or_incentive
    - eligibility_award_claim_recognition_cash_clawback
  derivative_or_hybrid:
    - PRS_perpetual_convertible_preferred
    - cash_proceeds_fair_value_PnL_settlement_and_refinancing
```

### 3. Scope Bridge

```text
Project Gross Cost
≠ JV Equity Commitment
≠ SK On Legal Contribution
≠ Parent-guaranteed Exposure
≠ Consolidated Accounting Debt
≠ Cash Drawn and Paid
≠ Net Economic Exposure after Grant·Credit·Partner Contribution
```

---
