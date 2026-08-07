---
id: skon-d14-d14-02-public-policy-compliance-event-register
title: Public Policy & Compliance Event Register
summary: "에너지·배터리 규제 및 세액인센티브에 관한 미국·EU·한국의 현황과 시행 상태를 정리하고, 2025년 이후 정책 변화·적용 시점을 설명하는 규제 이력 및 일정표"
tags: [d14, policy, table]
keywords: [IRA, 30D, 45X, 배터리규정, 세액공제, CBAM, 원산지, 강제노동, 탄소발자국, 규제준수, 배터리규제, 공급망추적, ESS, Battery Passport, 인센티브]
related: [REG-D14-US-30D, REG-D14-US-45X, REG-D14-US-48E, REG-D14-US-PFE, REG-D14-US-301, REG-D14-US-UFLPA, REG-D14-EU-BATT, REG-D14-EU-PASS, REG-D14-EU-DD, REG-D14-EU-CF, REG-D14-EU-RC, REG-D14-EU-CBAM, REG-D14-CHEM, REG-D14-KR-TAX]
priority: normal
domain: D14
section: D14-02
source: SK온_D14_Policy_Regulation_Incentives_Compliance.md
breadcrumb: "SK온 D14 — Policy, Regulation, Incentives & Compliance"
tokens: 1181
updated: 2026-08-03
---

> SK온 · D14 정책·규제·인센티브·컴플라이언스 · SK온 D14 — Policy, Regulation, Incentives & Compliance

## D14-02 Public Policy & Compliance Event Register

| ID | 관할·제도 | 기준일 상태 | SK온 관련 단위 | 핵심 통제 |
|---|---|---|---|---|
| `REG-D14-US-30D` | 미국 New Clean Vehicle Credit §30D | `TERMINATED_WITH_TRANSITION` | OEM 차량 취득시점 | 2025-09-30 후 취득 차량 신규공제 불가; 기존 경과거래 분리 |
| `REG-D14-US-45X` | 미국 Advanced Manufacturing Production Credit | `ENACTED_EFFECTIVE_WITH_PFE_RULE` | 미국 납세법인·Cell/Module·판매 | Qualified production·sale·capacity·taxpayer·PFE MACR 증빙 |
| `REG-D14-US-48E` | 미국 Clean Electricity Investment Credit | `ENACTED_EFFECTIVE_WITH_PFE_RULE` | ESS Project Owner/Taxpayer | SK온 Cell 공급과 Project Taxpayer 적격성 분리 |
| `REG-D14-US-PFE` | OBBBA PFE·Material Assistance | `GUIDANCE_OR_SAFE_HARBOR` | 법인·시설·원재료·기술계약 | 소유·통제·계약·직접재료원가·Certification |
| `REG-D14-US-301` | 대중 Section 301 관세 | `ENACTED_EFFECTIVE` | 중국산 특정 HTSUS 품목 | 품목분류·원산지·시행연도·Exclusion 분리 |
| `REG-D14-US-UFLPA` | 강제노동 수입금지·CBP 추적 | `ENACTED_EFFECTIVE` | 미국 수입 Shipment·Upstream | 광산~정련~소재~Cell Chain of Custody와 통관 Pack |
| `REG-D14-EU-BATT` | EU Regulation 2023/1542 | `ENACTED_PHASED` | EU 시장 EV·산업용 Battery | 제품·모델·공장별 Conformity·Label·Data·Waste 의무 |
| `REG-D14-EU-PASS` | EU Battery Passport·QR | `ENACTED_FUTURE_EFFECTIVE` | EV Battery, 산업용 >2kWh | 2027-02-18 개별 Battery Record·접근권한·Lineage |
| `REG-D14-EU-DD` | EU Battery Due Diligence | `ENACTED_FUTURE_EFFECTIVE` | EU 시장출시 Economic Operator | 2027-08-18, 제3자 검증·10년 기록·Upstream Risk |
| `REG-D14-EU-CF` | EU Battery Carbon Footprint | `EFFECTIVE_CONDITIONAL_ON_SECONDARY_ACT` | 모델·공장별 EV/산업용 Battery | 법정 Base Date와 위임법 발효 후 기간 중 늦은 날 |
| `REG-D14-EU-RC` | EU Recycled Content | `ENACTED_PHASED` | 모델·공장별 Co/Li/Ni/Pb | 2028 Disclosure·2031 최소비율, 위임법 조건 추적 |
| `REG-D14-EU-CBAM` | EU CBAM | `ENACTED_EFFECTIVE` | Annex I CN Code 수입품 | 완성 Battery 자동적용 금지; Aluminum 등 Scope 판정 |
| `REG-D14-CHEM` | EU PFAS·미국 NMP | `PROPOSED_OR_CONSULTATION` | Binder·Coating·Solvent·작업장 | 확정 의무와 대체기술 준비를 분리 |
| `REG-D14-KR-TAX` | 한국 국가전략기술 R&D·투자세액공제 | `ENACTED_EFFECTIVE` | 국내 법인·기술·사업화시설 | 기술목록·시설목록·취득시점·증빙별 적격 판정 |

### 핵심 변화

미국의 소비자·차량단 30D는 2025년 9월 30일 이후 취득 차량에 대해 종료됐다. 그러나 미국 내 생산자에게 적용되는 45X는 별도 제도로 유지되며, 2025년 7월 4일 이후 시작되는 과세연도부터 PFE Material Assistance 제한이 작동한다. 따라서 `IRA 적격 차량`이라는 과거 단일 Flag로 SK온의 2026년 정책효과를 설명할 수 없다. ([IRS Clean Vehicle FAQ](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb), [IRS Notice 2026-15](https://www.irs.gov/pub/irs-drop/n-26-15.pdf))

EU도 `2027년부터 모두 시행`이 아니다. Passport는 2027년 2월 18일, Battery Due Diligence는 개정 후 2027년 8월 18일이며, 탄소발자국·재생원료 세부 의무는 위임·시행법 발효일에 따라 실제 적용일이 뒤로 이동할 수 있다. ([EU Consolidated Batteries Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02023R1542-20250731))

---
