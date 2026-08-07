---
id: skes-d11-5-enterprise-profitability-bridge
title: Enterprise Profitability Bridge
summary: 공시 매출·영업이익에서 사업·자산별 반복수익까지 조정하는 8단계 프로세스와 계절성·정비·일회성 항목별 처리 기준을 제시하는 문서.
tags: [d11, cost, schema, table]
keywords: [반복이익, 계절성 정상화, EBIT 조정, 일회성 손익, 정비비 처리, LNG 재고평가, 파생상품 헤징, 내부거래 제거, Top-down reconciliation, Recurring profit]
related: []
priority: normal
domain: D11
section: 5
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 856
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 5. Enterprise Profitability Bridge

## 5.1 Top-down to Bottom-up Reconciliation

```yaml
reconciliation_sequence:
  step_1: lock_disclosed_ENS_revenue_and_operating_profit
  step_2: map_legal_entities_and_consolidation_eliminations
  step_3: map_business_and_asset_management_views
  step_4: reconcile_physical_volume_to_billed_volume
  step_5: reconcile_contract_settlement_to_revenue
  step_6: reconcile_cost_ledger_to_asset_and_customer_objects
  step_7: separate_recurring_one_off_and_timing_items
  step_8: reconcile_EBIT_to_cash_and_working_capital
  tolerance_rule: finance_approved_and_documented
```

## 5.2 Recurring Profit Adjustment Register

| Adjustment | 발생 예 | 반복 EBIT 처리 | 현금 확인 |
|---|---|---|---|
| 도시가스 계절성 | 난방수요 Q1/Q4 집중 | 기상정상화·계절지수로 분리 | 판매대금 회수 |
| 발전소 계획정비 | 정비기간 매출감소·비용 | 표준 정비주기 내 반복비용 | 정비대금·Lost Margin |
| 비계획 정지 | 설비 고장·연료 제약 | 발생원인별 반복확률 반영 | 보험·보상·수리비 |
| LNG 재고평가 | 가격·환율 변화 | 물리·회계·Hedge Timing 분리 | 매입·정산 시점 |
| 파생상품 | LNG·유가·FX Hedge | 대상거래와 함께 평가 | Margin call·정산 |
| Cargo Diversion | 목적지 변경·재판매 | 반복 Trading 역량 여부 확인 | 추가운임·정산 |
| 자산매각 | 터미널 지분 등 | 핵심 반복이익에서 제외 | 매각대금·TUA 의무 |
| 개발비 | 재생·수소·CCS Pipeline | Stage별 비용·자본화 분리 | 실제 지출·Write-off |
| 보조금·세액공제 | 재생·수소·CCS | Policy-on/off 병렬 Scenario | 신청·인식·수취 |
| 지분법손익 | JV 프로젝트 | EBITDA와 배당현금 분리 | 실제 Distribution |
| 충당금·손상 | 자산·계약·보증 | 반복 EBIT 제외 가능, ROIC 반영 | 비현금·미래지출 분리 |
| 내부거래 제거 | LNG 공급→발전·도시가스 | 외부 Margin만 보존 | Transfer price 제거 |

## 5.3 Seasonality Normalization

```text
Weather-normalized city-gas volume
= actual volume − modelled HDD/CDD effect

Maintenance-normalized power margin
= actual power margin
+ approved planned-outage lost contribution
− non-recurring outage insurance recovery

Portfolio normalized EBIT
= sum of recurring contract and asset margins
− recurring corporate/shared-service cost
− expected annualized outage and development-failure cost
```

정상화는 좋은 결과를 만들기 위한 조정이 아니다. 일회성 이익과 비용을 같은 정책으로 분류하고, 조정 전·후 수치와 현금영향을 모두 보존해야 한다.

---
