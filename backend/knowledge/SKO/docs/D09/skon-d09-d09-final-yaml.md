---
id: skon-d09-d09-final-yaml
title: D09 Final YAML
summary: "SK온의 현재/미래 OEM 고객 포트폴리오, 배터리 공급 계약 현황 및 주요 갭을 구조화된 형식으로 정리한 D09 도메인 최종 설정 및 완료 상태 문서."
tags: [d09, customer, schema, "xref:d10"]
keywords: [메타데이터, 배터리 공급, EV 고객, 에너지저장, 용량 할당, 운영 갭, 계약 맵핑, 고객 통합, 미래 프로그램, OEM 고객, 고객 포트폴리오, 공급 계약, ESS, GWh, 계약갭]
related: []
priority: normal
domain: D09
section: ""
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 583
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09 Final YAML

```yaml
domain:
  domain_id: D09
  canonical_name: Customers, Orders and OEM Relationships
  company_id: CO-SKON
  version: 1.0
  reference_date: 2026-08-03
  status: CONDITIONALLY_COMPLETE_WITH_CONTRACT_AND_ALLOCATION_GAPS

registry:
  current_or_transition_customer_groups: 4
  future_OEM_customers: 2
  ESS_customers: 1
  agreement_records: 4
  pain_points: 12
  external_cases: 6
  oi_seeds: 14
  priority_poc_candidates: 5
  sources: 19

confirmed_current_customer_groups:
  - Hyundai_Motor_Group
  - Volkswagen_Group
  - Mercedes_Benz
  - Ford_CURRENT_TRANSITION

future_customer_programs:
  Nissan:
    total_supply: nearly_100_GWh
    period: 2028_to_2033
    production_site: UNKNOWN
  Slate:
    total_supply: approximately_20_GWh
    period: 2026_to_2031
    option_volume: UNKNOWN
    production_site: UNKNOWN

ess_customer_programs:
  Flatiron:
    contracted: 1_GWh
    preferential_pipeline: 6.2_GWh
    first_delivery_window: H2_2026

critical_gaps:
  - Customer-level revenue, GWh and margin concentration
  - Current program and plant mapping for Volkswagen and Mercedes-Benz
  - Post-restructuring Ford program and contract scope
  - Nissan and Slate plant nomination and annual drawdown
  - HSBMA line-level customer-qualified capacity
  - Flatiron shipment acceptance and 6.2GWh conversion
  - Claim and compensation customer attribution

d17_priority_handoff:
  - OI-D09-05 Customer-Qualified Capacity Graph
  - OI-D09-12 EV-to-ESS Customer-Mix Optimizer
  - OI-D09-01 Contract-to-Capacity Demand Bridge
  - OI-D09-10 ESS Pipeline Probability Engine
  - OI-D09-02 OEM Forecast Data Space

completion:
  domain_boundary: COMPLETE
  customer_and_relationship_model: COMPLETE
  public_customer_ledger: COMPLETE_WITH_GAPS
  demand_and_order_operating_model: COMPLETE
  pain_point_register: COMPLETE
  external_case_mapping: COMPLETE
  oi_portfolio: COMPLETE_PRELIMINARY
  d17_bridge: COMPLETE
  source_registry: COMPLETE
```

## D09 완료 상태

**완료:** `SK온 D09 Customers, Orders & OEM Relationships v1.0`

**다음 작업 지점:** `D10`
