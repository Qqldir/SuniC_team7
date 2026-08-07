---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-8-8
title: 011 — StoreDot — SK온 적용 가치 (8)
summary: "SK온의 전고체 배터리 기술경로, 파트너 협력 현황, 제조공정, 안전기술 등을 조회하기 위한 그래프 데이터베이스 쿼리 정의"
tags: [d04, technology, schema, table, "xref:d03"]
keywords: [그래프 쿼리, 전고체 배터리, 기술 파트너, 제조공정, 안전기술, 공동연구, 증거 성숙도, 품질 원인 추적, 셀 설계, AI Researcher, 기술 로드맵, 파트너 협력, 안전 기술, 기술 성숙도, AI 시스템]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3815
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
query_id: GQ-D04-006
natural_language: SK온의 전고체 배터리 기술경로를 소재·계면·공정별로 보여줘.

start_nodes:
  - TECH-SKON-D04-001
  - TECH-SKON-D04-065

traversals:
  - HAS_MATERIAL_COMPONENT
  - REQUIRES
  - IMPROVED_BY
  - PILOT_TECHNOLOGY_PARTNER
  - SUPPORTED_BY_SOURCE

answer_mode: FACT_ONLY
```

---

## GQ-D04-007 — 전고체 파트너 비교

```yaml
query_id: GQ-D04-007
natural_language: Solid Power와 Factorial의 SK온 협력범위와 상태를 비교해줘.

start_nodes:
  - PART-SOLID-POWER
  - PART-FACTORIAL

traversals:
  - CONNECTED_TO_TECHNOLOGY
  - HAS_RELATION_STATUS
  - SUPPORTED_BY_SOURCE

mandatory_labels:
  - ACTIVE_TECHNOLOGY_TRANSFER
  - FEASIBILITY_MOU

answer_mode: PARTNER_MAPPING
```

---

## GQ-D04-008 — 제품별 제조공정

```yaml
query_id: GQ-D04-008
natural_language: 특정 제품을 만들기 위해 필요한 핵심 제조공정을 연결해줘.

start_nodes:
  - USER_SELECTED_PRODUCT

traversals:
  - USES_TECHNOLOGY
  - USES_PROCESS
  - REQUIRES_PROCESS
  - HAS_CRITICAL_QUALITY_ATTRIBUTE

answer_mode: FACT_AND_ANALYSIS
```

---

## GQ-D04-009 — 안전기술 계층

```yaml
query_id: GQ-D04-009
natural_language: 셀 내부단락부터 팩 열전파까지 SK온의 안전기술을 계층별로 정리해줘.

start_nodes:
  - TECH-SKON-D04-021

traversals:
  - HAS_CHILD_TECHNOLOGY
  - SUPPORTS
  - PREVENTS
  - DETECTS
  - ENABLES_RESPONSE

answer_mode: FACT_AND_ANALYSIS
```

---

## GQ-D04-010 — AI Researcher 구조

```yaml
query_id: GQ-D04-010
natural_language: AI Researcher가 고객 요구에서 셀 설계안까지 어떻게 작동하는가?

start_nodes:
  - TECH-SKON-D04-032

traversals:
  - HAS_COMPONENT
  - RECEIVES_INPUT
  - GENERATES
  - PREDICTS
  - ESTIMATES
  - REQUIRES_HUMAN_APPROVAL

answer_mode: FACT_ONLY
```

---

## GQ-D04-011 — 분석 목표역량 제외

```yaml
query_id: GQ-D04-011
natural_language: 공식적으로 확인된 SK온 기술만 보여줘.

filters:
  ownership_scope:
    excluded:
      - ANALYTICAL_TARGET

  evidence_scope:
    excluded:
      - ANALYSIS
      - HYPOTHESIS

excluded_nodes:
  - TECH-SKON-D04-038
  - TECH-SKON-D04-042
  - TECH-SKON-D04-044
  - TECH-SKON-D04-064
  - TECH-SKON-D04-073
  - TECH-SKON-D04-078

