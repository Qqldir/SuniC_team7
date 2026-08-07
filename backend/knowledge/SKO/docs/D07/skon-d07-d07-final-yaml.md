---
id: skon-d07-d07-final-yaml
title: D07 Final YAML
summary: "SK온의 글로벌 생산 시설, 공장 위치, 현재 용량(97.4 GWh) 및 향후 확장 계획을 정의하는 마스터 데이터 레지스트리 문서다."
tags: [d07, footprint, schema, "xref:d08"]
keywords: [생산거점, 설비용량, GWh, 배터리, 합작투자, 고객매핑, 전기차, ESS, 소유권, 공정능력, 배터리 공장, 생산능력, 글로벌 생산거점, 용량계획, 이용률, 합작회사, EV-ESS, 공장 마스터, 생산 발자국]
related: []
priority: normal
domain: D07
section: ""
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1775
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07 Final YAML

```yaml
domain:
  domain_id: D07
  canonical_name: Manufacturing Footprint, Plants and Capacity
  company_id: CO-SKON
  company_name: SK On
  version: 1.3
  reference_date: 2026-08-02

  status:
    value: CONDITIONALLY_COMPLETE_WITH_CURRENT_CAPACITY_OPEN
    reason:
      - Post-restructuring official capacity table unavailable
      - Plant-level operating and customer-qualified capacity unavailable

scope:

  included:
    - Global plant master
    - Site clusters
    - Legal ownership
    - Joint ventures
    - Transferred assets
    - Design and reported capacity
    - Capacity events
    - Operating and ramp status
    - Plant–product–customer mapping
    - EV–ESS conversion assessment
    - Customer-linked capacity
    - Capacity redundancy
    - Policy eligibility
    - Logistics
    - Utility and labor constraints
    - Footprint economics boundary
    - Footprint OI opportunities

  deferred:
    - Detailed material origin
    - Customer contract economics
    - Plant-level manufacturing cost
    - CAPEX and subsidy accounting
    - Environmental permit audit
    - Field quality by plant

registry:

  sources:
    canonical_total: 19
    deprecated_aliases:
      - SRC-OFF-D07-009

  plants:
    current_or_pending: 13
    transferred_historical: 2
    total: 15

  site_clusters:
    total: 1
    entities:
      - SITE-D07-US-COMMERCE

  ownership_events: 3
  capacity_events: 8
  confirmed_customer_mappings: 4
  risk_entities: 6
  pain_points: 10
  oi_seeds: 21
  chunks: 20
  graph_queries: 18
  relationship_triples: 32

capacity_truth:

  latest_official_consolidated_snapshot:
    reference_date: 2026-03-31
    value_gwh: 97.4
    evidence_level: DIRECT_REGULATORY

  historical:
    2024_gwh: 71.5
    2025_gwh: 94.6

  utilization:
    2024: 43.8_percent
    2025: 48.7_percent
    2026_Q1: 36.5_percent

  post_kentucky_known_scope_pro_forma:
    value_gwh: 94.3
    evidence_level: ANALYST_INFERENCE
    official_company_value: false

  current_official_consolidated_capacity:
    value: UNRESOLVED

capacity_non_additive_records:

  HSBMA:
    gross_design_capacity_gwh: 35
    ownership:
      SK_On: 50_percent
      Hyundai_Motor_Group: 50_percent
    capacity_type: JV_GROSS_DESIGN_CAPACITY
    commercial_production_start: 2026-06-01
    consolidated_addition: prohibited

  Tennessee:
    legacy_design_reference_gwh: 45
    current_operating_capacity_gwh: 0
    production_target: 2028
    capacity_type: LEGACY_DESIGN_REFERENCE

  Nissan:
    contract_total_gwh: nearly_100
    delivery_period: 2028_to_2033
    production_site: UNRESOLVED

  Slate:
    contract_total_gwh: approximately_20
    delivery_period: 2026_to_2031
    production_site: UNRESOLVED

plant_master:

  korea:
    - PLANT-D07-KR-SEO

  europe:
    - PLANT-D07-HU-KOM1
    - PLANT-D07-HU-KOM2
    - PLANT-D07-HU-IVA

  china:
    - PLANT-D07-CN-CHA-JV
    - PLANT-D07-CN-HUI-JV
    - PLANT-D07-CN-YAN1
    - PLANT-D07-CN-YAN2
    - PLANT-D07-CN-YAN3

  united_states_current:
    - PLANT-D07-US-GA1
    - PLANT-D07-US-GA2
    - PLANT-D07-US-HSBMA
    - PLANT-D07-US-TN

  transferred:
    - PLANT-D07-US-KY1
    - PLANT-D07-US-KY2

confirmed_customer_links:

  Commerce:
    status: HISTORICAL_CURRENT_REVALIDATION_REQUIRED
    products:
      - Ford_F150_Lightning
      - Volkswagen_ID4

  HSBMA:
    status: CURRENT
    customer:
      - Hyundai_Motor_Group
    initial_model:
      - Hyundai_IONIQ_9

  Nissan:
    plant_nomination: UNRESOLVED

  Slate:
    plant_nomination: UNRESOLVED

  GRIDON:
    production_site: UNRESOLVED

capacity_qualification_ladder:
  - Gross Design Capacity
  - Installed Capacity
  - Mechanically Available Capacity
  - Process-Qualified Capacity
  - Customer-Qualified Capacity
  - Scheduled Capacity
  - Good-Output Capacity
  - Commercially Allocable Capacity

priority_oi_portfolio:

  foundation:
    - OI-SEED-D07-006 Plant-Line-Product-Customer Knowledge Graph
    - OI-SEED-D07-007 Qualified Capacity Ledger
    - OI-SEED-D07-014 Real-Time Capacity Event Ledger

  customer_and_demand:
    - OI-SEED-D07-008 Customer Concentration Early Warning
    - OI-SEED-D07-011 HSBMA Ramp Control Tower
    - OI-SEED-D07-017 Contract-to-Capacity Bridge

  flexibility:
    - OI-SEED-D07-003 EV-to-ESS Conversion Readiness
    - OI-SEED-D07-009 Alternative Site Qualification
    - OI-SEED-D07-010 EV-ESS Conversion Assessment
    - OI-SEED-D07-013 Global Footprint Stress Test

  policy_and_economics:
    - OI-SEED-D07-015 45X-PFE Eligibility Twin
    - OI-SEED-D07-016 Tariff and Local-Content Rules Engine
    - OI-SEED-D07-020 Incentive Covenant Tracker
    - OI-SEED-D07-021 Footprint Economics Scenario Engine

  ramp_and_resources:
    - OI-SEED-D07-005 Ramp-Up Learning Transfer
    - OI-SEED-D07-012 Tennessee Pre-SOP Readiness Twin
    - OI-SEED-D07-019 Utility-Labor Constraint Twin

data_quality:

  strengths:
    - Ownership and JV structure
    - Regulatory capacity history
    - Major 2026 restructuring events
    - HSBMA and Tennessee current status
    - Capacity-definition governance
    - Scenario and OI architecture

  weaknesses:
    - Current consolidated capacity
    - Plant and line utilization
    - Customer-qualified capacity
    - Europe and China customer mapping
    - Current Commerce customer mix
    - Nissan and Slate plant nomination
    - EV-to-ESS conversion status
    - Plant-level cost and policy eligibility

  critical_open_items:
    - Post-restructuring regulatory capacity table
    - Plant–line–product master
    - Customer qualification by site
    - Good-output capacity
    - Alternative-site approval
    - Material-origin and policy ledger
    - Plant utility and workforce headroom

completion:
  domain_boundary: COMPLETE
  capacity_vocabulary: COMPLETE
  research_pack: COMPLETE_V3
  global_plant_master: COMPLETE_PROVISIONAL
  ownership_and_jv: COMPLETE
  capacity_timeline: COMPLETE
  site_product_customer_mapping: COMPLETE_WITH_MAJOR_GAPS
  qualified_capacity_model: COMPLETE
  conversion_and_redundancy: COMPLETE_PRELIMINARY
  policy_and_economics_boundary: COMPLETE
  chunk_library: COMPLETE_V1
  graph_queries: QUERY_DESIGN_ACCEPTED
  relationship_graph: COMPLETE_V1
  final_quality_audit: COMPLETE
  human_readable_strategy: COMPLETE
  final_yaml: COMPLETE

next_domain:
  domain_id: D08
  canonical_name: Raw Materials, Suppliers and Supply Chain
```
