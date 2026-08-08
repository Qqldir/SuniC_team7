---
id: skon-d07-d07-18-footprint-pain-point-register
title: Footprint Pain-Point Register
summary: "SK온의 생산거점별 캐파시티 관리에서 발생하는 10가지 핵심 문제점을 우선순위별로 정리한 레지스터로, 각 이슈의 영향도를 명시한다."
tags: [d07, footprint, schema]
keywords: [설비 관리, 용량 할당, 고객 연계, 지역 집중 위험, 설비 확장, 능력 편차, 테네시, JV 구조, ESS 전환, 우선순위, 생산거점, 캐파 계획, 공급 능력, 리스크 요소, 고객 연결, JV 거점, EV ESS 전환, 생산 준비, 플랜트 운영]
related: []
priority: normal
domain: D07
section: D07-18.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 621
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-18. Footprint Pain-Point Register

```yaml
footprint_pain_points:

  - pain_point_id: PP-D07-001
    title: Plant–Line–Customer Mapping Gap
    impact:
      - Capacity cannot be accurately allocated
      - Concentration risk is obscured
    priority: CRITICAL

  - pain_point_id: PP-D07-002
    title: Design Capacity versus Qualified Capacity
    impact:
      - GWh may overstate supply capability
      - Ramp progress becomes unclear
    priority: CRITICAL

  - pain_point_id: PP-D07-003
    title: JV Capacity Fungibility
    impact:
      - Gross JV capacity can be mistaken for freely allocable SK On capacity
    affected:
      - HSBMA
      - China JVs
    priority: VERY_HIGH

  - pain_point_id: PP-D07-004
    title: Customer-Linked Single-Site Exposure
    impact:
      - Customer demand change directly affects plant utilization
      - Plant disruption affects specific vehicle programs
    priority: VERY_HIGH

  - pain_point_id: PP-D07-005
    title: EV–ESS Conversion Uncertainty
    impact:
      - Underutilized capacity cannot be rapidly redeployed
      - Conversion investment is difficult to estimate
    priority: VERY_HIGH

  - pain_point_id: PP-D07-006
    title: Ramp-Up Knowledge Fragmentation
    impact:
      - Repeated launch problems
      - Slow Tennessee preparation
    priority: VERY_HIGH

  - pain_point_id: PP-D07-007
    title: Alternative-Site Qualification Gap
    impact:
      - Physical capacity exists but cannot serve disrupted customers
    priority: VERY_HIGH

  - pain_point_id: PP-D07-008
    title: Capacity Snapshot Lag
    impact:
      - Ownership and production changes occur faster than regulatory tables update
    priority: HIGH

  - pain_point_id: PP-D07-009
    title: Regional Concentration
    examples:
      - Hungary concentration in Europe
      - Yancheng concentration after China restructuring
      - Georgia concentration in current U.S. production
    impact:
      - Regional utility, labor, regulatory and logistics shocks
    priority: HIGH

  - pain_point_id: PP-D07-010
    title: Pre-SOP Capacity Overstatement
    affected:
      - Tennessee
    impact:
      - Future design capacity is confused with current supply
    priority: VERY_HIGH
```

---
