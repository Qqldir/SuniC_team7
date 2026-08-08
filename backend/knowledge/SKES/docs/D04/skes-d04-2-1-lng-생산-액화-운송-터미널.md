---
id: skes-d04-2-1-lng-생산-액화-운송-터미널
title: LNG 생산·액화·운송·터미널
summary: "SK이노베이션 LNG 체인 전체 단계에서 10가지 핵심기술의 기술ID, 입출력 데이터, KPI, 상태를 정의한 마스터 테이블."
tags: [d04, technology, table]
keywords: [LNG, 가스전생산, 메탄누출, 액화공정, BOG, 선박최적화, 탱크계측, 극저온설비]
related: [TECH-ENS-LNG-01, TECH-ENS-LNG-02, TECH-ENS-LNG-03, TECH-ENS-LNG-04, TECH-ENS-LNG-05, TECH-ENS-LNG-06, TECH-ENS-LNG-07, TECH-ENS-LNG-08, TECH-ENS-LNG-09, TECH-ENS-LNG-10]
priority: normal
domain: D04
section: 2.1
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 796
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.1 LNG 생산·액화·운송·터미널

SK이노베이션 E&S의 공개 LNG 체인은 가스전, 액화설비, 전용선, 보령 터미널, 발전으로 이어진다. 따라서 기술 분류의 초점은 개별 설비 스펙보다 단계 간 생산·선박·재고·송출 데이터 연결이다. ([SRC-ENS-D04-0001])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-LNG-01` | 가스전 생산예측·저류층 모델 | L3 | 압력, 유량, 조성, 정비, 시추 | 생산계획·이상구간 | 생산량, decline 오차 | `ENABLING_CANDIDATE` | 중 |
| `TECH-ENS-LNG-02` | methane·가스 누출 LDAR | L1/L5 | 고정센서, 카메라, 드론·위성, 풍향 | 누출위치·배출량·정비지시 | 탐지시간, 누출감축 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-03` | 액화공정 성능·에너지 최적화 | L2/L3 | 유량, 조성, 압축기, 냉매, 전력 | 운전점·에너지 손실 | kWh/t-LNG, 수율 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-LNG-04` | 열교환기·압축기 상태진단 | L1/L3 | 온도, 압력, 진동, 접근온도 | 성능저하·정비시점 | 비계획정지, 효율 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-05` | LNG선 ETA·항로 최적화 | L3 | AIS, 기상, 항만, 속도, 연료 | ETA·항로·속도 | 지연, 연료, 배출 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-06` | 선박·터미널 일정 통합 | L4 | 계약, 선박ETA, berth, 탱크재고 | 하역·입출항 일정 | 대기시간, 재고충돌 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-07` | LNG BOG 예측·회수 최적화 | L2/L3 | 탱크압력·온도, 입출고, 조성, 기상 | 압축·재액화·연료사용 계획 | venting, BOG 손실 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-08` | 탱크 stratification·재고계측 | L1/L3 | 레벨, 온도층, 밀도, 조성 | usable inventory·rollover 경보 | 재고오차, 안전경보 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-LNG-09` | 기화·송출 최적화 | L2/L3 | 수요, send-out, 해수·열원, 펌프 | 기화기·펌프 운전 | 에너지, 송출신뢰도 | `CAPABILITY_CONFIRMED` | 중상 |
| `TECH-ENS-LNG-10` | 극저온 설비 누출·건전성 감시 | L1 | 가스, 온도, 압력, 밸브, 영상 | 경보·격리 권고 | 탐지시간, 오경보 | `ENABLING_CANDIDATE` | 높음 |
