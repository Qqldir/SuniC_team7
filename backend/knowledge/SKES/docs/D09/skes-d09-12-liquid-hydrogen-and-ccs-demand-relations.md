---
id: skes-d09-12-liquid-hydrogen-and-ccs-demand-relations
title: Liquid-Hydrogen and CCS Demand Relationships
summary: "액화수소와 탄소포집의 수요를 예측하기 위해 정책공약부터 실판매까지 8단계로 분류한 수소 수요, 고객 관계, 운영 데이터를 설명한다."
tags: [d09, customer, table]
keywords: [액화수소, 탄소포집, 수소버스, 수소충전소, offtake, 저장계약, take-or-pay, CO2 저장, 수요 단계, 고객 선정 기준]
related: []
priority: normal
domain: D09
section: 12
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 864
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 12. Liquid-Hydrogen and CCS Demand Relationships

## 12.1 Hydrogen Demand-State Ladder

| State | Evidence | Capacity planning treatment |
|---|---|---|
| policy target | government announcement | scenario only |
| MOU | multi-party cooperation | non-binding pipeline |
| station planned | site·permit under development | probability weighted |
| station commissioned | safety/operation confirmed | available outlet |
| vehicle planned | procurement target | conditional demand |
| vehicle registered | fleet record | active demand candidate |
| fuel contract | signed volume/term | contracted demand |
| dispensed kg | meter/transaction | actual demand |

## 12.2 Public Hydrogen Relationship Cards

### SK hynix Icheon

- Incheon plant-produced liquid hydrogen is supplied through the Icheon Daehung station.
- Public design statement: up to 120 buses per day; this is station capability, not confirmed daily throughput.
- Demand drivers: commute timetable, route length, bus tank state, refueling window, campus shift pattern.
- O/I question: can fleet timetable, trailer ETA and station inventory jointly reduce queue and stockout?

### KD Transport Group

- Public relationship: E&S, KD Transport and Hyundai cooperation.
- Public plan: six or more liquid-hydrogen stations at metropolitan depots.
- KD's large bus fleet creates demand potential, but MOU does not disclose firm purchase volume.
- Required gate: vehicle conversion schedule, station COD, kg/km, minimum off-take and fallback supply.

### Cheonan

- Public target: 350 hydrogen buses by 2027 with city support and E&S infrastructure role.
- City, bus operator, station operator, vehicle OEM and fuel supplier require separate IDs.
- Vehicle target must be probability-weighted by procurement completion and station availability.

## 12.3 Hydrogen Customer-Operations Data

| Data | Granularity | O/I use |
|---|---|---|
| bus schedule | vehicle/route/day | demand curve |
| vehicle tank SOC | vehicle/event | fueling priority |
| station inventory | tank/5-min | stockout warning |
| trailer ETA | load/trip | replenishment |
| dispenser flow | session/sec | throughput anomaly |
| boil-off | station/hour | loss allocation |
| price/subsidy | kg/month | margin/scenario |
| downtime | equipment/event | SLA/root cause |

## 12.4 CCS Customer Boundary

CCS는 현재 공개된 상용 고객명·확정 저장계약을 충분히 확인할 수 없는 개발영역이다. Santos·Honeywell·정부·저장권 파트너는 기술·JV·인허가 이해관계자이며 자동으로 CO2 저장 고객이 되지 않는다.

잠재 고객 DB는 다음 Gate를 통과해야 한다.

1. 배출원별 연간 CO2 양·농도·압력·불순물.
2. 포집설비 소유·운영 주체.
3. 운송거리·방식·허브접속.
4. 저장공간 entitlement와 주입 schedule.
5. MRV·장기책임·크레딧 귀속.
6. take-or-pay 또는 ship-or-pay 여부.
7. 탄소가격·보조·변경법 위험.

---
