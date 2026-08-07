---
id: skon-d11-d11-11-source-registry
title: Source Registry
summary: 배터리 원가·수익성 분석에 사용되는 공식 자료들을 신뢰도 등급(S1A/S1B)으로 분류한 17개 정보 출처 레지스트리.
tags: [d11, cost, table]
keywords: [배터리 원가, 비용 벤치마크, IRS Section 45X, Argonne BatPaC, SK Innovation 실적, 제조 원가, AMPC, 수익성, 정부 규정, 데이터 소스, 원가분석, 배터리, IRS, DOE, 출처등급, 비용벤치마크, 공급망정책, 신뢰도]
related: [SRC-D11-001, SRC-D11-002, SRC-D11-003, SRC-D11-004, SRC-D11-005, SRC-D11-006, SRC-D11-007, SRC-D11-008, SRC-D11-009, SRC-D11-010, SRC-D11-011, SRC-D11-012, SRC-D11-013, SRC-D11-014, SRC-D11-015, SRC-D11-016, SRC-D11-017]
priority: normal
domain: D11
section: D11-11
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1017
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-11 Source Registry

| Source ID | 등급 | 출처 | 사용 범위 |
|---|---|---|---|
| `SRC-D11-001` | S1B | [SK Innovation 2025 Q1 Results](https://askinno.com/global/archives/21145) | Battery Q1 매출·손실·가동률 방향 |
| `SRC-D11-002` | S1B | [SK Innovation 2025 Q2 Results](https://askinno.com/global/archives/21825) | Battery Q2 손익·AMPC·Segment/통합범위 |
| `SRC-D11-003` | S1B | [SK Innovation 2025 Q3 Results](https://askinno.com/global/archives/22126) | Q3 손익·AMPC·통합법인 Scope |
| `SRC-D11-004` | S1B | [SK Innovation 2025 Q4 & FY Results](https://askinno.com/global/archives/153922) | 연간·Q4 손익·AMPC·손상·현금·전략 |
| `SRC-D11-005` | S1B | [SK Innovation 2026 Q1 Results](https://askinno.com/global/archives/154570) | Q1 매출·손실·수요회복 |
| `SRC-D11-006` | S1B | [SK Innovation 2026 Q2 Results](https://askinno.com/global/archives/156625) | Q2 흑자·고객보상·Credit·원가절감 |
| `SRC-D11-007` | S1A | [IRS Section 45X Final Regulations](https://www.irs.gov/irb/2024-51_IRB) | Cell/Module Credit율·생산·판매·귀속 요건 |
| `SRC-D11-008` | S1A | [IRS Notice 2026-15](https://www.irs.gov/pub/irs-drop/n-26-15.pdf) | 2026 적격·공급망 관련 정책판정 연결 |
| `SRC-D11-009` | S1A | [Argonne BatPaC](https://www.anl.gov/partnerships/batpac-battery-manufacturing-cost-estimation) | Bottom-up Battery Cost Model |
| `SRC-D11-010` | S1A | [Argonne BatPaC Manual](https://publications.anl.gov/anlpubs/2022/07/176234.pdf) | 공정·생산규모·설계 Cost 구조 |
| `SRC-D11-011` | S1A | [DOE 2023 EV Battery Pack Cost Estimate](https://www.energy.gov/cmei/vehicles/articles/fotw-1354-august-5-2024-electric-vehicle-battery-pack-costs-light-duty) | 외부 Cost Benchmark의 범위·규모 조건 |
| `SRC-D11-012` | S1A | [DOE Transformative Battery Manufacturing](https://www.energy.gov/cmei/ammto/funding-selections-platform-technologies-transformative-battery-manufacturing) | ML In-line QC·Sensor·Digital Thread 사례 |
| `SRC-D11-013` | S1A | [DOE Better Plants Program](https://betterbuildingssolutioncenter.energy.gov/better-plants/about) | 산업 Energy Intensity·Cost Saving Framework |
| `SRC-D11-014` | S1B | [BMW Virtual Factory](https://www.press.bmwgroup.com/global/article/detail/T0450699EN/bmw-group-scales-virtual-factory?language=en) | 30개 이상 공장·계획비용 최대 30% 절감 전망 |
| `SRC-D11-015` | S1B | [CATL 2025 Annual Report Release](https://www.catl.com/en/news/6773.html) | 매출·이익·현금·판매량·Capacity·R&D |
| `SRC-D11-016` | S1B | [Samsung SDI 2025 Results](https://news.samsungsdi.com/global/articleView?seq=370) | 적자·ESS Mix·AMPC·고객보상 사례 |
| `SRC-D11-017` | S1B | [Samsung SDI 2026 Q2 Results](https://news.samsungsdi.com/global/press/view?seq=440) | Battery 흑자·Mix·AMPC·관세환급 사례 |

### Source Quality Rule

- `S1A`: 정부·국책연구소·규제기관의 법령·공식모델·보고서
- `S1B`: 당사자 공식 실적발표·연차보고서·공식 사례
- 기업 발표의 비용절감률과 시장지위는 `COMPANY_CLAIM`으로 유지한다.
- 단순 산술값은 산식과 원본 Source ID를 함께 저장하고 공시값으로 승격하지 않는다.
- 공개자료로 산출할 수 없는 제품·공장·고객 Margin은 `NOT_DISCLOSED` 또는 `NOT_CALCULABLE_FROM_PUBLIC_DATA`로 둔다.

---
