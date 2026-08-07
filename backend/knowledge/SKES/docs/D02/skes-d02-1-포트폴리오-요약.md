---
id: skes-d02-1-포트폴리오-요약
title: 포트폴리오 요약
summary: SK이노베이션 E&S의 LNG·전력·도시가스·수소·재생에너지 등 사업을 고객·수익모델·운영단계별로 정의한 포트폴리오 Master DB
tags: [d02, business, schema, table, "xref:d01", "xref:d03", "xref:d06", "xref:d07"]
keywords: [LNG 밸류체인, 도시가스, 재생에너지, 수소, 에너지솔루션, 비즈니스 모델, PPA, CCS, ESS·VPP·DERMS, 사업 단계, LNG Value Chain, Energy Solution, Business Master, 사업모델, 수익모델]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001, BUS-ENS-01, BUS-ENS-02, BUS-ENS-03, BUS-ENS-04, BUS-ENS-05, BUS-ENS-06, BUS-ENS-07]
priority: normal
domain: D02
section: 1
source: SK이노베이션E&S_D02_Business_Portfolio_v2_보강본.md
breadcrumb: ""
tokens: 1892
updated: 2026-08-06
---

> SK이노베이션 E&S · D02 사업 포트폴리오

# SK이노베이션 E&S AI Knowledge Database

## D02. Business Portfolio｜사업 포트폴리오

**Version 2.0 / 기준일: 2026년 8월 4일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Source namespace: `SRC-ENS-D02-*`
- Fact namespace: `FACT-ENS-D02-*`
- Business namespace: `BUS-ENS-*`
- 작성 원칙: O/I 과제 생성에 직접 필요한 사업·고객·수익모델·핵심자산·운영단계·Pain Point 중심의 압축형 DB
- D01 상속 규칙: 2024년 11월 1일 이전 `SK E&S`, 이후 `SK이노베이션 E&S CIC`를 시점별로 구분

---

## 0. 도메인 정의

D02는 SK이노베이션 E&S의 LNG, 발전, 도시가스, 재생에너지, 수소, 에너지솔루션, CCS 사업을 사업모델 단위로 분해한다. 단순 사업소개가 아니라 AI가 다음 질문에 답할 수 있도록 설계한다.

1. 무엇을 생산·판매·운영하는가.
2. 고객은 누구이며 어떤 방식으로 매출이 발생하는가.
3. 핵심 자산과 운영기능은 무엇인가.
4. 현재 운영사업과 개발·검토사업은 무엇인가.
5. O/I 과제를 발굴할 때 어느 운영문제를 우선 탐색해야 하는가.

### 0.1 포함·제외 범위

```yaml
included:
  - LNG upstream, liquefaction, shipping, terminal, power generation
  - CHP and heat supply
  - seven city-gas subsidiaries and eight supply regions
  - solar, onshore wind, offshore wind and RE100/PPA solutions
  - liquefied hydrogen, blue hydrogen, green hydrogen
  - ESS, VPP, DERMS, EMS, renewable O&M and EV charging
  - CCS-linked low-carbon LNG
excluded_or_deferred:
  - asset-by-asset engineering specification: D03, D06, D07
  - supplier and LNG procurement contract detail: D08, D13
  - segment profitability and cost breakdown: D11
  - regulation, emissions verification and taxonomy judgment: D14, D15
  - external vendors and startups: D16
```

### 0.2 데이터 해석 규칙

- 공식 홈페이지의 `보유`, `운영`, `개발`, `검토`, `계획`을 서로 다른 상태값으로 저장한다.
- 발전용량, 재생에너지 파이프라인, LNG 계약량, 터미널 처리능력을 합산하지 않는다.
- `운영 및 개발 3.5GW`와 `약 5GW 파이프라인`은 범위가 중첩될 수 있으므로 합계 8.5GW로 계산하지 않는다.
- 사업별 매출액이 공개되지 않으면 사업 메커니즘에 따른 `revenue_model_inference`로만 기록한다.
- 2026년 분기 E&S 실적은 여러 사업을 포함한 E&S 전체 실적이며 개별 사업 매출로 배분하지 않는다.

