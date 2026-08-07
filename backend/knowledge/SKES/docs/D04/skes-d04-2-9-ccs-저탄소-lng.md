---
id: skes-d04-2-9-ccs-저탄소-lng
title: CCS·저탄소 LNG
summary: "저탄소 LNG 달성을 위해 필요한 탄소포집·압축·운송·저장·모니터링·검증의 6가지 핵심기술을 ID, 계층, KPI로 정의한 기술 명세표"
tags: [d04, technology, table]
keywords: [탄소포집저장, CO2 분리, 배관수송, 저장소 최적화, 누출감시, MRV, 탄소강도, 블루수소, 포집률, 플룸]
related: [TECH-ENS-CCS-01, TECH-ENS-CCS-02, TECH-ENS-CCS-03, TECH-ENS-CCS-04, TECH-ENS-CCS-05, TECH-ENS-CCS-06]
priority: normal
domain: D04
section: 2.9
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 545
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.9 CCS·저탄소 LNG

E&S는 Barossa–Darwin LNG–Bayu-Undan을 연계한 저탄소 LNG와 장기 블루수소 방향을 제시한다. 이는 계획 단계이므로 포집·운송·저장 성능을 확정하지 않는다. CCS 데이터는 저장량뿐 아니라 영구성·불확실성을 다루는 MRV가 필요하다. ([SRC-ENS-D04-0001], [SRC-ENS-D04-0011])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-CCS-01` | CO2 분리·포집 | L0/L2 | 유량, 조성, 압력, 흡수제, 에너지 | 포집운전·제품 CO2 | 포집률, 에너지페널티 | `PLANNED_OR_CONSIDERING` | 중상 |
| `TECH-ENS-CCS-02` | CO2 탈수·압축 | L0/L2 | 수분, 불순물, 압력, 유량 | 수송규격·압축운전 | 전력, 부식위험 | `PLANNED_OR_CONSIDERING` | 중상 |
| `TECH-ENS-CCS-03` | CO2 배관·선박 수송 | L0/L1 | 유량, 압력, 조성, 위치, 기상 | 수송·누출감시 | 손실, 가동률, 안전 | `PLANNED_OR_CONSIDERING` | 중 |
| `TECH-ENS-CCS-04` | 저장소 모델·주입 최적화 | L2/L3 | 지질, 압력, 주입량, 시추자료 | 주입률·압력·용량 | 저장량, injectivity | `PLANNED_OR_CONSIDERING` | 중상 |
| `TECH-ENS-CCS-05` | 누출·플룸 모니터링 | L1/L3 | 지진·압력·화학·원격탐사 | 플룸·이상·누출후보 | 탐지한계, 불확실성 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-CCS-06` | 전주기 MRV·탄소강도 원장 | L5 | 포집·수송·주입·누출·에너지·계약 | 검증량·탄소강도·감사추적 | 데이터완전성, 검증시간 | `PLANNED_OR_CONSIDERING` | 높음 |
