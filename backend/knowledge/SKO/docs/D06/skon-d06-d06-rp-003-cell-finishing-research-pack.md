---
id: skon-d06-d06-rp-003-cell-finishing-research-pack
title: 003. Cell Finishing Research Pack
summary: "배터리 셀 포메이션 공정의 제조 병목 현황, 결함 검출 기술, 검사 시스템 개선 방안을 다룬 SK온 연구 자료집"
tags: [d06, process, schema]
keywords: [포메이션, Formation, 배터리셀, 결함검출, 전해액, 에이징, 병목공정, 검사트레이, EoL, 셀 마감, 제조 병목, 결함 검출, 전해액 함침, 배터리 제조공정, 검사 시스템, 초기충전, 설비점유]
related: []
priority: normal
domain: D06
section: D06-RP
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2303
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-RP-003. Cell Finishing Research Pack

## SRC-BASE-D06-016 — Formation Manufacturing Challenge

```yaml
source_id: SRC-BASE-D06-016
title: Formation Challenges of Lithium-Ion Battery Manufacturing
publication_year: 2019
source_type: Peer-Reviewed Perspective
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

confirmed:
  - Formation is essential for interphase creation and cell stabilization
  - Electrolyte wetting, formation and aging are major manufacturing bottlenecks
  - Formation protocol affects cell quality and long-term performance
  - Reducing formation and aging time is an important manufacturing objective
```

포메이션은 단순 출하 전 충전이 아니라 최초 충전 과정에서 전극–전해액 계면을 형성하고 셀을 안정화하는 제조단계다. 관련 연구는 전해액 함침·포메이션·에이징이 긴 처리시간과 설비점유 때문에 셀 생산의 주요 병목이라고 설명한다. ([OSTI][1])

---

## SRC-BASE-D06-017 — End-to-End Manufacturing Review

```yaml
source_id: SRC-BASE-D06-017
title: From Materials to Cell
publication_year: 2021
source_type: Peer-Reviewed Manufacturing Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

confirmed:
  - Formation and aging follow electrolyte filling and cell assembly
  - These processes may require days or longer depending on protocol
  - They occupy substantial manufacturing space and inventory
  - Formation data can support quality evaluation
```

공개 제조 리뷰는 포메이션과 에이징을 셀 제조의 시간적 병목으로 분류하며, 처리시간이 수일 이상 이어질 수 있다고 설명한다. 이는 일반 산업 기준이며 SK온의 실제 공정시간을 뜻하지 않는다. ([OSTI][2])

---

## SRC-SKON-D06-018 — Formation Defect Detection

```yaml
source_id: SRC-SKON-D06-018
title: Method and System for Detecting Defect of Battery in Formation Process
publication_number: US20250290992A1
publication_date: 2025-09-18
applicant_snapshot:
  - SK On

source_type: Patent Application Publication
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Battery manufacturing is divided into electrode, assembly, formation and EoL stages
  - Cell pressure and voltage behavior may be used for formation-stage defect detection
  - The application seeks earlier detection of defective cells during formation

legal_status:
  source: AGGREGATOR_SNAPSHOT
  status: PENDING_APPLICATION
```

SK온 출원문서는 전극 제조, 셀 조립, 포메이션과 EoL을 순차 공정으로 구분하고, 포메이션 중 셀에 압력을 가하며 측정한 전압 상승·하강 패턴을 결함판정에 활용하는 방식을 제시한다. 공개출원 단계의 기술이므로 실제 양산 적용 여부는 확인되지 않았다. ([구글 특허][3])

---

## SRC-SKON-D06-019 — Activation·Inspection Tray System

```yaml
source_id: SRC-SKON-D06-019
title: Battery Cell Inspection System
publication_number: EP4509851A1
applicant_snapshot:
  - SK On

source_type: Patent Application Publication
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Pre-charging and cell-defect inspection can be integrated
  - Multiple cells may be contacted through an inspection tray
  - Multi-level transport architecture seeks higher spatial density
  - Formation takt-time reduction is an identified technical objective

legal_status:
  source: AGGREGATOR_SNAPSHOT
  status: PENDING_APPLICATION
```

