---
id: skes-d06-3-canonical-end-to-end-operating-architect
title: Canonical End-to-End Operating Architecture
summary: "SK이노베이션의 에너지·공익 사업을 운영하기 위한 전체 아키텍처로, 9개 사업 체인의 처리 흐름·핵심 데이터·계획 루프를 설명합니다"
tags: [d06, process, schema, table]
keywords: [운영 아키텍처, 가치 체인, LNG, 급전계획, 도시가스, 에너지저장장치, 액화수소, CCS, 계획 루프, 운영 프로세스]
related: [CHAIN-ENS-LNG-01, CHAIN-ENS-PWR-01, CHAIN-ENS-CHP-01, CHAIN-ENS-CG-01, CHAIN-ENS-REN-01, CHAIN-ENS-ESS-01, CHAIN-ENS-EVC-01, CHAIN-ENS-H2-01, CHAIN-ENS-CCS-01]
priority: normal
domain: D06
section: 3
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1168
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 3. Canonical End-to-End Operating Architecture

## 3.1 Value-Chain Process Map

| Chain ID | 운영 흐름 | 상태 | 핵심 수익/서비스 | 가장 중요한 D06 데이터 |
|---|---|---|---|---|
| `CHAIN-ENS-LNG-01` | 가스전 → 전처리 → 액화 → 저장 → 선적 → 운송 → 터미널 → 기화·송출 | 운영+개발 | LNG 확보·사용·판매 | nomination, cargo, inventory, BOG, sendout |
| `CHAIN-ENS-PWR-01` | 전력수요/가격 → 급전계획 → 가스지명 → 기동 → GT/HRSG/ST → 계통송전 | 운영 | 전력판매 | dispatch, heat rate, starts, availability, emissions |
| `CHAIN-ENS-CHP-01` | 열수요 → 발전/보일러 최적화 → 열수송 → 고객공급 → 정산 | 운영 | 전력+열판매 | heat demand, supply/return temp, losses, availability |
| `CHAIN-ENS-CG-01` | 도매가스 인수 → 정압/부취 → 배관 → 지구정압 → 계량 → 청구/안전 | 운영 | 도시가스 판매 | pressure, flow, odorant, leak, meter, customer event |
| `CHAIN-ENS-REN-01` | 자원예측 → 발전 → 변환 → 계통연계 → 계량 → PPA/REC 정산 | 운영+개발 | 전력·REC·PPA | forecast, SCADA, availability, curtailment, settlement |
| `CHAIN-ENS-ESS-01` | 가격·계통상태 → 입찰 → SOC 계획 → 충방전 → 성과정산 → 열화관리 | 운영 | 에너지·보조서비스·피크절감 | bid, award, telemetry, SOC/SOH, degradation, revenue |
| `CHAIN-ENS-EVC-01` | 건물용량 → 충전요청 → 부하배분 → 세션 → 과금 → 유지보수 | 운영 | 충전서비스 | site limit, session, charger status, queue, payment |
| `CHAIN-ENS-H2-01` | 부생수소 → 정제 → 액화 → 저장 → 로딩 → 탱크로리 → 충전소 | 운영 | 액화수소 공급 | purity, energy, BOR, transfer loss, delivery, availability |
| `CHAIN-ENS-CCS-01` | CO₂ 발생 → 포집 → 재생 → 탈수/압축 → 수송 → 주입 → MRV | 계획·실증 | 저탄소 LNG·감축가치 | mass balance, purity, energy penalty, injection, monitoring |

## 3.2 Cross-Chain Planning Loops

```yaml
planning_loops:
  yearly:
    - LNG entitlement and contract portfolio
    - plant outage and major maintenance
    - renewable generation and PPA delivery plan
    - city_gas demand and network investment
  monthly:
    - cargo and tank inventory plan
    - power fuel requirement and maintenance window
    - ESS market strategy and warranty budget
  day_ahead:
    - power dispatch and gas nomination
    - renewable forecast and PPA schedule
    - ESS bids and charge discharge plan
    - CHP heat demand plan
  intraday:
    - cargo terminal sendout balancing
    - unit loading and reserve response
    - renewable forecast update and curtailment
    - ESS re_dispatch and EV load allocation
  real_time:
    - process control alarm trip and safety interlock
    - gas pressure and leak response
    - battery thermal and electrical protection
    - hydrogen gas and cryogenic safety
```

## 3.3 Material·Energy·Information Genealogy

```yaml
genealogy_keys:
  LNG:
    physical: [gas_source, entitlement, liquefaction_batch, cargo, tank_inventory, sendout_stream, fuel_consumer]
    commercial: [contract, nomination, title_transfer, terminal_slot, imbalance, settlement]
  power:
    physical: [fuel_stream, unit, start_event, operating_hour, MWh, emission_record]
    commercial: [bid, dispatch_instruction, meter, settlement, REC_or_credit]
  city_gas:
    physical: [gate_station, pressure_zone, pipe_segment, regulator, service_line, meter]
    commercial: [customer_contract, tariff, reading, bill, payment, service_event]
  renewable:
    physical: [resource, turbine_or_inverter, meter_interval, MWh]
    commercial: [forecast, schedule, PPA_allocation, REC, settlement]
  hydrogen:
    physical: [source_lot, purification_lot, liquefaction_run, storage_batch, tanker_load, station_delivery]
    commercial: [order, delivery_slot, acceptance, quantity_quality_certificate, settlement]
```

---
