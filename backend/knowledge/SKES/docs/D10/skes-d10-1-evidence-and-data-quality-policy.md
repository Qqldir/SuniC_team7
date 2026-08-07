---
id: skes-d10-1-evidence-and-data-quality-policy
title: Evidence and Data-Quality Policy
summary: "에너지 시장 분석에서 데이터 출처별 신뢰도(E1~E5), 주장의 성격과 확실성(9가지 상태), 데이터 혼동을 방지하기 위한 금지 원칙 20가지를 정의한 정책"
tags: [d10, market, table]
keywords: [증거등급, 주장상태분류, 데이터검증, 설비용량, LNG, BESS, 시장점유율, 경쟁사정보, CCS]
related: []
priority: normal
domain: D10
section: 1
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 1144
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 1. Evidence and Data-Quality Policy

## 1.1 Evidence Tier

| Tier | 정의 | D10 허용 용도 |
|---|---|---|
| E1 | E&S·SK이노베이션·자회사·공시 | 자산·사업상태·공개실적 확정 |
| E2 | 정부·국제기구·시장운영기관·통계기관 | 시장실적·정책·가격·전망 baseline |
| E3 | 경쟁사 공식보고서·IR·제품발표 | 경쟁사 주장·전략·공개성과 |
| E4 | 신뢰 산업기관·표준·연구기관 | 비교·시장구조·기술 baseline |
| E5 | 기사·검색 스니펫·미검증 2차자료 | 탐색만 허용, 확정값 저장 금지 |

## 1.2 Claim Status

| Code | 정의 | 저장 예시 |
|---|---|---|
| `ACTUAL_FINAL` | 확정된 과거 실적 | 2025 연간 설치량 |
| `ACTUAL_PRELIMINARY` | 잠정·속보 실적 | KPX 월간 속보 |
| `FORECAST_BASE` | 특정 기관의 기준 전망 | IEA 2026 전망 |
| `FORECAST_SCENARIO` | 조건부 시나리오 | Strait 재개 가정 LNG 전망 |
| `COMPANY_CLAIM` | 기업이 발표한 규모·성능 | Tesla storage deployment |
| `PIPELINE_ANNOUNCED` | 발표·개발 pipeline | KCE 8GW 개발 |
| `FID_OR_CONSTRUCTION` | 투자확정·건설 단계 | 프로젝트별 별도 확인 |
| `OPERATING` | 상업운영 확인 | KCE operating assets |
| `STRUCTURAL_ANALYSIS` | 공개사실 기반 내부 분석 | gas-to-coal switching 영향 |
| `NOT_DISCLOSED` | 공개되지 않음 | PPA 가격 |
| `OI_HYPOTHESIS` | 내부 데이터로 검증할 가설 | 시장 신호 조기경보 |

## 1.3 Hard Guardrails

1. 수요 actual·전망·정책목표를 같은 열에서 합산하지 않는다.
2. 설비 MW, 저장에너지 MWh, 발전량 MWh, 거래량 MWh를 구분한다.
3. LNG 생산지분·액화 사용권·터미널 사용권·실제 도입량을 중복 합산하지 않는다.
4. 개발 pipeline을 운영자산·수주잔고·확정매출로 표시하지 않는다.
5. 경쟁사 회사 전체 매출과 특정 energy segment 매출을 동일 비교하지 않는다.
6. 회사 발표 점유율은 조사기관·지역·기간·분모가 같을 때만 비교한다.
7. 월간 SMP 속보는 잠정치이며 연간 평균·장기 PPA 가격으로 대체하지 않는다.
8. 장기 PPA MW를 실제 공급 MWh나 RE100 이행률로 치환하지 않는다.
9. BESS merchant revenue를 단일 고객매출이나 고정수익으로 표시하지 않는다.
10. BESS 운영 MW와 개발 queue MW를 더해 시장점유율을 계산하지 않는다.
11. EV 충전 port·connector·station·site·session·active driver를 구분한다.
12. 수소 플랜트 명목능력과 실제 생산·출하·판매량을 구분한다.
13. 수소 MOU·차량도입 목표·충전소 계획을 최소구매의무로 저장하지 않는다.
14. CCS 발표용량과 운영·건설·FID·저장권·확정 주입량을 분리한다.
15. 정책보조금과 세액공제를 구조적 시장가격으로 취급하지 않는다.
16. 서로 다른 통화·기준열량·인도조건의 LNG 가격을 무보정 비교하지 않는다.
17. 경쟁사 기술·수익성 주장은 `COMPANY_CLAIM`으로 보존한다.
18. 시장전망은 기관·발표일·기준연도·scenario를 함께 저장한다.
19. AI는 입찰·헤지·가격·투자·시장철수를 자동 확정하지 않는다.
20. 공개되지 않은 E&S 시장점유율·마진·계약가격은 `NOT_DISCLOSED`로 둔다.

---
