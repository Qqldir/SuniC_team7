---
id: skes-d17-d17-11-value-measurement-double-count-control
title: Value Measurement & Double-Count Control
summary: "에너지 사업별 편익의 물리·경제·안전 측정지표와 이중계상 방지 원칙, 금융검증 단계를 정의한 문서."
tags: [d17, oi-portfolio, table]
keywords: [편익측정, 이중계상, 가치분모, LNG, 발전, BESS, Benefit State, 금융검증]
related: []
priority: normal
domain: D17
section: D17-11
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 778
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-11 Value Measurement & Double-Count Control

## 1. 사업별 공통 가치 분모

| 사업 | 물리 분모 | 경제 분모 | 안전/리스크 분모 |
|---|---|---|---|
| LNG | Cargo·MMBtu/GJ·tank inventory | landed KRW/GJ·demurrage·working capital | stockout/constraint breach |
| Power | net MWh·GJ fuel·start | KRW/MWh·dispatch margin | forced outage hour·trip |
| CHP | MWh + GJ heat | joint margin | heat SLA violation |
| City Gas | received/sold gas·customer | UFG value·cost/customer | leak/excavation exposure |
| Renewable/PPA | generated/delivered MWh | captured price·imbalance·settlement | curtailment/delay |
| BESS | MWh throughput·EFC·available MW | lifecycle net margin | SOH loss·thermal event precursor |
| EV Charging | paid kWh·port·session | contribution margin/site | outage/overload/SLA |
| LH2 | produced/sold/paid kg | KRW/paid-kg·inventory cash | barrier impairment·unaccounted kg |
| CCS | firm injected/verified tCO2 | margin/tCO2·liability-adjusted NPV | injectivity/MMV/long-tail liability |
| O/I | PoC·asset·period | Finance-verified cash | avoided risk는 별도 표시 |

## 2. Benefit State

```text
IDEA
→ BASELINE_DEFINED
→ TECHNICALLY_VALIDATED
→ PILOT_MEASURED
→ FINANCE_MODELLED
→ FINANCE_VERIFIED
→ CASH_REALIZED
→ SCALED
```

`FINANCE_VERIFIED` 전에는 “절감했다/벌었다”가 아니라 **편익가설 또는 PoC 측정값**이라고 표시한다.

## 3. 이중계상 방지 예시

- `Heat rate 개선`, `연료절감`, `탄소배출 감소`, `발전마진 개선`이 같은 GJ 절감에서 나오면 한 Benefit Group으로 묶고 현금효과를 한 번만 계산한다.
- LNG `demurrage 감소`와 `재고최적화`가 같은 Cargo schedule change에서 생기면 변화원인을 lineage로 연결한다.
- BESS `gross revenue uplift`와 `lifecycle margin uplift`를 더하지 않는다. 후자가 전자를 포함하면 lifecycle 기준만 사용한다.
- LH2 `BOG 감소`, `sold kg 증가`, `cost/kg 감소`가 같은 recovered kg이면 한 물리 Benefit에서 파생된 것으로 연결한다.
- 48E `eligible basis`, `accounting recognition`, `transfer proceeds`, `cash receipt`을 여러 편익으로 합산하지 않는다.
- CAPEX 회피와 감가상각 감소가 같은 투자중단에서 발생하면 NPV 한 건으로 계산한다.
- 안전가치는 임의 화폐화하지 않고 Barrier/KRI 개선을 별도 보고하며 보험·손실회피 현금이 실제 검증된 경우만 Finance layer에 연결한다.

---
