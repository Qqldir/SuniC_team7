---
id: skon-d06-d06-33-cell-to-pack-direct-cell-installation
title: Cell-to-Pack Direct Cell Installation
summary: "모듈 조립 단계를 생략하고 셀을 직접 팩에 탑재하는 CTP 기술의 제조 경계와 핵심 공정(셀 어셈블리 준비, 팩 하우징 직접 탑재, 전기 연결)을 정의한 문서."
tags: [d06, process, schema, "xref:d04", "xref:d05"]
keywords: [CTP, 모듈 공정 삭제, 셀 어셈블리, 팩 통합, 제조 경계, 열 인터페이스, 버스바, 품질 기준, 검사 방법, 직접 탑재 설비, 셀-팩 직접 통합, 팩 하우징 탑재, 모듈 공정 생략, 열관리 통합, 버스바 연결, 가스 경로 관리, 구조 통합, 제조 공정]
related: []
priority: normal
domain: D06
section: D06-33.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1384
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-33. Cell-to-Pack Direct Cell Installation

## 33.1 CTP Manufacturing Boundary

```text
Conventional:
Cell → Module Assembly → Module Test → Pack Installation

CTP:
Cell / Cell Assembly
        ↓
Direct Electrical·Thermal·Structural Integration
        ↓
Pack Test
```

CTP는 모듈 공정이 단순 삭제되는 것만을 의미하지 않는다. 모듈이 담당하던 셀 고정·압축·전기연결·절연·열관리·가스배출·서비스 기능을 팩 구조가 직접 수행해야 한다. 이는 SK온 공식 설명과 직접 팩 탑재형 특허를 결합한 분석이다. ([ASK Inno][1])

---

## PROC-SKON-D06-020A — Direct Cell-Assembly Preparation

```yaml
process_id: PROC-SKON-D06-020A
canonical_name: Direct Cell-Assembly Preparation for CTP
korean_name: CTP 직접 탑재용 셀 어셈블리 준비
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

functions:
  - Cell matching
  - Cell stacking
  - Side-cover or support-component installation
  - Busbar pre-assembly
  - Heat-exchange surface preparation
  - Gas-path component alignment

critical_quality_attributes:
  - Cell alignment
  - Cell-assembly rigidity
  - Busbar position
  - Heat-exchange surface flatness
  - Gas-path openness
  - Pack-housing interface dimensions

technology_ids:
  - TECH-SKON-D04-004
  - TECH-SKON-D04-024
  - TECH-SKON-D04-026
  - TECH-SKON-D04-062

patent_family_ids:
  - PF-SKON-D05-027

source_ids:
  - SRC-PAT-D06-027

evidence_level: ANALYST_INFERENCE
```

---

## PROC-SKON-D06-020B — Direct Installation into Pack Housing

```yaml
process_id: PROC-SKON-D06-020B
canonical_name: Direct Cell Installation into Pack Housing
korean_name: 셀 어셈블리 팩 하우징 직접 탑재
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

equipment_classes:
  - Pack-housing fixture
  - Cell-assembly handling robot
  - Positioning and guide system
  - Insertion-force sensor
  - Vision and 3D metrology
  - Fastening or adhesive system

critical_process_parameters:
  - Cell-assembly position
  - Insertion path
  - Insertion force
  - Bottom thermal-interface contact
  - Side-cover engagement
  - Fastening position
  - Housing deformation

critical_quality_attributes:
  - Direct thermal contact
  - Assembly position
  - Cell clearance
  - Pack-floor flatness
  - Insulation clearance
  - Structural retention
  - Gas-path alignment

defect_modes:
  - Cell or pouch damage
  - Mis-seating
  - Thermal-interface displacement
  - Housing interference
  - Side-cover coupling failure
  - Insufficient bottom contact
  - Gas-path blockage

inspection_methods:
  - Force–position curve
  - Vision
  - 3D dimensional scan
  - Thermal-contact inspection
  - Electrical isolation
  - Gas-path check

patent_family_ids:
  - PF-SKON-D05-027
  - PF-SKON-D05-028
  - PF-SKON-D05-029

technology_ids:
  - TECH-SKON-D04-004
  - TECH-SKON-D04-017
  - TECH-SKON-D04-062

source_ids:
  - SRC-PAT-D06-027

evidence_level: ANALYST_INFERENCE
```

---

## PROC-SKON-D06-020C — CTP Electrical Connection

```yaml
process_id: PROC-SKON-D06-020C
canonical_name: CTP Electrical Connection
korean_name: CTP 전기 연결
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

assembly_components:
  - Cell-level or assembly-level busbars
  - Pack high-voltage busbar
  - Voltage-sensing circuit
  - Pack service disconnect
  - Fuse and contactor interface

critical_quality_attributes:
  - Electrical topology
  - Joint resistance
  - Isolation distance
  - Voltage-channel integrity
  - Polarity
  - Serviceability

principal_risk:
  - A connection defect can affect a larger pack section because the module boundary is reduced

technology_ids:
  - TECH-SKON-D04-004
  - TECH-SKON-D04-055
  - TECH-SKON-D04-062

source_ids:
  - SRC-PAT-D06-027
  - SRC-PAT-D06-028

evidence_level: ANALYST_INFERENCE
```

---

## PROC-SKON-D06-020D — CTP Thermal·Gas-Path Integration

```yaml
process_id: PROC-SKON-D06-020D
canonical_name: CTP Thermal and Gas-Path Integration
korean_name: CTP 열관리·가스경로 통합
process_layer: MODULE_PACK
ownership_scope: SK_ON_DEVELOPMENT

functions:
  - Cell-to-pack cooling contact
  - Coolant-channel integration
  - Thermal-barrier placement
  - Sidewall or center-beam vent connection
  - Gas discharge to pack exterior
  - Thermal-propagation compartmentalization

critical_quality_attributes:
  - Cooling contact
  - Coolant flow
  - Barrier position
  - Gas-path continuity
  - Vent direction
  - Electrical isolation

technology_ids:
  - TECH-SKON-D04-002
  - TECH-SKON-D04-016
  - TECH-SKON-D04-024
  - TECH-SKON-D04-025
  - TECH-SKON-D04-026
  - TECH-SKON-D04-027

patent_family_ids:
  - PF-SKON-D05-020
  - PF-SKON-D05-022
  - PF-SKON-D05-027
  - PF-SKON-D05-029

source_ids:
  - SRC-SKON-D06-025
  - SRC-PAT-D06-027
  - SRC-PAT-D06-030

evidence_level: ANALYST_INFERENCE
```

---
