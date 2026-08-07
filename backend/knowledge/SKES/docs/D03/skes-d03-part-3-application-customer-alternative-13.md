---
id: skes-d03-part-3-application-customer-alternative-13
title: Part 3. Application·Customer·Alternative·Graph·Chunk 확장 — Revised D04 Handover
summary: "D03 제품·솔루션을 D04로 이관하기 위해 필요한 기술 매핑, 보유 기술 정의, 필수 데이터 필드를 규정한 이관 명세서."
tags: [d03, product, schema, "xref:d04"]
keywords: [기술 매핑, 데이터 이관, 제품솔루션 연계, owned_capability, crosswalk, KPI, 필드 정의, DERMS]
related: []
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 3. Application·Customer·Alternative·Graph·Chunk 확장
tokens: 245
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 3. Application·Customer·Alternative·Graph·Chunk 확장

## 32. Revised D04 Handover

```yaml
handover_id: HANDOVER-ENS-D03-D04-002
source_domain_version: D03_v2.0
required_crosswalk:
  - 29 base product_solution records to 61+ technologies
  - 25 applications to data and decision technologies
  - 52 OI seeds to owned capability and external solution needs
owned_capability_priority:
  - KCE MarketCapture
  - EverCharge SmartPower mesh EVSE turnkey service
  - city gas RBMS and drone inspection
  - E&S direct PPA operating process
  - LNG integrated value chain operating data
planned_capability_boundary:
  - DERMS and renewable O&M are planned
  - VPP is considering
  - blue hydrogen and CCS are planned/considering
required_D04_fields:
  - technology_id
  - linked_PS_APP_SEED
  - disclosed_internal_status
  - data_input_output
  - KPI_and_failure_mode
  - owned_build_buy_partner classification
  - safety_regulatory_cyber gate
```
