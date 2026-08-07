---
id: skon-d03-d03-11-human-readable-report-baas-portfolio-6
title: Human-Readable Report — BaaS Portfolio
summary: "배터리 모니터링에서 진단, 수명 예측, 잔존가치 평가를 거쳐 재활용 의사결정을 지원하는 SK온 BaaS의 서비스 구조와 향후 생태계 확장 방향을 설명한다."
tags: [d03, product, schema, "xref:d17"]
keywords: [배터리 모니터링, 배터리 진단, SOH, 수명 추정, 잔존가치 평가, 데이터 인프라, 재활용, 배터리 서비스, BaaS, 잔여수명 추정, 이상 감지, 재활용 의사결정, 생태계 연결, ESS]
related: []
priority: normal
domain: D03
section: D03-11.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Human-Readable Report
tokens: 509
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Human-Readable Report

## 11.4 BaaS Portfolio

SK온의 BaaS는 배터리 판매 이후의 데이터와 생애주기를 서비스 사업으로 연결하는 구조다. 공식 사업 페이지는 배터리 모니터링을 B2B와 B2C 고객에게 제공하고 OEM, 시스템 통합사 및 기타 생태계 참여자와 BaaS 네트워크를 구축하는 방향을 제시한다. ([SK On][3])

BaaS의 핵심 기능은 다음과 같이 구조화된다.

```text
Battery data
  ↓
Monitoring
  ↓
Diagnosis
  ↓
SOH / remaining-life estimation
  ↓
Residual-value assessment
  ↓
Continue use / repair / reuse / recycle
```

### 주요 서비스 엔티티

```yaml
services:
  - Battery Monitoring Service
  - Battery Diagnosis Service
  - Abnormality Detection
  - Remaining Useful Life Estimation
  - Residual Value Assessment
  - Reuse Decision Support
  - Recycling Decision Support
```

D03에서는 BaaS 기술과 과거 협력 프로젝트의 존재는 `FACT`로 관리하지만, 플랫폼 전체가 현재 대규모 유료서비스로 운영되고 있다는 주장은 하지 않는다. 현재 매출, 고객 수, 진단 건수 및 API 사용량은 공개자료에서 확인되지 않았다.

### D17 연결 가치

BaaS는 향후 배터리 제조사 단독 서비스보다 금융회사, 중고차 플랫폼, 보험사, 플릿 운영사, ESS 사업자 및 재활용기업을 연결하는 데이터 인프라로 발전할 가능성이 있다. 이 부분은 제품 사실이 아니라 D17에서 검토할 **분석 가설**이다.

---
