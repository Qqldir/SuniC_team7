---
id: skon-d14-d14-00-domain-boundary
title: Domain Boundary
summary: "규제·정책·인센티브가 특정 법인·제품·거래에 부과하는 의무와 혜택을 판정하는 기준, 범위, 원칙을 정의하는 D14 도메인 개요."
tags: [d14, policy, core-candidate, table, "xref:d13", "xref:d17", "xref:d00", "xref:d03"]
keywords: [정책·규제, 세액공제, 보조금, 적격성판정, 30D·45X·48E, CBAM, 배터리규정, 투자지원, 의무·혜택, 컴플라이언스, 정책의무, 미국30D·45X·48E, EU배터리규정, 인센티브, Clawback, UFLPA]
related: []
priority: critical
domain: D14
section: D14-00
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 1197
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

# SK온 D14 — Policy, Regulation, Incentives & Compliance

- 문서 버전: **v1.0.1**
- 기준일: **2026-08-03 (KST)**
- 이전 완료 지점: `D13 Contracts, Joint Ventures, Governance & Partnership Structure v1.0`
- 작성 방식: **실무형 요약 DB** — 법령·행정지침·제안·기업발표·분석값을 분리하고, 공개되지 않은 SK온의 실제 세액공제·지원금·Clawback 금액을 추정하지 않음
- 상위 목적: 국가·법인·공장·제품·원료·거래별 정책 의무와 경제효과를 증빙에 연결하고 D17 O/I 과제로 전달
- D00 통합검수: Domain-local Source/Entity ID를 보존하고 Canonical Alias는 D00 Crosswalk로 해석한다. 법정 기준일·위임법령·실제 적격성·신고·현금은 D00 Time·Status Standard로 분리한다.

---

## D14-00 Domain Boundary

### 1. 도메인 정의

D14는 규제 뉴스나 보조금 목록이 아니다. 정책 문구를 다음 의사결정 흐름으로 바꾸는 도메인이다.

```text
Jurisdiction / Authority / Legal Instrument / Version
→ Effective Date / Transition / Eligibility / Prohibition / Reporting Duty
→ Legal Entity / Facility / Line / Product / Material / Shipment / Customer Program
→ Required Evidence / Calculation / Certification / Third-party Verification
→ Credit / Grant / Tariff / Penalty / Clawback / Market-access Effect
→ Product Allocation / Sourcing / Contract / CAPEX / Pricing Decision
→ Monitoring / Audit / Remediation / Appeal
→ D17 Open-Innovation Seed
```

핵심 관리단위는 `규제 이름`이 아니라 **특정 시점에 특정 법인·제품·거래에 적용되는 의무 또는 혜택과 그 판정 증빙**이다.

### 2. 포함·제외 범위

| 포함 | 제외 또는 다른 도메인 원본 |
|---|---|
| 미국 30D·45X·48E·PFE/MACR·UFLPA·Section 301 | 제품·공정·공장 원본은 D03·D06·D07 |
| EU 배터리 규정, Passport, 탄소발자국, 재생원료, 실사 | 원료 Lot·원산지·Mass Balance 원본은 D08 |
| 주정부·EU·한국 투자지원·세액공제·Covenant·Clawback | CAPEX·자금·현금 원본은 D12 |
| CBAM·관세·원산지·수입통관·화학물질 규제 | 공급계약·Change-in-law 조항은 D13 |
| 법령 Version·시행일·적용범위·증빙·책임자·Audit | 전사 Risk·보험·위기대응 원본은 D15 |
| RegTech·TaxTech·DPP·LCA·Traceability O/I 후보 | 외부 Solution 기업 원장은 D16 |

### 3. 판정 원칙

1. `법률 제정`, `시행`, `세부규칙 확정`, `기업 적용`, `현금 수령`을 분리한다.
2. 세액공제율·지원한도에 생산능력이나 발표투자액을 곱해 실제 수혜액으로 만들지 않는다.
3. 법인·공장·Line·제품·판매시점·납세자·거래형태가 다르면 별도 적격성 판정을 한다.
4. 미국 30D, 45X, 48E와 관세·UFLPA는 서로 대체하거나 통합할 수 없는 별도 제도다.
5. PFE는 회사 국적 하나가 아니라 소유·통제·부채·계약권리·공급원가를 함께 검토한다.
6. EU 배터리 규정의 고정일과 `위임·시행법 발효 후 N개월 중 늦은 날`을 분리한다.
7. CBAM은 완성 배터리라는 이유만으로 자동 적용하지 않고 CN Code와 Annex 범위로 판정한다.
8. PFAS 제한안과 미국 NMP TSCA 규칙은 기준일 현재 절차상 상태를 보존하며 확정 금지로 쓰지 않는다.
9. AI 판정은 Tax·Legal·Trade Compliance·EHS의 승인 전 신고·인증·통관·계약변경에 사용하지 않는다.
10. D14의 O/I 점수는 D17 선별용 분석값이며 SK온의 공식 법률·세무 판단이 아니다.

---
