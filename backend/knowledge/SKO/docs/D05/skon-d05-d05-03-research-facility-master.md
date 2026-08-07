---
id: skon-d05-d05-03-research-facility-master
title: Research Facility Master
summary: "SK온의 배터리 R&D 시설, 파일럿 플랜트, 품질 인프라의 위치, 운영 상태, 기술 범위, 협력사 정보를 기록한 시설 목록."
tags: [d05, rnd, schema]
keywords: [전고체 배터리, 파일럿 플랜트, 배터리 R&D, 리튬이온, ESS, Solid Power, 교정시설, KOLAS, 품질관리, 고체전해질, 배터리 개발 센터, 대전 미래기술원, 전고체 파일럿 플랜트, KOLAS 교정, 셀 제조, 품질관리 인프라, 고체 전해질, 배터리 관리 시스템]
related: []
priority: normal
domain: D05
section: D05-03.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 964
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-03. Research Facility Master

## FAC-SKON-D05-001 — Daejeon Future Technology Institute

```yaml
facility_id: FAC-SKON-D05-001
canonical_name: SK On Institute of Future Technology
korean_name: SK온 미래기술원

location:
  city: Daejeon
  country: South Korea

facility_type:
  - Corporate Battery R&D Center
  - Pilot Development Site

confirmed_research_scope:
  - Lithium-ion battery
  - Automotive cell and system
  - ESS
  - Solid-state battery
  - Battery materials
  - BMS and safety

operational_status: ACTIVE

source_ids:
  - SRC-SKON-D05-001
  - SRC-SKON-D05-003
  - SRC-SKON-D05-004
```

---

## FAC-SKON-D05-002 — All-Solid-State Battery Pilot Plant

```yaml
facility_id: FAC-SKON-D05-002
canonical_name: All-Solid-State Battery Pilot Plant
korean_name: 전고체 배터리 파일럿 플랜트

parent_facility:
  - FAC-SKON-D05-001

location:
  city: Daejeon

area:
  value: 4628
  unit: square_meters

completion:
  period: 2025_H2
  ceremony_date: 2025-09-15

facility_status: PILOT_OPERATION_AND_VALIDATION

technology_tracks:
  - Polymer-oxide composite battery
  - Sulfide all-solid-state battery
  - Solid electrolyte
  - Lithium-metal interface
  - Pilot cell manufacturing

partner_technology:
  - Solid Power

not_confirmed:
  - Annual cell capacity
  - Cell format and dimensions
  - Pilot yield
  - Line speed
  - Sample customers
  - Commercial production volume

source_ids:
  - SRC-SKON-D05-003
  - SRC-SKON-D05-004
  - SRC-SKON-D05-005
```

파일럿 플랜트는 소재연구와 셀 제조공정 사이의 스케일업 검증시설이다. 완공 사실과 Solid Power 기술라인의 현장인수시험은 확인되지만, 생산능력·수율·고객 샘플 단계는 공개되지 않았다. ([ASK Inno][3])

---

## FAC-SKON-D05-003 — Daejeon Calibration & Quality Infrastructure

```yaml
facility_id: FAC-SKON-D05-003
canonical_name: SK On Daejeon Calibration and Quality Infrastructure
korean_name: SK온 대전 교정·품질 인프라

organization:
  - ORG-SKON-QUALITY-001

facility_type:
  - Calibration Laboratory
  - Quality Assurance Infrastructure

certification:
  - KOLAS International Calibration Laboratory

status: ACTIVE_AT_2024_DISCLOSURE

research_role:
  - Test-equipment calibration
  - Measurement traceability
  - Quality reliability support

source_ids:
  - SRC-SKON-D05-006
```

---

## FAC-SKON-D05-004 — Global Quality-Control Center Plan

```yaml
facility_id: FAC-SKON-D05-004
canonical_name: Global Quality-Control Center
korean_name: 글로벌 품질관리센터

facility_status: HISTORICAL_PLAN_NOT_FULLY_RECONCILED

original_plan:
  target_year: 2025
  source_year: 2022

confirmed_follow_up:
  - Daejeon quality-management organization exists
  - KOLAS calibration capability confirmed

not_confirmed:
  - Completion under exact official name
  - Final building scope
  - Full operational functions
  - Investment completion amount

source_ids:
  - SRC-SKON-D05-002
  - SRC-SKON-D05-006

confidence: MEDIUM
```

과거 ESG 보고서의 `글로벌 품질관리센터` 계획과 2024년 확인된 대전 품질경영 부문의 관계는 높아 보이지만, 동일 시설인지 공식적으로 확인되지 않는다. 따라서 두 기록을 자동 병합하지 않는다. ([ASK Inno][5])

---
