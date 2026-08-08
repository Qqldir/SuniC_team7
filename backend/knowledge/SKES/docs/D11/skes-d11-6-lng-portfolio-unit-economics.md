---
id: skes-d11-6-lng-portfolio-unit-economics
title: LNG Portfolio Unit Economics
summary: "LNG 카고의 구매부터 판매까지 전 과정의 수익성 계산 체계와 12개 핵심 원가 드라이버, 8개 성과 지표를 정의한 경제성 분석 프레임워크."
tags: [d11, cost, table]
keywords: [LNG 카고, 원가 드라이버, 수익 마진, 액화비용, 운송비, 항구 사용료, BOG 손실, 헤징, Use-or-pay, 목적지 선택가치]
related: [CST-ENS-D11-001, CST-ENS-D11-002, CST-ENS-D11-003, CST-ENS-D11-004, CST-ENS-D11-005, CST-ENS-D11-006, CST-ENS-D11-007, CST-ENS-D11-008, CST-ENS-D11-009, CST-ENS-D11-010, CST-ENS-D11-011, CST-ENS-D11-012, KPI-ENS-D11-001, KPI-ENS-D11-002, KPI-ENS-D11-003, KPI-ENS-D11-004, KPI-ENS-D11-005, KPI-ENS-D11-006, KPI-ENS-D11-007, KPI-ENS-D11-008]
priority: normal
domain: D11
section: 6
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1007
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 6. LNG Portfolio Unit Economics

## 6.1 Value Waterfall

```text
Equity gas / long-term LNG / spot procurement
→ production and gathering
→ liquefaction or tolling right
→ vessel and voyage
→ terminal slot / storage / BOG / regasification
→ power plant / city gas / trading destination
→ external sale and cash settlement
```

## 6.2 Cargo Economics Formula

```text
Cargo realized margin
= destination sale value or downstream avoided procurement cost
− upstream gas purchase or production cost
− liquefaction toll and fuel retention
− shipping charter, bunker, canal, insurance and demurrage
− terminal use, storage, BOG and regasification cost
− customs, tax, carbon and methane-related cost
− FX and hedge settlement
− quality adjustment and imbalance
− fixed take-or-pay/use-or-pay allocation
```

## 6.3 LNG Cost Driver Record

| ID | Driver | 최소 입력 | 손익 전파 | 의사결정 |
|---|---|---|---|---|
| `CST-ENS-D11-001` | Feed-gas price | index·basis·volume·FX | 구매원가 | Nomination·Hedge |
| `CST-ENS-D11-002` | Equity production cost | field OPEX·share·yield | Upstream Margin | 생산·정비 |
| `CST-ENS-D11-003` | Liquefaction toll | fixed/variable fee·fuel | Landed Cost | Slot utilization |
| `CST-ENS-D11-004` | Use-or-pay obligation | reserved capacity·used capacity | 고정비 미흡수 | Third-party use·schedule |
| `CST-ENS-D11-005` | Vessel cost | charter·bunker·speed | 운송원가 | Vessel/route |
| `CST-ENS-D11-006` | Demurrage | laytime·delay | Cargo Margin 누수 | ETA·Berth |
| `CST-ENS-D11-007` | Terminal slot | slot·storage·regas fee | Delivered Cost | Cargo sequencing |
| `CST-ENS-D11-008` | BOG loss | tank level·pressure·recovery | 물량·에너지 손실 | Recondense/send-out |
| `CST-ENS-D11-009` | Inventory timing | receipt·issue·valuation | 회계·현금 변동 | Inventory policy |
| `CST-ENS-D11-010` | Destination optionality | diversion clause·price spreads | Trading Upside | Cargo allocation |
| `CST-ENS-D11-011` | Quality adjustment | HHV·impurity·spec | Price/processing | Blend·acceptance |
| `CST-ENS-D11-012` | Commodity/FX hedge | exposure·instrument·settlement | Margin-at-Risk | Hedge ratio |

## 6.4 LNG KPI

| KPI ID | KPI | 분모·단위 | 목적 |
|---|---|---|---|
| `KPI-ENS-D11-001` | Landed LNG Cost | KRW/MMBtu by cargo | 공급경로 비교 |
| `KPI-ENS-D11-002` | Portfolio Margin | KRW/MMBtu delivered | 계약·Cargo 수익성 |
| `KPI-ENS-D11-003` | Use-or-pay Utilization | used/reserved capacity | 권리 미활용 비용 |
| `KPI-ENS-D11-004` | BOG Economic Loss | KRW and % send-out | 탱크 운영 개선 |
| `KPI-ENS-D11-005` | Demurrage Cost | KRW/cargo | 입항·하역 병목 |
| `KPI-ENS-D11-006` | Diversion Option Value | KRW/cargo | 목적지 선택가치 |
| `KPI-ENS-D11-007` | Hedge Effectiveness | offset/exposure | 가격·환율 방어 |
| `KPI-ENS-D11-008` | Inventory Cash Days | days and KRW | 운전자본 |

## 6.5 LNG Internal Data Gate

- 계약별 가격공식·Slope·Lag·Ceiling/Floor·Take-or-pay·Destination 조항
- Equity gas 생산량·현금원가·Royalty·Tax·지분율
- Cargo별 FOB/DES, Vessel, ETA, Laytime, Bunker, Demurrage
- Freeport 액화 사용권과 보령터미널 사용권의 예약·실사용·제3자 활용
- 탱크 재고·BOG·기화·송출·품질·Blend 이력
- 발전·도시가스·Trading 목적지별 Transfer Price와 연결제거
- Commodity·FX Hedge 대상·수단·정산·담보

---
