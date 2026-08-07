---
id: skon-d11-d11-08-external-cases-transferable-patterns
title: External Cases & Transferable Patterns
summary: "배터리 제조·원가·수익성 개선을 위한 7개 해외 주요 사례(Argonne, IRS, DOE, BMW, CATL, Samsung SDI)와 각각의 SK온 적용 방식을 정리한 벤치마킹 매트릭스"
tags: [d11, cost, table]
keywords: [BatPaC, 하향식 원가모델, 공정 디지털 트윈, IRS 45X 세액공제, AI 불량검출, Digital Thread, CATL 규모, 현금흐름, 정책 환급, 제품 Mix 효과, 벤치마킹, 배터리 원가, 디지털 트윈, 생산 최적화, 제품 믹스, kWh, 경쟁 분석]
related: [CASE-D11-01, CASE-D11-02, CASE-D11-03, CASE-D11-04, CASE-D11-05, CASE-D11-06, CASE-D11-07]
priority: normal
domain: D11
section: D11-08
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1246
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-08 External Cases & Transferable Patterns

| Case ID | 외부 사례 | 확인된 방식 | SK온 적용 포인트 |
|---|---|---|---|
| `CASE-D11-01` | Argonne BatPaC | Cell·Pack 설계와 공정단계·생산규모를 연결하는 Bottom-up 원가모델 | 내부 BOM·공정·수율을 연결한 Shadow Cost Model 구축 |
| `CASE-D11-02` | IRS 45X Component Ledger | Cell·Module별 kWh Credit과 생산·판매·귀속 요건을 분리 | 인식액이 아닌 적격 kWh→신청→현금화 Audit Trail |
| `CASE-D11-03` | DOE Smart Battery Manufacturing | ML 기반 In-line QC, 비침습 Sensor, Digital Thread와 폐쇄루프 공정제어 지원 | 불량검출 정확도보다 Scrap·Accepted kWh·Margin 개선을 공동 KPI로 설정 |
| `CASE-D11-04` | BMW Virtual Factory | 30개 초과 공장 Digital Twin, 생산계획비용 최대 30% 절감 전망 | EV→ESS·Pouch→Prismatic 전환의 Layout·Ramp·CAPEX 사전검증 |
| `CASE-D11-05` | CATL Scale·Cash·Portfolio | 2025년 661GWh 판매, 영업현금흐름 RMB 133.2bn, 다중 화학계·ESS·재활용 | 경쟁비용 Benchmark를 소재가격 하나가 아닌 규모·Mix·현금·순환성으로 확장 |
| `CASE-D11-06` | Samsung SDI Mix Turnaround | 2026 Q2 ESS·UPS·BBU·유럽 EV Mix와 미국 생산 Credit·관세환급으로 흑자 | 제품 Mix 효과와 정책·환급 효과를 분리한 회복 Bridge 비교 |
| `CASE-D11-07` | DOE Better Plants | 산업체가 Energy Intensity와 누적 비용절감을 표준화해 관리 | Dry room·Formation·Utility를 accepted kWh와 연결한 Energy P&L |

Argonne의 BatPaC는 생산규모와 각 제조공정의 비용을 반영해 Lithium-ion Battery의 Bottom-up Cost를 계산한다. 공개모델을 SK온 원가의 정답으로 복사하는 것이 아니라, 내부 Cost Ledger의 누락 항목과 가정 민감도를 검증하는 독립 Shadow Model로 쓰는 것이 적절하다. ([Argonne BatPaC](https://www.anl.gov/partnerships/batpac-battery-manufacturing-cost-estimation), [BatPaC Manual](https://publications.anl.gov/anlpubs/2022/07/176234.pdf))

DOE의 Transformative Battery Manufacturing 선정과제는 In-line Data·Machine Learning·Physics Simulation·Non-invasive Sensor·Digital Thread를 결합해 폐기 Trial과 품질비용을 줄이는 방향을 보여준다. 이는 외부 파트너를 단일 AI 모델 공급자가 아니라 Sensor–공정모델–MES/API–현장검증의 Consortium으로 구성해야 함을 시사한다. ([U.S. DOE AMMTO](https://www.energy.gov/cmei/ammto/funding-selections-platform-technologies-transformative-battery-manufacturing))

BMW는 30개가 넘는 생산거점의 Digital Twin을 확장하고, 생산계획 비용을 최대 30% 줄일 수 있다고 발표했다. SK온에는 기존 EV Line의 ESS·다른 Form Factor 전환을 실제 설비 변경 전에 검증하는 `conversion economics twin`으로 이전할 수 있다. ([BMW Virtual Factory](https://www.press.bmwgroup.com/global/article/detail/T0450699EN/bmw-group-scales-virtual-factory?language=en))

CATL은 2025년 661GWh 판매, RMB 423.7bn 매출, RMB 72.2bn 지배주주 순이익, RMB 133.2bn 영업현금흐름을 발표했다. 회계기준·사업범위가 달라 SK온 Segment Margin과 직접 비교할 수 없지만, 규모·다중 화학계·ESS·재활용·현금창출을 함께 운영하는 경쟁모델은 D11 Benchmark 축으로 유효하다. ([CATL 2025 Annual Report Release](https://www.catl.com/en/news/6773.html))

Samsung SDI는 2026 Q2 Battery 사업 영업이익 1,593억원을 기록했으나 고부가 제품 판매와 가동률뿐 아니라 AMPC와 미국 관세환급도 개선요인으로 제시했다. 경쟁사의 흑자 역시 `Mix·Operation·Policy·One-off`를 분리해야 한다는 비교사례다. ([Samsung SDI 2026 Q2](https://news.samsungsdi.com/global/press/view?seq=440))

---
