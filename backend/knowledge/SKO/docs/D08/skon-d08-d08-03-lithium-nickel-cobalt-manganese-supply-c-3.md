---
id: skon-d08-d08-03-lithium-nickel-cobalt-manganese-supply-c-3
title: Lithium / Nickel / Cobalt / Manganese Supply Chain — 대표 지식그래프 레코드
summary: "SK온의 리튬 공급 협력사와의 계약 상세 정보(계약 조건, 공급량, 일정 등)를 지식그래프 레코드로 표현한 메타데이터 모음이다."
tags: [d08, supply-chain, schema]
keywords: [리튬 공급 계약, SQM, Pilbara, POSCO-ARG, Lake Resources, 계약 수량, 공급 현황, 지식그래프, 바인딩 상태, 원소재 공급망, 리튬, 공급 계약, PPLS, 공급사, 메타데이터, 공급량, 원소재, LCE]
related: []
priority: normal
domain: D08
section: D08-03
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain"
tokens: 1407
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain

### 7. 대표 지식그래프 레코드

```yaml
agreement_record:
  agreement_id: AGR-LI-SQM-2022
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-SQM
  agreement_type: SUPPLY
  binding_status: BINDING
  material_id: MAT-LI-OH-BG
  announced_quantity_value: 57000
  announced_quantity_unit: metric_tonne_product
  quantity_semantics: CONTRACT_TOTAL_MAX_NOT_ANNUAL_NOT_REMAINING
  contract_signed_date: 2022-11-04
  announced_supply_start_year: 2023
  announced_supply_end_year: 2027
  structural_origin_nodes:
    - ORG-SQM-SALAR-ATACAMA
    - FAC-SQM-SALAR-CARMEN
  actual_drawdown: UNKNOWN
  remaining_quantity: UNKNOWN
  confirmed_receiving_plant: UNKNOWN
  physical_supply_confirmed: unknown
  traceability_status: ASSET_LEVEL_PARTIAL
  status: ACTIVE
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S03-001, S03-002]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-LIOH-PPLS-2024
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-PPLS
  agreement_type: SUPPLY
  binding_status: BINDING
  material_id: MAT-LI-OH-BG
  announced_quantity_value: 15000
  announced_quantity_unit: metric_tonne_product
  quantity_semantics: THREE_YEAR_TOTAL_MAX
  contract_signed_date: 2024-11-22
  announced_supply_start_year: 2025
  announced_supply_end_year: 2027
  structural_route:
    - MINE-PILGANGOORA
    - FAC-PPLS-YULCHON
  facility_nameplate_capacity_tpy: 43000
  facility_capacity_is_contract_quantity: false
  actual_drawdown: UNKNOWN
  confirmed_receiving_plant: UNKNOWN
  traceability_status: ASSET_LEVEL_PARTIAL
  status: ACTIVE
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S03-010, S03-011]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-LI-POSCO-ARG-2026
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-POSCO-ARG
  agreement_type: SUPPLY
  binding_status: BINDING
  mineral_family: LITHIUM
  material_id: UNKNOWN
  disclosed_product_form: UNSPECIFIED
  announced_quantity_value: 25000
  announced_quantity_unit: metric_tonne_form_unspecified
  quantity_semantics: THREE_YEAR_TOTAL_MAX
  contract_signed_date: 2026-02-24
  announced_supply_start_year: 2026
  announced_supply_end_year: 2028
  source_project_id: PRJ-POSCO-SAL-DE-ORO
  intended_markets: [EUROPE_EV, NORTH_AMERICA_EV]
  ess_use: UNDER_DISCUSSION
  qualification_status: FOUR_M_PENDING
  first_shipment_status: UNKNOWN
  physical_supply_confirmed: unknown
  status: BINDING_SIGNED
  evidence_status: CONFIRMED_MULTI
  source_ids: [S03-014, S03-015, S03-016, S03-017]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: CFA-LI-LAKE-2022
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-LAKE-RESOURCES
  project_id: PRJ-LAKE-KACHI
  agreement_type: CONDITIONAL_FRAMEWORK
  binding_status: CONDITIONAL
  material_id: MAT-LI-CARB-BG
  announced_quantity_tpa_max_LCE: 25000
  announced_total_max_LCE: 230000
  initial_term_years: 5
  option_years: 5
  strategic_equity_target_percent: 10
  conditions_precedent:
    - DFS
    - DEMONSTRATION_PLANT_RESULTS
    - SK_ON_DUE_DILIGENCE
    - PRODUCT_SPECIFICATIONS
    - FORMAL_AGREEMENTS_AND_APPROVALS
  current_fid_status: NOT_MADE_AS_OF_LAKE_FY2025
  equity_investment_completed: UNKNOWN
  first_delivery: NOT_CONFIRMED
  physical_supply_confirmed: false
  implementation_status: STALE_CONDITIONAL_UNVERIFIED
  status: FRAMEWORK
  evidence_status: CONFIRMED_MULTI
  source_ids: [S03-003, S03-004, S03-005]
  as_of_date: 2026-08-02
```

```yaml
project_record:
  project_id: PRJ-MHP-MOROWALI-SK-ECO-GEM
  participants_announced:
    - ENT-SKON
    - ENT-ECOPRO-GROUP
    - SUP-GEM
  country: ID
  region: SULAWESI_MOROWALI
  process: HPAL
  material_id: MAT-NI-MHP
  announced_nameplate_contained_Ni_tpy: 30000
  announced_start_target: 2024-Q3
  planned_ore_source: ORG-HENGJAYA-ORE-CANDIDATE
  final_jv_agreement: NOT_PUBLICLY_CONFIRMED
  legal_entity_id: UNKNOWN
  cap_table: UNKNOWN
  plant_completion: UNKNOWN
  commercial_operation: UNKNOWN
  verified_operating_capacity_tpy: null
  sk_on_offtake: UNKNOWN
  status: MOU_NON_BINDING
  evidence_status: CONFIRMED_MULTI
  regulatory_tags: [US_PFE_REVIEW_HIGH, ESG_HPAL_TAILINGS, ORIGIN_ID]
  source_ids: [S03-019, S03-020, S03-021]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-CO-GLENCORE-2019
  buyer_of_record_as_announced: SK_INNOVATION
  successor_business_relevance: SK_ON_BATTERY_BUSINESS
  counterparty_id: SUP-GLENCORE
  agreement_type: SUPPLY
  binding_status: BINDING_HISTORICAL
  material_id: MAT-CO-HYDROXIDE
  quantity_value: 30000
  quantity_unit: metric_tonne_contained_cobalt
  quantity_semantics: SIX_YEAR_TOTAL_MAX
  announced_supply_start_year: 2020
  announced_supply_end_year: 2025
  historical_resource_country: CD
  annual_third_party_audit: ANNOUNCED
  audit_standard: RMI_COBALT_REFINERY_SUPPLY_CHAIN_DD
  actual_drawdown: UNKNOWN
  renewal_after_2025: NOT_PUBLICLY_CONFIRMED
  status: EXPIRED
  traceability_status: HISTORICAL_PARTIAL
  evidence_status: CONFIRMED_MULTI
  source_ids: [S03-001, S03-022, S03-023]
  as_of_date: 2026-08-02
```
