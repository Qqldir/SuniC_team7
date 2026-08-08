---
id: skes-d03-part-3-application-customer-alternative-6
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Product Relationship Graph
summary: "SK이노베이션 E&S의 제품·자산·고객 관계를 그래프 데이터로 모델링하기 위한 노드 클래스, 엣지 타입 정의 및 LNG·전력·도시가스·PPA 사업별 관계 구조 예시를 제시하는 문서."
tags: [d03, product, table, "xref:d04", "xref:d17"]
keywords: [그래프 모델, LNG, 도시가스, PPA, 노드 클래스, 엣지, SCADA, BOG, 자산 구조, 데이터 모델링]
related: []
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 1229
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 25. Product Relationship Graph

### 25.1 Node Classes

| Node Class | 예시 | Canonical prefix |
|---|---|---|
| Organization | E&S CIC, KCE, EverCharge, 도시가스 자회사 | `ORG-ENS-*` |
| Product/Solution | LNG terminal, direct PPA, liquid hydrogen | `PS-ENS-*` |
| Application | BOG optimization, PPA settlement | `APP-ENS-*` |
| Asset | vessel, tank, turbine, pipeline, electrolyzer | `AST-ENS-*` |
| Customer | RE100 기업, 가정, fleet | `CUST-ENS-*` |
| Data | SCADA, meter, contract, weather | `DATA-ENS-*` |
| KPI | heat rate, forecast error, MTTR | `KPI-ENS-*` |
| Pain Point | fragmented schedule, false alarm | `PAIN-ENS-*` |
| O/I Seed | 통합최적화·예지보전·MRV | `SEED-ENS-D03-*` |
| Source | 공식 사업페이지·자회사 발표 | `SRC-ENS-D03-*` |

### 25.2 Edge Types

| Edge | From → To | 필수 속성 |
|---|---|---|
| `OWNS_OR_CONTROLS` | ORG → AST/ORG | scope, effective_date, source |
| `PROVIDES` | ORG → PS | geography, status, source |
| `USES_ASSET` | PS → AST | criticality, status |
| `SERVES` | PS → CUST | contract/status, source |
| `APPLIED_TO` | PS → APP | maturity |
| `REQUIRES_DATA` | APP → DATA | frequency, owner, sensitivity |
| `IMPROVES` | APP → KPI | baseline, target, confidence |
| `ADDRESSES` | APP/SEED → PAIN | hypothesis_status |
| `EVIDENCED_BY` | node/edge → SRC | quote/section, as_of |
| `HANDOVER_TO` | SEED → D04~D17 | target_domain |

### 25.3 Core LNG Graph

```text
ORG-SKI-ENS-CIC-000001
  PROVIDES -> PS-ENS-LNG-01
  PROVIDES -> PS-ENS-LNG-03
  PROVIDES -> PS-ENS-LNG-04
PS-ENS-LNG-01 USES_ASSET -> AST-ENS-GAS-FIELD
PS-ENS-LNG-01 USES_ASSET -> AST-ENS-LIQUEFACTION-RIGHT
PS-ENS-LNG-03 USES_ASSET -> AST-ENS-LNG-CARRIER-FLEET
PS-ENS-LNG-04 USES_ASSET -> AST-ENS-LNG-TERMINAL
PS-ENS-LNG-03 APPLIED_TO -> APP-ENS-002
PS-ENS-LNG-04 APPLIED_TO -> APP-ENS-003
APP-ENS-002 REQUIRES_DATA -> DATA-ENS-AIS-WEATHER
APP-ENS-002 REQUIRES_DATA -> DATA-ENS-TERMINAL-INVENTORY
APP-ENS-003 IMPROVES -> KPI-ENS-BOG-LOSS
```

### 25.4 LNG-to-Power Graph

```text
PS-ENS-LNG-04 ENABLES -> PS-ENS-PWR-01
PS-ENS-LNG-04 ENABLES -> PS-ENS-PWR-02
PS-ENS-PWR-01 APPLIED_TO -> APP-ENS-004
PS-ENS-PWR-02 APPLIED_TO -> APP-ENS-005
APP-ENS-004 REQUIRES_DATA -> DATA-ENS-MARKET-FUEL
APP-ENS-004 REQUIRES_DATA -> DATA-ENS-PLANT-HISTORIAN
APP-ENS-005 REQUIRES_DATA -> DATA-ENS-HEAT-DEMAND
```

