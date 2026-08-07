---
id: skon-d06-d06-rp-001-manufacturing-research-pack
title: 001. Manufacturing Research Pack
summary: SK온 배터리 제조의 4가지 핵심기술(건식전극·AI캘린더링·Z-Folding·스마트팩토리) 현황자료
tags: [d06, process, schema]
keywords: [건식전극, 캘린더링, Z-Folding, 디지털 트윈, 스마트팩토리, 배터리 셀 조립, 공정 제어, 분리막 기술, 디지털트윈, Smart Factory, 배터리셀, AI제어, 공정최적화, 설비지능화]
related: []
priority: normal
domain: D06
section: D06-RP
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2607
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-RP-001. Manufacturing Research Pack

## SRC-SKON-D06-001 — SK온 건식전극·AI 캘린더링

```yaml
source_id: SRC-SKON-D06-001
title: Battery Deep Dive Part 3 – The Dry Electrode Process
publisher: SK Innovation
publication_date: 2026-01-22
source_type: Official Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Dry powder mixing without solvent
  - Dry coating onto current collector
  - Calendering as critical scale-up process
  - AI-based real-time process control
  - Control variables include roll speed, pressure and temperature

not_confirmed:
  - Commercial mass-production application
  - Yield improvement
  - Exact line speed
  - Actual process recipe
```

SK온은 건식전극을 활물질·도전재·바인더를 용매 없이 혼합하고 집전체에 코팅·압착하는 공정으로 설명한다. 특히 캘린더링의 롤 속도·압력·온도 등을 AI로 분석해 입력조건을 조정하는 기술을 공개했지만, 양산수율이나 실제 적용공장은 공개하지 않았다. ([ASK Inno][1])

---

## SRC-SKON-D06-002 — Z-Folding

```yaml
source_id: SRC-SKON-D06-002
title: Z-Folding Technique
publisher: SK Innovation
publication_date: 2021-07-09
source_type: Official Manufacturing Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Continuous separator
  - Zigzag folding
  - Alternating cathode and anode insertion
  - Pouch-cell stacking process
  - Alignment and separation objective

not_confirmed:
  - Actual line takt time
  - Alignment tolerance
  - Equipment model
  - Current defect rate
```

Z-Folding은 분리막을 절단하지 않고 연속적으로 지그재그 적층하면서 양극과 음극을 교대로 삽입하는 SK온의 공개 셀 조립기술이다. 회사는 전극 간 접촉과 정렬불량 위험을 줄이는 목적을 제시하지만 실제 정렬공차와 양산 불량률은 공개하지 않았다. ([ASK Inno][2])

---

## SRC-SKON-D06-003 — Manufacturing Digital Twin

```yaml
source_id: SRC-SKON-D06-003
title: SK On–Siemens DISW Smart Factory Collaboration
publisher: SK On
publication_date: 2024-04-14
source_type: Official Corporate Release
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Smart-factory cooperation
  - Digital-twin application
  - Virtual battery-factory and process simulation
  - Global production-facility application objective

not_confirmed:
  - Full global rollout
  - Quantified ramp-up reduction
  - Quantified yield improvement
```

SK온은 Siemens Digital Industries Software와 배터리 공장의 디지털 트윈 및 스마트팩토리 시스템 구축을 위한 협력을 발표했다. 이는 공장·공정의 가상 검증과 최적화를 목표로 한 협력 근거이며, 전 공장 배포나 정량 성과까지 확인되는 자료는 아니다. ([SK On][3])

---

## SRC-SKON-D06-004 — Intelligent Production Equipment

```yaml
source_id: SRC-SKON-D06-004
title: Battery Production Equipment Intelligence Cooperation
publisher: SK On
publication_date: 2023-12
source_type: Official Corporate Communication
source_grade: A
evidence_level: DIRECT_CORPORATE_COMMUNICATION

partners:
  - Beckhoff Automation
  - Cisco
  - IFM Electronic
  - Yaskawa Electric Korea
  - Woowon Technology

target_components:
  - Equipment controller
  - Smart sensor
  - Industrial communication network
  - Power device
  - Robotics and automation

corporate_objectives:
  - Reduce equipment modification
  - Reduce cost
  - Improve yield

claim_status: CORPORATE_EXPECTATION
```

공식 기업 채널은 SK온이 제어기·스마트센서·통신망·전력장치·로봇 및 배터리 설비기업과 생산장비 지능화 협력을 체결했다고 설명한다. 원가절감과 수율향상은 협력 목표이며 달성실적으로 저장하지 않는다. ([LinkedIn][4])

---

## SRC-SKON-D06-005 — Pouch-Integrated Prismatic Manufacturing

