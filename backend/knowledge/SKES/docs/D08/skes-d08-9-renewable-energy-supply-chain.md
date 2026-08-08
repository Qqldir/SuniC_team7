---
id: skes-d08-9-renewable-energy-supply-chain
title: Renewable-Energy Supply Chain
summary: "해상풍력과 태양광 프로젝트의 공급망 구조, 패키지별 위험요소, 품질 검증 게이트를 매핑한 가이드"
tags: [d08, supply-chain, table]
keywords: [해상풍력, 태양광, 공급망 게이트, WTG, FAT/SAT, EPC, 설비 위험, 패키지 맵, 공급사 관리, 품질 검증]
related: []
priority: normal
domain: D08
section: 9
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 628
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 9. Renewable-Energy Supply Chain

## 9.1 Offshore-Wind Package Map

| Package | 공급범위 | 핵심 데이터 | 대표 위험 |
|---|---|---|---|
| WTG | nacelle·blade·tower·SCADA·warranty | serial·BOM·power curve·alarm | blade/gearbox·OEM lock-in |
| foundation | steel·fabrication·coating·TP | heat·weld·NDT·coating | steel price·quality |
| array/export cable | cable·joint·termination·test | drum·route·joint·TDR | damage·repair vessel |
| offshore substation | transformer·switchgear·control | FAT/SAT·relay setting | long lead-time |
| installation vessel | WTG/foundation/cable vessel | weather window·availability | schedule congestion |
| port/logistics | marshalling·heavy lift·storage | item location·preservation | damage·delay |
| O&M | CTV/SOV·spares·inspection | weather·work order·parts | access restriction |

Jeonnam OWF1은 96MW·10기 상업운전과 현지 제작 foundation·설치선·subsea cable 방향이 공식/투자자 자료에서 확인된다. 특정 OEM·개별 공급사명은 신뢰 가능한 공개근거가 확보되지 않은 경우 내부 EPC package ledger에서 확인한다.

## 9.2 Solar-PV Package Map

| Package | 승인 필드 | 운영 인계 필드 |
|---|---|---|
| module | maker·model·serial·BOM·flash·degradation warranty | string mapping·replacement history |
| inverter | model·serial·firmware·efficiency | alarm·spare·warranty |
| structure | material·coating·load | inspection·corrosion |
| cable/connector | lot·rating·compatibility | route·joint·thermal event |
| transformer | serial·test·oil | DGA·maintenance |
| EPC | design revision·as-built·punch | handover completeness |

## 9.3 Renewable Supply-Chain Gates

| Gate | 필수 증빙 | AI/OI 적용 |
|---|---|---|
| design freeze | approved BOM·interface matrix | change-impact graph |
| factory acceptance | FAT·NCR·photo·test raw data | anomaly/NCR clustering |
| shipment | packing·serial·preservation·ETA | delay prediction |
| installation | weather·vessel·lift·inspection | schedule optimization |
| commissioning | SAT·SCADA point list·punch | digital handover QA |
| warranty | baseline·defect·claim·response | claim detection |

---
