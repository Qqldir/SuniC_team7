---
id: skes-d03-part-2-대표기업-심층-확장팩-상세-product-solution-r-3
title: Part 2. 대표기업 심층 확장팩 — 상세 Product/Solution Record Schema
summary: SK이노베이션의 제품·솔루션 정보를 관리하기 위한 표준 레코드 필드 구조와 각 필드의 정의
tags: [d03, product, core-candidate, schema]
keywords: [레코드 스키마, 필드 정의, 제품솔루션, 데이터 구조, 비즈니스 클러스터, 라이프사이클, 가치명제, KPI, 메타데이터]
related: []
priority: critical
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 337
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 15. 상세 Product/Solution Record Schema

각 레코드는 다음 필드를 재사용한다.

```yaml
record_schema:
  product_solution_id: canonical ID
  canonical_name: 표준명
  business_cluster: LNG | POWER | CITY_GAS | RENEWABLE | HYDROGEN | ENERGY_SOLUTION | CCS
  lifecycle_status: commercial | active_service | developing | planned | considering
  fact_class: disclosed_fact | structural_analysis | oi_hypothesis | undisclosed_gap
  value_proposition: 고객 또는 내부 운영조직이 얻는 가치
  user_customer: 고객·사용자 유형
  delivery_mechanism: 물리적 공급·계약·디지털·운영서비스 방식
  asset_dependency: 필요한 물리자산
  data_inputs: 운영·거래·고객 데이터
  decision_outputs: 계획·제어·정산·경보·보고
  kpi: 측정 가능한 성과지표
  pain_point_hypotheses: 내부 확인이 필요한 문제 후보
  oi_interfaces: 외부 기술·스타트업이 접속할 수 있는 지점
  governance_gates: 안전·규제·계약·보안·경제성 Gate
  source_ids: 근거 출처
```

---
