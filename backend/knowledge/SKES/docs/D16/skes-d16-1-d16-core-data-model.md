---
id: skes-d16-1-d16-core-data-model
title: D16 Core Data Model
summary: 외부 기술·솔루션 평가의 표준 데이터 모델과 기술 성숙도 검증 단계(L0~L6)를 정의한 SK E&S의 평가 프레임워크이다.
tags: [d16, ecosystem, schema, table]
keywords: [기술 성숙도, 솔루션 평가, 벤더 선별, 기술검증, L0~L6 단계, 배포형, cyber_gate, 사업적합성, 구현비용, 실증]
related: []
priority: normal
domain: D16
section: 1
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 417
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 1. D16 Core Data Model

## 1.1 Canonical Solution Record

```yaml
solution_id: SOL-ENS-D16-XXXX
technology_id: TECH-ENS-D16-XXXX
vendor_id: VEN-ENS-D16-XXXX
product: string
use_case: string
business_fit: [LNG, POWER, CITY_GAS, RENEWABLE, BESS, EV, H2, CCS, ENTERPRISE]
maturity: COMMERCIAL|DEPLOYED_CASE|PILOT|DEMO|R&D
evidence_state: E1_STANDARD|E2_CUSTOMER_CASE|E3_PRODUCT_CONFIRMED|E4_VENDOR_CLAIM|E5_HYPOTHESIS
evidence_ids: []
inputs: []
outputs: []
integration: []
deployment: edge|on_prem|cloud|hybrid|unknown
safety_criticality: low|medium|high
cyber_gate: string
vendor_lockin: qualitative
expected_value_driver: string
effect_value: INTERNAL_REQUIRED
implementation_cost: INTERNAL_REQUIRED
fit_score: screening_only
d15_links: []
d17_seed_ids: []
```

## 1.2 Maturity Gate

| 단계 | 통과조건 | 금지 해석 |
|---|---|---|
| L0 Watch | 기술원리·벤더 존재 | E&S 적용가능 확정 |
| L1 Product | 상용 제품·서비스 확인 | ROI 확정 |
| L2 Case | 고객·자산·활용이 공개 | E&S에서도 같은 효과 |
| L3 Bench | 샘플 E&S 데이터 offline 재현 | 운영효과 확정 |
| L4 Shadow | 운영데이터 실시간 read-only 검증 | 자동제어 승인 |
| L5 Bounded PoC | 제한 자산·기간·KPI 실증 | 전사 확대 승인 |
| L6 Scale | 보안·경제성·운영표준·지원체계 검증 | 영구 vendor lock-in 허용 |

---
