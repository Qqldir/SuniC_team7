---
id: skon-d13-d13-08-contract-governance-pain-point-register
title: Contract & Governance Pain-Point Register
summary: "SK온의 계약·거버넌스 분야 14개 주요 위험을 우선순위별로 등록한 문제 추적표로, 지분혼동·계약연동 미연결·IP권리 미구조화·운영지연 등을 모니터링한다."
tags: [d13, contract, table]
keywords: [계약위험, JV, 지분혼동, Reserved Matter, Milestone, IP권리, Amendment, 당사자속성, 의무추적, 계약 위험, 거버넌스, 지분구조, 지적재산권, Pain Point Register, Cross-agreement, 우선순위 관리]
related: [PP-D13-01, PP-D13-02, PP-D13-03, PP-D13-04, PP-D13-05, PP-D13-06, PP-D13-07, PP-D13-08, PP-D13-09, PP-D13-10, PP-D13-11, PP-D13-12, PP-D13-13, PP-D13-14]
priority: normal
domain: D13
section: D13-08
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 835
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-08 Contract & Governance Pain-Point Register

| Pain Point ID | 문제 | 공개 근거·징후 | 내부 확인 KPI | 우선순위 |
|---|---|---|---|---|
| `PP-D13-01` | 50:50 지분을 동일 통제·부담으로 오인 | HSBMA 공개지분, 상세 Governance 비공개 | reserved-matter coverage | P0 |
| `PP-D13-02` | 법적 당사자·운영회사·보증인·경제부담자 혼합 | BOSK–SKBA–SK On–SK Innovation–Ford 구조 | attribution completeness | P0 |
| `PP-D13-03` | MoU·본계약·Option·ROFO의 구속력 혼합 | Exxon·Ferrari·Flatiron | binding-status accuracy | P0 |
| `PP-D13-04` | 장기 총량과 Firm Call-off·Accepted Volume 혼합 | Nissan·Slate 계약 | contract-to-accepted bridge | P0 |
| `PP-D13-05` | JV 계약군과 공급·금융·지원계약의 상호의존 미연결 | BOSK Asset·Loan·Guarantee 이전 | cross-agreement coverage | P0 |
| `PP-D13-06` | Reserved Matter·Capital Call·Default Remedy 가시성 부족 | 대규모 50:50 JV | decision and call latency | P0 |
| `PP-D13-07` | 설비·기술 Milestone과 지급·검수증빙 분산 | Solid Power 3계약 | milestone acceptance cycle | P0 |
| `PP-D13-08` | R&D License를 상업생산권으로 확대해석 | Solid Power Field of Use 제한 | unauthorized-use incidents | P0 |
| `PP-D13-09` | Background·Foreground IP와 데이터 권리 미구조화 | 기술 MOU·JDA·License 병존 | IP-rights completeness | P0 |
| `PP-D13-10` | Amendment·Side Letter·Waiver가 운영 Baseline에 늦게 반영 | 다년·다법인 계약 | change propagation lead time | P0 |
| `PP-D13-11` | JV 해소 후 Orphan 자산·부채·보증·의무 발생 | BOSK Separation | orphan obligation count | P0 |
| `PP-D13-12` | Partner 수요·신용·기술진척 변화가 계약위험에 늦게 반영 | Startup·신기술·Project형 고객 | alert lead time | P1 |
| `PP-D13-13` | Claim·LD·Price True-up·Reimbursement 누락 | 품질·납기·원가변동 계약 | leakage recovered / at risk | P1 |
| `PP-D13-14` | 생성형 AI의 조항 오독·기밀유출·무권한 실행 위험 | 계약·IP·분쟁자료 민감성 | citation accuracy / access violations | P0 |

### 핵심 해석

SK온의 계약위험은 `계약서가 많다`는 문제가 아니다. 고객수요·공장투자·기술개발·정책금융이 변할 때 **서로 다른 계약의 조건·의무·권리가 같은 속도로 갱신되지 않고, 법적 당사자와 실제 경제부담자가 분리되는 것**이 핵심이다. D17은 단순 계약검색보다 `Clause → Obligation → Evidence → Economic Attribution → Decision/Exit`의 폐쇄루프를 우선해야 한다.

---
