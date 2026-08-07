---
id: skes-d08-6-lng-marine-logistics-terminal-and-invent
title: "LNG Marine Logistics, Terminal and Inventory"
summary: "LNG 선박 운영·터미널 관리를 위한 항해 이벤트, 의사결정 변수, 재고 원장, 제어 경보의 데이터 구조와 통제식을 정의한다."
tags: [d08, supply-chain, table]
keywords: [Voyage Event, vessel assignment, slow steam, BOG, Terminal Inventory, Control-Tower Alert, berth slot, ullage, 화물 계약, demurrage]
related: [ALT-LNG-001, ALT-LNG-002, ALT-LNG-003, ALT-LNG-004, ALT-LNG-005, ALT-LNG-006, ALT-LNG-007, ALT-LNG-008, ALT-LNG-009, ALT-LNG-010]
priority: normal
domain: D08
section: 6
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1050
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 6. LNG Marine Logistics, Terminal and Inventory

## 6.1 Vessel Master — Public Layer

| Vessel/Group | 공개 사양 | 역할 | 데이터 gap |
|---|---|---|---|
| Prism Agility | 299m×48m, 180,000㎥, 약 75,000t, 19.5kn, GTT Mark III Flex, BOR 0.085%/day | Freeport 등 LNG 운송 | IMO·선주·charter expiry·docking |
| Prism Brilliance | 1호선과 함께 공개된 동형선 | Freeport 등 LNG 운송 | IMO·선주·charter expiry·docking |
| LNG Carrier No.3 | 2021년 인수 완료 | portfolio 운송 | 실명·사양·route·계약 |
| LNG Carrier No.4 | 2022년 인수 완료 | portfolio 운송 | 실명·사양·route·계약 |

## 6.2 Voyage Event Model

| Event | 필수 timestamp | 필수 수량/상태 | 예외코드 |
|---|---|---|---|
| cargo nomination | nomination/acceptance | quantity·quality·window | late_nomination |
| berth slot | requested/confirmed | terminal·berth·window | slot_conflict |
| loading start/end | NOR/all-fast/complete | loaded volume·heel | terminal_delay |
| departure | pilot-off | draft·fuel·cargo | weather_hold |
| canal/waypoint | ETA/ATA | speed·weather·route | congestion |
| arrival/NOR | ETA/NOR/all-fast | remaining cargo·BOR | berth_wait |
| unloading | start/end | discharged quantity | unloading_rate |
| reconciliation | bill/terminal/meter | loss·difference | quantity_claim |

## 6.3 Marine Decision Variables

| 변수 | 데이터 | 결정 | KPI |
|---|---|---|---|
| vessel assignment | capacity·position·availability | cargo-vessel match | laden utilization |
| speed | ETA·fuel curve·weather·slot | slow steam/speed-up | fuel/t, on-time arrival |
| route | canal·weather·security | route selection | voyage cost·risk |
| heel/BOG | cargo temp·BOR·engine demand | heel target·reliquefaction/consumption | cargo loss |
| berth synchronization | terminal slot·tank ullage | ETA adjustment | demurrage/queue |
| drydock | class window·fleet demand | maintenance timing | lost days |

## 6.4 Terminal and Inventory Ledger

| Ledger | 최소 필드 | 통제식 |
|---|---|---|
| tank inventory | tank·level·density·temperature·composition | opening+receipt-sendout-BOG=closing |
| contractual inventory | owner/right·cargo·allocation | physical stock와 분리 |
| available inventory | physical-reserve-unavailable | dispatch 가능량 |
| ullage | safe max-current forecast | cargo 수용가능성 |
| sendout | meter·quality·destination | terminal vs pipeline reconciliation |
| BOG | generation·compressor·fuel/recondense/flare | BOG mass balance |
| terminal capacity | gross·TUA·scheduled·available | 소유/권리/실적 분리 |

## 6.5 LNG Control-Tower Alerts

| Alert ID | 조건 | 영향 | 자동 제안 |
|---|---|---|---|
| `ALT-LNG-001` | cargo ETA와 berth slot 충돌 | demurrage·재고 | speed/slot swap |
| `ALT-LNG-002` | forecast ullage < arriving cargo | 하역불가 | sendout·cargo swap |
| `ALT-LNG-003` | inventory cover 하한 접근 | 발전중단 위험 | spot/nomination 조정 |
| `ALT-LNG-004` | Freeport outage notice | use-or-pay·공급부족 | 대체 cargo·dispatch |
| `ALT-LNG-005` | Barossa production shortfall | entitlement 부족 | JV reconciliation |
| `ALT-LNG-006` | BOR/heel 예상 초과 | cargo loss | speed·engine mode |
| `ALT-LNG-007` | quality off-spec 가능성 | 발전효율·수령분쟁 | blending·lab priority |
| `ALT-LNG-008` | vessel drydock 중첩 | 운송capacity 부족 | charter-in 검토 |
| `ALT-LNG-009` | 환율/JKM/HH 급변 | cargo economics | hedge/dispatch review |
| `ALT-LNG-010` | pipeline/sendout constraint | tank high-high | 발전·도시가스 조정 |

---
