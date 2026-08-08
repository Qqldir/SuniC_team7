---
id: skes-d08-7-fuel-to-power-and-mro-supply-chain
title: Fuel-to-Power and MRO Supply Chain
summary: "발전소의 연료와 설비별 부품 공급망 구조, 중요도별 재고정책 분류, MRO 디지털 스레드 연결 방법을 설명한다."
tags: [d08, supply-chain, table, "xref:d06"]
keywords: [LNG, 가스터빈, 중요부품, 재고정책, MRO, 디지털스레드, 부품공동화, 장기납기, 정비계획, LTSA]
related: []
priority: normal
domain: D08
section: 7
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 684
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 7. Fuel-to-Power and MRO Supply Chain

## 7.1 Power-Plant Supply Architecture

| Layer | 주요 품목/서비스 | D06 연결 | 공개상태 |
|---|---|---|---|
| fuel | LNG/pipeline gas·metering | PWR-001/003 | source route partial |
| gas turbine | hot-section·filters·controls·LTSA | PWR-002/003/008 | OEM/terms internal |
| HRSG | tubes·valves·burner·inspection | PWR-004/008 | vendor internal |
| steam turbine | blade·seal·lube·inspection | PWR-005/008 | vendor internal |
| cooling/water | chemicals·resin·membrane·lab | PWR-005/007 | vendor internal |
| emissions | CEMS·catalyst·reagent·calibration | PWR-007 | vendor internal |
| electrical | transformer·breaker·relay·UPS | PWR-002/006/008 | vendor internal |
| outage service | field engineer·NDT·crane·scaffold | PWR-008 | contractor internal |

## 7.2 Critical-Spare Policy

| Criticality | 판정 | 재고정책 | 승인 |
|---|---|---|---|
| A1 | 고장 시 발전정지, lead time > outage tolerance | 현장/공동 pool 필수 | plant+central |
| A2 | 출력저하·안전 barrier 영향 | min-max+repair loop | plant |
| B | 계획정비 시 필요, 대체 가능 | forecast order | maintenance |
| C | 범용·단기조달 | vendor managed/spot | buyer |

## 7.3 MRO Digital Thread

`equipment serial → BOM → failure mode → spare part → approved vendor → PO → receipt inspection → warehouse bin → reservation → work order → installation serial → removed-part repair → warranty claim`

이 연결이 끊기면 같은 부품을 과잉구매하거나, 다른 revision을 설치하거나, 보증 회수 가능 부품을 폐기할 수 있다. D17에서는 발전소별 ERP·EAM 데이터를 먼저 표준화한 뒤 최적재고를 계산해야 한다.

## 7.4 Fuel and Spare O/I Questions

1. 발전수요와 LNG 재고를 같은 horizon에서 계획하는가.
2. GT별 heat-rate 변화가 연료 nomination에 반영되는가.
3. 동일 OEM 설비 간 critical spare 공동재고가 가능한가.
4. 장기납기 부품의 failure probability와 outage cost가 발주점에 반영되는가.
5. repairable part의 repair loop와 warranty claim이 추적되는가.
6. contractor performance가 작업위험·재작업·outage 연장과 연결되는가.

---
