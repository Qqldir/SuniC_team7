---
id: skon-d04-d04-001-001-solid-power-sk온-적용-가치
title: 001 — Solid Power — SK온 적용 가치
summary: "Solid Power 고체 전해질 기술의 SK온 적용 가치와 리스크 요소, 그리고 Factorial의 전고체 배터리 기술 플랫폼 벤치마킹 현황을 정리한 문서."
tags: [d04, technology, schema]
keywords: [전고체배터리, 황화물 전해질, 기술성숙도, 양산화, Factorial, FEST, 호환성, 공정수율, 고체전해질, 양산수율, 벤치마크, MOU, Stellantis, 차량통합]
related: []
priority: normal
domain: D04
section: D04-001
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 001 — Solid Power
tokens: 513
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 001 — Solid Power

### SK온 적용 가치

```yaml
applicable_capabilities:
  - Sulfide electrolyte formulation
  - Pilot-cell process design
  - Large-area electrolyte processing
  - Process transfer and licensing
  - Continuous electrolyte production

principal_risks:
  - Electrolyte cost
  - Moisture sensitivity
  - H2S management
  - Partner-technology dependency
  - Pilot-to-commercial yield
```

**판정:** `최우선 직접 파트너`

---

## BENCH-D04-002 — Factorial

```yaml
benchmark_id: BENCH-D04-002
company: Factorial

technology_platforms:
  FEST:
    type: Quasi-Solid-State or Solid-State Platform
    manufacturing_strategy:
      - Compatibility with existing lithium-ion infrastructure
      - Reduced greenfield-capital requirement

  Solstice:
    type: All-Solid-State Platform

  Gammatron:
    type: Battery AI Platform

technology_maturity:
  cell_validation: AUTOMOTIVE_SCALE
  vehicle_integration: DEVELOPMENT_VEHICLE_ROAD_TEST
  mass_production: NOT_CONFIRMED

sk_on_relationship:
  status: NEW_NON_BINDING_MOU
  effective_date: 2026-07-29
```

Factorial은 기존 리튬이온 생산설비와의 호환성을 산업화 전략으로 강조한다. SK온과의 MOU 역시 FEST를 기존 SK온 생산 인프라에 통합할 기술적·제조적 가능성을 평가하는 데 초점이 있다. ([Factorial Energy][2])

FEST는 Stellantis 개발차량에 통합돼 도로시험 단계에 진입했다는 점에서, 아직 파일럿 셀 검증 중심인 여러 전고체 기술보다 차량·팩 통합 근거가 구체적이다. 다만 해당 시험이 양산원가, 공정수율 및 장기보증을 입증한 것은 아니다. ([Factorial Energy][3])
