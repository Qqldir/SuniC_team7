---
id: skes-d11-4-canonical-economics-data-model
title: Canonical Economics Data Model
summary: "계약·자산·전력·수소 등 다양한 사업 영역의 경제성을 표준화된 데이터 엔터티, 손익 정상화 기준, 편익 분류 체계로 측정·보고하기 위한 SK이노베이션 E&S의 핵심 데이터 모델"
tags: [d11, cost, table, "xref:d17"]
keywords: [경제성분석, 손익정상화, 편익분류, ContractEconomics, 수익성측정, 원가절감, 현금기여, EBIT/EBITDA, 사업이코노믹스, 자산경제성]
related: []
priority: normal
domain: D11
section: 4
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1116
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 4. Canonical Economics Data Model

## 4.1 핵심 엔터티

| Entity | Primary Key | 최소 필드 |
|---|---|---|
| `ReportingScope` | `scope_id + period` | entity·segment·JV·currency·accounting standard |
| `ProfitBridge` | `scope_id + period + bridge_version` | reported→normalized→cash adjustments |
| `ContractEconomics` | `contract_id + delivery_period` | price formula·volume·optionality·penalty·settlement |
| `CargoEconomics` | `cargo_id + route_id` | source·FOB/DES·shipping·terminal·inventory·destination |
| `AssetEconomics` | `asset_id + period` | capacity·availability·throughput·fixed/variable cost·cash |
| `PowerDispatchEconomics` | `unit_id + interval` | SMP·fuel·heat rate·start cost·emission·dispatch·margin |
| `HeatEconomics` | `CHP_id + interval` | heat load·power co-product·fuel allocation·margin |
| `CustomerEconomics` | `customer_id + tariff_or_contract + period` | volume·revenue·service cost·credit·churn·cash |
| `PPAEconomics` | `PPA_id + settlement_interval` | generation·load shape·price·REC·imbalance·curtailment |
| `BESSEconomics` | `project_id + interval + market` | bid·award·dispatch·SOC·degradation·revenue·penalty |
| `ChargingEconomics` | `site_id + port_id + session` | capex·demand charge·energy·fee·uptime·service cost |
| `HydrogenEconomics` | `plant_id + batch_or_day` | feedstock·production·liquefaction·BOG·delivery·sale |
| `CCSEconomics` | `hub_id + emitter_id + tonne` | capture·transport·storage·MRV·liability·tariff |
| `WorkingCapital` | `entity_or_project + period` | inventory·receivable·payable·collateral·cash cycle |
| `ImprovementBenefit` | `initiative_id + baseline_version` | capex·opex·saving·avoided cost·cash·validator |

## 4.2 Profit Waterfall

```text
Reported Operating Profit
− one-off gain / temporary settlement / asset disposal
+ one-off loss / temporary shutdown only when evidence supports normalization
± inventory valuation / FX / commodity hedge timing normalization
± development capitalization and impairment scope bridge
± equity-method and consolidation elimination bridge
= Normalized Recurring EBIT Range

Normalized Recurring EBIT
+ depreciation and amortization
= Recurring EBITDA

Recurring EBITDA
− maintenance CAPEX
− growth CAPEX attributable to operating period
− increase in working capital and collateral
− cash tax / interest / JV settlement
= Operating Cash Contribution
```

## 4.3 Benefit Classification

| Benefit class | 정의 | D17 인정 조건 |
|---|---|---|
| `P&L_REDUCTION` | 실제 비용계정 감소 | 동일 물량·품질·안전 조건, Controller 확인 |
| `CASH_RELEASE` | 재고·채권·담보 등 현금 회수 | 현금흐름표 또는 Treasury 확인 |
| `AVOIDED_COST` | 계획된 비용·CAPEX 회피 | 승인된 Baseline 계획과 비교 |
| `REVENUE_UPLIFT` | 동일 위험에서 실현 순매출 증가 | Counterfactual·정산내역 검증 |
| `RISK_REDUCTION` | 손실확률·Tail Loss 감소 | 확률·노출액·검증기간 명시 |
| `CAPACITY_RELEASE` | 동일 자산으로 추가 처리량 | 실제 추가 판매·기여이익 확인 |
| `POTENTIAL_VALUE` | 아직 실현되지 않은 분석가치 | 확정 절감으로 보고 금지 |

## 4.4 공통 Unit Economics 공식

```text
Unit contribution
= realized net revenue per physical unit
− variable feedstock and procurement cost
− conversion and utility cost
− logistics and terminal cost
− market settlement and imbalance cost
− quality, reliability and expected loss cost
− variable carbon and compliance cost

Asset recurring EBIT
= unit contribution × paid physical volume
− fixed operating cost
− fixed access/tolling/use-or-pay cost
− depreciation and recurring development expense

Risk-adjusted project NPV
= Σ probability-weighted after-tax free cash flow_t / (1+WACC)^t
− initial CAPEX
− decommissioning and contingent liability present value
```

---
