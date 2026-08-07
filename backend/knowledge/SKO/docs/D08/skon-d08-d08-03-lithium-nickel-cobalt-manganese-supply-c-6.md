---
id: skon-d08-d08-03-lithium-nickel-cobalt-manganese-supply-c-6
title: Lithium / Nickel / Cobalt / Manganese Supply Chain — 검증 큐
summary: "배터리 원소재 공급망에서 계약 현황, 공급사 확인, 원산지 추적을 위한 14개 항목의 검증 큐 체크리스트 및 산출물 통계."
tags: [d08, supply-chain, table]
keywords: [원료 공급 검증, 오프테이크 계약, LOT 추적성, 공급사 현황 확인, 원산지 증명, 계약 이행도, traceability, MOU 갱신, CAM 원산지, 공급 리스크, 공급망 추적성, 계약 이행 확인, 공급사 실사, CAM 원료 조달, offtake 계약, 원료 품질 증명, 소싱 체크리스트]
related: []
priority: normal
domain: D08
section: D08-03
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain"
tokens: 1117
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain

### 10. 검증 큐

| 우선순위 | verification_id | 확인 질문 | 필요한 1차 자료 | 완료 조건 |
|---|---|---|---|---|
| P0 | `V-RAW-001` | SQM 계약의 2023~기준일 실제 drawdown·잔여량과 2028 이후 갱신은? | SK온 구매원장, SQM shipment, 후속 계약 | 연도별 actual·remaining·renewal ID 확인 |
| P0 | `V-RAW-002` | PPLS 15,000t의 연도·lot·CAM/입고공장 배정은? | PPLS 출하, COO/CoA, SK온 PO·입고 | Pilgangoora–PPLS–CAM–SK온 lot 연결 |
| P0 | `V-RAW-003` | POSCO Argentina 계약의 제품형태·4M·첫 출하는? | 계약 specification, 4M 승인서, 첫 B/L·CoA | LiOH/Li2CO3 ID와 physical flow 확정 |
| P0 | `V-RAW-004` | EcoPro Innovation 후속 2~3년 계약이 체결됐는가? | SK온·EcoPro 공식계약/공시 | 기간·총량·원료원·공급시설 확인 |
| P0 | `V-RAW-005` | Lake CFA 선행조건과 SK온 10% 투자가 완료됐는가? | 최종계약, 주주명부, FID, Lake 공시 | 조건 충족일·투자·first delivery 확인 |
| P0 | `V-RAW-006` | Exxon MOU가 구속 오프테이크로 전환됐는가? | 양사 최종계약·FID·상업생산 공시 | 제품형태·물량·기간·도착공장 확인 |
| P1 | `V-RAW-007` | Global Lithium 2년 MOU가 갱신·본계약화됐는가? | ASX·SK온 후속 공시 | 갱신/종료일 또는 최종계약 확인 |
| P0 | `V-RAW-008` | Indonesia MHP JV가 실제 설립·가동됐는가? | 인도네시아 법인등기, GEM/EcoPro/SK온 공시, EPC·시운전 | 법인·지분·시설·actual output·offtake 확정 |
| P0 | `V-RAW-009` | 2026년 현재 직접 Ni sulfate/MHP 공급계약은 무엇인가? | SK온 구매계약, 공급사 공시, PO·CoA | supplier–refinery–material–plant edge 확보 |
| P0 | `V-RAW-010` | Glencore 계약 이후 현행 Co 공급사는 누구인가? | 갱신계약·신규 공급계약·CoC | 현행 agreement ID·원산지·기간 확인 |
| P0 | `V-RAW-011` | NCM 계약의 Mn sulfate 공급사·정련시설·광산은? | pCAM/CAM BOM, tier-2/3 declaration | sulfate lot부터 CAM lot까지 연결 |
| P0 | `V-RAW-012` | D08-02 CAM 계약의 Ni/Co/Mn sulfate 원산지는? | supplier sub-tier list, COO, RMI/EMRT, audit | 계약·grade·시설별 upstream edge 생성 |
| P1 | `V-RAW-013` | ioneer–Ford 물량이 현재도 SK온 관련 공장에 배정되는가? | Ford/ioneer 최신 오프테이크·shipment·plant allocation | 법적 buyer와 current receiving entity 확정 |
| P0 | `V-RAW-014` | 공개 구조경로를 실제 lot traceability로 승격할 수 있는가? | PO–invoice–B/L–COO–CoA–CAM lot–cell receiving lot | 전 단계 공통 key와 질량수지 검증 |

### 11. D08-03 산출물 수량

- 리튬 직접 계약·조건부 프레임워크·MOU: 7개
- D08-02에서 재사용한 포괄 원료 MOU: 1개(중복 레코드 미생성)
- 니켈·코발트 직접/전신 관계: 3개
- 고객 지정 간접 후보: 1개
- 공급사·광산/염호·프로젝트·정련시설 노드: 20개
- 자산별 추적성 경로: 10개
- 대표 지식그래프 YAML: 6개
- 공급 리스크 레코드: 13개
- 검증 큐: 14개
- 기준일 현재 계약기간 내 직접 LiOH 계약 상대방: 2개(SQM, PPLS)
- 공급 전 품질인증 단계의 구속 리튬 계약 상대방: 1개(POSCO Argentina)
- 공개 1차 자료로 확인된 현행 직접 독립 Ni/Co/Mn 계약: 0개(`NOT_PUBLICLY_CONFIRMED`)
- `FULLY_TRACEABLE` 경로: 0개
