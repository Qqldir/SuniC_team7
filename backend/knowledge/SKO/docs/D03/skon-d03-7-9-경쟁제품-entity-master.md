---
id: skon-d03-7-9-경쟁제품-entity-master
title: 경쟁제품 Entity Master
summary: "CATL, BYD, LG, Samsung SDI, Panasonic, Tesla 등의 배터리 제품 정보를 담은 마스터 테이블로, 화학 구성·형태·개발 단계와 SK온 벤치마킹 대상을 정리하고 있다."
tags: [d03, product, core-candidate, schema]
keywords: [CATL, LFP, 벤치마킹, 전기차 배터리, Blade Battery, 니켈, 에너지저장, CTP, BYD, Samsung SDI, NCA, EV, ESS, Shenxing]
related: []
priority: critical
domain: D03
section: 7.9
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 736
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 7.9 경쟁제품 Entity Master

```yaml
competitive_entity_master:

  - entity_id: COMP-CATL-EV-001
    name: Shenxing PLUS
    company: CATL
    chemistry: LFP
    status: PRODUCT_DISCLOSED
    benchmark_for:
      - SK On LFP EV
      - SF Family
      - CTP

  - entity_id: COMP-CATL-EV-002
    name: Second-Generation Shenxing
    company: CATL
    chemistry: LFP
    status: PRODUCT_DISCLOSED
    benchmark_for:
      - Hyper Fast Battery
      - Cold-Weather Charging

  - entity_id: COMP-CATL-EV-003
    name: Shenxing Pro
    company: CATL
    chemistry: LFP
    status: PRODUCT_DISCLOSED
    benchmark_for:
      - Safety
      - Lifetime
      - European EV

  - entity_id: COMP-CATL-ESS-001
    name: TENER
    company: CATL
    chemistry: LFP
    status: COMMERCIAL_PRODUCT
    benchmark_for:
      - GRIDON Gen 1
      - GRIDON Gen 2

  - entity_id: COMP-CATL-ESS-002
    name: TENER Stack
    company: CATL
    status: MASS_PRODUCTION_SOLUTION_DISCLOSED
    benchmark_for:
      - High-Capacity ESS

  - entity_id: COMP-BYD-EV-001
    name: Blade Battery
    company: BYD
    chemistry: LFP
    form_factor: LONG_PRISMATIC
    status: COMMERCIAL
    benchmark_for:
      - LFP EV
      - Cell-to-Pack
      - Safety

  - entity_id: COMP-LGES-EV-001
    name: High-Nickel NCMA Pouch
    company: LG Energy Solution
    status: COMMERCIAL
    benchmark_for:
      - NCM9+
      - Advanced SF

  - entity_id: COMP-LGES-EV-002
    name: LFP Pouch Battery
    company: LG Energy Solution
    status: CONTRACTED
    benchmark_for:
      - SK On LFP EV

  - entity_id: COMP-LGES-EV-003
    name: 46-Series Cylindrical
    company: LG Energy Solution
    status: COMMERCIALIZING
    benchmark_for:
      - SK On Cylindrical Platform

  - entity_id: COMP-SDI-EV-001
    name: PRiMX680-EV
    company: Samsung SDI
    chemistry: High-Nickel NCA
    form_factor: PRISMATIC
    status: COMMERCIAL_PRODUCT
    benchmark_for:
      - SK On Prismatic Platform

  - entity_id: COMP-SDI-ESS-001
    name: SBB 1.7
    company: Samsung SDI
    chemistry: High-Nickel NCA
    status: PRODUCTION_PLANNED

  - entity_id: COMP-SDI-ESS-002
    name: SBB 2.0
    company: Samsung SDI
    chemistry: LFP
    status: PRODUCTION_PLANNED

  - entity_id: COMP-PANA-EV-001
    name: Panasonic 2170
    company: Panasonic Energy
    form_factor: CYLINDRICAL
    status: LARGE_SCALE_COMMERCIAL

  - entity_id: COMP-TESLA-EV-001
    name: Tesla 4680 Dry-Electrode Cell
    company: Tesla
    form_factor: CYLINDRICAL
    status: VEHICLE_PRODUCTION

  - entity_id: COMP-TESLA-ESS-001
    name: Megapack
    company: Tesla
    status: LARGE_SCALE_COMMERCIAL
```

---
