---
id: skon-d10-d10-07-o-i-opportunity-portfolio
title: O/I Opportunity Portfolio
summary: "기술·시장 기회 15개 평가 점수와 우선 PoC 5개, 추진 범위를 제시하는 전략 의사결정 문서"
tags: [d10, market, schema, table, "xref:d17"]
keywords: [O/I Seed, Innovation Portfolio, PoC 평가, 시장 기회 분석, 신기술 도입, 경쟁사 분석, ESS 배터리, 우선순위 결정, 기회 평가, PoC 우선순위, 기술 신호 탐지, 경쟁 비용 분석, EV ESS 시장, 시나리오 시뮬레이션, 프로젝트 인텔리전스, 의사결정 지원]
related: [OI-D10-01, OI-D10-02, OI-D10-03, OI-D10-04, OI-D10-05, OI-D10-06, OI-D10-07, OI-D10-08, OI-D10-09, OI-D10-10, OI-D10-11, OI-D10-12, OI-D10-13, OI-D10-14, OI-D10-15]
priority: normal
domain: D10
section: D10-07
source: SK온_D10_Market_Competition_Industry_Dynamics.md
breadcrumb: "SK온 D10 — Market, Competition & Industry Dynamics"
tokens: 1494
updated: 2026-08-03
---

> SK온 · D10 시장·경쟁·산업동향 · SK온 D10 — Market, Competition & Industry Dynamics

## D10-07 O/I Opportunity Portfolio

아래 점수는 공개사실이 아니라 D17 선별을 위한 **분석 점수(1~5점, 총 25점)**다. 평가축은 `문제의 크기`, `데이터 확보 가능성`, `6~12개월 PoC`, `의사결정 연결성`, `외부 협업 필요성`이다.

| O/I Seed | 과제명 | 해결문제 | 핵심 데이터·PoC | 후보 Partner 유형 | 점수/25 |
|---|---|---|---|---|---:|
| `OI-D10-01` | Market-to-Capacity Scenario Twin | 시장성장과 공장구성 불일치 | 지역·고객·화학계 수요를 Qualified GWh와 연결 | Market Data·Optimization | 25 |
| `OI-D10-02` | Chemistry Adoption Radar | LFP·Na-ion 전환 대응 지연 | 차종·ESS Project별 Chemistry 채택 Signal | Battery Intelligence·NLP | 23 |
| `OI-D10-03` | Form-Factor Migration Radar | Pouch·Prismatic 전환시점 불명 | OEM Platform·Pack Architecture·공장투자 추적 | Automotive Teardown·Data | 22 |
| `OI-D10-04` | Competitor Cost-Gap Decomposer | 중국 가격격차 원인 불명 | 소재·수율·가동률·설계·물류 Cost Bridge | Cost Engineering·Teardown | 25 |
| `OI-D10-05` | Policy-adjusted Profitability Radar | Credit 포함 이익의 오판 | 제품·공장별 EBIT에서 Credit·보상·환입 분리 | FP&A·Tax Analytics | 24 |
| `OI-D10-06` | EV↔ESS Conversion Option Engine | 전환 순서·경제성 불명 | 설비·BOM·인증·Margin·수요 Scenario | Digital Twin·OR Provider | 25 |
| `OI-D10-07` | ESS Bid & Project Intelligence Graph | Project Pipeline 정보 분산 | Developer·Interconnection·Permit·Financing·COD | Energy Project Data | 24 |
| `OI-D10-08` | AI Data-Center Battery Demand Model | UPS·BBU·Grid ESS 수요혼합 | Data Center MW·Grid Queue·Backup Architecture | Data-center·Grid Analytics | 23 |
| `OI-D10-09` | Competitive Claim Verification Lab | 경쟁사 성능 Claim 비교 오류 | Cell/Pack/System 시험단위·조건 표준화 | Testing Lab·Benchmark Platform | 20 |
| `OI-D10-10` | Multi-Chemistry Portfolio Optimizer | 기술 Portfolio 과다·과소투자 | Segment별 Cost·Performance·SOP·IP·CAPEX | Materials Informatics·OR | 24 |
| `OI-D10-11` | Emerging-Market Entry Radar | 신흥시장 성장 Capture 부족 | EV·Commercial Fleet·ESS·Partner·정책 Signal | Geo-market Intelligence | 19 |
| `OI-D10-12` | Competitor Ecosystem Knowledge Graph | JV·고객·소재·서비스 연결 누락 | 경쟁사–OEM–Supplier–Site–Product–Deal Graph | Knowledge Graph Provider | 23 |
| `OI-D10-13` | Price-war Stress Simulator | 가격하락 시 손익·가동률 충격 | ASP·원료·수율·가동률·환율 Scenario | Pricing·Risk Analytics | 24 |
| `OI-D10-14` | Roadmap-to-SOP Speed Benchmark | 기술발표와 양산속도 격차 | Patent·Sample·Qualification·SOP Event Timeline | Tech Intelligence·Process Mining | 22 |
| `OI-D10-15` | Market Signal Decision Copilot | Signal 수집 후 실행 지연 | 승인된 Source→영향공장·제품→Action Draft | Enterprise Search·Agentic Workflow | 22 |

### 1. D10 우선 PoC 5개

1. `OI-D10-01 Market-to-Capacity Scenario Twin`
2. `OI-D10-04 Competitor Cost-Gap Decomposer`
3. `OI-D10-06 EV↔ESS Conversion Option Engine`
4. `OI-D10-05 Policy-adjusted Profitability Radar`
5. `OI-D10-07 ESS Bid & Project Intelligence Graph`

### 2. 권장 PoC 범위

```yaml
poc_scope:
  duration: 12_to_16_weeks
  market_scope:
    - North_America_EV
    - North_America_ESS_and_AI_data_center
    - Europe_EV
  product_scope:
    - high_nickel_pouch
    - LFP_prismatic_or_containerized_ESS
  plant_scope:
    - one_operating_US_EV_line
    - one_EV_to_ESS_conversion_candidate
  competitor_scope:
    - CATL
    - LG_Energy_Solution
    - Samsung_SDI
  input:
    - market_actuals_and_forecast_versions
    - customer_program_and_calloff_data
    - product_BOM_and_cost_bridge
    - plant_line_capacity_yield_and_qualification
    - policy_credit_and_localization_rules
    - competitor_product_site_and_deal_events
  output:
    - market_to_qualified_capacity_gap
    - chemistry_and_form_factor_scenarios
    - competitor_cost_gap_hypotheses
    - EV_to_ESS_conversion_options
    - recurring_profitability_view
    - human_approved_decision_log
```

### 3. 성공 KPI

| KPI | 정의 |
|---|---|
| Market-to-Capacity Mapping Coverage | 우선시장 수요 중 제품·공장·Line까지 연결된 비율 |
| Scenario Refresh Lead Time | 시장·정책 Signal 발생 후 계획 Scenario 갱신시간 |
| Cost Gap Explainability | 경쟁 가격차 중 원인별로 설명 가능한 비율 |
| Chemistry Forecast Error | Segment별 Chemistry Mix 예측과 Actual의 차이 |
| Conversion Decision Lead Time | EV→ESS 전환안 생성부터 승인까지 시간 |
| Recurring EBIT Accuracy | 일회성·Credit 제외 예측 EBIT와 Actual의 차이 |
| ESS Pipeline Conversion | 식별 Project가 Bid·계약으로 전환된 비율 |
| Decision Adoption Rate | 제안 Scenario 중 실제 S&OP·투자검토에 사용된 비율 |

---
