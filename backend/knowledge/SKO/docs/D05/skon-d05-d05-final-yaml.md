---
id: skon-d05-d05-final-yaml
title: D05 Final YAML
summary: "SK온 배터리 R&D의 조직, 시설, 프로그램, 특허 포트폴리오, 발명자 네트워크, 논문-기술 매핑 및 IP 전략을 정의하는 도메인 메타데이터 구조."
tags: [d05, rnd, schema, "xref:d06"]
keywords: [특허 포트폴리오, R&D 마스터 데이터, 배터리 기술 분류, 특허 소유권, 자유실시권 사전검토, 연구 조직, 고체전지 기술, 기술 매핑, 연구자 네트워크, 특허 패밀리, 발명자 네트워크, 논문-특허 매핑, FTO 사전 검토, 배터리 기술, 고무전해질, Solid-state battery, IP 전략]
related: []
priority: normal
domain: D05
section: ""
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1884
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05 Final YAML

```yaml
domain:
  domain_id: D05
  canonical_name: R&D, Patents and Intellectual Property
  company_id: CO-SKON
  version: 1.8
  reference_date: 2026-08-02
  status: CONDITIONALLY_COMPLETE

scope:
  included:
    - R&D organization
    - Research facilities
    - R&D programs
    - Patent taxonomy
    - Applicant and assignee normalization
    - Patent family master
    - Patent ownership and transfer
    - Peer-reviewed research outputs
    - Author and inventor network
    - Paper–patent–technology mapping
    - Preliminary legal-status audit
    - Product–patent technical mapping
    - Competitor claim-density benchmark
    - FTO pre-screening
    - Design-around opportunities
    - IP white-space analysis
    - Joint research IP governance
    - External IP strategy
    - Chunk library
    - Graph query templates

  excluded_or_deferred:
    - Legal FTO opinion
    - Patent infringement opinion
    - Patent validity opinion
    - Confidential joint-development contracts
    - Internal R&D budget
    - Internal researcher headcount
    - Product BOM and claim implementation
    - Complete global patent portfolio

organization_master:
  primary_rnd_institute:
    - ORG-SKON-RND-001

  group_collaboration:
    - ORG-SKI-RND-001

  quality_infrastructure:
    - ORG-SKON-QUALITY-001

facility_master:
  active_or_confirmed:
    - FAC-SKON-D05-001
    - FAC-SKON-D05-002
    - FAC-SKON-D05-003

  historical_plan_reconciliation:
    - FAC-SKON-D05-004

program_master:
  total_programs: 10

  priority_programs:
    - Commercial Lithium-Ion Advancement
    - Thermal Propagation Prevention
    - Dry Electrode Scale-Up
    - CTP and Multi-Form-Factor
    - ESS and Battery Intelligence
    - Solid-State Battery
    - Next-Generation Materials
    - AI Researcher
    - Quality and Validation
    - Open Research Collaboration

patent_master:
  confirmed_or_provisional_families: 33
  candidate_families: 4

  principal_clusters:
    - Cathode and Active Material
    - High-Voltage Electrolyte
    - Silicon Fast-Charging Anode
    - Separator
    - Z-Folding and Cell Assembly
    - Thermal Propagation and Venting
    - CTP and Pack Architecture
    - BMS and Diagnostics
    - BaaS and Lifecycle Data
    - Solid-State Battery
    - Manufacturing Inspection and AI

  ownership_scopes:
    - SOLE_SK_ON
    - TRANSFERRED_TO_SK_ON
    - SK_GROUP_JOINT
    - EXTERNAL_JOINT
    - AFFILIATE_OWNED
    - OWNERSHIP_UNVERIFIED

paper_master:
  verified_peer_reviewed_papers: 7
  candidate_papers: 1

  research_topics:
    - SIPE
    - Photonic Sintering
    - Lithium-Metal Interface
    - Gel Polymer Electrolyte
    - LMRO
    - Sulfide ASSB Interface
    - Ultrahigh-Nickel Single Crystal

researcher_network:
  verified_sk_on_paper_authors: 11
  external_research_leaders: 6
  verified_cross_role_researchers: 5
  probable_cross_role_researchers: 1

legal_status:
  document_reconciliation_batches: 2
  official_register_audit: PENDING

  rule:
    - Patent publication does not prove current enforceability
    - PCT cessation does not prove national-right expiration
    - Current owner requires official assignment verification

product_patent_mapping:
  direct_public_implementation_count: 0

  allowed_relations:
    - STRONG_TECHNICAL_MATCH
    - SUPPORTING_PLATFORM_IP
    - RESEARCH_IP_ONLY
    - NO_MAPPING

competitor_landscape:
  method: SAMPLE_BASED_CLAIM_DENSITY

  covered_areas:
    - Dry Electrode
    - Silicon Fast Charging
    - Sulfide ASSB
    - Thermal Propagation
    - EIS Diagnostics
    - Battery Passport

  legal_conclusion_allowed: false

ip_white_space:
  principal_areas:
    - On-Vent Closed-Loop Manufacturing
    - Dry Electrode Process Genealogy
    - Reworkable CTP
    - Immersion Cooling Intelligence
    - Solid-State Interface NDI
    - GPE Conversion Sensor
    - AI Researcher Provenance
    - Privacy-Preserving Battery Passport
    - Lightweight ASSB Pressure Control

rag:
  chunk_library:
    count: 20
    status: COMPLETE_V1

  graph_query_templates:
    count: 20
    status: COMPLETE_V1

  relationship_graph:
    canonical_edge_types: COMPLETE
    core_triples: 30
    status: COMPLETE_V1

data_quality:
  overall: MEDIUM_HIGH_FOR_TECHNOLOGY_INTELLIGENCE

  strong:
    - Technology–patent mapping
    - Paper–technology mapping
    - Research-program coverage
    - IP white-space generation
    - Joint-research governance

  weak:
    - Official legal status
    - Exact current ownership
    - Product claim implementation
    - Complete competitor portfolio
    - Contractual IP rights

  critical_open_items:
    - Official-register audit
    - Patent-family boundary reconciliation
    - Product BOM and claim chart
    - Joint-IP contract review
    - Candidate family normalization

open_innovation:
  rnd_governance_seeds: 6
  research_output_seeds: 6
  ip_strategy_seeds: 6
  external_ip_actions: 6

  priority_programs:
    - Dry Electrode Patent and Trade-Secret Fortress
    - Solid-State Interface NDI Consortium
    - On-Vent Closed-Loop Laser JDA
    - Reworkable CTP Circular-Pack IP
    - AI-Assisted Invention Evidence System
    - Joint-IP Contract Analytics

completion:
  organization: COMPLETE_V1
  facilities: COMPLETE_V1
  programs: COMPLETE_V1
  patent_taxonomy: COMPLETE_V1
  patent_family_master: COMPLETE_PROVISIONAL
  paper_master: COMPLETE_V1
  researcher_network: COMPLETE_V1
  product_patent_mapping: COMPLETE_V1
  legal_status_audit: PARTIAL
  competitor_landscape: COMPLETE_SAMPLE_BASED
  white_space: COMPLETE_V1
  chunk_library: COMPLETE_V1
  graph_queries: COMPLETE_V1
  human_report: COMPLETE
  final_yaml: COMPLETE

next_domain:
  domain_id: D06
  canonical_name: Manufacturing Process and Operations
```

