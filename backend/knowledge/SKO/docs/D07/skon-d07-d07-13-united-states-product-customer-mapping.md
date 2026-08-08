---
id: skon-d07-d07-13-united-states-product-customer-mapping
title: United States Product·Customer Mapping
summary: "SK온의 미국 생산공장(조지아, 테네시)에서 EV·ESS 배터리를 생산할 때 어떤 자동차 제조사와 차종에 공급하는지 보여주는 현황 및 계획."
tags: [d07, footprint, schema, table]
keywords: [SK Battery America, HSBMA, F-150 Lightning, IONIQ 9, 배터리 생산능력, 미국 EV 거점, OEM 공급처, 현대자동차, 생산 매핑, GWh 설비용량, SK온 미국, 배터리 고객사, Commerce Georgia, EV 배터리, 생산거점 매핑]
related: []
priority: normal
domain: D07
section: D07-13.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1850
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-13. United States Product·Customer Mapping

## 13.1 SK Battery America — Commerce, Georgia

조지아 주정부는 SK Battery America의 Commerce 공장이 Ford F-150 Lightning과 Volkswagen ID.4용 배터리를 생산한다고 2023년 공식 발표했다. 두 공장의 합산 생산능력은 약 22GWh로 제시됐다. 다만 이는 **공장–차종의 역사적 직접 근거**이며, 2026년 현재 동일 물량구성이 유지된다고 자동 연장하지 않는다. ([켐프 주지사 사무실][3])

```yaml
plant_id: PLANT-D07-US-GA1_GA2
canonical_name: SK Battery America Commerce Complex

confirmed_historical_mapping:

  Ford_F150_Lightning:
    mapping_level: DIRECT_SITE_MODEL
    product_scope:
      - EV battery cell
    status: DIRECT_HISTORICAL_PRODUCTION

  Volkswagen_ID4:
    mapping_level: DIRECT_SITE_MODEL
    product_scope:
      - EV battery cell
    status: DIRECT_HISTORICAL_PRODUCTION

capacity:
  combined_design_capacity_gwh: approximately_22

current_2026_mapping:
  Ford_F150_Lightning: REVALIDATION_REQUIRED
  Volkswagen_ID4: REVALIDATION_REQUIRED
  New_EV_customers: UNRESOLVED
  ESS_allocation: SITE_NOT_PUBLICLY_SPECIFIED

chemistry:
  plant_level_current_mapping: UNRESOLVED

line_allocation:
  Georgia_1_vs_Georgia_2: UNRESOLVED

source_ids:
  - SRC-GOV-D07-008
```

### 핵심 통제

`F-150 Lightning 생산 이력`을 `2026년 현재 전용 Line`으로 표현하지 않는다. 또한 ID.4 공급근거도 어느 Building 또는 Line이 담당했는지는 공개자료에서 확인되지 않는다.

---

## 13.2 HSBMA — Bartow County, Georgia

HSBMA는 SK온과 현대차그룹의 50:50 합작공장이다. 공식 HSBMA 자료는 생산 Cell이 Hyundai·Kia·Genesis 전기차용이라고 설명한다. 2026년 7월 발표에서는 상업생산 개시와 함께 첫 생산 Cell이 Hyundai IONIQ 9 생산을 지원한다고 밝혔다. ([HSAGP ENERGY LLC][4])

```yaml
plant_id: PLANT-D07-US-HSBMA
canonical_name: Hyundai SK Battery Manufacturing America

ownership:
  SK_On: 50_percent
  Hyundai_Motor_Group: 50_percent

capacity:
  gross_design_capacity_gwh: 35
  capacity_type: JV_GROSS_DESIGN_CAPACITY

operating_status:
  - COMMERCIAL_PRODUCTION_STARTED
  - RAMPING

customer_mapping:

  Hyundai_Motor:
    mapping_level: DIRECT_SITE_OEM
    status: CURRENT_CONFIRMED

  Kia:
    mapping_level: DIRECT_SITE_OEM
    status: CURRENT_CONFIRMED

  Genesis:
    mapping_level: DIRECT_SITE_OEM
    status: CURRENT_CONFIRMED

vehicle_mapping:

  Hyundai_IONIQ_9:
    mapping_level: DIRECT_SITE_MODEL
    status: INITIAL_PRODUCTION_CONFIRMED

  Other_Hyundai_Kia_Genesis_models:
    mapping_level: OEM_SCOPE_ONLY
    status: SPECIFIC_MODEL_ALLOCATION_UNRESOLVED

product_scope:
  - EV battery cell

chemistry:
  current_public_mapping: UNRESOLVED

line_level_capacity:
  status: NOT_DISCLOSED
```

