---
id: skon-d05-d05-40-joint-research-publication-ip-governance
title: Joint Research·Publication·IP Governance
summary: "공동연구와 기술이전 계약에서 지식재산권의 소유와 배분을 규정하고, 논문 발표 전 검토 절차와 AI 지원 발명의 발명자 판정 기준을 제시한다."
tags: [d05, rnd, schema]
keywords: [공동 특허, 지적재산 소유권, 특허 기술공개, 출판 검토 절차, 배경기술/응용기술, 발명자 인정, 산학협력 R&D, AI 보조 발명, 기술 이전, 공동 의사결정, 지식재산권, 특허, 발명자, AI발명, 기술이전, 공동소유, 배경IP, 발명공개, 논문검토]
related: []
priority: normal
domain: D05
section: D05-40.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1126
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-40. Joint Research·Publication·IP Governance

## 40.1 공동연구 유형별 권리구조

```yaml
joint_research_ip_models:

  university_scientific_discovery:
    examples:
      - SIPE
      - GPE residual monomer
      - LMRO degradation

    recommended_ip_structure:
      background_ip:
        - Each party retains pre-existing materials and methods

      foreground_ip:
        - Inventorship determined by actual contribution
        - Ownership follows agreed contribution and jurisdiction rules

      publication:
        - Pre-publication patent review
        - Confidential data removal
        - Filing before disclosure

  process_scale_up:
    example:
      - Photonic sintering with KICET

    recommended_ip_structure:
      sk_on_ownership:
        - Battery-specific cell design
        - Internal process window
        - Pilot data

      partner_ownership:
        - Generic equipment and light-source know-how

      joint_foreground:
        - Battery-specific photonic process
        - Inline control method
        - Large-area electrolyte-sheet process

  joint_material_platform:
    example:
      - LLZO with Dankook University

    required_controls:
      - Joint patent decision authority
      - Cost-sharing rule
      - Exclusive field-of-use license
      - Improvement-IP allocation
      - Third-party licensing approval

  technology_transfer:
    example:
      - Solid Power

    required_controls:
      - Licensed background IP
      - SK On process improvements
      - Electrolyte supply rights
      - Geographic manufacturing rights
      - Post-termination use rights
```

---

## 40.2 Publication Review Workflow

```text
Research Result Generated
        ↓
Confidentiality Classification
        ↓
Invention Disclosure Submission
        ↓
Prior Patent Search
        ↓
Inventorship Review
        ↓
Patent Filing Decision
        ↓
Joint-Owner Approval
        ↓
Paper and Conference Review
        ↓
Publication
        ↓
Patent–Paper–Pilot Link Registration
```

---

## 40.3 AI-Assisted Invention Rule

```yaml
ai_assisted_invention_governance:

  human_contribution_record:
    - Problem definition
    - Constraint selection
    - Training-data selection
    - Output evaluation
    - Experimental validation
    - Final inventive concept

  ai_record:
    - Model name and version
    - Prompt or task instruction
    - Input data lineage
    - Generated candidate set
    - Human modifications
    - Rejected outputs

  inventorship_rule:
    - AI system is not registered as inventor
    - Human inventive contribution must be documented
    - Mere selection of an AI output is insufficient without technical contribution

  confidentiality:
    - Customer RFQ must not enter external public models
    - Patent-unpublished results require isolated environment
    - Model vendor must not reuse internal data

  ownership:
    - Vendor background model remains vendor IP
    - SK On experiment data remains SK On-controlled
    - Fine-tuned model ownership must be contractually specified
```

---

## 40.4 공동연구 계약 필수 메타데이터

```yaml
joint_research_contract_metadata:

  project_identity:
    - Project ID
    - Program ID
    - Technology ID
    - Principal investigators
    - Research period

  background_ip:
    - Patent family
    - Know-how
    - Software
    - Dataset
    - Material sample

  foreground_ip:
    - Invention disclosure
    - Inventors
    - Owner
    - Filing jurisdiction
    - Cost allocation

  improvement_ip:
    - Sole improvement
    - Joint improvement
    - Platform improvement
    - Application-specific improvement

  data:
    - Raw data ownership
    - Processed data ownership
    - Model-training permission
    - Retention period

  publication:
    - Review period
    - Filing delay period
    - Confidential section removal
    - Attribution rule

  exit:
    - Project termination
    - Sample return or destruction
    - Post-project licensing
    - Surviving confidentiality
```

---
