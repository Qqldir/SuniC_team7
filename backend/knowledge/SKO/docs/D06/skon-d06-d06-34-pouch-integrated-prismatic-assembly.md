---
id: skon-d06-d06-34-pouch-integrated-prismatic-assembly
title: Pouch-Integrated Prismatic Assembly
summary: "파우치 셀을 알루미늄 케이스에 통합 조립하는 공정의 단계, 임계 파라미터, 품질 검사 방법을 상세히 설명하는 배터리 모듈 제조 기술 명세서."
tags: [d06, process, schema, "xref:d04"]
keywords: [니켈계 셀, 알루미늄 케이스, 냉각판, 열접착제, 버스바, PCB, 조립 공정, PROC-SKON-D06-020E, 품질 검사, 파우치 셀, 각형 배터리, 배터리 조립, 모듈 패킹, 열관리]
related: []
priority: normal
domain: D06
section: D06-34.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1099
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-34. Pouch-Integrated Prismatic Assembly

## PROC-SKON-D06-020E — Pouch-Integrated Prismatic Cell Assembly

```yaml
process_id: PROC-SKON-D06-020E
canonical_name: Pouch-Integrated Prismatic Cell Assembly
korean_name: 파우치 통합 각형 셀 조립
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

development_status:
  stage: PROTOTYPE_FINAL_VALIDATION
  source_id: SRC-SKON-D06-026

input_objects:
  - Multiple mid-nickel pouch cells
  - Aluminum case
  - Bottom cooling plate
  - Thermal adhesive
  - Inter-cell cooling plates where applicable
  - Compression pads
  - External busbars
  - PCB or sensing circuit
  - Directional vent components

output_object:
  - Pouch-integrated prismatic battery unit

provisional_assembly_flow:
  - Pouch-cell receiving and matching
  - Cell electrical-configuration assignment
  - Thermal-adhesive dispensing
  - Pouch-cell placement on bottom cooling plate
  - Compression-pad placement
  - Inter-cell cooling-plate placement where applicable
  - Cell stacking inside aluminum case
  - Busbar alignment and connection
  - PCB connection
  - Directional-vent alignment
  - Case closure
  - Electrical, structural and thermal validation

critical_process_parameters:
  - Cell serial and electrical sequence
  - Thermal-adhesive amount
  - Cell position
  - Compression-pad thickness
  - Inter-cell pressure
  - Cooling-plate position
  - Busbar alignment
  - PCB connector force
  - Aluminum-case dimensional tolerance
  - Vent orientation

critical_quality_attributes:
  - Cell-to-cooling-plate contact
  - Stack compression
  - Aluminum-case structural fit
  - Electrical configuration
  - Busbar connection resistance
  - PCB channel continuity
  - Vent direction
  - Insulation
  - Unit dimensions

defect_modes:
  - Incorrect series-parallel configuration
  - Missing compression pad
  - Thermal-adhesive void
  - Cooling-plate misalignment
  - Cell damage during case insertion
  - Busbar or PCB connection failure
  - Vent orientation error
  - Aluminum-case deformation
  - Uneven cell compression

inspection_methods:
  - Serial-sequence verification
  - Adhesive bead and mass inspection
  - Force–displacement monitoring
  - 3D dimensional scan
  - Busbar resistance test
  - PCB continuity test
  - Leak and coolant-flow test
  - Thermal-response test
  - Vibration and structural validation at prototype stage

technology_ids:
  - TECH-SKON-D04-017
  - TECH-SKON-D04-016
  - TECH-SKON-D04-026
  - TECH-SKON-D04-027
  - TECH-SKON-D04-062

source_ids:
  - SRC-SKON-D06-026

evidence_level: ANALYST_INFERENCE
basis_source_ids:
  - SRC-SKON-D06-026

sk_on_parameter_disclosure: PARTIALLY_DISCLOSED
```

공식자료는 중형 니켈계 파우치 셀, 알루미늄 케이스, 열접착제, 냉각판, 압축패드, 외부 버스바와 PCB 연결을 직접 설명한다. 위 조립순서는 해당 구조를 제조공정으로 변환한 분석이며 실제 SK온 파일럿 순서와 동일하다고 확정하지 않는다. ([ASK Inno][3])

---

## 34.1 Pouch-Integrated Prismatic Build Record

```yaml
pouch_integrated_prismatic_record:

  unit_identity:
    - Integrated unit serial number
    - Configuration: 1P4S, 2P2S or other
    - Tab orientation
    - Product revision

  cells:
    - Cell serial sequence
    - Cell matching result
    - Electrical position
    - Physical position

  structure:
    - Aluminum-case ID
    - Compression-pad lot and position
    - Cooling-plate ID
    - Vent-component ID

  thermal_interface:
    - Thermal-adhesive lot
    - Dispense amount
    - Dispense coordinates
    - Cure condition

  electrical:
    - Busbar ID
    - PCB ID
    - Joint records
    - Channel-continuity result

  final_validation:
    - Dimension
    - Compression
    - Resistance
    - Isolation
    - Thermal response
    - Vent orientation
```

---
