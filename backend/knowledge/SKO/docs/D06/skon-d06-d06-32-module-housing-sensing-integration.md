---
id: skon-d06-d06-32-module-housing-sensing-integration
title: Module Housing·Sensing Integration
summary: "셀 스택을 하우징에 조립하고 버스바·센서·하네스를 통합하는 배터리 모듈 제조공정의 입출력, 주요 파라미터, 결함 모드, 검사 기준을 정의한 산업 기준 명세"
tags: [d06, process, schema, "xref:d04"]
keywords: [셀 스택, 토크, FPCB, 센서, 버스바, 하네스, 검사, 절연, 가스 경로, 배터리 모듈, 고전압 절연, 환기경로]
related: []
priority: normal
domain: D06
section: D06-32.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 550
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-32. Module Housing·Sensing Integration

## PROC-SKON-D06-019E — Module Housing and Sensing

```yaml
process_id: PROC-SKON-D06-019E
canonical_name: Module Housing and Sensing Integration
korean_name: 모듈 하우징·센싱부 통합
process_layer: MODULE_PACK
ownership_scope: INDUSTRY_BASELINE

input_objects:
  - Compressed cell stack
  - Module housing
  - End and side plates
  - Busbar assembly
  - FPCB or wire harness
  - Voltage and temperature sensors
  - Insulation cover
  - Vent and gas-path components

output_object:
  - Completed battery module

assembly_functions:
  - Stack insertion into housing
  - Structural fastening
  - Busbar insulation
  - Voltage-sense connection
  - Temperature-sensor installation
  - Module-terminal installation
  - Vent-path alignment
  - Cover closing

critical_process_parameters:
  - Housing insertion position
  - Fastener torque and angle
  - Connector insertion force
  - Harness routing
  - Sensor attachment pressure
  - Cover-seal compression
  - Vent-component position

critical_quality_attributes:
  - Structural rigidity
  - Fastener completeness
  - Electrical isolation
  - Sensor-channel continuity
  - Harness retention
  - Terminal location
  - Gas-path continuity
  - Module dimensions

defect_modes:
  - Missing fastener
  - Incorrect torque
  - Pinched harness
  - Disconnected voltage channel
  - Sensor detachment
  - Insulation-cover displacement
  - Blocked vent path
  - Housing deformation

inspection_methods:
  - Torque trace
  - Vision and presence check
  - Connector-force monitoring
  - Sensor continuity
  - High-voltage isolation test
  - Module dimension inspection
  - Gas-path vision or flow test

technology_ids:
  - TECH-SKON-D04-026
  - TECH-SKON-D04-030
  - TECH-SKON-D04-062

source_ids:
  - SRC-PAT-D06-028
  - SRC-PAT-D06-029

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-PAT-D06-028
  - SRC-PAT-D06-029

sk_on_parameter_disclosure: NOT_DISCLOSED
```

---
