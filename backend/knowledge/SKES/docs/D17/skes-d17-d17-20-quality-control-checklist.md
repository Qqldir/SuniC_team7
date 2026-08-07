---
id: skes-d17-d17-20-quality-control-checklist
title: Quality-Control Checklist
summary: 에너지 사업 포트폴리오 과제를 포트폴리오·근거·경제성·거버넌스·AI 5가지 관점에서 검증하는 기준
tags: [d17, oi-portfolio, "xref:d01", "xref:d12", "xref:d13", "xref:d14"]
keywords: [포트폴리오, 품질 검증, 경제성, 근거 검증, 거버넌스, 리스크, LNG, BESS, 게이트, AI/RAG]
related: []
priority: normal
domain: D17
section: D17-20
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 604
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-20 Quality-Control Checklist

## 1. Portfolio QC

- [x] 12개 Portfolio × 5개 = 60개 최종 과제
- [x] P0 20 / P1 24 / P2 16으로 분리
- [x] P0 20개에 Hypothesis·Scope·Owner·Capability·KPI·Guardrail·Gate 정의
- [x] P1/P2 40개에 READY 조건과 Hold/Kill 조건 정의
- [x] LNG·Power·City Gas·Renewable/PPA·BESS·EV·LH2·CCS·Policy·Finance/JV·OT를 모두 포함

## 2. Evidence QC

- [x] D01~D16을 Source lineage로 사용
- [x] 벤더 Claim과 외부 Customer Case를 E&S 실적으로 오인하지 않음
- [x] Dragon LNG 등 외부 절감/ROI 수치를 E&S 기대효과로 복사하지 않음
- [x] Public/External Signal을 E&S 내부 incident로 기록하지 않음
- [x] Rule effective date·future/cancelled/expired 상태를 D14에서 승계

## 3. Economics QC

- [x] LNG는 purchase price가 아닌 landed cost·right·demurrage·inventory를 포함
- [x] 발전은 heat rate→fuel→carbon→margin lineage 유지
- [x] BESS는 gross revenue와 degradation 포함 lifecycle margin을 분리
- [x] EV는 Port count가 아닌 Site/Port/Session/Paid kWh 경제성 사용
- [x] LH2는 produced kg가 아닌 sold/paid kg와 meter uncertainty 포함
- [x] CCS는 announced capacity가 아닌 firm volume·storage readiness·liability 분리
- [x] Benefit double-count 규칙 정의
- [x] Finance 검증 전 realized saving으로 표시하지 않음

## 4. Governance / Safety QC

- [x] D12 Finance Gate 통합
- [x] D13 Contract/JV/Data-right Gate 통합
- [x] D14 Compliance/Tax Gate 통합
- [x] D15 Risk/Safety/BCP Gate 통합
- [x] D16 Vendor/Evidence/Cyber Gate 통합
- [x] OT write·SIS/ESD·bid·legal/tax·CAPEX·contract Human approval 유지
- [x] Rollback·Exit·Data export·EOL 고려

## 5. AI/RAG QC

- [x] Canonical task schema 정의
- [x] Source/state/version/effective-date 필드 포함
- [x] Dedupe key 정의
- [x] Dependency rule 정의
- [x] BLOCKED_BY_FOUNDATION 논리 정의
- [x] G0~G8 학습 루프 정의
- [x] No-Go Memory/PIR 포함

---
