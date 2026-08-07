---
id: skes-d16-7-build-buy-partner-decision-framework
title: Build / Buy / Partner Decision Framework
summary: 기술 도입 시 자체개발·구매·협력 중 최선의 방식을 판단하는 10가지 의사결정 기준과 통합 아키텍처 참고안
tags: [d16, ecosystem, table, "xref:d01", "xref:d17"]
keywords: [자체개발, 라이선싱, 외부협력, 기술도입, vendor lock-in, OEM, CMMS, PoC, 데이터권리, 의사결정]
related: [BBP-01, BBP-02, BBP-03, BBP-04, BBP-05, BBP-06, BBP-07, BBP-08, BBP-09, BBP-10]
priority: normal
domain: D16
section: 7
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 578
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 7. Build / Buy / Partner Decision Framework

| Decision ID | 질문 | Build 선호 | Buy 선호 | Partner 선호 |
|---|---|---|---|---|
| `BBP-01` | 경쟁우위 핵심 로직인가 | 예: LNG portfolio logic | 범용 CMMS | 공동 IP 가능 |
| `BBP-02` | 물리/도메인 모델이 희소한가 | 내부 운전지식 | 검증된 OEM model | 엔지니어링사 co-build |
| `BBP-03` | 안전인증 필요인가 | 제한적 | 인증제품 | 인증사+통합사 |
| `BBP-04` | 데이터권리가 복잡한가 | 내부 graph | 표준 connector | JV/OEM 협약 |
| `BBP-05` | 빠른 PoC가 중요한가 | thin layer | SaaS | vendor sandbox |
| `BBP-06` | vendor lock-in 위험이 큰가 | canonical data model | export 보장 제품 | multi-vendor architecture |
| `BBP-07` | 24/7 support 필요한가 | 내부 NOC 가능 시 | enterprise SLA | OEM+local partner |
| `BBP-08` | 모델 drift가 큰가 | 내부 MLOps | managed service | shared monitoring |
| `BBP-09` | 규제해석 책임이 큰가 | legal-owned rules | legal tech | law/tax advisory partner |
| `BBP-10` | OT write 권한이 필요한가 | control owner | certified system | staged integration |

# 8. Reference Integration Architecture

```text
External Data
  ├─ LNG/price/AIS/weather/grid/regulation
  └─ vendor intelligence / standards
             ↓
Authoritative Data Layer
  ├─ OT historian / SCADA / BMS / EMS
  ├─ CMMS / EAM / ERP / CLM / GIS / CRM
  └─ D01~D16 canonical IDs + timestamps + lineage
             ↓
Analytics / Twin / AI Sandbox
  ├─ read-only feature layer
  ├─ physics / statistical / ML models
  └─ RAG / KG / scenario engine
             ↓
Decision Layer
  ├─ recommendation + confidence + evidence
  ├─ human approval / MOC / legal / tax / CISO gate
  └─ bounded action / work order / alert
             ↓
Outcome Store
  ├─ KPI / avoided failure / false positive
  ├─ override / incident / model drift
  └─ D17 learning loop
```
