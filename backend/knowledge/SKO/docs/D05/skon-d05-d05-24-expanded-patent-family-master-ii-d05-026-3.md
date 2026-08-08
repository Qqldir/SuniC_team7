---
id: skon-d05-d05-24-expanded-patent-family-master-ii-d05-026-3
title: Expanded Patent Family Master II — D05-026 — On-Vent H-Pattern Structure
summary: "이차전지 셀 벤트에 적용된 H형 노치 구조로 목표 파열압력을 구현하는 SK온 D05-026 특허의 기술 원리, 청구항 범위, 그리고 선행 특허와의 차별성 및 FTO 분석 방향을 설명합니다."
tags: [d05, rnd, schema, "xref:d04"]
keywords: [노치 형상, 각형 셀, 파열압력, 응력집중, On-Vent, D05-026, 이차전지, 레이저 가공, 이차전지 셀, 벤트 노치, 각형 케이스, FTO 분석, prismatic cell, stress concentration]
related: []
priority: normal
domain: D05
section: D05-24.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: Expanded Patent Family Master II
tokens: 675
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산 · Expanded Patent Family Master II

## PF-SKON-D05-026 — On-Vent H-Pattern Structure

```yaml
patent_family_id: PF-SKON-D05-026
canonical_title: Secondary Battery Cell with H-Pattern Vent Notch
korean_title: H형 노치 패턴을 포함하는 각형 이차전지 셀

earliest_priority_date: 2022-06-15

representative_publications:
  - US20230411778A1
  - US11990637B2

priority_applications:
  - KR10-2022-0072821
  - KR10-2023-0043968

original_applicant:
  - APP-SKON-001

current_assignee_snapshot:
  - APP-SKON-001

inventors:
  - Jae Sik Shin
  - Seung Hoon Ju
  - Ji Yong Park
  - Jae Gyu Byun
  - Gi Jeong Seo

technology_ids:
  - TECH-SKON-D04-006
  - TECH-SKON-D04-061

product_ids:
  - PROD-SKON-EV-009

claim_scope_summary: >
  각형 셀 케이스의 벤트 베이스에 길이방향 노치와 수직방향
  노치를 결합한 H형 또는 유사 패턴을 형성해 특정 압력범위에서
  신뢰성 있게 파단되도록 하는 구조.

ownership_scope: SOLE_SK_ON
relevance: CORE_ON_VENT

status_snapshot:
  us: GRANTED_2024
  legal_status_source: AGGREGATOR_SNAPSHOT

source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY
```

PF-D05-025와 PF-D05-026은 우선일·발명자가 같지만 한국 우선권번호와 노치구조가 서로 다르다. 하나의 패밀리로 병합하지 않고 `ON_VENT_SIBLING_CLUSTER` 안의 별도 개선발명으로 관리해야 한다. ([구글 특허][4])

### On-Vent Patent Cluster

```text
ON_VENT_SIBLING_CLUSTER
├── PF-D05-025
│   └── Intersecting cross-direction notch structure
│
└── PF-D05-026
    └── H-pattern longitudinal/perpendicular notch structure

Shared Objectives
├── Predetermined fracture pressure
├── Reliable stress concentration
├── Directional gas discharge
└── Flexible vent location on prismatic case
```

### IP 해석

On-Vent 관련 공개특허의 핵심은 단순히 “레이저를 사용한다”는 점보다, **캔 또는 베이스에 어떤 노치 형상을 어느 깊이로 구성해 목표 파열압력을 구현하는가**에 있다. 따라서 FTO 분석은 레이저 장비특허와 별도로 노치 형상·응력집중·파열막 구조의 유효 청구항을 검토해야 한다.

---
