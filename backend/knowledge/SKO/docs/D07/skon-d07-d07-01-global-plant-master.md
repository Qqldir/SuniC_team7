---
id: skon-d07-d07-01-global-plant-master
title: Global Plant Master
summary: "SK온의 국내외 배터리 생산 거점들의 위치, 지배구조, 설계용량, 현재 운영 상태를 정리한 표"
tags: [d07, footprint, schema, table]
keywords: [배터리 생산거점, 전 세계 공장, 생산용량, GWh, 운영상태, 법인 구조, 설계용량, 캐파, 배터리 생산 거점, 생산능력, 운영 현황, 지배구조, 한국·유럽·중국·미국, 증설 계획, 합작회사, 공시용량]
related: []
priority: normal
domain: D07
section: D07-01.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1552
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-01. Global Plant Master

## 01.1 Korea·Europe·China·United States

| Plant ID            | 국가·거점             | 법인·지배구조                            | 공시상 Capacity |         설계·계획 Capacity | 2026-08 상태                    | 연결 Capacity 처리  |
| ------------------- | ----------------- | ---------------------------------- | -----------: | ---------------------: | ----------------------------- | --------------- |
| PLANT-D07-KR-SEO    | 한국 서산             | SK온 단독                             |       4.7GWh | 7GWh 기존동·14GWh 증설계획 별도 | OPERATIONAL                   | 포함              |
| PLANT-D07-HU-KOM1   | 헝가리 코마롬 1         | SK On Hungary 100%                 |       7.5GWh |                 7.5GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-HU-KOM2   | 헝가리 코마롬 2         | SK Battery Manufacturing Kft. 100% |      10.3GWh |                약 10GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-HU-IVA    | 헝가리 이반차           | SK온 계열 100%                        |      20.0GWh |                  30GWh | PARTIAL_OPERATION·RAMPING     | 20GWh 포함        |
| PLANT-D07-CN-YAN1   | 중국 옌청 1           | SK On Jiangsu, Q1 기준 SK온 70%       |      10.0GWh |      SKOJ 1·2 합계 27GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-CN-YAN2   | 중국 옌청 2           | SK On Jiangsu, Q1 기준 SK온 70%       |      17.0GWh |      SKOJ 1·2 합계 27GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-CN-YAN3   | 중국 옌청 3           | SK On Yancheng 100%                |       2.8GWh |                  33GWh | PARTIAL_OPERATION·RAMPING     | 2.8GWh 포함       |
| PLANT-D07-US-GA1    | 미국 조지아 Commerce 1 | SK Battery America 100%            |      10.3GWh |                약 10GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-US-GA2    | 미국 조지아 Commerce 2 | SK Battery America 100%            |      11.7GWh |                약 12GWh | OPERATIONAL                   | 포함              |
| PLANT-D07-CN-CHA-JV | 중국 창저우            | Beijing BESK JV                    |       연결표 제외 |           과거 설계 7.5GWh | OPERATIONAL_JV                | 별도 관리           |
| PLANT-D07-CN-HUI-JV | 중국 후이저우           | EUE, SK온 49%                       |       연결표 제외 |            과거 설계 10GWh | DISPOSAL_PENDING              | 별도 관리           |
| PLANT-D07-US-HSBMA  | 미국 조지아 Bartow     | 현대차그룹·SK온 50:50                    |       연결표 제외 |                  35GWh | COMMERCIAL_PRODUCTION_STARTED | JV Gross로 별도 관리 |
| PLANT-D07-US-TN     | 미국 테네시 Stanton    | SK On Tennessee 단독                 |  현재 생산능력 미반영 |            과거 설계 45GWh | PREPARING_FOR_MASS_PRODUCTION | 현재 Capacity 제외  |
| PLANT-D07-US-KY1    | 미국 켄터키 1          | 2026-05 Ford 이전                    | Q1 당시 3.1GWh |           현재 SK온 기준 제외 | TRANSFERRED                   | 제외              |
| PLANT-D07-US-KY2    | 미국 켄터키 2          | 2026-05 Ford 이전                    |     상업생산 미반영 |           현재 SK온 기준 제외 | TRANSFERRED                   | 제외              |

1분기 공시상 환산 Capacity는 서산 4.7GWh, 코마롬 1·2가 각각 7.5·10.3GWh, 이반차 20GWh, 옌청 1·2·3이 10·17·2.8GWh, 조지아 1·2가 10.3·11.7GWh, 당시 BlueOval SK 켄터키 1이 3.1GWh였다. 이 합계가 97.4GWh다. ([KIND][1])

이반차는 전체 30GWh 설계능력 중 20GWh가 공시상 환산 생산능력에 반영됐다. SK온도 이반차 공장의 전체 연간 설계능력을 30GWh로 설명한다. ([SK On][7])

HSBMA의 35GWh는 2026년 6월 상업생산을 시작한 **JV 전체 Capacity**이고, 테네시는 2028년 생산개시가 예상되는 SK온 단독 거점이다. 켄터키 공장은 2026년 5월 Ford로 이전됐다. ([HSAGP ENERGY LLC][5])

---

## 01.2 Plant Master Schema

```yaml
plant_master_schema:

  plant_id: required
  canonical_name: required

  location:
    country: required
    state_or_province: required
    city_or_county: required
    coordinates: optional

  legal_structure:
    operating_entity: required
    ownership_type:
      - WHOLLY_OWNED
      - CONSOLIDATED_SUBSIDIARY
      - JOINT_VENTURE
      - EQUITY_METHOD_AFFILIATE
      - TRANSFERRED
    sk_on_ownership_percent: optional
    ownership_effective_date: required

  capacity_records:
    - capacity_value_gwh
    - capacity_type
    - reference_date
    - product_scope
    - ramp_ratio
    - inclusion_in_consolidated_capacity

  operating_status:
    status: required
    effective_date: required

  products:
    - EV
    - ESS
    - POUCH
    - LFP
    - NCM
    - CUSTOMER_SPECIFIC
    - UNRESOLVED

  customer_ids: []

  source_ids:
    required: true

  evidence_level:
    required: true

  confidence:
    - VERY_HIGH
    - HIGH
    - MEDIUM
    - LOW
```

---
