---
id: skon-d08-d08-05-electrolyte-separator-current-collector-6
title: "Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain — 검증 큐"
summary: 배터리 전해액·동박·CNT·PVDF 등의 공급사·시설·물량·원료경로를 검증하는 17개 항목의 검증 큐 테이블.
tags: [d08, supply-chain, table]
keywords: [공급사 검증, 배터리 소재, 추적성, 원산지, BOM, 공급망 리스크, 납품 승인, 계약 관리, 동박, CNT, CoA, 원료경로, sub-tier, PVDF, 폐기회수]
related: []
priority: normal
domain: D08
section: D08-05
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain"
tokens: 1172
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain

### 10. 검증 큐

| 우선순위 | verification_id | 확인 질문 | 필요한 1차 자료 | 완료 조건 |
|---|---|---|---|---|
| P0 | `V-AUX-001` | SKIET 5년 계약의 2026~2027 source plant·면적·도착공장은? | 계약변경서·forecast·PO·출하·입고 | plant–grade–area–receiving plant 연결 |
| P0 | `V-AUX-002` | 중국법인 매각과 증평 중단이 SK온 계약에 미치는 영향은? | transition plan·4M·고객승인·BCP | 이전일정·대체공장·안전재고 확인 |
| P0 | `V-AUX-003` | WCP 신규 ESS 고객은 법적으로 SK온인가? | 계약서·당사자 공시·PO | customer entity와 공급조건 직접 확인 |
| P0 | `V-AUX-004` | Enchem·Soulbrain의 SK온향 formula·시설·물량은? | 계약·AVL·PO·CoA·입고원장 | plant/platform/formula별 actual 확보 |
| P0 | `V-AUX-005` | 전해액의 LiPF6/LiFSI·용매·첨가제 sub-tier는? | supplier declaration·COO·CoA·BOM | sub-tier facility/country–blend lot 연결 |
| P1 | `V-AUX-006` | Georgia·Poland NMP closed loop의 실제 회수율과 복귀량은? | mass balance·정제 CoA·폐기/재투입 기록 | virgin/recovered/purge tonne reconciliation |
| P0 | `V-AUX-007` | Solid Power 최소 8t의 validation과 실제 인도는 진행됐는가? | acceptance·invoice·B/L·CoA·R&D receiving | delivered tonne과 validation gate 확인 |
| P0 | `V-AUX-008` | SK온의 직접 동박 공급사와 grade는 무엇인가? | supplier master·계약·PO·CoA·입고 | supplier/facility/thickness/plant 매핑 |
| P0 | `V-AUX-009` | SK Nexilis가 SK온에 직접 납품하는가? | 양사 계약·invoice·shipment·receiving | 그룹관계와 분리된 supply edge 확인 |
| P0 | `V-AUX-010` | Wuxing 32,400t 중 연도별 실제 주문·출하량은? | call-off PO·invoice·B/L·입고 | estimate와 actual drawdown 분리 |
| P1 | `V-AUX-011` | 삼아알미늄의 SK온 계약·공장·물량·원료경로는? | 계약·고객별 매출·COO·CoA | 고객별 actual과 Al feedstock 경로 확인 |
| P0 | `V-AUX-012` | 미국향 중국계 foil의 PFE·material assistance 판정은? | cap table·통제권·원료·기술·계약 | D08-08 rule engine과 법무검토 완료 |
| P1 | `V-AUX-013` | artience CNT의 계약량·grade·cell platform은? | 계약·승인규격·PO·CoA·입고 | facility/formula/platform별 actual 확보 |
| P1 | `V-AUX-014` | Kentucky CNT 시설이 가동·승인됐는가? | occupancy·commissioning·4M·첫 출하 | operating date와 SK온 승인 확인 |
| P0 | `V-AUX-015` | PVDF·수계 바인더와 탭/리드 직접 공급사는? | AVL·BOM·계약·PO·입고 | material/grade/facility별 supplier 확정 |
| P1 | `V-AUX-016` | PFAS 제한안·NMP 규제 변화의 제품별 영향은? | 최종 법령·SDS·사용량·노출·derogation | 법적 의무·전환시점·대체승인 계획 확인 |
| P0 | `V-AUX-017` | 보조소재 lot을 electrode/cell batch까지 추적 가능한가? | PO–invoice–B/L–COO–CoA–lot–MES | 공통 key·질량수지·예외처리 검증 |

### 11. D08-05 산출물 수량

- 관계 원장: 13개(확정·부분확인 9개, 후보·미확인 4개)
- 사업재편·생산중단·별도계약 축소 이벤트: 3개
- 그룹 인접·언론 추정·공급사 미확인 관계: 4개
- 공급사·시설 노드: 17개
- 추적성 경로: 10개
- 대표 지식그래프 YAML: 6개
- 공급 리스크 레코드: 16개
- 검증 큐: 17개
- 수량이 공개된 계약: 2개(Solid Power 최소 8t 조건부 R&D, Wuxing 예상 32,400t 주문형 framework)
- 기준일 현재 공개자료로 확인된 SK온 직접 동박 계약: 0개
- 기준일 현재 `FULLY_TRACEABLE` 경로: 0개
