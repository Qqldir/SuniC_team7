---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-7-7
title: 011 — StoreDot — SK온 적용 가치 (7)
summary: "SK온이 추진하는 디지털 트윈, 전고체, 폴리머-산화물 복합전해질, 리튬메탈 등 차세대 배터리 기술 개발 현황과 국제 협력 사례를 설명한다."
tags: [d04, technology, schema]
keywords: [전고체 배터리, 황화물 ASSB, 디지털 트윈, 폴리머 전해질, 리튬메탈 음극, Solid Power, 스마트팩토리, 파일럿 라인, 스마트 팩토리, 황화물 전해질, 복합전해질, SIPE, 리튬메탈, 인공계면, 국제 협력]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3760
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

```yaml
chunk_id: CH-SKON-D04-017
title: 제조 디지털 트윈·지능형 설비
information_type: FACT
evidence_scope: OFFICIAL_DIRECT
maturity_status: PARTNERSHIP_AND_VALIDATION
evidence_maturity_level: EML_6

chunk_text: >
  SK온은 Siemens DISW와 배터리 제조 디지털 트윈 협력을 추진했고,
  Beckhoff, Cisco, IFM, Yaskawa와 우원기술 등과 제어기·센서·통신·
  로봇·설비 지능화를 검증했다. 협력 사실은 확인되지만 전 공장 배포,
  수율향상과 램프업 단축의 정량성과는 공개되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-040
  - TECH-SKON-D04-041

partner_ids:
  - PART-SIEMENS-DISW
  - PART-BECKHOFF
  - PART-CISCO
  - PART-IFM
  - PART-YASKAWA
  - PART-WOOWON

source_ids:
  - SRC-SKON-D04-031
  - SRC-SKON-D04-032
  - SRC-SKON-D04-038

source_grades:
  - A

confidence: HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 디지털 트윈
  - 스마트 팩토리
  - OT
  - 설비 지능화
  - 가상 시운전

exclusions:
  - 글로벌 전 공장에 완성 플랫폼이 구축됐다고 표현 금지
```

---

## CH-SKON-D04-018 — Sulfide ASSB

```yaml
chunk_id: CH-SKON-D04-018
title: 황화물계 전고체 셀·전해질 플랫폼
information_type: FACT
evidence_scope: PARTNER_CONFIRMED
maturity_status: PILOT_VALIDATION
evidence_maturity_level: EML_6

chunk_text: >
  SK온은 황화물계 고체전해질과 전고체 셀을 개발하며 Solid Power의
  셀 설계·공정기술과 전해질을 활용한 파일럿 라인을 구축했다.
  Solid Power는 SK온 파일럿 셀 라인의 현장인수시험 완료를 발표했다.
  황화물 기술은 높은 이온전도와 전극 접촉성이 장점이지만 수분,
  H2S, 계면반응과 압력관리 문제가 남아 있다.

primary_entity_ids:
  - TECH-SKON-D04-001
  - TECH-SKON-D04-069
  - TECH-SKON-D04-072
  - TECH-SKON-D04-073

partner_ids:
  - PART-SOLID-POWER

source_ids:
  - SRC-SKON-D04-042
  - SRC-EXT-D04-052

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 황화물 전고체
  - Solid Power
  - 파일럿 라인
  - H2S
  - 고체-고체 계면

exclusions:
  - 상용화 완료 또는 고객차량 적용으로 표현 금지
```

---

## CH-SKON-D04-019 — Polymer–Oxide·SIPE

