---
id: skon-d01-14-기업문화-및-조직-운영-단서
title: 기업문화 및 조직 운영 단서
summary: "SK온의 조직문화, One Team 협업 원칙, 핵심 엔티티 ID, 관계 데이터를 정의한 문서로 CEO Recognition 제도와 우수성과를 중심으로 설명한다."
tags: [d01, identity]
keywords: [One Team, CEO Recognition, 법인구조, 엔티티 ID, SK Innovation, Collaboration, Manufacturing Excellence, SKMS, 조직 운영 원칙, 협업, 엔티티 식별, COMP/ORG/SITE ID, 관계 데이터, 배터리]
related: []
priority: normal
domain: D01
section: 14
source: SK온_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 749
updated: 2026-08-03
---

> SK온 · D01 기업 기본정보·법인구조·연혁

# 14. 기업문화 및 조직 운영 단서

SK온은 2023년부터 `CEO Recognition` 제도를 운영하며, 도전적 과제를 통해 성과를 낸 팀과 협업에 기여한 개인을 시상하고 있다. 2025년에는 미국 조지아 공장 생산성 향상, 헝가리 공장 가동률 개선, AI 기반 제조지능화, ESS 공급계약 등이 주요 우수성과로 선정됐다. ([ASK Inno][10])

통합 SK온의 2025년 타운홀에서는 서로 다른 사업조직이 하나의 법인에 결합된 만큼 `One Team` 협업이 핵심 조직운영 원칙으로 강조됐다. 이는 배터리, 트레이딩, 윤활기유·에너지효율화 조직 간 협력 필요성을 공식적으로 보여준다. ([ASK Inno][4])

### 조직문화 키워드

```text
One Team
Collaboration
Execution
Customer Orientation
Manufacturing Excellence
Recognition
Challenge
AI Transformation
Global Coordination
```

---

# 15. Corporate Identity 핵심 엔티티

## 15.1 Company Entities

```text
COMP-SKON-001       SK On Co., Ltd.
COMP-SKI-001        SK Innovation Co., Ltd.
COMP-SKINC-001      SK Inc.
CIC-SKON-TI-001     SK On Trading International CIC
CIC-SKON-ENMOVE-001 SK Enmove CIC
```

## 15.2 Organization Entities

```text
ORG-SKON-BATTERY
ORG-SKON-MANUFACTURING
ORG-SKON-OPERATIONS
ORG-SKON-RND
ORG-SKON-GLOBAL
ORG-SKON-ESS
ORG-SKON-TRADING
ORG-SKON-ENMOVE
```

## 15.3 Site Entities

```text
SITE-SKON-KR-SEOUL-001
SITE-SKON-KR-DAEJEON-001
SITE-SKON-KR-SEOSAN-001
SITE-SKON-US-GA-001
SITE-SKON-US-TN-001
SITE-SKON-HU-KOMAROM-001
SITE-SKON-HU-IVANCSA-001
SITE-SKON-CN-001
```

위 해외 Site ID는 식별을 위한 상위 레코드이며, 정확한 법인명·주소·소유구조·가동상태는 D07에서 공식자료를 재검증한 후 확정한다.

---

# 16. 핵심 관계 데이터

```text
SK_ON — SUBSIDIARY_OF → SK_INNOVATION
SK_INNOVATION — MEMBER_OF → SK_GROUP
SK_ON — PRECEDED_BY → SK_INNOVATION_BATTERY_BUSINESS
SK_ON — ESTABLISHED_ON → 2021-10-01
SK_ON — OPERATES_BUSINESS → BATTERY
SK_ON — OPERATES_CIC → SK_ON_TRADING_INTERNATIONAL
SK_ON — OPERATES_CIC → SK_ENMOVE
SK_ON — OPERATES_SITE → SEOUL_GWANHUN
SK_ON — OPERATES_RND_SITE → DAEJEON_FUTURE_TECH_INSTITUTE
SK_ON — OPERATES_MANUFACTURING_SITE → SEOSAN
SK_ON — APPLIES → SKMS
SK_ON — PURSUES → TECHNOLOGY_LEADERSHIP
SK_ON — PURSUES → CUSTOMER_TRUST
SK_ON — PURSUES → FINANCIAL_STABILITY
SK_ON — TARGETS → GLOBAL_BATTERY_MARKET
```

---
