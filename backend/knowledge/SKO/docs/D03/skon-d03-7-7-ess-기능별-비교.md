---
id: skon-d03-7-7-ess-기능별-비교
title: ESS 기능별 비교
summary: "SK온·CATL·삼성SDI·Tesla의 에너지저장장치 안전, 용량, 진단 기술을 비교한 스펙표로, 각사의 기술 특징과 컨테이너 용량, 모니터링 기능을 담고 있다."
tags: [d03, product, schema, table]
keywords: [ESS, GRIDON, TENER, SBB, Megapack, 안전기술, 용량, 진단기술, AI모니터링, 예측진단, 에너지저장장치, 배전지, 안전관리, 저장용량, CATL, 삼성SDI, 예지정비]
related: []
priority: normal
domain: D03
section: 7.7
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 533
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 7.7 ESS 기능별 비교

## Safety Layer

```text
SK On GRIDON
→ EIS predictive diagnosis
→ Coolant immersion
→ Dual-valve structure

CATL TENER
→ Cell chemistry and SEI control
→ End-to-end validation
→ AI risk monitoring
→ Early-warning operation

Samsung SBB
→ Enhanced Direct Injection
→ No Thermal Propagation
→ Vent and fuse structure
→ AI predictive maintenance

Tesla Megapack
→ Integrated product architecture
→ Site-level monitoring and control
→ Utility project operating experience
```

삼성SDI는 EDI를 이용해 컨테이너 내 화재 확산을 억제하고, 각형 셀에 No-TP·벤트·퓨즈 구조를 적용한다. CATL은 셀 열화관리부터 운전 중 AI 조기경보까지 전 생애주기 안전관리체계를 강조한다. ([삼성SDI][11])

## Capacity Layer

```yaml
ess_container_capacity:

  CATL_TENER:
    value: 6.25
    unit: MWh
    boundary: 20-foot container

  CATL_TENER_STACK:
    value: 9
    unit: MWh
    boundary: product architecture disclosed by CATL

  SAMSUNG_SBB_1_7:
    value: 6.14
    unit: MWh
    boundary: 20-foot container

  SK_ON_GRIDON_GEN_1:
    value: NOT_DISCLOSED

  SK_ON_GRIDON_GEN_2:
    value: 15_percent_higher_than_previous_generation
    absolute_value: NOT_DISCLOSED
```

## Diagnostic Layer

| 기업    | 진단기술      | 데이터 수준 | 공개된 기능         |
| ----- | --------- | ------ | -------------- |
| SK온   | EIS BMS   | 셀·시스템  | 상태분석·예측진단      |
| CATL  | AI 위험모니터링 | 제품·현장  | 조기경보·수명주기 위험관리 |
| 삼성SDI | AI 알고리즘   | 시스템    | 예지정비·내구수명 예측   |
| Tesla | 통합 운영 SW  | 사이트·플릿 | 전력운영·원격관리      |

---
