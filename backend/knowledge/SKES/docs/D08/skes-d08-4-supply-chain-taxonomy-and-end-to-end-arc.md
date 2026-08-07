---
id: skes-d08-4-supply-chain-taxonomy-and-end-to-end-arc
title: Supply-Chain Taxonomy and End-to-End Architecture
summary: LNG부터 수소·CCS까지 SK이노베이션 E&S 각 사업 영역의 주요 물질·서비스에 대한 공급망 마스터 데이터와 품목별 규격·중요도 기준.
tags: [d08, supply-chain, core-candidate, table, "xref:d06", "xref:d07"]
keywords: [공급망군, Material Master, 핵심규격, LNG, 발전, 도시가스, 재생에너지, 에너지저장, 수소, CCS]
related: [MAT-ENS-D08-0001, MAT-ENS-D08-0002, MAT-ENS-D08-0003, MAT-ENS-D08-0004, MAT-ENS-D08-0005, MAT-ENS-D08-0006, MAT-ENS-D08-0007, MAT-ENS-D08-0008, MAT-ENS-D08-0009, MAT-ENS-D08-0010, MAT-ENS-D08-0011, MAT-ENS-D08-0012, MAT-ENS-D08-0013, MAT-ENS-D08-0014, MAT-ENS-D08-0015, MAT-ENS-D08-0016, MAT-ENS-D08-0017, MAT-ENS-D08-0018, MAT-ENS-D08-0019, MAT-ENS-D08-0020, MAT-ENS-D08-0021, MAT-ENS-D08-0022, MAT-ENS-D08-0023, MAT-ENS-D08-0024]
priority: critical
domain: D08
section: 4
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1839
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 4. Supply-Chain Taxonomy and End-to-End Architecture

## 4.1 Material and Service Master

| Material ID | 품목·서비스 | 공급망군 | 핵심 규격·증빙 | 중요도 |
|---|---|---|---|---|
| `MAT-ENS-D08-0001` | pipeline natural gas | LNG | 조성·수분·CO₂·H₂S·압력 | P0 |
| `MAT-ENS-D08-0002` | LNG cargo | LNG | 발열량·조성·밀도·온도·heel | P0 |
| `MAT-ENS-D08-0003` | liquefaction tolling | LNG | train·capacity·availability·fuel gas | P0 |
| `MAT-ENS-D08-0004` | marine transport | LNG | vessel·ETA·BOR·fuel·weather | P0 |
| `MAT-ENS-D08-0005` | terminal service | LNG | berth·tank·sendout·BOG·capacity | P0 |
| `MAT-ENS-D08-0006` | spot LNG | LNG | origin·delivery window·quality·price | P0 |
| `MAT-ENS-D08-0007` | gas-turbine hot-section parts | Power | serial·life limit·repair history | P0 |
| `MAT-ENS-D08-0008` | compressor/pump spares | LNG/Power | OEM part·criticality·lead time | P0 |
| `MAT-ENS-D08-0009` | water-treatment chemicals | Power | concentration·CoA·shelf life | P1 |
| `MAT-ENS-D08-0010` | emission-control consumables | Power | catalyst/reagent spec·activity | P1 |
| `MAT-ENS-D08-0011` | PE/steel gas pipe | City gas | heat/lot·dimension·pressure rating | P0 |
| `MAT-ENS-D08-0012` | valve/regulator | City gas | serial·set pressure·test certificate | P0 |
| `MAT-ENS-D08-0013` | gas meter/corrector | City gas | model·calibration·firmware | P0 |
| `MAT-ENS-D08-0014` | odorant | City gas | concentration·batch·SDS | P0 |
| `MAT-ENS-D08-0015` | wind turbine package | Renewable | turbine·blade·tower·SCADA | P0 |
| `MAT-ENS-D08-0016` | offshore foundation | Renewable | steel heat·weld·NDT·coating | P0 |
| `MAT-ENS-D08-0017` | subsea/export cable | Renewable | drum·joint·test·route | P0 |
| `MAT-ENS-D08-0018` | PV module | Renewable | serial·BOM·flash test·warranty | P1 |
| `MAT-ENS-D08-0019` | inverter/transformer | Renewable | serial·firmware·efficiency·warranty | P1 |
| `MAT-ENS-D08-0020` | BESS integrated system | ESS | cell/rack/PCS/EMS/BMS/fire system | P0 |
| `MAT-ENS-D08-0021` | BESS LTSA | ESS | availability·response·spares·warranty | P0 |
| `MAT-ENS-D08-0022` | EPC/BOP service | ESS/Renewable | design·procurement·construction·handover | P0 |
| `MAT-ENS-D08-0023` | EVSE hardware | EV charging | power·connector·meter·firmware | P1 |
| `MAT-ENS-D08-0024` | EVSE installation service | EV charging | panel·circuit·permit·commissioning | P1 |
| `MAT-ENS-D08-0025` | byproduct hydrogen | Hydrogen | purity·pressure·impurity·flow | P0 |
| `MAT-ENS-D08-0026` | LH₂ tank/trailer | Hydrogen | vacuum·insulation·pressure·inspection | P0 |
| `MAT-ENS-D08-0027` | cryogenic spares | Hydrogen | valve·seal·pump·sensor·lead time | P0 |
| `MAT-ENS-D08-0028` | CO₂ capture solvent | CCS | composition·degradation·make-up | P1 |
| `MAT-ENS-D08-0029` | CO₂ compression/injection service | CCS | purity·pressure·meter·custody transfer | P0 |
| `MAT-ENS-D08-0030` | MRV verification service | CCS | plan·calibration·audit·report | P0 |
| `MAT-ENS-D08-0031` | inspection/NDT | Common | scope·technician qualification·evidence | P0 |
| `MAT-ENS-D08-0032` | cybersecurity support | Common | SBOM·patch·remote access·incident SLA | P0 |
| `MAT-ENS-D08-0033` | logistics/warehouse | Common | handling·temperature·stock accuracy | P1 |
| `MAT-ENS-D08-0034` | technical consulting | Common | deliverable·IP·data right·acceptance | P2 |

