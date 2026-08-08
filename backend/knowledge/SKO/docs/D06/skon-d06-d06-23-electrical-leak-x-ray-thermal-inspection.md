---
id: skon-d06-d06-23-electrical-leak-x-ray-thermal-inspection
title: Electrical·Leak·X-Ray·Thermal Inspection
summary: 배터리 셀의 전기·절연·실링·X-ray·열화상을 포함한 EoL 검사 프로세스의 멀티모달 스택과 각 검사 공정의 상세 정의.
tags: [d06, process, schema, "xref:d05"]
keywords: [절연저항, 누설검사, 내부검사, 열화상, OCV, 단락검사, 실링, 배터리셀, 파우치, 품질관리, EoL 최종검사, 전기저항·절연, X-ray 내부검사, 열화상검사, 실링 무결성, OCV·DC저항, 포우치절연]
related: []
priority: normal
domain: D06
section: D06-23.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1315
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-23. Electrical·Leak·X-Ray·Thermal Inspection

## 23.1 Multimodal EoL Inspection Stack

```text
Cell Identification
        ↓
Appearance and Dimension
        ↓
Electrical Contact·OCV·Resistance
        ↓
Insulation and Short Inspection
        ↓
Leak and Seal Integrity
        ↓
X-Ray Internal Structure
        ↓
Thermographic Secondary Inspection
        ↓
Integrated Quality Decision
        ↓
Good / Retest / Repair / Reject
```

SK온의 공개 특허문서에는 충전저항·쇼트·외관·X-ray 검사와 결과기반 자동 선별이 포함되며, 다른 출원은 파우치 절연저항과 열화상, 또 다른 출원은 압력 또는 추적가스를 이용한 실링 검사를 제시한다. 이들은 SK온이 관련 검사기술을 연구·출원하고 있다는 근거이지만, 하나의 양산라인에 모두 결합됐다는 증거는 아니다. ([구글 특허][7])

---

## PROC-SKON-D06-018A — Electrical & Insulation Inspection

```yaml
process_id: PROC-SKON-D06-018A
canonical_name: Cell Electrical and Insulation Inspection
korean_name: 셀 전기·절연 검사
process_layer: CELL_FINISHING
ownership_scope: SK_ON_DEVELOPMENT

inspection_items:
  - OCV
  - DC resistance
  - Charge resistance
  - Short-circuit indication
  - Pouch insulation resistance
  - Terminal polarity
  - Contact integrity

candidate_secondary_signal:
  - Thermographic image

defect_modes:
  - Internal short indication
  - High resistance
  - Pouch insulation defect
  - Terminal contact defect
  - Measurement contact failure
  - False electrical reject

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-005
  - PF-CAND-SKON-D05-007

source_ids:
  - SRC-SKON-D06-018
  - SRC-SKON-D06-020
  - SRC-SKON-D06-022

evidence_level: DIRECT_OFFICIAL
sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

---

## PROC-SKON-D06-018B — Seal & Leak Inspection

```yaml
process_id: PROC-SKON-D06-018B
canonical_name: Cell Seal and Leak Inspection
korean_name: 셀 실링·누설 검사
process_layer: CELL_FINISHING
ownership_scope: SK_ON_DEVELOPMENT

candidate_methods:
  - Pressure decay
  - Vacuum decay
  - Tracer-gas leakage
  - Chamber pressure response
  - Gas concentration detection
  - Vision inspection

critical_quality_attributes:
  - Leak rate
  - Seal continuity
  - Seal-location integrity
  - Pouch damage absence
  - Electrolyte leakage absence

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-008

source_ids:
  - SRC-SKON-D06-021

evidence_level: DIRECT_OFFICIAL
sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

---

## PROC-SKON-D06-018C — X-Ray Internal Inspection

```yaml
process_id: PROC-SKON-D06-018C
canonical_name: Battery Cell X-Ray Inspection
korean_name: 배터리 셀 X-ray 내부검사
process_layer: CELL_FINISHING
ownership_scope: SK_ON_DEVELOPMENT

inspection_targets:
  - Electrode alignment
  - Electrode edge position
  - Tab and connection region
  - Foreign object candidate
  - Internal geometric defect
  - Stack structure

equipment_options:
  - Line scanner
  - TDI detector
  - Flat-panel detector
  - Multi-view imaging
  - Moving-stage imaging

system_functions:
  - Cell supply
  - Image acquisition
  - Defect determination
  - Good and defective cell sorting

patent_family_ids:
  - PF-SKON-D05-030
  - PF-SKON-D05-031

source_ids:
  - SRC-SKON-D06-022
  - SRC-SKON-D06-023

evidence_level: DIRECT_OFFICIAL
sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

SK온 출원은 검사 중 다음 셀을 공급·배치하는 교번형 스테이지와 검사결과에 따른 양품·불량품 분류를 제시하며, X-ray 전체영상을 한 번 또는 복수 촬영으로 획득하는 구조도 포함한다. ([구글 특허][7])

---

## 23.2 Inspection Fusion Record

```yaml
cell_eol_inspection_record:

  cell_identity:
    - Cell serial number
    - Formation batch
    - Aging batch
    - Grade record

  physical:
    - Dimensions
    - Thickness
    - Weight
    - Surface image

  electrical:
    - OCV
    - DCIR
    - Insulation resistance
    - Short-test result
    - Charge-resistance result

  seal:
    - Pressure-decay result
    - Tracer-gas result
    - Seal image
    - Leak location candidate

  internal_imaging:
    - X-ray image ID
    - Alignment measurements
    - Defect classification
    - Model confidence

  thermal:
    - Thermographic image ID
    - Maximum temperature
    - Local hotspot position

  final_decision:
    - Accept
    - Retest
    - Engineering review
    - Rework
    - Reject
```

---
