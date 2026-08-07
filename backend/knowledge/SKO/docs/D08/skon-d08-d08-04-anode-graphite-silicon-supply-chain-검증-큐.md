---
id: skon-d08-d08-04-anode-graphite-silicon-supply-chain-검증-큐
title: Anode / Graphite / Silicon Supply Chain — 검증 큐
summary: 음극재·흑연·실리콘 공급망의 검증·추적성 체크리스트와 현재 정보 완성도를 정리한 문서. 12개 검증 항목의 우선순위·확인질문·필요자료·완료조건을 명시한다.
tags: [d08, supply-chain, table]
keywords: [검증 체크리스트, 공급계약 관리, 공급사 실적, 원산지 추적, CoO 증빙, 탄소발자국, PPAP 양산승인, Lot 추적성, 공급 리스크, 흑연 대체, 검증 큐, 흑연 공급사, 실리콘 원료, 공급망 추적성, 원산지 확인, 4M/PPAP, JDA]
related: []
priority: normal
domain: D08
section: D08-04
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain"
tokens: 1054
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain

### 10. 검증 큐

| 우선순위 | verification_id | 확인 질문 | 필요한 1차 자료 | 완료 조건 |
|---|---|---|---|---|
| P0 | `V-ANODE-001` | Westwater 해지분을 대체하는 미국향 천연흑연 계약은 무엇인가? | SK온 공급계약·구매원장·supplier 공시 | supplier·facility·grade·기간·물량·도착공장 확인 |
| P0 | `V-ANODE-002` | 기준일 현재 천연/합성흑연 공급사와 비중은? | supplier master, PO·invoice·입고·BOM | 공장·platform·grade별 실제 tonne/share 확보 |
| P0 | `V-ANODE-003` | Urbix JDA가 본계약·양산승인으로 전환됐는가? | 양사 최종계약, 4M/PPAP, 첫 B/L·CoA | 계약·상업시설·첫 출하 확인 |
| P0 | `V-ANODE-004` | 대주전자재료의 2024~2026 실제 공급량과 계약기간은? | 공급계약·출하장·SK온 PO·입고 | 연도별 actual tonne·grade·valid_to 확인 |
| P0 | `V-ANODE-005` | 대주전자재료 Si계 소재의 원료 실리콘·탄소원과 제조시설은? | supplier sub-tier, COO, CoA, process declaration | 원료국–시설–Si grade–SK온 lot 연결 |
| P0 | `V-ANODE-006` | BTR 2025 SK온 그룹 거래 중 AAM 비중과 생산시설은? | BTR 거래명세·SK온 구매원장·facility shipment | cathode/anode/other와 CN/ID facility 분리 |
| P0 | `V-ANODE-007` | BTR Indonesia 또는 다른 비중국 시설의 PFE 판정은? | cap table, 통제권, license, 기술·구매계약 | D08-08 규칙엔진·법무검토 완료 |
| P1 | `V-ANODE-008` | Group14 SCC55가 SK온에 공급되는가? | SK온·Group14 공급계약·승인·출하 | 그룹투자와 별개인 직접 supply edge 확인 |
| P0 | `V-ANODE-009` | 흑연 원료원 변경이 4M·고객승인에 어떻게 연결되는가? | 변경통보·승인 workflow, cell validation | mine/refinery change–approval revision 연결 |
| P1 | `V-ANODE-010` | 제품별 천연/합성흑연·실리콘 blend ratio는? | cell BOM, electrode recipe revision | platform·revision별 범위와 승인 supplier set 확인 |
| P1 | `V-ANODE-011` | 시설별 탄소발자국과 정제 화학물질·폐수 데이터는? | supplier PCF, 전력계량, LCA, 환경허가 | 동일 경계·단위의 facility-specific PCF 확보 |
| P0 | `V-ANODE-012` | 음극재 lot을 셀 입고·전극 batch까지 추적할 수 있는가? | PO–invoice–B/L–COO–CoA–AAM lot–receiving/ME batch | 공통 key·수량 질량수지·예외처리 검증 |

### 11. D08-04 산출물 수량

- 공급계약·JDA·상용 공급·상업관계 레코드: 7개(기존 D08-02 레코드 2개 재사용)
- 그룹 인접·오인 방지 관계: 2개
- 공급사·시설·자산 노드: 12개
- 원산지·추적성 경로: 5개
- 대표 지식그래프 YAML: 4개
- 공급 리스크 레코드: 12개
- 검증 큐: 12개
- 기준일 현재 공개 확인된 현행 직접 천연흑연 장기 구매계약: 0개
- 취소된 천연흑연 최대 계획물량: 34,000t(Westwater, 현행 합산 0)
- 실리콘계 상용 공급 발표 상대방: 1개(대주전자재료; 실제 물량 미공개)
- JDA만 공개되고 본계약이 확인되지 않은 천연흑연 상대방: 1개(Urbix)
- `FULLY_TRACEABLE` 음극 경로: 0개
