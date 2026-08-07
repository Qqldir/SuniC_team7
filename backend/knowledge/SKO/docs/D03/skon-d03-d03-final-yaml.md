---
id: skon-d03-d03-final-yaml
title: D03 Final YAML
summary: "SK온의 EV배터리, ESS, BaaS 등 제품 포트폴리오의 상용화 상태 분류 체계와 지식 인덱싱 구조를 정의하는 도메인 스키마."
tags: [d03, product, schema, "xref:d04"]
keywords: [EV 배터리, ESS, BaaS, 전고체 배터리, GRIDON, LFP, 상용화 상태, 지식 그래프, 포트폴리오, RAG, EV배터리, 전고체배터리, 지식그래프, 상용화분류]
related: []
priority: normal
domain: D03
section: ""
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1284
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03 Final YAML

```yaml
domain:
  domain_id: D03
  canonical_name: Products & Solutions
  company_id: CO-SKON
  company_name: SK On
  version: 1.5
  reference_date: 2026-07-30
  status: CONDITIONALLY_COMPLETE

scope:
  included:
    - EV battery products
    - ESS cells and systems
    - BaaS services
    - Next-generation batteries
    - Product architecture
    - Applications
    - Customers
    - Competitive benchmarks
    - Product knowledge graph
    - RAG chunks
    - OI seed candidates

  excluded_or_deferred:
    - Detailed patents
    - Manufacturing process parameters
    - Factory equipment
    - Product-level economics
    - Non-public customer specifications
    - Final Open Innovation recommendations

portfolio:
  ev_battery:
    commercial_core:
      - PROD-SKON-EV-001
      - PROD-SKON-EV-002
      - PROD-SKON-EV-003
      - PROD-SKON-EV-004

    disclosed_or_precommercial:
      - PROD-SKON-EV-005
      - PROD-SKON-EV-006
      - PROD-SKON-EV-007
      - PROD-SKON-EV-008
      - PROD-SKON-EV-009
      - PROD-SKON-EV-010
      - PROD-SKON-EV-011

  ess:
    entities:
      - PROD-SKON-ESS-001
      - PROD-SKON-ESS-002
      - PROD-SKON-ESS-003
      - PROD-SKON-ESS-004
      - PROD-SKON-ESS-005

    flagship_brand: GRIDON
    primary_chemistry: LFP
    principal_technologies:
      - EIS-Based BMS
      - Coolant Immersion
      - Coolant-Based Fire Suppression
      - DC Block
      - AC Block

  baas:
    services:
      - SERV-SKON-BAAS-001
      - SERV-SKON-BAAS-002
      - SERV-SKON-BAAS-003
      - SERV-SKON-BAAS-004
      - SERV-SKON-BAAS-005

    core_engine: TECH-SKON-BAAS-AI
    current_scale: NOT_DISCLOSED

  next_generation:
    products:
      - PROD-SKON-NEXT-001
      - PROD-SKON-NEXT-002

    pilot_infrastructure:
      - Daejeon All-Solid-State Battery Pilot Plant

    corporate_target:
      assb_commercialization: 2029

commercial_status_rules:
  commercial:
    - Actual sales or vehicle application confirmed

  contracted:
    - Signed supply contract confirmed

  production_planned:
    - Official production plan without verified output

  precommercial:
    - Product technology or prototype exists without mass production

  r_and_d:
    - Research or pilot development only

  corporate_target:
    - Forward-looking company objective

knowledge_graph:
  graph_id: KG-SKON-D03
  type:
    - Property Graph
    - Temporal Graph
    - Evidence-Linked Graph

  principal_node_classes:
    - Company
    - Product
    - Service
    - Technology
    - Chemistry
    - Form Factor
    - Architecture
    - Application
    - Customer
    - Partner
    - Pain Point
    - Competitor Product
    - OI Seed
    - Source

  provisional_entity_count: 178
  count_status: REQUIRES_AUTOMATED_EXPORT_AUDIT

rag:
  standard_chunks_created: 15
  fact_analysis_separation: true
  commercial_status_filter: true
  prototype_warning_required: true
  manufacturer_claim_tag_required: true
  missing_value_policy: RETURN_NOT_DISCLOSED

competitive_position:
  strengths:
    - High-nickel pouch heritage
    - Fast-charge product lineage
    - Hyper Fast prototype
    - EIS-based ESS diagnosis
    - Coolant-based ESS safety
    - Pouch-type LFP development
    - Solid-state pilot facility
    - BaaS analytics capability

  critical_gaps:
    - EV LFP commercial reference
    - Prismatic mass-production reference
    - Cylindrical platform
    - Hyper Fast commercial validation
    - GRIDON absolute performance disclosure
    - ESS operating reference
    - Dry-electrode scale-up
    - BaaS commercial scale
    - ASSB pilot yield

oi_seeds:
  - OI-SEED-D03-001
  - OI-SEED-D03-002
  - OI-SEED-D03-003
  - OI-SEED-D03-004
  - OI-SEED-D03-005
  - OI-SEED-D03-006
  - OI-SEED-D03-007
  - OI-SEED-D03-008
  - OI-SEED-D03-009
  - OI-SEED-D03-010

data_quality:
  overall: MEDIUM_HIGH
  source_quality: HIGH
  quantitative_spec_coverage: MEDIUM_LOW
  commercial_status_integrity: HIGH
  source_normalization_required: true
  annual_update_required: true

canonical_sources:
  sk_on_official: 13
  partner_official: 1
  competitor_official: 6
  total_primary_canonical_sources: 20

completion:
  D03_research_pack: COMPLETE_WITH_NORMALIZATION_REQUIRED
  product_taxonomy: COMPLETE
  product_master: COMPLETE
  application_mapping: COMPLETE
  customer_mapping: COMPLETE
  competitive_mapping: COMPLETE
  knowledge_graph: COMPLETE_V1
  entity_master: COMPLETE_V1
  chunk_library: COMPLETE_V1
  human_report: COMPLETE
  data_quality_register: COMPLETE
  source_index: COMPLETE_CANONICAL_SET

next_domain:
  domain_id: D04
  canonical_name: Technology Taxonomy
```

---
