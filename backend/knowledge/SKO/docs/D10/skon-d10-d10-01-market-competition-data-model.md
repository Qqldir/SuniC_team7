---
id: skon-d10-d10-01-market-competition-data-model
title: Market & Competition Data Model
summary: "시장·경쟁 데이터를 수집·관리하는 표준 엔터티 스키마, 데이터 상태 분류, 비교 단위 통제 기준을 정의한 모델."
tags: [d10, market, schema, table]
keywords: [MarketSnapshot, 시장규모, CompetitorMove, 경쟁사동향, PriceSignal, 가격신호, LFP·NCM·NCA, 배터리기술, Scenario, EV·BESS·UPS, 경쟁사, 시장신호, 배터리화학, 데이터상태, 점유율, 원료가격, FormFactor, 엔터티, Exposure, 비교단위]
related: []
priority: normal
domain: D10
section: D10-01
source: SK온_D10_Market_Competition_Industry_Dynamics.md
breadcrumb: "SK온 D10 — Market, Competition & Industry Dynamics"
tokens: 620
updated: 2026-08-03
---

> SK온 · D10 시장·경쟁·산업동향 · SK온 D10 — Market, Competition & Industry Dynamics

## D10-01 Market & Competition Data Model

### 1. 핵심 엔터티

| 엔터티 | 기본 키 | 최소 필드 |
|---|---|---|
| `MarketSnapshot` | `market_id + period + geography` | 수요량·단위·Actual/Forecast·범위·출처 |
| `Segment` | `segment_id` | EV/BESS/UPS/BBU/Truck·고객유형·Duty cycle |
| `ChemistryMarket` | `chemistry_id + period + geography` | LFP/NCM/NCA/Na-ion 등 점유·가격·성능요구 |
| `FormFactorMarket` | `form_factor_id + period` | Pouch/Prismatic/Cylindrical·적용시장·변화방향 |
| `Competitor` | `competitor_id` | 본사국가·주력제품·시장·통합범위 |
| `CompetitorMove` | `move_id + announced_at` | 기술·Capacity·고객·ESS·현지화·서비스 전략 |
| `PriceSignal` | `signal_id + period` | Pack·원료·지역가격 Index·변화율·근거 |
| `Exposure` | `exposure_id` | 시장변화–SK온 제품–고객–공장–손익 연결 |
| `StrategicGap` | `gap_id` | 경쟁격차·원인·영향·내부 검증데이터 |
| `Scenario` | `scenario_id + version` | 가정·시장변수·Trigger·대응·경제성 연결 |

### 2. 상태 Vocabulary

```yaml
market_evidence_status:
  ACTUAL_REPORTED:
    meaning: 종료된 기간의 실적 또는 설치·판매 통계
  CURRENT_COMPANY_GUIDANCE:
    meaning: 기업이 기준일 현재 제시한 계획·전망
  INSTITUTIONAL_FORECAST:
    meaning: IEA·정부기관 등의 전망
  COMPANY_CLAIM:
    meaning: 경쟁사가 발표한 제품·기술·시장지위
  ANALYTICAL_INFERENCE:
    meaning: 복수 공개자료를 연결해 도출한 분석
  NOT_DISCLOSED:
    meaning: 공개근거가 없어 수치화 금지
```

### 3. 비교 단위 통제

```text
EV Sales ≠ EV Battery Deployment ≠ Total Li-ion Deployment
Cell Production Capacity ≠ Cell Production ≠ Shipment ≠ Vehicle Installation
Global Share ≠ Non-China Share ≠ Regional Share
Revenue ≠ Battery-only Revenue ≠ Shipment Value
Reported Operating Profit ≠ Recurring Operating Profit
Pack Price ≠ Cell Price ≠ Material Cost
```

---