---

# D05 완료 상태

**완료:** `SK온 D05 R&D, Patents & Intellectual Property v1.8`

## 최종 산출물

* R&D Program: **10개**
* Patent Family: **33개**
* Candidate Patent Family: **4개**
* 검증 논문: **7건**
* 후보 논문: **1건**
* SK온 논문 저자: **11명**
* D05 Chunk: **20개**
* Graph Query Template: **20개**
* Core Relationship Triple: **30개**
* IP White Space: **9개**

## 다음 시작점

`SK온 D06 Manufacturing Process & Operations`

```text
D06-00 Domain Boundary
→ D06-RP-001 Manufacturing Research Pack
→ D06-01 End-to-End Manufacturing Flow
→ D06-02 Raw Material Receiving & Preparation
→ D06-03 Mixing
→ D06-04 Coating & Drying
→ D06-05 Calendering
→ D06-06 Slitting & Notching
→ D06-07 Stacking & Cell Assembly
→ D06-08 Electrolyte Filling
→ D06-09 Formation & Aging
→ D06-10 Inspection & Grading
→ D06-11 Module·Pack·CTP Assembly
→ D06-12 Smart Factory·OT·Digital Twin
→ D06-13 Yield·Scrap·Energy Pain Point
→ D06-14 Manufacturing OI Seed
```

---
