---
id: skes-d08-19-internal-data-request-pack
title: Internal Data Request Pack
summary: "LNG, 발전, 수소 등 E&S 사업의 데이터 활용 목적별로 필요한 내부 데이터의 최소 보유 기간과 민감도를 정의하는 28개 항목 매트릭스."
tags: [d08, supply-chain, table]
keywords: [LNG 계약, 공급망 데이터, 터미널 최적화, 발전 디스패치, 자산관리, EAM, 창고 재고, 수소, EVSE, 민감도 등급]
related: [REQ-ENS-D08-001, REQ-ENS-D08-002, REQ-ENS-D08-003, REQ-ENS-D08-004, REQ-ENS-D08-005, REQ-ENS-D08-006, REQ-ENS-D08-007, REQ-ENS-D08-008, REQ-ENS-D08-009, REQ-ENS-D08-010, REQ-ENS-D08-011, REQ-ENS-D08-012, REQ-ENS-D08-013, REQ-ENS-D08-014, REQ-ENS-D08-015, REQ-ENS-D08-016, REQ-ENS-D08-017, REQ-ENS-D08-018, REQ-ENS-D08-019, REQ-ENS-D08-020, REQ-ENS-D08-021, REQ-ENS-D08-022, REQ-ENS-D08-023, REQ-ENS-D08-024]
priority: normal
domain: D08
section: 19
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 991
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 19. Internal Data Request Pack

| Request ID | 요청 데이터 | 최소 기간/범위 | 연결 목적 | 민감도 |
|---|---|---|---|---|
| `REQ-ENS-D08-001` | LNG contract master·amendment metadata | active+5년 | right ledger | restricted |
| `REQ-ENS-D08-002` | entitlement/ADP/cargo schedule | 3년 | optimizer | restricted |
| `REQ-ENS-D08-003` | LNG trade blotter·confirmation | 3년 | spot/copilot | highly restricted |
| `REQ-ENS-D08-004` | cargo CoA·quantity documents | 3년 | quality/reconciliation | confidential |
| `REQ-ENS-D08-005` | vessel AIS/noon/fuel/BOG | 2년 | ETA/speed | confidential |
| `REQ-ENS-D08-006` | terminal slot·tank·sendout·BOG | 2년 5~15min | terminal optimization | critical OT |
| `REQ-ENS-D08-007` | power dispatch·heat rate·fuel | 2년 hourly | fuel-dispatch | critical OT |
| `REQ-ENS-D08-008` | LNG invoice/tolling/terminal/freight cost | 3년 | landed cost | highly restricted |
| `REQ-ENS-D08-009` | supplier master·hierarchy | current+history | entity resolution | confidential |
| `REQ-ENS-D08-010` | material/service master·BOM | current | traceability | confidential |
| `REQ-ENS-D08-011` | PR/RFx/bid/PO/GR/invoice | 3년 | S2P analytics | restricted |
| `REQ-ENS-D08-012` | supplier OTIF/NCR/CAPA | 3년 | score/risk | confidential |
| `REQ-ENS-D08-013` | EAM asset/BOM/work order | 5년 | spare optimizer | critical OT |
| `REQ-ENS-D08-014` | warehouse stock/movement/reservation | 3년 daily | inventory | confidential |
| `REQ-ENS-D08-015` | repair/warranty claim | 5년 | recovery | confidential |
| `REQ-ENS-D08-016` | city-gas material lot·GIS·joint | asset life | safety genealogy | critical |
| `REQ-ENS-D08-017` | regional city-gas stock/demand | 3년 | multi-echelon | confidential |
| `REQ-ENS-D08-018` | contractor safety/quality events | 3년 | contractor score | personal data controlled |
| `REQ-ENS-D08-019` | renewable package milestone/ETA | project life | schedule twin | confidential |
| `REQ-ENS-D08-020` | renewable as-built/SCADA handover | asset life | handover QA | critical OT |
| `REQ-ENS-D08-021` | KCE cell/rack/container genealogy | asset life | recall | OEM restricted |
| `REQ-ENS-D08-022` | KCE warranty/LTSA/dispatch | asset life | warranty-aware dispatch | restricted |
| `REQ-ENS-D08-023` | EVSE BOM/AVL/SBOM/EOL | current+history | component risk | confidential |
| `REQ-ENS-D08-024` | EVSE installer/test/ticket | 3년 | first-time-fix | customer data controlled |
| `REQ-ENS-D08-025` | H₂ feed/production/storage/loading | 1년 minute/hourly | LH₂ optimizer | critical OT |
| `REQ-ENS-D08-026` | trailer route/station inventory | 1년 | logistics | safety/location controlled |
| `REQ-ENS-D08-027` | supplier ESG assessment/CAP | 3 cycles | ESG copilot | confidential |
| `REQ-ENS-D08-028` | contract data-right/cyber clauses | active | PoC gate | highly restricted |

## 19.1 Safe Sandbox Rule

1. 계약가격·거래상대·신용한도는 원문 대신 tokenized ID와 필요한 파생변수만 사용한다.
2. OT historian은 read-only replica에서 추출하고 제어망에 모델이 직접 명령하지 않는다.
3. 개인·위치·운행 데이터는 목적 최소화·보존기간·접근권을 적용한다.
4. 공급사 평가 모델은 자동배제·계약해지 결정을 하지 않는다.
5. PoC 결과는 holdout period·planner override·시장가격 효과를 포함해 측정한다.

---
