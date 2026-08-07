---
id: skon-d05-d05-02-r-d-organization-governance
title: R&D Organization & Governance
summary: SK온 미래기술원과 SK이노베이션 환경과학기술원의 배터리·ESS 개발 조직 구조와 협업 관계를 정의하는 조직 메타데이터 레지스트리.
tags: [d05, rnd, schema]
keywords: [미래기술원, 환경과학기술원, 배터리, ESS, 고체전지, BMS, 품질경영, KOLAS, 배터리 개발, ESS 연구, 셀 모듈 팩, 조직도, 협력 체계, 대전]
related: []
priority: normal
domain: D05
section: D05-02.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1430
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-02. R&D Organization & Governance

## 02.1 Publicly Confirmed Organization Map

```text
SK Innovation R&D System
│
├── SK Innovation Institute of Environmental Science & Technology
│   ├── Energy transportation and storage
│   ├── Thermal management
│   ├── Core material and analysis technology
│   └── Collaborates with SK On Future Technology Institute
│
└── SK On Future Technology Institute
    ├── Automotive Battery R&D
    │   ├── Material
    │   ├── Cell
    │   ├── Module
    │   ├── Pack
    │   └── BMS
    │
    ├── ESS R&D
    │   ├── Cell
    │   ├── Module
    │   ├── Rack
    │   ├── System
    │   └── BMS
    │
    ├── Next-Generation Battery R&D
    │   ├── Solid electrolyte
    │   ├── Lithium-metal anode
    │   └── Solid-state cell
    │
    └── Digital R&D
        ├── AI Researcher
        ├── Cell design AI
        ├── Performance prediction
        └── Materials AI
```

현행 공식 페이지는 SK이노베이션 환경과학기술원과 SK온 미래기술원이 배터리·ESS 및 에너지저장 기술에서 협업한다고 설명한다. 양 조직을 동일 기관으로 합치지 않고, 그룹 공통 기반연구와 SK온 배터리 전문개발 조직으로 구분해 관리한다. ([SK Innovation][1])

---

## 02.2 Organization Entity Master

### ORG-SKON-RND-001 — SK On Future Technology Institute

```yaml
organization_id: ORG-SKON-RND-001
canonical_name: SK On Future Technology Institute
korean_name: SK온 미래기술원

organization_type:
  - Corporate R&D Institute
  - Battery Technology Center

ownership:
  company: SK On

location:
  city: Daejeon
  country: South Korea

confirmed_functions:
  - Automotive battery research
  - ESS research
  - Solid-state battery research
  - Battery material development
  - Cell, module, pack and BMS development
  - Pilot manufacturing

public_status: ACTIVE
confidence: VERY_HIGH

source_ids:
  - SRC-SKON-D05-001
  - SRC-SKON-D05-003
  - SRC-SKON-D05-004
```

---

### ORG-SKI-RND-001 — SK Innovation Institute of Environmental Science & Technology

```yaml
organization_id: ORG-SKI-RND-001
canonical_name: SK Innovation Institute of Environmental Science and Technology
korean_name: SK이노베이션 환경과학기술원

organization_type:
  - Group-Level R&D Institute

ownership:
  company: SK Innovation

location:
  city: Daejeon
  country: South Korea

confirmed_functions:
  - Energy storage research
  - Thermal management
  - Material analysis
  - Computational chemistry and engineering
  - Process research
  - Life-cycle assessment

relationship_to_sk_on:
  relation: COLLABORATES_WITH
  object: ORG-SKON-RND-001

confidence: VERY_HIGH
source_ids:
  - SRC-SKON-D05-001
  - SRC-SKON-D05-009
```

---

### ORG-SKON-QUALITY-001 — Quality Management Division

```yaml
organization_id: ORG-SKON-QUALITY-001
canonical_name: SK On Quality Management Division
korean_name: SK온 품질경영 부문

organization_type:
  - Quality Assurance Organization
  - Calibration and Metrology Infrastructure

location:
  city: Daejeon

confirmed_capability:
  - KOLAS international calibration laboratory
  - Battery quality measurement traceability
  - Calibration range management

relationship_to_rnd:
  - Supports measurement reliability
  - Supports test-equipment calibration
  - Supports global quality standardization

classification_rule:
  - Do not merge with Future Technology Institute
  - Do not classify calibration accreditation as product R&D

source_ids:
  - SRC-SKON-D05-006

confidence: VERY_HIGH
```

---

## 02.3 R&D Governance Layers

```yaml
rnd_governance_layers:

  strategy_layer:
    functions:
      - Technology portfolio selection
      - Product-roadmap alignment
      - Investment and pilot approval
      - Partner and IP strategy
    public_detail_level: LOW

  institute_layer:
    principal_entity:
      - ORG-SKON-RND-001
    functions:
      - Material and cell research
      - Module, pack and BMS development
      - Prototype and pilot validation

  program_layer:
    functions:
      - Technical objective
      - Target specification
      - Milestone and test plan
      - Customer requirement integration

  quality_layer:
    principal_entity:
      - ORG-SKON-QUALITY-001
    functions:
      - Measurement traceability
      - Equipment calibration
      - Quality-standard alignment

  external_collaboration_layer:
    functions:
      - University research
      - Startup and technology-company collaboration
      - Licensing and pilot technology transfer
      - Joint publications and patent ownership

  digital_rnd_layer:
    functions:
      - RFQ analysis
      - Design generation
      - Performance and cost prediction
      - Research-data utilization
```

이 거버넌스 구조는 공식적으로 확인된 조직과 기능을 배열한 D05 분석모델이다. SK온 내부의 실제 보고라인·예산권한·인사체계와 동일하다고 단정하지 않는다.

---
