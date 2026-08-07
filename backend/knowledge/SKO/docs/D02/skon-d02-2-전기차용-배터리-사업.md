---
id: skon-d02-2-전기차용-배터리-사업
title: 전기차용 배터리 사업
summary: "SK온의 전기차 배터리 사업의 정의, 고객가치제안, 셀·모듈·팩 제품범위, NCM·LFP·VIB 화학계 포트폴리오를 정리한 사업 개요 문서다."
tags: [d02, business, schema, table]
keywords: [배터리 셀, 배터리 모듈, 배터리 팩, NCM, LFP, VIB, 하이니켈, 에너지 밀도, 화학계, 전고체, 셀, 모듈, 팩, NCM 계열, 바나듐이온, 완성차 제조사, 고객 맞춤]
related: [BUS-SKON-EV-001, CHEM-NCM, CHEM-LFP, CHEM-VIB, CHEM-ASSB, REG-KR, REG-NA, REG-EU, REG-CN, REG-OTHER]
priority: normal
domain: D02
section: 2
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 2670
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# 2. 전기차용 배터리 사업

## 2.1 사업 정의

| 필드          | 데이터                       |
| ----------- | ------------------------- |
| Business ID | `BUS-SKON-EV-001`         |
| 공식 사업명      | 전기차 배터리                   |
| 영문명         | Electric Vehicle Battery  |
| 사업유형        | B2B 제조·공급·공동개발            |
| 핵심 고객       | 글로벌 완성차 제조사               |
| 주요 제공단위     | 셀, 모듈, 팩 및 고객 맞춤형 배터리 솔루션 |
| 주요 화학계      | NCM 계열, LFP 계열            |
| 핵심 적용처      | 승용 전기차, 상용 전기차 및 전동화 플랫폼  |
| 사업단계        | 상업화·글로벌 확장                |
| 포트폴리오 역할    | Core Business             |

SK온은 전기차 배터리 제조 경험과 하이니켈 기술을 바탕으로 글로벌 시장에 배터리를 공급하며, 성능과 안전에 대한 신뢰성을 최우선 가치로 제시한다. 공식 사업소개에는 배터리 셀부터 모듈·팩까지 고객 요구에 맞는 다양한 형태를 제공한다고 명시돼 있다. ([SK On][1])

---

## 2.2 고객가치 제안

### 공식적으로 확인되는 가치요소

```text
Performance
Safety
Energy Density
Quality
Customer-specific Configuration
Global Supply
Manufacturing Reliability
Battery Life
Charging Performance
```

SK온 공식 전기차 배터리 페이지가 직접 강조하는 핵심은 `우수한 품질`, `하이니켈 기술`, `성능`, `안전`, `엄격한 생산·공급 기준`이다. 따라서 D02에서 전기차 배터리사업의 기본 가치제안은 **고성능 배터리를 고객의 차량 플랫폼에 맞추어 안정적으로 공급하는 것**으로 정의한다. ([SK On][1])

### 가치제안 데이터

```yaml
value_proposition_id: VP-SKON-EV-001
business_id: BUS-SKON-EV-001
customer_value:
  - 높은 에너지 밀도
  - 전기차 주행성능 지원
  - 안전성과 품질 신뢰성
  - 고객 차량 플랫폼 맞춤 대응
  - 셀·모듈·팩 단위 공급
  - 글로벌 현지 생산 및 공급
fact_status: official_fact_with_structured_interpretation
```

---

## 2.3 제품 제공범위

전기차 배터리사업의 제공범위는 다음과 같이 계층화한다.

### 2.3.1 배터리 셀

배터리의 기본 전기화학적 에너지 저장단위다. SK온은 하이니켈 NCM 계열을 중심으로 기술력을 축적했으며, 이후 LFP 등으로 화학계 포트폴리오를 확대하고 있다. 공식 사업소개가 셀부터 모듈·팩까지 제공한다고 명시하므로 셀은 독립적인 제품 엔티티로 관리한다. ([SK On][3])

### 2.3.2 배터리 모듈

복수의 셀을 기계적·전기적으로 결합한 중간 제품이다. 고객사의 차량 설계와 시스템 요구에 따라 구성과 인터페이스가 달라질 수 있으므로, 모듈은 셀과 별도의 제품·프로젝트 엔티티로 관리한다. SK온 공식 홈페이지는 ESS와 자동차용 사업에서 모듈 단위 제품 제공을 명시한다. ([SK On][4])

### 2.3.3 배터리 팩

차량에 탑재 가능한 시스템 단위로, 셀·모듈·구조물·열관리·제어·안전부품 등이 결합된다. SK온이 모든 고객에게 동일 범위의 팩을 공급한다고 단정할 수는 없으므로, 고객별 공급범위는 D08에서 계약·차량 플랫폼 단위로 확인해야 한다. 공식 홈페이지는 셀부터 모듈·팩까지 고객 요구에 맞춘 형태를 제공한다고 설명한다. ([SK On][3])

