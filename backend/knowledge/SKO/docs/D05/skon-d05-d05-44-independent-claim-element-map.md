---
id: skon-d05-d05-44-independent-claim-element-map
title: Independent-Claim Element Map
summary: 배터리 특허 청구항의 기술요소 구성과 설계변경 가능성을 정리한 분석표
tags: [d05, rnd, schema, "xref:d04"]
keywords: [배터리 청구항, 기술요소 분석, Z-폴딩, 분리막, 열차단 구조, 설계우회, 배터리 모듈, 특허족, 청구항, 기술요소, 특허가족, 설계변경, Z폴딩, 열차단, 배터리원장]
related: []
priority: normal
domain: D05
section: D05-44.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 2325
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-44. Independent-Claim Element Map

> 아래 표는 공개 청구항을 기술요소 단위로 정리한 사전 분석이며 법률적 Claim Construction이 아니다.

## 44.1 Claim Element Schema

```yaml
claim_element_schema:

  claim_map_id: required
  patent_family_id: required
  jurisdiction: required
  claim_number: optional

  elements:
    - element_id
    - normalized_element
    - technical_function
    - required_or_optional

  protected_problem:
    type: string

  possible_design_around:
    type: array

  product_implementation_evidence:
    allowed_values:
      - DIRECT
      - INDIRECT
      - TECHNICAL_MATCH_ONLY
      - NONE

  legal_review_required: true
```

---

## CLM-D05-001 — Modern Z-Folding

```yaml
claim_map_id: CLM-D05-001
patent_family_id: PF-SKON-D05-024

protected_problem:
  - Electrode misalignment
  - Exposure of outer cathode surface
  - Internal-short risk
  - Stack-edge protection

elements:
  E1:
    normalized_element: Continuous separator
    function: Electrical isolation

  E2:
    normalized_element: Zigzag-folded separator
    function: Sequential electrode stacking

  E3:
    normalized_element: Alternating positive and negative plates
    function: Electrochemical cell formation

  E4:
    normalized_element: Negative plates at upper and lower outer surfaces
    function: Outer-surface safety

  E5:
    normalized_element: Separator surrounding outer stack
    function: Edge insulation

implementation_relation:
  technology: TECH-SKON-D04-022
  evidence: TECHNICAL_MATCH_ONLY

possible_design_around:
  - Discrete separator sheets
  - Lamination-based stacking
  - Different outer-electrode sequence
  - Winding or stack-and-fold architecture
```

공개출원은 연속 분리막의 지그재그 적층과 최외곽 음극판 구성을 주요 요소로 포함한다. 실제 SK온 양산라인이 모든 청구요소를 실시하는지는 공개자료만으로 확인되지 않는다. ([구글 특허][3])

---

## CLM-D05-002 — Thermal Barrier

```yaml
claim_map_id: CLM-D05-002
patent_family_id: PF-SKON-D05-020

protected_problem:
  - Heat transfer from abnormal cell block
  - Thermal propagation between cell groups

elements:
  E1:
    normalized_element: Multiple battery-cell blocks
    function: Module segmentation

  E2:
    normalized_element: Barrier positioned between cell blocks
    function: Thermal isolation

  E3:
    normalized_element: Cell assembly containing blocks and barrier
    function: Integrated safety structure

  E4:
    normalized_element: Housing containing cell assembly
    function: Module containment

implementation_relation:
  products:
    - S-Pack
    - S-Pack+
  evidence: TECHNICAL_MATCH_ONLY

possible_design_around:
  - Cell-level barrier rather than block-level barrier
  - Cooling-channel isolation
  - Intumescent coating
  - Structural air gap
  - Vent-first propagation control
```

이 특허의 중심은 배터리 모듈에 단열재가 존재한다는 넓은 개념보다, 복수 셀 블록 사이에 특정 차단부재를 배치하는 구조적 조합에 있다. ([구글 특허][4])

---

## CLM-D05-003 — Battery Ledger

