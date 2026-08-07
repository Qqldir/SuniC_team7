---
id: skon-d07-d07-dq-003-site-product-mapping-evidence-correc
title: 003. Site–Product Mapping Evidence Correction
summary: 배터리 공장의 제품·고객 정보 신뢰도 분류 기준과 데이터 검증 규칙을 규정하는 문서.
tags: [d07, footprint, schema]
keywords: [Plant-Customer Mapping, Product Chemistry, Manufacturing footprint, 생산 근거 수준, OEM 공급 관계, Evidence level, Source ID 정규화, 배터리 생산 확인, 공장-제품-고객 매핑, 신뢰도 분류 체계, 데이터 검증 기준, 배터리 화학성, 생산라인, OEM 공급처, 공식자료 근거, 증거 등급, 기술적 가능성]
related: []
priority: normal
domain: D07
section: D07-DQ
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 879
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# SK온 D07 Manufacturing Footprint, Plants & Capacity

## Part 2. Site·Line·Product·Customer Mapping·Conversion Flexibility·Capacity Redundancy

**문서 버전:** D07 v1.1
**기준일:** 2026-08-02
**이전 완료 지점:** `D07-09 Initial Manufacturing Footprint OI Seeds`

---

# D07-DQ-003. Site–Product Mapping Evidence Correction

## 1. 공개 링크·Source ID 정규화

이전 구간의 원문 URL 표시는 비정규 표현으로 간주하고, 이후 데이터베이스에서는 `source_id`와 인라인 근거 인용으로 대체한다.

```yaml
source_presentation_rule:

  canonical:
    - Internal source ID
    - Publisher
    - Publication date
    - Source grade
    - Evidence level
    - Web citation

  non_canonical:
    - Raw URL embedded in plant record
    - Tracking parameter
    - Search-result URL treated as source metadata
```

---

## 2. Plant–Customer Mapping 수준

```yaml
plant_customer_mapping_levels:

  DIRECT_SITE_MODEL:
    definition: >
      공식자료가 특정 공장과 특정 완성차 모델을 직접 연결
    permitted_statement:
      - The plant supplies the specified model

  DIRECT_SITE_OEM:
    definition: >
      특정 공장이 특정 OEM 또는 OEM 그룹에 공급한다고 직접 확인
    permitted_statement:
      - The plant supplies the specified OEM group

  DIRECT_COMPANY_MODEL:
    definition: >
      SK온이 특정 모델에 배터리를 공급하지만 생산공장은 미공개
    permitted_statement:
      - SK On supplies the model
    prohibited_statement:
      - Assign the model to a specific plant

  REGIONAL_TECHNICAL_MATCH:
    definition: >
      공장 위치·생산시기·고객공장 위치를 바탕으로 기술적 가능성만 존재
    evidence_level: ANALYST_INFERENCE

  UNRESOLVED:
    definition: >
      공개자료만으로 고객·모델·라인을 연결할 수 없음
```

**회사 차원의 고객관계를 특정 공장에 자동 배정하지 않는다.** 또한 한 공장이 특정 모델에 공급했다는 과거 근거가 있어도 2026년 현재 동일 라인에서 계속 생산한다는 뜻은 아니다.

---

## 3. Product·Chemistry Mapping 수준

```yaml
plant_product_mapping_levels:

  DIRECT_CURRENT_PRODUCTION:
    - Current commercial production is directly confirmed

  DIRECT_HISTORICAL_PRODUCTION:
    - Past production or supply is directly confirmed
    - Current continuation requires revalidation

  OFFICIAL_FUTURE_PLAN:
    - Company announced future production
    - Production has not yet been confirmed

  DEVELOPMENT_OR_OPTIONALITY:
    - Plant or company is positioned for a market
    - Equipment qualification is not confirmed

  ANALYTICAL_CONVERSION_CANDIDATE:
    - Conversion appears technically possible
    - No public implementation evidence

  UNRESOLVED:
    - Product, chemistry or line allocation is not public
```

---
