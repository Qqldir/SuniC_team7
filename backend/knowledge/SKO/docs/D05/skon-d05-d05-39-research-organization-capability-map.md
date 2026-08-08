---
id: skon-d05-d05-39-research-organization-capability-map
title: Research Organization Capability Map
summary: "배터리 소재·공정·안전 등 10개 기술 영역의 성숙도와 공개 성과를 매핑하고, 5개 핵심 역량의 증거와 체계를 정리한 문서"
tags: [d05, rnd, schema, table]
keywords: [역량맵, 전고체, 급속충전, 산화물, 황화물, 리튬메탈, CTP, EIS, 성숙도, 기술이전, 배터리 역량, 기술 성숙도, 산화물 전고체, 공개성과]
related: []
priority: normal
domain: D05
section: D05-39.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1413
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-39. Research Organization Capability Map

## 39.1 Capability Layers

| Capability Cluster | 공개 성과          | 증거 단계  |   잠정 수준 |
| ------------------ | -------------- | ------ | ------: |
| 하이니켈·단결정 양극        | 논문·복수 특허       | 연구셀·특허 |      강함 |
| 산화물 전고체            | 논문·특허·파일럿 연결   | 소재·공정  |      강함 |
| 황화물 전고체            | 파일럿·외부 기술이전    | 파일럿    |      강함 |
| 리튬메탈 계면            | 논문             | 연구셀    |    성장 중 |
| 실리콘 급속충전 음극        | 제품기술·특허        | 상용·개발  |      강함 |
| 건식전극               | 특허·개발공정        | 파일럿    |    성장 중 |
| EIS·BaaS           | 제품·특허·서비스      | 시스템    |      강함 |
| CTP·각형             | 복수 구조특허·시제품    | 시제품    |    성장 중 |
| 제조검사               | X-ray·검사시스템 특허 | 공정개발   |    성장 중 |
| AI Researcher      | 내부 플랫폼 공개      | 내부운영   | 평가자료 부족 |

---

## 39.2 Capability Entity Master

```yaml
research_capability_master:

  - capability_id: CAP-SKON-D05-001
    canonical_name: Oxide Solid-State Material-to-Process Capability
    evidence:
      - Photonic-sintering paper
      - Oxide thin-film patent
      - LLZO joint patent
      - Solid-state pilot facility
    capability_chain:
      - Material formulation
      - Thin-film formation
      - Photonic sintering
      - Electrolyte-sheet characterization
      - Research-cell integration
    maturity: LAB_TO_PILOT_TRANSITION
    confidence: HIGH

  - capability_id: CAP-SKON-D05-002
    canonical_name: Fast-Charging Electrode Co-Design Capability
    evidence:
      - Commercial SF lineage
      - Fast-charging patent family
      - Silicon multilayer patent family
      - Charging-protocol technology
    capability_chain:
      - Material
      - Electrode architecture
      - Manufacturing
      - Charging control
    maturity: COMMERCIAL_AND_NEXT_GENERATION
    confidence: HIGH

  - capability_id: CAP-SKON-D05-003
    canonical_name: Battery Safety Architecture Capability
    evidence:
      - Thermal-barrier families
      - Vent families
      - CTP thermal-path families
      - EIS abnormality patent
    capability_chain:
      - Detect
      - Vent
      - Block heat
      - Control gas
      - Contain propagation
    maturity: PRODUCT_AND_PROTOTYPE
    confidence: HIGH

  - capability_id: CAP-SKON-D05-004
    canonical_name: Battery Lifecycle Intelligence Capability
    evidence:
      - SOH patent
      - Battery ledger patent
      - AI fault-detection patent
      - EIS patent
      - BaaS service
    maturity: SYSTEM_AND_SERVICE
    confidence: HIGH

  - capability_id: CAP-SKON-D05-005
    canonical_name: Multi-Form-Factor Pack Integration Capability
    evidence:
      - Pouch direct-to-pack patent
      - Corner-lead pouch patent
      - CTP thermal-path patent
      - On-Vent prismatic patent
    maturity: PROTOTYPE_AND_IP_PORTFOLIO
    confidence: HIGH
```

---

## 39.3 Capability Gap Analysis

**FACT**

급속충전, 산화물 전고체, 열전파 방지, EIS 진단과 CTP 분야에는 제품·논문·특허 중 최소 두 종류 이상의 공개성과가 연결된다. 반면 AI Researcher는 공식 플랫폼 공개는 있으나 논문·직접 특허·정량 정확도 자료가 부족하다.

**ANALYSIS**

공개 포트폴리오상 SK온의 강점은 단일 소재 특허보다 `소재 → 전극·셀 설계 → 팩 구조 → 진단`을 연결하는 계층형 IP에 있다. 다만 연구논문과 특허가 파일럿 수율·고객 샘플·상용제품으로 전환됐는지를 보여주는 중간 데이터가 부족하다.

```yaml
research_capability_gaps:

  - gap_id: GAP-D05-CAP-001
    subject: Paper-to-pilot conversion
    missing:
      - Pilot experiment ID
      - Scale-up lot
      - Yield
      - Process window
    priority: VERY_HIGH

  - gap_id: GAP-D05-CAP-002
    subject: Patent-to-product implementation
    missing:
      - Claim-to-BOM mapping
      - Product implementation record
      - Customer nomination
    priority: VERY_HIGH

  - gap_id: GAP-D05-CAP-003
    subject: Researcher succession
    missing:
      - Backup technical owner
      - Tacit-knowledge transfer
      - Cross-project staffing
    priority: HIGH

  - gap_id: GAP-D05-CAP-004
    subject: AI R&D evidence
    missing:
      - Patent families
      - Model architecture
      - Prediction accuracy
      - Researcher adoption
    priority: VERY_HIGH
```

---
