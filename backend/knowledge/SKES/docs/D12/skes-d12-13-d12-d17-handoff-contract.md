---
id: skes-d12-13-d12-d17-handoff-contract
title: D12 → D17 Handoff Contract
summary: "프로젝트 인수인계 시 D17 재무 영역에서 필요한 필수 데이터 항목, 재무 검증 기준 10가지, 이익 인정 상태의 진행 단계를 정의하는 계약 기준입니다."
tags: [d12, capex, schema, "xref:d17"]
keywords: [재무 게이트, 필수 필드, 증분 현금흐름, 자금조달 구조, 검증자, O/I 인정, 베이스라인, 자산 ID, 비용절감]
related: []
priority: normal
domain: D12
section: 13
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 544
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 13. D12 → D17 Handoff Contract

## 13.1 Mandatory Fields

```yaml
d17_finance_handoff:
  scope:
    - legal_entity
    - project_spv
    - asset_or_contract_right
    - capacity_and_unit
  investment:
    - case_version
    - decision_gate
    - approved_budget
    - committed
    - paid
    - capitalized
    - cost_to_complete
  funding:
    - sponsor_equity
    - partner_contribution
    - debt_limit_and_drawn
    - guarantee_and_support
    - grant_and_tax_credit_status
  economics:
    - baseline
    - base_downside_severe
    - incremental_forward_cash
    - risk_adjusted_roic_or_npv_if_internal_inputs_exist
  options:
    - expand
    - hold
    - convert
    - refinance
    - sell
    - exit
  governance:
    - finance_validator
    - legal_validator
    - technical_validator
    - source_ids
    - internal_data_ids
```

## 13.2 D17 Finance Gate

아래 중 하나라도 충족하지 못하면 `financially_verified O/I`로 승격하지 않는다.

1. 발표 총액이 아닌 baseline이 존재한다.
2. gross project value와 E&S net cash exposure가 분리된다.
3. sunk cost가 아닌 forward incremental cash가 계산된다.
4. partner·debt·grant·tax-credit 기여가 중복 제거된다.
5. 운전자본·금융비용·보증·exit cost가 누락되지 않는다.
6. 지원금은 eligible/awarded/recognized/cash/clawback 상태가 구분된다.
7. Base/Downside/Severe가 동일한 model version으로 계산된다.
8. Project/asset/right ID가 D07과 연결된다.
9. 비용절감이 D11의 동일 driver와 중복계상되지 않는다.
10. Finance가 baseline과 realized cash를 사후 검증할 수 있다.

## 13.3 O/I Benefit State

```text
IDEA
→ BASELINE_DEFINED
→ TECHNICALLY_VALIDATED
→ FINANCE_MODELLED
→ PILOT_MEASURED
→ FINANCE_VERIFIED
→ CASH_REALIZED
→ SCALED
```

---
