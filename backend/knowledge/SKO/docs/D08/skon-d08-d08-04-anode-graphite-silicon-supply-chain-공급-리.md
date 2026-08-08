---
id: skon-d08-d08-04-anode-graphite-silicon-supply-chain-공급-리
title: Anode / Graphite / Silicon Supply Chain — 공급 리스크와 조기경보
summary: "음극재·흑연·실리콘의 공급망 리스크 12개를 정의하고, 각 리스크의 노출 대상, 조기경보 신호, 완화 방안을 정리한 리스크 관리 매트릭스."
tags: [d08, supply-chain, table]
keywords: [음극재, 흑연 정제, 규소, 수출허가제, 무역정책, 중국 의존도, 공급 다변화, 원료 조달, 공급 리스크, 조기경보, 중국 집중도, graphite refining, AAM, 무역구제, 수급 공백, 이중 공급, traceability, export control]
related: [RISK-ANODE-REPLACEMENT-GAP, RISK-ANODE-CN-CONCENTRATION, RISK-ANODE-PFE-CONTROL, RISK-ANODE-EXPORT-CONTROL, RISK-ANODE-TRADE-POLICY, RISK-ANODE-PROJECT-FINANCE, RISK-ANODE-QUALIFICATION, RISK-SI-SINGLE-SOURCE, RISK-SI-EXPANSION-YIELD, RISK-ANODE-CARBON, RISK-ANODE-TRACEABILITY, RISK-ANODE-DATA-MISCLASS]
priority: normal
domain: D08
section: D08-04
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain"
tokens: 1129
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain

### 9. 공급 리스크와 조기경보

| risk_id | 리스크 | 노출 대상 | 조기경보 신호 | 완화/후속 데이터 | 우선순위 |
|---|---|---|---|---|---|
| `RISK-ANODE-REPLACEMENT-GAP` | Westwater 해지 후 북미 대체조달 공백 | 미국 EV·ESS 생산 | 대체 계약 미공개, 단기 중국산 의존·spot 비중 상승 | 대체 supplier/grade/volume/qualification 원장 | P0 |
| `RISK-ANODE-CN-CONCENTRATION` | 흑연 정제·AAM의 중국 집중 | 천연·합성흑연 전체 | 중국 supplier share·refining share 상승, 공급지연 | 공장·grade별 ex-China dual source, 안전재고 | P0 |
| `RISK-ANODE-PFE-CONTROL` | 비중국 소재 시설의 중국계 소유·통제·기술 연계 | BTR Indonesia 등 | cap table·license·management rights 변화 | D08-08 ownership/control/technology/contract 판정 | P0 |
| `RISK-ANODE-EXPORT-CONTROL` | 중국 흑연 수출허가 지연·제한 | 중국산 천연·합성흑연 및 중간재 | 허가 처리기간 증가, license 거절·물량감소 | 공급국·정제국 다변화, 허가 리드타임·재고 모니터링 | P0 |
| `RISK-ANODE-TRADE-POLICY` | 관세·AD/CVD·세액공제 규칙 변동 | 미국향 AAM | Section 301·PFE/MACR·무역구제 판정 변화 | landed cost 시나리오와 계약 change-in-law 조항 | P0 |
| `RISK-ANODE-PROJECT-FINANCE` | 비중국 신규시설의 자금조달·준공 지연 | Kellyton·Urbix 및 대체 후보 | CAPEX 미조달, 공사감속, commissioning 연기 | 단계별 milestone, 대체 계약, credit risk score | P1 |
| `RISK-ANODE-QUALIFICATION` | 원료원·정제시설 변경에 따른 승인 지연 | 모든 흑연 grade | 4M/PPAP 지연, 수명·급속충전 편차 | 원료변경 사전통보, dual qualification, 시험 데이터 | P0 |
| `RISK-SI-SINGLE-SOURCE` | Si계 승인소재·공정 집중 | 고속충전·고에너지 제품 | 공급사 장애, 증설·수율 지연, 품질 편차 | 대체 SiOx/Si-C grade와 blend 재승인 | P1 |
| `RISK-SI-EXPANSION-YIELD` | 실리콘 팽창·초기효율·수명 문제 | Si 혼합 음극 | swelling·gas·capacity retention 악화, scrap 증가 | 소재–바인더–전해액 공동 최적화와 SPC | P1 |
| `RISK-ANODE-CARBON` | 합성흑연 흑연화 전력과 천연흑연 정제의 탄소·환경부하 | EU향·저탄소 고객 | facility PCF 누락, 전력믹스·산세 공정 변화 | 시설별 PCF·전력원·폐수·화학물질 mass balance | P1 |
| `RISK-ANODE-TRACEABILITY` | 광산·정광→AAM→cell lot 연결 단절 | 모든 음극재 | COO·CoA·B/L·lot key 불일치 | 공통 lot ID, chain-of-custody, ERP 입고 연결 | P0 |
| `RISK-ANODE-DATA-MISCLASS` | 그룹 투자·고객목록을 공급계약으로 오인 | Group14·BTR 등 | 기사·IR에서 법인·제품·공장 혼용 | legal counterparty와 product/facility 필수검증 | P0 |

중국은 2023년 12월부터 특정 흑연 품목에 수출허가제를 시행하고 있으며 이는 금수조치와는 다르지만 허가 리드타임·최종사용자·용도 증빙 리스크를 만든다. 미국의 중국산 AAM AD/CVD 사건은 2026년 USITC의 산업피해 부정 판정으로 명령이 발령되지 않았지만, 천연흑연에 대한 Section 301 관세와 PFE·material assistance 판정은 별도 축이다. 무역구제 사건 종료를 중국계 공급망의 규제 리스크 해소로 해석하지 않는다.
