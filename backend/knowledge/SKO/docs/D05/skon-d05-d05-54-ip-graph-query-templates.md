---
id: skon-d05-d05-54-ip-graph-query-templates
title: IP Graph Query Templates
summary: "특허, 기술, 제품 간의 IP 관계를 그래프로 조회하는 11개 쿼리 템플릿. 권리추적·포트폴리오갭분석·FTO리스크 평가 등 특허 조회 시나리오별 쿼리 정의."
tags: [d05, rnd, schema, "xref:d04"]
keywords: [특허 쿼리, IP 그래프, 기술 매핑, 권리이전 추적, FTO 위험, White Space 분석, 지식재산 포트폴리오, 공동출원, 특허 조회, IP 매핑, 기술-특허 연결, 그래프 쿼리, 발명자-저자 네트워크, 포트폴리오 갭, FTO 리스크, 데이터 품질]
related: []
priority: normal
domain: D05
section: D05-54.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1974
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-54. IP Graph Query Templates

## GQ-D05-001 — 기술별 특허군

```yaml
query_id: GQ-D05-001
natural_language: 특정 SK온 기술과 연결되는 특허군을 보여줘.

start_nodes:
  - USER_SELECTED_TECHNOLOGY

traversals:
  - SUPPORTED_BY_PATENT
  - CLAIMS_TECHNICAL_ELEMENT
  - HAS_LEGAL_STATUS
  - OWNED_BY

answer_mode: FACT_AND_STATUS
```

## GQ-D05-002 — 제품별 특허 연결

```yaml
query_id: GQ-D05-002
natural_language: 특정 제품과 기술적으로 연결되는 특허군을 보여줘.

start_nodes:
  - USER_SELECTED_PRODUCT

traversals:
  - USES_TECHNOLOGY
  - TECHNICALLY_LINKED_TO_PATENT
  - HAS_MAPPING_CONFIDENCE

mandatory_labels:
  - DIRECT_PUBLIC_IMPLEMENTATION
  - STRONG_TECHNICAL_MATCH
  - SUPPORTING_PLATFORM_IP
  - RESEARCH_IP_ONLY
```

## GQ-D05-003 — 권리이전 추적

```yaml
query_id: GQ-D05-003
natural_language: SK이노베이션에서 SK온으로 이전된 특허를 보여줘.

start_nodes:
  - APP-SKI-001

traversals:
  - ORIGINAL_APPLICANT_OF
  - TRANSFERRED_TO
  - CURRENT_OWNER_OF

answer_mode: OWNERSHIP_TRACE
```

## GQ-D05-004 — 공식 상태 미검증 특허

```yaml
query_id: GQ-D05-004
natural_language: 공식 등록부 검증이 필요한 특허군을 보여줘.

filters:
  official_register_status:
    - PENDING
    - NOT_AUDITED
    - REQUIRES_RETRIEVAL
    - UNCONFIRMED

answer_mode: DATA_QUALITY
```

## GQ-D05-005 — 논문·특허 연결

```yaml
query_id: GQ-D05-005
natural_language: 특정 논문과 연결되는 특허와 기술을 보여줘.

start_nodes:
  - USER_SELECTED_PAPER

traversals:
  - VALIDATES_TECHNOLOGY
  - EXPLAINS_FAILURE_MODE
  - TECHNICALLY_LINKED_TO_PATENT
  - AUTHORED_BY
  - INVENTED_BY
```

## GQ-D05-006 — 저자·발명자 교차역할

```yaml
query_id: GQ-D05-006
natural_language: 논문 저자이면서 특허 발명자인 SK온 연구자를 보여줘.

filters:
  researcher_roles:
    required:
      - PAPER_AUTHOR
      - PATENT_INVENTOR

answer_mode: RESEARCHER_NETWORK
```

## GQ-D05-007 — 공동출원 특허

```yaml
query_id: GQ-D05-007
natural_language: 외부기관과 공동출원한 특허군을 보여줘.

filters:
  ownership_scope:
    - EXTERNAL_JOINT
    - SK_GROUP_JOINT

traversals:
  - JOINTLY_OWNED_BY
  - CONNECTED_TO_PROGRAM
  - REQUIRES_CONTRACT_REVIEW
```

## GQ-D05-008 — 전고체 IP 체인

```yaml
query_id: GQ-D05-008
natural_language: 전고체 기술의 소재·계면·공정·특허를 연결해줘.

start_nodes:
  - TECH-SKON-D04-001
  - TECH-SKON-D04-065

traversals:
  - HAS_MATERIAL_COMPONENT
  - VALIDATED_BY_PAPER
  - SUPPORTED_BY_PATENT
  - CO_DEVELOPED_WITH
  - HAS_IP_GAP
```

## GQ-D05-009 — 급속충전 IP 체인

```yaml
query_id: GQ-D05-009
natural_language: SF+와 Hyper Fast의 특허·기술·경쟁 IP 위험을 보여줘.

start_nodes:
  - PROD-SKON-EV-005
  - PROD-SKON-EV-006

traversals:
  - USES_TECHNOLOGY
  - TECHNICALLY_LINKED_TO_PATENT
  - BENCHMARKED_AGAINST
  - HAS_FTO_RISK
```

