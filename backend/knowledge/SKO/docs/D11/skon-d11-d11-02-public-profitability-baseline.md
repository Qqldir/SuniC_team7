---
id: skon-d11-d11-02-public-profitability-baseline
title: Public Profitability Baseline
summary: "SK온의 Battery 세그먼트 분기별·연간 매출과 영업손익, AMPC 의존도, 그리고 세그먼트-연결법인 범위 차이를 보여주는 공개실적 기초자료"
tags: [d11, cost, table]
keywords: [Battery 세그먼트, 영업손익, AMPC, IRA 세액공제, 분기별 실적, 가동률, 손상차손, Segment Scope, 원가절감, Battery 실적, 45X Credit, 영업이익률]
related: []
priority: normal
domain: D11
section: D11-02
source: SK온_D11_Cost_Profitability_Business_Economics.md
breadcrumb: "SK온 D11 — Cost, Profitability & Business Economics"
tokens: 1429
updated: 2026-08-03
---

> SK온 · D11 원가·수익성·비즈니스 이코노믹스 · SK온 D11 — Cost, Profitability & Business Economics

## D11-02 Public Profitability Baseline

### 1. Battery 세그먼트 실적

| 기간 | 매출 | 영업손익 | 단순 영업이익률 | 공개된 주요 설명 | 상태 |
|---|---:|---:|---:|---|---|
| 2025 FY | 6.9782조원 | -0.9319조원 | -13.4% | 북미 수요·가동률 변동, Q4 AMPC 감소와 손실 확대 | `REPORTED` |
| 2025 Q1 | 1.6054조원 | -0.2993조원 | -18.6% | 북미 가동률·판매 확대 계획 | `REPORTED` |
| 2025 Q2 | 2.1077조원 | -0.0664조원 | -3.2% | 북미·유럽 가동률과 판매 증가, AMPC 2,734억원 | `REPORTED` |
| 2025 Q3 | 1.8079조원 | -0.1248조원 | -6.9% | AMPC 1,731억원; 통합 SK온 연결손익과 Segment 손익 범위 차이 존재 | `REPORTED` |
| 2025 Q4 | 1.4572조원 | -0.4414조원 | -30.3% | 북미 고객 재고조정·연말 Shutdown·낮은 가동률·AMPC 1,013억원 | `REPORTED` |
| 2026 Q1 | 1.7912조원 | -0.3492조원 | -19.5% | 북미 판매 소폭 증가, 유럽·아시아 수요 회복 | `REPORTED` |
| 2026 Q2 | 2.9460조원 | +0.8218조원 | +27.9% | 아시아 판매 확대·고객보상·IRA Credit 증가·원가절감 | `REPORTED` |

2025년 Battery 세그먼트는 연간 매출 6.98조원과 영업손실 9,319억원을 기록했다. 분기별로는 Q2에 손실이 크게 축소됐지만 Q4에 북미 고객 재고조정과 낮은 가동률, AMPC 감소가 겹치며 손실이 다시 확대됐다. ([SK Innovation 2025 Q1](https://askinno.com/global/archives/21145), [2025 Q2](https://askinno.com/global/archives/21825), [2025 Q3](https://askinno.com/global/archives/22126), [2025 Q4/FY](https://askinno.com/global/archives/153922))

2026년에는 Q1 영업손실 3,492억원에서 Q2 영업이익 8,218억원으로 1조1,710억원 개선됐다. 그러나 회사는 Q2 이익에 고객보상과 IRA 세액공제 증가가 포함됐다고 밝혔으며 각 금액은 공개하지 않았다. 따라서 Q2의 27.9% 보고 Margin을 정상화 Margin으로 간주할 수 없고, 반복 EBIT는 `NOT_CALCULABLE_FROM_PUBLIC_DATA`다. ([SK Innovation 2026 Q1](https://askinno.com/global/archives/154570), [2026 Q2](https://askinno.com/global/archives/156625))

### 2. AMPC 의존도 Proxy

| 지표 | 공개값·산식 | 판정 |
|---|---:|---|
| 2025 Q3 누적 AMPC | 6,173억원 | 회사 공개값 |
| 2025 Q4 AMPC | 1,013억원 | 회사 공개값 |
| 2025 연간 AMPC 단순 합계 | 7,186억원 | `Q3 누적 + Q4`, `DERIVED_FROM_REPORTED` |
| 2025 AMPC 제외 단순 영업손실 Proxy | -1조6,505억원 | `보고손실 - 단순 AMPC 합계`, 감사된 반복 EBIT 아님 |
| 2025 AMPC 제외 단순 Margin Proxy | -23.7% | 의존도 Stress Test이며 공식 Margin 아님 |

미국 45X 최종규정은 적격 Battery Cell에 kWh당 35달러, Cell을 사용하는 Battery Module에 kWh당 10달러의 Credit을 규정한다. 다만 실제 인식액은 미국 내 생산·판매, 적격 Component, Related-person Election, 계약상 귀속, 세무기간과 증빙에 좌우된다. 그러므로 `미국 생산 kWh × 35달러`를 곧바로 SK온의 확정이익으로 계산해서는 안 된다. ([IRS 45X Final Regulations](https://www.irs.gov/irb/2024-51_IRB))

### 3. Segment와 연결법인 Scope 충돌

2025 Q2 공시의 Battery 세그먼트 영업손실은 664억원이지만 회사는 당시 통합 SK온 법인이 609억원의 흑자를 기록했다고 별도로 설명했다. Q3에도 Battery 세그먼트 영업손실은 1,248억원인 반면 SK온·SK Trading International·SK Enterm을 포함한 연결법인은 179억원의 흑자로 제시됐다. 이는 모순이 아니라 **연결범위와 내부거래 제거 범위가 다른 값**이다. D11에서는 두 계열을 별도 `scope_id`로 유지한다.

### 4. 손상차손과 현금흐름

SK Innovation은 2025 Q4에 BlueOval SK 재편 등을 반영해 SK온 관련 약 4.2조원의 자산손상차손을 인식했다. 회사는 이를 현금흐름에 직접 영향을 주지 않는 일회성 회계조정으로 설명했다. 그러나 비현금이라는 이유로 경제적 의미가 사라지는 것은 아니다. 손상차손은 과거 투자에서 기대한 미래현금흐름이 낮아졌다는 신호이므로 D12의 CAPEX·ROIC 검토와 연결한다. ([SK Innovation 2025 Q4/FY](https://askinno.com/global/archives/153922))

---
