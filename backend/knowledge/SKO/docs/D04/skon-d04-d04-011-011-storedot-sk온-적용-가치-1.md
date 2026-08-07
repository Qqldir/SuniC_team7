---
id: skon-d04-d04-011-011-storedot-sk온-적용-가치-1
title: 011 — StoreDot — SK온 적용 가치
summary: "StoreDot의 실리콘 초고속 충전 기술이 SK온 Hyper Fast와 어떻게 적용되며, 생산 수율·셀 비용 등 협력 시 해결해야 할 기술적 과제들은 무엇인지 설명한다."
tags: [d04, technology, schema, table, "xref:d17"]
keywords: [실리콘 XFC, 초고속 충전, 기술 벤치마크, 외부 역량 적합, Hyper Fast, 제조 전략, 차량 10분 충전, 충전 프로토콜 최적화, 협력 가치, SUFast, 전극 설계, 차량 충전 시연, 협력 적합도, 생산 수율, 충전 프로토콜, 셀 비용]
related: []
priority: normal
domain: D04
section: D04-011
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 011 — StoreDot
tokens: 3713
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 011 — StoreDot

### SK온 적용 가치

```yaml
benchmark_capabilities:
  - High-silicon fast-charge anode
  - Electrolyte-anode co-design
  - Vehicle-level charging demonstration
  - Fast-charge cycle validation
  - 46xx cylindrical XFC

sk_on_relevance:
  - SF+ silicon-graphite anode
  - Hyper Fast Battery
  - SUFast
  - Charging protocol optimization

principal_gap_questions:
  - Production yield
  - Silicon swelling under pack compression
  - Cell cost
  - OEM nomination
  - Warranty-cycle validation
```

**판정:** `Hyper Fast의 직접 기술 벤치마크`

---

# D04-41. External Capability Comparison Matrix

| 기업              | 핵심 기술            | 가장 강한 검증 근거        | 제조전략         | SK온 적합도 |
| --------------- | ---------------- | ------------------ | ------------ | ------: |
| Solid Power     | 황화물 전해질·셀 공정     | SK온 파일럿 라인 검수 완료   | 소재공급·라이선스    |   매우 높음 |
| Factorial       | FEST·Solstice    | Stellantis 차량 도로시험 | 기존 LIB 설비 활용 |   매우 높음 |
| QuantumScape    | 세라믹 분리막·Li-metal | Cobra B1 샘플        | 자체 분리막 공정    |      높음 |
| Toyota·Idemitsu | 황화물·공급망          | 소재 양산 협력           | OEM 수직통합     |      높음 |
| Samsung SDI     | SolidStack       | 파일럿·고객 샘플·BMW      | 자체 셀 양산      |   매우 높음 |
| LGES            | 무음극·건식전극         | 상용화 로드맵·파일럿        | 기존 라인 활용     |      높음 |
| CATL            | 나트륨이온            | 차량 적용·60GWh ESS    | 대규모 자체생산     |      높음 |
| ProLogium       | 무기계·세라믹·실리콘      | GWh급 시설            | 자체 기술·공장     |   중간~높음 |
| SES AI          | 소재발굴 AI          | AI 소재·서비스 사업       | 소프트웨어+셀      |   매우 높음 |
| 24M             | SemiSolid·ETOP   | 라이선스 플랫폼           | 공정 간소화       |      중간 |
| StoreDot        | 실리콘 XFC          | 차량 10분 충전 시연       | OEM·제조 파트너   |   매우 높음 |

---

# D04-42. SK온 External Capability Fit Map

## 1순위 — 이미 협력관계가 있는 기술

```yaml
priority_1_direct_partners:

  Solid_Power:
    current_relation:
      - Pilot line installed
      - Site acceptance completed
      - Cell and process technology
    next_needed_step:
      - Pilot cell yield validation
      - Continuous electrolyte qualification
      - H2S and moisture control
      - Automotive sample program

  Factorial:
    current_relation:
      - Non-binding manufacturing MOU
    next_needed_step:
      - FEST process-gap analysis
      - Existing equipment reuse assessment
      - Cell and pack sample build
      - Binding JDA decision
```

Solid Power는 이미 설비·공정 이전단계까지 진행됐고, Factorial은 기존 리튬이온 라인 활용 가능성을 검토하는 신규 협력이다. 따라서 두 기업은 경쟁 벤치마크가 아니라 `ACTIVE_OR_EXPLORATORY_PARTNER`로 분리해야 한다. ([Solid Power][1])

---

