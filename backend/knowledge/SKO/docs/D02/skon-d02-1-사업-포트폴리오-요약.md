---
id: skon-d02-1-사업-포트폴리오-요약
title: 사업 포트폴리오 요약
summary: "SK온이 영위하는 다섯 사업영역(배터리, ESS, BaaS, 트레이딩, 윤활기유)의 고객, 제공가치, 성숙도를 정리한 포트폴리오"
tags: [d02, business, table, "xref:d00", "xref:d03", "xref:d04", "xref:d08"]
keywords: [EV배터리, ESS, BaaS, 트레이딩, 윤활유, 사업 상태, 셀·모듈·팩, 배터리 생애주기, 열관리, 액침냉각, EV 배터리, 사업 성숙도, 포트폴리오, 고객군]
related: [ORG-SKON-000001, COMP-SKON-001, CO-SKON, BP-SKON-01, BP-SKON-02, BP-SKON-03, BP-SKON-04, BP-SKON-05]
priority: normal
domain: D02
section: 1
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 1768
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# SK온 AI Knowledge Database

## D02. Business Portfolio｜사업 포트폴리오

**Version 1.0.1 / 기준일: 2026년 7월 29일 / D00 통합검수: 2026년 8월 3일**

- Canonical company entity: `ORG-SKON-000001`
- Legacy aliases retained: `COMP-SKON-001`, `CO-SKON`
- 번호형 각주 `[1]~[16]`는 Legacy Source ID로 보존하며 `SK온_D00_Canonical_Source_Crosswalk.csv`의 정규화 URL을 통해 Canonical Source ID와 연결한다.

---

## 0. 도메인 정의

D02 Business Portfolio는 SK온이 현재 영위하거나 공식적으로 추진하는 사업을 **고객, 제품·서비스, 적용시장, 수익창출 방식, 사업 성숙도, 지역, 관련 조직 및 성장 방향**에 따라 구조화하는 도메인이다.

D01이 SK온의 법적·조직적 정체성을 정의했다면, D02는 다음 질문에 답하기 위한 데이터베이스다.

> SK온은 어떤 시장에서, 어떤 고객에게, 어떤 제품과 서비스를 제공하며, 각 사업은 현재 어느 단계에 있고 앞으로 어느 방향으로 확장되고 있는가?

D02에서는 제품의 세부 사양과 기술 원리는 D03·D04, 고객별 공급관계는 D08, 공장과 생산능력은 D07, 수익구조와 경제성은 D11, 개별 O/I 과제는 D16으로 연결한다.

---

# 1. 사업 포트폴리오 요약

## 1.1 최상위 사업구조

기준일 현재 SK온의 사업 포트폴리오는 크게 다음 다섯 영역으로 구조화할 수 있다.

| Portfolio ID | 사업영역            | 핵심 제공가치                          | 주요 고객                      | 사업 상태                         |
| ------------ | --------------- | -------------------------------- | -------------------------- | ----------------------------- |
| `BP-SKON-01` | 전기차용 배터리        | 전기차 구동용 배터리 셀·모듈·팩 및 관련 솔루션      | 글로벌 완성차 기업                 | Core / Commercial             |
| `BP-SKON-02` | ESS용 배터리        | 전력저장용 배터리 셀·모듈·컨테이너형 시스템 및 수명관리  | 에너지 개발사·전력사업자·산업 고객        | Growth / Commercial Expansion |
| `BP-SKON-03` | BaaS            | 배터리 진단·렌탈·충전·재사용·재활용 등 생애주기 서비스  | 차량 사용자·모빌리티·금융·재사용·재활용 사업자 | Emerging / Platform Expansion |
| `BP-SKON-04` | 트레이딩·에너지 공급망    | 원유·석유제품·화학제품 등의 글로벌 트레이딩과 공급망 운영 | 정유·석유화학·산업 고객              | Mature / CIC                  |
| `BP-SKON-05` | 윤활기유·열관리·에너지효율화 | 윤활기유, 열관리, 액침냉각 및 에너지효율 솔루션      | 윤활유사·데이터센터·산업·모빌리티 고객      | Mature + Growth / CIC         |

SK온 공식 사업 소개는 배터리 영역을 `전기차 배터리`, `ESS`, `BaaS`의 세 축으로 구성한다. SK온은 자동차와 ESS용 배터리를 생산하고, 셀부터 모듈·팩까지 고객 요구에 맞춘 형태로 공급하며, BaaS를 통해 배터리 생애주기 관리 서비스를 제공한다고 설명한다. ([SK On][1])

2025년의 기업결합을 반영하면 법인 전체의 사업범위에는 배터리사업 외에도 기존 SK트레이딩인터내셔널·SK엔텀 계열의 트레이딩·터미널 사업과 기존 SK엔무브의 윤활기유·에너지효율화 사업이 포함된다. 다만 공식 SK온 홈페이지의 사업 메뉴는 여전히 배터리 중심으로 구성되어 있으므로, 데이터베이스에서는 **‘SK온 배터리 브랜드 포트폴리오’와 ‘통합 SK온 법인 포트폴리오’를 구분**해야 한다. SK이노베이션의 2025년 3분기 공식 실적자료도 SK온 연결 범위에 SK트레이딩인터내셔널과 SK엔텀을 포함했으며, SK엔무브와의 통합법인은 2025년 11월 1일 출범한다고 밝혔다. ([ASK Inno][2])

---

## 1.2 포트폴리오 계층

```text
SK On Business Portfolio
│
├─ A. Battery Business
│  ├─ A1. Electric Vehicle Battery
│  ├─ A2. ESS Battery
│  ├─ A3. BaaS
│  └─ A4. Battery-adjacent Solutions
│
├─ B. Trading & Terminal Business
│  ├─ B1. Crude Oil Trading
│  ├─ B2. Petroleum Product Trading
│  ├─ B3. Chemical Product Trading
│  ├─ B4. Logistics and Supply Optimization
│  └─ B5. Terminal-linked Operations
│
└─ C. Lubricants & Energy Efficiency Business
   ├─ C1. Lube Base Oil
   ├─ C2. Lubricants-related Solutions
   ├─ C3. Thermal Management
   ├─ C4. Immersion Cooling
   └─ C5. Energy Efficiency Solutions
```

### 데이터 해석 원칙

* `Battery Business`는 SK온 브랜드의 핵심 사업이다.
* `Trading & Terminal Business`는 통합 SK온 내 트레이딩 관련 CIC의 사업으로 관리한다.
* `Lubricants & Energy Efficiency Business`는 통합 SK온 내 SK엔무브 CIC의 사업으로 관리한다.
* 법인 포트폴리오에 포함됐다는 사실과 배터리사업과의 실질적 시너지는 분리한다.
* 합병 시점 이후에도 사업별 매출·고객·설비·조직은 구분해 저장한다.
* 향후 공식 조직개편으로 CIC 명칭이나 범위가 변경될 수 있으므로 유효기간을 관리한다.

---
