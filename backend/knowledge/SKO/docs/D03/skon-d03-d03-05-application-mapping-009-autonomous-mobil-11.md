---
id: skon-d03-d03-05-application-mapping-009-autonomous-mobil-11
title: Application Mapping — 009 — Autonomous Mobile Robot
summary: 산업용 자율주행 모바일 로봇(AMR)에 탑재된 배터리의 기술 요구사항과 시장 기회 과제를 매핑한 문서.
tags: [d03, product, schema]
keywords: [자율이동로봇, AMR, NCM, 산업용 이동로봇, 고속 충전, 에너지 밀도, 배터리 모니터링, 현대위아, 자율주행 로봇, 산업용 배터리, 급속충전, 에너지밀도, 배터리 팩, 실내 안전, 상태 진단]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 472
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-009 — Autonomous Mobile Robot

```yaml
application_id: APP-SKON-009
application_name: Autonomous Mobile Robot
abbreviation: AMR
application_type: INDUSTRIAL_MOBILITY
maturity: COMMERCIAL_APPLICATION_CONFIRMED

confirmed_equipment:
  manufacturer: Hyundai WIA
  equipment_type: Autonomous Mobile Robot

confirmed_operating_environment:
  - Hyundai Motor Group Metaplant America
  - Industrial Manufacturing Site

mapped_battery:
  chemistry: NCM
  exact_product_name: NOT_DISCLOSED
  form_factor: NOT_DISCLOSED
  capacity: NOT_DISCLOSED

priority_requirements:
  - High cell-level energy density
  - Fast charging
  - High power
  - Compact size
  - Long operating time
  - High cycle frequency
  - Safe indoor operation

confidence:
  application: HIGH
  exact_cell_specification: LOW
```

현대위아 AMR에 SK온 NCM 배터리가 탑재돼 산업현장에서 사용된다는 사실은 공식 확인된다. 다만 배터리 모델명, 셀 규격, 용량 및 충전속도는 공개되지 않았으므로 기존 SF 제품군과 임의로 연결하지 않는다. ([ASK Inno][1])

### OI Metadata

```yaml
oi_metadata:
  priority: HIGH

  pain_points:
    - High-frequency opportunity charging
    - Indoor fire safety
    - Small-pack thermal management
    - Battery swapping downtime
    - Fleet-level battery imbalance
    - State-of-health variation

  external_capability_needs:
    - Wireless battery monitoring
    - Fleet charging optimization
    - Compact thermal interface material
    - Robotic battery swapping
    - Indoor off-gas sensing
    - Edge-based degradation prediction
```

---