## 4.2 End-to-End Supply Paths

| Flow ID | 경로 | D06 Process | D07 Asset/Right | 상태 |
|---|---|---|---|---|
| `FLOW-ENS-D08-0001` | Tangguh → LNG carrier → Gwangyang | LNG-001/006/007, PWR-001 | Gwangyang chain | operating |
| `FLOW-ENS-D08-0002` | Woodford production → U.S. gas network → Freeport | LNG-002/003/004 | Woodford/Freeport right | operating |
| `FLOW-ENS-D08-0003` | Freeport Train 3 → dedicated fleet → Boryeong | LNG-004~011 | Freeport/Boryeong TUA | operating |
| `FLOW-ENS-D08-0004` | Barossa FPSO → GEP → Darwin LNG | LNG-002~005 | Barossa/Darwin | operating 2026 |
| `FLOW-ENS-D08-0005` | Darwin LNG → carrier → Boryeong | LNG-006~011 | fleet/Boryeong TUA | operating 2026 |
| `FLOW-ENS-D08-0006` | Boryeong sendout → Paju/Yeoju/CHP | LNG-011, PWR-001 | power fleet | operating |
| `FLOW-ENS-D08-0007` | wholesale gas/city gate → 8 regions | CG-001~003 | city-gas networks | operating; supplier detail internal |
| `FLOW-ENS-D08-0008` | pipe/valve/meter vendor → regional warehouse → field | CG-004~008 | city-gas networks | operating; vendor detail internal |
| `FLOW-ENS-D08-0009` | turbine/cable/foundation supply → Jeonnam OWF1 | REN-003/004 | OWF1 | operating; vendor detail partial |
| `FLOW-ENS-D08-0010` | Sungrow integrated BESS → KCE NY6 | ESS-002/003 | KCE NY6 | disclosed |
| `FLOW-ENS-D08-0011` | Powin integrated BESS → KCE NY3 | ESS-002/003 | KCE NY3 | disclosed |
| `FLOW-ENS-D08-0012` | Powin/Mitsubishi Power → Texas portfolio | ESS-002/003 | KCE Texas | disclosed |
| `FLOW-ENS-D08-0013` | EverCharge components → Hayward → customer site | EVC-001/002 | EverCharge factory/sites | operating; component origin internal |
| `FLOW-ENS-D08-0014` | byproduct H₂ → purification → liquefaction → storage | H2-001/002 | Incheon LH₂ | operating; feed contract internal |
| `FLOW-ENS-D08-0015` | LH₂ storage → trailer → charging station | H2-003 | distribution network | operating; route volume internal |
| `FLOW-ENS-D08-0016` | solvent/equipment → capture → CO₂ transport/injection | CCS-001 | demonstration/planned assets | planned/pilot |

## 4.3 Planning Loops

| Loop | 입력 | 의사결정 | 출력 | 핵심 O/I |
|---|---|---|---|---|
| LNG S&OP | 발전수요·도시가스·계약 entitlement·재고 | cargo·tolling·선박·terminal slot | nomination·voyage·sendout | stochastic optimizer |
| Fuel-to-power | SMP·heat demand·heat rate·fuel price | 발전기동·fuel nomination | 전력·열·LNG 소비 | fuel-dispatch co-optimization |
| MRO | asset health·failure probability·lead time | repair/replace/stock | PO·work order·spare issue | risk-based inventory |
| City-gas materials | project plan·failure·regional stock | reorder·transfer·supplier allocation | pipe/valve/meter availability | multi-echelon inventory |
| Renewable construction | design·weather·vessel·delivery | installation sequence | milestone·acceptance | schedule risk twin |
| BESS procurement | market design·interconnection·technology | OEM·PCS·duration·warranty | EPC/LTSA package | bankability/warranty analytics |
| Supplier ESG | spend·criticality·country·assessment | due diligence·CAP | requalification | evidence automation |

---
