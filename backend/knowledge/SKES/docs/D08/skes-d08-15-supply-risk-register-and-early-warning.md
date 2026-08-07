---
id: skes-d08-15-supply-risk-register-and-early-warning
title: Supply-Risk Register and Early Warning
summary: LNG·수소·재생에너지 공급망의 26개 리스크를 점수 기반으로 분류하고 조기신호와 영향을 관리하는 리스크 레지스터 및 평가 매트릭스
tags: [d08, supply-chain, table]
keywords: [리스크 점수 모델, 조기신호, LNG 공급, 공급망 중단, 조달 리스크, 영향도 분석, 발생가능성, 우선순위, 물류 리스크, 모니터링]
related: [RSK-ENS-D08-0001, RSK-ENS-D08-0002, RSK-ENS-D08-0003, RSK-ENS-D08-0004, RSK-ENS-D08-0005, RSK-ENS-D08-0006, RSK-ENS-D08-0007, RSK-ENS-D08-0008, RSK-ENS-D08-0009, RSK-ENS-D08-0010, RSK-ENS-D08-0011, RSK-ENS-D08-0012, RSK-ENS-D08-0013, RSK-ENS-D08-0014, RSK-ENS-D08-0015, RSK-ENS-D08-0016, RSK-ENS-D08-0017, RSK-ENS-D08-0018, RSK-ENS-D08-0019, RSK-ENS-D08-0020, RSK-ENS-D08-0021, RSK-ENS-D08-0022, RSK-ENS-D08-0023, RSK-ENS-D08-0024]
priority: normal
domain: D08
section: 15
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1176
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 15. Supply-Risk Register and Early Warning

## 15.1 Risk-Scoring Model

`Risk Score = Likelihood × Impact × Exposure × (1-Control Effectiveness) × Data-Uncertainty Multiplier`

- Likelihood: 1~5.
- Impact: 안전·생산·재무·환경·평판 중 최대/가중값.
- Exposure: single source, lead time, inventory cover, switching cost.
- Control effectiveness: BCP·dual source·stock·insurance·contract protection.
- Data uncertainty multiplier: 공개자료만으로 판단할수록 상향.

## 15.2 Risk Master

| Risk ID | 위험 | 노출 영역 | 조기신호 | 영향 | 우선 |
|---|---|---|---|---|---|
| `RSK-ENS-D08-0001` | upstream production shortfall | Barossa/Woodford/Tangguh | production·maintenance | cargo 부족 | P0 |
| `RSK-ENS-D08-0002` | liquefaction outage | Freeport/Darwin | outage notice·weather | use-or-pay·공급 | P0 |
| `RSK-ENS-D08-0003` | feed-gas basis spike | U.S. route | basis·pipeline constraint | 원가 | P0 |
| `RSK-ENS-D08-0004` | vessel delay | LNG fleet | ETA·weather·canal | 재고·demurrage | P0 |
| `RSK-ENS-D08-0005` | terminal congestion | Boryeong | berth/tank/sendout | 하역불가 | P0 |
| `RSK-ENS-D08-0006` | LNG quality deviation | cargo/power | CoA·lab·Wobbe | 효율·분쟁 | P0 |
| `RSK-ENS-D08-0007` | inventory stockout | power/CHP | cover days | 발전중단 | P0 |
| `RSK-ENS-D08-0008` | contract under-utilization | Freeport/TUA | utilization | fixed-fee leakage | P0 |
| `RSK-ENS-D08-0009` | FX/price volatility | LNG/parts | FX·JKM·HH | 원가·현금 | P0 |
| `RSK-ENS-D08-0010` | sanctions/geopolitics | global LNG | regulation/news | route/counterparty | P0 |
| `RSK-ENS-D08-0011` | critical spare shortage | power/LNG | lead time·stock | outage 연장 | P0 |
| `RSK-ENS-D08-0012` | counterfeit/wrong revision | MRO | inspection/BOM mismatch | 안전·고장 | P0 |
| `RSK-ENS-D08-0013` | pipe/valve lot defect | city gas | NCR/leak | safety/recall | P0 |
| `RSK-ENS-D08-0014` | contractor safety failure | all sites | near miss·training | injury·shutdown | P0 |
| `RSK-ENS-D08-0015` | offshore package delay | wind | milestone·vessel | COD 지연 | P0 |
| `RSK-ENS-D08-0016` | cable damage | offshore wind | test/installation | long outage | P0 |
| `RSK-ENS-D08-0017` | BESS cell defect/recall | KCE | bulletin·temperature | fire·availability | P0 |
| `RSK-ENS-D08-0018` | BESS OEM insolvency | KCE | liquidity/rating | warranty loss | P0 |
| `RSK-ENS-D08-0019` | tariff/origin restriction | BESS/solar | policy | CAPEX·delay | P0 |
| `RSK-ENS-D08-0020` | firmware vulnerability | BESS/EVSE | CVE/SBOM | cyber/operation | P0 |
| `RSK-ENS-D08-0021` | obsolescence | EVSE/control | EOL notice | spares/service | P1 |
| `RSK-ENS-D08-0022` | LH₂ feed interruption | Incheon | source rate | production loss | P0 |
| `RSK-ENS-D08-0023` | cryogenic spare delay | LH₂ | lead time/condition | train outage | P0 |
| `RSK-ENS-D08-0024` | trailer/route disruption | LH₂ | ETA/traffic | station stockout | P0 |
| `RSK-ENS-D08-0025` | CCS technology performance | pilot | capture/energy | economics | P1 |
| `RSK-ENS-D08-0026` | MRV evidence gap | CCS | missing calibration | credit/claim | P0 |
| `RSK-ENS-D08-0027` | supplier ESG violation | common | audit/grievance | legal/reputation | P0 |
| `RSK-ENS-D08-0028` | supplier financial distress | common | payment/rating | delivery | P1 |
| `RSK-ENS-D08-0029` | sub-tier opacity | all equipment | BOM/origin gap | recall/compliance | P0 |
| `RSK-ENS-D08-0030` | data-right restriction | JV/OEM | contract clause | AI PoC block | P0 |
| `RSK-ENS-D08-0031` | master-data duplication | enterprise | duplicate vendor/material | spend/error | P1 |
| `RSK-ENS-D08-0032` | green claim misallocation | low-carbon LNG/renewable | CoC gap | compliance/reputation | P0 |

## 15.3 Alert Levels

| Level | 의미 | 대응 |
|---|---|---|
| Green | 정상 | standard monitoring |
| Yellow | 지표 악화·buffer 감소 | buyer/operations review |
| Orange | SLA 위반 가능·대체 필요 | control tower·BCP activation |
| Red | 공급중단·안전·법규 영향 현실화 | crisis governance·executive decision |

---
