---
id: skes-d04-2-6-ess-계통제어
title: ESS·계통제어
summary: "ESS 운영에 필요한 배터리 관리, 충방전 최적화, 계통제어 등 7개 핵심 기술의 개발 상태, KPI, 입출력 데이터를 정의한 기술 마스터."
tags: [d04, technology, table]
keywords: [BMS, EMS, PCS, 에너지저장장치, 배터리 상태, SOC, SOH, 충방전 최적화, 계통제어, 열폭주경보]
related: [TECH-ENS-ESS-01, TECH-ENS-ESS-02, TECH-ENS-ESS-03, TECH-ENS-ESS-04, TECH-ENS-ESS-05, TECH-ENS-ESS-06, TECH-ENS-ESS-07]
priority: normal
domain: D04
section: 2.6
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 575
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.6 ESS·계통제어

E&S의 ESS 적용은 수요관리, 재생에너지 연계, 미국 계통안정화로 구분된다. DOE 자료는 BMS·EMS·PCS, 환경·안전제어, 예측분석의 통합을 핵심 시스템 구조로 설명한다. ([SRC-ENS-D04-0006], [SRC-ENS-D04-0009])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-ESS-01` | BMS SOC·SOH·셀불균형 추정 | L1/L3 | 전압, 전류, 온도, 이력 | SOC·SOH·경보 | 추정오차, 가용용량 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-ESS-02` | 열화·잔여수명 예측 | L3 | C-rate, DOD, 온도, cycle, 달력노화 | RUL·운영제약 | 수명, 교체비, 오차 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-ESS-03` | 열폭주 조기경보 | L1/L3 | 온도, 전압, 가스, 연기, 압력 | 위험점수·격리 권고 | 탐지선행시간, 오경보 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-ESS-04` | EMS 충방전 최적화 | L2/L3 | 부하, 가격, 발전예측, SOC, 열화 | 충방전 스케줄 | 절감·수익, 가용성 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-ESS-05` | PCS·인버터 계통제어 | L1/L2 | 전압, 주파수, 전류, 계통지령 | 유효·무효전력 제어 | 응답속도, 효율 | `OPERATING_CONFIRMED` | 중상 |
| `TECH-ENS-ESS-06` | 시장입찰·수익 스태킹 | L3/L4 | 가격·보조서비스, SOC, 열화, 제약 | 입찰·운전계획 | 수익, 페널티, 열화비 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-ESS-07` | 사고대응·디지털 안전기록 | L4/L5 | 경보, 이벤트, 점검, 작업, 소방연계 | 타임라인·대응절차·증빙 | 대응시간, 재발방지 | `ENABLING_CANDIDATE` | 높음 |