---

# 1. 포트폴리오 요약

## 1.1 최상위 사업구조

```text
LNG Value Chain
  ├─ Upstream Gas Resource
  ├─ Liquefaction / Shipping / Terminal
  └─ Gas Power / CHP

Power Value Chain
  ├─ City Gas
  ├─ Renewable Energy / PPA
  ├─ Hydrogen
  ├─ Energy Solution: ESS / DERMS / VPP / EV Charging
  └─ CCS-linked Low-carbon LNG
```

SK이노베이션 E&S의 기반 수익축은 도시가스와 LNG 발전을 포함한 LNG Value Chain이다. 성장축은 재생에너지, 수소, 에너지솔루션, CCS이며, 이들은 별개의 신사업이면서 기존 LNG·전력 자산과 연결되는 구조다. 공식 기업소개는 이를 `LNG Value Chain 확장 + Power Value Chain Solution 통합`으로 설명한다. ([SRC-ENS-D02-0001])

## 1.2 Business Master

| Business ID | 사업군 | 주요 제공물 | 핵심 고객 | 주요 수익방식 | 단계 | O/I 우선도 |
|---|---|---|---|---|---|---|
| `BUS-ENS-01` | LNG Value Chain | 천연가스·LNG 조달 및 인프라 운영 | 발전·도시가스·산업 수요처 | 가스 판매, 자산·계약 기반 마진 | 운영+확장 | P0 |
| `BUS-ENS-02` | City Gas | 배관망 기반 도시가스 공급 | 가정·상업·산업 고객 | 규제요금 기반 가스 판매 | 성숙 운영 | P0 |
| `BUS-ENS-03` | Power / CHP | 전력과 열 | 전력시장·지역난방 고객 | 전력·열 판매 | 성숙 운영 | P0 |
| `BUS-ENS-04` | Renewable Energy | 태양광·풍력 전력, PPA·REC | 전력시장·RE100 기업 | 전력·PPA·REC 및 개발수익 | 운영+개발 | P0 |
| `BUS-ENS-05` | Hydrogen | 액화수소 및 미래 청정수소 | 모빌리티·산업 고객 | 수소 판매·인프라 서비스 | 초기 상업화+개발 | P1 |
| `BUS-ENS-06` | Energy Solution | ESS·VPP·DERMS·O&M·충전 | 전력망·발전사업자·기업·EV 이용자 | 프로젝트·운영·거래·서비스 수익 | 운영+확장 | P0 |
| `BUS-ENS-07` | CCS / Low-carbon LNG | CO2 포집·운송·저장 연계 | 자체 LNG 체인·잠재 외부 배출원 | 비용절감·저탄소 프리미엄·저장서비스 가능성 | 개발·검토 | P1 |

`O/I 우선도`는 사업 중요도가 아니라 외부기술·디지털 솔루션을 적용해 성과를 만들 가능성을 뜻한다.

## 1.3 사업별 핵심 자산형태

| 사업군 | 자산형태 | 핵심 운영변수 |
|---|---|---|
| LNG Upstream | 가스전 지분·생산권 | 생산량, 가동률, 정비, methane·CO2 |
| LNG Midstream | 액화계약, 선박, 터미널 | liquefaction yield, BOG, 선박일정, 저장재고 |
| Power / CHP | 복합화력·열병합 설비 | heat rate, SMP, 가동률, 정비, 열수요 |
| City Gas | 배관망·정압기·계량기 | 수요, 압력, 누출, 안전, 검침 |
| Renewable | 태양광·풍력 발전자산 | 발전량, 예측오차, 고장, 출력제한 |
| Hydrogen | 액화플랜트·저장·운송 | 전력소비, boil-off, 안전, 물류, 수요 |
| Energy Solution | ESS·전력망·플랫폼·충전기 | SOC, 가격, 화재안전, 집합제어, 이용률 |
| CCS | 포집·압축·배관·저장소 | 포집률, 에너지페널티, 부식, 누출, MRV |

---
