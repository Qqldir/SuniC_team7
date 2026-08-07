---
id: skon-d04-d04-010-010-24m-technologies-sk온-적용-가치
title: 010 — 24M Technologies — SK온 적용 가치
summary: 24M의 혁신 전극 제조·분리막 기술과 StoreDot의 초고속 충전 시연이 SK온 배터리 개발 전략과 부합하는지 평가한 외부 벤치마크.
tags: [d04, technology, schema]
keywords: [극초고속충전, 실리콘음극, StoreDot, 100inX, 바인더리스전극, 덴드라이트차단, 기술성숙도, Extreme Fast Charging, 에너지밀도, 라이선스형공정, 24M Technologies, 바인더 없는 전극, 극초고속 충전, 실리콘 음극, 분리막, 라이선스 공정, Polestar]
related: []
priority: normal
domain: D04
section: D04-010
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 010 — 24M Technologies
tokens: 551
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 010 — 24M Technologies

### SK온 적용 가치

```yaml
applicable_capabilities:
  - Simplified electrode manufacturing
  - Binderless electrode
  - Dendrite-blocking separator
  - Internal-short early detection
  - Electrode-to-pack
  - Direct active-material reuse

potential_conflicts:
  - SemiSolid process differs from SK On wet and dry electrode roadmap
  - ETOP reduces conventional cell and module boundaries
  - Adoption may require major product and process redesign
```

**판정:** `라이선스형 공정·구조 혁신 벤치마크`

---

## BENCH-D04-011 — StoreDot

```yaml
benchmark_id: BENCH-D04-011
company: StoreDot

core_platform:
  - Silicon-dominant anode
  - Extreme Fast Charging
  - Electrode-specific electrolyte
  - 100inX roadmap

technology_maturity:
  large_cell_samples: OEM_TESTING
  vehicle_demonstration: COMPLETED
  mass_production: NOT_CONFIRMED
  UN38_3_transport_certification:
    form_factor: 46xx
    year: 2025

vehicle_demonstration:
  partner: Polestar
  pack_energy: 77_kWh
  charge_window: 10_to_80_percent
  time: less_than_10_minutes
  cell_energy_density: 300_Wh_per_kg
  claim_boundary: Demonstration vehicle
```

StoreDot은 Polestar 5 기반 개발차량에서 77kWh 팩을 10%에서 80%까지 10분 미만에 충전하는 시연을 실시했다. 적용 셀은 실리콘 중심 음극과 300Wh/kg의 셀 에너지밀도를 사용한 것으로 발표됐으며, 이는 양산차가 아닌 시험용 차량의 시연 결과다. ([StoreDot][18])

StoreDot의 `100inX`는 5분·4분 등 일정 시간 동안 100마일의 주행거리를 추가한다는 로드맵이며, 배터리를 완전히 충전하는 시간이 아니다. 2026년 100마일·4분은 기술 로드맵으로 관리하고 실제 고객 양산은 별도 검증해야 한다. ([StoreDot][19])