```yaml
chunk_id: CH-SKON-D04-019
title: 폴리머-산화물 복합전해질과 SIPE
information_type: FACT
evidence_scope: PEER_REVIEWED
maturity_status: LAB_AND_PILOT_DEVELOPMENT
evidence_maturity_level: EML_4

chunk_text: >
  폴리머-산화물 복합전해질은 폴리머의 유연성과 산화물의 안정성을
  결합해 기존 생산공정과 전고체 기술 사이의 브리지 역할을 목표로 한다.
  SIPE는 리튬이온 전달수를 높여 농도분극과 리튬메탈 계면 불균일을
  줄이는 연구기술이다. 상온 연구결과는 공개됐지만 대형셀과 양산필름은
  검증되지 않았다.

primary_entity_ids:
  - TECH-SKON-D04-065
  - TECH-SKON-D04-066
  - TECH-SKON-D04-067

source_ids:
  - SRC-SKON-D04-042
  - SRC-SKON-D04-043
  - SRC-SKON-D04-044

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 폴리머 산화물
  - SIPE
  - LLZO
  - 고분자 전해질
  - 리튬 전달수

exclusions:
  - 연구셀 수치를 상용 셀 사양으로 표현 금지
```

---

## CH-SKON-D04-020 — Lithium-Metal Interface

```yaml
chunk_id: CH-SKON-D04-020
title: 리튬메탈 음극과 인공계면
information_type: FACT
evidence_scope: PEER_REVIEWED
maturity_status: LAB_VALIDATION
evidence_maturity_level: EML_4

chunk_text: >
  리튬메탈은 높은 용량과 낮은 전위를 갖지만 덴드라이트, 데드리튬,
  계면 공극과 반복적인 보호층 파괴가 문제다. SK온·한양대학교 연구는
  리튬 표면의 저항층을 제거하고 이온전도성·기계적 안정성을 가진
  인공계면을 형성해 특정 연구셀에서 300회 사이클을 보고했다.

primary_entity_ids:
  - TECH-SKON-D04-070
  - TECH-SKON-D04-071

partner_ids:
  - PART-HANYANG-UNIV

source_ids:
  - SRC-SKON-D04-046
  - SRC-RES-D04-047

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - 리튬메탈
  - 인공 SEI
  - 덴드라이트
  - 표면개질
  - 전고체

exclusions:
  - 300회를 대형 양산셀 수명으로 일반화 금지
```

---

## CH-SKON-D04-021 — Next-Generation Cathodes

```yaml
chunk_id: CH-SKON-D04-021
title: LMRO와 초고니켈 대형 단결정 양극
information_type: FACT
evidence_scope: PEER_REVIEWED
maturity_status: LAB_VALIDATION
evidence_maturity_level: EML_3

chunk_text: >
  SK온은 망간 비중이 높은 LMRO 단결정과 니켈 94% 초과의 대형
  단결정 양극을 연구하고 있다. LMRO는 원가경쟁력이 있지만 산소방출과
  전압저하가 문제이며, 초고니켈 단결정은 입계균열을 줄일 가능성이
  있으나 합성균일성, 열안정성과 고밀도 캘린더링 수율이 과제다.

primary_entity_ids:
  - TECH-SKON-D04-074
  - TECH-SKON-D04-075

partner_ids:
  - PART-SEOUL-NATIONAL-UNIV

source_ids:
  - SRC-SKON-D04-045
  - SRC-RES-D04-049
  - SRC-RES-D04-051

source_grades:
  - A

confidence: VERY_HIGH
claim_status: VERIFIED_FACT

embedding_tags:
  - LMRO
  - 초고니켈
  - 단결정
  - 산소방출
  - 입자균열

exclusions:
  - 상용 양극재 포트폴리오로 표현 금지
```

---

## CH-SKON-D04-022 — External Solid-State Partners

