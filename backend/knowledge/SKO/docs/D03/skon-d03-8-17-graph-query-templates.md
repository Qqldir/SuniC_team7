---
id: skon-d03-8-17-graph-query-templates
title: Graph Query Templates
summary: "SK온의 제품, 기술, 경쟁제품 등 다양한 엔티티를 그래프 데이터베이스에서 검색하기 위한 쿼리 템플릿 모음."
tags: [d03, product, schema]
keywords: [자연어 검색, 필터 조건, 관계도 순회, SK온 상품, 기술 벤치마크, 상용화 상태, OI 과제, 경쟁 분석, 그래프 데이터베이스, 경쟁제품 비교, 전고체 배터리, BaaS AI, 기술 역량, 자연언어 검색]
related: []
priority: normal
domain: D03
section: 8.17
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 504
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.17 Graph Query Templates

```yaml
graph_query_templates:

  - query_id: GQ-D03-001
    natural_language: SK온의 상용 제품만 보여줘.
    filters:
      company: SK On
      entity_type: PRODUCT
      commercial_status:
        - COMMERCIAL
        - CONTRACTED
        - VEHICLE_APPLICATION_CONFIRMED

  - query_id: GQ-D03-002
    natural_language: 양산이 확인되지 않은 제품은 무엇인가?
    filters:
      commercial_status:
        - PRE_COMMERCIAL
        - PROTOTYPE
        - EXPLORATORY
        - R_AND_D
        - CORPORATE_TARGET

  - query_id: GQ-D03-003
    natural_language: GRIDON에 적용된 안전기술과 경쟁제품을 연결해줘.
    start_node: PROD-SKON-ESS-002
    traverse:
      - USES_TECHNOLOGY
      - BENCHMARKED_AGAINST
      - HAS_PAIN_POINT

  - query_id: GQ-D03-004
    natural_language: Hyper Fast Battery의 상용화를 가로막을 수 있는 문제와 OI 과제를 보여줘.
    start_node: PROD-SKON-EV-006
    traverse:
      - HAS_PAIN_POINT
      - GENERATES_OI_SEED

  - query_id: GQ-D03-005
    natural_language: BaaS AI가 중고 전기차 시장에 어떻게 연결되는가?
    start_node: TECH-SKON-BAAS-AI
    traverse:
      - ESTIMATES
      - APPLIED_WITH
      - SUPPORTS_APPLICATION

  - query_id: GQ-D03-006
    natural_language: CATL TENER와 비교되는 SK온 제품은?
    start_node: COMP-CATL-ESS-001
    reverse_traverse:
      - BENCHMARKED_AGAINST

  - query_id: GQ-D03-007
    natural_language: 전고체 배터리에 필요한 외부 역량을 찾아줘.
    start_node: PROD-SKON-NEXT-002
    traverse:
      - HAS_PAIN_POINT
      - REQUIRES_CAPABILITY
      - POTENTIAL_PARTNER_TYPE
```

---
