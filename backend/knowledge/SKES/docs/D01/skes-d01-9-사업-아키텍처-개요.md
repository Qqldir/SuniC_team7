---
id: skes-d01-9-사업-아키텍처-개요
title: 사업 아키텍처 개요
summary: "SK이노베이션의 사업 포트폴리오를 LNG·전력·수소·재생에너지 등 7개 사업군으로 구분하고 각각의 핵심 기능, 밸류체인 구조를 정의하는 사업 분류 표."
tags: [d01, identity, table, "xref:d07", "xref:d08", "xref:d02"]
keywords: [LNG, 액화, 터미널, 복합화력, 도시가스, 신재생에너지, 태양광, 수소에너지, ESS, 탄소포집, LNG 밸류체인, 가스자원, 액화·운송, 발전사업, 재생에너지, ESS·VPP, CCS, 에너지솔루션]
related: [BUS-ENS-01, BUS-ENS-02, BUS-ENS-03, BUS-ENS-04, BUS-ENS-05, BUS-ENS-06, BUS-ENS-07]
priority: normal
domain: D01
section: 9
source: SK이노베이션E&S_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 459
updated: 2026-08-06
---

> SK이노베이션 E&S · D01 기업 기본정보·법인구조·연혁

# 9. 사업 아키텍처 개요

## 9.1 LNG Value Chain

```text
Upstream Gas Resource
  → Liquefaction
  → LNG Shipping
  → Terminal / Storage / Regasification
  → Gas Power / CHP
  → City Gas / Industrial Customer
```

공식 사업소개는 미국 Woodford, 인도네시아 Tangguh, 호주 Barossa 등 가스자원과 Freeport·Darwin 액화설비, 전용 LNG선, 보령 LNG터미널, 국내 발전소를 하나의 밸류체인으로 제시한다. 각 자산의 소유권·지분·계약량은 D07·D08·D13에서 별도 검증한다. ([SRC-ENS-D01-0007])

## 9.2 Power Value Chain

```text
Fuel Procurement
  → Centralized Gas Power / CHP
  → Renewable Generation
  → Transmission / Distribution Interface
  → ESS / DERMS / VPP / EMS
  → Electricity, Heat and Energy Service Customer
```

## 9.3 공식 사업군

| Business ID | 사업군 | 핵심 기능 | D02 인계 |
|---|---|---|---|
| `BUS-ENS-01` | LNG Value Chain | 가스자원·액화·운송·터미널·발전 | Yes |
| `BUS-ENS-02` | City Gas | 지역 독점·허가 기반 도시가스 공급 | Yes |
| `BUS-ENS-03` | Power Generation | LNG 복합화력·CHP·열 공급 | Yes |
| `BUS-ENS-04` | Renewable Energy | 태양광·육상풍력·해상풍력 | Yes |
| `BUS-ENS-05` | Hydrogen Energy | 액화수소·블루수소·그린수소 | Yes |
| `BUS-ENS-06` | Energy Solution | ESS·VPP·DERMS·EMS·EV 충전 | Yes |
| `BUS-ENS-07` | CCS / Low-carbon LNG | 가스전 연계 탄소포집·운송·저장 | Yes |

---
