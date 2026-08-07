---
id: skon-d02-3-ess-배터리-사업
title: ESS 배터리 사업
summary: "에너지저장장치의 사업 정의, 화학계별(NCM/LFP/VIB) 포트폴리오, 셀부터 컨테이너형까지의 제공형태, 고객가치, 세부시장 분류를 설명하는 SK온 문서."
tags: [d02, business, table]
keywords: [에너지저장, NCM, LFP, VIB, BESS, 배터리셀, 수명관리, 재생에너지연계, 안전성, 계통용저장, 에너지저장장치, 컨테이너형, 배터리수명관리]
related: [BUS-SKON-ESS-001, ESS-CELL, ESS-MODULE, ESS-CONTAINER, ESS-BMS, ESS-EPC, ESS-OPERATOR]
priority: normal
domain: D02
section: 3
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 1743
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# 3. ESS 배터리 사업

## 3.1 사업 정의

| 필드          | 데이터                         |
| ----------- | --------------------------- |
| Business ID | `BUS-SKON-ESS-001`          |
| 공식 사업명      | ESS                         |
| 영문명         | Energy Storage System       |
| 사업유형        | B2B 배터리·시스템 공급              |
| 주요 고객       | 발전·전력·재생에너지·BESS 개발사업자·산업체  |
| 주요 적용처      | 계통용 저장, 재생에너지 연계, 상업·산업용 저장 |
| 화학계         | NCM, LFP, VIB 공동개발          |
| 주요 제공형태     | 셀·모듈·컨테이너형 BESS·수명관리        |
| 사업단계        | 상업화 확대                      |
| 포트폴리오 역할    | Growth Business             |

SK온 공식 ESS 사업소개는 고품질·고에너지밀도의 NCM 배터리 셀과 배터리 수명관리시스템을 기반으로 안정적이고 효율적인 상업용 ESS를 제공한다고 설명한다. ([SK On][9])

---

## 3.2 ESS 포트폴리오 확대

SK온의 ESS사업은 기존 NCM 중심 설명에서 LFP 기반 북미 BESS와 VIB 공동개발까지 범위가 확대되고 있다. 2025년 SK온은 미국 Flatiron Energy Development와 매사추세츠 프로젝트에 1GWh 규모의 LFP 기반 컨테이너형 BESS를 공급하기로 했으며, 공급 개시는 2026년 하반기로 발표됐다. 또한 미국 조지아주의 SK Battery America 전기차 배터리 생산라인 일부를 활용해 ESS용 LFP 배터리를 생산할 계획이라고 밝혔다. ([ASK Inno][10])

SK이노베이션의 2025년 3분기 실적발표는 이 1GWh 공급계약과 함께 추가 6.2GWh 프로젝트에 대한 우선협상권 확보를 언급했다. 이는 ESS가 단순한 연구개발 항목을 넘어 실제 공급계약이 발생한 상업 확장사업이라는 근거가 된다. 다만 우선협상권은 확정 수주와 다르므로 각각 별도 상태값으로 관리해야 한다. ([ASK Inno][2])

2026년에는 Standard Energy와 VIB 기반 ESS 공동개발을 추진하면서 안전성과 고출력 특성이 필요한 단주기 ESS 영역까지 탐색범위를 넓혔다. 공식 발표는 VIB가 수계 전해질을 사용해 화재·폭발 위험을 낮추고 높은 출력을 제공할 수 있다고 설명했다. ([ASK Inno][7])

---

## 3.3 ESS 제공형태

```text
Battery Cell
→ Battery Module
→ Rack or System Configuration
→ Containerized BESS
→ Monitoring and Lifespan Management
→ Operation and Maintenance Interface
```

SK온 공식 자료에서 직접 확인되는 제공범위는 NCM 배터리 셀, 하이니켈·LFP ESS 모듈, 컨테이너형 LFP BESS, 배터리 수명관리시스템이다. 전체 EPC, 전력시장 운영, 장기 유지보수를 SK온이 모든 프로젝트에서 직접 수행한다고 볼 근거는 부족하므로, 프로젝트별 역할을 별도 확인해야 한다. ([SK On][9])

### 역할 분류

| Role Code       | 역할            | 데이터 상태      |
| --------------- | ------------- | ----------- |
| `ESS-CELL`      | ESS용 셀 공급     | 공식 확인       |
| `ESS-MODULE`    | ESS용 모듈 공급    | 공식 확인       |
| `ESS-CONTAINER` | 컨테이너형 BESS 공급 | 공식 확인       |
| `ESS-BMS`       | 배터리 상태·수명관리   | 공식 확인       |
| `ESS-EPC`       | 전체 EPC        | 프로젝트별 확인 필요 |
| `ESS-OPERATOR`  | 전력시장 운영       | 확인 필요       |
| `ESS-O&M`       | 장기 운영·정비      | 계약별 확인 필요   |

---

## 3.4 ESS 고객가치

### 공식 사실 기반 가치요소

* 안정성
* 효율성
* 배터리 수명관리
* 높은 에너지 밀도
* LFP 기반 가격경쟁력
* 북미 현지 생산
* 다양한 화학계 선택 가능성
* 화재 안전성 강화

SK온은 기존 공식 ESS 소개에서 안정성·효율성·고에너지밀도·수명관리를 강조하고, 북미 LFP 사업에서는 비용경쟁력과 안전성, VIB 공동개발에서는 화재 안전성과 고출력을 강조한다. ([SK On][9])

---

## 3.5 ESS 세부시장 분류

공개자료만으로 SK온의 모든 ESS 세부시장별 매출과 계약을 확정할 수는 없으나, 데이터베이스는 다음 시장분류를 사용한다.

```text
Utility-scale BESS
Renewable Energy Integration
Commercial and Industrial ESS
Data Center Energy Storage
Microgrid
EV Charging-linked ESS
Backup Power
Short-duration High-power ESS
Long-duration Energy Storage
```

각 세부시장은 다음 상태 중 하나로 기록한다.

* `confirmed_supply`
* `confirmed_development`
* `official_target_market`
* `potential_application`
* `not_verified`

현재 공식적으로 명확하게 확인되는 사업은 북미 대규모 BESS 공급, 상업용 ESS, LFP ESS, VIB 기반 고안전성·고출력 ESS 공동개발이다. 데이터센터·마이크로그리드·충전연계 ESS 등은 기술적으로 가능한 적용처일 수 있으나 SK온의 공식 수주나 사업영역으로 확인되지 않으면 `potential_application`으로만 저장한다.

---
