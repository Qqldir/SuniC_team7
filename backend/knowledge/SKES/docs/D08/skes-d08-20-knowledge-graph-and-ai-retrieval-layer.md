---
id: skes-d08-20-knowledge-graph-and-ai-retrieval-layer
title: Knowledge Graph and AI Retrieval Layer
summary: "에너지 공급망 knowledge graph 데이터 모델로, 생산권·자산·프로세스 노드와 관계 엣지를 정의하고 LNG·BESS·수소 체인 최적화 쿼리를 제시한다."
tags: [d08, supply-chain, table]
keywords: [LNG, BESS, tolling, TUA, 터미널, 위험 통제, genealogy, 공급처, ESG]
related: [CHUNK-ENS-D08-0001, CHUNK-ENS-D08-0002, CHUNK-ENS-D08-0003, CHUNK-ENS-D08-0004, CHUNK-ENS-D08-0005, CHUNK-ENS-D08-0006, CHUNK-ENS-D08-0007, CHUNK-ENS-D08-0008, CHUNK-ENS-D08-0009, CHUNK-ENS-D08-0010, CHUNK-ENS-D08-0011, CHUNK-ENS-D08-0012, CHUNK-ENS-D08-0013, CHUNK-ENS-D08-0014]
priority: normal
domain: D08
section: 20
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 2266
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 20. Knowledge Graph and AI Retrieval Layer

## 20.1 Node Types

| Node | Key | 예시 |
|---|---|---|
| organization | `supplier_id` | Freeport LNG, Santos, Sungrow |
| contract/right | `contract_id` | Freeport tolling, Boryeong TUA |
| material/service | `material_id` | LNG cargo, BESS package |
| flow | `flow_id` | Freeport→Boryeong |
| asset | `asset_id` | terminal, vessel, KCE site |
| process | `process_id` | cargo scheduling, ESS operation |
| shipment/cargo | `shipment_id` | voyage/cargo |
| batch/serial | `genealogy_id` | pipe lot, cell rack |
| supplier event | `event_id` | outage, defect, ESG finding |
| risk | `risk_id` | outage, recall, insolvency |
| seed | `seed_id` | optimizer/control tower |

## 20.2 Edge Types

| Edge | From→To | 의미 |
|---|---|---|
| `SUPPLIES` | supplier→material | 승인 공급관계 |
| `GOVERNS` | contract→flow | 물량 이동의 계약근거 |
| `PRODUCED_AT` | material→asset | 생산원 |
| `LIQUEFIED_AT` | gas→train | 액화 |
| `TRANSPORTED_BY` | cargo→vessel | 운송 |
| `RECEIVED_AT` | cargo→terminal | 수입 |
| `CONSUMED_BY` | material→asset/process | 사용 |
| `INSTALLED_IN` | serial→asset | 설치 genealogy |
| `WARRANTED_BY` | asset→supplier/contract | 보증 |
| `AFFECTED_BY` | asset→risk | 위험노출 |
| `MITIGATED_BY` | risk→control/seed | 통제·O/I |
| `EVIDENCED_BY` | fact/event→source | 근거 |

## 20.3 Example Triples

```text
(SK Innovation E&S)-[HOLDS_RIGHT:2200000_tpa]->(Freeport Train 3 Tolling)
(Freeport Train 3 Tolling)-[TYPE]->(TOLLING_USE_OR_PAY)
(Woodford Gas)-[MAY_FEED]->(Freeport LNG)
(Barossa Gas)-[TRANSPORTED_VIA]->(Barossa GEP)
(Barossa GEP)-[FEEDS]->(Darwin LNG)
(Barossa LNG Cargo)-[RECEIVED_AT]->(Boryeong LNG Terminal)
(SK Innovation E&S)-[HOLDS_TUA:3500000_tpa]->(Boryeong LNG Terminal)
(KCE NY6)-[USES_BESS]->(Sungrow)
(KCE NY6)-[EPC_BY]->(Black & McDonald)
(Pipe Lot)-[INSTALLED_IN]->(City Gas GIS Segment)
(LH2 Trailer)-[DELIVERS_TO]->(Hydrogen Station)
(Supply Risk)-[MITIGATED_BY]->(OI Seed)
```

## 20.4 Retrieval Queries

1. 지분 생산권과 장기구매·tolling·TUA가 함께 필요한 LNG 경로는 무엇인가.
2. Freeport outage가 어느 선박·terminal·발전소에 영향을 주는가.
3. 30일 이내 inventory cover 하한을 위협하는 cargo 지연은 무엇인가.
4. 동일 OEM/part를 쓰는 발전소 중 공동재고 가능한 설비는 무엇인가.
5. 특정 PE pipe lot가 설치된 GIS 구간과 관련 고장·시공사를 찾아라.
6. Sungrow BESS가 설치된 KCE 프로젝트와 warranty·firmware 상태를 찾아라.
7. 계약 data-right가 없어 PoC를 시작할 수 없는 Seed를 찾아라.
8. 2차 ESG 진단 기한이 지났지만 CAP가 미종결된 P0 supplier를 찾아라.
9. LH₂ station stockout을 막기 위해 어느 trailer route를 바꿔야 하는가.
10. 시장가격 효과를 제거한 뒤 실제 절감액이 양수인 O/I 과제를 찾아라.

