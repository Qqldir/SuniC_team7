---
id: skon-d08-d08-04-anode-graphite-silicon-supply-chain-대표-지
title: Anode / Graphite / Silicon Supply Chain — 대표 지식그래프 레코드
summary: "SK온의 음극재, 흑연, 규소 원소재 공급 계약과 협약 현황을 공급자별·수량·일정으로 정리한 기록"
tags: [d08, supply-chain, schema]
keywords: [공급계약, 공급사, 웨스트워터, 어비스, 대주, Group14, 지식그래프, 음극재, EV배터리, 원소재공급, 흑연, 규소, 공급협력사, 계약현황, JDA, Westwater, Urbix, Daejoo]
related: []
priority: normal
domain: D08
section: D08-04
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain"
tokens: 827
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain

### 7. 대표 지식그래프 레코드

```yaml
agreement_record:
  agreement_id: AGR-ANODE-WWR-2024
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-WESTWATER
  predecessor_relationship_id: JDA-ANODE-WWR-2022
  agreement_type: PRODUCTS_PROCUREMENT
  binding_status_at_signing: BINDING_CONDITIONAL
  material_id: MAT-GR-CSPG
  disclosed_product_grade: CSPG-10
  supplier_facility_id: FAC-WWR-KELLYTON
  announced_total_max_tonne: 34000
  announced_supply_window: 2027-2031
  final_year_forecast_tonne: 10000
  receiving_plants_announced:
    - SK_ON_GEORGIA
    - BLUEOVAL_SK_KENTUCKY
    - BLUEOVAL_SK_TENNESSEE
  conditions:
    - KELLYTON_PHASE1_COMPLETION_BY_LONGSTOP
    - THIRD_PARTY_OEM_NOMINATION_OR_SUPPLY_AGREEMENT
    - PRODUCT_CONFORMITY_AND_INTERNAL_ASSESSMENT
  termination_notice_date: 2026-03-31
  commercial_shipments_to_sk_on: 0
  status: CANCELLED
  current_secured_quantity_tonne: 0
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S04-001, S04-002, S04-004, S04-005]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: JDA-ANODE-URBIX-2023
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-URBIX
  agreement_type: RND_JDA
  binding_status: DEVELOPMENT_ONLY
  materials: [MAT-GR-NAT-FLAKE, MAT-GR-CSPG]
  announced_date: 2023-01-18
  procurement_clause: CONSIDER_AFTER_SUCCESSFUL_DEVELOPMENT
  announced_capacity_target_tpy: 28500
  target_capacity_is_current_operating_capacity: false
  final_supply_agreement: NOT_PUBLICLY_CONFIRMED
  commercial_shipments: NOT_PUBLICLY_CONFIRMED
  status: JDA_UNVERIFIED_CURRENT
  sk_on_procurement_confirmed: false
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S04-006]
  as_of_date: 2026-08-02
```

```yaml
agreement_record:
  agreement_id: AGR-SI-DAEJOO-2024
  buyer_entity_id: ENT-SKON
  counterparty_id: SUP-DAEJOO
  predecessor_relationship_id: JDA-SI-DAEJOO-2022
  agreement_type: COMMERCIAL_SUPPLY_ANNOUNCEMENT
  material_id: MAT-SI-OX
  production_part_approval_completed: 2023-Q2
  announced_supply_start: 2024-Q1
  intended_end_market: NORTH_AMERICA_EV
  quantity_tonne: null
  contract_end: null
  supplier_facility_id: FAC-DAEJOO-SIHEUNG
  confirmed_receiving_plant: UNKNOWN
  actual_drawdown: UNKNOWN
  status: ANNOUNCED_COMMERCIAL_SUPPLY
  sk_on_procurement_confirmed: true
  current_continuation_confirmed_as_of_date: unknown
  evidence_status: CONFIRMED_MULTI
  source_ids: [S04-007, S04-008, S04-009, S04-010]
  as_of_date: 2026-08-02
```

```yaml
relationship_record:
  relationship_id: REL-SKINC-GROUP14-2025
  from_entity_id: ENT-SKINC
  to_entity_id: SUP-GROUP14
  relationship_type: EQUITY_INVESTMENT_ECOSYSTEM
  event_date: 2025-08-20
  series_d_total_usd: 463000000
  round_led_by_sk_inc: true
  sangju_factory_owner_after_transaction: GROUP14_100_PERCENT
  sk_on_is_party: false
  sk_on_supply_agreement: NOT_PUBLICLY_CONFIRMED
  procurement_graph_eligible: false
  evidence_status: CONFIRMED_PRIMARY
  source_ids: [S04-013]
  as_of_date: 2026-08-02
```
