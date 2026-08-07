---
id: skon-d12-d12-00-domain-boundary
title: Domain Boundary
summary: "SK온의 투자·자금조달 관리에서 D12 도메인의 경계를 정의하고, CAPEX 승인부터 집행·회수·Exit까지 어떤 정보는 포함하며 어떤 정보는 다른 도메인에 위임하는지 포함·제외 표로 구분하는 문서."
tags: [d12, capex, core-candidate, table, "xref:d11", "xref:d17", "xref:d00", "xref:d07"]
keywords: [CAPEX, 투자승인, 자금조달, 귀속액, 현금부담, JV 투자, 정부지원, Greenfield, Exit, 투자, JV, ROIC, 의사결정, 손상]
related: []
priority: critical
domain: D12
section: D12-00
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 1298
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

# SK온 D12 — CAPEX, Investment, Funding & Financial Structure

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D11 Cost, Profitability & Business Economics v1.0`
- 작성 방식: **실무형 요약 DB** — 공개된 투자·재무·정책 사실을 보존하고, SK온 단독 수치와 SK이노베이션 연결 수치를 혼합하거나 비공개 투자분담을 추정하지 않음
- 상위 목적: 공장·제품·고객 Program별 투자와 자금조달을 수요·가동·현금·ROIC·중단조건에 연결하고 D17 O/I 과제로 전달
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. JV 총액·SK온 귀속액·승인한도·인출액·보증액을 D00 Scope Standard로 분리한다.

---

## D12-00 Domain Boundary

### 1. 도메인 정의

D12는 발표된 투자금액과 조달금액을 나열하는 재무자료가 아니다. 투자안의 최초 승인부터 집행·양산·현금회수·Exit까지를 같은 의사결정 단위로 연결한다.

```text
Customer Demand / Product Qualification / Policy Eligibility
→ CAPEX Option and Legal Ownership
→ Approval / Commitment / Purchase Order / Construction / Ramp
→ Equity / Debt / Grant / Tax Credit / Partner Contribution
→ Cost-to-Complete / Liquidity / Covenant / Guarantee Exposure
→ Accepted-kWh Cash Contribution / Risk-adjusted ROIC
→ Expand / Hold / Convert / Mothball / Exit Decision
→ D17 Open-Innovation Seed
```

핵심 관리단위는 `발표된 공장 총투자액`이 아니라 **법인·공장·Line·Program별 SK온 귀속 현금부담과 되돌릴 수 없는 집행액**이다. JV 총투자, 지분율, 실제 납입, 차입, 보증, 정부지원, 미집행 약정은 각각 분리한다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| Greenfield·Brownfield·전환·유지보수 CAPEX | 상세 공장·Capacity·Ramp 원본은 D07 |
| JV 총투자·지분·납입·차입·보증·지원약정 | 고객계약·Call-off·수주상태는 D09 |
| 모회사 증자·FI·PRS·사모·Green Finance·정책금융 | 반복 EBIT·제품별 Unit Economics는 D11 |
| 공사 진척·Cost-to-Complete·Contingency·Change Order | 상세 제조공정·설비 성능은 D06 |
| 보조금·Tax Credit·Clawback·고용·투자 Covenant | 정책 원문·적격성 판정은 D14 |
| NPV·IRR·ROIC·회수기간·Real Option·Exit Cost | 계약·JV Governance 원본은 D13 |
| 손상 Trigger·Liquidity·Guarantee Exposure | 전사 통합 Risk 원장은 D15 |
| 외부사례와 D17 O/I 후보 | 외부 후보기업·솔루션 원장은 D16 |

### 3. 판정 원칙

1. SK이노베이션 연결재무, Battery Segment, SK온 연결법인, 개별 자회사, JV 수치를 서로 다른 `scope_id`로 유지한다.
2. `announced total investment × ownership ratio`를 실제 납입액이나 SK온 확정부담으로 계산하지 않는다.
3. 대출 `approved/committed ceiling`, 실제 인출액, 회계상 차입금, 보증액과 상환액을 분리한다.
4. 정부지원은 `eligible`, `awarded`, `claimed`, `recognized`, `cash received`, `clawback exposure`로 분리한다.
5. 승인된 CAPEX와 발주·검수·지급·자산화된 CAPEX를 한 값으로 합치지 않는다.
6. 매몰비용은 투자 계속 여부의 근거로 사용하지 않고, 향후 증분현금흐름과 Exit Cost로 의사결정한다.
7. 내부 할인율·공장별 WACC·잔존가치·전환비용이 없으면 NPV나 IRR을 임의 산출하지 않는다.
8. PRS·전환우선주·영구채는 현금유입뿐 아니라 정산·상환·희석·파생손익 Exposure를 함께 저장한다.
9. 손상차손은 비현금 조정이지만 투자전제 붕괴의 후행신호로 보고, Stage Gate와 Early Warning에 환류한다.
10. D12의 점수·목표치는 D17 선별용 분석값이며 회사의 공식 KPI가 아니다.

---
