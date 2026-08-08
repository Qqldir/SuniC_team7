---
id: skes-d09-11-evercharge-customer-and-site-relationshi
title: EverCharge Customer and Site Relationship DB
summary: "충전소 유형별 구축 사례와 고객 여정(9단계), 성공 지표(10개)를 정의하는 EV 충전 비즈니스 프레임워크"
tags: [d09, customer, table]
keywords: [EV 충전, 고객 사례, 고객 여정, 부하 관리, SmartPower, DCFC, 포트 활성화, 운영 지표]
related: [EC-ENS-D09-001, EC-ENS-D09-002, EC-ENS-D09-003, EC-ENS-D09-004, EC-ENS-D09-005, EC-ENS-D09-006, EC-ENS-D09-007, EC-ENS-D09-008]
priority: normal
domain: D09
section: 11
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 740
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 11. EverCharge Customer and Site Relationship DB

## 11.1 Site Archetypes

| Archetype | Buyer | User | Core value | Primary SLA |
|---|---|---|---|---|
| condominium | HOA/property manager | residents | electrical upgrade avoidance | charger availability |
| apartment | owner/operator | tenants | amenity·retention | onboarding·billing |
| workplace | employer/facility | employees/visitors | benefit·decarbonization | access·uptime |
| stadium | venue operator | staff/fans/fleet | phased scale | event readiness |
| rental fleet | fleet operator | operations drivers | turnaround·vehicle readiness | departure SOC |
| corporate campus | facilities/ESG | employees/fleet | large-scale load sharing | peak demand |

## 11.2 Customer Case Ledger

| Case ID | Site | Public scale | Customer need | Quantified/public result | Data needed |
|---|---|---:|---|---|---|
| `EC-ENS-D09-001` | Avis IAH | L2+DCFC | rental fleet charging | powers Avis/Budget EV/PHEV fleet | flight/fleet turns·SOC |
| `EC-ENS-D09-002` | 340 On The Park | undisclosed | premium residential amenity | SmartPower adopted | session·capacity |
| `EC-ENS-D09-003` | Metropolis Tower 2 | 16 chargers | avoid upgrade | approx. $100k avoided | panel·load·utilization |
| `EC-ENS-D09-004` | AFC HQ | 13 L2 | employee charging | real-time visibility | access·wait time |
| `EC-ENS-D09-005` | Corporate Campus | 173 EVSE | expand from 45 | existing capacity leveraged | garage allocation |
| `EC-ENS-D09-006` | The Legacy | 80+67 ready | every owner pathway | expansion within 1,700A context | owner request queue |
| `EC-ENS-D09-007` | Las Flores | 55-car context | constrained service | required load described as 25% of usual | simultaneous demand |
| `EC-ENS-D09-008` | Sharon Park | 64; 100% EV-ready | scale from 6 | phased expansion | adoption curve |

## 11.3 Lead-to-Renewal Journey

1. Site lead and electrical one-line collection.
2. Parking/driver/fleet demand survey.
3. Load study and SmartPower design.
4. HOA·owner·utility·permit approval.
5. hardware/EPC quotation and contract.
6. installation·commissioning·user enrollment.
7. session authorization·dynamic allocation·billing.
8. maintenance·support·firmware·payment reconciliation.
9. expansion trigger and renewal.

## 11.4 Customer Success Metrics

- Port activation rate.
- Unique active drivers per month.
- Session success and first-plug success.
- Departure-SOC attainment for fleets.
- Peak-kW avoided and infrastructure CAPEX avoided.
- Charger uptime and mean time to restore.
- Support contacts per 1,000 sessions.
- Payment exception rate.
- Installed-to-EV-ready conversion.
- Customer expansion and renewal rate.

---
