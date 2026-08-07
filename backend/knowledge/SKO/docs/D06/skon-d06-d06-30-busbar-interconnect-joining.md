---
id: skon-d06-d06-30-busbar-interconnect-joining
title: Busbar·Interconnect Joining
summary: "배터리 모듈 버스바-전극 접합 공정의 조립·접합 방식, 핵심 파라미터, 품질 기준, 결함, 검사 방법을 정의하는 프로세스 규격"
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [전극탭, 버스바어셈블리, 전기접합, 레이저용접, 저항용접, 초음파용접, FPCB, 전기위상, 모듈팩, 품질검사, 결함, 전기연결]
related: []
priority: normal
domain: D06
section: D06-30.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 877
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-30. Busbar·Interconnect Joining

## PROC-SKON-D06-019C — Module Electrical Interconnection

```yaml
process_id: PROC-SKON-D06-019C
canonical_name: Module Busbar and Interconnect Joining
korean_name: 모듈 버스바·전기 연결부 접합
process_layer: MODULE_PACK
ownership_scope: SK_ON_CONFIRMED

input_objects:
  - Cell stack
  - Electrode leads or cell terminals
  - Busbar assembly
  - Insulation frame
  - FPCB or sensing module
  - Module terminal

output_object:
  - Electrically interconnected cell module

assembly_steps:
  - Busbar-frame positioning
  - Lead insertion through slot
  - Lead bending or forming
  - Lead-to-busbar joining
  - Module-terminal fastening
  - Sensing-line connection
  - Insulation-cover installation

candidate_joining_methods:
  - Laser welding
  - Ultrasonic welding
  - Resistance welding
  - Mechanical fastening where applicable

critical_process_parameters:
  - Lead and busbar alignment
  - Joining energy
  - Focus or horn position
  - Weld speed
  - Clamping force
  - Joint overlap
  - Lead-bending position
  - Busbar insulation clearance

critical_quality_attributes:
  - Electrical resistance
  - Mechanical strength
  - Weld penetration
  - Weld-area consistency
  - Spatter absence
  - Terminal-position accuracy
  - Insulation distance
  - FPCB connection integrity

defect_modes:
  - Missing weld
  - Weak weld
  - Excess penetration
  - Lead tearing
  - Busbar misalignment
  - Spatter
  - Electrical short
  - High joint resistance
  - Sensing-line disconnection
  - Wrong series-parallel connection

inspection_methods:
  - Vision inspection
  - Weld-signature monitoring
  - Joint resistance
  - Continuity test
  - Pull or peel sampling
  - Terminal-position measurement
  - Insulation-resistance test
  - Electrical topology verification

technology_ids:
  - TECH-SKON-D04-055
  - TECH-SKON-D04-061
  - TECH-SKON-D04-062

candidate_patent_family_ids:
  - PF-CAND-SKON-D05-010

source_ids:
  - SRC-PAT-D06-028

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-PAT-D06-028

sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

특허문서는 전극탭을 버스바 슬롯에 통과시켜 절곡·접합하고, 버스바 어셈블리를 FPCB 센싱모듈과 연결하는 구조를 제시한다. 레이저용접은 가능한 접합방식 중 하나로 설명되며 실제 공장별 접합방식은 공개되지 않았다. ([구글 특허][5])

---

## 30.1 Module Electrical Topology Record

```yaml
module_electrical_connection_record:

  module:
    - Module serial number
    - Electrical configuration
    - Busbar assembly ID
    - Sensing module ID

  joints:
    - Weld ID
    - Cell serial number
    - Cell terminal or lead ID
    - Busbar position
    - Polarity
    - Process signature

  sensing:
    - Voltage-sense channel
    - Temperature-sensor channel
    - FPCB connector position
    - Continuity result

  verification:
    - Expected topology
    - Measured topology
    - Joint resistance
    - Isolation result
    - Polarity result
```

---
