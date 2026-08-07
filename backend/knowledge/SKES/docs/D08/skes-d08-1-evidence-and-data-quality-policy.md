---
id: skes-d08-1-evidence-and-data-quality-policy
title: Evidence and Data-Quality Policy
summary: 증거신뢰도 5단계(E1~E5)·사실상태 7가지·계약권리 9가지 분류 기준과 LNG·생산·공급 관련 14개 검증규칙을 정의한다.
tags: [d08, supply-chain, table]
keywords: [신뢰도등급, E1-E5, 사실상태, 계약권리유형, LNG도입, 생산권, 공급관계, 검증규칙]
related: []
priority: normal
domain: D08
section: 1
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 1345
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 1. Evidence and Data-Quality Policy

## 1.1 Evidence Tier

| Tier | 정의 | 허용 판정 |
|---|---|---|
| E1 | E&S·SK이노베이션·공시·공식 사업 페이지 | 공개사실 확정 |
| E2 | 계약 상대방·자회사·JV·프로젝트 공식자료 | 관계·역할 교차확인 |
| E3 | 정부·규제기관·공공 기술기관 | 표준 공정·규제·위험 baseline |
| E4 | 신뢰도 높은 산업자료 | 보조 설명·탐색 후보 |
| E5 | 검색 스니펫·미검증 2차자료 | 저장 금지, 검증 queue만 허용 |

## 1.2 Claim Status

| Code | 의미 | 예시 |
|---|---|---|
| `DISCLOSED_FACT` | 직접 공개된 관계·물량·역할 | Freeport 220만 톤/년 사용계약 |
| `COUNTERPARTY_CONFIRMED` | 상대방 공식자료로 확인 | 20년 use-or-pay 구조 |
| `CALCULATED_FACT` | 공개값의 단순 산술변환 | 선박 7.5만 톤 × 4척 참고값 |
| `STRUCTURAL_ANALYSIS` | 공개사실 간 연결 분석 | 생산지분과 tolling의 결합 |
| `INDUSTRY_BASELINE` | 일반적으로 필요한 품목·데이터 | GT hot-gas-path spares |
| `OI_HYPOTHESIS` | 내부데이터로 검증할 개선가설 | cargo-재고 통합 최적화 |
| `UNDISCLOSED_GAP` | 내부확인 없이는 확정 불가 | 계약가격·destination clause |

## 1.3 Contract/Right Type

| right_type | 정의 | 소유자산 합산 여부 |
|---|---|---|
| `EQUITY_PRODUCTION` | 가스전 지분 기반 생산권 | 지분귀속량만 별도 계산 |
| `LONG_TERM_OFFTAKE` | 장기 LNG 구매·도입 | 소유량으로 합산 금지 |
| `TOLLING_USE_OR_PAY` | feed gas를 액화하는 사용권 | 액화자산 소유로 합산 금지 |
| `TERMINAL_USE_AGREEMENT` | 하역·저장·기화·송출 사용권 | 터미널 소유로 합산 금지 |
| `TIME_CHARTER` | 기간용선·전용선 사용권 | 선박 법적 소유와 분리 |
| `SPOT_PURCHASE` | 단기 cargo 구매 | 장기 확정물량으로 합산 금지 |
| `EPC_SUPPLY` | 설비·건설 일괄공급 | 운영권·소유권과 분리 |
| `LTSA_OAM` | 장기서비스·유지보수 | 자산 소유와 분리 |
| `FRAMEWORK_MSA` | 반복구매·서비스 기본계약 | 발주·검수 실적 별도 관리 |

## 1.4 Hard Guardrails

1. Tangguh 50~60만 톤/년은 장기 도입 규모이며 가스전 전체 생산능력이 아니다.
2. Woodford 약 110만 톤/년은 공동개발 생산 설명값이며 전량 한국 도입량으로 간주하지 않는다.
3. Freeport 220만 톤/년은 20년 use-or-pay 액화설비 사용권이며 LNG 구매량이나 실제 생산량과 다르다.
4. Barossa 약 130만 톤/년은 E&S 도입 설명물량이며 프로젝트 총 생산능력과 다르다.
5. Darwin LNG 지분, Barossa 지분, Barossa 장기 도입물량을 중복 합산하지 않는다.
6. 보령 LNG터미널 700만 톤/년 물리능력과 E&S 350만 톤/년 TUA를 분리한다.
7. 보령 지분 매각 후에도 유지되는 사용권을 E&S 소유자산으로 표시하지 않는다.
8. Ganyu는 2027년 예정 사용권으로 운영 실적에 포함하지 않는다.
9. LNG 4척은 공개 선대 수이며 선박별 용선주·선주·운항사·남은 계약기간은 내부확인한다.
10. KCE의 Powin·Sungrow 공급관계는 공개된 프로젝트에만 연결하고 전체 포트폴리오 표준벤더로 일반화하지 않는다.
11. KCE BESS의 cell 원산지·화학계·보증조건은 공개되지 않았으면 추정하지 않는다.
12. 도시가스 도매공급자·배관자재 공급사·발전 OEM 계약은 법인·자산별 내부자료로 검증한다.
13. 공급사 ESG 실사 약 100개 대상 pool과 2022년 실제 26개 실사를 전체 공급사 수로 해석하지 않는다.
14. 인천 액화수소 3만 톤/년은 명목 생산능력이며 부생수소 실제 조달량·출하량과 다르다.
15. 계약가격·take-or-pay·destination clause·hedge·penalty·warranty 조건은 공개되지 않으면 저장하지 않는다.

---
