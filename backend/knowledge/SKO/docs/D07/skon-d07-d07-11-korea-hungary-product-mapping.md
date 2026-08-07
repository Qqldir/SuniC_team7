---
id: skon-d07-d07-11-korea-hungary-product-mapping
title: Korea·Hungary Product Mapping
summary: "SK온의 국내 서산 공장과 헝가리 코마롐, 이반차 배터리 공장의 설계용량, 운영 현황, 고객·차종·화학계별 배분 상태를 정리한 생산거점별 매핑 자료"
tags: [d07, footprint, schema, table]
keywords: [배터리 공장, EV 배터리 셀, 설계능력, GWh, 고객 할당, 차종, 화학계, OEM, 서산, 코마롬, 이반차, 배터리공장, 생산거점, 설계용량, EV배터리셀, 고객할당, 헝가리]
related: []
priority: normal
domain: D07
section: D07-11.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1274
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-11. Korea·Hungary Product Mapping

## 11.1 서산

SK이노베이션은 2012년 서산 배터리공장 완공을, 이후 공시에서는 서산 1·2동의 설계능력을 7GWh로 제시해 왔다. 다만 공개자료만으로는 2026년 현재 각 동별 고객·차종·화학계·Line 배분을 확인할 수 없다. ([SK Innovation][1])

```yaml
plant_id: PLANT-D07-KR-SEO
canonical_name: Seosan Battery Plant

confirmed:
  plant_type:
    - Battery manufacturing site
  operating_status: OPERATIONAL
  broad_product_scope:
    - EV battery cell

unresolved:
  - Current customer by building
  - Current vehicle program
  - Cell product generation
  - Cathode chemistry by line
  - EV versus ESS allocation
  - Module and pack production scope
  - Actual line count
  - Customer-qualified capacity

mapping_status:
  product: GENERIC_EV_CELL_CONFIRMED
  customer: UNRESOLVED
  chemistry: UNRESOLVED
  line: UNRESOLVED

evidence_level: DIRECT_OFFICIAL
confidence: HIGH

source_ids:
  - SRC-OFF-D07-002
  - SRC-OFF-D07-007
```

### 서산 해석

서산은 SK온의 국내 초기 양산·공정학습 거점이라는 의미가 크지만, 이를 특정 현대차그룹 모델이나 특정 NCM 제품의 현재 전담공장으로 지정할 공개근거는 부족하다.

---

## 11.2 코마롬 1·2

SK이노베이션은 2020년 코마롬 EV 배터리공장 양산을 시작했으며, 현재 공식 글로벌 네트워크에는 코마롬의 `SK On Hungary Kft.`와 `SK Battery Manufacturing Kft.`가 별도 사업장으로 등록돼 있다. 과거 IR 기준 설계 Capacity는 각각 7.5GWh와 약 10GWh다. ([SK Innovation][1])

```yaml
hungary_komarom_mapping:

  plant_1:
    plant_id: PLANT-D07-HU-KOM1
    operating_entity: SK_ON_HUNGARY_KFT
    operating_status: OPERATIONAL
    broad_product_scope:
      - EV battery cell
    design_capacity_gwh: 7.5

  plant_2:
    plant_id: PLANT-D07-HU-KOM2
    operating_entity: SK_BATTERY_MANUFACTURING_KFT
    operating_status: OPERATIONAL
    broad_product_scope:
      - EV battery cell
    design_capacity_gwh: approximately_10

  common_unresolved:
    - OEM allocation by plant
    - Vehicle model
    - Product generation
    - Cathode chemistry
    - Cell dimensions
    - Line-level capacity
    - Customer qualification status

mapping_status:
  plant_to_ev_cell: DIRECT_OFFICIAL
  plant_to_customer: UNRESOLVED
  plant_to_model: UNRESOLVED
  plant_to_chemistry: UNRESOLVED
```

코마롬 두 공장이 모두 유럽 OEM 수요를 지원하는 EV 배터리 거점이라는 수준은 확인되지만, SK온의 글로벌 고객목록을 근거로 Volkswagen·Ford·Mercedes-Benz 등의 물량을 각 공장에 임의 배정하지 않는다.

---

## 11.3 이반차

이반차는 SK온의 헝가리 세 번째 배터리 생산시설이며 설계능력은 30GWh로 공개됐다. 공식 글로벌 네트워크에도 이반차 사업장이 등록돼 있지만, 공개자료만으로는 실제 가동 Line 수와 고객별 배분을 확인할 수 없다. ([SK On][2])

```yaml
plant_id: PLANT-D07-HU-IVA
canonical_name: Ivancsa Battery Plant

confirmed:
  broad_product_scope:
    - EV battery cell
  gross_design_capacity_gwh: 30
  operating_status:
    - PARTIAL_OPERATION
    - RAMPING

unresolved:
  - Customer-qualified capacity
  - Actual normalized output
  - Vehicle model allocation
  - Product chemistry
  - Number of active lines
  - Full 30 GWh ramp date

mapping_status:
  plant_to_product: DIRECT_OFFICIAL
  plant_to_customer: UNRESOLVED
  plant_to_vehicle: UNRESOLVED
  plant_to_chemistry: UNRESOLVED

confidence: HIGH
```

---

## 11.4 Korea·Hungary Mapping Summary

| 공장    | 공개 확인 제품    | 고객·모델 | 화학계 | Line 정보  |
| ----- | ----------- | ----- | --- | -------- |
| 서산    | EV 배터리 Cell | 미확인   | 미확인 | 미확인      |
| 코마롬 1 | EV 배터리 Cell | 미확인   | 미확인 | 미확인      |
| 코마롬 2 | EV 배터리 Cell | 미확인   | 미확인 | 미확인      |
| 이반차   | EV 배터리 Cell | 미확인   | 미확인 | 부분가동만 확인 |

---
