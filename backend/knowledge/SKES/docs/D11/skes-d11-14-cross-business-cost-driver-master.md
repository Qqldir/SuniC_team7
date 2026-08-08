---
id: skes-d11-14-cross-business-cost-driver-master
title: Cross-business Cost Driver Master
summary: "원가동인별 ID, 데이터 구성, 손익영향 영역, 중복방지 규칙을 한눈에 보는 마스터 테이블."
tags: [d11, cost, table]
keywords: [원가동인, 동인 ID 체계, 손익영향도, 운전자본, 중복방지규칙, 경영분석, 데이터 거버넌스, 비용구조]
related: []
priority: normal
domain: D11
section: 14
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 427
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# 14. Cross-business Cost Driver Master

| Driver Group | 대표 ID | 공통 데이터 | 주요 손익 | 중복방지 규칙 |
|---|---|---|---|---|
| Volume | D11-003·016·023·031·039·049·057·063 | plan·actual·paid | 고정비 흡수 | Volume uplift와 capacity release 중복 금지 |
| Price | D11-001·013·024·034·040·062 | index·contract·settlement | 매출·Margin | 시장가격과 계약정산 분리 |
| Efficiency | D11-008·015·019·042·050·056·064 | input/output | 변동원가 | 효율과 수율 절감 중복 금지 |
| Reliability | D11-017·032·045·052·058·068 | failure·downtime | Lost Margin | 가동률과 고장회피 편익 중복 금지 |
| Logistics | D11-005~007·059 | route·time·fee | 운송·재고 | 물류비와 재고현금 분리 |
| Contract | D11-004·010·036·061·071 | obligation·option·credit | 고정비·위험 | 명목권리와 실제사용 분리 |
| Market | D11-012~013·034·039~041 | price·spread·volatility | Revenue-at-Risk | Gross revenue와 risk-adjusted uplift 분리 |
| Quality/Safety | D11-011·026~027·048·052·058·066 | spec·event·expected loss | Claim·중단 | 예방편익과 보험회수 분리 |
| Carbon/Policy | D11-021·037·062·069 | eligibility·price·MRV | 비용·지원 | Gross 지원과 현금수취 분리 |
| Working Capital | 재고·채권·담보 | balance·days·rate | Cash·금융비 | P&L 절감과 Cash release 분리 |

---
