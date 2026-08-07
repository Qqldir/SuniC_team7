---
id: skon-d05-d05-36-researcher-entity-master-expansion
title: Researcher Entity Master Expansion
summary: 논문 저자와 특허 발명자로 나타나는 같은 인물의 정체성을 검증하고 교차 역할 연구자 네트워크를 매핑하는 기준
tags: [d05, rnd, core-candidate, schema]
keywords: [cross-role researcher, 다중역할 연구자, author-inventor linkage, identity verification, 특허 발명자, 논문 저자, oxide electrolyte, 산화물 전해질, photonic sintering, 지식재산, 정체성 검증, 저자-발명자, 교차 역할, 특허-논문 연결, 고체 전해질, 광소결, 공동연구자, 발명자 네트워크, 연구자 조사, 인명 확인]
related: []
priority: critical
domain: D05
section: D05-36.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2368
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# SK온 D05 R&D, Patents & Intellectual Property

## Part 6. Inventor–Author Network·Research Capability Map·Legal-Status Audit Batch 1

**문서 버전:** D05 v1.5
**기준일:** 2026-08-02
**이전 완료 지점:** `D05-35 Research Output OI Seeds`

---

# D05-36. Researcher Entity Master Expansion

## 36.1 Cross-Role Researcher 정의

```yaml
cross_role_researcher:
  definition: >
    논문 저자, 특허 발명자, 공동연구자 가운데 두 개 이상의
    연구성과 유형에 등장하는 인물

  role_types:
    - PAPER_AUTHOR
    - CORRESPONDING_AUTHOR
    - PATENT_INVENTOR
    - INTERNAL_RESEARCHER
    - EXTERNAL_RESEARCH_PARTNER

  identity_requirement:
    verified_same_person:
      - Name match
      - Affiliation match
      - Research-domain match
      - Publication and patent timeline consistency

    probable_same_person:
      - Name-format difference exists
      - Co-author or co-inventor network overlaps
      - Research topic and employer match

    unresolved:
      - Name alone matches
      - Affiliation or technical field cannot be confirmed
```

---

## RES-SKON-D05-002 — Kyeong Joon Kim

```yaml
researcher_id: RES-SKON-D05-002
canonical_name: Kyeong Joon Kim

roles:
  - PAPER_AUTHOR
  - PATENT_INVENTOR
  - SK_ON_RESEARCHER

paper_ids:
  - PAPER-SKON-D05-002

patent_family_ids:
  - PF-SKON-D05-032

research_domains:
  - Oxide solid electrolyte
  - Garnet electrolyte
  - Photonic sintering
  - Solid-state battery manufacturing

identity_status: VERIFIED_SAME_PERSON

identity_basis:
  - Exact English-name match
  - Same SK On research context
  - Same oxide-electrolyte and photonic-sintering field
  - Patent priority predates corresponding journal publication

confidence: VERY_HIGH
```

광소결 가넷 논문의 저자명과 산화물 박막 광소결 특허의 발명자명이 일치하며, 논문과 특허 모두 산화물 고체전해질·광소결을 대상으로 한다. 특허는 Kyeong Joon Kim, Min Kyu Kim, Eun Jeong Yi 등을 발명자로 기록하고 있으며, 논문에도 동일 연구자들이 참여했다. ([구글 특허][1])

---

## RES-SKON-D05-005 — Min Kyu Kim

```yaml
researcher_id: RES-SKON-D05-005
canonical_name: Min Kyu Kim

roles:
  - PAPER_AUTHOR
  - PATENT_INVENTOR
  - SK_ON_RESEARCHER

paper_ids:
  - PAPER-SKON-D05-002

patent_family_ids:
  - PF-SKON-D05-032

research_domains:
  - Oxide electrolyte sheet
  - Photonic processing
  - Solid-state cell integration

identity_status: VERIFIED_SAME_PERSON
confidence: VERY_HIGH
```

---

## RES-SKON-D05-007 — Eun Jeong Yi

```yaml
researcher_id: RES-SKON-D05-007
canonical_name: Eun Jeong Yi

roles:
  - PAPER_AUTHOR
  - CORRESPONDING_AUTHOR
  - PATENT_INVENTOR
  - SK_ON_RESEARCHER

paper_ids:
  - PAPER-SKON-D05-002

patent_family_ids:
  - PF-SKON-D05-032

research_domains:
  - Oxide electrolyte
  - Ceramic thin film
  - Photonic sintering
  - Solid-state battery process

identity_status: VERIFIED_SAME_PERSON
confidence: VERY_HIGH
```

Eun Jeong Yi는 광소결 논문의 교신저자이면서 산화물 박막 소결체 특허의 발명자로 확인된다. 이는 SK온 내부에서 소재연구와 공정 IP를 연결하는 연구자 역할의 직접적인 공개 근거다. ([구글 특허][1])

---

## RES-SKON-D05-010 — Young-Uk Park

```yaml
researcher_id: RES-SKON-D05-010
canonical_name: Young-Uk Park
aliases:
  - Young Uk Park

roles:
  - PAPER_AUTHOR
  - PATENT_INVENTOR
  - SK_ON_RESEARCHER

paper_ids:
  - PAPER-SKON-D05-007

patent_family_ids:
  - PF-CAND-SKON-D05-003
  - PF-CAND-SKON-D05-004

research_domains:
  - High-nickel cathode
  - Single-crystal cathode
  - Low-cobalt cathode
  - Cathode structural stability

identity_status: VERIFIED_SAME_PERSON
confidence: HIGH
```