### 25.5 City Gas Graph

```text
ORG-SKI-ENS-CIC-000001 OWNS_OR_CONTROLS -> ORG-ENS-CG-KOONE
ORG-SKI-ENS-CIC-000001 OWNS_OR_CONTROLS -> ORG-ENS-CG-BUSAN
ORG-ENS-CG-* PROVIDES -> PS-ENS-CG-01
ORG-ENS-CG-* PROVIDES -> PS-ENS-CG-02
ORG-ENS-CG-* OPERATES -> PS-ENS-CG-03
PS-ENS-CG-02 APPLIED_TO -> APP-ENS-009
PS-ENS-CG-02 APPLIED_TO -> APP-ENS-010
PS-ENS-CG-03 APPLIED_TO -> APP-ENS-007
PS-ENS-CG-03 APPLIED_TO -> APP-ENS-008
```

### 25.6 PPA Graph

```text
ORG-SKI-ENS-CIC-000001 PROVIDES -> PS-ENS-REN-03
PS-ENS-REN-03 SERVES -> CUST-ENS-PPA-AMORE
PS-ENS-REN-03 SERVES -> CUST-ENS-PPA-BASF
PS-ENS-REN-03 APPLIED_TO -> APP-ENS-013
PS-ENS-REN-05 APPLIED_TO -> APP-ENS-014
APP-ENS-013 REQUIRES_DATA -> DATA-ENS-CUSTOMER-LOAD
APP-ENS-013 REQUIRES_DATA -> DATA-ENS-RE-ASSET-PIPELINE
APP-ENS-014 REQUIRES_DATA -> DATA-ENS-METER-CONTRACT-CERTIFICATE
```

### 25.7 Hydrogen Graph

```text
ORG-ENS-SKIPC SUPPLIES_FEED -> PS-ENS-H2-01
PS-ENS-H2-01 USES_ASSET -> AST-ENS-INCHEON-LH2-PLANT
PS-ENS-H2-01 ENABLES -> PS-ENS-H2-02
PS-ENS-H2-02 ENABLES -> PS-ENS-H2-03
PS-ENS-H2-01 APPLIED_TO -> APP-ENS-015
PS-ENS-H2-02 APPLIED_TO -> APP-ENS-016
PS-ENS-H2-03 APPLIED_TO -> APP-ENS-016
```

### 25.8 North America Energy Solution Graph

```text
ORG-SKI-ENS-CIC-000001 OWNS_OR_CONTROLS -> ORG-ENS-PASSKEY
ORG-ENS-PASSKEY PORTFOLIO_LINK -> ORG-ENS-KCE
ORG-ENS-PASSKEY PORTFOLIO_LINK -> ORG-ENS-EVERCHARGE
ORG-ENS-KCE PROVIDES -> PS-ENS-ES-03
ORG-ENS-KCE PROVIDES -> PS-ENS-MARKETCAPTURE
ORG-ENS-EVERCHARGE PROVIDES -> PS-ENS-ES-07B
ORG-ENS-EVERCHARGE CO_DEVELOPS -> PS-ENS-ES-08
PS-ENS-ES-03 APPLIED_TO -> APP-ENS-019
PS-ENS-ES-07B APPLIED_TO -> APP-ENS-023
PS-ENS-ES-08 APPLIED_TO -> APP-ENS-024
```

### 25.9 CCS Graph

```text
PS-ENS-LNG-01 FEEDS -> PS-ENS-CCS-01
PS-ENS-CCS-02 ENABLES -> PS-ENS-CCS-01
PS-ENS-CCS-01 APPLIED_TO -> APP-ENS-025
PS-ENS-CCS-02 APPLIED_TO -> APP-ENS-025
APP-ENS-025 REQUIRES_DATA -> DATA-ENS-CO2-METER
APP-ENS-025 REQUIRES_DATA -> DATA-ENS-CUSTODY-TRANSFER
APP-ENS-025 REQUIRES_DATA -> DATA-ENS-RESERVOIR-MONITORING
```

---