answer_mode: FACT_ONLY
```

---

## GQ-D04-012 — 기술별 EML

```yaml
query_id: GQ-D04-012
natural_language: 기술별 공개근거 성숙도를 비교해줘.

traversals:
  - HAS_EVIDENCE_MATURITY_LEVEL
  - SUPPORTED_BY_SOURCE
  - HAS_COMMERCIAL_STATUS

sort:
  - evidence_maturity_level_descending

answer_mode: FACT_ONLY
```

---

## GQ-D04-013 — 대학 공동연구

```yaml
query_id: GQ-D04-013
natural_language: SK온이 대학과 공동 연구한 기술과 성과를 보여줘.

start_nodes:
  - PART-SEOUL-NATIONAL-UNIV
  - PART-HANYANG-UNIV
  - PART-YONSEI-UNIV
  - PART-DANKOOK-UNIV
  - PART-KICET
  - PART-UT-RESEARCH

traversals:
  - RESEARCHED_WITH
  - PRODUCED_RESEARCH_RESULT
  - SUPPORTED_BY_SOURCE

answer_mode: PARTNER_MAPPING
```

---

## GQ-D04-014 — 제조 품질 원인 추적

```yaml
query_id: GQ-D04-014
natural_language: 특정 셀 결함의 가능한 공정원인을 역추적해줘.

start_nodes:
  - USER_SELECTED_DEFECT

reverse_traversals:
  - CAN_CAUSE
  - HAS_CRITICAL_PROCESS_PARAMETER
  - USES_EQUIPMENT
  - GENERATED_FROM_MATERIAL_LOT

answer_mode: GAP_ANALYSIS
```

`CAN_CAUSE`는 인과관계가 확인되지 않은 경우 `POSSIBLE_CAUSE`로 표시하며, 실제 SK온 불량원인으로 단정하지 않는다.

---

## GQ-D04-015 — 외부 벤치마크

```yaml
query_id: GQ-D04-015
natural_language: SK온 기술과 직접 비교할 외부기업 기술을 찾아줘.

start_nodes:
  - USER_SELECTED_SKON_TECHNOLOGY

traversals:
  - BENCHMARKED_AGAINST
  - HAS_VALIDATION_EVIDENCE
  - HAS_MANUFACTURING_STRATEGY
  - HAS_RELATIONSHIP_WITH_SKON

answer_mode: FACT_AND_ANALYSIS
```

---

## GQ-D04-016 — OI 과제 생성

```yaml
query_id: GQ-D04-016
natural_language: 특정 기술의 Pain Point에서 Open Innovation 과제후보를 생성해줘.

start_nodes:
  - USER_SELECTED_TECHNOLOGY

traversals:
  - HAS_PAIN_POINT
  - REQUIRES_CAPABILITY
  - MATCHED_WITH_EXTERNAL_TECHNOLOGY
  - MATCHED_WITH_PARTNER
  - GENERATES_OI_SEED

answer_mode: OI_DISCOVERY
```

---

## GQ-D04-017 — 회사 주장 분리

```yaml
query_id: GQ-D04-017
natural_language: 독립적으로 검증되지 않은 회사 성능주장만 분리해줘.

filters:
  claim_status:
    - MANUFACTURER_CLAIM
    - CORPORATE_TARGET

traversals:
  - SUPPORTED_BY_SOURCE
  - HAS_TEST_BOUNDARY

answer_mode: FACT_ONLY
```

---

## GQ-D04-018 — D03·D04 교차검색

```yaml
query_id: GQ-D04-018
natural_language: 제품별 핵심기술·공정·성숙도·파트너를 한 번에 보여줘.

start_nodes:
  - USER_SELECTED_PRODUCT

traversals:
  - USES_TECHNOLOGY
  - USES_PROCESS
  - CO_DEVELOPED_WITH
  - HAS_EVIDENCE_MATURITY_LEVEL
  - HAS_COMMERCIAL_STATUS
  - HAS_PAIN_POINT

