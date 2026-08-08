---
id: skes-d04-2-8-ev-충전
title: EV 충전
summary: "EV 충전 운영을 위한 원격관제, 수요분석, 부하관리, 결제·로밍 등 4가지 기술의 요구사항과 KPI를 정의한 기술 마스터"
tags: [d04, technology, table]
keywords: [원격관제, 수요분석, 부하관리, 스마트충전, 로밍, 기술요구사항, 가동률, 입지분석]
related: [TECH-ENS-EVC-01, TECH-ENS-EVC-02, TECH-ENS-EVC-03, TECH-ENS-EVC-04]
priority: normal
domain: D04
section: 2.8
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 386
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.8 EV 충전

E&S는 주차시설 중심으로 EV 충전사업을 확대한다고 설명한다. 충전기 수·권역·세부 운영주체는 공개자료 Gap이므로, D04는 운영기술 요구사항만 정의한다. ([SRC-ENS-D04-0006])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-EVC-01` | 충전기 원격관제·고장진단 | L2/L3 | 세션, 전압·전류, 오류코드, 통신 | 장애분류·원격복구·출동 | 가동률, MTTR | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-EVC-02` | 수요·대기·입지 분석 | L3 | 주차·충전이력, 체류, 교통, 주변수요 | 증설·배치·예약 | 이용률, 대기시간 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-EVC-03` | 부하관리·스마트충전 | L2/L3 | 건물부하, 요금, 충전수요, 변압기 | 충전전력·시간대 | 피크, 전력비, 완충률 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-EVC-04` | 결제·로밍·고객지원 | L4 | 회원, 세션, 결제, 로밍, 민원 | 인증·과금·환불·상담 | 결제성공률, 민원 | `CAPABILITY_CONFIRMED` | 중상 |