```yaml
chunk_id: CH-SKON-D04-022
title: Solid Power·Factorial 전고체 협력
information_type: MIXED
evidence_scope: PARTNER_CONFIRMED
maturity_status: PARTNER_PROGRAM
evidence_maturity_level: EML_6

chunk_text: >
  Solid Power 협력은 황화물 전해질, 셀 설계와 파일럿 공정이전으로
  연결돼 있으며, Factorial 협력은 FEST 기술을 SK온의 기존
  리튬이온 생산 인프라에서 제조할 가능성을 평가하는 비구속 MOU다.
  두 협력은 각각 소재·공정 확보와 기존라인 호환성 검토라는 다른
  상용화 옵션으로 분석할 수 있다.

primary_entity_ids:
  - TECH-SKON-D04-001
  - TECH-SKON-D04-069

partner_ids:
  - PART-SOLID-POWER
  - PART-FACTORIAL

source_ids:
  - SRC-EXT-D04-052
  - SRC-EXT-D04-053

source_grades:
  - A

confidence: HIGH
claim_status: ANALYST_INFERENCE

embedding_tags:
  - Solid Power
  - Factorial
  - FEST
  - 기술이전
  - 제조 호환성

exclusions:
  - Factorial MOU를 공급계약·기술이전으로 표현 금지
```

---

## CH-SKON-D04-023 — Evidence Maturity

```yaml
chunk_id: CH-SKON-D04-023
title: D04 Evidence Maturity Level 해석
information_type: ANALYSIS
evidence_scope: ANALYTICAL_INTEGRATION
maturity_status: GOVERNANCE_RULE
evidence_maturity_level: EML_NA

chunk_text: >
  D04의 EML은 국제표준 TRL이 아니라 공개근거의 수준을 나타내는
  내부 분류다. 상용제품은 EML 9, 제품통합은 EML 8, 시스템 시연은
  EML 7, 파일럿은 EML 6, 시제품은 EML 5, 연구셀은 EML 3~4로
  관리한다. 목표기술과 분석 아키텍처는 EML N/A로 분리한다.

primary_entity_ids:
  - D04-EML-VOCABULARY

source_ids:
  - D04-INTERNAL-GOVERNANCE

source_grades:
  - A

confidence: VERY_HIGH
claim_status: ANALYST_INFERENCE

embedding_tags:
  - EML
  - 기술성숙도
  - TRL
  - 증거수준
  - 상용화 상태
```

---

## CH-SKON-D04-024 — Analytical Target Technologies

```yaml
chunk_id: CH-SKON-D04-024
title: 공식 보유기술이 아닌 분석 목표역량
information_type: ANALYSIS
evidence_scope: ANALYTICAL_INTEGRATION
maturity_status: ANALYTICAL_TARGET
evidence_maturity_level: EML_NA

chunk_text: >
  Battery Foundation Model, Predictive Quality Intelligence,
  Battery Operational Digital Twin, Manufacturing Digital Thread,
  고압 스택 관리와 프리리치에이션은 현재 동일 명칭의 SK온 완성
  플랫폼으로 확인되지 않았다. 이들은 기존 기술과 데이터의 연결을
  위해 D17에서 검토할 목표역량 또는 외부협력 후보로만 사용한다.

primary_entity_ids:
  - TECH-SKON-D04-038
  - TECH-SKON-D04-042
  - TECH-SKON-D04-044
  - TECH-SKON-D04-064
  - TECH-SKON-D04-073
  - TECH-SKON-D04-078

source_ids:
  - D04-ANALYSIS-REGISTRY

source_grades:
  - A

confidence: VERY_HIGH
claim_status: ANALYST_INFERENCE

embedding_tags:
  - 분석 목표역량
  - 파운데이션 모델
  - 디지털 스레드
  - 프리리치에이션
  - 운용 디지털 트윈

exclusions:
  - 현재 SK온 보유·운영기술로 답변 금지
```

---

## 51.2 Chunk Retrieval Priority