```yaml
source_id: SRC-SKON-D06-005
title: Pouch-Integrated Prismatic Cell
publisher: SK Innovation
publication_date: 2026-04-17
source_type: Official Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed_manufacturing_implications:
  - Existing pouch-cell line can be utilized
  - Multiple pouch cells are stacked in an aluminum case
  - Thermal adhesive bonds cells to bottom cooling plate
  - Compression pads are placed between cells
  - External busbar connection
  - Prototype phase

not_confirmed:
  - Mass-production yield
  - Assembly takt time
  - Additional CAPEX
  - Customer qualification
```

SK온은 파우치 통합 각형 구조를 기존 파우치 셀 생산라인을 활용할 수 있는 설계로 설명한다. 파우치 셀 적층, 알루미늄 케이스, 열접착제, 냉각판, 압축패드와 외부 버스바가 포함되며 현재는 최종 성능검증을 위한 시제품 단계다. ([ASK Inno][5])

---

## SRC-BASE-D06-006 — Argonne BatPaC Manufacturing Baseline

```yaml
source_id: SRC-BASE-D06-006
title: Modeling the Performance and Cost of Lithium-Ion Batteries
publisher: Argonne National Laboratory
publication_year: 2019
source_type: Government Laboratory Manufacturing Model
source_grade: A_PLUS
evidence_level: INDUSTRY_BASELINE
temporal_status: HISTORICAL_REFERENCE_MODEL

covered_processes:
  - Receiving
  - Materials preparation
  - Electrode coating
  - Calendering
  - Electrode slitting
  - Vacuum drying
  - Dry-room cell assembly
  - Electrolyte filling
  - Formation and charge-retention testing
  - Module and pack assembly
  - Scrap recycling
```

Argonne의 BatPaC는 원재료 입고부터 전극 제조, 건조, 셀 조립, 포메이션, 모듈·팩 조립까지 공정별 비용을 계산하는 공개 하향식 제조모델이다. 다만 수치와 설비가 2019년 기준 가상 기준공장을 전제로 하므로 SK온의 현재 공정값으로 사용할 수 없다. ([ANL Publications][6])

---

## SRC-BASE-D06-007 — Electrode Processing Review

```yaml
source_id: SRC-BASE-D06-007
title: From Materials to Cell
publisher: Oak Ridge National Laboratory
publication_year: 2021
source_type: Peer-Reviewed Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_scope:
  - Powder and slurry processing
  - Coating
  - Drying
  - Calendering
  - Electrode cutting
  - Cell assembly
  - Next-generation processes
```

ORNL의 리뷰는 전극 제조가 에너지밀도·원가·생산속도에 영향을 주며, 분말부터 셀 형성까지의 공정연결을 함께 분석해야 한다고 설명한다. ([OSTI][7])

---

## SRC-BASE-D06-008 — Wet Electrode Manufacturing Review

```yaml
source_id: SRC-BASE-D06-008
title: Electrode Manufacturing for Lithium-Ion Batteries
publisher: Oak Ridge National Laboratory
publication_year: 2019
source_type: Peer-Reviewed Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_pain_points:
  - Solvent recovery
  - Cut-off waste
  - Coating inconsistency
  - Drying-induced microstructural defect
  - Slurry-property control
```

습식전극 공정에서는 슬러리 특성, 코팅 불균일, 건조 중 미세구조 변화, 절단 스크랩과 용매 회수가 주요 제조문제로 지적된다. ([OSTI][8])

---

## SRC-BASE-D06-009 — Manufacturing Energy Baseline

```yaml
source_id: SRC-BASE-D06-009
title: Lithium-Ion Battery Manufacturing Life-Cycle Update
publisher: Argonne National Laboratory
source_type: Government Laboratory Study
source_grade: A_PLUS
evidence_level: INDUSTRY_BASELINE

energy_intensive_processes:
  - Cathode drying
  - NMP recovery
  - Cell wetting
  - Formation
```

Argonne의 제조 생애주기 분석은 양극 건조·NMP 회수와 셀 함침·포메이션을 주요 에너지소비 공정으로 식별한다. 이는 일반 산업 기준이며 SK온 공장별 에너지 비중을 뜻하지 않는다. ([Greet][9])

---

## SRC-BASE-D06-010 — Quality-Control Baseline

```yaml
source_id: SRC-BASE-D06-010
title: EERE Battery Manufacturing Quality-Control Workshop
publisher: U.S. Department of Energy and NREL
source_type: Government Workshop Report
source_grade: A_PLUS
evidence_level: INDUSTRY_BASELINE

covered_scope:
  - Electrode defect detection
  - Roll-to-roll inspection
  - Defect-performance correlation
  - Process feedback
```

공개 품질관리 연구는 결함을 단순 검출하는 것만으로는 부족하며, 결함이 셀 성능·안전에 미치는 영향을 공정조건과 연결하는 데이터가 필요하다고 지적한다. ([NREL][10])

---