Young-Uk Park은 Nature Energy 초고니켈 단결정 논문의 SK온 저자로 기재됐고, 니켈계 단결정 양극 활물질 관련 특허에서도 발명자로 확인된다. 다만 해당 특허가 논문의 `니켈 94% 초과·10μm급 단결정` 발명을 직접 청구하는지는 청구항 비교가 필요하다. ([구글 특허][2])

### 신규 후보 특허군

```yaml
candidate_patent_family:
  candidate_id: PF-CAND-SKON-D05-003
  representative_publications:
    - US20240222617A1
    - EP4397627A1

  earliest_priority_date: 2023-01-03

  inventors:
    - Young Uk Park
    - Min Gu Kang
    - Seung Hyun Kim
    - Jeong Hoon Jeun
    - Jae Young Choi
    - Je Nam Choi

  applicants:
    - SK Innovation
    - SK On

  technology_scope:
    - Single-particle cathode active material
    - Mn oxidation-state control
    - Low-cobalt cathode
    - High-temperature stability
    - Gas-generation reduction

  relation_to_paper:
    - SAME_RESEARCH_DOMAIN
    - NOT_CONFIRMED_AS_SAME_INVENTION

  status:
    - PUBLISHED_PENDING_SNAPSHOT
```

---

## RES-SKON-D05-011 — Mincheol Beak

```yaml
researcher_id: RES-SKON-D05-011
canonical_name: Mincheol Beak
aliases:
  - Min Cheol Beak
  - Min Cheol BEAK

roles:
  - PAPER_AUTHOR
  - PROBABLE_PATENT_INVENTOR
  - SK_ON_RESEARCHER

paper_ids:
  - PAPER-SKON-D05-007

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-004

research_domains:
  - High-nickel cathode
  - Cathode particle structure
  - Cathode active-material synthesis

identity_status: PROBABLE_SAME_PERSON

identity_basis:
  - Name differs only by spacing
  - Same SK On cathode field
  - Repeated co-inventor relationship with Young Uk Park

confidence: HIGH
```

2026년 공개된 추가 양극 활물질 특허에는 `Young Uk Park`과 `Min Cheol BEAK`이 공동 발명자로 나타난다. 논문의 `Young-Uk Park`·`Mincheol Beak`과 동일 인물일 가능성이 높지만, ORCID나 한국어 성명 등 직접 식별정보가 없어 `PROBABLE`로 유지한다. ([구글 특허][3])

---

## RES-SKON-D05-012 — Dong Hoon Lee

```yaml
researcher_id: RES-SKON-D05-012
canonical_name: Dong Hoon Lee

roles:
  - PATENT_INVENTOR
  - CROSS_PROGRAM_INVENTOR

patent_family_ids:
  - PF-SKON-D05-002
  - PF-SKON-D05-003

research_domains:
  - Fast-charging electrode
  - Dry electrode manufacturing
  - Electrode adhesion
  - Calendering

identity_status: VERIFIED_WITHIN_PATENT_NETWORK
confidence: HIGH
```

Dong Hoon Lee는 급속충전 전극 패밀리와 건식전극 시트 패밀리에 모두 발명자로 나타난다. 이는 급속충전용 전극설계와 건식 제조공정 사이의 내부 지식 연결 가능성을 보여주지만, 조직상 동일 프로젝트를 담당했다는 의미는 아니다. ([구글 특허][4])

---

## RES-SKON-D05-013 — Kyu Min Hwang

```yaml
researcher_id: RES-SKON-D05-013
canonical_name: Kyu Min Hwang

roles:
  - PATENT_INVENTOR

patent_family_ids:
  - PF-SKON-D05-023

research_domains:
  - Electrochemical impedance spectroscopy
  - Battery abnormality detection
  - ESS BMS

identity_status: VERIFIED_WITHIN_PATENT_RECORD
confidence: VERY_HIGH
```

---

## RES-SKON-D05-014 — Jae Sik Shin

```yaml
researcher_id: RES-SKON-D05-014
canonical_name: Jae Sik Shin

roles:
  - PATENT_INVENTOR
  - FORM_FACTOR_INVENTOR

patent_family_ids:
  - PF-SKON-D05-025
  - PF-SKON-D05-026

research_domains:
  - Prismatic cell
  - Vent notch
  - Rupture-pressure control
  - Gas discharge

identity_status: VERIFIED_WITHIN_PATENT_NETWORK
confidence: VERY_HIGH
```

Jae Sik Shin을 포함한 동일 발명자 그룹은 교차형 노치와 H형 노치라는 서로 다른 On-Vent 패밀리에 반복 등장한다. 두 미국 특허는 각각 2024년 5월 등록문서가 발행된 것으로 나타난다. ([구글 특허][5])

---

## RES-SKON-D05-015 — Jun Hee Jung

```yaml
researcher_id: RES-SKON-D05-015
canonical_name: Jun Hee Jung

roles:
  - PATENT_INVENTOR
  - PACK_ARCHITECTURE_INVENTOR

patent_family_ids:
  - PF-SKON-D05-027

research_domains:
  - Pouch cell
  - Cell-to-pack
  - Thermal interface
  - Gas-discharge path

identity_status: VERIFIED_WITHIN_PATENT_RECORD
confidence: VERY_HIGH
```

---
