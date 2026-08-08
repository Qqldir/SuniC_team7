---
id: skon-d06-d06-dq-006-entity-evidence-correction-ledger
title: 006. Entity·Evidence Correction Ledger
summary: "SK온 제조공정 데이터의 데이터 품질 보정 기록, 운영 제어탑의 근거 수준, KPI 표준 버전 관리 방법을 정의하는 문서."
tags: [d06, process, schema, "xref:d04"]
keywords: [데이터 품질, 정정 레지스트, 기술ID 매핑, Control Tower, 제조운영, OEE 표준, KPI 버전 관리, ISO 22400, 디지털 트윈, 스마트팩토리, 데이터 품질 정정, 제어탑 (Control Tower), OEE·수율 KPI, 메타데이터 관리, 제조공정 표준화, 증거 수준, 기술 ID 정정, KPI 버전 제어]
related: [TECH-SKON-D04-042]
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 930
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 6. End-to-End Operations Control Tower·Yield Waterfall·Ramp-Up·Cross-Plant Transfer

**문서 버전:** D06 v1.5
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-50 Smart Factory Gap Register`

> 이번 구간은 공개된 SK온 공장 성과를 설명하는 것이 아니라, D06에서 정리한 공정·결함·설비·품질·에너지 데이터를 실제 의사결정에 연결하기 위한 **분석·운영 목표모델**이다. SK온 공장별 수율·OEE·WIP·Ramp-Up 실적은 공개자료에서 확인되지 않아 입력하지 않는다.

---

# D06-DQ-006. Entity·Evidence Correction Ledger

## DQ-D06-006-001 — 존재하지 않는 기술 ID 정정

이전 `PROC-SKON-D06-015 Cell Formation`에 연결된 `TECH-SKON-D04-042`는 D04 Canonical Registry에 존재하지 않는다.

```yaml
correction_id: DQ-D06-006-001

invalid_edge:
  process_id: PROC-SKON-D06-015
  invalid_technology_id: TECH-SKON-D04-042

corrected_edges:
  - technology_id: TECH-SKON-D04-035
    canonical_name: Cell Performance Prediction AI
    relationship: SUPPORTS_FORMATION_ANALYTICS

  - technology_id: TECH-SKON-D04-043
    canonical_name: Simulation-Based Charging Protocol Optimization
    relationship: SUPPORTS_FORMATION_PROTOCOL_DESIGN

resolution:
  - Remove TECH-SKON-D04-042
  - Preserve formation-defect-detection candidate patent links
  - Do not infer autonomous formation control
```

---

## DQ-D06-006-002 — Control Tower 적용상태

```yaml
correction_id: DQ-D06-006-002
subject: End-to-End Manufacturing Control Tower

publicly_confirmed:
  - SK On and Siemens DISW smart-factory cooperation
  - Digital-twin and simulation objective

not_publicly_confirmed:
  - Enterprise-wide control tower deployment
  - All-plant common manufacturing ontology
  - Real-time global yield dashboard
  - Automatic cross-factory recipe optimization
  - Autonomous scheduling and process control

handling:
  ownership_scope: ANALYTICAL_TARGET
  evidence_level: ANALYST_INFERENCE
```

SK온은 Siemens Digital Industries Software와 디지털 트윈·시뮬레이션 기반 스마트팩토리 협력을 공식 발표했지만, 아래에서 설계하는 전사 Control Tower가 이미 구축됐다고 볼 근거는 없다. ([SK On][1])

---

## DQ-D06-006-003 — KPI 표준 기준일

ISO 22400-1은 제조운영 KPI의 정의·구성·교환·활용을 위한 산업중립적 틀을 제공한다. ISO 22400-2:2014는 현재 공개된 국제표준이지만 개정안이 진행 중이므로, D06 KPI는 표준명과 산식 버전을 함께 저장해야 한다. ([ISO][2])

```yaml
correction_id: DQ-D06-006-003

kpi_version_control:
  required:
    - KPI canonical name
    - Formula
    - Included time categories
    - Excluded time categories
    - Product and equipment boundary
    - Standard reference
    - Internal definition version

prohibited:
  - Compare plant KPIs with different formula versions
  - Compare OEE without planned-time boundary
  - Compare yield without rework treatment
```

---
