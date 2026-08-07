---
id: skon-d06-d06-dq-004-module-ctp-process-id-reconciliation
title: 004. Module·CTP Process-ID Reconciliation
summary: 배터리 모듈과 팩 조립 공정을 공식 공정 ID와 세부 단계로 정의하는 SK온 제조 프로세스 마스터.
tags: [d06, process, schema, "xref:d05"]
keywords: [공정 ID 매핑, 모듈 조립 공정, Cell-to-Pack 조립, 팩 조립 공정, 공정 계층 구조, 제조공정 마스터, End-of-Line 검사, Busbar 조립, BMS 통합, D06 배터리 제조, 모듈 조립, Cell-to-Pack, 공정 ID 체계, 팩 조립, BMS, EoL 검사, 냉각 회로, SK온 D06]
related: []
priority: normal
domain: D06
section: D06-DQ
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 605
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# SK온 D06 Manufacturing Process & Operations

## Part 4. Module·Pack·CTP Assembly·Pouch-Integrated Prismatic·Pack EoL

**문서 버전:** D06 v1.3
**기준일:** 2026-08-02
**이전 완료 지점:** `D06-27 D05 Patent Backlog Update`

> 모듈·팩 공정은 고객 차량 구조, 셀 폼팩터와 열관리 방식에 따라 크게 달라진다. 아래 내용은 SK온 공식 공개기술·공개 특허와 일반 제조구조를 결합한 데이터 모델이며, 실제 공장별 공정순서·접합조건·검사기준·수율은 공개되지 않았다.

---

# D06-DQ-004. Module·CTP Process-ID Reconciliation

D06 초기 Process Master에 등록된 상위 공정 ID를 유지하고, 세부공정은 하위 ID로 확장한다.

```yaml
process_id_reconciliation:

  PROC-SKON-D06-019:
    canonical_name: Module Assembly
    sub_processes:
      - PROC-SKON-D06-019A Cell Receiving and Matching
      - PROC-SKON-D06-019B Module Cell Stacking and Compression
      - PROC-SKON-D06-019C Busbar and Interconnect Joining
      - PROC-SKON-D06-019D Thermal Interface and Cooling Plate
      - PROC-SKON-D06-019E Module Housing and Sensing Integration

  PROC-SKON-D06-020:
    canonical_name: Cell-to-Pack Assembly
    sub_processes:
      - PROC-SKON-D06-020A Direct Cell-Assembly Preparation
      - PROC-SKON-D06-020B Direct Installation into Pack Housing
      - PROC-SKON-D06-020C CTP Electrical Connection
      - PROC-SKON-D06-020D CTP Thermal and Gas-Path Integration
      - PROC-SKON-D06-020E Pouch-Integrated Prismatic Assembly

  PROC-SKON-D06-021:
    canonical_name: Pack Assembly and End-of-Line
    sub_processes:
      - PROC-SKON-D06-021A Pack Structural Assembly
      - PROC-SKON-D06-021B BMS and High-Voltage Integration
      - PROC-SKON-D06-021C Coolant-Circuit Integration
      - PROC-SKON-D06-021D Pack End-of-Line Test

reserved_existing_ids:
  PROC-SKON-D06-022: Manufacturing Digital Twin
  PROC-SKON-D06-023: Intelligent Production Equipment
  PROC-SKON-D06-024: Manufacturing Digital Thread
```

---
