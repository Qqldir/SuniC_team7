---
id: skes-d04-2-2-가스발전-chp-열망
title: 가스발전·CHP·열망
summary: SK이노베이션의 가스복합발전·열병합발전 설비 운영에 필요한 성능진단·예지보전·최적화 등 7가지 핵심기술의 개발 현황과 우선순위
tags: [d04, technology, table]
keywords: [가스터빈, HRSG, 예지보전, 성능진단, 경제급전, 열병합발전, 열수요, CEMS, 효율, 신뢰성]
related: [TECH-ENS-PWR-01, TECH-ENS-PWR-02, TECH-ENS-PWR-03, TECH-ENS-PWR-04, TECH-ENS-PWR-05, TECH-ENS-PWR-06, TECH-ENS-PWR-07]
priority: normal
domain: D04
section: 2.2
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 583
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.2 가스발전·CHP·열망

E&S는 광양·파주·여주 가스복합과 하남·위례 CHP를 운영한다. 발전기술의 O/I 초점은 신규 발전방식보다 기존 가스터빈·HRSG·증기터빈·열망의 효율과 신뢰성이다. ([SRC-ENS-D04-0001])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-PWR-01` | 가스터빈 성능진단 | L3 | 부하, 연료, 배기가스, 온도·압력 | 성능저하·세정·정비 권고 | heat rate, 출력 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-02` | 회전체 예지보전 | L1/L3 | 진동, 음향, 윤활유, 온도 | 고장확률·잔여수명 | 비계획정지, MTBF | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-03` | HRSG·열교환 성능 최적화 | L2/L3 | 증기·급수·배기가스, 오염 | 운전·세정·정비 권고 | 종합효율, 압력손실 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-04` | 발전계획·경제급전 분석 | L3/L4 | SMP, LNG원가, 수요, 기상, 정비 | 기동정지·부하계획 | 마진, 가동률 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-05` | CHP 전기·열 동시최적화 | L2/L3 | 전력가격, 열수요, 축열, 설비제약 | 전력·열 생산계획 | 종합효율, 열손실 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-06` | 열수요·배관손실 예측 | L3 | 기상, 건물, 공급·환수온도, 유량 | 열공급·펌프·온도계획 | 예측오차, 손실률 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-PWR-07` | 배출·용수·대기오염 실시간 관리 | L1/L5 | 연료, CEMS, 용수, 폐수, NOx·SOx·PM | 경보·보고·운전지원 | 배출원단위, 용수원단위 | `OPERATING_CONFIRMED` | 중상 |
