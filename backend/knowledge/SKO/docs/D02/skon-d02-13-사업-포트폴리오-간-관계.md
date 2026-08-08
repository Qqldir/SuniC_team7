---
id: skon-d02-13-사업-포트폴리오-간-관계
title: 사업 포트폴리오 간 관계
summary: "SK온의 EV배터리, ESS, 트레이딩, 열관리 등 주요 사업들이 데이터, 배터리 재사용, 소재조달을 통해 어떻게 연결되는지 보여주는 포트폴리오 관계도"
tags: [d02, business]
keywords: [EV Battery, ESS Battery, BaaS, 배터리 재사용, 배터리 재활용, 열관리, 배터리 화학, 소재조달, 공급망, Second-life, EV배터리, ESS배터리, 배터리 생애주기, 재사용 배터리, 열관리 솔루션, 원자재 조달, 트레이딩]
related: []
priority: normal
domain: D02
section: 13
source: SK온_D02_Business_Portfolio.md
breadcrumb: ""
tokens: 355
updated: 2026-08-03
---

> SK온 · D02 사업 포트폴리오

# 13. 사업 포트폴리오 간 관계

## 13.1 핵심 관계 그래프

```text
EV Battery
  ├─ GENERATES_DATA → BaaS
  ├─ GENERATES_USED_BATTERY → Reuse
  ├─ GENERATES_END_OF_LIFE_BATTERY → Recycling
  ├─ REQUIRES_THERMAL_MANAGEMENT → Cooling Solutions
  └─ SHARES_MANUFACTURING_ASSET_WITH → ESS Battery

ESS Battery
  ├─ USES_CHEMISTRY → NCM
  ├─ USES_CHEMISTRY → LFP
  ├─ DEVELOPS_CHEMISTRY → VIB
  ├─ USES_LIFESPAN_MANAGEMENT → BaaS Capability
  └─ REUSES_EV_BATTERY_POTENTIALLY → Second-life ESS

Trading
  ├─ PROVIDES_MARKET_INTELLIGENCE → Material Procurement
  ├─ SUPPORTS_LOGISTICS → Supply Chain
  └─ CONNECTS_TO → Terminal

Lube Base Oil
  └─ EXTENDS_TO → Thermal Management

Thermal Management
  ├─ APPLIES_TO → EV Battery
  ├─ APPLIES_TO → ESS
  └─ APPLIES_TO → Data Center
```

`EV Battery → BaaS`, `EV·ESS용 배터리`, `배터리 생애주기 서비스`, `액침냉각과 배터리사업의 연계`는 공식자료로 뒷받침된다. 트레이딩 역량과 배터리 소재조달 간 연계, 재사용 배터리의 ESS 적용은 합리적인 전략적 연결이지만 구체적 실행은 별도 검증이 필요하다. ([SK On][3])

---
