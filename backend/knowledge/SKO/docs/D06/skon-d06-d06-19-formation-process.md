---
id: skon-d06-d06-19-formation-process
title: Formation Process
summary: "리튬이온 배터리 셀의 전기화학적 활성화 공정(포메이션)의 표준 절차, SK온 사양, 공정 파라미터, 품질 기준을 정의한다."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [배터리 셀 활성화, 충방전, SEI 형성, 쿨롱 효율, 공정 파라미터, 품질 속성, 초기 용량, 가스 생성, 셀 스웰링, Electrochemical activation, 포메이션, 배터리 셀, 충방전 사이클, 내부 저항, 이상 검출, 전극 활성화]
related: []
priority: normal
domain: D06
section: D06-19.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1580
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-19. Formation Process

## 19.1 Canonical Formation Flow

```text
Electrolyte-Filled and Temporarily Sealed Cell
                ↓
Pre-Wetting / Pre-Aging Hold
                ↓
Formation Tray Loading
                ↓
Electrical Contact Verification
                ↓
Initial Low-Rate Charging
                ↓
Voltage Hold or Rest
                ↓
Discharge / Additional Charge Steps
                ↓
Gas and Swelling Generation
                ↓
Intermediate Inspection
                ↓
Degassing and Final Sealing
                ↓
Additional Formation or Aging
```

정확한 순서는 제조사·셀 구조에 따라 달라진다. 일부 공정은 초기 충전 후 디개싱을 수행하고 다시 충방전하며, 일부는 별도의 프리차징·에이징·리텐션 검사단계를 둔다. SK온의 실제 순서는 공개자료만으로 확정할 수 없다.

---

## PROC-SKON-D06-015 — Cell Formation

```yaml
process_id: PROC-SKON-D06-015
canonical_name: Lithium-Ion Cell Formation
korean_name: 배터리 셀 포메이션
process_layer: CELL_FINISHING
ownership_scope: SK_ON_CONFIRMED

input_object:
  - Electrolyte-filled and temporarily sealed cell

output_object:
  - Electrochemically activated cell

equipment_classes:
  - Formation rack
  - Formation tray
  - Programmable charge-discharge channel
  - Cell-contact probe
  - Temperature sensor
  - Pressure or compression fixture
  - Thermal-management system
  - Safety monitoring system

critical_process_parameters:
  - Charge current
  - Discharge current
  - Voltage limits
  - Constant-voltage duration
  - Rest duration
  - Number of steps
  - Cell temperature
  - Applied stack pressure
  - Cut-off conditions
  - Channel calibration

critical_quality_attributes:
  - Voltage response
  - Current response
  - Charge and discharge capacity
  - Coulombic efficiency
  - DC internal resistance
  - Temperature rise
  - Cell swelling
  - Gas generation
  - Self-discharge indication
  - Channel-to-channel consistency

primary_functions:
  - Electrode–electrolyte interphase formation
  - Cell electrochemical activation
  - Initial capacity measurement
  - Early defect detection
  - Formation of quality-prediction features

defect_modes:
  - Abnormal voltage rise
  - Abnormal voltage drop
  - Excessive temperature rise
  - Excessive gas generation
  - Low initial efficiency
  - Internal leakage current
  - Contact-channel error
  - Incomplete electrochemical activation

inspection_methods:
  - Voltage and current curve analysis
  - Capacity measurement
  - Coulombic-efficiency calculation
  - Temperature monitoring
  - Thickness or pressure monitoring
  - Relative cell comparison
  - Model-based anomaly detection

technology_ids:
  - TECH-SKON-D04-058
  - TECH-SKON-D04-035
  - TECH-SKON-D04-042

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-005
  - PF-CAND-SKON-D05-006

source_ids:
  - SRC-BASE-D06-016
  - SRC-BASE-D06-017
  - SRC-SKON-D06-018
  - SRC-SKON-D06-019

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-BASE-D06-016
  - SRC-SKON-D06-018

sk_on_parameter_disclosure: NOT_DISCLOSED
```

---

## 19.2 Formation Curve Data Model

```yaml
formation_channel_record:

  cell_identity:
    - Cell serial number
    - Stack ID
    - Electrolyte-filling record
    - Temporary-seal record

  formation_identity:
    - Formation batch ID
    - Rack ID
    - Tray ID
    - Channel ID
    - Recipe version
    - Start and end timestamp

  time_series:
    - Voltage
    - Current
    - Capacity
    - Temperature
    - Applied pressure
    - Cell thickness
    - Channel status
    - Alarm event

  calculated_features:
    - Initial coulombic efficiency
    - Charge-capacity segments
    - Discharge capacity
    - DC resistance
    - Differential capacity features
    - Voltage relaxation
    - Temperature-rise rate
    - Swelling rate
    - Abnormal-pattern score

  disposition:
    - Continue
    - Additional formation
    - Hold
    - Degas
    - Rework
    - Scrap
```

---

## 19.3 Formation Defect Detection Architecture

```text
Cell Voltage·Current·Temperature·Pressure
                    ↓
          Recipe-Phase Alignment
                    ↓
        Reference Curve Comparison
                    ↓
  Absolute Threshold + Relative Cell Comparison
                    ↓
       Defect Probability and Cause Class
                    ↓
Continue / Hold / Retest / Degas / Scrap
```

SK온의 공개출원은 포메이션 단계에서 압력과 전압 패턴을 이용해 결함을 판별하는 방향을 제시한다. 이를 실제 시스템으로 구현하려면 충방전기 채널오차, 셀 접촉불량과 진짜 내부결함을 구분해야 한다. ([구글 특허][3])

---

## 19.4 Formation Root-Cause Graph

```text
Incomplete Electrolyte Wetting
             ↓
Local Ionic-Transport Limitation
             ↓
Abnormal Voltage·Resistance Response
             ↓
Formation Anomaly
```

```text
Tab Weld High Resistance
             ↓
Local Joule Heating·Voltage Loss
             ↓
Abnormal Temperature and Voltage Curve
             ↓
Formation Hold or Reject
```

```text
Separator or Electrode Defect
             ↓
Leakage Current or Local Contact
             ↓
Abnormal Voltage Relaxation
             ↓
Potential Low-Voltage Defect
```

위 관계는 일반적 원인 후보이며, 실제 결함판정에는 조립·용접·함침·충방전 채널 데이터를 함께 검증해야 한다.

---
