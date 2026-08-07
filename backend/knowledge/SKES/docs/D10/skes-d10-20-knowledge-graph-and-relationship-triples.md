---
id: skes-d10-20-knowledge-graph-and-relationship-triples
title: Knowledge Graph and Relationship Triples
summary: 에너지 자산·계약과 LNG·BESS·재생에너지·수소 등 시장 간 영향 관계를 knowledge graph(노드·엣지·트리플)로 모델링하는 구조 및 검색 방법 정의.
tags: [d10, market, "xref:d06"]
keywords: [지식 그래프, 온톨로지, LNG, BESS, ERCOT, 재생에너지, 수소, CCS, 노드·엣지, 시맨틱]
related: []
priority: normal
domain: D10
section: 20
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 619
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 20. Knowledge Graph and Relationship Triples

## 20.1 Node Types

`Market`, `Segment`, `Metric`, `ForecastVersion`, `Signal`, `Scenario`, `Competitor`, `Substitute`, `Asset`, `Process`, `Product`, `Customer`, `Contract`, `Policy`, `PriceIndex`, `Risk`, `Evidence`, `O/ISeed`.

## 20.2 Edge Types

`PARTICIPATES_IN`, `COMPETES_WITH`, `SUBSTITUTES_FOR`, `AFFECTS`, `PRICES`, `CONSTRAINS`, `EXPOSES`, `TRIGGERS`, `SUPPLIES`, `OFFTAKES`, `OPERATES`, `FORECASTS`, `EVIDENCES`, `REQUIRES_DATA_FROM`, `HANDOFF_TO`.

## 20.3 Core Triples

```text
Hormuz_disruption --AFFECTS--> Global_LNG_supply
Global_LNG_price --PRICES--> EandS_generation_fuel
LNG_heat_cost --AFFECTS--> Korean_SMP
Renewable_growth --INCREASES_NEED_FOR--> Flexibility
Grid_queue --CONSTRAINS--> Renewable_COD
KCE_assets --PARTICIPATE_IN--> ERCOT_and_NYISO
ERCOT_BESS_growth --AFFECTS--> Merchant_spread
MarketCapture --OPTIMIZES--> BESS_bid
EverCharge_SmartPower --CONSTRAINS--> Site_peak_load
EV_stock --DRIVES--> Charging_sessions
Vehicle_delivery --PRECEDES--> Firm_H2_demand
Firm_emitter_contract --PRECEDES--> Bankable_CCS
ForecastVersion --MUST_NOT_OVERWRITE--> PriorForecastVersion
MarketSignal --HANDOFF_TO--> D11_PnL_and_D17_Seed
```

## 20.4 Retrieval Queries

1. 2026 LNG 공급충격이 E&S의 어느 계약·자산·KPI에 영향을 주는가.
2. IEA 전망과 actual을 섞지 않고 2026 LNG 수요를 보여줘.
3. 한국 SMP 하락이 연료비 때문인지 수요 때문인지 분해할 데이터는 무엇인가.
4. KCE 운영 MW와 개발 pipeline을 분리해서 보여줘.
5. ERCOT BESS 증가가 MarketCapture 수익성에 주는 위험은 무엇인가.
6. EverCharge의 경쟁단위를 port 수가 아니라 constrained kW로 비교해줘.
7. 수소 MOU 중 firm demand로 인정되는 gate는 무엇인가.
8. CCS 발표 pipeline에서 운영·FID·건설을 분리해줘.
9. PPA 고객부하와 재생자산 shape를 연결할 Seed는 무엇인가.
10. D10 P0 과제 중 D06 공정데이터를 가장 많이 사용하는 것은 무엇인가.

---
