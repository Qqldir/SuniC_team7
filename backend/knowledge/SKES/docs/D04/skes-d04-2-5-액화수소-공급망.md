---
id: skes-d04-2-5-액화수소-공급망
title: 액화수소 공급망
summary: 인천 액화수소플랜트에서 부생수소를 정제·액화하여 저장·운송·충전하는 전 공정의 7가지 핵심 기술과 극저온·boil-off 관리 현황을 정리한 표.
tags: [d04, technology, table]
keywords: [액화수소, 부생수소, 정제, 극저온, boil-off, 탱크로리, 충전소, 누출감지]
related: [TECH-ENS-H2-01, TECH-ENS-H2-02, TECH-ENS-H2-03, TECH-ENS-H2-04, TECH-ENS-H2-05, TECH-ENS-H2-06, TECH-ENS-H2-07]
priority: normal
domain: D04
section: 2.5
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 608
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.5 액화수소 공급망

인천 액화수소플랜트는 부생수소를 정제·액화해 저장·탱크로리 운송·충전소 공급으로 연결한다. 액화수소는 약 -253°C의 극저온이며 액화 에너지와 저장·이송 중 boil-off가 핵심 관리변수다. ([SRC-ENS-D04-0005], [SRC-ENS-D04-0008])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-H2-01` | 부생수소 정제·품질관리 | L0/L1 | 조성, 압력, 불순물, 유량 | 제품순도·공정조건 | 순도, 회수율 | `OPERATING_CONFIRMED` | 중상 |
| `TECH-ENS-H2-02` | 수소 액화 사이클 최적화 | L2/L3 | 압축기·팽창기, 온도, 압력, 전력 | 운전점·병목·효율 | kWh/kg-H2, 생산량 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-H2-03` | 극저온 탱크 열침입·BOG 예측 | L1/L3 | 압력, 온도, 레벨, 외기, 체류시간 | boil-off·venting 예측 | 손실률, dormancy | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-H2-04` | BOG 회수·재액화·활용 | L0/L2 | BOG 유량·조성·압력, 수요, 전력 | 회수경로·운전계획 | 회수율, 에너지비 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-H2-05` | 탱크로리 배차·재고 최적화 | L3/L4 | 플랜트·충전소 재고, 주문, 위치, 교통 | 생산·배송·회수계획 | 품절, 운송비, km/kg | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-H2-06` | 충전소 수요·가동률 예측 | L3 | 차량·충전이력, 노선, 요일, 고장 | 재고·충전·정비계획 | 대기, 품절, 가동률 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-H2-07` | 수소 누출·화재 통합감지 | L1/L2 | H2센서, 열·불꽃, 환기, 영상 | 다중센서 경보·격리 권고 | 탐지시간, 오경보 | `OPERATING_CONFIRMED` | 높음 |
