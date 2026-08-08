---
id: skon-d04-d04-007-007-catl-naxtra-sk온-적용-가치
title: 007 — CATL Naxtra — SK온 적용 가치
summary: 비리튬 저온 배터리의 상용화 진행 현황과 SK온의 ESS 및 대체 화학 포트폴리오 구축에서의 활용 가치를 평가한 벤치마크 분석 문서다.
tags: [d04, technology, schema]
keywords: [CATL Naxtra, ProLogium, 고체전해질, 세라믹 분리막, 실리콘 음극, LFP, 저온화학, ESS, 대체화학, 비리튬 공급망, CATL, Naxtra, 저온배터리, 비리튬, 상용화]
related: []
priority: normal
domain: D04
section: D04-007
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: External Benchmark Master > 007 — CATL Naxtra
tokens: 557
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · External Benchmark Master > 007 — CATL Naxtra

### SK온 적용 가치

```yaml
benchmark_capabilities:
  - Non-lithium supply-chain diversification
  - Cold-temperature chemistry
  - Chemistry-specific CTP
  - EV and ESS dual application
  - Large named commercial agreement

sk_on_relevance:
  - VIB ESS commercialization
  - LFP low-temperature improvement
  - Alternative chemistry portfolio
  - Data-center and grid ESS segmentation
```

**판정:** `대체화학 상용화 벤치마크`

---

## BENCH-D04-008 — ProLogium

```yaml
benchmark_id: BENCH-D04-008
company: ProLogium

core_platform:
  - Superfluidized all-inorganic solid-state electrolyte
  - Fully ceramic separator
  - All-silicon anode
  - Active Safety Mechanism

technology_maturity:
  taiwan_factory: GWh_CLASS_FACTORY_OPERATING
  sample_shipments: COMPANY_REPORTED
  france_factory:
    construction_target: 2026
    ramp_up_target: 2028_Q4_TO_2029_Q1
    delivery_target: 2029_Q2

manufacturer_claims:
  electrolyte_conductivity:
    value: 57
    unit: mS_per_cm
    external_test_reported_by_company: SGS
  external_stack_pressure: NOT_REQUIRED_COMPANY_CLAIM
```

ProLogium은 초유동화 무기계 고체전해질, 완전 세라믹 분리막과 100% 실리콘 음극을 결합한 플랫폼을 공개했다. 회사는 57mS/cm의 상온 이온전도도와 외부 고압 없이 계면접촉을 유지할 수 있다고 주장하지만, D04에서는 독립적인 전체 셀 검증이 아닌 `MANUFACTURER_CLAIM`으로 저장한다. ([Prologium][12])

ProLogium은 대만 GWh급 시설을 운영하고 있으며 프랑스 Dunkirk 공장의 2028년 말~2029년 초 램프업을 계획하고 있다. 회사 발표의 출하량은 소형·샘플 셀을 포함할 수 있으므로 자동차용 대량 양산실적으로 직접 간주하지 않는다. ([Prologium][13])
