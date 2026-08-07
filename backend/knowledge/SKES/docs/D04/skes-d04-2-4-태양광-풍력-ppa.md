---
id: skes-d04-2-4-태양광-풍력-ppa
title: 태양광·풍력·PPA
summary: 재생에너지 발전자산 운영(태양광·풍력)과 PPA 계약 관리에 필요한 8개 핵심 기술의 기능·입출력·KPI·현황을 정리한 표
tags: [d04, technology, table]
keywords: [발전예측, PPA 계약관리, SCADA, 상태감시, O&M 최적화, 정산관리, 원격점검, RE100, 인증서 추적]
related: [TECH-ENS-REN-01, TECH-ENS-REN-02, TECH-ENS-REN-03, TECH-ENS-REN-04, TECH-ENS-REN-05, TECH-ENS-REN-06, TECH-ENS-REN-07, TECH-ENS-REN-08]
priority: normal
domain: D04
section: 2.4
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 668
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.4 태양광·풍력·PPA

재생에너지는 발전자산 운영과 직접 PPA 계약·정산을 분리해 다룬다. E&S는 태양광·풍력, 직접 PPA, 비용분석 서비스를 운영하지만 DERMS·재생 O&M은 계획 상태다. ([SRC-ENS-D04-0003], [SRC-ENS-D04-0004])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-REN-01` | 태양광·풍력 발전예측 | L3 | 수치예보, 현장기상, SCADA, 가용성 | 단기·일전 발전량 | MAE, 정산·불균형비용 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-REN-02` | 태양광 이상·오염·음영 진단 | L1/L3 | 인버터, IV, 열화상, 기상, 영상 | 스트링·모듈 이상 | 손실발전량, 진단정확도 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-REN-03` | 풍력 상태감시·잔여수명 | L1/L3 | SCADA, 진동, 오일, 음향, 기상 | 블레이드·기어박스 이상 | downtime, 정비비 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-REN-04` | 드론·로봇 원격점검 | L1/L3 | RGB·열화상·LiDAR·위치 | 결함지도·정비후보 | 점검시간, 접근위험 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-REN-05` | O&M 작업·부품 최적화 | L4 | 결함, CMMS, 인력, 선박·차량, 부품, 기상 | 작업순서·자재·접근계획 | MTTR, 발전손실 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-REN-06` | PPA 부하·발전 시뮬레이션 | L3/L4 | 고객부하, 발전예측, 요금, 계약조건 | 비용·공급률·위험 시나리오 | RE100 충족률, 비용 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-REN-07` | PPA 자동정산·불균형 관리 | L4/L5 | 계량, 계약, 시장가, 부족·초과전력 | 정산서·이상·헤지 권고 | 정산오류, 처리시간 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-REN-08` | 전력·인증서 데이터 계보 | L5 | 발전·사용량, REC·인증서, 계약 | 증빙·감사추적 | 증빙시간, 중복·누락 | `ENABLING_CANDIDATE` | 중상 |
