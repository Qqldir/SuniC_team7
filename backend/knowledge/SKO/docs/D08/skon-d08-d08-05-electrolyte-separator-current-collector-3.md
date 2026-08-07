---
id: skon-d08-d08-05-electrolyte-separator-current-collector-3
title: "Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain — 대표 지식그래프 레코드"
summary: "SK온의 전해질·분리막·집전체 및 보조재료 공급처 간 계약, 공급 현황, 공급망 변화를 정리한 지식그래프 마스터 레코드"
tags: [d08, supply-chain, schema]
keywords: [배터리 소재, 공급계약, SKIET, Solid Power, 전해질 공급, 고체전해질, 도전성 첨가제, 공급망 이벤트, 구조조정, 알루미늄 호일, 전해질, 분리막, 집전체, 공급망, 배터리소재, SolidPower, 황화물, 알루미늄포일, 장기공급계약]
related: []
priority: normal
domain: D08
section: D08-05
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain"
tokens: 971
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain

### 7. 대표 지식그래프 레코드

```yaml
agreement_record:
  agreement_id: AGR-SEP-SKIET-2023
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-SKIET
  agreement_type: LONG_TERM_SUPPLY
  material_ids: [MAT-SEP-BASE, MAT-SEP-COATED]
  product_label: LiBS
  valid_from: 2023-01-01
  valid_to: 2027-12-31
  sales_region: [KOREA, OTHER_OVERSEAS]
  contract_value: CONFIDENTIAL
  contracted_area_m2: null
  actual_drawdown_m2: null
  assigned_supplier_facilities: UNKNOWN
  status: ACTIVE_CONFIRMED
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S05-001, S05-002]
  as_of_date: 2026-08-02
```

```yaml
supply_chain_event:
  event_id: EVT-SKIET-RESTRUCTURING-2026
  supplier_id: SUP-SKIET
  events:
    - facility_id: FAC-SKIET-CHANGZHOU
      event: DISPOSAL_OF_100_PERCENT_STAKE_ANNOUNCED
      announced_date: 2026-05-27
      completion_status: NOT_PUBLICLY_CONFIRMED_AS_OF_DATE
    - facility_id: FAC-SKIET-JEUNGPYEONG
      event: PRODUCTION_SUSPENSION_ANNOUNCED
      effective_date: 2026-11-30
      restart_date: UNDECIDED
  sk_on_contract_terminated: false
  supply_continuity_impact: UNKNOWN
  source_ids: [S05-003, S05-004, S05-005]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-SSE-SOLIDPOWER-2024
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-SOLIDPOWER
  agreement_type: RND_LICENSE_LINE_INSTALLATION_AND_ELECTROLYTE_SUPPLY
  material_id: MAT-SSE-SULFIDE
  initial_validation_purchase: true
  minimum_after_validation_tonne_through_2030: 8
  original_expected_minimum_revenue_usd: 10000000
  latest_expected_minimum_revenue_usd: 8300000
  commercial_cell_production_right: false
  line_site_acceptance_date: 2026-04-10
  electrolyte_validation_completed: NOT_PUBLICLY_CONFIRMED
  actual_delivered_tonne: UNKNOWN
  status: RND_SUPPLY_AGREEMENT_ACTIVE
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S05-015, S05-016, S05-017]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-ALFOIL-WUXING-SKON-2023
  buyer_entities:
    - SK_NEW_ENERGY_OR_DESIGNATED_SK_ON_PLANTS
  counterparty_id: SUP-WUXING-AL
  agreement_type: PRICE_AND_QUANTITY_FRAMEWORK
  material_id: MAT-AL-FOIL
  announced_supply_window: 2023-H2_TO_2027
  announced_estimated_quantity_tonne: 32400
  guaranteed_quantity_tonne: null
  final_quantity_basis: SUBSEQUENT_PURCHASE_ORDERS
  actual_drawdown_tonne: UNKNOWN
  status: ACTIVE_ORDER_BASED_FRAMEWORK
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S05-021, S05-022]
  as_of_date: 2026-08-02
```

```yaml
relationship_record:
  relationship_id: REL-CNT-ARTIENCE-SKON
  supplier_id: SUP-ARTIENCE
  buyer_entity_id: ENT-SKON
  material_id: MAT-CONDUCTIVE
  product_label: Lioaccum_CNT_Dispersion
  adoption_announced: 2021
  confirmed_supplier_facilities:
    - FAC-ARTIENCE-HUNGARY
    - FAC-ARTIENCE-GEORGIA
  kentucky_facility_status: PLANNED_TARGET_UNVERIFIED_CURRENT
  quantity: UNKNOWN
  contract_end: UNKNOWN
  status: COMMERCIAL_SUPPLY_CONFIRMED
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S05-025, S05-026, S05-027]
  as_of_date: 2026-08-02
```

```yaml
relationship_record:
  relationship_id: REL-CUFOIL-SKNEXILIS-CANDIDATE
  from_entity_id: SUP-SKNEXILIS
  to_entity_id: ENT-SKON
  relationship_type: POSSIBLE_GROUP_ADJACENT_SUPPLY
  material_id: MAT-CU-FOIL
  supplier_business_confirmed: true
  direct_contract_confirmed: false
  procurement_graph_eligible: false
  status: GROUP_ADJACENT_CANDIDATE
  source_ids: [S05-023, S05-024]
  as_of_date: 2026-08-02
```
