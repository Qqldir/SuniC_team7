---
id: skon-d07-d07-12-china-product-customer-mapping
title: China Product·Customer Mapping
summary: "SK온 중국 5개 생산거점의 배터리 생산능력, 고객사 할당 현황 및 매핑 관리 규칙을 정의한 문서"
tags: [d07, footprint, schema]
keywords: [생산거점, EV배터리, 창저우, 옌청, 고객할당, 설계용량, 배터리셀, 제조라인, 중국 거점, 고객사 할당, 화학계, 합작법인, 설계능력]
related: []
priority: normal
domain: D07
section: D07-12.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 652
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-12. China Product·Customer Mapping

## 12.1 중국 생산거점 구조

공개 IR 자료는 창저우 7.5GWh, 후이저우 10GWh, 옌청 1·2 합계 27GWh, 옌청 3 33GWh의 설계능력을 제시한다. 그러나 공장별 고객·차종·화학계는 공식 Capacity 표에 포함되지 않는다. 

```yaml
china_plant_product_master:

  changzhou:
    plant_id: PLANT-D07-CN-CHA-JV
    ownership_scope: JOINT_VENTURE
    broad_product_scope:
      - EV battery cell
    customer_mapping: UNRESOLVED
    chemistry_mapping: UNRESOLVED

  huizhou:
    plant_id: PLANT-D07-CN-HUI-JV
    ownership_scope: JOINT_VENTURE_DISPOSAL_PENDING
    broad_product_scope:
      - EV battery cell
    customer_mapping: UNRESOLVED
    chemistry_mapping: UNRESOLVED

  yancheng_1:
    plant_id: PLANT-D07-CN-YAN1
    broad_product_scope:
      - EV battery cell
    customer_mapping: UNRESOLVED
    chemistry_mapping: UNRESOLVED

  yancheng_2:
    plant_id: PLANT-D07-CN-YAN2
    broad_product_scope:
      - EV battery cell
    customer_mapping: UNRESOLVED
    chemistry_mapping: UNRESOLVED

  yancheng_3:
    plant_id: PLANT-D07-CN-YAN3
    broad_product_scope:
      - EV battery cell
    operating_status:
      - PARTIAL_OPERATION
      - RAMPING
    customer_mapping: UNRESOLVED
    chemistry_mapping: UNRESOLVED
```

---

## 12.2 China Mapping Control

```yaml
china_customer_mapping_control:

  company_level_relationship:
    status: NOT_SUFFICIENT_FOR_PLANT_MAPPING

  geographic_proximity:
    status: NOT_SUFFICIENT_FOR_PLANT_MAPPING

  permitted:
    - Identify the plant as an EV battery site
    - Store ownership and capacity
    - Store confirmed customer only when the plant is named

  prohibited:
    - Assign Hyundai, Kia or another OEM solely from market reports
    - Assign all China output to local Chinese customers
    - Treat Yancheng 1, 2 and 3 as interchangeable qualified lines
```

### 분석

중국 거점은 옌청 중심의 운영통합 가능성이 있지만, 각 건물·법인의 고객승인과 제품사양이 같다는 증거는 없다. 지분 Swap이 완료되더라도 **법적 지배력 통합과 제조 Line 호환성은 별개**로 관리해야 한다.

---
