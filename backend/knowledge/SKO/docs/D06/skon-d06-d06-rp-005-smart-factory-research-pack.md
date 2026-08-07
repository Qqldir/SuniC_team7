---
id: skon-d06-d06-rp-005-smart-factory-research-pack
title: 005. Smart Factory Research Pack
summary: "배터리 제조 스마트팩토리의 기술 표준, 디지털 트윈 협력 사례, OT 보안 및 네트워크 무결성 관리 방안을 정리한 연구 자료집"
tags: [d06, process, schema]
keywords: [스마트팩토리, 디지털 트윈, 배터리 제조, Siemens, ISA-95, ISO 22400, OT 보안, NIST, virtual commissioning, KPI, Siemens Xcelerator, NIST OT보안, 제조공정 시뮬레이션, OT 네트워크, 무결성 보호, 가상 커미셔닝]
related: []
priority: normal
domain: D06
section: D06-RP
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1209
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-RP-005. Smart Factory Research Pack

## SRC-SKON-D06-031 — SK온·Siemens 스마트팩토리 협력

```yaml
source_id: SRC-SKON-D06-031
title: SK On–Siemens DISW Smart Factory Cooperation
publisher: SK On
publication_date: 2024-04-14
source_type: Official Corporate Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Smart-factory cooperation
  - Siemens Xcelerator planned for use
  - Digital-twin and simulation technology
  - Virtual battery production and process verification objective

not_confirmed:
  - Complete implementation
  - Autonomous process control
  - Quantified operating performance
```

---

## SRC-SIEMENS-D06-032 — Battery Manufacturing Digital Twin

Siemens는 배터리 제조용 디지털 트윈 활용범위로 공정 시뮬레이션, 가상 Ramp-up, 설비·공정의 Virtual Commissioning과 생산목표 사전검증을 제시한다. 이는 Siemens 솔루션의 일반적 기능 설명이며 SK온이 모든 기능을 도입했다는 증거는 아니다. ([Siemens][2])

```yaml
source_id: SRC-SIEMENS-D06-032
publisher: Siemens
source_type: Official Vendor Technology Description
source_grade: A
evidence_level: DIRECT_OFFICIAL
claim_status: VENDOR_CAPABILITY_CLAIM

capabilities:
  - Factory and process simulation
  - Virtual commissioning
  - Virtual ramp-up
  - Production-flow optimization
  - Physical-performance feedback
  - Product and production lifecycle linkage
```

---

## SRC-STD-D06-033 — ISA-95 Manufacturing Architecture

ISA-95는 기업 업무기능과 제조 제어기능 사이의 공통 모델·용어·정보교환을 정의한다. 2025년에는 Part 1의 갱신판인 `ANSI/ISA-95.00.01-2025`가 발표됐다. ([isa.org][3])

```yaml
source_id: SRC-STD-D06-033
standard: ISA-95 / IEC 62264
source_grade: A_PLUS
evidence_level: DIRECT_OFFICIAL

relevant_scope:
  - Enterprise and manufacturing-control integration
  - Common equipment hierarchy
  - Manufacturing operations management
  - Information exchange between layers
```

---

## SRC-STD-D06-034 — ISO 22400 Manufacturing KPI

ISO 22400은 제조운영관리에서 KPI를 정의·구성·교환·사용하기 위한 산업중립적 프레임워크를 제공하며, Part 1의 2014판은 2025년 재검토 후 현행으로 확인됐다. ([ISO][4])

```yaml
source_id: SRC-STD-D06-034
standard: ISO 22400
source_grade: A_PLUS
evidence_level: DIRECT_OFFICIAL

relevant_scope:
  - Manufacturing KPI terminology
  - KPI definition and composition
  - Data acquisition
  - Energy-management KPI
```

---

## SRC-NIST-D06-035 — OT Security

NIST SP 800-82 Rev.3은 PLC·SCADA·DCS 등 OT 시스템의 보안관리에서 생산성뿐 아니라 안전·신뢰성·가용성을 함께 고려하도록 안내한다. NIST는 2026년 1월 차기 개정을 위한 의견수렴도 시작했지만, 현재 공개된 최종판은 Rev.3이다. ([NIST CSRC][5])

```yaml
source_id: SRC-NIST-D06-035
title: NIST SP 800-82 Rev.3
source_grade: A_PLUS
evidence_level: DIRECT_OFFICIAL

relevant_scope:
  - OT asset inventory
  - Network architecture
  - Access control
  - Monitoring
  - Incident response
  - Safety and availability requirements
```

---

## SRC-NIST-D06-036 — Manufacturing Network Integrity

NIST는 제조 IT·OT 연결이 생산성과 데이터 활용을 높일 수 있지만, 동시에 제어시스템과 생산데이터의 무결성 공격면을 확대한다고 설명한다. 네트워크 분리, 변경관리, 이상탐지와 파일 무결성 보호가 주요 대응수단으로 제시된다. ([NIST CSRC][6])

---

## SRC-ANL-D06-037 — Battery Assembly Energy Baseline

Argonne은 2025년 R&D GREET의 리튬이온 배터리 조립 에너지 모델을 최근 문헌과 BatPaC 5.2에 맞춰 갱신했다. 이는 여러 화학계의 일반적인 제조 에너지 모델이며 SK온 공장의 에너지 사용량을 의미하지 않는다. ([Greet][7])

---
