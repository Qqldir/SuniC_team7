---
id: skes-d17-d17-09-dependency-graph-readiness-rules
title: Dependency Graph & Readiness Rules
summary: 포트폴리오 60개 과제의 선행/후속 의존관계 매트릭스와 DISCOVERED부터 SCALE_READY까지 11단계 준비상태 진행 기준
tags: [d17, oi-portfolio, table]
keywords: [의존성, 포트폴리오, 준비상태, 선행과제, 후속과제, LNG·재생·수소·CCS, Gate·Benefit·Evidence, 권리확인, 베이스라인]
related: []
priority: normal
domain: D17
section: D17-09
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 411
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-09 Dependency Graph & Readiness Rules

## 1. 핵심 Dependency

| 선행기반 | 의존 과제 | 이유 |
|---|---|---|
| 001·002·003 | 전체 60개 | Portfolio·Evidence·Gate·Benefit 공통 기반 |
| 004 | 008·011·012·015·021·026·027·031·036·038·041·043·056 | 외부솔루션 비교·Data/IP 통제 |
| 006·007 | 008·009·010·011·013·046 | LNG 물량·권리·비용·발전 연결 |
| 011·012 | 014·015·046 | 발전 baseline·asset/equipment thread |
| 016 | 017·018·019·020 | city-gas canonical network/entity |
| 021·022 | 023·024·025 | 재생 actual/loss/contract lineage |
| 026·028 | 029·030·047 | KCE 운영경제성·market/tax case |
| 032·033 | 034·035 | 충전 Site 전력·Unit economics |
| 036·037 | 038·039·040·050 | H2 safety·mass/economic truth |
| 041·042 | 043·044 | CCS firm volume·storage/MMV 기반 |
| 048 | 046·047·049·050·053 | rule/effective-date freshness |
| 051·052 | 053·054·055 | 계약/프로젝트/현금·권리 기반 |
| 056·057 | OT 연결되는 전체 Live PoC | asset/zone/cyber/safety boundary |

## 2. Readiness State

```text
DISCOVERED
→ PROBLEM_PROVEN
→ OWNER_CONFIRMED
→ DATA_MAPPED
→ RIGHTS_CONFIRMED
→ GATES_CLEARED
→ REPLAY_READY
→ SHADOW_READY
→ BOUNDED_LIVE_READY
→ INDEPENDENTLY_VALIDATED
→ SCALE_READY
→ SCALED | STOPPED | OBSERVE
```

AI는 선행상태가 없을 때 후속 과제를 `READY`로 표시하지 않는다.

---
