---
id: skon-d09-d09-06-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: 고객·수주·OEM 관계 영역의 AI 데이터 기회 14개를 1~5점으로 평가하고 협력파트너 유형을 제시한 혁신 포트폴리오이자 PoC 진행 가이드.
tags: [d09, customer, schema, table, "xref:d17"]
keywords: [고객, 용량, ESS, 수요예측, PoC, 이상탐지, 평가점수, 지식그래프, 혁신, OEM 포캐스트, ESS 파이프라인, Contract-to-Capacity, 용량 그래프, 데이터스페이스, 고객신용평가, 협상최적화]
related: [OI-D09-01, OI-D09-02, OI-D09-03, OI-D09-04, OI-D09-05, OI-D09-06, OI-D09-07, OI-D09-08, OI-D09-09, OI-D09-10, OI-D09-11, OI-D09-12, OI-D09-13, OI-D09-14]
priority: normal
domain: D09
section: D09-06
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 1370
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09-06 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점)**다. 평가축은 D08과 동일하게 `문제의 크기`, `데이터 확보 가능성`, `6~12개월 PoC`, `SK온 의사결정 연결성`, `외부 협업 필요성`을 사용한다.

| O/I Seed | 과제명 | 해결문제 | 핵심 데이터·PoC | 후보 Partner 유형 | 점수/25 |
|---|---|---|---|---|---:|
| `OI-D09-01` | Contract-to-Capacity Demand Bridge | 다년 총량과 공장계획 단절 | Nissan·Slate·Flatiron 계약을 월별 Scenario로 변환 | S&OP·Optimization Startup | 24 |
| `OI-D09-02` | OEM Forecast Data Space | 고객 Portal·Excel Forecast Version 불일치 | 2~3개 고객 Forecast·Capacity 표준교환 | Catena-X·Data-space Provider | 23 |
| `OI-D09-03` | Program Early-Warning Radar | 차종 지연·취소 반영 지연 | 판매·공장 Shift·정책·뉴스 Signal→Risk Alert | Market Intelligence·AI Startup | 22 |
| `OI-D09-04` | Call-off Anomaly Detector | Forecast 대비 주문 급변 | Forecast–EDI–PO–출하 시계열 이상탐지 | Time-series AI Provider | 22 |
| `OI-D09-05` | Customer-Qualified Capacity Graph | 명목 Capacity를 공급 가능량으로 오인 | 고객–Program–Cell Rev–Plant–Line–승인 Graph | Knowledge Graph·PLM Provider | 25 |
| `OI-D09-06` | Alternative Customer Qualification Engine | 유휴 Line의 전환 지연 | 유사 Cell·시험·4M·승인 Lead time 추천 | Simulation·Materials Informatics | 22 |
| `OI-D09-07` | JV Capacity Governance Cockpit | 파트너 전용 Capacity 의사결정 지연 | HSBMA Forecast·승인·가동·Consent Workflow | JV Workflow·Planning Provider | 20 |
| `OI-D09-08` | Claim & Compensation Root-Cause AI | 보상금·Chargeback 반복 | Claim 문서·8D·품질·납기·계약조항 연결 | Document AI·Process Mining | 23 |
| `OI-D09-09` | Startup Customer Risk Twin | Slate 등 Ramp·신용 불확실성 | Funding·SOP·Supplier·예약·Payment Milestone | Credit·Venture Data Provider | 18 |
| `OI-D09-10` | ESS Pipeline Probability Engine | 1GWh 확정과 6.2GWh Pipeline 혼합 | 개발단계·Interconnection·Permit·Financing·COD | Energy Project Data·AI | 24 |
| `OI-D09-11` | AI Data-Center ESS Demand Twin | Hyperscaler 수요의 Location·Timing 불확실 | Data-center Pipeline–Grid Queue–ESS Sizing | Grid·Data-center Analytics | 22 |
| `OI-D09-12` | EV↔ESS Customer-Mix Optimizer | NCM/LFP·EV/ESS 전환 Trade-off | Margin·전환비·승인·계약·45X Scenario | Operations Research Provider | 25 |
| `OI-D09-13` | Customer Concentration Stress Test | 고객·차종 의존도 불투명 | 고객별 GWh·Margin·Plant·EOP Monte Carlo | Risk Analytics Provider | 23 |
| `OI-D09-14` | Negotiation Scenario Copilot | 가격·물량·Option·보상조건의 복합성 | 승인된 계약 Template 기반 What-if, Human approval | Legal AI·Pricing Analytics | 19 |

### 1. D09 우선 PoC 5개

1. `OI-D09-05 Customer-Qualified Capacity Graph`
2. `OI-D09-12 EV↔ESS Customer-Mix Optimizer`
3. `OI-D09-01 Contract-to-Capacity Demand Bridge`
4. `OI-D09-10 ESS Pipeline Probability Engine`
5. `OI-D09-02 OEM Forecast Data Space`

### 2. 권장 PoC 범위

```yaml
poc_scope:
  duration: 12_to_16_weeks
  customers:
    - one_existing_OEM
    - one_future_OEM_program
    - one_ESS_customer
  plants:
    - one_operating_US_site
    - one_future_or_JV_site
  input:
    - agreement_versions
    - customer_forecast_snapshots
    - firm_calloffs
    - product_and_BOM_revisions
    - plant_line_qualification
    - shipment_and_acceptance
  output:
    - annual_and_monthly_demand_scenarios
    - unallocated_or_unqualified_GWh
    - forecast_error_and_alerts
    - EV_ESS_reallocation_options
    - decision_log_with_human_approval
```

### 3. 성공 KPI

| KPI | 정의 |
|---|---|
| Forecast Version Completeness | 유효 Program 중 Snapshot·Version이 연결된 비율 |
| Contract-to-Call-off Conversion | 계약/Forecast 중 Firm Call-off로 전환된 비율 |
| Qualified Allocation Coverage | Firm 수요 중 고객승인 Plant·Line에 배정된 비율 |
| Unallocated GWh Lead Time | 미배정 수요가 해소되기까지 걸린 시간 |
| Alert Lead Time | Program 변화 신호와 의사결정 사이의 선행시간 |
| EV↔ESS Conversion NPV | 전환비·승인·Margin·세액공제를 반영한 경제가치 |
| Claim Recurrence Rate | 동일 원인의 고객 Claim 재발률 |
| ESS Pipeline Conversion | 우선협상·Bid가 확정계약으로 전환된 비율 |

---
