---
id: skes-d11-18-priority-poc-portfolio
title: Priority PoC Portfolio
summary: "에너지·발전사업의 원가 절감과 수익성 개선을 목표로 하는 15개 PoC 프로젝트의 순위, 범위, 성공조건과 실행 통제 프레임워크."
tags: [d11, cost, schema, table, "xref:d17"]
keywords: [원가절감, 발전마진, BESS, 수소, 사업타당성, 통제체계, 에너지효율, CCS]
related: [SEED-ENS-D11-002, SEED-ENS-D11-007, SEED-ENS-D11-017, SEED-ENS-D11-018, SEED-ENS-D11-022, SEED-ENS-D11-024, SEED-ENS-D11-029, SEED-ENS-D11-035, SEED-ENS-D11-036, SEED-ENS-D11-042, SEED-ENS-D11-048, SEED-ENS-D11-050, SEED-ENS-D11-054, SEED-ENS-D11-003, SEED-ENS-D11-060]
priority: normal
domain: D11
section: 18
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 855
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 18. Priority PoC Portfolio

## 18.1 D17 우선 전달 후보 15개

| Rank | Seed | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `SEED-ENS-D11-002` Segment-to-Asset Margin Graph | 1개 발전소+연결 LNG 경로 | Segment Control Total 98% 이상 조정 |
| 2 | `SEED-ENS-D11-007` Cargo Landed-cost Twin | 10~20개 Cargo | Cargo별 실제원가·정산 Bridge 95% 이상 |
| 3 | `SEED-ENS-D11-017` Heat-rate-to-P&L AI | 1개 CCGT Unit | 연료효율 개선과 EBIT을 Finance 검증 |
| 4 | `SEED-ENS-D11-018` Outage Economic Prioritizer | 핵심 설비군 1개 | 안전 유지·Lost Margin 감소 |
| 5 | `SEED-ENS-D11-022` CHP Co-optimizer | 1개 CHP·1개 계절 | 전력·열 SLA 유지, Joint Margin 개선 |
| 6 | `SEED-ENS-D11-024` Gas Mass-balance | 1개 도시가스 권역 | 미계량가스 원인·가치 90% 분류 |
| 7 | `SEED-ENS-D11-029` PPA Shape Pricing | 신규·기존 PPA 각 2건 | Quote-to-actual Margin 오차 감소 |
| 8 | `SEED-ENS-D11-035` BESS Counterfactual Lab | KCE 프로젝트 1~2개 | 동일 제약 Shadow Bid 대비 검증 |
| 9 | `SEED-ENS-D11-036` Degradation-aware Bid | BESS 1개 자산 | 열화 포함 Lifecycle Margin 개선 |
| 10 | `SEED-ENS-D11-042` Charging Site Scorer | 운영 Site 20개 | Site별 Breakeven·확장 Gate 정립 |
| 11 | `SEED-ENS-D11-048` Paid-kg H2 Cost Twin | 인천 Plant→1개 Cluster | 생산→판매 kg·원가 95% 조정 |
| 12 | `SEED-ENS-D11-050` Hydrogen BOG Router | Tank·Tanker·Station 1개 Route | 안전범위 내 회수/회피가치 검증 |
| 13 | `SEED-ENS-D11-054` CCS Match Graph | Bayu-Undan 후보 Emitter | Firm volume·COD·권리 Gate |
| 14 | `SEED-ENS-D11-003` Benefit Double-count Guard | 상위 개선과제 20개 | 중복·회피·현금 분류 100% |
| 15 | `SEED-ENS-D11-060` Capital Real-options Gate | H2·CCS·재생 후보 각 1건 | Downside·Exit 포함 Risk-adjusted NPV |

## 18.2 PoC 공통 통제

```yaml
d11_poc_control:
  baseline:
    - finance_approved_scope_period_and_counterfactual
    - minimum_12_months_or_full_operating_cycle
    - preserve_weather_market_and_maintenance_context
  measurement:
    - use_paid_physical_unit_not_nameplate
    - same_currency_and_settlement_boundary
    - separate_accounting_cash_avoided_and_risk_value
    - prevent_overlap_between_volume_efficiency_reliability_and_inventory
  approval:
    - business_owner
    - operations_or_OT_owner
    - controller_or_FPandA
    - safety_regulatory_and_cyber_review
  automation_limit:
    - no_autonomous_process_setpoint
    - no_autonomous_market_bid_without_limit
    - no_autonomous_shutdown_or_maintenance
    - no_autonomous_contract_or_CAPEX_commitment
  scale_gate:
    - verified_recurring_benefit
    - positive_downside_case_or_documented_strategic_option
    - integration_and_change_cost_included
    - data_rights_security_and_vendor_exit_confirmed
```

---