## 20.5 AI Retrieval Chunks

### `CHUNK-ENS-D08-0001` — LNG Rights Are Not Physical Ownership

Freeport 220만 톤/년은 20년 use-or-pay 액화 사용권이고, Boryeong 350만 톤/년은 터미널 사용권이다. 두 수치는 E&S가 해당 물리자산을 소유하거나 그만큼 실제 생산·수입했다는 뜻이 아니다. 최적화와 capacity 집계는 right type을 먼저 구분해야 한다.

### `CHUNK-ENS-D08-0002` — Woodford–Freeport Gap

Woodford 공동개발 생산 설명값 약 110만 톤/년은 Freeport 사용권 220만 톤/년보다 작다. 공개자료만으로 feed-gas 전체 조달구조를 확정할 수 없으므로 pipeline·spot·portfolio 구매내역을 내부 확인해야 한다.

### `CHUNK-ENS-D08-0003` — Barossa 2026 Operating State

Barossa는 2026년 첫 LNG cargo와 한국 도입이 확인된 운영경로다. Barossa 지분, Darwin 지분, 약 130만 톤 도입 설명물량은 중복되지 않는 별도 권리 레코드로 저장한다.

### `CHUNK-ENS-D08-0004` — Cargo Control Tower

수요예측·계약 entitlement·액화 outage·vessel ETA·terminal slot·tank ullage·sendout·발전 dispatch를 하나의 시간축에서 연결해야 한다. 추천은 계약기밀을 보호하고 planner override와 audit trail을 남겨야 한다.

### `CHUNK-ENS-D08-0005` — MRO Genealogy

발전·LNG 설비의 critical spare는 asset serial–BOM–failure mode–PO–warehouse–work order–installed serial–repair/warranty를 연결해야 한다. 단순 재고최적화는 호환성·안전·revision을 놓칠 수 있다.

### `CHUNK-ENS-D08-0006` — City-Gas Safety Genealogy

PE/steel pipe의 lot·heat, fusion/weld joint, valve/regulator/meter serial을 GIS 구간과 연결하면 불량 lot recall, 반복고장 분석, 긴급자재 배치를 고도화할 수 있다. 공개자료로 공급사명은 확정하지 않는다.

### `CHUNK-ENS-D08-0007` — Offshore-Wind Handover

Jeonnam OWF1은 상업운전이 확인되지만 package vendor 상세는 제한적이다. 향후 OWF2/3는 FAT–shipment–installation–commissioning–as-built–SCADA point list를 serial 기반으로 인계하는 digital handover를 설계해야 한다.

### `CHUNK-ENS-D08-0008` — KCE Supplier Boundary

Powin·Sungrow·Mitsubishi Power·Black & McDonald·SunGrid 관계는 공개된 프로젝트·역할에만 연결한다. 특정 프로젝트 관계를 전체 KCE 포트폴리오 표준으로 일반화하거나 cell origin을 추정하지 않는다.

### `CHUNK-ENS-D08-0009` — Warranty-Aware Dispatch

ESS의 수익 최적화는 market revenue만이 아니라 throughput·temperature·capacity-retention warranty와 열화비용을 함께 고려해야 한다. OEM data-right와 안전 operating envelope가 선행 Gate다.

### `CHUNK-ENS-D08-0010` — EverCharge Multi-Tier Risk

EverCharge는 수직통합 EVSE 제조·software·설치 역량과 Hayward 생산거점을 보유하지만 tier-2 부품 공급사는 공개되지 않았다. BOM·AVL·SBOM·EOL·lot failure를 연결하는 내부 supply graph가 필요하다.

### `CHUNK-ENS-D08-0011` — Liquid-Hydrogen Constraint Chain

3만 톤/년은 명목능력이다. 실제 공급은 부생수소 feed, train availability, storage/boil-off, trailer, station inventory의 최소능력에 의해 결정된다. feed→produced→loaded→delivered→dispensed 질량수지를 분리한다.

### `CHUNK-ENS-D08-0012` — Supplier ESG Process

E&S의 공개 ESG 실사는 약 100개 대상 pool, 2022년 26개 실사, 21개 핵심항목·33개 세부요소·A/B/C 등급, 약 4~6개월 후 2차 진단 구조다. 이 수치를 전체 공급사 수나 현재 실사완료 수로 일반화하지 않는다.

### `CHUNK-ENS-D08-0013` — Data Rights as Procurement Requirement

JV·OEM·EPC 계약에서 telemetry·raw data·remote access·model output·audit·AI 학습 권리를 사전에 확보하지 않으면 O/I PoC가 차단될 수 있다. data-right는 기술규격과 동일한 조달필드다.

### `CHUNK-ENS-D08-0014` — Benefit Measurement

공급망 O/I의 절감액은 시장가격·환율·수요·자산상태 변화와 알고리즘 효과를 분리해야 한다. holdout/replay, 승인 전 baseline, planner override, audit trail이 없으면 성과를 확정하지 않는다.

---
