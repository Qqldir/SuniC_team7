---
id: skon-d04-d04-058-d04-058-formation-degassing-aging-oi-met
title: "D04-058 — Formation, Degassing & Aging — OI Metadata"
summary: 포메이션 완료 후 배터리 셀의 선별·등급분류·비파괴 검사를 통해 품질을 보증하는 기술의 요구사항과 프로세스를 정의한 문서
tags: [d04, technology, schema]
keywords: [포메이션, 셀 등급분류, 선별, 비파괴 검사, NDI, 에이징, 내부저항, 용량, 셀 매칭, 셀 선별, 등급분류, 내부 저항, 결함 검출, X선 검사, 임피던스, 품질 관리]
related: []
priority: normal
domain: D04
section: D04-058
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: "Manufacturing Technology Master > D04-058 — Formation, Degassing & Aging"
tokens: 1049
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-058 — Formation, Degassing & Aging

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: VERY_HIGH

  external_capability_needs:
    - Accelerated formation protocol
    - Formation-free or preformed interface material
    - High-efficiency bidirectional cycler
    - Formation heat recovery
    - Early defect prediction
    - Adaptive aging-duration algorithm
    - Formation digital twin

  poc_kpis:
    - Formation time
    - Energy per cell
    - First-cycle efficiency
    - Gas generation
    - Early defect detection rate
    - Aging inventory
    - Cell life retention
```

---

## TECH-SKON-D04-059 — Cell Grading & Sorting

```yaml
technology_id: TECH-SKON-D04-059
canonical_name: Cell Grading and Sorting
korean_name: 셀 등급분류·선별기술

technology_category:
  - End-of-Line Quality
  - Cell Matching
  - Data Analytics

technology_status:
  base_process: INDUSTRY_BASELINE
  sk_on_algorithm: NOT_DISCLOSED

input_measurements:
  - Capacity
  - Internal resistance
  - Open-circuit voltage
  - Self-discharge
  - Impedance
  - Thermal behavior
  - Formation history
  - Dimensional data

functions:
  - Identify defective cells
  - Assign performance grade
  - Match similar cells for module or pack
  - Route cells to rework or rejection
  - Create final cell genealogy record

critical_decisions:
  - Acceptance threshold
  - Grade boundary
  - Module matching rule
  - Rework eligibility
  - Data-retention policy

principal_risks:
  - Overly wide pack dispersion
  - False rejection
  - Latent defect escape
  - Inconsistent grade criteria
  - Measurement drift
  - Incomplete genealogy

source_ids:
  - SRC-SKON-D04-040
  - SRC-SKON-D04-041

confidence:
  process_need: VERY_HIGH
  sk_on_grading_rule: NOT_DISCLOSED
```

포메이션 이후 셀은 용량·저항·전압 안정성 등을 기준으로 선별되고, 유사한 특성을 가진 셀을 모듈이나 팩에 배치해야 한다. DOE 자료는 포메이션과 선별을 하나의 주요 제조영역으로 다루지만, SK온의 등급기준과 매칭 알고리즘은 공개되지 않았다. ([energy.gov][6])

---

## TECH-SKON-D04-060 — Nondestructive Cell Inspection

```yaml
technology_id: TECH-SKON-D04-060
canonical_name: High-Speed Nondestructive Cell Inspection
korean_name: 고속 비파괴 셀 검사

technology_category:
  - Quality Inspection
  - Defect Detection
  - End-of-Line and In-Line NDI

technology_status:
  industry_need: VERY_HIGH
  sk_on_integrated_system: NOT_DISCLOSED

candidate_methods:
  - Optical vision
  - X-Ray radiography
  - Computed tomography
  - Ultrasound
  - Thermography
  - Acoustic inspection
  - Electrical impedance
  - Helium or pressure leak test

target_defects:
  electrode:
    - Misalignment
    - Fold
    - Crack
    - Burr
    - Foreign particle

  cell_assembly:
    - Tab-weld defect
    - Stack deformation
    - Pouch wrinkle
    - Can-insertion defect

  sealing:
    - Microleak
    - Seal contamination
    - Incomplete weld

  electrochemical:
    - Internal short precursor
    - Abnormal resistance
    - Self-discharge

source_ids:
  - SRC-SKON-D04-036
  - SRC-SKON-D04-037
  - SRC-SKON-D04-040

confidence:
  industry_requirement: VERY_HIGH
  sk_on_tool_mapping: NOT_DISCLOSED
```

DOE는 고속 인라인 비파괴검사를 셀 결함과 내부단락을 조기에 찾기 위한 주요 제조혁신으로 제시했다. SK온은 Z-Folding 정렬과 On-Vent 레이저 깊이·파열압력 제어의 중요성을 공개했지만, 실제 검사장비 구성과 전수검사 범위는 공개하지 않았다. ([energy.gov][6])