## GQ-D05-010 — 건식전극 White Space

```yaml
query_id: GQ-D05-010
natural_language: 건식전극의 내부 특허·경쟁특허·White Space를 보여줘.

start_nodes:
  - TECH-SKON-D04-003

traversals:
  - SUPPORTED_BY_PATENT
  - COMPETES_WITH_PATENT_CLUSTER
  - HAS_PORTFOLIO_GAP
  - GENERATES_OI_SEED
```

## GQ-D05-011 — 안전 IP 계층

```yaml
query_id: GQ-D05-011
natural_language: 열전파·벤트·가스경로 관련 특허를 안전계층별로 보여줘.

start_nodes:
  - TECH-SKON-D04-002

traversals:
  - SUPPORTED_BY_PATENT
  - BLOCKS_HEAT
  - BLOCKS_FLAME
  - DIRECTS_GAS
  - INTEGRATED_INTO_PACK
```

## GQ-D05-012 — BaaS·Passport IP

```yaml
query_id: GQ-D05-012
natural_language: BaaS와 Battery Passport를 보호하는 특허군은 무엇인가?

start_nodes:
  - TECH-SKON-D04-018
  - TECH-SKON-D04-046

traversals:
  - SUPPORTED_BY_PATENT
  - MANAGES_BATTERY_ID
  - ESTIMATES_SOH
  - STORES_LIFECYCLE_EVENT
  - HAS_PRIVACY_GAP
```

## GQ-D05-013 — 후보 특허군

```yaml
query_id: GQ-D05-013
natural_language: 아직 정식 패밀리로 확정되지 않은 후보 특허를 보여줘.

filters:
  family_status:
    - CANDIDATE
    - FAMILY_RECONCILIATION_REQUIRED
```

## GQ-D05-014 — 만료·존속기간

```yaml
query_id: GQ-D05-014
natural_language: 특허군별 명목 보호기간과 공식 검증상태를 보여줘.

traversals:
  - HAS_PRIORITY_DATE
  - HAS_NOMINAL_TERM_BAND
  - HAS_OFFICIAL_STATUS

mandatory_warning:
  - Exact expiration requires official audit
```

## GQ-D05-015 — 외부 라이선스 필요영역

```yaml
query_id: GQ-D05-015
natural_language: 외부 라이선스나 공동개발이 필요한 기술영역을 보여줘.

traversals:
  - HAS_INTERNAL_IP_GAP
  - DEPENDS_ON_EXTERNAL_BACKGROUND_IP
  - MATCHED_WITH_PARTNER_TYPE
  - RECOMMENDS_COLLABORATION_MODEL
```

## GQ-D05-016 — 연구성과 상용화 전환

```yaml
query_id: GQ-D05-016
natural_language: 논문성과가 파일럿·특허·제품으로 전환됐는지 보여줘.

start_nodes:
  - USER_SELECTED_PAPER

traversals:
  - VALIDATES_TECHNOLOGY
  - TECHNICALLY_LINKED_TO_PATENT
  - TESTED_AT_FACILITY
  - APPLIED_TO_PRODUCT

answer_control:
  - Missing edge must be reported as NOT_CONFIRMED
```

## GQ-D05-017 — 핵심 발명자 집중도

```yaml
query_id: GQ-D05-017
natural_language: 특정 기술에 발명자 지식이 집중돼 있는지 보여줘.

start_nodes:
  - USER_SELECTED_TECHNOLOGY

traversals:
  - SUPPORTED_BY_PATENT
  - INVENTED_BY
  - AUTHORED_PAPER
  - CONNECTED_TO_OTHER_PROGRAM

answer_mode: CAPABILITY_RISK
```

## GQ-D05-018 — FTO 사전검색

```yaml
query_id: GQ-D05-018
natural_language: 특정 기술의 잠정 FTO 위험과 우선 조사대상을 보여줘.

start_nodes:
  - USER_SELECTED_TECHNOLOGY

traversals:
  - HAS_FTO_RISK
  - COMPETES_WITH_APPLICANT
  - HAS_DENSE_CLAIM_ZONE
  - HAS_DESIGN_AROUND_OPTION

mandatory_warning:
  - Not a legal opinion
```

## GQ-D05-019 — AI 발명관리

```yaml
query_id: GQ-D05-019
natural_language: AI Researcher를 이용한 발명에서 무엇을 기록해야 하는가?

start_nodes:
  - RDP-SKON-D05-008

traversals:
  - REQUIRES_HUMAN_CONTRIBUTION_RECORD
  - REQUIRES_MODEL_PROVENANCE
  - PROTECTED_AS
```

## GQ-D05-020 — D04·D05 통합 기술검색

```yaml
query_id: GQ-D05-020
natural_language: 기술의 제품·공정·특허·논문·연구자·파트너를 통합해줘.

start_nodes:
  - USER_SELECTED_TECHNOLOGY

traversals:
  - USED_IN_PRODUCT
  - USES_PROCESS
  - SUPPORTED_BY_PATENT
  - VALIDATED_BY_PAPER
  - INVENTED_BY
  - CO_DEVELOPED_WITH
  - HAS_IP_GAP
```

---