answer_mode: FACT_AND_ANALYSIS
```

---

## 52.2 Graph Answer-Control Rules

```yaml
graph_answer_control:

  source_requirement:
    rule: >
      FACT 관계는 하나 이상의 source_id를 가져야 한다.

  analytical_edge_requirement:
    rule: >
      ANALYSIS 또는 HYPOTHESIS 관계는 basis_entity_ids 또는
      basis_triple_ids를 가져야 한다.

  may_use_rule:
    rule: >
      MAY_USE는 실제 제품 적용이 아니라 적용가능성으로 출력한다.

  partner_status_rule:
    rule: >
      MOU, 공동개발, 기술이전, 공급계약을 서로 다른 상태로 출력한다.

  manufacturer_claim_rule:
    rule: >
      기업 자체 시험수치는 제조사 주장 또는 회사 시험결과로 표시한다.

  future_target_rule:
    rule: >
      목표연도와 목표성능에는 CORPORATE_TARGET 표기를 붙인다.

  ownership_rule:
    rule: >
      SKIET, SK엔무브와 외부기업 기술을 SK온 단독 보유기술로 표현하지 않는다.

  analytical_target_rule:
    rule: >
      EML_NA 엔티티는 사용자가 미래전략·OI를 묻지 않는 한
      현재 보유기술 목록에서 제외한다.
```

---

# D04-53. Human-Readable Technology Report

## 53.1 Executive Summary

SK온의 기술 포트폴리오는 단순히 셀 화학기술에 한정되지 않는다. 공개근거를 기준으로 보면 SK온의 기술체계는 다음 다섯 층으로 구분된다.

```text
1. 소재·전기화학
   ├─ 하이니켈 NCM
   ├─ 미드니켈
   ├─ LFP
   ├─ 실리콘 음극
   └─ 전고체·리튬메탈

2. 셀·팩 설계
   ├─ 파우치
   ├─ On-Vent 각형
   ├─ 파우치 통합 각형
   ├─ CTP
   └─ S-Pack+

3. 성능·안전
   ├─ SF·SUFast
   ├─ 열전파 방지
   ├─ 대면적·액침냉각
   ├─ EIS 진단
   └─ 무선 BMS

4. 제조
   ├─ 건식전극
   ├─ Z-Folding
   ├─ 레이저 가공
   ├─ 포메이션·검사
   └─ 지능형 생산설비

5. 디지털·서비스
   ├─ AI Researcher
   ├─ 공정 AI
   ├─ 제조 디지털 트윈
   ├─ BaaS AI
   └─ SOH·RUL·잔존가치
```

상용화 근거가 가장 강한 영역은 하이니켈 NCM, 파우치 셀, Z-Folding과 기존 SF 급속충전 제품이다. 제품에 통합되거나 파트너 서비스로 검증된 기술에는 EIS 기반 ESS 진단, BaaS AI, GRIDON 안전기술과 AI Researcher가 포함된다.

반면 Hyper Fast, 각형 플랫폼, S-Pack+, EV 액침냉각, 무선 BMS와 건식전극은 시제품·개발·파일럿 단계다. 전고체는 Solid Power 기술을 적용한 파일럿 라인과 Factorial 제조 타당성 검토까지 진행됐지만, 상용차량·실명 고객샘플·양산공장과 양산수율은 공개적으로 확인되지 않았다.

---

## 53.2 핵심 기술강점

```yaml
technology_strengths:

  commercial_core:
    - High-Nickel NCM
    - Pouch Cell Manufacturing
    - Z-Folding
    - SF Fast-Charging Product Lineage

  differentiated_development:
    - SUFast electrode-protocol co-design
    - Magnetic alignment
    - On-Vent laser structure
    - Pouch-integrated prismatic architecture
    - Large-surface cooling

  ess_and_safety:
    - EIS-Based BMS
    - Coolant-based ESS safety
    - Flexible DC and AC block architecture
    - Multi-layer abnormality-detection concept

  digital:
    - AI Researcher
    - AI calendering
    - Manufacturing digital-twin cooperation
    - BaaS lifecycle analytics

  next_generation:
    - Solid Power pilot-line technology access
    - Polymer-oxide and sulfide dual-track research
    - Lithium-metal interface research
    - LLZO, LMRO and single-crystal cathode research