HSBMA는 현대차그룹 미국 생산거점과 가까운 고객연계형 공장이며, 초기 생산부터 IONIQ 9과 직접 연결된다. 그러나 35GWh 전체가 이미 고객승인을 마치고 정상가동한다는 뜻은 아니다. 기존 공식 계획은 이 공장이 현대·기아·제네시스 미국 생산 EV를 지원하도록 설계됐다고 설명한다. ([SK][5])

---

## 13.3 SK On Tennessee

SK On Tennessee는 2026년 BlueOval SK 구조에서 분리돼 SK온 단독법인으로 전환됐다. 공식자료는 EV와 ESS 시장 변화에 대응할 전략적 유연성을 언급하지만, 상업생산은 2028년 시작을 전망한다. ([SK][6])

```yaml
plant_id: PLANT-D07-US-TN
canonical_name: SK On Tennessee

ownership:
  type: WHOLLY_CONTROLLED_BY_SK_ON
  effective_year: 2026

operating_status:
  - PREPARING_FOR_MASS_PRODUCTION
  - PRE_SOP

official_positioning:
  potential_markets:
    - EV
    - ESS

production_start:
  target_year: 2028
  claim_status: CORPORATE_TARGET

unresolved:
  - Initial customer
  - Initial product
  - EV versus ESS allocation
  - Chemistry
  - Initial active capacity
  - Customer qualification
  - Line configuration

current_production_capacity:
  counted_gwh: 0
```

`EV·ESS 시장 대응 가능성`은 법인의 전략적 방향이지, 설비가 두 제품을 모두 생산하도록 이미 개조·검증됐다는 증거가 아니다.

---

## 13.4 미국 ESS 생산 Mapping

SK온은 2026년 6월 GRIDON 1세대의 미국 생산을 연내 시작할 계획이라고 발표했고, 미국 제조 네트워크로 SK Battery America, HSBMA, SK On Tennessee를 언급했다. 그러나 **어느 공장이 GRIDON Cell 또는 System을 생산하는지는 명시하지 않았다.** ([SK][7])

```yaml
us_ess_production_mapping:

  product:
    - GRIDON_Gen_1

  official_plan:
    target: U.S._production_in_2026
    claim_status: CORPORATE_TARGET

  candidate_network_named_by_company:
    - SK_Battery_America
    - HSBMA
    - SK_On_Tennessee

  exact_production_site:
    status: UNRESOLVED

  chemistry:
    status: UNRESOLVED_IN_CITED_SOURCE

  line_conversion:
    status: NOT_PUBLICLY_CONFIRMED

  prohibited:
    - Assign GRIDON to SK Battery America without a plant-specific source
    - Treat HSBMA EV capacity as freely available ESS capacity
    - Treat Tennessee as 2026 production capacity
```

---

## 13.5 United States Mapping Summary

| 거점            | 직접 확인된 제품·고객            | 현재 상태                 | 미확인 핵심항목           |
| ------------- | ----------------------- | --------------------- | ------------------ |
| SKBA Commerce | 과거 F-150 Lightning·ID.4 | EV 양산거점, 현재 배분 재검증 필요 | 신규 고객·ESS Line·화학계 |
| HSBMA         | 현대·기아·제네시스, 초기 IONIQ 9  | 2026 상업생산·Ramp-Up     | Line별 Capacity·화학계 |
| Tennessee     | EV·ESS 시장 대응 방향         | 2028 생산준비             | 고객·제품·초기 Capacity  |
| 미국 GRIDON     | 2026년 미국 생산 목표          | 공장 미지정                | 생산 Site·화학계·전환범위   |

---
