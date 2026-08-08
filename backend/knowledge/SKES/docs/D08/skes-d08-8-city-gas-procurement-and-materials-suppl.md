---
id: skes-d08-8-city-gas-procurement-and-materials-suppl
title: City-Gas Procurement and Materials Supply Chain
summary: 도시가스 설비자재의 입고검사·현장 연결·권역별 재고관리 및 공급사 자격심사 기준을 통합 규정한 E&S 공급망 운영 표준
tags: [d08, supply-chain, table]
keywords: [도시가스, 자재 추적, lot·serial, 공급사 자격, 권역별 재고, 현장 검사, 긴급복구, BCP]
related: []
priority: normal
domain: D08
section: 8
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 652
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 8. City-Gas Procurement and Materials Supply Chain

## 8.1 Boundary

E&S는 7개 도시가스 법인을 통해 8개 권역에 공급하지만, 법인별 도매가스 계약·city gate·자재 공급사·창고·시공사 명단은 공개자료에서 충분히 확인되지 않는다. 따라서 `공개 운영구조`와 `산업 baseline 자재체계`를 분리하고, 공급사명은 내부 구매원장 확보 전 확정하지 않는다.

## 8.2 City-Gas Material Genealogy

| 자재 | 추적키 | 입고검사 | 현장 연결 | 주요 위험 |
|---|---|---|---|---|
| PE pipe | maker·lot·resin·dimension | 외관·치수·성적서 | GIS segment·fusion joint | lot defect·aging |
| steel pipe | heat·mill·grade·coating | MTC·NDT·coating | weld ID·segment | corrosion·weld defect |
| valve | serial·size·pressure class | function/leak test | valve ID·GIS | stuck/leak |
| regulator | serial·set point·capacity | calibration | station ID | pressure excursion |
| meter | serial·model·class | calibration/seal | customer/site | bias·tamper |
| volume corrector | serial·firmware | configuration | meter ID | firmware/config error |
| odorant | batch·SDS·concentration | CoA | odorizer/run | under/over odorization |
| cathodic protection | anode/rectifier serial | output test | pipeline zone | corrosion protection loss |

## 8.3 Regional Inventory Model

| 레이어 | 재고 | 공유 가능성 | 통제 |
|---|---|---|---|
| central | 장기납기 공통품 | 7개사 공동조달 후보 | 표준규격·ownership |
| regional | 긴급복구 핵심품 | 인접권역 transfer | minimum emergency stock |
| contractor | 공사별 자재 | 제한적 | consignment/return |
| field vehicle | 소모·응급부품 | 낮음 | issue/usage reconciliation |

## 8.4 Supplier Qualification Gate

1. 법규·인증·시험설비.
2. lot/serial 추적성.
3. 공정변경 사전통보.
4. 불량 containment와 recall 능력.
5. 긴급납품·재난 BCP.
6. 현장 시공자 자격과 안전교육.
7. OT 장비의 firmware·SBOM·remote-access 통제.
8. ESG 행동강령·실사·개선계획.

---