## 2순위 — 직접 협력 가치가 높은 외부 역량

```yaml
priority_2_high_fit:

  SES_AI:
    capability:
      - Electrolyte molecular discovery
      - Materials AI
    sk_on_link:
      - Materials Development AI Researcher

  StoreDot:
    capability:
      - Silicon fast-charge
      - Vehicle charging validation
    sk_on_link:
      - SUFast and Hyper Fast

  24M:
    capability:
      - Dendrite-resistant separator
      - Direct material recycling
      - ETOP
    sk_on_link:
      - Lithium metal
      - CTP
      - Recycling

  ProLogium:
    capability:
      - Ceramic separator
      - Low-pressure interface
    sk_on_link:
      - LLZO and polymer-oxide battery
```

---

## 3순위 — 경쟁 모니터링·벤치마킹 대상

```yaml
priority_3_benchmark_only:

  Samsung_SDI:
    focus:
      - 2027 commercialization
      - Customer sample validation
      - Solid Power electrolyte integration

  QuantumScape:
    focus:
      - Ceramic separator throughput
      - B-sample quality
      - Lithium-metal architecture

  Toyota_Idemitsu:
    focus:
      - Material supply-chain industrialization
      - OEM-led qualification

  LG_Energy_Solution:
    focus:
      - Anodeless cell
      - Dry-electrode multi-chemistry use

  CATL:
    focus:
      - Alternative chemistry commercialization
      - Large customer contracts
```

---

# D04-43. Technology Positioning Analysis

## 43.1 SK온의 전고체 협력 구조

```text
SK온 자체 연구
├─ Polymer–Oxide Composite
├─ Sulfide ASSB
├─ Lithium-Metal Interface
├─ LMRO
├─ LLZO
└─ Pilot Manufacturing

외부 협력
├─ Solid Power
│   ├─ Sulfide electrolyte
│   ├─ Cell design and process
│   └─ Pilot-line installation
│
└─ Factorial
    ├─ FEST cell technology
    ├─ Existing-line compatibility
    └─ Manufacturing feasibility
```

**ANALYSIS**

Solid Power 협력은 `황화물 소재·셀 공정 확보`, Factorial 협력은 `기존 생산자산을 활용한 산업화 가능성`에 상대적으로 무게가 있다. 두 협력은 중복이라기보다 서로 다른 전고체 상용화 경로에 대한 기술 옵션을 확보하는 구조로 볼 수 있다. ([Solid Power][1])

다만 플랫폼이 늘어날수록 전해질·양극·음극·압력조건과 생산설비가 달라져 연구자원과 파일럿 투자가 분산될 수 있다. D17에서는 각 플랫폼을 동일하게 추진하기보다 고객 적용가능성·기존라인 전환비용·수율·안전·IP 종속성을 기준으로 단계별 중단조건을 설정해야 한다.

---

## 43.2 SK온의 상대적 강점

```yaml
relative_strengths:
  - Direct access to Solid Power technology
  - Completed Solid Power pilot-line acceptance
  - New Factorial manufacturing collaboration option
  - Global pouch manufacturing footprint
  - Polymer-oxide and sulfide dual-track research
  - AI Researcher and manufacturing AI
  - Fast-charge product lineage
  - Pack and ESS safety-system capability
```

---

## 43.3 공개근거상 상대적 약점

```yaml
relative_evidence_gaps:
  - No named SK On solid-state evaluation vehicle
  - No public automotive-scale solid-state cell specification
  - No disclosed B-sample or equivalent status
  - No disclosed pilot-line yield
  - No named solid-state customer validation
  - No definitive commercial plant
  - Commercialization target has changed over time
  - Multiple technology paths may fragment resources
```

Samsung SDI는 고객 샘플과 BMW 평가차량 협력, Factorial은 Stellantis 개발차량 도로시험, QuantumScape는 B1 샘플 출하를 공개했다. 이에 비해 SK온은 파일럿 인프라와 파트너십은 구체적이지만 차량·고객 샘플 단계의 공개근거가 상대적으로 부족하다. ([Samsung SDI][7])

---

# D04-44. External Capability Gap Register

