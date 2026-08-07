---
id: skes-d08-12-liquid-hydrogen-supply-chain
title: Liquid-Hydrogen Supply Chain
summary: "액화수소의 부생 생산부터 충전소 공급까지 전 단계의 물리적 흐름, 입력물·품질·공급 위험을 매핑하고 인천 플랜트의 3만 톤/년 명목능력 제약 요인을 규정하는 운영 가이드."
tags: [d08, supply-chain, table]
keywords: [부생수소, 정화·액화, 비등손실, 냉동저장, 질량수지, 수소충전소, 공급위험, LTSA, 인천플랜트, trailer용량]
related: []
priority: normal
domain: D08
section: 12
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 506
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 12. Liquid-Hydrogen Supply Chain

## 12.1 Physical Flow

`byproduct hydrogen source → custody meter → purification → liquefaction train → cryogenic storage → loading bay → tank trailer → hydrogen station storage → dispensing/customer`

## 12.2 Supply-Chain Record

| 단계 | 입력·공급품 | 핵심 품질/수량 | 공급 위험 | 데이터 gap |
|---|---|---|---|---|
| feed H₂ | 부생수소 | purity·pressure·flow·impurity | source outage | supplier/contract volume |
| purification | adsorbent/filter/spare | outlet purity·DP | media lead-time | OEM/BOM |
| liquefaction | refrigerant·compressor·expander | kWh/kg·availability | critical spare | OEM/LTSA |
| storage | vacuum tank·valve·sensor | level·BOR·vacuum | leak/boil-off | tank serial/spec |
| loading | arm/hose/meter | quantity·temperature | transfer loss | custody rule |
| transport | trailer·tractor·driver | route·ETA·pressure | accident/traffic | fleet/3PL |
| station | receiving/storage/pump | delivered/dispensed | station outage | customer inventory |

## 12.3 Nominal Capacity Guardrail

인천 플랜트의 3만 톤/년 명목능력은 실제 부생수소 계약량·liquefaction availability·출하수요·trailer capacity·충전소 수요에 의해 제한된다. D08은 `feed secured`, `produced`, `loaded`, `delivered`, `dispensed`, `boil-off/loss`를 별도 질량수지로 저장한다.

## 12.4 Hydrogen O/I Priorities

1. feed–production–station inventory 통합계획.
2. trailer routing과 충전소 stockout 위험 예측.
3. boil-off·transfer loss 원인분해.
4. cryogenic critical-spare lead-time 기반 재고.
5. purity deviation 조기탐지.
6. tanker/driver 자격·검사·운행 증빙 자동화.

---
