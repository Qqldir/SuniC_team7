---
id: skes-d12-0-domain-boundary
title: Domain Boundary
summary: D12 도메인이 투자금액 합산이 아니라 투자 생명주기 전체와 실제 순현금노출을 관리하는 범위·규칙·원칙을 정의하는 문서.
tags: [d12, capex, core-candidate, table, "xref:d02", "xref:d06", "xref:d07", "xref:d08"]
keywords: [CAPEX, 투자 생명주기, 순현금노출, 의사결정단위, 사용권 vs 소유, Project SPV, FID·COD, 현금흐름 추적, 자금조달, Hard Guardrail]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D12
section: 0
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 1701
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# SK이노베이션 E&S AI Knowledge Database

## D12. CAPEX, Investment, Funding & Financial Structure｜CAPEX·투자·자금조달·재무구조

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Investment namespace: `INV-ENS-D12-*`
- Funding namespace: `FUND-ENS-D12-*`
- Financial-risk namespace: `FRSK-ENS-D12-*`
- Pain-point namespace: `PAIN-ENS-D12-*`
- O/I Seed namespace: `SEED-ENS-D12-*`
- Data-request namespace: `DR-ENS-D12-*`
- Source namespace: `SRC-ENS-D12-*`
- 상속 도메인: `D02 Business Portfolio`, `D06 Process and Operations`, `D07 Footprint`, `D08 Supply Chain`, `D09 Customers`, `D10 Market Dynamics`, `D11 Business Economics`
- 작성 목적: E&S의 LNG·발전·도시가스·재생에너지/PPA·BESS·EV충전·수소·CCS 투자를 자산·법인·계약·현금·조달·위험 단위로 연결하고 D17에서 검증 가능한 O/I 과제로 전환

---

# 0. Domain Boundary

## 0.1 D12의 역할

D12는 기사에 나온 투자금액을 합산하는 문서가 아니다. 투자안의 발표부터 실제 자금집행·상업운전·회수·재투자·Exit까지를 동일한 의사결정 단위로 연결한다.

```text
Market / Customer / Regulation / Asset Need
→ Investment Case & Alternatives
→ Ownership / Contract Right / SPV Boundary
→ FID / Approval / Commitment / Construction / COD
→ Equity / Debt / PF / Grant / Tax Credit / Partner Contribution
→ Cash Paid / Cost-to-Complete / Working Capital / Debt Service
→ D11 Unit Economics / Risk-adjusted ROIC / Liquidity
→ Expand / Hold / Convert / Refinance / Sell / Exit
→ D17 O/I Opportunity
```

E&S의 핵심 관리단위는 `발표된 총 투자액`이 아니라 **법인·프로젝트·자산·계약별 실제 순현금노출과 되돌릴 수 없는 약정**이다.

## 0.2 Hard Guardrails

1. `SK그룹`, `SK이노베이션 연결`, `E&S 사업`, `E&S CIC`, `2024-11-01 이전 SK E&S`, `자회사`, `JV`, `Project SPV`를 별도 Scope로 유지한다.
2. 2024년 11월 1일 이전 SK E&S 자료는 역사적 법인의 당시 사실이며 현 E&S CIC의 동일 회계범위로 자동 승계하지 않는다.
3. `announced project cost × ownership ratio`를 실제 납입액으로 계산하지 않는다. 공식자료가 지분귀속 투자액을 직접 공개한 경우에만 별도 사실로 저장한다.
4. `승인한도`, `committed`, `drawn`, `paid`, `capitalized`, `outstanding`, `guaranteed`, `cost-to-complete`를 분리한다.
5. 소유자산과 사용권을 분리한다. 보령 LNG터미널 TUA와 Freeport liquefaction right를 자산 CAPEX로 재합산하지 않는다.
6. `MOU`, `개발 pipeline`, `우선협상`, `FID`, `착공`, `준공`, `COD`, `운영`, `매각`을 구분한다.
7. 보조금은 `eligible → awarded → claimed → recognized → cash received → clawback cleared` 상태를 분리한다.
8. Project Financing의 약정액을 Sponsor의 차입금이나 E&S의 실제 순현금부담으로 간주하지 않는다.
9. Non-recourse 표시는 프로젝트 SPV 대주단의 원칙적 상환재원 구조를 의미하며 모든 Sponsor support가 없다는 뜻으로 확장하지 않는다.
10. 공개되지 않은 WACC·IRR·NPV·DSCR·금리·PPA 가격·LNG 계약가격·Project EBITDA는 `NOT_DISCLOSED` 또는 `INTERNAL_REQUIRED`로 둔다.
11. 매몰비용이 아니라 `향후 증분현금흐름 + Exit/전환비용 + 옵션가치`로 계속투자 여부를 비교한다.
12. D12의 O/I 효과는 Finance 검증 전까지 `HYPOTHESIS`이며 자동 투자승인·차입·헤지·매각 판단에 사용하지 않는다.

## 0.3 포함 범위

| 포함 | D12 처리 |
|---|---|
| Greenfield/Brownfield CAPEX | 승인·발주·진척·지급·COD·Cost-to-complete |
| LNG upstream/liquefaction/terminal rights | 지분투자·사용권·계약약정 분리 |
| 발전·CHP | 유지보수/성능개선/신규개발 투자와 현금회수 |
| 재생에너지 | SPV 지분·PF·주민참여·PPA/REC cash-flow 연결 |
| BESS/EV charging | Project debt·ITC·장비·interconnection·portfolio capital |
| 수소 | 생산·충전·운송 투자, PF, 정부지원, 가동률 Ramp |
| CCS | Capture/transport/storage 투자와 FID·저장권·오프테이크 동시성 |
| 금융구조 | Equity, corporate debt, PF, lease, guarantee, grant, tax credit |
| 투자 후 관리 | impairment signal, refinancing, sell/hold/convert/exit |

## 0.4 다른 도메인으로 이관되는 원본

| 원본 | D12 사용 방식 |
|---|---|
| D06 공정·설비 태그 | CAPEX package의 효과·진척·성능검증에 조인 |
| D07 자산·용량·소유권 | Asset ID·COD·capacity 원본 유지 |
| D08 조달·EPC·물류 | 공급사·발주·lead time·change order 조인 |
| D09 고객·PPA·수요 | 확정수요와 투자규모 정합성 검증 |
| D10 가격·경쟁·정책 | Base/Downside/Severe scenario 입력 |
| D11 Unit Economics | 투자 후 현금기여·ROIC 검증 |
| D13 JV·계약 | Sponsor support·보증·Exit·governance clause 심화 |
| D14 규제·보조금 | 적격성·clawback 법적 판정 |
| D15 Risk | 재무·건설·정책 위험을 전사 Risk 원장으로 통합 |
| D16 외부사 | EPC·금융·FinTech·AI 후보 검증 |

---
