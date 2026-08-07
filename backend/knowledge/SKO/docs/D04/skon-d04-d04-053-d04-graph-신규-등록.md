---
id: skon-d04-d04-053-d04-graph-신규-등록
title: D04 Graph 신규 등록
summary: "SK온-Factorial 고체전지 협력 내용, FEST 셀 차량 성능 검증, 그리고 배터리 기술 벤치마크 분류표를 제시한다."
tags: [d04, technology, schema]
keywords: [Factorial, FEST, 고체상태 배터리, 실차 검증, Stellantis, 벤치마크, MOU, 빠른 충전, XFC, 고체전지, Solid-State, 초고속충전, 차량통합, 중에너지밀도]
related: []
priority: normal
domain: D04
section: D04-053
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: 008. External Benchmark Source Library > D04-053 — Factorial·SK온 신규 MOU
tokens: 1074
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · 008. External Benchmark Source Library > D04-053 — Factorial·SK온 신규 MOU

### D04 Graph 신규 등록

```text
CO-SKON
├─ OPERATES_PILOT_LINE_WITH_TECHNOLOGY_FROM → PART-SOLID-POWER
└─ EXPLORES_MANUFACTURING_WITH → PART-FACTORIAL

PART-FACTORIAL
├─ OWNS → TECH-FACTORIAL-FEST
├─ OWNS → TECH-FACTORIAL-SOLSTICE
└─ HAS_RELATION_STATUS → NON_BINDING_MOU
```

---

## SRC-EXT-D04-054 — Factorial 차량 통합 검증

```yaml
source_id: SRC-EXT-D04-054
title: Stellantis and Factorial Integrate Advanced Solid-State Battery into Development Vehicle
publisher:
  - Factorial
  - Stellantis
publication_date: 2026-06-11
access_date: 2026-08-01
reliability_grade: A

confirmed_validation:
  vehicle: Dodge Charger Daytona Development Vehicle
  technology: FEST
  activity:
    - Cell-to-pack integration
    - Vehicle control calibration
    - Road testing

previous_cell_results:
  cell_capacity: 77_Ah
  gravimetric_energy_density: 375_Wh_per_kg
  charging: 15_to_90_percent_in_18_minutes
  temperature_range: minus_30_to_45_C
  claim_boundary: Company and OEM laboratory result
```

Factorial의 FEST 셀은 Stellantis의 Dodge Charger Daytona 개발차량에 실제 탑재돼 2026년 도로시험을 시작했다. 2025년 셀 시험에서는 77Ah, 375Wh/kg, 15%에서 90%까지 18분 충전 및 영하 30℃에서 45℃ 범위의 운전 결과가 제시됐지만, 이는 Factorial·Stellantis가 발표한 시험 결과이며 양산차 보증사양은 아니다. ([Factorial Energy][3])

---

# D04-39. Technology Benchmark Taxonomy

```text
External Technology Benchmark Universe
│
├── B01 Sulfide Solid-State Material & Licensing
│   ├── Solid Power
│   ├── Toyota–Idemitsu
│   └── Samsung SDI–Solid Power
│
├── B02 Lithium-Metal Ceramic Separator
│   ├── QuantumScape
│   └── ProLogium
│
├── B03 Manufacturing-Compatible Solid-State
│   ├── Factorial FEST
│   ├── 24M SemiSolid
│   └── LGES Dry-Electrode / Anodeless
│
├── B04 Automotive Validation
│   ├── Factorial–Stellantis
│   ├── Factorial–Mercedes-Benz
│   ├── Samsung SDI–BMW
│   └── Toyota Material Supply Chain
│
├── B05 Fast-Charging Materials
│   ├── StoreDot Silicon-Dominant XFC
│   ├── CATL Shenxing
│   └── Factorial FEST
│
├── B06 Alternative Chemistry
│   ├── CATL Sodium-Ion
│   ├── SK On–Standard Energy VIB
│   └── LGES Sodium-Ion / Lithium-Sulfur
│
├── B07 AI Battery Intelligence
│   ├── SES AI Molecular Universe
│   ├── Factorial Gammatron AI
│   ├── SK On AI Researcher
│   └── LGES Materials Informatics
│
└── B08 Manufacturing & Architecture
    ├── 24M SemiSolid
    ├── 24M ETOP
    ├── ProLogium Ceramic Platform
    ├── Solid Power Electrolyte Licensing
    └── Factorial Existing-Line Compatibility
```

---

# D04-40. External Benchmark Master

## BENCH-D04-001 — Solid Power

```yaml
benchmark_id: BENCH-D04-001
company: Solid Power

core_platform:
  - Sulfide solid electrolyte
  - Solid-state cell design
  - Process and cell-technology licensing

business_model:
  - Electrolyte material supply
  - Technology licensing
  - Partner pilot-line installation
  - Joint cell development

technology_maturity:
  electrolyte: PILOT_CONTINUOUS_PRODUCTION_DEVELOPMENT
  cell: PARTNER_PILOT_VALIDATION
  commercial_ev: NOT_CONFIRMED

sk_on_relationship:
  status: DIRECT_ACTIVE_TECHNOLOGY_PARTNER
  evidence:
    - Pilot-line installation
    - Site-acceptance testing completed
    - Cell-design and process access
```

Solid Power의 차별점은 완성 배터리 제조사로 직접 대규모 공장을 소유하기보다, 황화물 전해질 공급과 셀 설계·공정 라이선스를 기존 배터리 제조사에 제공하는 구조다. SK온은 이 모델을 통해 자체 파일럿 라인에서 Solid Power 기술을 시험할 수 있다. ([Solid Power][1])