이 출원은 단층 트레이를 순차 이송하는 기존 구조가 낮은 공간밀도와 긴 검사시간으로 포메이션 생산성을 떨어뜨릴 수 있다고 설명하고, 복수 셀의 프리차징과 결함검사를 보다 고밀도로 수행하는 시스템을 제안한다. ([구글 특허][4])

---

## SRC-SKON-D06-020 — Pouch Insulation·Thermal Inspection

```yaml
source_id: SRC-SKON-D06-020
title: Device for Inspecting Battery Cell Pouch
publication_number: US20250349916A1
applicant_snapshot:
  - SK On

source_type: Patent Application Publication
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Pouch insulation resistance is measured using a probe
  - Thermographic imaging can be used for secondary defect analysis
  - Electrical and thermal signals are combined to reduce false defect decisions
  - Local heating position may support defect localization

legal_status:
  source: AGGREGATOR_SNAPSHOT
  status: PENDING_APPLICATION
```

이 출원은 파우치 절연저항으로 1차 판정한 뒤 열화상 온도분포로 실제 발열 여부와 위치를 확인하는 2단계 검사구조를 제시한다. 특허문서상 기술이며, SK온 전 공장의 표준 EoL 검사라고 판단할 근거는 없다. ([구글 특허][5])

---

## SRC-SKON-D06-021 — Seal Leak Inspection

```yaml
source_id: SRC-SKON-D06-021
title: Seal Inspection Device and Method for Battery Cell
publication_number: US20260126338A1
publication_date: 2026-05-07
applicant_snapshot:
  - SK On

source_type: Patent Application Publication
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Cell is placed in a chamber
  - Chamber decompression may be used
  - Gas may be injected into the chamber or cell
  - Pressure or gas detection may determine leakage
  - Helium is listed as one possible inert tracer gas

legal_status:
  source: AGGREGATOR_SNAPSHOT
  status: PENDING_APPLICATION
```

SK온의 2026년 공개출원은 감압 챔버와 가스 주입, 압력센서 또는 가스검출기를 이용해 셀 실링상태를 판정하는 방식을 다룬다. 헬륨은 가능한 추적가스 중 하나로 제시되며, 실제 양산검사 가스로 사용된다는 뜻은 아니다. ([구글 특허][6])

---

## SRC-SKON-D06-022 — Integrated Cell Inspection·Sorting

```yaml
source_id: SRC-SKON-D06-022
title: Battery Cell Inspection Apparatus, Method and System
publication_number: WO2024063482A1
applicant_snapshot:
  - SK On

source_type: Patent Application Publication
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed_inspections:
  - Charging-resistance inspection
  - Short-circuit inspection
  - Appearance inspection
  - X-ray inspection

confirmed_system_elements:
  - Cell supply
  - Reciprocating inspection stage
  - Inspection unit
  - Good and defective cell sorting
```

이 출원은 충전저항·쇼트·외관·X-ray 검사와 검사결과에 따른 양품·불량품 분류를 하나의 자동화 시스템으로 연결한다. 검사 중 다음 셀을 공급하는 교번 스테이지 구조를 통해 검사시간을 줄이는 방향도 제시한다. ([구글 특허][7])

---

## SRC-BASE-D06-023 — Early Cell Quality Prediction

```yaml
source_id: SRC-BASE-D06-023
title: Early Quality Classification and Prediction of Battery Cycle Life in Production Using Machine Learning
publication_year: 2022
source_type: Peer-Reviewed Research
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

confirmed:
  - Early production data can support cell-quality classification
  - Machine learning may reduce dependence on long testing
  - Prediction must be validated across lots, chemistries and equipment conditions
```

학술연구에서는 초기 충방전 데이터로 셀 품질과 이후 수명을 조기에 예측하는 방법을 검토하고 있다. 다만 특정 데이터셋의 정확도를 다른 제품·공장에 바로 적용할 수는 없으며, Lot·설비·화학계 변화에 대한 재검증이 필요하다. ([ScienceDirect][8])

---
