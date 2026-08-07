---
id: skes-d07-7-capacity-ledger-and-reconciliation
title: Capacity Ledger and Reconciliation
summary: "LNG, 발전, 재생에너지 등 E&S 자산의 용량을 ID별로 정리하고 중복 계산을 방지하는 통합 자산 용량 대장"
tags: [d07, footprint, table]
keywords: [LNG, 발전소, 재생에너지, 수소, 에너지자산, 터미널, BESS, TUA, 용량관리, 중복계산]
related: []
priority: normal
domain: D07
section: 7
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 972
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 7. Capacity Ledger and Reconciliation

## 7.1 LNG Capacity Ledger

| CAP ID | Asset | Value | Type | Status | Inclusion rule |
|---|---|---:|---|---|---|
| CAP-ENS-D07-0001 | Barossa E&S offtake | 1.3Mt/y | contracted/equity-linked offtake | operating 2026 | not field gross |
| CAP-ENS-D07-0002 | Woodford description | 1.1Mt/y equivalent | production description | operating | not LNG plant capacity |
| CAP-ENS-D07-0003 | Tangguh import | 0.5~0.6Mt/y | contracted import | active | not equity capacity |
| CAP-ENS-D07-0004 | Freeport | 2.2Mt/y | contracted liquefaction right | active | not actual output |
| CAP-ENS-D07-0005 | Boryeong gross | 7Mt/y | terminal nameplate gross | operating | physical asset |
| CAP-ENS-D07-0006 | Boryeong E&S right | 3.5Mt/y | TUA | active | subset commercial right |
| CAP-ENS-D07-0007 | Boryeong storage | 1.4m kl | gross static tank volume | operating | 7×200,000kl |
| CAP-ENS-D07-0008 | Boryeong sendout | 1,400t/h | gross regas sendout | operating | unit configuration gap |

## 7.2 Power and Heat Ledger

| CAP ID | Asset | Electric | Thermal | Type | Boundary |
|---|---|---:|---:|---|---|
| CAP-ENS-D07-0010 | Gwangyang | 1,126MW | n/a | nameplate/public | operating |
| CAP-ENS-D07-0011 | Paju | 1,800MW | n/a | nameplate/public | operating |
| CAP-ENS-D07-0012 | Yeoju | 1,000MW | n/a | nameplate/public | operating |
| CAP-ENS-D07-0013 | Hanam | 399MW | 263Gcal/h | dual product | operating |
| CAP-ENS-D07-0014 | Wirye | 450MW | 238Gcal/h | dual product | operating |
| CAP-ENS-D07-0015 | Kimcheon | 59MW | 480t/h | O&M-managed | ownership excluded |
| CAP-ENS-D07-0016 | Jeonbuk | 21MW | 215t/h | O&M-managed | ownership excluded |
| CAP-ENS-D07-0017 | Quynh Lap | 1,500MW | n/a | development | excluded from operating |

## 7.3 Renewable, BESS and Hydrogen Ledger

| CAP ID | Asset | Value | Type | Status |
|---|---|---:|---|---|
| CAP-ENS-D07-0020 | Jeonnam OWF1 | 96MW | gross operating | operating |
| CAP-ENS-D07-0021 | Jeonnam OWF1 equity reference | 48.96MW | calculated at 51% | analytical only |
| CAP-ENS-D07-0022 | Jeonnam OWF2 | 399MW | development | target 2031 |
| CAP-ENS-D07-0023 | Jeonnam OWF3 | 399MW | development | target 2031 |
| CAP-ENS-D07-0024 | E&S renewable portfolio | 3.5GW | operating+developing | mixed |
| CAP-ENS-D07-0025 | E&S renewable pipeline | approx. 5GW | development pipeline | planned |
| CAP-ENS-D07-0026 | KCE operating | 623MW | operating portfolio | snapshot |
| CAP-ENS-D07-0027 | KCE development | 8,000MW | pipeline | development |
| CAP-ENS-D07-0028 | KCE NY6 | 20MW | power | operating |
| CAP-ENS-D07-0029 | KCE NY6 | 45.6MWh | energy | operating |
| CAP-ENS-D07-0030 | Incheon LH2 | 30,000t/y | annual nominal | operating |
| CAP-ENS-D07-0031 | Incheon trains | 90t/day | aggregate instantaneous | operating |
| CAP-ENS-D07-0032 | Incheon storage | 120t | static gross | operating |

## 7.4 Anti-Double-Count Checks

| Check | Failure example | Control |
|---|---|---|
| portfolio vs project | 623MW + NY6 20MW | inclusion_parent marks NY6 inside 623MW |
| physical vs right | Boryeong 7Mt + 3.5Mt | capacity_type prevents sum |
| operating vs pipeline | renewable 3.5GW + 5GW | lifecycle filters |
| gross vs equity | OWF1 96 + 48.96MW | equity value is reference only |
| electric vs heat | Hanam 399MW + 263Gcal/h | separate measure dimensions |
| charger vs ready circuit | Legacy 80 + 67 | readiness flag separate |
| daily vs annual | LH2 90t/day × 365 | no inferred annual overwrite |

---
