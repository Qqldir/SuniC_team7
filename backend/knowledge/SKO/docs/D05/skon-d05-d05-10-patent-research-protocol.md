---
id: skon-d05-d05-10-patent-research-protocol
title: Patent Research Protocol
summary: "배터리 특허를 특허군 단위로 발굴·정규화·분석하는 절차와 신뢰도 등급, 정준 스키마를 정의한 문서로, 특허분석 10단계 프로세스와 3단계 증거계층 표가 핵심이다."
tags: [d05, rnd, schema, "xref:d04", "xref:d03"]
keywords: [특허 패밀리, 권리자, 출원인, KIPRIS, FTO 분석, IPC/CPC, 법적 상태, WIPO, 기술 매핑, 무효가능성, 특허군, 권리자정규화, 권리분석, 기술매핑, FTO, 특허증거계층, PATENTSCOPE, 우선권, 배터리]
related: []
priority: normal
domain: D05
section: D05-10.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1346
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 2. Patent Research Protocol·Assignee Normalization·Initial Patent Family Master

**문서 버전:** D05 v1.1
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-09 R&D Governance OI Seeds`

---

# D05-10. Patent Research Protocol

## 10.1 분석 목적

```yaml
patent_research_objectives:

  portfolio_identification:
    - SK온 및 전신 SK이노베이션의 배터리 특허 탐색
    - 동일 발명을 국가별 공개문서가 아닌 하나의 특허군으로 통합

  technology_mapping:
    - Patent Family → D04 Technology
    - Patent Family → D03 Product
    - Patent Family → D05 R&D Program
    - Patent Family → Inventor and Partner

  rights_analysis:
    - 최초 출원인
    - 현재 권리자
    - 공동 출원인
    - 국가별 등록·심사·소멸 상태
    - 잔여 권리기간

  oi_application:
    - 내부 보유기술과 외부 필요역량 구분
    - 공동개발 시 Background IP 확인
    - 경쟁사 특허와 중첩 가능성이 높은 영역 식별
```

---

## 10.2 Patent Family 분석 절차

```text
1. 출원인·권리자 후보명 검색
        ↓
2. 기술 키워드·IPC/CPC 결합검색
        ↓
3. 한국 최초 우선권 문서 확인
        ↓
4. PCT·미국·유럽·중국·일본 문서 연결
        ↓
5. 계속출원·분할출원·Continuation 확인
        ↓
6. 최초 출원인과 현재 권리자 분리
        ↓
7. 독립청구항 중심 권리범위 요약
        ↓
8. D04 기술·D03 제품과 연결
        ↓
9. 국가별 법적 상태 공식 등록부 재확인
        ↓
10. FTO·무효가능성·라이선스 필요성 검토
```

KIPRIS는 출원인 입력도우미와 IPC·키워드를 결합한 검색을 지원하고, PATENTSCOPE는 검색 필드와 특허 패밀리 정보를 이용한 구조화 검색을 제공한다. 미국 등록·심사상태는 USPTO Patent Center, 유럽은 EP Register에서 최종 확인하는 방식으로 설계한다. ([KIPRIS][1])

---

## 10.3 Patent Evidence Hierarchy

```yaml
patent_evidence_hierarchy:

  level_1_primary:
    source_grade: A_PLUS
    sources:
      - KIPRIS patent document
      - WIPO PATENTSCOPE publication
      - USPTO Patent Center
      - European Patent Register
      - National patent-office register

  level_2_mirror:
    source_grade: A
    sources:
      - Google Patents
      - Espacenet bibliographic view
    permitted_use:
      - Fast discovery
      - Family navigation
      - Full-text and claim reading
    restriction:
      - Legal status must be confirmed in official register

  level_3_secondary:
    source_grade: B
    sources:
      - Corporate patent analytics
      - Commercial database summary
      - News article
    permitted_use:
      - Search expansion only
    restriction:
      - Cannot establish ownership or legal status alone
```

Google Patents 자체도 표시된 출원인·우선일·법적 상태가 법률적 판단이 아니며 정확성을 보증하지 않는다고 명시한다. 따라서 아래 초기 Master의 상태값은 `DISCOVERY_SNAPSHOT`이며, 최종 권리판단은 국가별 공식 등록부 검증 후 확정한다. ([구글 특허][2])

---

## 10.4 Patent Family Canonical Schema

```yaml
patent_family_schema:

  patent_family_id:
    required: true

  canonical_title:
    required: true

  korean_title:
    required: true

  earliest_priority_date:
    required: true

  priority_application:
    required: false

  representative_publications:
    type: array

  family_members:
    type: array

  continuation_or_divisional_members:
    type: array

  original_applicants:
    type: array

  current_assignees:
    type: array

  joint_applicants:
    type: array

  inventors:
    type: array

  technology_ids:
    type: array

  product_ids:
    type: array

  program_ids:
    type: array

  claim_scope_summary:
    type: string

  legal_status_by_country:
    type: object

  status_verified_at:
    type: date

  status_source:
    allowed_values:
      - OFFICIAL_REGISTER
      - AGGREGATOR_SNAPSHOT
      - NOT_VERIFIED

  ownership_confidence:
    allowed_values:
      - VERY_HIGH
      - HIGH
      - MEDIUM
      - LOW

  relevance:
    allowed_values:
      - CORE
      - SUPPORTING
      - HISTORICAL
      - EXTERNAL_JOINT_IP
      - REVIEW_REQUIRED

  source_ids:
    required: true
```

---
