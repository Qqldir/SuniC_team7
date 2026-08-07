---
id: skes-d08-11-evercharge-ev-charging-supply-chain
title: EverCharge EV-Charging Supply Chain
summary: "EverCharge 전기차 충전 공급망의 수직통합 운영 모델, EVSE 부품별 추적·위험 요소 표, 다단계 공급사 리스크 관리 방안"
tags: [d08, supply-chain, table]
keywords: [EVSE, BOM, 공급사 리스크, 부품 추적, 펌웨어, SBOM, 충전 인프라, 공급망 최적화]
related: []
priority: normal
domain: D08
section: 11
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 426
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 11. EverCharge EV-Charging Supply Chain

## 11.1 Operating Model

EverCharge는 EVSE hardware·SmartPower software·설계·설치·운영지원의 수직통합형 공급자이며, 2022년 Hayward에 약 30,000ft² 생산시설을 확대했다. 그러나 반도체·전력모듈·connector·cable·meter 등 tier-2 부품 공급사와 원산지는 공개자료에서 확인되지 않으므로 내부 BOM·AVL이 필요하다.

## 11.2 EVSE Genealogy

| Layer | 필수 추적필드 | 실패/공급 위험 |
|---|---|---|
| power electronics | maker·lot·rating·firmware | shortage·thermal failure |
| connector/cable | type·lot·cycle rating | wear·standard change |
| meter | serial·accuracy·certification | billing dispute |
| controller | board serial·OS·SBOM | cyber·obsolescence |
| mesh network | radio·firmware·topology | interoperability |
| enclosure | material·IP/NEMA·factory test | ingress·corrosion |
| SmartPower | software version·policy | allocation error |
| site installation | panel·circuit·permit·installer | schedule·rework |

## 11.3 Procurement/OI Priorities

- multi-tier BOM risk와 end-of-life 예측.
- 현장고장–부품lot–공급사 연결.
- installer별 재방문·commissioning 실패 분석.
- spare pool과 first-time-fix 최적화.
- component 대체 시 firmware·인증·열설계 영향 자동검토.
- 공급사 remote access와 SBOM 취약점 관리.

---
