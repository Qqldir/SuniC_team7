---
id: skon-d11-d11-01-economics-data-model
title: Economics Data Model
summary: "배터리 제품의 원가·수익성·현금화를 고객·제품·공장별로 추적하기 위한 11개 데이터 엔터티와 경제성 상태 어휘, 보고 범위 정의."
tags: [d11, cost, schema, table]
keywords: [원가분석, 수익성, 경제성증거, ProgramEconomics, CostLedger, 보고범위, 데이터엔터티, Margin, 원가·수익, 비용체계, 원가, 배터리, 마진, 현금, 수율, 가격, 고객, 공장, 시나리오]
related: []
priority: normal
domain: D11
section: D11-01
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 800
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-01 Economics Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `ReportingScope` | `scope_id + period` | segment/entity/JV·연결범위·회계기준·통화 |
| `ProgramEconomics` | `customer_program_id + product_id + plant_id + period` | 견적·판매량·가격·원가·Margin·현금 |
| `VolumeWaterfall` | `plant_id + line_id + period` | nameplate→planned→produced→good→shipped→accepted kWh |
| `PriceBridge` | `contract_id + period` | 기준가격·Metal/FX 연동·Premium·Claim·실현가격 |
| `CostLedger` | `cost_object_id + period` | 소재·가공·고정비·물류·품질·Warranty·감가상각 |
| `YieldLossEvent` | `line_id + process_step + lot + timestamp` | Scrap/Rework·원인·재료·Capacity·Margin 손실 |
| `PolicyCredit` | `facility_id + eligible_component + tax_period` | 적격 kWh·법적 요건·신청·인식·현금화·Clawback |
| `OneOffAdjustment` | `event_id + accounting_period` | 보상·환입·손상·구조조정·현금/비현금·반복성 |
| `WorkingCapital` | `entity_id + period` | 재고·매출채권·매입채무·재고평가·현금전환주기 |
| `EconomicsScenario` | `scenario_id + version` | 가격·물량·수율·가동률·환율·원료·Credit 가정 |
| `ImprovementInitiative` | `initiative_id` | Baseline·원인·투자비·절감액·Owner·실현·검증 |

### 2. 상태 Vocabulary

```yaml
economics_evidence_status:
  REPORTED:
    meaning: 공시·실적발표에 보고된 값
  DERIVED_FROM_REPORTED:
    meaning: 동일 범위의 공개수치로 단순 산술 계산한 값
  COMPANY_EXPLANATION:
    meaning: 회사가 제시한 증감 원인이나 전망
  INTERNAL_REQUIRED:
    meaning: 제품·공장·고객 내부 데이터가 있어야 계산 가능
  ANALYTICAL_PROXY:
    meaning: 의사결정을 위한 단순 Proxy이며 회계상 실적이 아님
  NOT_CALCULABLE_FROM_PUBLIC_DATA:
    meaning: 필수 조정금액 또는 분모가 공개되지 않아 산출 금지
```

### 3. Scope Key

```yaml
reporting_scope_control:
  battery_segment:
    definition: SK Innovation 공시의 Battery 사업부문
    use: 외부 공시 Trend와 Segment Margin
  consolidated_SK_On_entity:
    definition: 해당 시점 회사가 제시한 SK온 연결범위
    use: 법인·합병효과와 연결손익
  plant_program_management_view:
    definition: plant-product-customer-program 내부 관리단위
    use: 원인분석과 개선 의사결정
    public_status: NOT_DISCLOSED
  rule: never_compare_or_sum_without_scope_bridge
```

---