---

## 2.4 배터리 화학계 포트폴리오

### NCM

NCM은 니켈·코발트·망간을 주요 양극 구성요소로 활용하는 배터리 계열이다. SK온은 하이니켈 기술을 전기차 배터리의 대표적인 기술 기반으로 제시하며, 과거 NCM9+ 등 니켈 비중을 높인 제품을 공개했다. ([SK On][5])

### LFP

SK온은 LFP 배터리를 전기차와 ESS 포트폴리오 확장 수단으로 개발·사업화하고 있다. 2024년 공식 전시자료에서는 저온 성능을 개선한 `Winter Pro LFP` 기술을 공개했으며, 2025년에는 북미 ESS 시장을 겨냥한 LFP 양극재 공급망 구축과 현지 생산계획을 발표했다. ([SK On][6])

### VIB

VIB, 즉 바나듐이온배터리는 현재 SK온이 독자적으로 대규모 양산하는 기존 주력 셀이라기보다 ESS 포트폴리오를 확장하기 위한 공동개발 영역이다. SK온과 SK이노베이션은 2026년 Standard Energy와 고안전성 VIB 기반 ESS 공동개발 협약을 체결하며 ESS 화학계 포트폴리오를 NCM·LFP·VIB로 확대한다고 발표했다. ([ASK Inno][7])

### 화학계 상태 테이블

| Chemistry ID | 화학계   |   EV 적용 | ESS 적용 | 현재 상태 | Fact Status   |
| ------------ | ----- | ------: | -----: | ----- | ------------- |
| `CHEM-NCM`   | NCM   |      핵심 |     적용 | 상용·주력 | Official      |
| `CHEM-LFP`   | LFP   |   개발·확장 | 상용화 추진 | 성장    | Official      |
| `CHEM-VIB`   | 바나듐이온 | 확인되지 않음 |   공동개발 | 개발    | Official Plan |
| `CHEM-ASSB`  | 전고체   |  차세대 후보 |    미확정 | 연구개발  | R&D Domain    |

전고체전지 등 차세대 기술은 사업 포트폴리오 후보로 볼 수 있지만, 현재 상용 매출사업과 동일하게 분류해서는 안 된다. 세부 기술상태는 D04와 D05에서 검증한다.

---

## 2.5 고객 및 거래구조

전기차 배터리사업의 기본 거래구조는 완성차 기업을 대상으로 하는 장기 B2B 공급과 공동개발이다. 자동차 배터리는 특정 차량 플랫폼의 공간, 전압, 성능, 안전, 충전, 원가 요구에 맞추어 개발되기 때문에 범용 완제품 판매보다 고객 프로젝트 중심의 사업구조가 강하다.

다만 위 설명 중 자동차산업의 일반적 거래특성은 `industry_context`이며, 개별 고객별 계약기간·공급량·가격·개발범위는 공개된 공식자료가 있을 때만 `official_fact`로 저장한다.

### 거래구조 엔티티

```text
OEM Request
→ Battery Specification Development
→ Validation and Qualification
→ Supply Agreement
→ Production Capacity Allocation
→ Serial Production
→ Quality and Warranty Management
```

### 데이터 상태

```yaml
business_model_type:
  - B2B
  - project_based_supply
  - long_term_supply
  - joint_development_possible
customer_relationship_status:
  - nomination
  - development
  - contract
  - validation
  - mass_production
  - completed
  - suspended
```

---

## 2.6 지역 포트폴리오

전기차 배터리사업은 북미, 유럽, 중국 및 한국을 중심으로 생산·공급 구조를 형성해 왔다. SK온은 글로벌 주요 시장에 생산거점을 구축하고 현지 고객 대응력을 확대해 왔으며, 과거 공식 ESG 자료는 미국·유럽·중국을 중심으로 배터리 생산능력을 확대하는 전략을 설명했다. ([SK Innovation][8])

지역별 사업의 구체적인 고객, 법인, 공장, 생산능력과 가동상태는 D07과 D08에서 별도 검증한다. D02에서는 지역을 사업 포트폴리오 차원에서 다음과 같이 분류한다.

| Region ID   | 지역 | 전략적 역할                      |
| ----------- | -- | --------------------------- |
| `REG-KR`    | 한국 | 연구개발·기술·국내 생산기반             |
| `REG-NA`    | 북미 | 현지 생산·OEM 공급·정책 인센티브·ESS 확장 |
| `REG-EU`    | 유럽 | 유럽 완성차 고객 대응·현지 생산          |
| `REG-CN`    | 중국 | 생산·현지 시장 및 공급망 연계           |
| `REG-OTHER` | 기타 | 신규 고객·시장 탐색                 |

---
