---
id: skon-d17-d17-03-100-point-pre-screening-hard-gates
title: 100-Point Pre-screening & Hard Gates
summary: AI 사업화 과제의 사전심사 100점 평가 기준(8개 평가축)과 Tier별 처리 방안 및 중단 조건
tags: [d17, oi-portfolio, table]
keywords: [AI과제평가, 심사기준, 절대중단기준, Tier판정, Strategic Relevance, Data Readiness, PoC검증, 과제선별, 거버넌스, 기술검증, 평가 기준, 사전심사, Tier, PoC, Hard Gate, 중단 조건, 데이터 준비]
related: []
priority: normal
domain: D17
section: D17-03
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 715
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-03 100-Point Pre-screening & Hard Gates

### 1. 사전심사 점수

| 평가축 | 배점 | 핵심 질문 |
|---|---:|---|
| Strategic Relevance | 15 | 원가·제품·수주·안전·시장접근 중 핵심 경영문제를 직접 바꾸는가? |
| Quantified Value / Risk | 20 | KRW, accepted-kWh, Cash, Lead time, Recall Population 또는 Safety Risk로 측정 가능한가? |
| Evidence & Problem Proof | 15 | 문제·분모·기간·원인확신도와 Source Lineage가 있는가? |
| Data Readiness | 10 | 필수 Data와 Label·Genealogy·권한·품질이 준비됐는가? |
| External Capability | 10 | 명명된 Industrial/Battery Reference 또는 검증 가능한 Capability가 있는가? |
| Bounded PoC Feasibility | 10 | 3~9개월 안에 Control·Counterfactual과 함께 검증 가능한가? |
| Scale & Cross-domain Reuse | 10 | 다공장·다제품에 재사용 가능하며 기존 Architecture와 연결되는가? |
| Governance & Reversibility | 10 | Owner·Human Approval·Data/IP·Cyber·Exit·Rollback이 명확한가? |
| **합계** | **100** | 공개자료 기반 점수는 사전심사일 뿐 승인점수가 아니다. |

### 2. Tier

| Tier | 점수 | 처리 |
|---|---:|---|
| `P0` | 85~100 | G0·G1을 우선 착수. G2 이후는 내부 Evidence와 승인 필요 |
| `P1` | 75~84 | 선행조건·Data Gap을 닫은 뒤 PoC |
| `P2` | 60~74 | 기술실사·Option·Observe. 생산 적용 금지 |
| `HOLD/NO-GO` | 0~59 또는 Hard Gate 위반 | 이번 Cycle 중단 또는 재정의 |

### 3. Hard Gate

다음 중 하나라도 해당하면 점수와 무관하게 중단한다.

- 책임 있는 내부 Sponsor·Operator가 없음
- Baseline·분모·Scope 없이 Solution부터 제안됨
- 안전·품질 Release, Recall, 세무·통관·법률판정 또는 PLC Write를 AI가 단독 수행함
- 핵심 Recipe·Cell·BMS·계약 Data의 무제한 학습·재사용을 요구함
- Data Export·삭제·Rollback·Transition이 불가능함
- PFE·제재·수출통제·경쟁사 Conflict·IP 침해 위험이 미해결임
- Control Group 또는 합리적 Counterfactual 없이 편익을 주장함
- Vendor 자체평가만 있고 독립적인 품질·재무·법률·SHE 검증이 없음

---
