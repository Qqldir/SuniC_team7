---
id: skes-d06-24-knowledge-graph-and-query-templates
title: Knowledge Graph and Query Templates
summary: "LNG·발전·수소·ESS 운영 자산의 관계를 지식그래프로 모델링하고, 프로세스·고장·계약을 통합 추적하는 쿼리 템플릿을 제공한다."
tags: [d06, process, schema, "xref:d05"]
keywords: [지식그래프, 운영데이터, LNG·발전·수소, 프로세스 관계, RBMS, PPA, ESS, 고장 진단, KPI, 계약의무]
related: []
priority: normal
domain: D06
section: 24
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 848
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 24. Knowledge Graph and Query Templates

## 24.1 Node Types

```yaml
nodes:
  - Organization
  - Site
  - Asset
  - EquipmentClass
  - Process
  - FlowLot
  - Cargo
  - TankInventory
  - Tag
  - OperatingEvent
  - Alarm
  - FailureMode
  - WorkOrder
  - Inspection
  - KPI
  - ContractObligation
  - MeterRecord
  - Model
  - SafetyBarrier
  - OI_Seed
  - Provider
  - EvidenceSource
```

## 24.2 Edge Types

```yaml
edges:
  - OPERATES
  - LOCATED_AT
  - PARTICIPATES_IN
  - PRECEDES
  - CONSUMES
  - PRODUCES
  - STORED_IN
  - MEASURED_BY
  - CONTROLLED_BY
  - TRIGGERS
  - INDICATES
  - CAUSES
  - MITIGATED_BY
  - GENERATES_WORK_ORDER
  - SATISFIES_CONTRACT
  - CALCULATES_KPI
  - USES_MODEL
  - REQUIRES_DATA
  - CANDIDATE_FOR
  - SUPPORTED_BY_SOURCE
```

## 24.3 Example Relationship Triples

```yaml
triples:
  - subject: PROC-ENS-D06-LNG-008
    predicate: PRECEDES
    object: PROC-ENS-D06-LNG-009
  - subject: PROC-ENS-D06-LNG-010
    predicate: CANDIDATE_FOR
    object: SEED-ENS-D06-013
  - subject: FM-ENS-D06-009
    predicate: INDICATED_BY
    object: gas_turbine_exhaust_temperature_spread
  - subject: PROC-ENS-D06-CG-004
    predicate: USES_MODEL
    object: RBMS_model_internal_gap
  - subject: PROC-ENS-D06-REN-005
    predicate: SATISFIES_CONTRACT
    object: direct_PPA_obligation
  - subject: PROC-ENS-D06-ESS-001
    predicate: USES_MODEL
    object: MarketCapture
  - subject: PROC-ENS-D06-H2-002
    predicate: PRODUCES
    object: liquid_hydrogen_batch
  - subject: PROC-ENS-D06-CCS-001
    predicate: CALCULATES_KPI
    object: KPI-ENS-D06-CCS-002
```

## 24.4 Query Templates

1. `LNG cargo ETA가 48시간 지연될 때 terminal inventory와 발전 dispatch에 연결되는 프로세스·KPI·Seed는?`
2. `BOG compressor 고장에 앞서 나타나는 tag와 alarm, downstream 영향은?`
3. `복합발전 heat rate 저하를 GT·HRSG·condenser·ambient 요인으로 분해하려면 어떤 데이터가 필요한가?`
4. `7개 도시가스 자회사에 공통 적용 가능한 RBMS 과제와 법인별 내부검증 항목은?`
5. `드론 영상 anomaly가 실제 배관수리까지 이어졌는지 어떻게 추적하는가?`
6. `직접 PPA 정산에서 meter·REC·계약 version 불일치를 찾는 방법은?`
7. `ESS 수익 최적화가 degradation 또는 안전 한계를 침해하는지 검증하는 필드는?`
8. `EV 충전부하 제어가 건물 피크와 고객충전 완료율에 미친 효과는?`
9. `액화수소 boil-off가 생산·저장·탱크로리·충전소 중 어디서 발생했는가?`
10. `CCS gross captured와 net avoided 차이를 계산하는 계량 lineage는?`
11. `D05 파트너 IP 때문에 build보다 partner가 적합한 D06 Seed는?`
12. `OT write access 없이 shadow-mode로 검증할 수 있는 P0 과제는?`

---