```yaml
claim_map_id: CLM-D05-003
patent_family_id: PF-SKON-D05-006

protected_problem:
  - Fragmented battery lifecycle data
  - Inability to identify battery across owners and uses
  - Incomplete residual-value and maintenance history

elements:
  E1:
    normalized_element: Battery production information input
    function: Manufacturing origin registration

  E2:
    normalized_element: Unique battery ID generation
    function: Persistent battery identity

  E3:
    normalized_element: State-information management
    function: SOC, SOH or current-state tracking

  E4:
    normalized_element: Usage-information management
    function: Charging, driving and operation history

  E5:
    normalized_element: Maintenance and replacement history
    function: Lifecycle-event tracking

implementation_relation:
  technologies:
    - BaaS AI
    - Battery Passport Data Architecture
  evidence: TECHNICAL_MATCH_ONLY

possible_design_around:
  - Vehicle-level rather than battery-level identity
  - Decentralized credential architecture
  - Event-based data exchange without central ledger
  - Privacy-preserving federated lifecycle records
```

Battery Ledger의 독립적 기술가치는 블록체인 사용 여부가 아니라 배터리 고유 ID를 중심으로 생산·상태·사용이력을 연결하는 데이터 객체 구조에 있다. ([구글 특허][5])

---

## CLM-D05-004 — AI Fault Detection

```yaml
claim_map_id: CLM-D05-004
patent_family_id: PF-SKON-D05-007

protected_problem:
  - Detection of individual abnormal cells in a multi-cell pack
  - Joint use of temporal and cross-cell deviation patterns

elements:
  E1:
    normalized_element: Cell data measured for a defined period
    function: Time-series collection

  E2:
    normalized_element: Two-dimensional input data
    function: Structured model input

  E3:
    normalized_element: Time axis
    function: Temporal-pattern retention

  E4:
    normalized_element: Cell-index axis
    function: Cross-cell comparison

  E5:
    normalized_element: Pre-trained detection model
    function: Anomaly inference

  E6:
    normalized_element: Abnormal-cell determination
    function: Safety decision

implementation_relation:
  technologies:
    - Multi-Layer Battery Abnormality Detection
    - Predictive Quality Intelligence
  evidence: TECHNICAL_MATCH_ONLY

possible_design_around:
  - Graph neural-network representation
  - One-dimensional per-cell model
  - Physics-residual model
  - Frequency-domain feature model
  - Event-driven probabilistic detector
```

청구범위 분석에서 핵심 차별점은 일반적인 AI 이상감지가 아니라 시간축과 셀 인덱스축을 결합한 2차원 입력 표현이다. ([구글 특허][6])

---

## CLM-D05-005 — ASSB Composite Cathode

```yaml
claim_map_id: CLM-D05-005
patent_family_id: PF-SKON-D05-011

protected_problem:
  - Poor dispersion in sulfide composite cathode
  - Chemical instability of binder
  - Reduced ionic conduction
  - Cathode–electrolyte contact degradation

elements_high_level:
  - Cathode active material
  - Sulfide solid electrolyte
  - Rubber-based binder system
  - Composite cathode
  - All-solid-state battery including the composite cathode

implementation_relation:
  technologies:
    - Sulfide ASSB
    - Solid–Solid Interface Engineering
  evidence: RESEARCH_AND_TECHNICAL_MATCH_ONLY

possible_design_around:
  - Different binder chemistry
  - Binder-free cathode
  - Gradient binder distribution
  - Dry composite-cathode processing
  - Surface-treated electrolyte particles
```

EP4651239A1은 황화물 전해질을 사용하는 복합양극을 대상으로 하지만, 정확한 청구요소와 허용범위는 향후 심사과정에서 변경될 수 있다. ([EPO Data][8])

---

## CLM-D05-006 — Li-Metal·Glass Electrolyte Laminate

```yaml
claim_map_id: CLM-D05-006
patent_family_id: PF-SKON-D05-012

protected_problem:
  - High lithium-metal and electrolyte interfacial resistance
  - Weak adhesion
  - Contact loss when external pressure is removed

elements_high_level:
  - Lithium-containing metal foil
  - Sulfide glass-electrolyte film
  - Direct contact between the layers
  - Heat-and-pressure lamination
  - All-solid-state cell using the laminate

implementation_relation:
  technology:
    - Lithium-Metal Anode Platform
    - Sulfide Solid Electrolyte
    - Solid–Solid Interface Engineering
  evidence: JOINT_RESEARCH_TECHNICAL_MATCH

possible_design_around:
  - Artificial intermediate layer
  - Vapor-deposited lithium
  - In-situ lithium formation
  - Polymer-buffer interface
  - Different glass-ceramic electrolyte
```

이 패밀리는 리튬메탈과 황화물 유리 전해질의 직접 적층이라는 구체적 계면 형성방식에 집중돼 있다. ([구글 특허][9])

---
