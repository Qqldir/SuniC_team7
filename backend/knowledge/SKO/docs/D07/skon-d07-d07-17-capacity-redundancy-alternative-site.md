---
id: skon-d07-d07-17-capacity-redundancy-alternative-site
title: Capacity Redundancy·Alternative Site
summary: 배터리 셀 생산 공장의 대체 가능 조건을 6개 측면(물리·고객·상업·소재·물류·실제)으로 정의하고 지역별 현황을 평가한다.
tags: [d07, footprint, schema]
keywords: [캐파시티 리던던시, 대체 공장 자격, 지역별 평가, 물리적 호환성, 고객 승인, 공급망 검증, 계약 제약, Cell 제조, 생산능력 분산, 공급망, 적격 기준, 리던던시, HSBMA, JV]
related: []
priority: normal
domain: D07
section: D07-17.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1023
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-17. Capacity Redundancy·Alternative Site

## 17.1 Capacity Redundancy Definition

```yaml
capacity_redundancy_types:

  PHYSICAL_REDUNDANCY:
    definition: >
      다른 공장이 동일하거나 유사한 Cell을 제조할 설비를 보유

  CUSTOMER_QUALIFIED_REDUNDANCY:
    definition: >
      고객이 대체공장의 생산품을 승인

  COMMERCIAL_REDUNDANCY:
    definition: >
      계약·JV·지역규정상 물량을 이전할 수 있음

  MATERIAL_REDUNDANCY:
    definition: >
      대상공장에서 승인된 공급망과 소재를 확보

  LOGISTICS_REDUNDANCY:
    definition: >
      고객 납기와 운송조건을 충족

  EFFECTIVE_REDUNDANCY:
    definition: >
      위 조건을 모두 충족한 실제 대체 Capacity
```

---

## 17.2 Regional Redundancy Assessment

```yaml
regional_redundancy_assessment:

  korea:
    sites:
      - Seosan
    assessment:
      - Single publicly identified domestic cell manufacturing cluster
    effective_redundancy: LOW_OR_UNRESOLVED

  europe:
    sites:
      - Komarom_1
      - Komarom_2
      - Ivancsa
    strength:
      - Three manufacturing units in Hungary
    constraints:
      - Customer and product qualification by site is undisclosed
      - Same-country concentration
    effective_redundancy: MEDIUM_UNVERIFIED

  china:
    sites:
      - Changzhou
      - Huizhou
      - Yancheng_1
      - Yancheng_2
      - Yancheng_3
    strength:
      - Multiple assets
    constraints:
      - JV ownership
      - Pending ownership restructuring
      - Customer qualification unknown
      - Increasing concentration in Yancheng
    effective_redundancy: MEDIUM_LOW_UNVERIFIED

  united_states:
    sites:
      - SKBA_Commerce
      - HSBMA
      - SK_On_Tennessee

    current_constraints:
      - HSBMA is HMG-linked JV capacity
      - Tennessee is not yet producing
      - SKBA current customer and product mix is unresolved
      - ESS site is not publicly specified

    effective_current_redundancy: LOW_TO_MEDIUM
    future_potential: HIGHER_AFTER_TENNESSEE_SOP
```

HSBMA의 Capacity는 현대차그룹 연계 JV이므로 SK온이 다른 고객이나 ESS 프로젝트에 독자적으로 전환할 수 있는 유휴 Capacity로 간주해서는 안 된다. Tennessee도 2028년 이전의 현재 대체 생산능력으로 계산할 수 없다. ([HSAGP ENERGY LLC][4])

---

## 17.3 Alternative Site Qualification Record

```yaml
alternative_site_record:

  product_id: required
  current_plant_id: required
  alternative_plant_id: required

  physical_compatibility:
    - Cell dimensions
    - Chemistry
    - Electrode design
    - Equipment capability
    - Module or pack interface

  customer:
    - Approval status
    - Audit status
    - PPAP or equivalent
    - Validation samples
    - Lead time

  commercial:
    - Contract restriction
    - JV approval
    - Tariff
    - Incentive
    - Local-content requirement

  supply_chain:
    - Material qualification
    - Supplier capacity
    - Logistics
    - Customs

  status:
    - FULLY_QUALIFIED
    - TECHNICALLY_COMPATIBLE
    - QUALIFICATION_REQUIRED
    - CONTRACTUALLY_RESTRICTED
    - NOT_COMPATIBLE
    - UNRESOLVED
```

---

## 17.4 Redundancy Scenario Graph

```text
Plant Disruption
      ↓
Affected Customer·Product·Capacity
      ↓
Technically Compatible Sites
      ↓
Customer-Qualified Sites
      ↓
Commercially Available Capacity
      ↓
Material·Logistics Feasibility
      ↓
Effective Recoverable Capacity
```

---
