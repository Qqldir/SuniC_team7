---
id: skon-d08-d08-02-cathode-supply-chain-검증-큐
title: Cathode Supply Chain — 검증 큐
summary: "양극재(CAM) 공급사의 계약 상태, 지분 구조, 공급량, 미국 규정 준수를 검증하기 위한 우선순위별 확인 항목 테이블"
tags: [d08, supply-chain, table]
keywords: [캐소드, 공급사, 에코프로비엠, 엘앤에프, 당성과기, CAM, 지분, PFE 규정, BTR, 공급계약, EcoPro, L&F, PFE, LFP, 검증 항목, 계약 갱신]
related: []
priority: normal
domain: D08
section: D08-02
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain"
tokens: 811
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain

### 9. 검증 큐

| 우선순위 | verification_id | 확인 질문 | 필요한 1차 자료 | 완료 조건 |
|---|---|---|---|---|
| P0 | `V-CAM-001` | 에코프로비엠 2024~2026 계약의 2027년 이후 갱신·대체가 있는가? | DART 정정/신규 공시, SK온·에코프로비엠 공식 발표 | 후속 계약 ID·기간·품목 확인 |
| P0 | `V-CAM-002` | 엘앤에프 30만t 계약의 연도·공장·도착법인별 실제 drawdown은? | 사업보고서, 공급계약 정정공시, 구매/출하 데이터 | 연도별 actual tonne과 facility edge 확보 |
| P0 | `V-CAM-003` | 당성과기 1.7만t 프레임워크의 실제 PO와 공급시설은? | 월별 PO, supplier shipment, COO, SK온 구매원장 | PO 단위 물량·CN/FI 생산시설 확인 |
| P0 | `V-CAM-004` | 당성과기·BTR 경로가 미국 PFE 규정상 어떤 분류를 받는가? | 최신 주주명부, 통제권, 계약·라이선스, facility BOM | D08-08 규칙엔진 판정과 법무 검토 |
| P0 | `V-CAM-005` | EcoPro CAM Canada가 재개됐는가? | 회사·정부 재개 공시, 공사 진척, 시운전/양산 증거 | `SUSPENDED`를 변경할 1차 증거 확보 |
| P1 | `V-CAM-006` | BTR 2025 SK온 그룹 매출의 제품군·시설별 구성은? | BTR/SK온 거래 세부, JV 감사자료 | CAM/AAM/기타 금액과 facility 분리 |
| P1 | `V-CAM-007` | BTR 창저우 JV의 현재 SK온 지분은 25.0%인가 31.3%인가? | 현재 JV 주주명부·공시 | 지분 변동일·거래 원인까지 확인 |
| P1 | `V-CAM-008` | Eco&D→Umicore→SK온 경로가 실제인가? | 당사자 계약·공시, 출하·인증 자료 | direct/indirect relationship과 물량 확인 |
| P1 | `V-CAM-009` | LFP MOU가 구속력 있는 공급계약으로 전환됐는가? | 엘앤에프·SK온 공시, 제품승인·발주 | 계약량·기간·공급공장·도착지역 확인 |

### 10. D08-02 산출물 수량

- 공급계약·프레임워크·MOU 레코드: 9개
- JV·시설·프로젝트·보도경로 레코드: 4개
- 공급사·시설 정규화 노드: 10개
- 대표 지식그래프 YAML: 4개
- 공급 리스크 레코드: 8개
- 검증 큐: 9개
- 현행 직접 CAM 장기계약으로 공개 확인된 상대방: 2개(에코프로비엠, 엘앤에프)
- 주문 기반 CAM 프레임워크 상대방: 1개(베이징당성과기)
- LFP 확정 공급계약: 0개; 공개 MOU: 1개(엘앤에프)
