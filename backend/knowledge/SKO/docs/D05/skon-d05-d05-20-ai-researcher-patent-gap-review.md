---
id: skon-d05-d05-20-ai-researcher-patent-gap-review
title: AI Researcher Patent Gap Review
summary: "AI 연구자 플랫폼의 핵심 기술별 특허 현황을 분석하고, 검색된 용접제어 특허 후보를 제시하며, 특허·영업비밀·저작권·계약을 통합한 IP 보호 전략을 제안하는 문서."
tags: [d05, rnd, schema, "xref:d04"]
keywords: [특허포트폴리오, RFQ분석, 셀설계AI, 용접제어, 영업비밀, IP거버넌스, 배터리진단, 모델보호, 지식재산보호, 기술갭분석, 특허 공백, RFQ, 배터리 설계, 이상감지, 특허군, 폐루프제어, 지식재산 보호]
related: []
priority: normal
domain: D05
section: D05-20.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 989
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-20. AI Researcher Patent Gap Review

## 20.1 Targeted Search Result

```yaml
ai_researcher_patent_search:

  searched_concepts:
    - RFQ analysis AI
    - Cell design AI
    - Battery design generation
    - Battery cost calculation AI
    - AI Researcher
    - Machine-learning battery design

  directly_identified_sk_on_families:
    - AI-based battery abnormality detection
    - AI-based welding control candidate
    - SOH and battery-state estimation

  not_identified_as_explicit_patent_family:
    - RFQ Analysis AI
    - Generative Cell Design AI
    - Cell Cost Calculation AI
    - AI Researcher Orchestration Platform

  search_status:
    - TARGETED_SEARCH_ONLY
    - NOT_EXHAUSTIVE
```

정확한 `RFQ 분석`, `셀 설계안 생성`, `원가계산 AI` 명칭으로는 SK온 특허군이 확인되지 않았다. 이는 특허가 없다는 결론이 아니라 아직 공개 전이거나, 다른 명칭·분류로 출원됐거나, 소프트웨어·데이터·모델을 영업비밀로 관리할 가능성을 남긴다. 반면 AI 기반 이상감지와 배터리 진단 관련 특허는 확인된다. ([구글 특허][14])

---

## 20.2 AI Welding Control Candidate

```yaml
candidate_patent_family:
  candidate_id: PF-CAND-SKON-D05-002
  canonical_title: AI-Based Welding Control System
  representative_publication:
    - CN120382281A

  applicant:
    - APP-SKON-001

  filing_date_snapshot: 2025-07-29

  technology_scope:
    - Welding image analysis
    - Machine-learning defect recognition
    - Automated welding control
    - Industrial image inspection

  related_technology_ids:
    - TECH-SKON-D04-042
    - TECH-SKON-D04-055
    - TECH-SKON-D04-061

  status:
    - NEW_CANDIDATE
    - FAMILY_AND_PRIORITY_AUDIT_REQUIRED
```

중국 공개문서에서 SK온 출원으로 표시된 AI 기반 용접제어 시스템이 검색됐으며, 영상·패턴인식과 기계학습을 이용한 용접 검사·제어와 연결된다. 이 특허는 AI Researcher보다는 제조 AI와 예측 품질영역에 포함하는 것이 적절하며, 원 우선권과 다른 국가 패밀리를 추가 확인해야 한다. ([구글 특허][15])

---

## 20.3 AI IP Governance Decision

```yaml
ai_ip_governance:

  patent_candidates:
    - Novel battery model architecture
    - Sensor and model integration
    - Manufacturing closed-loop control
    - Model-based safety action
    - Explainable fault classification

  trade_secret_candidates:
    - Training data
    - Customer RFQ corpus
    - Cost tables
    - Hyperparameters
    - Feature engineering
    - Internal evaluation set
    - Model deployment architecture

  copyright_and_database:
    - Source code
    - Technical reports
    - Structured battery ontology
    - Curated experimental database

  contractual_controls:
    - Employee invention assignment
    - Vendor model ownership
    - Open-source license review
    - Cloud provider data-use restriction
    - University publication review
```

AI Researcher는 알고리즘 하나보다 데이터·모델·업무흐름·비용정보가 결합된 시스템이므로 모든 요소를 특허화하는 것보다 특허·영업비밀·저작권·계약을 혼합한 보호전략이 필요하다.

---
