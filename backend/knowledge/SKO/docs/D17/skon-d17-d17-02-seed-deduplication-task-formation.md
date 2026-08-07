---
id: skon-d17-d17-02-seed-deduplication-task-formation
title: Seed Deduplication & Task Formation
summary: "오픈이노베이션 과제 포트폴리오에서 중복을 제거하고 과제를 형성하기 위한 6가지 중복제거키와 8단계 프로세스, 병합 금지 규칙을 제시한다."
tags: [d17, oi-portfolio, schema]
keywords: [오픈이노베이션, 중복제거, Seed Deduplication, 과제 형성, 의사결정자, Bounded PoC, 능력 정의, 규제 적격, Task Formation, 포트폴리오, 중복 제거, 문제점, 데이터 세분도, 능력 개발, 가치 검증]
related: []
priority: normal
domain: D17
section: D17-02
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 439
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-02 Seed Deduplication & Task Formation

### 1. 중복 제거 키

```yaml
dedupe_key:
  - verified_pain_point_or_failure_mode
  - affected_decision_and_accountable_owner
  - required_internal_data_and_granularity
  - intervention_or_required_capability
  - site_line_product_customer_supplier_period_scope
  - primary_KPI_and_guardrail
```

제목이 달라도 위 여섯 항목이 같으면 하나의 D17 과제로 합친다. 반대로 동일 기술이라도 의사결정자·데이터·위험이 다르면 분리한다.

### 2. 과제 형성 흐름

```text
Domain Seed
→ Evidence & Scope Normalization
→ Pain Point / Owner / Data 기준 중복 제거
→ Capability 정의
→ Build·Buy·Co-develop·License·Partner·Invest·Observe 판정
→ Bounded PoC
→ Independent Value Validation
→ Scale·Re-negotiate·Internalize·Stop
```

### 3. 금지되는 자동 병합

- `MOU`, `기술협력`, `Pilot`, `상용운영`, `다공장 확산`을 같은 실적으로 병합하지 않는다.
- JV 총설계 Capacity와 SK온 단독 통제 Capacity를 합산하지 않는다.
- Battery Segment 손익과 통합 SK온 또는 SK이노베이션 연결 손익을 섞지 않는다.
- 경쟁사·Provider가 주장한 ROI를 SK온 기대편익으로 복사하지 않는다.
- DPP, PFE/MACR, 45X, UFLPA, 관세, 탄소발자국을 `규제 적격` 한 칸으로 합치지 않는다.

---
