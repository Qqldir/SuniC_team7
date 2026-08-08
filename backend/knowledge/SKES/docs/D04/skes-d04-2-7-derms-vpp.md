---
id: skes-d04-2-7-derms-vpp
title: DERMS·VPP
summary: "배전망 기반 분산자원 통합 운영을 위한 DERMS·VPP 기술 체계: 자산등록부터 정산까지 5가지 핵심 기술의 계층, 입출력, KPI, 추진 상태를 정의한 기술 마스터 표."
tags: [d04, technology, table]
keywords: [분산자원관리, DER, 배전망운영, DERMS, VPP, 상태추정, hosting capacity, 자산등록, 프로토콜상호운용, 정산]
related: [TECH-ENS-DER-01, TECH-ENS-DER-02, TECH-ENS-DER-03, TECH-ENS-DER-04, TECH-ENS-DER-05]
priority: normal
domain: D04
section: 2.7
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 499
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.7 DERMS·VPP

E&S는 Ensolve 배전망을 기반으로 DERMS 등을 추진하고 VPP는 검토한다고 설명한다. 따라서 아래 기술은 상용 배치가 아니라 최소기능 PoC 요구사항이다. NREL은 DERMS를 분산자원 운전·최적화 플랫폼으로 다루며 통신과 제어 경계가 핵심임을 제시한다. ([SRC-ENS-D04-0006], [SRC-ENS-D04-0010])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-DER-01` | DER 자산등록·가시성 | L4 | 자원사양, 위치, 계량, 연결상태 | 자원목록·가용성 | 등록시간, 데이터완전성 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-DER-02` | 프로토콜·데이터 상호운용 | L2/L4 | SCADA, AMI, 인버터, API, 시계열 | 표준 데이터모델·명령 | 연결성공률, 지연 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-DER-03` | 배전망 상태추정·제약관리 | L3/L4 | 토폴로지, 전압, 부하, DER 출력 | hosting capacity·제어범위 | 전압위반, 손실 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-DER-04` | VPP 집합예측·입찰 | L3/L4 | 자원예측, 가격, 계약, 제약 | 집합용량·입찰·배분 | 예측오차, 수익 | `PLANNED_OR_CONSIDERING` | 높음 |
| `TECH-ENS-DER-05` | 자원별 성과·정산 | L4/L5 | 계량, 지령, 응답, 계약, 시장정산 | 기여도·정산·분쟁증빙 | 정산오류, 처리시간 | `PLANNED_OR_CONSIDERING` | 높음 |
