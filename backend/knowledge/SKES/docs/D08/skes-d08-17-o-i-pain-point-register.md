---
id: skes-d08-17-o-i-pain-point-register
title: O/I Pain-Point Register
summary: LNG·계약·재고·설비 운영의 데이터 단절로 인한 30개 운영문제의 근본원인과 영향을 정리한 표
tags: [d08, supply-chain, table, "xref:d17"]
keywords: [데이터 통합, supply chain risk, LNG, 계약 관리, 재고, asset management, 데이터 gap, operational efficiency, 근본원인, 우선순위]
related: [PAIN-ENS-D08-001, PAIN-ENS-D08-002, PAIN-ENS-D08-003, PAIN-ENS-D08-004, PAIN-ENS-D08-005, PAIN-ENS-D08-006, PAIN-ENS-D08-007, PAIN-ENS-D08-008, PAIN-ENS-D08-009, PAIN-ENS-D08-010, PAIN-ENS-D08-011, PAIN-ENS-D08-012, PAIN-ENS-D08-013, PAIN-ENS-D08-014, PAIN-ENS-D08-015, PAIN-ENS-D08-016, PAIN-ENS-D08-017, PAIN-ENS-D08-018, PAIN-ENS-D08-019, PAIN-ENS-D08-020, PAIN-ENS-D08-021, PAIN-ENS-D08-022, PAIN-ENS-D08-023, PAIN-ENS-D08-024]
priority: normal
domain: D08
section: 17
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1027
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 17. O/I Pain-Point Register

| Pain ID | Pain Point | 근본 데이터 gap | 영향 | D17 후보 |
|---|---|---|---|---|
| `PAIN-ENS-D08-001` | LNG 수요·cargo·재고·dispatch 분리 계획 | 통합 time series 없음 | 원가/stockout | P0 |
| `PAIN-ENS-D08-002` | 계약권리와 물리재고 혼동 | contract/asset ID 불일치 | 잘못된 가용량 | P0 |
| `PAIN-ENS-D08-003` | JV/operator outage 정보 지연 | notice 표준 없음 | 재계획 지연 | P0 |
| `PAIN-ENS-D08-004` | vessel ETA·slot·ullage 충돌 | event timestamp 불일치 | demurrage | P0 |
| `PAIN-ENS-D08-005` | cargo quality가 발전효율에 미연결 | CoA–unit mapping 없음 | heat-rate | P1 |
| `PAIN-ENS-D08-006` | landed cost 원인분해 부족 | trade/flow/cost key 단절 | 의사결정 | P0 |
| `PAIN-ENS-D08-007` | contract optionality 가치 미측정 | clause 비정형 | 기회손실 | P1 |
| `PAIN-ENS-D08-008` | supplier master 중복 | 법인명·brand 불일치 | spend 왜곡 | P0-foundation |
| `PAIN-ENS-D08-009` | critical spare가 failure risk와 분리 | BOM/EAM/PO 단절 | outage | P0 |
| `PAIN-ENS-D08-010` | repairable part 순환 추적 부족 | serial/repair loop 누락 | 재고/보증 | P1 |
| `PAIN-ENS-D08-011` | 7개 도시가스사 재고 사일로 | 공통 material code 부족 | 과잉/품절 | P0 |
| `PAIN-ENS-D08-012` | 배관 lot–GIS–고장 연결 부족 | genealogy gap | recall/safety | P0 |
| `PAIN-ENS-D08-013` | contractor 안전·품질 score 분리 | event 통합 없음 | 재작업/사고 | P0 |
| `PAIN-ENS-D08-014` | offshore wind package schedule 정적 | weather/vessel/ETA 분리 | COD 지연 | P0 |
| `PAIN-ENS-D08-015` | digital handover 문서 누락 | as-built/point list 검증 수작업 | 운영준비 | P0 |
| `PAIN-ENS-D08-016` | KCE cell–rack–project genealogy 불완전 | OEM data right | recall | P0 |
| `PAIN-ENS-D08-017` | warranty와 dispatch 충돌 | market/BMS/contract 단절 | degradation cost | P0 |
| `PAIN-ENS-D08-018` | BESS supplier early warning 부족 | 재무·recall·CVE 분산 | 가동/보증 | P0 |
| `PAIN-ENS-D08-019` | EVSE sub-tier BOM 불투명 | AVL/SBOM 미통합 | shortage/cyber | P1 |
| `PAIN-ENS-D08-020` | installer 품질 편차 미학습 | site visit data 비정형 | 재방문 | P1 |
| `PAIN-ENS-D08-021` | LH₂ 생산·trailer·station 분리계획 | 통합재고 없음 | stockout/BOG | P0 |
| `PAIN-ENS-D08-022` | cryogenic spare 장기납기 | condition/lead time 분리 | train outage | P0 |
| `PAIN-ENS-D08-023` | CCS MRV 공급자 증빙 단절 | calibration/flow/model ID 단절 | credit risk | P0 |
| `PAIN-ENS-D08-024` | supplier ESG evidence 수작업 | 문서·CAP 분산 | 실사비용 | P1 |
| `PAIN-ENS-D08-025` | 계약 data-right 뒤늦은 확인 | clause registry 없음 | AI PoC 차단 | P0 |
| `PAIN-ENS-D08-026` | 공급중단 시 대체 시나리오 수작업 | network model 없음 | 대응지연 | P0 |
| `PAIN-ENS-D08-027` | scope 3/CoC 배분 불명확 | lot/cargo carbon gap | claim risk | P1 |
| `PAIN-ENS-D08-028` | invoice/GR/quantity claim 분리 | 3-way/terminal data 단절 | 비용누수 | P1 |
| `PAIN-ENS-D08-029` | 공급사 remote access 통제 분산 | IAM/contract/asset 단절 | cyber | P0 |
| `PAIN-ENS-D08-030` | PoC 절감액 시장효과 혼합 | baseline/control 없음 | 효과 과대평가 | P0 |

---
