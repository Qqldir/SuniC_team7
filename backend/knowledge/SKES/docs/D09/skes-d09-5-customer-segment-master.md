---
id: skes-d09-5-customer-segment-master
title: Customer Segment Master
summary: "에너지 포트폴리오 13개 비즈니스 라인의 고객 분류 및 각 고객군의 주요 니즈, 거래 단위, 제품·프로세스 연계 정보."
tags: [d09, customer, table, "xref:d03", "xref:d06"]
keywords: [에너지 포트폴리오, 비즈니스 라인, LNG 발전용, 도시가스, 전력시장, 재생에너지 PPA, BESS, 충전 인프라, 수소, CCS]
related: [SEG-ENS-D09-01, SEG-ENS-D09-02, SEG-ENS-D09-03, SEG-ENS-D09-04, SEG-ENS-D09-05, SEG-ENS-D09-06, SEG-ENS-D09-07, SEG-ENS-D09-08, SEG-ENS-D09-09, SEG-ENS-D09-10, SEG-ENS-D09-11, SEG-ENS-D09-12, SEG-ENS-D09-13]
priority: normal
domain: D09
section: 5
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 529
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 5. Customer Segment Master

| Segment ID | Segment | Primary need | Buying/dispatch unit | D03 product join | D06 process join |
|---|---|---|---|---|---|
| `SEG-ENS-D09-01` | 발전용 LNG | 안정적 연료·가격·품질 | cargo/MMBtu | PS-ENS-LNG-01~04 | PRC-ENS-D06-01~13 |
| `SEG-ENS-D09-02` | 전력시장 | 가용전력·계통안정 | MW/MWh | PS-ENS-PWR-01 | PRC-ENS-D06-14~20 |
| `SEG-ENS-D09-03` | 지역열·증기 | 중단 없는 열·증기 | Gcal/h | PS-ENS-PWR-02 | PRC-ENS-D06-21~23 |
| `SEG-ENS-D09-04` | 가정용 도시가스 | 안전·정확요금·편의 | 계량점/Nm3 | PS-ENS-CG-01~03 | PRC-ENS-D06-24~30 |
| `SEG-ENS-D09-05` | 산업·상업 도시가스 | 공급신뢰·원가·부하관리 | Nm3/h | PS-ENS-CG-01 | PRC-ENS-D06-24~30 |
| `SEG-ENS-D09-06` | 직접 PPA | RE100·가격안정·증빙 | MW/MWh | PS-ENS-REN-03~05 | PRC-ENS-D06-34~36 |
| `SEG-ENS-D09-07` | KCE 시장형 BESS | 계통서비스·가격차익 | bid/award/MW | PS-ENS-ES-03 | PRC-ENS-D06-37~39 |
| `SEG-ENS-D09-08` | Utility NWA | 피크제어·투자회피 | availability/MW | PS-ENS-ES-03 | PRC-ENS-D06-37~39 |
| `SEG-ENS-D09-09` | 공동주택 충전 | 확장성·공정한 과금 | EVSE/session | PS-ENS-ES-07B | PRC-ENS-D06-40~41 |
| `SEG-ENS-D09-10` | 직장·상업 충전 | 직원편의·에너지관리 | port/kWh | PS-ENS-ES-07B | PRC-ENS-D06-40~41 |
| `SEG-ENS-D09-11` | Fleet 충전 | 출차준비·TCO·uptime | vehicle/route | PS-ENS-ES-07B~08 | PRC-ENS-D06-40~41 |
| `SEG-ENS-D09-12` | 수소버스·상용차 | 안정공급·짧은 충전 | kgH2/vehicle | PS-ENS-H2-01~03 | PRC-ENS-D06-42~44 |
| `SEG-ENS-D09-13` | 잠재 CCS 고객 | 감축·규제준수·저장확실성 | tCO2 | PS-ENS-CCS | PRC-ENS-D06-45 |

---
