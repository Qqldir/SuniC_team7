---
id: skon-d03-d03-05-application-mapping-012-individual-ev-ba-14
title: Application Mapping — 012 — Individual EV Battery Monitoring
summary: "개인 EV 소유자를 위한 배터리 모니터링 애플리케이션(APP-SKON-012)의 서비스 구성, 배포 채널, 제공 기능, 파트너 정보를 정리한 문서."
tags: [d03, product, schema]
keywords: [BAAS, 배터리 에즈 어 서비스, 배터리 진단, 전기차 충전, 운전 습관 분석, 배터리 잔여수명, Battery Management, APP-SKON-012, EV 소유자, 차량 배터리 모니터링, EV 배터리 모니터링, 배터리 상태 관리, 개인용 전기차, 수명 예측, 충전 이력, EV 인프라, Mycle, 배터리 서비스]
related: []
priority: normal
domain: D03
section: D03-05.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Application Mapping
tokens: 168
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Application Mapping

## APP-SKON-012 — Individual EV Battery Monitoring

```yaml
application_id: APP-SKON-012
application_name: Individual EV Battery Monitoring
application_type: BAAS
maturity: PILOT_AND_PARTNER_SERVICE

mapped_services:
  - SERV-SKON-BAAS-001
  - SERV-SKON-BAAS-002

delivery_channels:
  - EV Infra
  - Mycle

customer:
  type: Individual EV Owner

outputs:
  - Battery condition
  - Remaining life indication
  - Abnormality information
  - Charging history
  - Driving habit score
  - Weather-dependent driving range

partners:
  - SoftBerry
  - SK Rent-a-car
  - Macarong Factory

confidence: HIGH
```

---
