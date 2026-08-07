---
id: skon-d07-d07-26-logistics-customer-proximity
title: Logistics·Customer Proximity
summary: "SK온 배터리 공급거점의 OEM 고객 근접성 현황(Georgia, Tennessee, Mississippi)과 물류·계약 체계의 필수 요건을 요약한다."
tags: [d07, footprint, schema]
keywords: [고객근접성, 배터리 생산거점, 물류 레인, OEM 연계, 지역공급망, 공급능력, 물류 리스크, SKBA, HSBMA, 차량공장 인접, 배터리 공급망, OEM 고객, 생산거점, 지역공급, 물류 운영, 제품 인증, Georgia, Ford, 현대차, ESS]
related: []
priority: normal
domain: D07
section: D07-26.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 723
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-26. Logistics·Customer Proximity

## 26.1 Customer-Proximity Evidence

### SKBA Commerce

Georgia 주정부는 SKBA Commerce 생산 Battery가 Ford F-150 Lightning과 Volkswagen ID.4에 탑재된다고 2023년에 밝혔다. 이는 역사적으로 직접 확인되는 공장–차종 관계지만 2026년 현재 물량비중과 지속여부는 재검증 대상이다. ([켐프 주지사 사무실][14])

### HSBMA

HSBMA는 현대차그룹 미국 생산기지와의 인접성을 고려해 설립됐고, 2026년 초기 생산물량은 IONIQ 9을 지원한다. IONIQ 9의 미국 판매차량은 Georgia의 HMGMA에서 조립되므로 Cell–Vehicle 지역공급망 구축의 직접 사례다. ([SK][15])

### Tennessee

Tennessee Battery Plant는 BlueOval City 내부에 Ford 차량공장과 함께 설계됐으나, 2026년 JV 해소 이후 SK온의 독립법인이 됐다. 기존 물리적 인접성이 새로운 고객계약을 자동 보장하지는 않으며, 현재 고객·제품은 미확정이다. ([포드 회사 홈페이지][16])

### Nissan

Nissan은 2028년부터 Mississippi Canton에서 생산하는 차세대 EV에 미국산 SK온 Battery를 사용할 예정이지만, 공급공장은 공개되지 않았다. ([SK][8])

---

## 26.2 Logistics Entity Schema

```yaml
plant_customer_logistics_schema:

  logistics_lane_id: required

  origin:
    - Plant
    - Module or pack site
    - Warehouse

  destination:
    - Customer plant
    - Port
    - Distribution center
    - ESS project

  product:
    - Cell
    - Module
    - Pack
    - ESS block

  transport:
    - Road
    - Rail
    - Sea
    - Intermodal

  operational_data:
    - Distance
    - Transit time
    - Frequency
    - Packaging
    - Maximum inventory
    - Hazardous-goods requirement

  commercial_data:
    - Incoterm
    - Transport owner
    - Emergency freight
    - Tariff
    - Customs

  risk:
    - Single route
    - Border delay
    - Port disruption
    - Weather
    - Customer schedule volatility
```

---

## 26.3 Customer-Proximity Is Not Sufficient

```text
Geographic Proximity
        ↓
Lower Potential Transit Time
        ↓
But Requires:
Product Qualification
+ Contract Allocation
+ Material Compliance
+ Available Good Output
+ Module·Pack Compatibility
        ↓
Effective Customer-Linked Capacity
```

---
