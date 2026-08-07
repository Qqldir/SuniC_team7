---
id: skon-d08-d08-05-electrolyte-separator-current-collector-5
title: "Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain — 공급 리스크와 조기경보"
summary: 배터리 재료(전해액·분리막·집전체 등) 공급망에서 발생 가능한 16가지 리스크별로 조기경보 신호와 완화 방안을 정리한 리스크 맵핑 테이블.
tags: [d08, supply-chain, table]
keywords: [위험 식별, 공급사 집중, 이중 공급, 원산지 추적, PFAS, NMP, sub-tier 투명성, 추적성, 규제 변화, 배터리 원소재, 공급망 위험, 조기경보 신호, 전해액, 분리막, 집전체, COO, 다원소싱, 규제]
related: [RISK-SEP-CAPACITY-TRANSFER, RISK-SEP-SINGLE-RELATION, RISK-SEP-RAW-MATERIAL, RISK-ELY-FORMULA-LOCKIN, RISK-ELY-SALT-CONCENTRATION, RISK-ELY-HAZMAT-LOGISTICS, RISK-NMP-HEALTH-REGULATION, RISK-BINDER-PFAS, RISK-ALFOIL-CN-POLICY, RISK-FOIL-THICKNESS-YIELD, RISK-CUFOIL-UNKNOWN-SOURCE, RISK-SSE-SCALEUP, RISK-CNT-DISPERSION, RISK-AUX-SUPPLIER-UNKNOWN, RISK-DATA-OVERCLAIM, RISK-TRACEABILITY-AUX]
priority: normal
domain: D08
section: D08-05
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain"
tokens: 1206
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Electrolyte, Separator, Current Collector & Auxiliary Materials Supply Chain

### 9. 공급 리스크와 조기경보

| risk_id | 리스크 | 노출 대상 | 조기경보 신호 | 완화/후속 데이터 | 우선순위 |
|---|---|---|---|---|---|
| `RISK-SEP-CAPACITY-TRANSFER` | SKIET 중국 매각·한국 중단에 따른 공급기지 재편 | LiBS | 매각종결·중단 일정, 납기·물류거리 변화 | SK온 계약별 source plant와 이전 승인계획 | P0 |
| `RISK-SEP-SINGLE-RELATION` | 공개 확정 분리막 공급관계 집중 | 주요 셀 platform | 공급사 가동률·품질사고·계약변경 | plant/grade별 dual source와 안전재고 | P0 |
| `RISK-SEP-RAW-MATERIAL` | PE·coating 원료의 sub-tier 불투명 | 분리막 | 원료 변경·수분·입도·shutdown | sub-tier COO·4M·lot genealogy | P1 |
| `RISK-ELY-FORMULA-LOCKIN` | 고객맞춤 formula·첨가제 package 전환비용 | 액체 전해액 | 신규공급사 승인 지연·수명/가스 편차 | formula revision별 dual qualification | P0 |
| `RISK-ELY-SALT-CONCENTRATION` | LiPF6·LiFSI 생산국·공급사 집중 | 전해액 | 가격급등·품질편차·수출통제 | salt 제조시설·원료국·재고 원장 | P0 |
| `RISK-ELY-HAZMAT-LOGISTICS` | 수분민감·유해화학물 운송과 현지 blending 장애 | 전해액 | tanker 지연·오염·누출·보관기한 초과 | 지역별 backup tank·packaging·SDS·BCP | P0 |
| `RISK-NMP-HEALTH-REGULATION` | NMP 작업자 노출과 미국 TSCA 규제 변화 | 양극 slurry·재생공정 | 최종규칙·노출한계·보호프로그램 변경 | 회수율·작업환경측정·대체공정 시나리오 | P0 |
| `RISK-BINDER-PFAS` | PFAS 제한 논의가 fluorinated binder에 미칠 영향 | PVDF 사용 전극 | ECHA 최종 의견·입법·derogation 범위 | grade별 PFAS 분류·비불소 대체·고객승인 | P1 |
| `RISK-ALFOIL-CN-POLICY` | 중국 생산 알루미늄박의 PFE·관세·통상 노출 | 미국향 셀 | 소유·통제·원료국·관세 판정 변화 | D08-08 법률판정, 비중국 dual source | P0 |
| `RISK-FOIL-THICKNESS-YIELD` | 박막화에 따른 pinhole·찢김·코팅수율 저하 | 동박·알루미늄박 | web break·scrap·저항·두께 Cpk 악화 | supplier lot–electrode batch SPC | P1 |
| `RISK-CUFOIL-UNKNOWN-SOURCE` | 직접계약·원산지 미확인 | 음극 집전체 | 공개/내부 supplier master 불일치 | 계약·PO·COO·CoA 확보 | P0 |
| `RISK-SSE-SCALEUP` | 고체전해질 validation·원가·양산 scale-up 지연 | 전고체 개발 | delivery·purity·line yield milestone 지연 | R&D와 commercial readiness gate 분리 | P1 |
| `RISK-CNT-DISPERSION` | CNT 분산·carrier 품질과 단일 formulation 의존 | 도전재 | viscosity·agglomerate·electrode resistance 편차 | 원료·분산공정 dual source와 SPC | P1 |
| `RISK-AUX-SUPPLIER-UNKNOWN` | 바인더·탭/리드 공급사 미가시성 | 전극·조립 | change notice 누락·품질 이슈 | supplier master·approved vendor list 확보 | P0 |
| `RISK-DATA-OVERCLAIM` | 그룹사·고객목록·언론 추정을 직접계약으로 오인 | SK Nexilis·WCP 등 | 법인·제품·시설 없는 관계 생성 | 당사자·계약·grade·실적 필드 필수화 | P0 |
| `RISK-TRACEABILITY-AUX` | sub-tier 원료와 cell lot 연결 단절 | 전해액·분리막·foil·도전재 | COO·CoA·lot key 불일치 | 공통 ID·질량수지·ERP/MES 입고 연결 | P0 |

미국 EPA의 NMP 규제는 기준일 현재 제안 단계이며 배터리 제조를 일률적으로 금지하는 규칙으로 확정하지 않는다. ECHA의 PFAS 제한안 역시 의견·협의 과정과 최종 입법을 분리하며, 현재 단계에서 PVDF 사용금지를 확정 사실로 기록하지 않는다.
