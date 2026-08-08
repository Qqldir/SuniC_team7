---
id: skon-d07-d07-rp-001-manufacturing-footprint-research-pac
title: 001. Manufacturing Footprint Research Pack
summary: "SK온의 글로벌 생산거점 위치, 설계 용량, 실제 가동 현황을 규제 공시와 공식 자료로 정리한 종합 연구 팩"
tags: [d07, footprint, schema]
keywords: [생산거점, 생산용량, BlueOval SK, HSBMA, SK온 미국, 설계용량, 켄터키, 테네시, 배터리 공장, SK온, 배터리 용량, GWh, 설계 용량, 공시]
related: []
priority: normal
domain: D07
section: D07-RP
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1560
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-RP-001. Manufacturing Footprint Research Pack

## SRC-REG-D07-001 — 2026년 1분기 분기보고서

```yaml
source_id: SRC-REG-D07-001
title: SK Innovation 2026 First-Quarter Report
publisher: Korea Exchange / SK Innovation
publication_date: 2026-05-15
source_type: Regulatory Quarterly Report
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY
confidence: VERY_HIGH

covered_scope:
  - Consolidated production capacity
  - Plant-by-plant normalized capacity
  - Partial-operation ratios
  - Production volume
  - Average utilization
  - Consolidated and non-consolidated site boundary
  - Subsidiary ownership
```

이 자료를 D07의 최신 **연결 Capacity 기준점**으로 사용한다. 다만 보고서 기준일 이후인 5~7월에 미국 JV 해소와 HSBMA 가동개시가 발생했기 때문에 현재 구조와 완전히 같지는 않다. ([KIND][1])

---

## SRC-OFF-D07-002 — 2025년 4분기 생산거점 계획표

```yaml
source_id: SRC-OFF-D07-002
title: SK Innovation 2025 Fourth-Quarter Earnings Release
publication_date: 2026-01-28
source_type: Official Investor Presentation
source_grade: A
evidence_level: DIRECT_OFFICIAL
temporal_status: HISTORICAL_PLAN_AND_DESIGN_CAPACITY

covered_scope:
  - Design maximum capacity
  - Planned commercial-production dates
  - Korea, Europe, United States and China footprint
```

해당 IR 자료는 서산 7GWh, 이반차 30GWh, 테네시 45GWh 등 **설계·계획 기준 Capacity**를 제시한다. 1분기 공시의 환산 생산능력과 산정기준이 다르므로 별도 필드로 보존한다. ([파일SCS][2])

---

## SRC-REG-D07-003 — BlueOval SK 자산 이전

```yaml
source_id: SRC-REG-D07-003
title: Ford 8-K — BlueOval SK Joint Venture Disposition Closing
publisher: U.S. Securities and Exchange Commission
publication_date: 2026-05-20
source_type: Regulatory Filing
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY
confidence: VERY_HIGH

confirmed:
  - BlueOval SK restructuring closed on 2026-05-20
  - Ford interest in BlueOval SK was redeemed
  - Ford subsidiary acquired the two Kentucky battery plants
  - BlueOval SK retained the Tennessee plant
  - BlueOval SK became controlled by SK Battery America
```

2026년 5월 20일 거래종결 후 켄터키의 두 공장은 Ford 측으로 이전됐다. 따라서 켄터키 공장은 2026년 8월 기준 SK온 현재 생산거점으로 계산하지 않는다. ([SEC][3])

---

## SRC-OFF-D07-004 — SK On Tennessee

```yaml
source_id: SRC-OFF-D07-004
title: SK On Tennessee Becomes Newest SK On U.S. Company
publisher: SK
publication_date: 2026-05-21
source_type: Official Corporate Release
source_grade: A
evidence_level: DIRECT_OFFICIAL
confidence: VERY_HIGH

confirmed:
  - Tennessee facility became a standalone SK On company
  - Former BlueOval SK Tennessee facility
  - Operational systems and workforce preparation continue
  - Mass production projected to begin in 2028

not_confirmed:
  - Current battery output
  - Customer allocation
  - Final product chemistry
  - Utilized production capacity
```

테네시 거점은 현재 SK온 단독 생산기지로 편입됐지만, 공식자료는 대량생산 시작 시점을 2028년으로 제시한다. 따라서 45GWh 설계 Capacity를 현재 가동 Capacity로 계산하지 않는다. ([SK][4])

---

## SRC-OFF-D07-005 — HSBMA 상업생산

```yaml
source_id: SRC-OFF-D07-005
title: HSBMA Begins EV Battery Cell Production in Georgia
publisher: HSBMA
publication_date: 2026-07-17
source_type: Official Joint-Venture Release
source_grade: A
evidence_level: DIRECT_OFFICIAL
confidence: VERY_HIGH

confirmed:
  - Commercial production began on 2026-06-01
  - Plant is located in Bartow County, Georgia
  - Gross annual design capacity is 35 GWh
  - Hyundai Motor Group and SK On each own 50 percent
  - Initial cells support Hyundai IONIQ 9 production

capacity_class:
  value_gwh: 35
  type: JV_GROSS_DESIGN_CAPACITY
  consolidated_in_sk_on_capacity: false
```

HSBMA는 2026년 6월 1일 상업생산을 시작했다고 공식 발표했다. 연간 설계능력은 35GWh지만 50:50 합작법인이므로 35GWh 전체를 SK온 연결 Capacity에 더해서는 안 된다. ([HSAGP ENERGY LLC][5])

---

## SRC-REG-D07-006 — 중국 EVE 지분 Swap

```yaml
source_id: SRC-REG-D07-006
title: Decision on Disposal and Acquisition of Chinese JV Shares
publisher: Korea Exchange / Financial Supervisory Service
latest_correction_date: 2026-06-22
source_type: Regulatory Filing
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

transaction:
  disposal:
    company: Huizhou EVE United Energy
    sk_on_stake: 49_percent

  acquisition:
    company: SK On Jiangsu
    eve_stake: 30_percent

  additional_consideration:
    payer: EVE
    amount: CNY_200_million

scheduled_completion:
  date: 2026-09-09

status_as_of_2026_08_02:
  - DISPOSAL_PENDING
  - ACQUISITION_PENDING
```

2026년 6월 정정공시는 후이저우 JV 지분 49%와 EVE가 보유한 SK On Jiangsu 지분 30%를 교환하는 구조를 재확인하고 거래 예정일을 2026년 9월 9일로 제시했다. 따라서 8월 2일 기준으로는 완료된 소유구조로 선반영하지 않는다. ([KIND][6])

---
