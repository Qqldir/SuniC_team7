---
id: skon-d05-d05-51-design-around-opportunity-map
title: Design-Around Opportunity Map
summary: 배터리 드라이전극·실리콘·전고체·열관리 등 핵심 기술별로 경쟁사 특허 밀집 영역을 파악하고 SK온의 우회설계 차별화 전략을 수립하기 위한 기술 로드맵
tags: [d05, rnd, schema]
keywords: [설계우회, Design-Around, 건식전극, 실리콘 음극, 황화물 전고체전지, ASSB, 특허 회피, 차별화 전략, 아지로다이트, 인라인 센싱, 특허 포화, 드라이 전극, 전고체 배터리, 우회 설계, 차별화, White Space, 센싱]
related: []
priority: normal
domain: D05
section: D05-51.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1878
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-51. Design-Around Opportunity Map

## DA-D05-001 — Dry Electrode

```yaml
design_around_id: DA-D05-001
technology: Dry Electrode

dense_claim_zones:
  - PTFE fibrillation
  - Free-standing dry film
  - Dry film lamination to current collector
  - Extrusion and preforming rolls
  - Conventional calender stack

design_around_candidates:
  - Non-PTFE functional binder
  - Powder deposition directly onto primed collector
  - Binder-gradient electrode
  - Electrostatic powder deposition
  - In-situ surface activation
  - Sensor-controlled asymmetric rolling
  - Defect-responsive adaptive calendering

sk_on_priority:
  - Inline porosity
  - Adhesion sensing
  - Powder genealogy
  - AI control

risk: VERY_HIGH
```

LG에너지솔루션의 필름·압출·분체코팅과 Samsung SDI의 비대칭 롤 제어 표본을 고려하면, 단순히 “용매를 사용하지 않는 전극”만으로는 차별화가 어렵다. SK온은 소재조성보다 인라인 센싱과 폐루프 제어, 불량원인 추적을 독립 권리층으로 형성하는 방향이 유리하다. ([구글 특허][1])

---

## DA-D05-002 — Silicon Fast Charging

```yaml
design_around_id: DA-D05-002
technology: Silicon Fast-Charging Anode

dense_claim_zones:
  - Porous silicon-carbon composites
  - Silicon particle coating
  - High-silicon large-format electrode
  - Multilayer silicon–graphite electrode
  - Prelithiation and initial-loss compensation

design_around_candidates:
  - Spatially graded silicon concentration
  - Patterned expansion-relief zones
  - Layer-specific binder system
  - Local current-density redistribution
  - Reversible compression control
  - Electrolyte–protocol co-optimization

sk_on_differentiation:
  - Dual-layer architecture
  - Charging protocol
  - Pack thermal management
```

실리콘 소재 자체의 구조·제조 특허가 Sila·Group14·Enevate 등에 밀집돼 있으므로, SK온은 독자 소재권리보다 `층별 실리콘 농도`, `저항분포`, `충전전류 제어`와 `팩 압력·열관리`를 결합한 셀 시스템 청구를 강화하는 것이 상대적으로 현실적이다. ([구글 특허][4])

---

## DA-D05-003 — Sulfide ASSB

```yaml
design_around_id: DA-D05-003
technology: Sulfide All-Solid-State Battery

dense_claim_zones:
  - Argyrodite composition
  - Halogen ratio
  - Particle synthesis and crystallization
  - Surface coating
  - Composite cathode binder
  - Lithium-metal interface
  - Stack pressure

design_around_candidates:
  - Dual-electrolyte architecture
  - Gradient sulfide composition
  - Polymer-buffered interface
  - Binder-free dry composite cathode
  - Low-pressure compliant interlayer
  - Non-contact pressure monitoring
  - Interface-specific NDI

sk_on_priority:
  - Solid Power improvement IP
  - Composite-cathode process
  - Lightweight pressure management
  - Interface inspection
```

황화물 전해질은 Toyota·Idemitsu·Samsung SDI·LGES·Solid Power의 소재 및 제조 특허가 겹치는 고밀도 영역이다. SK온의 독자 White Space는 새로운 아지로다이트 조성 자체보다 `파일럿 공정조건`, `복합양극 제조`, `저압 계면`, `검사·수명예측`에서 찾는 편이 적절하다. ([구글 특허][9])

---

## DA-D05-004 — Thermal Propagation

```yaml
design_around_id: DA-D05-004
technology: Thermal Propagation Prevention

dense_claim_zones:
  - Barrier between cells or blocks
  - Aerogel or inorganic insulation
  - Intumescent layer
  - Gas vent channel
  - Module enclosure and cover

design_around_candidates:
  - Adaptive thermal isolation
  - Triggered coolant release
  - Replaceable barrier cassette
  - Sensor-integrated thermal pad
  - Reworkable barrier structure
  - Vent-gas heat exchanger
  - Gas-composition-based response

sk_on_priority:
  - Detection–vent–barrier integrated control
  - CTP repairability
  - Barrier health monitoring
```

단열재 조성과 단순 셀간 배치에는 기존 선행권리가 많다. 따라서 SK온은 차단재 자체보다 감지센서, 방향성 배기, 냉각·격리 동작을 연계한 시스템 제어와 유지보수 가능한 CTP 구조를 권리화할 필요가 있다. ([구글 특허][12])

---

## DA-D05-005 — EIS Diagnostics

```yaml
design_around_id: DA-D05-005
technology: EIS Battery Diagnostics

dense_claim_zones:
  - Impedance excitation
  - Charger-based signal generation
  - Equivalent-circuit fitting
  - SOC, SOH and temperature estimation
  - Early short and failure detection

design_around_candidates:
  - Passive operational excitation
  - Sparse-frequency adaptive selection
  - Multi-cell transfer learning
  - Physics-residual anomaly score
  - EIS–gas–acoustic multimodal diagnosis
  - Confidence-aware safety response

sk_on_priority:
  - ESS multimodal diagnosis
  - Low-cost edge implementation
  - False-alarm control
```

Ford 계열 표본은 온보드 충전기와 BMS를 이용한 EIS에, SK온은 임피던스 특징과 등가회로 파라미터를 이용한 이상판정에 초점을 둔다. SK온의 차별화 기회는 측정 자체보다 ESS 필드데이터와 가스·음향센서를 결합한 원인분류 및 오탐 제어에 있다. ([구글 특허][15])

---

## DA-D05-006 — Battery Passport

```yaml
design_around_id: DA-D05-006
technology: Battery Passport

dense_claim_zones:
  - Unique battery identity
  - Central lifecycle ledger
  - Blockchain-based usage record
  - Product passport and decentralized identity
  - Material environmental attributes

design_around_candidates:
  - Federated passport
  - Selective disclosure
  - Zero-knowledge proof
  - Role-based data credential
  - Off-chain raw data with signed summaries
  - Dispute and correction workflow
  - Privacy-preserving residual-value calculation

sk_on_priority:
  - Battery-specific health credential
  - Recycler and used-EV access policy
  - SOH proof without raw-data disclosure
```

SK온은 배터리 ID와 사용이력을 중심으로 한 강점을 유지하되, BASF식 소재 Passport나 Toyota식 분산원장 구조와 직접 중첩되지 않도록 선택적 공개와 검증가능 자격증명 방식으로 확장할 수 있다. ([구글 특허][17])

---
