---
id: skon-d14-d14-03-united-states-tax-credit-architecture
title: United States Tax-Credit Architecture
summary: "미국 배터리 세액공제(30D·45X·48E) 정책의 종료일정, Cell·Module 계산기준, 적격요건과 Phase-out 일정을 정리한 문서로 SK온의 세액공제 수혜 조건을 설명한다."
tags: [d14, policy, table, "xref:d09", "xref:d11", "xref:d10"]
keywords: [45X, 48E, 배터리 세액공제, Qualified kWh, Phase-out, ESS, 미국 세제 인센티브, PFE, 적격성 기준, IRS 규정, 30D, 적격kWh, AMPC, 프로젝트경제성]
related: []
priority: normal
domain: D14
section: D14-03
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 927
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-03 United States Tax-Credit Architecture

### 1. 30D 종료와 수요모델 분리

| 구분 | 2026 기준 | D09~D11 연결 |
|---|---|---|
| 신규 Clean Vehicle Credit §30D | 2025-09-30 후 취득분 신규적용 종료 | OEM Forecast의 정책수요 Assumption 변경 |
| 중고차 §25E·상용차 §45W | 동일하게 2025-09-30 후 취득분 종료 | Fleet·Lease 수요 시나리오 변경 |
| 미국산 Cell/Module §45X | 생산·판매·적격요건 충족 시 유지 | 생산자별 Qualified kWh·반복 EBIT 분리 |
| ESS Project §48E | Project Taxpayer와 EST 적격성 기준 | ESS 고객의 Project Economics, SK온 수혜와 분리 |

30D 종료는 미국 내 Battery 생산 자체가 불필요해졌다는 뜻이 아니다. 고객의 차량수요·가격전가력에는 부정적 변수가 될 수 있지만, 45X 생산세액공제와 관세·PFE·현지조달 규정은 별도로 남는다. D10 수요 Scenario와 D11 반복이익은 각 정책의 전달경로를 분해해야 한다.

### 2. 45X Cell·Module 계산 경계

미국 45X 최종규칙상 Battery Cell은 기본적으로 `USD 35 × 적격 kWh`, Cell을 사용하는 Battery Module은 `USD 10 × 적격 kWh`다. Cell은 최소 에너지·에너지밀도 요건, Module은 정의·최소용량·최초 적격 Module 규칙, 양쪽 모두 용량측정과 생산·판매·납세자 요건을 충족해야 한다. ([IRS 45X Final Regulations](https://www.irs.gov/irb/2024-51_IRB))

```text
Announced Capacity
→ Actual Production
→ Completed Eligible Component
→ Qualified U.S. Taxpayer
→ Sale / Valid Related-person Election
→ Tested Eligible Capacity
→ PFE/MACR Pass
→ Return Filed / Credit Claimed
→ Accounting Recognition
→ Cash Monetization / Sharing / Adjustment
```

따라서 다음 산식은 내부 증빙이 없으면 금지한다.

```text
공장 명목 GWh × USD 35 또는 USD 45 = 실제 AMPC 수혜액
```

### 3. Phase-out와 Program Economics

현행 45X 최종규칙은 일반 Eligible Component에 대해 2030년 75%, 2031년 50%, 2032년 25%, 이후 0%의 Phase-out을 둔다. 적용 Critical Mineral은 해당 규칙의 예외지만, 2025년 이후 법 개정과 PFE 제한을 함께 검토해야 한다. Cell/Module Program의 Lifetime Margin은 `Credit-on` 기간과 `Credit-off` 기간을 별도 계산한다.

### 4. 48E ESS 전달경로

48E의 에너지저장기술은 일반적으로 5kWh 이상으로 에너지를 받아 저장하고 전달하는 자산을 포함한다. 그러나 Project Owner·Taxpayer·Placed-in-service·Construction·PFE Material Assistance가 적격성 단위이며, SK온의 Cell 납품이 곧 SK온의 48E Credit을 의미하지 않는다. 2025년 12월 31일 이후 Construction을 시작하는 EST에는 PFE 제한이 적용된다. ([IRS Notice 2026-15](https://www.irs.gov/pub/irs-drop/n-26-15.pdf))

---
