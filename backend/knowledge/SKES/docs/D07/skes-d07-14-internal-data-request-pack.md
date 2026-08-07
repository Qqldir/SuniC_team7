---
id: skes-d07-14-internal-data-request-pack
title: Internal Data Request Pack
summary: "LNG터미널, 발전소, 신재생에너지 등 사업별로 어떤 데이터를 얼마나 수집할지와 품질 기준을 정의한 데이터 요청 명세"
tags: [d07, footprint, table]
keywords: [데이터 요청, 자산 마스터, LNG, 터미널, 발전소, SCADA, EAM, 데이터 품질, 시계열, 신재생에너지]
related: []
priority: normal
domain: D07
section: 14
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 832
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 14. Internal Data Request Pack

| Request ID | Scope | Requested tables/files | Minimum period | Key joins | Purpose |
|---|---|---|---|---|---|
| DR-ENS-D07-0001 | enterprise | legal entity/JV/SPV master | current + history | entity_id | ownership |
| DR-ENS-D07-0002 | enterprise | asset/site/equipment hierarchy | current + history | asset_id | canonical master |
| DR-ENS-D07-0003 | enterprise | capacity ledger definitions | current | capacity_id | anti-double-count |
| DR-ENS-D07-0004 | enterprise | contract/right metadata | contract life | right_id | access/volume |
| DR-ENS-D07-0005 | Barossa/Darwin | production/train/cargo daily | 24 months | cargo_id | supply forecast |
| DR-ENS-D07-0006 | fleet | voyage/AIS/BOG/cargo | 24 months | vessel_id/voyage_id | shipping |
| DR-ENS-D07-0007 | Boryeong | tank/BOG/sendout 1–5 min | 12 months | tag/asset | terminal |
| DR-ENS-D07-0008 | power | historian/unit events | 24 months | unit/time | heat rate/start |
| DR-ENS-D07-0009 | power | EAM/work orders/outages | 5 years | equipment_id | reliability |
| DR-ENS-D07-0010 | CHP | heat load/weather/price | 24 months | time/site | co-optimize |
| DR-ENS-D07-0011 | city gas | GIS pipe/regulator/meter | current + history | segment_id | asset graph |
| DR-ENS-D07-0012 | city gas | leak/inspection/work | 5 years | segment_id | integrity |
| DR-ENS-D07-0013 | city gas | receipt/meter/billing | 24 months | meter/customer | UFG |
| DR-ENS-D07-0014 | OWF1 | SCADA/CMS/metocean | 12+ months | turbine/time | forecast/O&M |
| DR-ENS-D07-0015 | renewable | project/COD/gate register | current + history | project_id | status |
| DR-ENS-D07-0016 | KCE | site/block/BMS/EMS | 12+ months | site/block/time | health |
| DR-ENS-D07-0017 | KCE | bid/award/dispatch/price | 24 months | interval/site | optimization |
| DR-ENS-D07-0018 | EverCharge | site electrical/session/fault | 12 months | site/port/time | load/uptime |
| DR-ENS-D07-0019 | Incheon LH2 | process historian/lab/EAM | 12 months | train/time | SEC/reliability |
| DR-ENS-D07-0020 | LH2 network | plant/tanker/station inventory | 12 months | batch/location | logistics |
| DR-ENS-D07-0021 | Quynh Lap | FEED/EPC tag/document specs | project life | document/tag | digital handover |
| DR-ENS-D07-0022 | all | data access/security matrix | current | system/role | PoC gate |

## 14.1 Data-Quality Acceptance

| Test | Acceptance criterion |
|---|---|
| asset uniqueness | one physical asset has one canonical asset_id |
| temporal validity | every ownership/status record has effective dates |
| unit normalization | original unit preserved and normalized unit documented |
| scope | gross/equity/contract/actual explicitly tagged |
| hierarchy | every project-level asset points to a parent portfolio where applicable |
| right separation | physical asset and commercial right use different records |
| status evidence | operating status requires COD/current operation evidence |
| data access | right-to-use captured before PoC |

---
