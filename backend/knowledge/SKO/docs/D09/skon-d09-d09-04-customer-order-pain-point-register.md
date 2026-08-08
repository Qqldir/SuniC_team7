---
id: skon-d09-d09-04-customer-order-pain-point-register
title: Customer & Order Pain-Point Register
summary: "OEM 수요변동, 계약관리, 공장배정 등 SK온 배터리 사업의 12개 고객·수주 리스크를 우선순위와 모니터링 KPI별로 정리한 문제점 레지스터"
tags: [d09, customer, table]
keywords: [OEM수요, 계약관리, 용량할당, ESS, 신규고객, 수요예측, 고객보상, 신용위험, GWh, 배터리화학, OEM, 공장배정, Capacity, 배터리, 지역공급]
related: [PP-D09-01, PP-D09-02, PP-D09-03, PP-D09-04, PP-D09-05, PP-D09-06, PP-D09-07, PP-D09-08, PP-D09-09, PP-D09-10, PP-D09-11, PP-D09-12]
priority: normal
domain: D09
section: D09-04
source: SK온_D09_Customers_Orders_OEM_Relationships.md
breadcrumb: "SK온 D09 — Customers, Orders & OEM Relationships"
tokens: 847
updated: 2026-08-03
---

> SK온 · D09 고객·수주·OEM 관계 · SK온 D09 — Customers, Orders & OEM Relationships

## D09-04 Customer & Order Pain-Point Register

| Pain Point ID | 문제 | 공개 근거·징후 | 내부에서 확인할 KPI | 우선순위 |
|---|---|---|---|---|
| `PP-D09-01` | OEM 수요 급변·Program 취소 | Ford EV 재편, Ford·VW 판매둔화, SK온 설치량 -7.8% | Forecast error, cancellation exposure, unused qualified GWh | P0 |
| `PP-D09-02` | 계약 총량과 Firm Call-off 혼합 | Nissan 100GWh·Slate 20GWh는 다년 총량 | contract-to-calloff conversion, annual drawdown | P0 |
| `PP-D09-03` | 미래 수주의 생산공장 미배정 | Nissan·Slate 생산공장 비공개 | unallocated contracted GWh, qualification lead time | P0 |
| `PP-D09-04` | 고객·차종–공장 Mapping 공백 | VW·Mercedes 현재 Program, Commerce 현재 Mix 미확인 | mapping completeness, orphan capacity/program | P0 |
| `PP-D09-05` | 고객승인 Capacity와 명목 Capacity 괴리 | HSBMA Ramp, Tennessee 2028 준비 | qualified/gross ratio, first-pass yield, customer release rate | P0 |
| `PP-D09-06` | JV·전용 Capacity의 낮은 전환 유연성 | HSBMA는 HMG 50:50 JV, Ford JV 해소 | fungible GWh, consent lead time, stranded cost | P1 |
| `PP-D09-07` | 고객 보상·Claim의 반복가능성 불명 | 2026 Q2 고객 보상금이 수익성 개선 요인 | claim root cause, recurring/non-recurring EBIT | P0 |
| `PP-D09-08` | 신규 스타트업 고객 Ramp·신용위험 | Slate 2026~2031 공급, 추가 option | customer milestone score, payment security, ramp variance | P1 |
| `PP-D09-09` | ESS Pipeline과 확정수주의 혼합 | Flatiron 1GWh + 6.2GWh 우선협상 | pipeline probability, award conversion, COD delay | P0 |
| `PP-D09-10` | NCM 중심 고객구성과 LFP·ESS 수요전환 | Flatiron LFP, 미국 ESS 확대 | chemistry demand mix, conversion cost, margin by product | P0 |
| `PP-D09-11` | 지역별 고객수요와 공장 제약의 비동기 | 아시아 판매증가, 북미·유럽 조정 | regional demand/capacity gap, logistics and tariff delta | P1 |
| `PP-D09-12` | 외부 신호의 수작업 반영 지연 | 차종 지연·Shift·정책·판매가 여러 소스에 분산 | signal-to-decision lead time, missed alerts | P1 |

SK온 Battery Business는 2026년 2분기 아시아 판매량 확대, 고객 보상, 미국 세액공제 증가의 영향을 받아 흑자 전환했다. 회사도 고객 보상을 일회성 요인으로 구분했고 향후 AI Hyperscaler·전력 Utility를 포함한 ESS 수주 확대를 제시했다. 따라서 고객관계 DB는 단순 수주총량보다 **반복 가능한 물량·Margin·고객 유형**을 구분해야 한다. ([SK Innovation 2026 Q2](https://askinno.com/global/archives/156625))

---
