---
id: skon-d03-d03-05-application-mapping-006-renewable-energy-8
title: Application Mapping — 006 — Renewable Energy Integration
summary: "SK온의 GRIDON 배터리 제품이 태양광·풍력 재생에너지 프로젝트에서 출력평탄화, 시간이동, 첨두제어 등의 기능으로 어떻게 활용되는지 매핑한 문서."
tags: [d03, product, schema]
keywords: [재생에너지, GRIDON, 에너지저장, 태양광, 풍력, 계통 안정화, 배터리 저장, ESS, 피크 시프팅, 분산전원, 배터리, 계통안정화, 변동억제, IPP, LFP]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 315
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-006 — Renewable Energy Integration

```yaml
application_id: APP-SKON-006
application_name: Renewable Energy Integration
application_type: STATIONARY_ENERGY_STORAGE
maturity: COMMERCIAL_TARGET

energy_sources:
  - Solar
  - Wind
  - Hybrid Renewable Generation

system_functions:
  - Output smoothing
  - Time shifting
  - Curtailment reduction
  - Peak shifting
  - Frequency response
  - Capacity support

mapped_products:
  - GRIDON Gen 1
  - GRIDON Gen 2
  - LFP ESS Battery
  - DC Block
  - AC Block-Compatible Configuration

customer_types:
  - Renewable Energy Developer
  - IPP
  - Utility
  - Project Investor
```

**ANALYSIS**

Flatiron이 재생에너지·대규모 저장 프로젝트 개발·운영사라는 점과 GRIDON의 계통 안정화 목적을 고려하면, 재생에너지 연계는 핵심 적용영역으로 분류할 수 있다. 다만 개별 태양광·풍력 프로젝트와 SK온 제품의 직접 연결은 프로젝트별 계약자료로 별도 확인해야 한다. ([ASK Inno][2])

---
