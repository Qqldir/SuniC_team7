---
id: skes-d17-d17-00-executive-decision-summary
title: Executive Decision Summary
summary: E&S 16개 도메인 분석을 통합하여 60개 오픈이노베이션 과제와 20개 우선검증 과제를 제시하는 최종의사결정 DB
tags: [d17, oi-portfolio, table, "xref:d01", "xref:d16", "xref:d03"]
keywords: [오픈이노베이션, O/I과제, 포트폴리오, 우선순위, Digital Twin, LNG, BESS, 검증, PoC, 의사결정]
related: [SRC-D17-EXT-001, SRC-D17-EXT-002]
priority: normal
domain: D17
section: D17-00
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 2042
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# SK이노베이션 E&S AI Knowledge Database

## D17. Open-Innovation Opportunity Portfolio & AI Task Recommendation｜외부사례 기반 O/I 혁신과제 추천 DB

**Version 1.0 / 기준일: 2026-08-06 / D01~D16 통합 최종의사결정 문서**

- 대상: SK이노베이션 E&S CIC 및 연결·관계 사업의 공개확인 범위
- 상위 목적: D01~D16의 사실·Pain Point·Failure Mode·Risk·Economics·O/I Seed·External Capability를 중복 제거하고, E&S가 실제로 `검증 → PoC → 독립가치검증 → 확장 또는 중단`할 수 있는 60개 과제 포트폴리오를 제시한다.
- 문서 성격: 공개자료와 선행 도메인 DB에 기반한 **사전심사·추천 DB**다. 내부 운전값, 손익, 계약원문, 데이터권리, 세무·법률·SHE·Cyber 승인 없이 실제 운영·구매·투자·입찰·제어를 승인하지 않는다.
- 핵심 원칙: **기술·벤더에서 출발하지 않고 검증된 문제와 의사결정에서 출발한다.** 외부사례의 ROI·성능수치를 E&S 예상효과로 복사하지 않는다.
- 우선순위 상태: 본 문서의 Score/Tier는 `ANALYTICAL_PRE_SCREEN`이며 내부 Baseline과 Owner 확인 전 승인점수가 아니다.

---

# D17-00 Executive Decision Summary

## 1. 최종 포트폴리오

| 구분 | 수량 | 의미 |
|---|---:|---|
| 선행 도메인 | 16개 | D01~D16. 기업·사업·제품·기술·R&D/IP·운영·자산·공급망·고객·시장·경제성·투자·계약·규제·리스크·외부기술 |
| 심층 Seed Pool | 수백 개 | D03~D16의 O/I Seed·Pain·Failure Mode·PoC 후보를 통합. 도메인별 동일 문제가 반복되므로 원시 개수 합계를 실행과제 수로 해석하지 않는다. |
| 최종 O/I 과제 | 60개 | 12개 Portfolio × 5개. 문제·Owner·Data·Decision·KPI 기준으로 재설계 |
| `P0` | 20개 | G0/G1 검증을 가장 먼저 시작할 후보. 내부 Gate 통과 전 Live 적용 아님 |
| `P1` | 24개 | 선행 Data/권리/운영조건을 닫은 뒤 PoC |
| `P2` | 16개 | Option·기술실사·장기개발·Observe 중심. 바로 Scale 금지 |

## 2. E&S D17의 핵심 결론

E&S의 가장 큰 O/I 기회는 특정 생성형 AI를 도입하는 것이 아니다. **가스·전력·열·수소·CO2·전력저장·계약권리의 물리 흐름을 시장·원가·안전·규제·현금과 같은 시간축으로 연결하는 의사결정 구조**를 만드는 것이다.

특히 다음 6개 Value Thread가 E&S만의 차별적 우선순위다.

1. `LNG Cargo → Vessel → Terminal → Power/CHP → Margin`의 수직통합 의사결정
2. `Asset Condition → Failure/Outage → Lost Energy → Lost Margin → Maintenance`의 신뢰성 경제성
3. `BESS SOC/SOH → Bid → Dispatch → Settlement → Degradation → Lifecycle Margin`의 폐루프 수익성
4. `LH2 Feed → Liquefaction → Tank → Trailer → Station → Sold/Paid kg`의 안전·질량수지·경제성
5. `Emitter FID → Capture → Transport → Storage → MMV → Liability`의 CCS bankability
6. `Rule/Contract/JV → Applicable Entity/Asset → Obligation → Evidence → Cash/Risk`의 규제·거버넌스 증빙