```

---

## 53.3 핵심 기술격차

```yaml
critical_technology_gaps:

  product_validation:
    - Hyper Fast commercial vehicle reference
    - Prismatic OEM validation
    - CTP mass-production and rework evidence
    - Wireless BMS automotive qualification

  manufacturing:
    - Dry-electrode first-pass yield
    - Inline porosity and adhesion measurement
    - High-speed internal defect inspection
    - Formation time and energy reduction
    - Process-to-field genealogy

  ess:
    - Public GRIDON absolute system specification
    - Long-term field availability
    - Warranty and degradation analytics
    - PCS and EMS interoperability

  digital:
    - AI prediction accuracy and uncertainty
    - Closed experiment loop for Materials AI
    - Cross-factory AI model transfer
    - Battery passport and data ownership

  solid_state:
    - Pilot yield
    - Sulfide electrolyte cost and H2S control
    - Solid-solid interface inspection
    - Lightweight pressure management
    - Named automotive evaluation program
```

---

## 53.4 Open Innovation 우선영역

D04에서 공식 등록된 OI Seed는 총 47건이며, 이를 기술적으로 통합하면 다음 여덟 개의 상위 프로그램으로 묶을 수 있다.

| 상위 OI 프로그램                     | 포함 기술                       |   우선도 |
| ------------------------------ | --------------------------- | ----: |
| 전고체 플랫폼 선정·차량검증                | Solid Power·Factorial·계면·압력 | 매우 높음 |
| 건식전극 양산 가속                     | 분말·코팅·캘린더링·검사               | 매우 높음 |
| Hyper Fast 상용검증                | 실리콘 음극·SUFast·열관리           | 매우 높음 |
| 차세대 ESS 안전·보증                  | EIS·가스센서·냉각·열화분석            | 매우 높음 |
| 멀티폼팩터 양산                       | 각형·CTP·On-Vent·조립검사         | 매우 높음 |
| AI 기반 R&D 자동화                  | AI Researcher·소재AI·실험자동화    |    높음 |
| Gigafactory Digital Thread     | 설비·공정·검사·필드 데이터             | 매우 높음 |
| Battery Lifecycle Intelligence | SOH·RUL·잔존가치·여권             |    높음 |

---

## 53.5 종합 판단

**FACT**

SK온은 하이니켈 파우치 배터리와 Z-Folding을 기반으로 한 상용기술을 보유하며, 급속충전·ESS·전고체·건식전극·AI R&D와 다중 폼팩터로 기술영역을 확장하고 있다.

**ANALYSIS**

현재 SK온의 주요 과제는 새로운 기술을 더 많이 추가하는 것보다 이미 공개된 기술을 고객검증·양산수율·필드운영 데이터로 연결하는 것이다. 특히 전고체, 각형, Hyper Fast와 건식전극은 기술 존재보다 `공통 시험기준`, `고객 샘플`, `파일럿 수율`, `기존 라인 전환비용`이 의사결정에 더 중요하다.

**HYPOTHESIS**

Solid Power·Factorial·자체 전고체 플랫폼을 동일한 셀 규격과 경제성 기준으로 비교하고, 차량실증까지 연결할 경우 SK온은 분산된 차세대 기술개발을 하나의 상용화 의사결정 체계로 전환할 수 있다.

---

# D04-54. Data Quality & Gap Register

## 54.1 Overall Quality Status

```yaml
data_quality_summary:

  domain_id: D04
  overall_status: CONDITIONALLY_COMPLETE

  technology_taxonomy_quality: HIGH
  product_technology_linkage: HIGH
  source_traceability: HIGH
  commercial_status_integrity: HIGH
  quantitative_performance_coverage: MEDIUM_LOW
  partner_status_integrity: HIGH
  manufacturing_specificity: MEDIUM_LOW
  machine_export_validation: PENDING
```

---

## DQ-D04-001 — Source Duplicate Records
