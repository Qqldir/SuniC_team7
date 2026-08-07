---
id: skon-d03-8-16-canonical-triple-registry
title: Canonical Triple Registry
summary: "SK온 제품과 기술의 관계를 트리플 형태로 정의하여 제품 속성, 기술 사양, 아키텍처를 조회할 수 있는 시맨틱 데이터베이스."
tags: [d03, product, schema]
keywords: [배터리 제품, 전기차, 에너지저장장치, NCM 화학, 포우치셀, BMS, 냉각액침, 제품 기술, 메타데이터, Solid Power, 제품 기술 관계, 배터리 화학, 배터리관리시스템, 배터리 형태, 냉각 침지, 고체전해질, BaaS]
related: []
priority: normal
domain: D03
section: 8.16
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1196
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 8.16 Canonical Triple Registry

```yaml
triples:

  - triple_id: TR-D03-001
    subject: CO-SKON
    predicate: HAS_PRODUCT
    object: PROD-SKON-EV-001
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-051

  - triple_id: TR-D03-002
    subject: PROD-SKON-EV-001
    predicate: USES_CHEMISTRY
    object: CHEM-NCM
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D03-003
    subject: PROD-SKON-EV-001
    predicate: HAS_FORM_FACTOR
    object: FORM-POUCH
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH

  - triple_id: TR-D03-004
    subject: PROD-SKON-EV-003
    predicate: HAS_SUCCESSOR
    object: PROD-SKON-EV-004
    evidence_type: OFFICIAL_DIRECT
    confidence: HIGH
    source_ids:
      - SRC-SKON-D03-052

  - triple_id: TR-D03-005
    subject: PROD-SKON-EV-003
    predicate: HAS_SUCCESSOR
    object: PROD-SKON-EV-005
    evidence_type: OFFICIAL_DIRECT
    confidence: HIGH
    source_ids:
      - SRC-SKON-D03-052

  - triple_id: TR-D03-006
    subject: PROD-SKON-EV-006
    predicate: USES_TECHNOLOGY
    object: TECH-SKON-SUFAST
    evidence_type: OFFICIAL_DIRECT
    confidence: HIGH
    source_ids:
      - SRC-SKON-D03-052

  - triple_id: TR-D03-007
    subject: PROD-SKON-EV-009
    predicate: USES_TECHNOLOGY
    object: TECH-SKON-CONFIGURABLE-VENT
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-053

  - triple_id: TR-D03-008
    subject: PROD-SKON-EV-008
    predicate: HAS_FORM_FACTOR
    object: FORM-PRISMATIC
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-054

  - triple_id: TR-D03-009
    subject: PROD-SKON-ESS-002
    predicate: USES_TECHNOLOGY
    object: TECH-SKON-EIS-BMS
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-057

  - triple_id: TR-D03-010
    subject: PROD-SKON-ESS-002
    predicate: USES_TECHNOLOGY
    object: TECH-SKON-COOLANT-IMMERSION
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-057

  - triple_id: TR-D03-011
    subject: PROD-SKON-ESS-003
    predicate: SUPPORTS_ARCHITECTURE
    object: ARCH-DC-BLOCK
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-058

  - triple_id: TR-D03-012
    subject: PROD-SKON-ESS-003
    predicate: SUPPORTS_ARCHITECTURE
    object: ARCH-AC-BLOCK
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-058

  - triple_id: TR-D03-013
    subject: PROD-SKON-NEXT-002
    predicate: CO_DEVELOPED_WITH
    object: PART-SOLID-POWER
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-023
      - SRC-SKON-D03-055

  - triple_id: TR-D03-014
    subject: SERV-SKON-BAAS-001
    predicate: USES_TECHNOLOGY
    object: TECH-SKON-BAAS-AI
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-056

  - triple_id: TR-D03-015
    subject: TECH-SKON-BAAS-AI
    predicate: ESTIMATES
    object: METRIC-BATTERY-RESIDUAL-VALUE
    evidence_type: OFFICIAL_DIRECT
    confidence: VERY_HIGH
    source_ids:
      - SRC-SKON-D03-056

  - triple_id: TR-D03-016
    subject: PROD-SKON-EV-007
    predicate: BENCHMARKED_AGAINST
    object: COMP-LGES-EV-002
    evidence_type: ANALYST_INFERENCE
    confidence: HIGH
    source_ids:
      - SRC-COMP-D03-062

  - triple_id: TR-D03-017
    subject: PROD-SKON-ESS-002
    predicate: BENCHMARKED_AGAINST
    object: COMP-CATL-ESS-001
    evidence_type: ANALYST_INFERENCE
    confidence: HIGH
    source_ids:
      - SRC-COMP-D03-061

  - triple_id: TR-D03-018
    subject: PROD-SKON-ESS-002
    predicate: BENCHMARKED_AGAINST
    object: COMP-SDI-ESS-001
    evidence_type: ANALYST_INFERENCE
    confidence: HIGH
    source_ids:
      - SRC-COMP-D03-063

  - triple_id: TR-D03-019
    subject: PROD-SKON-EV-006
    predicate: HAS_PAIN_POINT
    object: PAIN-LITHIUM-PLATING
    evidence_type: ANALYST_INFERENCE
    confidence: HIGH

  - triple_id: TR-D03-020
    subject: PAIN-LITHIUM-PLATING
    predicate: GENERATES_OI_SEED
    object: OI-SEED-D03-005
    evidence_type: ANALYST_INFERENCE
    confidence: HIGH
```

---
