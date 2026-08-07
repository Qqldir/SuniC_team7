---
id: skon-d08-d08-02-cathode-supply-chain-대표-지식그래프-레코드
title: Cathode Supply Chain — 대표 지식그래프 레코드
summary: "SK온의 양극재(NCM) 공급 계약, 프로젝트, 협력사 관계에 대한 구조화된 지식그래프 레코드로, 공급처·규모·상태를 기술한다."
tags: [d08, supply-chain, schema]
keywords: [양극재, 공급망, 계약, NCM, 공급사, 배터리 소재, 프로젝트, 원재료, 지식그래프, 정극, 공급 계약, 협력사, 프레임워크, 공급처, EcoPro, 조달 정보]
related: []
priority: normal
domain: D08
section: D08-02
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain"
tokens: 766
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain

### 6. 대표 지식그래프 레코드

```yaml
agreement_record:
  agreement_id: AGR-CAM-LANDF-2024
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-LANDF
  agreement_type: SUPPLY
  binding_status: BINDING
  materials:
    - MAT-NCM-CAM-HN
  announced_quantity_value: 300000
  announced_quantity_unit: metric_tonne
  announced_value_krw: 13191000000000
  value_semantics: ANNOUNCED_ESTIMATE_NOT_BACKLOG
  valid_from: 2024-03-22
  announced_valid_through: 2030-12-31
  valid_to_exclusive: 2031-01-01
  receiving_entities:
    - SK_ON_DOMESTIC_AND_OVERSEAS_PRODUCTION_ENTITIES
    - SK_ON_DESIGNATED_ENTITIES
  supplier_facilities: []
  final_oem: UNKNOWN
  actual_drawdown: UNKNOWN
  status: ACTIVE
  sk_on_procurement_confirmed: true
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S02-006, S02-007]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-CAM-EASPRING-2025-A
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-EASPRING
  agreement_type: FRAMEWORK_SUPPLY
  binding_status: FRAMEWORK
  materials:
    - MAT-NCM-CAM-HN
    - MAT-NCM-CAM-GEN
  expected_quantity_value: 17000
  expected_quantity_unit: metric_tonne
  quantity_semantics: EXPECTED_UNDER_MONTHLY_PURCHASE_ORDERS
  valid_from: 2025-02-28
  announced_valid_through: 2027-12-31
  valid_to_exclusive: 2028-01-01
  candidate_supply_countries: [CN, FI]
  confirmed_supply_facility: UNKNOWN
  confirmed_receiving_plant: UNKNOWN
  status: FRAMEWORK
  sk_on_procurement_confirmed: unknown
  evidence_status: CONFIRMED_MULTI
  regulatory_tags: [US_PFE_MATERIAL_ASSISTANCE, EU_BATT_CF, EU_BATT_DD]
  source_ids: [S02-010, S02-011, S02-012]
  as_of_date: 2026-08-02
```

```yaml
project_record:
  project_id: PRJ-CAM-ECOPRO-CANADA
  facility_id: FAC-ECOPRO-CANADA-BECANCOUR
  participants_announced:
    - EcoPro_BM_or_project_affiliate
    - SK_On
    - Ford
  material_id: MAT-NCM-CAM-HN
  announced_nameplate_capacity_tpy: 45000
  announced_start_target: 2026-H1
  current_operating_capacity_tpy: 0
  current_status: SUSPENDED
  restart_date: UNKNOWN
  cap_table_current: UNKNOWN
  status_note: ORIGINAL_START_TARGET_IS_NOT_CURRENT_OPERATIONAL_EVIDENCE
  evidence_status: CONFIRMED_MULTI
  source_ids: [S02-015, S02-016, S02-017, S02-018]
  as_of_date: 2026-08-02
```

```yaml
relationship_record:
  relationship_id: REL-BTR-SKON-2025
  from_entity_id: SUP-BTR
  to_entity_id: ENT-SKON_GROUP
  relationship_type: SUPPLIER_GROUP_SALES
  sales_value_cny_2025: 3472997237.57
  product_scope: BATTERY_MATERIALS_NOT_DISCLOSED
  cathode_material_value: UNKNOWN
  producing_facility: UNKNOWN
  jv_equity_latest_percent: 25.00
  jv_equity_historical_claim_percent: 31.3
  evidence_status: CONFLICTED
  source_ids: [S02-013, S02-014]
  as_of_date: 2026-08-02
```
