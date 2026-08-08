---
id: skon-d11-d11-09-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: 배터리 생산의 원가·수익성 개선을 위한 15개 프로젝트의 평가점수(손익영향·PoC 실행성 등 5개축)와 우선순위 선별 현황
tags: [d11, cost, schema, table, "xref:d17"]
keywords: [원가 절감, 수익성 개선, 기회과제, Digital Twin, Causal AI, D11, PoC, 평가 점수, KPI, 배터리, 마진, 수율 개선, 공정 최적화, 에너지 비용, 우선순위]
related: [OI-D11-01, OI-D11-02, OI-D11-03, OI-D11-04, OI-D11-05, OI-D11-06, OI-D11-07, OI-D11-08, OI-D11-09, OI-D11-10, OI-D11-11, OI-D11-12, OI-D11-13, OI-D11-14, OI-D11-15]
priority: normal
domain: D11
section: D11-09
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1416
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-09 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점, 총 25점)**다. 평가축은 `손익영향`, `내부 데이터 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부 협업 필요성`이다.

| O/I ID | 후보과제 | 핵심 기능 | 외부 Partner 유형 | KPI | 점수 |
|---|---|---|---|---|---:|
| `OI-D11-01` | Qualified-kWh Cost Digital Twin | 생산→합격→출하→인수량과 실제원가 연결 | Battery TEA·Industrial data platform | cost/accepted kWh, close latency | 25 |
| `OI-D11-02` | Recurring Profit Waterfall Engine | Credit·보상·환입·Ramp를 자동 분류해 정상화 범위 제시 | Finance AI·Accounting analytics | bridge coverage, recurring EBIT accuracy | 24 |
| `OI-D11-03` | Yield-to-Margin Causal AI | 공정조건·검사·Scrap을 원화·kWh 손실로 변환 | Causal AI·Sensor·Process analytics | FPY, COPQ, recovered margin | 25 |
| `OI-D11-04` | Fixed-Cost Absorption & Mix Optimizer | 고객승인·Call-off·Changeover를 반영한 Line Mix 최적화 | Operations research·APS | fixed cost/kWh, qualified utilization | 24 |
| `OI-D11-05` | Customer Program Lifecycle Economics Graph | 견적부터 EOP·Warranty까지 Cost-to-Serve 추적 | Knowledge graph·CPQ/PLM analytics | quote-to-actual gap, CTS coverage | 24 |
| `OI-D11-06` | AMPC Eligibility-to-Cash Ledger | 적격 kWh·귀속·신청·인식·현금·Clawback 연결 | TaxTech·Compliance ledger | eligible-to-cash reconciliation | 23 |
| `OI-D11-07` | Metal & FX Margin Guardrail | 계약연동·재고·Hedge 시차의 Margin-at-Risk 계산 | Commodity/FX analytics | leakage/kWh, hedge effectiveness | 22 |
| `OI-D11-08` | Scrap & Rework Economic Router | Scrap Lot별 재작업·재활용·폐기 최적경로 | Circularity platform·Optimization | recovery value, rework ROI | 22 |
| `OI-D11-09` | Energy Cost Flex Scheduler | 전력Tariff·Peak·공정제약 기반 Schedule | Energy AI·EMS·Demand response | energy/accepted kWh, peak charge | 22 |
| `OI-D11-10` | Warranty Risk-to-Margin Early Warning | Field/BMS·품질·충당금의 Lifetime Margin 예측 | Reliability AI·Warranty analytics | expected loss/kWh, alert lead time | 23 |
| `OI-D11-11` | EV→ESS Conversion NPV Configurator | 설비개조·승인·Ramp·Opportunity Cost Scenario | Digital twin·TEA·Simulation | NPV accuracy, decision lead time | 23 |
| `OI-D11-12` | Make-Buy-Localize Landed-Cost Optimizer | BOM·물류·관세·Credit·Risk를 통합 | Supply-chain design·TEA | landed cost, risk-adjusted NPV | 21 |
| `OI-D11-13` | Slow-moving Inventory Cash Engine | Program 변경·Shelf-life·재고평가 위험 조기경보 | Inventory AI·Process mining | DIO, obsolete inventory, cash release | 22 |
| `OI-D11-14` | ESS Bid-to-Lifetime-Margin Engine | Cell·System·Warranty·COD·LD를 입찰경제성으로 연결 | Project finance·BESS analytics | bid margin accuracy, variance at COD | 23 |
| `OI-D11-15` | CAPEX Real-options Stage Gate | 수요·승인·정책 Trigger별 증설·휴지·전환 Option 평가 | Real-options·Scenario analytics | avoided CAPEX, ROIC, exit cost | 22 |

### 우선 PoC 5개

| 우선순위 | 후보 | 6~12개월 PoC 범위 | 성공조건 |
|---:|---|---|---|
| 1 | `OI-D11-01 Qualified-kWh Cost Digital Twin` | 1개 Plant·1개 Program·월별 Close | 표준원가와 실제원가, 수율·물량 차이 95% 이상 Bridge |
| 2 | `OI-D11-03 Yield-to-Margin Causal AI` | Coating~Formation 중 고손실 1개 공정 | FPY 개선과 원화 절감의 통계·재무 검증 |
| 3 | `OI-D11-02 Recurring Profit Waterfall Engine` | Battery Segment→2개 Plant 내부 Bridge | 조정항목 100% 근거·승인·현금영향 연결 |
| 4 | `OI-D11-04 Fixed-Cost Absorption & Mix Optimizer` | 1개 지역의 고객승인 Line 배정 | 서비스율 유지하며 fixed cost/accepted kWh 감소 |
| 5 | `OI-D11-05 Customer Program Lifecycle Economics Graph` | 신규/양산/EOP Program 각 1개 | Quote-to-actual Gap과 미청구 CTS 가시화 |

### PoC 공통 설계

```yaml
d11_poc_common_design:
  baseline_period: minimum_12_months_or_full_program_phase
  economic_unit: KRW_per_customer_accepted_kWh
  control_group: comparable_line_shift_or_product_when_possible
  finance_validation:
    - controller_signoff
    - no_double_counting_between_yield_utilization_energy_and_inventory
    - distinguish_accounting_saving_cash_saving_and_avoided_cost
  operational_safety:
    - human_approval_for_setpoint_schedule_bid_and_shutdown
    - no_unvalidated_model_writeback_to_process_control
  security:
    - customer_contract_and_price_access_control
    - plant_OT_network_separation
    - source_lineage_and_model_version
```

---
