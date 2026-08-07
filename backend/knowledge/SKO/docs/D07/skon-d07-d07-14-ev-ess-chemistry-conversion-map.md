---
id: skon-d07-d07-14-ev-ess-chemistry-conversion-map
title: EV·ESS·Chemistry Conversion Map
summary: SK온 생산거점의 EV에서 ESS 전환 가능성을 평가하는 현황 매트릭스와 기술 요구사항 체크리스트
tags: [d07, footprint, schema, table]
keywords: [생산거점, 배터리 화학, EV→ESS 전환, NCM·LFP, 셀 포맷, 전환 요구사항, 고객 승인, 공정 호환성, 듀얼 유스, 배터리 제조, 배터리 셀, ESS, 전환 가능성, NCM LFP, 공정변경, 고객승인, CTP, 제조인증, 기술요구사항]
related: []
priority: normal
domain: D07
section: D07-14.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1159
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-14. EV·ESS·Chemistry Conversion Map

## 14.1 Conversion Status Vocabulary

```yaml
conversion_status:

  CURRENTLY_PRODUCING:
    definition: Target product is in commercial production

  QUALIFIED_DUAL_USE:
    definition: >
      Same line is officially confirmed as qualified for both products

  OFFICIAL_CONVERSION_PROGRAM:
    definition: >
      Company directly announced a named plant conversion

  OFFICIAL_MARKET_OPTIONALITY:
    definition: >
      Company states that a facility can pursue multiple markets,
      but manufacturing qualification is not disclosed

  ANALYTICAL_CONVERSION_CANDIDATE:
    definition: >
      Similar cell format or process suggests possible reuse,
      but no official conversion evidence exists

  NOT_FUNGIBLE:
    definition: >
      JV, customer agreement, equipment or product constraints prevent
      free reallocation

  UNRESOLVED:
    definition: Insufficient public evidence
```

---

## 14.2 Plant Conversion Matrix

| 거점            | 현재 공개 제품     | EV→ESS                      | NCM→LFP | 판정                               |
| ------------- | ------------ | --------------------------- | ------- | -------------------------------- |
| 서산            | EV Cell      | 공개 전환계획 없음                  | 미확인     | UNRESOLVED                       |
| 코마롬 1·2       | EV Cell      | 공개 전환계획 없음                  | 미확인     | UNRESOLVED                       |
| 이반차           | EV Cell      | 공개 전환계획 없음                  | 미확인     | UNRESOLVED                       |
| 옌청 1·2·3      | EV Cell      | 공개 전환계획 없음                  | 미확인     | UNRESOLVED                       |
| SKBA Commerce | EV Cell 생산이력 | 미국 ESS 후보 가능성은 있으나 Site 미지정 | 미확인     | ANALYTICAL_CANDIDATE             |
| HSBMA         | HMG EV Cell  | 자유로운 ESS 전환 근거 없음           | 미확인     | NOT_FUNGIBLE_PENDING_JV_APPROVAL |
| Tennessee     | 생산 전         | EV·ESS 전략적 선택 가능            | 미확인     | OFFICIAL_MARKET_OPTIONALITY      |

SK온은 미국 제조거점을 ESS 확대에 활용할 계획을 밝혔지만, 특정 EV Line의 ESS 전환, 공정변경 범위 또는 고객승인 상태를 공개하지 않았다. ([SK][7])

---

## 14.3 EV→ESS Conversion Requirement

```yaml
ev_to_ess_conversion_requirements:

  product:
    - Cell dimension
    - Capacity
    - Power-to-energy ratio
    - Cycle-life target
    - Calendar-life target
    - Safety architecture

  chemistry:
    - Cathode material
    - Anode formulation
    - Electrolyte
    - Formation protocol
    - Voltage window

  electrode:
    - Mixing recipe
    - Coating loading
    - Electrode thickness
    - Calender density
    - Slitting dimensions

  cell_assembly:
    - Stack count
    - Pouch dimensions
    - Electrolyte dose
    - Seal configuration

  cell_finishing:
    - Formation
    - Aging
    - Grading
    - Customer acceptance limits

  downstream:
    - Module or CTP architecture
    - ESS rack and container
    - BMS
    - Fire suppression
    - PCS interface

  commercial:
    - Customer qualification
    - Warranty
    - Local content
    - Incentive eligibility
    - JV partner approval
```

---

## 14.4 Conversion Readiness Score

```yaml
conversion_readiness_score:

  equipment_reuse:
    weight: 0.20

  material_and_chemistry_similarity:
    weight: 0.15

  cell_format_similarity:
    weight: 0.15

  formation_and_test_compatibility:
    weight: 0.10

  customer_qualification:
    weight: 0.15

  commercial_flexibility:
    weight: 0.10

  local_content_and_regulation:
    weight: 0.10

  conversion_downtime:
    weight: 0.05

  control:
    - Public capacity alone does not indicate conversion readiness
    - JV capacity receives a partner-approval constraint
    - Pre-SOP capacity cannot be counted as immediately convertible
```

---
