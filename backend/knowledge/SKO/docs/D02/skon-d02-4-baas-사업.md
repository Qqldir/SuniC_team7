---
id: skon-d02-4-baas-사업
title: BaaS 사업
summary: "SK온의 BaaS 사업 정의, 배터리 생애주기 전체 가치사슬, 진단·렌탈·충전·재사용·재활용 서비스 및 사업모델 구조와 수익원 가설을 설명하는 문서다."
tags: [d02, business, table]
keywords: [Battery as a Service, 배터리 렌탈, 배터리 진단, 충전 서비스, 재사용, 재활용, 배터리 생애주기, 배터리 모니터링, 가치사슬, 잔존가치, 생애주기, 모니터링, 재사용·재활용, 수익 모델, 플랫폼]
related: [BUS-SKON-BAAS-001]
priority: normal
domain: D02
section: 4
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 1446
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# 4. BaaS 사업

## 4.1 사업 정의

| 필드          | 데이터                           |
| ----------- | ----------------------------- |
| Business ID | `BUS-SKON-BAAS-001`           |
| 공식 사업명      | BaaS                          |
| 영문명         | Battery as a Service          |
| 사업유형        | 데이터·플랫폼·서비스                   |
| 주요 대상       | 배터리 사용자와 생애주기 참여자             |
| 서비스 범위      | 렌탈·충전·진단·수명관리·재사용·재활용         |
| 핵심 데이터      | 배터리 상태·사용이력·수명·잔존가치           |
| 사업단계        | 구축·확장                         |
| 포트폴리오 역할    | Emerging / Lifecycle Business |

SK온 공식 BaaS 소개는 배터리 렌탈, 충전, 재사용, 재활용을 포함한 배터리 생애주기 전반의 서비스를 제공한다고 설명한다. 또한 배터리 상태를 실시간으로 모니터링하고 사용습관을 분석해 배터리 수명과 상태를 관리하는 플랫폼 개념을 제시한다. ([SK On][11])

---

## 4.2 BaaS 가치사슬

```text
Battery Production
→ Vehicle or ESS Use
→ Real-time Monitoring
→ State and Life Diagnosis
→ Charging Service
→ Rental or Financing
→ Collection
→ Residual Value Assessment
→ Reuse
→ Recycling
```

공식 홈페이지는 BaaS 흐름을 `Rental → Recharge → Reuse → Recycling`으로 표현하고 있으며, 상태 모니터링과 수명관리를 플랫폼의 핵심 기능으로 설명한다. ([SK On][11])

---

## 4.3 BaaS 세부 서비스

### 4.3.1 배터리 진단

차량 또는 시스템에서 수집된 데이터를 활용해 배터리의 현재 상태와 수명을 분석하는 서비스다. SK온은 과거 외부 협력 프로젝트에서도 BaaS 분석기술을 활용해 배터리 상태와 수명을 실시간으로 측정한다고 설명했다. ([SK On][12])

### 4.3.2 배터리 렌탈

배터리를 차량과 분리된 서비스 자산으로 제공하는 모델이다. 공식 BaaS 페이지가 렌탈을 서비스 구성요소로 제시하지만, 기준일 현재 국가·차종별 대규모 상용화 규모는 공식 홈페이지만으로 확인하기 어렵다. 따라서 `official_service_scope`로 저장하되 `commercial_scale`은 별도 검증한다. ([SK On][11])

### 4.3.3 충전 서비스

배터리 사용과 충전을 연결해 고객 편의성과 상태관리를 높이는 서비스 영역이다. 공식 페이지는 충전을 BaaS 생애주기의 구성요소로 포함한다. 직접 충전사업자 역할인지, 충전사업자와의 데이터·플랫폼 협력인지 프로젝트별로 구분해야 한다. ([SK On][11])

### 4.3.4 재사용

전기차에서 사용된 배터리의 잔존성능을 평가해 ESS 등 다른 용도로 활용하는 영역이다. 공식 BaaS 포트폴리오에 재사용이 포함되지만, 실제 재사용 제품의 소유권·운영주체·판매모델은 개별 프로젝트 기준으로 저장한다. ([SK On][13])

### 4.3.5 재활용

수명이 종료된 배터리에서 리튬·니켈·코발트 등 자원을 회수해 배터리 가치사슬에 재투입하는 영역이다. 공식 BaaS 페이지는 재활용을 생애주기 서비스 범위에 포함한다. SK온이 직접 수행하는 공정과 외부 재활용 파트너에게 맡기는 범위는 D10과 D14에서 구분한다. ([SK On][13])

---

## 4.4 BaaS 사업모델 구조

```text
Data Acquisition
→ Battery Diagnosis
→ Decision Support
→ Financial or Operational Service
→ Residual Value Creation
→ Reuse or Recycling
```

### 잠재 수익원 분류

다음 항목은 데이터베이스 설계를 위한 `business_model_hypothesis`이며, 모두 SK온의 공식 매출원으로 확정된 것은 아니다.

* 진단 서비스 수수료
* 데이터 분석 플랫폼 이용료
* 배터리 렌탈료
* 배터리 보증·잔존가치 관리
* 재사용 배터리 판매 또는 운영수익
* 재활용 자원 판매·회수수익
* 충전·모빌리티 파트너십 수익
* 금융·보험사 대상 배터리 데이터 서비스

공식 사업범위와 추정 수익모델은 반드시 분리한다.

---
