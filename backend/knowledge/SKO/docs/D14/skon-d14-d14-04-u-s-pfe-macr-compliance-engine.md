---
id: skon-d14-d14-04-u-s-pfe-macr-compliance-engine
title: U.S. PFE & MACR Compliance Engine
summary: "U.S. IRA 세액공제 적격성을 판정하기 위한 PFE 및 MACR 기준, 계산 방식, 검증 절차와 SK온의 우선 검토 대상을 정의한 가이드."
tags: [d14, policy, schema]
keywords: [외국계 영향, 재료 기준, 배터리 세액공제, 공급자 인증, 원가 추적, 원산지 확인, 세금 컴플라이언스, 관련자 거래, 적격 구성요소, 안전항구, PFE, MACR, 금지된 외국 영향, IRA 세액공제, 배터리 원산지, 공급사 인증, Eligible Component, Safe Harbor, 직접재료원가, 중국 연계]
related: []
priority: normal
domain: D14
section: D14-04
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 908
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-04 U.S. PFE & MACR Compliance Engine

### 1. 두 개의 서로 다른 판정

| 판정 | 질문 | 핵심 데이터 |
|---|---|---|
| Taxpayer/Entity PFE | Credit을 청구하는 법인 자체가 금지된 외국 영향·통제에 해당하는가? | 지분·Officer 선임권·부채·계약상 Effective Control·상장예외 |
| Material Assistance PFE | 적격 Cell·Module 또는 EST에 PFE 원재료·부품·제조지원이 기준 이상 들어갔는가? | 구성재료·직접재료원가·생산주체·공급사 Certification·Lot |

Notice 2026-15는 Foreign-influenced Entity 판단에서 특정 단일 Specified Foreign Entity의 25% 지분, 복수 Specified Foreign Entity의 합산 40%, 특정 부채 15%, Officer 선임권과 계약상 Effective Control 등을 다룬다. 하지만 상장사·80% 소유 예외와 구체적 사실관계가 있으므로 숫자 Threshold만으로 자동 확정하지 않는다.

### 2. Eligible Component MACR

```text
Eligible Component MACR
= (Total Direct Material Costs − PFE Direct Material Costs)
   / Total Direct Material Costs
```

판정은 연간 전체 구매량이 아니라 동일 Eligible Component·구성재료·지정기간별 추적 또는 허용된 평균화 방식으로 수행한다. `Reason to Know`가 있는 경우 공급사 확인서만으로 PFE Cost를 0으로 만들 수 없다. Safe Harbor 사용기간, 2026년 말 예정된 후속 Table, 최종규칙 발행을 Version으로 관리한다.

### 3. 최소 입력 필드

```yaml
pfe_macr_decision:
  taxpayer_legal_entity: null
  taxable_year_start_end: null
  eligible_component_type: BATTERY_CELL|BATTERY_MODULE|EAM|CRITICAL_MINERAL
  facility_line_product_grade: []
  sale_date_and_related_party_election: null
  constituent_materials:
    - material_id: null
      supplier_legal_entity: null
      production_facility: null
      ownership_control_debt_contract_rights: []
      direct_material_cost: null
      PFE_sourced_status: YES|NO|UNKNOWN
      lot_and_average_period: null
      certification_id: null
  total_direct_material_cost: null
  PFE_direct_material_cost: null
  MACR: null
  applicable_threshold_source_and_version: null
  conclusion: PASS|FAIL|REVIEW
  reason_to_know_checks: []
  tax_legal_reviewer: null
  source_ids: []
```

### 4. SK온 우선 검증대상

- 중국계 소유·통제 또는 기술·License 연계가 있는 CAM·AAM·Foil·Separator·Electrolyte 경로
- 중국 밖 시설이지만 중국계 Parent·Officer·Debt·Technology Agreement가 있는 경로
- JV·Related-party Sale·OEM 지정소재로 세액공제 납세자와 실제 경제부담자가 다른 Program
- EV Cell을 ESS로 전환해 45X 생산세액공제와 고객 48E 적격성을 동시에 검토하는 Program
- 공급사 Certification이 계약·Invoice·원산지·Lot·직접재료원가와 일치하지 않는 경로

---
