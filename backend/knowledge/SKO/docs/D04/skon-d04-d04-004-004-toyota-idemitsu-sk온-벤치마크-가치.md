---
id: skon-d04-d04-004-004-toyota-idemitsu-sk온-벤치마크-가치
title: 004 — Toyota·Idemitsu — SK온 벤치마크 가치
summary: 전고체 배터리 개발에서 Toyota·Idemitsu의 공급망 통합과 차량 검증 역량을 분석하고 SK온의 기술 격차를 진단하는 벤치마크
tags: [d04, technology, schema]
keywords: [전고체배터리, ASSB, 고체전해질, 공급망 통합, OEM 협력, Samsung SDI, SolidStack, 양산 목표, 전고체 배터리, 황화물 전해질, 벤치마크, Solid Power, 차량 검증]
related: []
priority: normal
domain: D04
section: D04-004
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 004 — Toyota·Idemitsu
tokens: 555
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 004 — Toyota·Idemitsu

### SK온 벤치마크 가치

```yaml
benchmark_capabilities:
  - Material-to-vehicle vertical coordination
  - Sulfide electrolyte supply chain
  - Automotive qualification
  - Cathode-electrolyte co-development
  - Long-term supplier integration

sk_on_gap_implication:
  - Solid Power electrolyte dependence requires dual sourcing
  - Cathode and electrolyte must be validated as one interface system
  - Vehicle-level partner involvement should begin before final cell design
```

**판정:** `공급망·OEM 통합 벤치마크`

---

## BENCH-D04-005 — Samsung SDI SolidStack

```yaml
benchmark_id: BENCH-D04-005
company: Samsung SDI
platform_name: SolidStack

core_platform:
  - Sulfide all-solid-state battery
  - Anode-free or advanced-anode architecture
  - Prismatic ASSB
  - Pouch ASSB for robotics

technology_maturity:
  pilot_line:
    name: S-Line
    operation_start: 2023_PROTOTYPE_PRODUCTION

  customer_samples: TESTING_WITH_MULTIPLE_CUSTOMERS
  mass_production_target: 2027_H2

manufacturer_claim:
  volumetric_energy_density:
    value: 900
    unit: Wh_per_L
```

Samsung SDI는 2023년 S-Line 전고체 파일럿 라인을 구축하고 시제품 생산을 시작했으며, 복수 고객과 샘플 검증을 진행하고 있다. 2026년에는 전고체 브랜드를 `SolidStack`으로 명명하고 각형 EV용뿐 아니라 로봇용 파우치형까지 폼팩터를 확대했으며, 2027년 하반기 양산을 목표로 제시했다. ([Samsung SDI][6])

Samsung SDI는 BMW·Solid Power와 협력해 Solid Power의 고체전해질을 적용한 Samsung SDI 셀, BMW 모듈·팩 및 평가차량을 연결하는 검증체계를 구축했다. 이는 소재기업·셀 제조사·OEM의 역할을 분리하면서도 차량검증까지 연결한 사례다. ([Samsung SDI][7])
