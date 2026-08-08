---
id: skes-d10-3-canonical-data-model
title: Canonical Data Model
summary: 에너지 시장의 수요·신호·경쟁·시나리오 정보를 표준화된 구조로 저장·관리하기 위한 데이터 스키마 명세서.
tags: [d10, market, schema, "xref:d11", "xref:d12", "xref:d15"]
keywords: [Market Record, Market Signal, Competitor Record, Scenario Record, LNG, POWER, 신호 추적, 스키마, 경쟁사 분석, 시나리오]
related: []
priority: normal
domain: D10
section: 3
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 571
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 3. Canonical Data Model

## 3.1 Market Record

```yaml
market_id: MKT-ENS-D10-0001
name: Global LNG
geography: GLOBAL | KOREA | ASIA | ERCOT | NYISO | SITE
segment: LNG | POWER | CITY_GAS | RENEWABLE | PPA | BESS | EV_CHARGING | HYDROGEN | CCS
metric_name: demand
metric_value: 0
unit: bcm | mtpa | MW | MWh | KRW_per_kWh | USD_per_MMBtu | port | kg | tCO2
period: YYYY | YYYY-MM | timestamp
claim_status: ACTUAL_FINAL | ACTUAL_PRELIMINARY | FORECAST_BASE | FORECAST_SCENARIO
scope_definition: explicit
source_ids: []
affected_assets: []
affected_contracts: []
confidence: high | medium | low
refresh_date: YYYY-MM-DD
```

## 3.2 Market Signal

```yaml
signal_id: SIG-ENS-D10-0001
event_date: YYYY-MM-DD
signal_type: PRICE | DEMAND | SUPPLY | POLICY | COMPETITOR | TECHNOLOGY | PROJECT | RISK
market_id: MKT-ENS-D10-0001
direction: UP | DOWN | VOLATILITY | MIX_SHIFT | DELAY | ACCELERATION
facts: []
transmission_path: source_to_asset_to_KPI
time_horizon: immediate | 3m | 12m | 3y | 10y
decision_owner: trading | generation | city_gas | renewable | KCE | EverCharge | H2 | CCS
required_internal_data: []
recommended_action: monitor | hedge | rebid | reallocate | partner | stop | invest
human_approval: required
```

## 3.3 Competitor Record

```yaml
competitor_id: COM-ENS-D10-0001
name: competitor_or_substitute
archetype: integrated_energy | utility | trader | developer | optimizer | OEM | platform
markets: []
geographies: []
competitive_unit: cargo | generation_MWh | PPA | MW_MWh | port_session | kg_H2 | tCO2
public_move: text
claim_status: COMPANY_CLAIM | OPERATING | PIPELINE_ANNOUNCED
strengths: []
limits: []
EandS_overlap: direct | adjacent | partner_competitor | substitute
source_ids: []
```

## 3.4 Scenario Record

```yaml
scenario_id: SCN-ENS-D10-0001
name: LNG_TIGHT_HIGH_PRICE
trigger_set: []
probability: NOT_PUBLIC_INTERNAL_ESTIMATE
horizon: 2026H2 | 2027 | 2030
market_variables: []
affected_assets: []
affected_contracts: []
financial_bridge: D11
capex_bridge: D12
risk_bridge: D15
leading_indicators: []
decision_gates: []
```

---
