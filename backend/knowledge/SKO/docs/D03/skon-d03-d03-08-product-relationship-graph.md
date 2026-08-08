---
id: skon-d03-d03-08-product-relationship-graph
title: Product Relationship Graph
summary: "SK온 제품·솔루션 간의 관계를 구축하는 지식 그래프의 노드 클래스, 엣지 타입, 메타데이터 스키마를 정의한 명세"
tags: [d03, product, schema]
keywords: [지식그래프, 노드클래스, 엣지타입, 메타데이터, 제품관계, PropertyGraph, 제품족, SKON, 화학조성, 기술스택, 지식 그래프, 제품 관계도, 노드 클래스, 엣지 타입, 그래프 스키마, 제품 분류체계, Knowledge Graph, 구조화 데이터, 온톨로지]
related: []
priority: normal
domain: D03
section: D03-08.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1278
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# D03-08. Product Relationship Graph

## 8.1 Graph Metadata

```yaml
graph_id: KG-SKON-D03
graph_name: SK On Products and Solutions Knowledge Graph
graph_version: 1.0
company_scope:
  - SK On

domain_scope:
  - D03 Products and Solutions

external_scope:
  - Competitive Product Benchmarks
  - Customer Applications
  - BaaS Partners
  - Open Innovation Seeds

graph_type:
  - Directed
  - Property Graph
  - Temporal
  - Evidence-Linked
  - Confidence-Weighted

canonical_language:
  primary: Korean
  secondary: English

temporal_fields:
  - valid_from
  - valid_to
  - reference_date
  - last_verified_at

provenance_fields:
  - source_ids
  - evidence_type
  - reliability_grade
  - confidence
  - extraction_method
```

---

## 8.2 Node Classes

```yaml
node_classes:

  COMPANY:
    id_prefix: CO-
    examples:
      - CO-SKON
      - CO-CATL
      - CO-LGES

  PRODUCT_FAMILY:
    id_prefix: PF-
    examples:
      - PF-SKON-HIGH-NICKEL
      - PF-SKON-ESS
      - PF-SKON-BAAS

  PRODUCT:
    id_prefix: PROD-
    examples:
      - PROD-SKON-EV-003
      - PROD-SKON-ESS-002

  SERVICE:
    id_prefix: SERV-
    examples:
      - SERV-SKON-BAAS-001

  TECHNOLOGY:
    id_prefix: TECH-
    examples:
      - TECH-SKON-SUFAST
      - TECH-SKON-EIS-BMS

  CHEMISTRY:
    id_prefix: CHEM-
    examples:
      - CHEM-NCM
      - CHEM-LFP

  FORM_FACTOR:
    id_prefix: FORM-
    examples:
      - FORM-POUCH
      - FORM-PRISMATIC
      - FORM-CYLINDRICAL

  ARCHITECTURE:
    id_prefix: ARCH-
    examples:
      - ARCH-CTP
      - ARCH-DC-BLOCK
      - ARCH-AC-BLOCK

  APPLICATION:
    id_prefix: APP-
    examples:
      - APP-SKON-005
      - APP-SKON-009

  CUSTOMER:
    id_prefix: CUST-
    examples:
      - CUST-SKON-OEM-001
      - CUST-SKON-ESS-001

  PARTNER:
    id_prefix: PART-
    examples:
      - PART-SOLID-POWER
      - PART-SOFTBERRY

  PAIN_POINT:
    id_prefix: PAIN-
    examples:
      - PAIN-LITHIUM-PLATING
      - PAIN-THERMAL-PROPAGATION

  COMPETITOR_PRODUCT:
    id_prefix: COMP-
    examples:
      - COMP-CATL-EV-001
      - COMP-SDI-ESS-001

  OI_SEED:
    id_prefix: OI-SEED-
    examples:
      - OI-SEED-D03-001

  SOURCE:
    id_prefix: SRC-
```

---

## 8.3 Canonical Edge Types

```yaml
edge_types:

  HAS_PRODUCT:
    domain: COMPANY
    range:
      - PRODUCT
      - PRODUCT_FAMILY

  HAS_VARIANT:
    domain:
      - PRODUCT
      - PRODUCT_FAMILY
    range: PRODUCT

  EVOLVED_FROM:
    domain: PRODUCT
    range: PRODUCT

  USES_CHEMISTRY:
    domain: PRODUCT
    range: CHEMISTRY

  HAS_FORM_FACTOR:
    domain: PRODUCT
    range: FORM_FACTOR

  USES_TECHNOLOGY:
    domain:
      - PRODUCT
      - SERVICE
    range: TECHNOLOGY

  HAS_COMPONENT:
    domain:
      - PRODUCT
      - ARCHITECTURE
    range:
      - PRODUCT
      - TECHNOLOGY
      - ARCHITECTURE

  SUPPORTS_APPLICATION:
    domain:
      - PRODUCT
      - SERVICE
    range: APPLICATION

  SUPPLIED_TO:
    domain: PRODUCT
    range: CUSTOMER

  APPLIED_TO:
    domain: PRODUCT
    range:
      - APPLICATION
      - CUSTOMER

  CO_DEVELOPED_WITH:
    domain:
      - PRODUCT
      - TECHNOLOGY
    range: PARTNER

  ENABLES:
    domain: TECHNOLOGY
    range:
      - PRODUCT
      - PERFORMANCE
      - APPLICATION

  HAS_PAIN_POINT:
    domain:
      - PRODUCT
      - SERVICE
      - APPLICATION
    range: PAIN_POINT

  BENCHMARKED_AGAINST:
    domain: PRODUCT
    range: COMPETITOR_PRODUCT

  HAS_COMMERCIAL_STATUS:
    domain:
      - PRODUCT
      - SERVICE
    range: STATUS

  SUPPORTED_BY_SOURCE:
    domain: ANY
    range: SOURCE

  GENERATES_OI_SEED:
    domain:
      - PRODUCT
      - PAIN_POINT
      - COMPETITOR_PRODUCT
    range: OI_SEED

  ADDRESSES:
    domain: OI_SEED
    range:
      - PAIN_POINT
      - PRODUCT_GAP

  DERIVED_FROM:
    domain:
      - ANALYSIS
      - OI_SEED
    range: SOURCE
```

---

## 8.4 Edge Evidence Properties

```yaml
edge_property_schema:

  edge_id:
    type: string
    required: true

  relation:
    type: controlled_vocabulary
    required: true

  source_ids:
    type: array
    required: true

  evidence_type:
    allowed_values:
      - OFFICIAL_DIRECT
      - OFFICIAL_INDIRECT
      - CUSTOMER_CONFIRMED
      - THIRD_PARTY_CONFIRMED
      - ANALYST_INFERENCE
      - HYPOTHESIS

  confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW

  temporal_status:
    allowed_values:
      - CURRENT
      - HISTORICAL
      - PLANNED
      - TARGET
      - UNKNOWN

  valid_from:
    type: date_or_period

  valid_to:
    type: date_or_period_or_null

  note:
    type: string
```

---
