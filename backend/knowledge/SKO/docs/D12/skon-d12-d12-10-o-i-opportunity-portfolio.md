---
id: skon-d12-d12-10-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: SK온 투자기회 15개를 현금영향·데이터확보·PoC 등 5가지 기준으로 채점한 평가표 및 우선 PoC 선정안
tags: [d12, capex, schema, table, "xref:d17"]
keywords: [CAPEX, 투자 기회 과제, Stage-Gate, PoC, 현금영향, Real-options, 자금조달, ESS 전환, JV 자본호출, 손상 조기경고, CAPEX계획, 투자기회평가, Real-Options분석, 자산-부채그래프, 프로젝트비용예측, 현금흐름최적화, 협약감시, 디지털트윈, NPV평가, PoC우선순위]
related: [OI-D12-01, OI-D12-02, OI-D12-03, OI-D12-04, OI-D12-05, OI-D12-06, OI-D12-07, OI-D12-08, OI-D12-09, OI-D12-10, OI-D12-11, OI-D12-12, OI-D12-13, OI-D12-14, OI-D12-15]
priority: normal
domain: D12
section: D12-10
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 1473
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-10 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점, 총 25점)**다. 평가축은 `현금·투자영향`, `내부 데이터 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부 협업 필요성`이다.

| O/I ID | 후보과제 | 핵심 기능 | 외부 Partner 유형 | KPI | 점수 |
|---|---|---|---|---|---:|
| `OI-D12-01` | CAPEX Real-Options Stage-Gate Engine | 수요·승인·정책 Trigger별 expand/hold/convert/exit 비교 | Real-options·FP&A analytics | avoided CAPEX, risk-adjusted NPV | 25 |
| `OI-D12-02` | Asset–Debt–Guarantee Knowledge Graph | 법인·공장·대출·보증·Partner 의무 연결 | LegalTech·Knowledge graph | obligation coverage, orphan exposure | 25 |
| `OI-D12-03` | Project Cost-to-Complete Causal AI | WBS·진척·Change Order·일정으로 EAC 예측 | Construction analytics·Causal AI | EAC error, overrun lead time | 24 |
| `OI-D12-04` | Ramp-to-Cash Liquidity Twin | CAPEX·Ramp·재고·Credit·Debt Service 월별 현금통합 | Treasury analytics·Digital twin | minimum cash, forecast error | 25 |
| `OI-D12-05` | Incentive Covenant & Clawback Monitor | 고용·투자·생산·보고 조건 자동 증빙 | RegTech·TaxTech·Workflow | covenant coverage, clawback-at-risk | 24 |
| `OI-D12-06` | Brownfield Conversion Digital Twin | EV→ESS·Pouch→Prismatic의 Layout·Utility·승인 검증 | Industrial 3D·Simulation | conversion CAPEX, lead-time | 24 |
| `OI-D12-07` | Funding Instrument All-in Cost Engine | Debt·Equity·PRS·우선주·영구채의 경제비용 비교 | TreasuryTech·Derivative analytics | all-in cost, settlement VaR | 23 |
| `OI-D12-08` | JV Capital Call & Partner Risk Radar | 약정·납입·Default·분담·Remedy 추적 | Contract analytics·Risk data | overdue call, partner exposure | 23 |
| `OI-D12-09` | Impairment Early-Warning Engine | 수요·가동률·Margin·정책·EAC로 CGU 위험 탐지 | Valuation AI·Scenario platform | alert lead time, false alarm | 24 |
| `OI-D12-10` | Grant & Green-Finance Eligibility Graph | 자산·Use-of-Proceeds·성과지표·신청기회 연결 | Climate FinTech·Grant intelligence | eligible funding captured | 22 |
| `OI-D12-11` | CAPEX Procurement Benchmark Network | 설비·공사 Package별 익명 Benchmark와 Change Order 탐지 | Procurement analytics·Clean room | unit cost gap, change-order rate | 21 |
| `OI-D12-12` | Contractor Schedule-Risk Twin | Critical Path·공급망·현장진척의 지연확률 예측 | Project controls·Computer vision | delay lead time, milestone hit rate | 22 |
| `OI-D12-13` | Asset Reuse & Monetization Marketplace | 유휴설비·Spare·건물의 재사용·매각 Option 연결 | Industrial marketplace·Asset analytics | cash released, reuse rate | 21 |
| `OI-D12-14` | Utility Capacity & Tariff Investment Optimizer | 전력·가스·용수·폐수 투자와 Peak·증설 비교 | Energy systems·Optimization | utility CAPEX, cost/accepted kWh | 22 |
| `OI-D12-15` | Post-Investment Review Closed Loop | 승인 가정과 실제 Ramp·현금·ROIC 차이를 다음 투자에 학습 | Process mining·Decision intelligence | PIR coverage, forecast bias | 24 |

### 우선 PoC 5개

| 우선순위 | 후보 | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `OI-D12-01 CAPEX Real-Options Stage-Gate Engine` | 1개 기존공장의 EV 유지·ESS 전환·휴지 Option | Scenario별 증분 NPV·중단조건과 CFO 승인 Trace |
| 2 | `OI-D12-02 Asset–Debt–Guarantee Knowledge Graph` | BOSK 해소 전후 Tennessee·Kentucky 의무 | 자산·부채·보증·계약 100% 법인·Clause 연결 |
| 3 | `OI-D12-04 Ramp-to-Cash Liquidity Twin` | HSBMA 또는 1개 Ramp 공장의 18개월 월별 전망 | Cash Forecast 오차 감소와 Downside Runway 가시화 |
| 4 | `OI-D12-03 Project Cost-to-Complete Causal AI` | 1개 전환·증설 Project의 WBS·EAC | Cost Overrun 3개월 이상 선행경보 |
| 5 | `OI-D12-05 Incentive Covenant & Clawback Monitor` | 미국 1개 공장의 계약·고용·투자·보고조건 | 모든 Covenant에 Owner·Evidence·Alert·Exposure 연결 |

### PoC 공통 설계

```yaml
d12_poc_common_design:
  baseline:
    - approved_business_case_version
    - monthly_cash_and_physical_progress
    - customer_qualification_and_demand_scenario
  finance_validation:
    - CFO_controller_treasury_and_legal_signoff
    - reconcile_gross_project_JV_entity_and_parent_scope
    - distinguish_cash_saving_accounting_effect_and_avoided_CAPEX
    - no_double_counting_of_grant_credit_partner_contribution_and_asset_sale
  decision_safety:
    - human_approval_for_CAPEX_debt_guarantee_shutdown_and_asset_sale
    - model_outputs_are_scenario_ranges_not_single_point_truth
  security:
    - restricted_access_to_contract_rate_covenant_and_financing_terms
    - source_document_clause_and_model_version_lineage
    - OT_and_construction_system_separation
```

---
