---
id: skes-d04-10-technology-evaluation-card
title: Technology Evaluation Card
summary: "기술의 역량 상태, 아키텍처 계층, 데이터 요구사항, 배포 검증 등을 정의하는 기술 평가 카드의 표준 템플릿 및 평가 항목 구조"
tags: [d04, technology, schema, "xref:d03"]
keywords: [capability_status, architecture_layer, deployment_gate, 기술평가, 데이터요구사항, KPI, OT사이버보안, 기술검증구조]
related: []
priority: normal
domain: D04
section: 10
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 335
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 10. Technology Evaluation Card

```yaml
technology_evaluation_card:
  technology_id: canonical
  technology_name: canonical
  linked_product_ids: [PS-ENS-*]
  linked_application_ids: [APP-ENS-*]
  linked_seed_ids: [SEED-ENS-D03-*]
  capability_status:
    - disclosed_owned_or_subsidiary
    - disclosed_operating
    - disclosed_planned
    - industry_reference_only
    - unknown
  architecture_layer:
    - sensor_edge
    - connectivity_data
    - model_analytics
    - optimization_control
    - workflow_application
    - governance_security
  data_requirement:
    source_system: DCS_SCADA_historian_CMS_CRM_GIS_market_contract
    frequency: static_batch_hourly_realtime
    label: required_optional
    sensitivity: public_internal_confidential_restricted
  output:
    - prediction
    - anomaly
    - recommendation
    - schedule
    - control_signal
    - settlement_or_report
  KPI:
    technical: accuracy_latency_reliability
    business: cost_revenue_availability_safety_cycle_time
  deployment_gate:
    - safety
    - OT_cyber
    - regulation
    - contract_IP_data_right
    - human_approval
  build_buy_partner:
    - reuse_owned
    - build
    - buy
    - partner
    - research
```
