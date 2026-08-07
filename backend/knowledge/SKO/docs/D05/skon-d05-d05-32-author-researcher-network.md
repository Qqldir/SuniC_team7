---
id: skon-d05-d05-32-author-researcher-network
title: Author·Researcher Network
summary: "SK온 R&D 연구자의 신원, 소속, 연구 분야를 체계적으로 관리하기 위한 데이터 스키마와 배터리 개발 분야 저자 9명의 마스터 정보"
tags: [d05, rnd, schema]
keywords: [연구자 정보 관리, 저자 마스터, 논문 저자 연계, 특허 발명자, 배터리 연구, 고체전지, 전해질, 포토닉 소결, 연구자 스키마, 대응 저자, 엔티티 스키마, 소속 정보, 교신저자, 발명자, 신원검증, 광자소결]
related: []
priority: normal
domain: D05
section: D05-32.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2068
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-32. Author·Researcher Network

## 32.1 Researcher Entity Schema

```yaml
researcher_entity_schema:

  researcher_id: required
  canonical_name: required

  affiliations:
    required_fields:
      - organization
      - valid_period
      - source_id

  roles:
    allowed_values:
      - AUTHOR
      - CORRESPONDING_AUTHOR
      - SK_ON_AUTHOR
      - EXTERNAL_PRINCIPAL_INVESTIGATOR
      - PATENT_INVENTOR
      - RESEARCH_PARTNER

  paper_ids:
    type: array

  patent_family_ids:
    type: array

  identity_status:
    allowed_values:
      - VERIFIED
      - PARTIALLY_VERIFIED
      - NAME_COLLISION_RISK

  prohibited_fields:
    - Personal email
    - Personal phone
    - Residential address
```

---

## 32.2 SK온 Author Master

```yaml
sk_on_author_master:

  - researcher_id: RES-SKON-D05-001
    canonical_name: Hansol Lee
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-001
    research_domain:
      - SIPE
      - Lithium-metal electrolyte
    affiliation:
      - Next Generation Cell Development 1 Unit
      - Next Generation Battery R&D Office
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-002
    canonical_name: Kyeong Joon Kim
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Photonic sintering
      - Garnet electrolyte
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-003
    canonical_name: Junghun Han
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Oxide electrolyte manufacturing
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-004
    canonical_name: Myung-Soo Park
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Solid-state battery
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-005
    canonical_name: Min Kyu Kim
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Photonic sintering
      - Oxide electrolyte
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-006
    canonical_name: Do Kyeong Lee
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Solid-state process
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-007
    canonical_name: Eun Jeong Yi
    role:
      - SK_ON_AUTHOR
      - CORRESPONDING_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Garnet electrolyte
      - Photonic sintering
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-008
    canonical_name: Jaehoon Choi
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-004
    research_domain:
      - Gel polymer electrolyte
      - Cathode interface
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-009
    canonical_name: Jeonghyun Ko
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-004
    research_domain:
      - Gel polymer electrolyte
      - High-nickel cathode degradation
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-010
    canonical_name: Young-Uk Park
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-007
    research_domain:
      - Ultrahigh-nickel cathode
      - Single-crystal cathode
    identity_status: VERIFIED

  - researcher_id: RES-SKON-D05-011
    canonical_name: Mincheol Beak
    role:
      - SK_ON_AUTHOR
    paper_ids:
      - PAPER-SKON-D05-007
    research_domain:
      - Ultrahigh-nickel cathode
    identity_status: VERIFIED
```

광소결 논문에는 총 9명의 저자 중 6명의 SK온 연구자가 참여했고, Nature Energy 초고니켈 논문에는 Young-Uk Park과 Mincheol Beak이 SK온 R&D Center 소속 저자로 기재됐다. ([ACS Publications][3])

---

## 32.3 External Research Leader Master

```yaml
external_research_leaders:

  - researcher_id: RES-EXT-D05-001
    canonical_name: Hadi Khani
    organization:
      - University of Texas at Austin
    role:
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-001
    research_domain:
      - Single-ion polymer electrolyte
      - Lithium-metal battery

  - researcher_id: RES-EXT-D05-002
    canonical_name: Jin Ho Kim
    organization:
      - Korea Institute of Ceramic Engineering and Technology
    role:
      - CORRESPONDING_AUTHOR
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-002
    research_domain:
      - Ceramic processing
      - Photonic sintering

  - researcher_id: RES-EXT-D05-003
    canonical_name: Dong-Won Kim
    organization:
      - Hanyang University
    role:
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-003
    research_domain:
      - Lithium-metal interface
      - Solid-state battery

  - researcher_id: RES-EXT-D05-004
    canonical_name: Jong Hyeok Park
    organization:
      - Yonsei University
    role:
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-004
    research_domain:
      - Polymer electrolyte
      - High-nickel interface

  - researcher_id: RES-EXT-D05-005
    canonical_name: Kyu Tae Lee
    organization:
      - Seoul National University
    role:
      - CORRESPONDING_AUTHOR
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-005
      - PAPER-SKON-D05-006
    research_domain:
      - LMRO
      - Sulfide ASSB cathode

  - researcher_id: RES-EXT-D05-006
    canonical_name: Kisuk Kang
    organization:
      - Seoul National University
      - Institute for Basic Science
    role:
      - RESEARCH_PARTNER
    paper_ids:
      - PAPER-SKON-D05-007
    research_domain:
      - Ultrahigh-nickel cathode
      - Single-crystal cathode
```

---

## 32.4 Author Network Graph

```text
SK On Future Technology Institute
│
├── SIPE Research
│   ├── Hansol Lee
│   └── University of Texas / Hadi Khani Group
│
├── Oxide Electrolyte & Photonic Sintering
│   ├── Kyeong Joon Kim
│   ├── Junghun Han
│   ├── Myung-Soo Park
│   ├── Min Kyu Kim
│   ├── Do Kyeong Lee
│   ├── Eun Jeong Yi
│   └── KICET / Jin Ho Kim
│
├── Lithium-Metal Interface
│   ├── SK On Joint Research Team
│   └── Hanyang University / Dong-Won Kim
│
├── Gel Polymer Electrolyte
│   ├── Jaehoon Choi
│   ├── Jeonghyun Ko
│   └── Yonsei University / Jong Hyeok Park
│
├── LMRO Cathode
│   └── Seoul National University / Kyu Tae Lee Group
│
└── Ultrahigh-Nickel Single Crystal
    ├── Young-Uk Park
    ├── Mincheol Beak
    ├── Seoul National University / Kisuk Kang Group
    ├── KICET
    └── Institute for Basic Science
```

---

## 32.5 Identity Resolution Rules

```yaml
researcher_identity_resolution:

  matching_keys:
    - Full name
    - Affiliation
    - Research topic
    - Publication year
    - Co-author network
    - ORCID when available
    - Patent inventor address or affiliation when legally public

  name_collision_controls:
    - Do not merge authors using English name alone
    - Korean and English names require source-backed alias
    - Patent inventor and paper author require independent identity match
    - Organization changes must preserve valid period

  author_inventor_edge:
    allowed_when:
      - Full name match
      - Institution or employer match
      - Technology-field match
      - No contradictory identity evidence

    edge_status:
      - VERIFIED_SAME_PERSON
      - PROBABLE_SAME_PERSON
      - UNRESOLVED
```

---