## 3. P0 20개 — 가장 먼저 검증할 과제

| Wave | ID | 과제 | 핵심 이유 |
|---|---|---|---|
| W0 Control | `001` | Opportunity Portfolio Control Tower | D03~D16 중복·무주인 Seed 차단 |
| W0 Control | `002` | External Evidence & Source Freshness Agent | 외부 Claim·Rule·MOU 단계 오인 차단 |
| W0 Control | `003` | PoC-to-Scale Stage-Gate & Finance-Verified Benefit Engine | Zombie PoC·편익 이중계상 차단 |
| W1 LNG | `006` | LNG–Terminal–Power Resilience & Constraint Twin | E&S 수직통합의 핵심 차별점 |
| W1 LNG | `007` | Cargo Landed-Cost & Optionality Twin | Cargo별 실제원가·권리·현금 연결 |
| W1 LNG | `008` | Terminal Energy–BOG Digital Twin | BOG·전력·탱크·send-out 통합 |
| W1 Power | `011` | Fleet Heat-Rate Residual & Dispatch Margin Twin | 연료효율을 EBIT 가설로 연결 |
| W1 Power | `012` | Turbine Trip Precursor & Historian–EAM Thread | Trip 신호를 작업과 경제손실에 연결 |
| W1 Power | `013` | CHP Power–Heat Co-optimizer | 전력 단독 최적화 오류 방지 |
| W1 City Gas | `016` | City-Gas Network Truth & Explainable RBMS | 7개 도시가스사의 공통 안전 데이터 기반 |
| W2 Renewable | `021` | Offshore Wind Risk, Weather-Window & Cable Twin | 신규 운영자산의 긴 MTTR·해상접근 병목 |
| W2 BESS | `026` | Degradation-Aware BESS Bidder | KCE 시장수익과 열화비용 동시 최적화 |
| W2 BESS | `027` | BESS Thermal Precursor Fusion | 안전·가용성의 선행신호 통합 |
| W2 BESS | `028` | BESS Counterfactual Revenue & Settlement Lab | optimizer alpha를 독립검증 가능하게 함 |
| W2 H2 | `036` | LH2 Safety Barrier Health Monitor | 안전중요 Barrier의 proof-test·상태 가시화 |
| W2 H2 | `037` | LH2 Mass-Balance & Paid-kg Cost Twin | 생산량이 아닌 판매·수금 kg 경제성 |
| W3 CCS | `041` | Risk-based CCS Digital MMV | CCS bankability·규제증빙의 공통 기반 |
| W3 Policy | `046` | K-ETS Allocation–Dispatch Position Twin | 4기 ETS 탄소비용 변화와 발전운영 연결 |
| W3 Policy | `047` | PFE/48E Supplier Evidence & Eligibility Graph | KCE 세액공제·공급망 증빙 연결 |
| W3 Resilience | `057` | OT Safety–Cyber Correlation & Triage | 안전 Barrier와 OT 위협의 공동 우선순위 |

## 4. 외부환경 Why-now 검증

- IEA Gas Market Report Q3-2026은 호르무즈를 통과하던 LNG가 기존 글로벌 LNG 공급의 거의 20%였으며 2026년 공급충격과 정상화 불확실성이 시장 변동성을 키웠다고 설명한다. 이는 E&S에서 Cargo–Terminal–Power를 분리 최적화하지 않고 공급충격 대응을 하나의 제약문제로 다뤄야 할 근거다. `SRC-D17-EXT-001`.
- 한국 제4기 배출권거래제(2026~2030)는 발전부문 유상할당 강화 경로를 포함한다. 따라서 LNG 발전의 Heat Rate 개선과 Dispatch 의사결정은 탄소 포지션을 떼고 보면 안 된다. `SRC-D17-EXT-002`.
- 미국 48E/PFE, 호주 Safeguard, 베트남 LNG-to-power 일정 조건 등은 D14의 시점관리 규칙을 그대로 승계한다. D17은 제도 최고혜택을 실제 E&S/KCE 현금으로 간주하지 않는다.

---