```yaml
external_capability_gaps:

  - gap_id: GAP-D04-EXT-001
    subject: Solid-state technology selection
    gap:
      - Solid Power, Factorial and internal platforms need common decision criteria
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-002
    subject: Automotive validation
    gap:
      - No named SK On solid-state development vehicle
      - No public B-sample equivalent
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-003
    subject: Sulfide electrolyte scale-up
    gap:
      - Continuous production not yet commissioned
      - Cost and purity not disclosed
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-004
    subject: Existing-line compatibility
    gap:
      - Factorial feasibility study not completed
      - Required equipment changes unknown
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-005
    subject: Ceramic electrolyte and separator
    gap:
      - SK On research exists but no commercial process
      - QuantumScape and ProLogium manufacturing evidence requires benchmarking
    priority: HIGH

  - gap_id: GAP-D04-EXT-006
    subject: AI materials discovery
    gap:
      - Materials AI completion status unclear
      - No disclosed closed experiment loop
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-007
    subject: Hyper-fast charging validation
    gap:
      - Hyper Fast has no named vehicle program
      - StoreDot has vehicle demonstration reference
    priority: VERY_HIGH

  - gap_id: GAP-D04-EXT-008
    subject: Alternative chemistry commercialization
    gap:
      - VIB joint product not finalized
      - CATL sodium-ion has named large-scale applications
    priority: HIGH

  - gap_id: GAP-D04-EXT-009
    subject: Technology licensing governance
    gap:
      - IP ownership
      - Improvement ownership
      - Field-of-use rights
      - Partner dependency
    priority: VERY_HIGH
```

---

# D04-45. D17 연결용 External Collaboration OI Seeds

```yaml
oi_seeds:

  - seed_id: OI-SEED-D04-EXT-001
    title: Solid-State Platform Down-Selection Program
    problem:
      - Multiple internal and partner solid-state platforms compete for pilot resources
    candidate_partners:
      - Solid Power
      - Factorial
      - Universities and independent test labs
    deliverable:
      - Common cell specification
      - Common test protocol
      - Technology kill criteria
      - 2027 platform decision
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-002
    title: Factorial–SK On Manufacturing Compatibility PoC
    problem:
      - FEST integration requirements for SK On existing lines are unknown
    poc_scope:
      - Mixing and coating compatibility
      - Stacking and packaging
      - Formation requirements
      - Yield and equipment modification
    collaboration_model:
      - Binding JDA after feasibility gate
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-003
    title: Solid Power Continuous Electrolyte Qualification
    problem:
      - Pilot electrolyte production must meet cell-scale purity and consistency requirements
    poc_scope:
      - Lot uniformity
      - Moisture sensitivity
      - H2S generation
      - Cost and recycle rate
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-004
    title: Automotive Solid-State Demonstration Vehicle
    problem:
      - SK On has no publicly verified solid-state evaluation vehicle
    benchmark:
      - Factorial–Stellantis
      - Samsung SDI–BMW
    collaboration_model:
      - Cell maker–OEM–pack integrator consortium
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-005
    title: AI Electrolyte Discovery Partnership
    problem:
      - Electrolyte and additive discovery remains experiment intensive
    benchmark_partner:
      - SES AI
    sk_on_asset:
      - Materials Development AI Researcher
      - Internal cell and process data
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-006
    title: Silicon XFC Joint Validation
    problem:
      - Hyper Fast commercialization requires silicon expansion and vehicle-level validation
    benchmark:
      - StoreDot
    poc_scope:
      - Silicon composition
      - Electrolyte and charging protocol
      - Low-temperature charging
      - Pack thermal performance
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-007
    title: Solid-State Interface NDI Consortium
    problem:
      - Buried ceramic and sulfide interface defects are difficult to inspect
    benchmark:
      - QuantumScape
      - ProLogium
    external_capability:
      - X-Ray CT
      - Ultrasound
      - Acoustic microscopy
      - AI reconstruction
    priority: VERY_HIGH

  - seed_id: OI-SEED-D04-EXT-008
    title: Alternative Chemistry Commercial Launch Model
    problem:
      - SK On VIB technology requires a clear product, customer and production pathway
    benchmark:
      - CATL Naxtra
    collaboration:
      - Standard Energy
      - SK Innovation material recovery
      - Data-center or industrial customer
    priority: HIGH

  - seed_id: OI-SEED-D04-EXT-009
    title: Modular Technology Licensing Framework
    problem:
      - External technologies create IP and supplier-dependency risks
    benchmark:
      - Solid Power
      - 24M
    required_terms:
      - Field-of-use rights
      - Improvement IP
      - Dual sourcing
      - Termination and technology transfer
      - Production geography
    priority: VERY_HIGH
```

---

## 이번 구간 완료

* Source Grade 정규화 기준 확정
* 외부 Benchmark Source `SRC-EXT-D04-052~063` 등록
* `D04-39 Technology Benchmark Taxonomy`
* 외부 기술 Benchmark Master
