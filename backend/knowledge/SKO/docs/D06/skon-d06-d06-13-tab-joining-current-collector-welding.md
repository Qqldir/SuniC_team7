---
id: skon-d06-d06-13-tab-joining-current-collector-welding
title: Tab Joining & Current-Collector Welding
summary: "배터리 셀의 전극 탭과 집전체 접합 공정에 적용 가능한 세 가지 용접 방식의 파라미터, 품질 기준, 검사 방법을 규정한다."
tags: [d06, process, schema, "xref:d04"]
keywords: [전극 탭, 집전체, 초음파 용접, 레이저 용접, 저항용접, 용접 신호, 전기저항, 셀 조립, 저항 용접, 공정 파라미터, 품질 속성, 전기 저항]
related: []
priority: normal
domain: D06
section: D06-13.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1007
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-13. Tab Joining & Current-Collector Welding

## PROC-SKON-D06-012 — Tab and Current-Collector Joining

```yaml
process_id: PROC-SKON-D06-012
canonical_name: Electrode Tab and Current-Collector Joining
korean_name: 전극 탭·집전체 접합
process_layer: CELL_ASSEMBLY
ownership_scope: INDUSTRY_BASELINE

input_objects:
  - Electrode stack
  - Cathode-tab bundle
  - Anode-tab bundle
  - External lead tab or terminal

output_object:
  - Electrically connected electrode assembly

candidate_joining_methods:
  - Ultrasonic welding
  - Laser welding
  - Resistance welding

selection_factors:
  - Aluminum or copper material
  - Number and thickness of foils
  - Lead-tab material
  - Joint geometry
  - Heat-input limitation
  - Required electrical resistance
  - Required mechanical strength
  - Production takt time

critical_process_parameters:
  ultrasonic:
    - Amplitude
    - Force
    - Energy
    - Welding time
    - Horn displacement

  laser:
    - Laser power
    - Scan speed
    - Focus position
    - Beam path
    - Shielding condition

  resistance:
    - Current
    - Force
    - Pulse duration
    - Electrode condition

critical_quality_attributes:
  - Joint electrical resistance
  - Joint tensile or peel strength
  - Weld area
  - Penetration depth
  - Void and crack absence
  - Spatter absence
  - Tab deformation
  - Heat-affected-zone control

defect_modes:
  - Insufficient weld
  - Excessive weld
  - Foil tearing
  - Tab burning
  - Spatter
  - Misalignment
  - Porosity
  - Interfacial contamination
  - High electrical resistance

inspection_methods:
  - Electrical-resistance measurement
  - Vision inspection
  - Weld-signature monitoring
  - Displacement monitoring
  - Pull or peel sampling
  - Ultrasound
  - X-ray or CT sampling
  - Metallographic cross-section sampling

sk_on_joining_method: NOT_DISCLOSED

technology_ids:
  - TECH-SKON-D04-055
  - TECH-SKON-D04-061

source_ids:
  - SRC-BASE-D06-015

evidence_level: THIRD_PARTY_VERIFIED
sk_on_parameter_disclosure: NOT_DISCLOSED
```

접합부의 전기저항·기계적 강도·열영향은 셀 성능과 안전에 영향을 줄 수 있으며, 레이저·초음파·저항용접은 소재와 구조에 따라 서로 다른 장단점을 가진다. ([ScienceDirect][7])

---

## 13.1 Weld Signature Data Model

```yaml
weld_event_record:

  joint_identity:
    - Weld ID
    - Cell-stack ID
    - Positive or negative polarity
    - Tab-bundle ID
    - External-lead ID

  equipment:
    - Welder ID
    - Tool or horn ID
    - Laser-head ID
    - Recipe version

  process_signature:
    - Energy
    - Power
    - Current
    - Force
    - Displacement
    - Vibration amplitude
    - Acoustic signal
    - Optical emission
    - Duration

  quality:
    - Resistance
    - Vision result
    - Weld-area estimate
    - Destructive-test sample result
    - Model defect probability

  disposition:
    - Accept
    - Rework
    - Scrap
    - Engineering review
```

---

## 13.2 Welding Quality Decision Hierarchy

```text
Process Signature
      ↓
Inline Visual·Electrical Check
      ↓
Anomaly-Detection Model
      ↓
Accept / Hold
      ↓
Sampling Destructive Test
      ↓
Model and Control-Limit Update
```

공정신호만으로 접합품질을 완전히 확정하기 어려우므로, 전기저항·비전·파괴검사 표본을 결합해 모델을 검증해야 한다. 이는 D06 분석모델이며 SK온의 현재 검사체계를 의미하지 않는다.

---
