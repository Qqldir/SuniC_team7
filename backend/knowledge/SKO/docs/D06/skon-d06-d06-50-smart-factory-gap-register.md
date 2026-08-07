---
id: skon-d06-d06-50-smart-factory-gap-register
title: Smart Factory Gap Register
summary: "SK온 제조공정의 스마트화에 필요한 9가지 주요 부족 영역(시스템, 디지털트윈, 장비연결, OEE, 수율, 에너지, 예측정비, 보안, AI)을 체계적으로 정의한 개선 과제 목록이다."
tags: [d06, process, schema]
keywords: [MES, 디지털 트윈, OEE, 예측보전, 에너지 효율, 사이버보안, 설비 연결, 제조 AI, 공백 분석, 기술 진단, OT 보안, 예측 정비, 수율, 다운타임]
related: []
priority: normal
domain: D06
section: D06-50.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 528
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-50. Smart Factory Gap Register

```yaml
smart_factory_gaps:

  - gap_id: GAP-D06-SF-001
    subject: Current SK On system architecture
    missing:
      - MES and historian vendors
      - Plant-specific architecture
      - Integration completeness
    priority: HIGH

  - gap_id: GAP-D06-SF-002
    subject: Siemens digital-twin implementation
    missing:
      - Applied plant
      - Applied process
      - Twin maturity
      - Quantified performance
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-003
    subject: Equipment connectivity
    missing:
      - Connected-equipment ratio
      - Common tag standard
      - Time-synchronization quality
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-004
    subject: OEE and downtime
    missing:
      - Actual OEE
      - Loss taxonomy
      - Unclassified downtime
      - Changeover performance
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-005
    subject: Yield and scrap
    missing:
      - Process FPY
      - Rework rate
      - Value-added scrap
      - Coordinate genealogy
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-006
    subject: Energy
    missing:
      - Meter coverage
      - Process-level consumption
      - Energy per accepted cell
      - Formation recovery efficiency
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-007
    subject: Predictive maintenance
    missing:
      - Deployed asset list
      - Failure-prediction performance
      - Maintenance savings
    priority: HIGH

  - gap_id: GAP-D06-SF-008
    subject: OT cybersecurity
    missing:
      - Zone architecture
      - Asset inventory coverage
      - Recovery-test result
      - Vendor-access controls
    priority: VERY_HIGH

  - gap_id: GAP-D06-SF-009
    subject: Manufacturing AI
    missing:
      - Production deployment
      - Model version and validation
      - Drift and rollback performance
    priority: VERY_HIGH
```

---
