---
id: skon-d07-d07-dq-005-canonical-correction-ledger
title: 005. Canonical Correction Ledger
summary: "SK온 미국 배터리 생산 통계의 공장 ID 통합, 중복 제거, 용량 계산 정정 등 5가지 데이터 품질 개선사항과 적용 규칙을 기록한 정정원장"
tags: [d07, footprint, schema]
keywords: [배터리, 생산거점, 생산능력, HSBMA, 정정 레지, 공장ID, ESS, GWh, 데이터 품질 정정, 배터리 용량, 공장 ID 통합, Kentucky, Commerce, 정규화]
related: []
priority: normal
domain: D07
section: D07-DQ
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1356
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# SK온 D07 Manufacturing Footprint, Plants & Capacity

## Part 4. Chunk Library·Graph Query·Relationship Graph·Final Audit

**문서 버전:** D07 v1.3
**기준일:** 2026-08-02
**이전 완료 지점:** `D07-31 Integrated OI Priority`

---

# D07-DQ-005. Canonical Correction Ledger

## DQ-D07-005-001 — Commerce 공장 ID 정정

`PLANT-D07-US-GA1_GA2`는 두 공장을 합친 비정규 ID이므로 폐기한다.

```yaml
correction_id: DQ-D07-005-001

deprecated_id:
  - PLANT-D07-US-GA1_GA2

replacement:
  site_cluster_id: SITE-D07-US-COMMERCE

  contains:
    - PLANT-D07-US-GA1
    - PLANT-D07-US-GA2

mapping_rule:
  - F-150 Lightning and ID.4 evidence is assigned to the Commerce site cluster
  - Do not assign either vehicle program to Georgia 1 or Georgia 2 individually
```

Georgia 주정부 자료는 Commerce의 두 공장을 합쳐 약 22GWh 생산거점으로 설명하고, F-150 Lightning과 Volkswagen ID.4 탑재 배터리의 생산이력을 확인한다. 어느 건물 또는 Line이 각 차종을 담당했는지는 공개하지 않았다. ([켐프 주지사 사무실][1])

---

## DQ-D07-005-002 — HSBMA Source 중복 제거

```yaml
correction_id: DQ-D07-005-002

deprecated_alias:
  - SRC-OFF-D07-009

merged_into:
  - SRC-OFF-D07-005

canonical_source:
  title: HSBMA Begins EV Battery Cell Production in Georgia
  publication_date: 2026-07-17
  event_effective_date: 2026-06-01
```

HSBMA는 2026년 6월 1일 상업생산을 시작했으며, 연간 35GWh 설계능력과 현대차그룹·SK온의 50:50 지분구조가 공식 확인된다. 초기 생산 Cell은 IONIQ 9을 지원한다. ([HSAGP ENERGY LLC][2])

---

## DQ-D07-005-003 — 미국 ESS Source 정의

```yaml
source_id: SRC-OFF-D07-020
title: SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026
publisher: SK
publication_date: 2026-06-04
source_type: Official Corporate Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

permitted_use:
  - U.S. ESS expansion strategy
  - GRIDON U.S. production target
  - U.S. manufacturing network context

blocked_use:
  - Assign GRIDON production to a specific factory
  - Claim that an EV line has completed ESS conversion
  - Count Tennessee as current 2026 production capacity
```

---

## DQ-D07-005-004 — 94.3GWh의 지위

```yaml
correction_id: DQ-D07-005-004

value_gwh: 94.3

derivation:
  q1_2026_official_capacity_gwh: 97.4
  kentucky_1_transferred_capacity_gwh: -3.1

status:
  value_type: ANALYST_DERIVED_PRO_FORMA
  official_company_restatement: false
  use_as_current_official_capacity: prohibited
```

SK이노베이션 공시는 2026년 3월 말 최대 생산능력을 97.4GWh로 기재하고, 2026년 1분기 평균 가동률을 36.5%로 공시했다. 5월 20일 Ford 측이 Kentucky 두 공장을 인수했으므로 94.3GWh는 Kentucky 1의 3.1GWh만 기계적으로 차감한 분석치일 뿐이다. ([KIND][3])

---

## DQ-D07-005-005 — Capacity 오합산 방지

```yaml
capacity_non_additivity:

  hsbma_35_gwh:
    capacity_type: JV_GROSS_DESIGN_CAPACITY
    add_to_sk_on_consolidated_capacity: false

  tennessee_45_gwh:
    capacity_type: LEGACY_DESIGN_REFERENCE
    current_operating_capacity: false
    projected_mass_production_start: 2028

  nissan_nearly_100_gwh:
    capacity_type: MULTI_YEAR_SUPPLY_COMMITMENT
    period: 2028_to_2033
    annual_capacity: not_equivalent

  slate_approximately_20_gwh:
    capacity_type: MULTI_YEAR_SUPPLY_COMMITMENT
    period: 2026_to_2031
    annual_capacity: not_equivalent
```

Tennessee는 독립 SK온 법인으로 전환됐지만 대량생산은 2028년 시작할 것으로 안내됐다. Nissan 약 100GWh와 Slate 약 20GWh도 여러 해에 걸친 계약 총량이며, 특정 공장의 연간 Capacity가 아니다. ([SK][4])

---

## DQ-D07-005-006 — 중국 지분교환 상태

```yaml
correction_id: DQ-D07-005-006
reference_date: 2026-08-02

transaction:
  disposal:
    entity: Huizhou EVE United Energy
    sk_on_stake: 49_percent

  acquisition:
    entity: SK On Jiangsu
    counterparty_stake: 30_percent

status:
  - TRANSACTION_PENDING
  - OWNERSHIP_CHANGE_NOT_YET_APPLIED_TO_PLANT_MASTER

control:
  - Preserve pre-closing ownership structure
  - Apply new ownership only after closing evidence
```

공시상 SK온은 Huizhou EVE United Energy 지분 49%를 처분하고 EVE 측이 보유한 SK On Jiangsu 지분을 취득하는 Portfolio 재편을 추진하고 있다. 2026년 8월 2일 기준 완료 상태로 선반영하지 않는다. ([KIND][5])

---
