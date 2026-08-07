---
id: skon-d12-d12-07-covenant-guarantee-incentive-control
title: "Covenant, Guarantee & Incentive Control"
summary: SK온 CAPEX 자금조달 시 채무약정·정부보증·지역인센티브를 통합 관리하는 방식과 위반 탐지 규칙을 정의한다.
tags: [d12, capex, schema]
keywords: [부채약정, 고용·투자약속, 정부인센티브, HSBMA, Clawback위험, 보증한도, 약정이행, 환경의무, CAPEX, covenant 약정, 고용 투자 조건, clawback 리스크, 채무약정 모니터링, 보증 한도, 생산 목표, 정부지원금]
related: []
priority: normal
domain: D12
section: D12-07
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 606
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-07 Covenant, Guarantee & Incentive Control

### 1. HSBMA와 지역 Incentive

SK이노베이션 2026 Q1 공시는 HSBMA가 현지정부와 고용·투자 조건부 Incentive Agreement를 체결했고, 관련 의무를 위한 SK온 계열의 지원약정이 있음을 설명한다. 공개 발췌만으로 금액과 Threshold를 확정할 수 없으므로 `employment`, `qualified investment`, `production`, `reporting`, `environmental obligation`, `clawback`을 계약원문 기준으로 관리해야 한다. ([SK Innovation 2026 Q1 Report](https://kind.krx.co.kr/external/2026/05/15/001636/20260515003618/11013.htm), [Georgia Incentive Summary](https://georgia.org/sites/default/files/2023-09/hyundai_motor_group_incentives_-_updated_executive_summary_09.08.23_final.pdf))

### 2. 통합 Covenant Ledger

```yaml
covenant_control:
  event_types:
    - debt_financial_covenant
    - employment_and_investment_commitment
    - production_start_and_maintenance_period
    - community_benefit_and_reporting
    - environmental_and_site_restoration
    - customer_volume_or_supply_commitment
    - partner_capital_call_and_default
  statuses:
    - compliant
    - watch
    - cure_period
    - breached
    - waived
    - released
  mandatory_links:
    - legal_document_and_clause
    - legal_entity_and_facility
    - responsible_owner
    - measurement_period_and_evidence
    - cash_or_guarantee_exposure
    - remediation_and_approval
```

### 3. 통제 Rule

- 승인한도나 보증 Maximum을 Expected Loss와 동일시하지 않는다.
- 정부지원 수령액을 CAPEX 절감으로 반영할 때 현금수령과 Clawback Risk를 함께 표시한다.
- 자산이 Partner에게 이전되면 관련 Debt·Guarantee·Grant·환경의무가 실제로 함께 이전됐는지 Clause별로 확인한다.
- AI는 위반 가능성을 탐지하고 근거를 제시하되, 차입·보증·CAPEX 중단·자산매각을 자동 실행하지 않는다.

---
