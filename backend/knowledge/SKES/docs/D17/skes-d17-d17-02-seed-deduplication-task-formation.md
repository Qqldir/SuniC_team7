---
id: skes-d17-d17-02-seed-deduplication-task-formation
title: Seed Deduplication & Task Formation
summary: "D17 과제에서 중복을 제거하는 8가지 기준, 단계별 형성 프로세스, 그리고 7가지 개입 형태별 통제 방식을 명시한 문서다."
tags: [d17, oi-portfolio, schema, table, "xref:d03", "xref:d16", "xref:d12"]
keywords: [중복 제거, Dedupe, 과제 형성, 오픈이노베이션, 개입 형태, 디지털 트윈, 데이터 모델, 경쟁력, TCO, 물리 위험]
related: [CO-DEVELOP]
priority: normal
domain: D17
section: D17-02
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 613
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-02 Seed Deduplication & Task Formation

## 1. Dedupe Key

```yaml
d17_dedupe_key:
  - verified_pain_failure_or_decision_gap
  - affected_business_asset_contract_customer
  - accountable_owner_and_operator
  - required_internal_data_and_granularity
  - intervention_or_required_capability
  - physical_and_financial_denominator
  - primary_KPI_and_guardrail
  - safety_legal_tax_cyber_gate
```

제목과 기술명이 달라도 위 항목이 실질적으로 같으면 하나의 D17 과제로 합친다. 반대로 같은 Digital Twin이라도 LNG Terminal과 LH2 Plant처럼 물리위험·Owner·데이터·안전 Gate가 다르면 별도 과제로 유지한다.

## 2. 과제 형성 흐름

```text
D03~D16 Raw Seed / Pain / Failure Mode
→ Evidence & Scope Normalization
→ Problem / Owner / Data / Denominator 기준 Dedupe
→ Required Capability 정의
→ Build · Buy · Co-develop · License · Partner · Invest · Observe 판정
→ Hard-Gate 검사
→ 100점 Pre-screen
→ Bounded PoC
→ Independent Value Validation
→ Scale · Re-negotiate · Internalize · Stop
→ G8 PIR / No-Go Memory
```

## 3. O/I 개입 형태

| Mode | 언제 쓰는가 | E&S의 핵심 통제 |
|---|---|---|
| `BUILD` | 핵심 의사결정·데이터 모델이 경쟁력이고 외부 의존을 줄여야 함 | 내부 Product Owner·Architecture |
| `BUY` | 성숙 상용기능이고 차별화보다 배포속도가 중요 | TCO·SLA·Export·EOL |
| `CO-DEVELOP` | E&S 물리/시장 Know-how와 외부 기술을 결합 | Background/Foreground IP·Model rights |
| `LICENSE` | 특허·공정·알고리즘 사용권이 핵심 | Field-of-use·개선권·종료 후 권리 |
| `PARTNER` | 데이터·시장·검증기관·OEM 공동작업 필요 | Data right·conflict·Liability |
| `INVEST` | 전략적 통제·장기 접근권이 필요하고 단순 구매로 부족 | D12 Finance Gate·Option/Exit |
| `OBSERVE` | 사업단계·데이터·규제가 이른 단계 | trigger 기반 재평가 |

---