```yaml
chunk_retrieval_priority:

  priority_1:
    condition: 사용자가 현재 보유·상용기술을 질문
    filters:
      information_type:
        - FACT
      evidence_maturity_level:
        - EML_9
        - EML_8
        - EML_7

  priority_2:
    condition: 개발 중 기술을 질문
    filters:
      evidence_maturity_level:
        - EML_6
        - EML_5
        - EML_4
        - EML_3
    required_output:
      - 개발단계 표시
      - 고객·양산 근거 표시

  priority_3:
    condition: 미래기술·협력기회를 질문
    filters:
      information_type:
        - ANALYSIS
        - HYPOTHESIS
    required_output:
      - 공식 보유기술과 분리
      - 검증 필요사항 표시

  prohibited_retrieval_behavior:
    - EML_NA 기술을 현재 상용기술 답변에 포함
    - MANUFACTURER_CLAIM을 독립검증값으로 변환
    - MAY_USE 관계를 실제 제품 BOM으로 변환
    - CORPORATE_TARGET을 완료실적으로 변환
```

---

# D04-52. Graph Query Templates

## 52.1 Query Schema

```yaml
graph_query_schema:

  query_id:
    type: canonical_string

  natural_language:
    type: string

  start_nodes:
    type: array

  filters:
    type: object

  traversals:
    type: ordered_array

  excluded_edge_types:
    type: array

  answer_mode:
    allowed_values:
      - FACT_ONLY
      - FACT_AND_ANALYSIS
      - OI_DISCOVERY
      - GAP_ANALYSIS
      - PARTNER_MAPPING

  mandatory_labels:
    type: array
```

---

## GQ-D04-001 — 현재 상용 핵심기술

```yaml
query_id: GQ-D04-001
natural_language: SK온이 현재 상용화한 핵심 배터리 기술은 무엇인가?

filters:
  evidence_maturity_level:
    - EML_9
    - EML_8
  evidence_scope:
    - OFFICIAL_DIRECT

excluded_edge_types:
  - MAY_USE
  - POTENTIALLY_SUPPORTS
  - HYPOTHESIS

answer_mode: FACT_ONLY
```

---

## GQ-D04-002 — 개발·연구단계 기술

```yaml
query_id: GQ-D04-002
natural_language: 아직 양산되지 않은 SK온 기술을 단계별로 보여줘.

filters:
  evidence_maturity_level:
    - EML_6
    - EML_5
    - EML_4
    - EML_3

traversals:
  - HAS_COMMERCIAL_STATUS
  - SUPPORTED_BY_SOURCE

mandatory_labels:
  - maturity_status
  - customer_status
  - mass_production_status

answer_mode: FACT_ONLY
```

---

## GQ-D04-003 — Hyper Fast 기술체인

```yaml
query_id: GQ-D04-003
natural_language: Hyper Fast Battery의 핵심기술과 상용화 병목을 연결해줘.

start_nodes:
  - PROD-SKON-EV-006

traversals:
  - ENABLED_BY
  - HAS_ALGORITHM_COMPONENT
  - USES_TECHNOLOGY
  - HAS_PAIN_POINT
  - REQUIRES_CAPABILITY
  - GENERATES_OI_SEED

answer_mode: GAP_ANALYSIS
```

---

## GQ-D04-004 — GRIDON 안전기술

```yaml
query_id: GQ-D04-004
natural_language: GRIDON에 적용된 진단·화재대응 기술과 미공개 정보를 정리해줘.

start_nodes:
  - PROD-SKON-ESS-002
  - PROD-SKON-ESS-003

traversals:
  - USES
  - HAS_ARCHITECTURE
  - HAS_PAIN_POINT
  - SUPPORTED_BY_SOURCE

answer_mode: FACT_AND_ANALYSIS
```

---

## GQ-D04-005 — 건식전극 병목

```yaml
query_id: GQ-D04-005
natural_language: SK온 건식전극의 양산 병목과 필요한 외부역량은?

start_nodes:
  - TECH-SKON-D04-003

traversals:
  - HAS_PROCESS_COMPONENT
  - OPTIMIZED_BY
  - HAS_PAIN_POINT
  - REQUIRES_CAPABILITY
  - GENERATES_OI_SEED

answer_mode: OI_DISCOVERY
```

---

## GQ-D04-006 — 전고체 기술 경로
