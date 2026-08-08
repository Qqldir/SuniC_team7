---
id: skon-d11-d11-07-profitability-pain-point-register
title: Profitability Pain-Point Register
summary: 공개 손익 변동을 설명하는 SK온의 수익성 문제점 14가지와 각각을 측정할 내부 KPI 정리표
tags: [d11, cost, table]
keywords: [수익성 진단, 원가분석, EBIT, 가동률, 합격량, 고정비, 반복이익, AMPC, 고객보상, Margin, 배터리원가, 손상, 현금흐름, 수익율, 비용효율, ESS]
related: [PP-D11-01, PP-D11-02, PP-D11-03, PP-D11-04, PP-D11-05, PP-D11-06, PP-D11-07, PP-D11-08, PP-D11-09, PP-D11-10, PP-D11-11, PP-D11-12, PP-D11-13, PP-D11-14]
priority: normal
domain: D11
section: D11-07
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 843
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-07 Profitability Pain-Point Register

| Pain Point ID | 문제 | 공개 근거·징후 | 내부 확인 KPI | 우선순위 |
|---|---|---|---|---|
| `PP-D11-01` | 보고이익과 반복이익 혼합 | 2026 Q2 고객보상·IRA Credit 증가 | recurring EBIT/kWh, one-off bridge | P0 |
| `PP-D11-02` | Segment와 연결법인 범위 혼합 | 2025 Q2·Q3 서로 다른 손익 방향 | scope reconciliation error | P0 |
| `PP-D11-03` | 명목 Capacity와 합격 판매량의 괴리 | 고객 재고조정·낮은 가동률로 손실 변동 | accepted/nameplate GWh | P0 |
| `PP-D11-04` | 공장·제품·고객별 실제 Margin 불투명 | 공개자료에 세부원가 미공개 | margin coverage, close latency | P0 |
| `PP-D11-05` | 가동률 하락의 고정비 증폭 | 2025 Q4 낮은 가동률과 손실 확대 | fixed cost absorption/kWh | P0 |
| `PP-D11-06` | Yield 손실이 재료·Capacity·Margin에 분산 | 고가 소재와 다단 공정 | COPQ, lost good kWh, scrap value | P0 |
| `PP-D11-07` | AMPC 인식·현금·적격성 혼동 | 45X는 생산·판매·귀속·증빙 요건 존재 | eligible/claimed/recognized/cash | P0 |
| `PP-D11-08` | 고객보상과 계약가격의 경제성 혼동 | Q2 보상액 비공개 | compensation reason/repeatability | P0 |
| `PP-D11-09` | Metal·FX 연동 시차로 견적 Margin 누수 | 원료·환율·재고의 기간 불일치 | pass-through lag, margin-at-risk | P1 |
| `PP-D11-10` | Customer-specific Cost-to-Serve 누락 | 긴급물류·품질지원·ECR·Warranty | CTS/kWh by program | P0 |
| `PP-D11-11` | EV→ESS 전환의 Opportunity Cost 불완전 | 경쟁사·SK온의 자산 전환 확대 | conversion NPV, delay cost | P0 |
| `PP-D11-12` | 재고와 Program 변경이 현금·손상으로 지연 반영 | 2025 약 4.2조원 손상 | slow-moving inventory, impairment trigger | P0 |
| `PP-D11-13` | 에너지 비용이 생산량 기준으로만 관리 | Dry room·Formation의 고정/변동부하 | energy/accepted kWh, peak charge | P1 |
| `PP-D11-14` | 개선과제 절감액의 중복 계상 | 수율·가동률·에너지 효과 상호중첩 | benefit overlap, realized cash | P1 |

### 핵심 해석

SK온의 공개 손익 변동은 단순 판매량만으로 설명되지 않는다. 가동률, 미국 생산 Credit, 고객보상, 공장 재편과 자산손상이 같은 기간에 작용한다. 따라서 D17은 `원가절감 아이디어 목록`이 아니라 **어떤 합격 kWh에서 어떤 원인이 얼마의 반복 Margin과 현금을 바꾸었는지 증명하는 폐쇄루프**를 우선해야 한다.

---
