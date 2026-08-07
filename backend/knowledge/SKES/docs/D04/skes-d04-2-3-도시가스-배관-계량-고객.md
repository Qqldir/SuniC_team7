---
id: skes-d04-2-3-도시가스-배관-계량-고객
title: 도시가스 배관·계량·고객
summary: 도시가스 배관·계량·고객의 8대 핵심기술(RBMS·드론·AMI·OCR 등)이 각 레이어에서 무엇을 입출력·제어하고 KPI로 삼는지 보여주는 기술마스터.
tags: [d04, technology, table]
keywords: [RBMS, 누출탐지, 드론점검, AMI, 원격검침, SCADA, OCR, 이상탐지, 자동화]
related: [TECH-ENS-CG-01, TECH-ENS-CG-02, TECH-ENS-CG-03, TECH-ENS-CG-04, TECH-ENS-CG-05, TECH-ENS-CG-06, TECH-ENS-CG-07, TECH-ENS-CG-08]
priority: normal
domain: D04
section: 2.3
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: 세부 Technology Master
tokens: 683
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · 세부 Technology Master

## 2.3 도시가스 배관·계량·고객

공식 자료는 7개 도시가스 자회사, 8개 권역, 약 510만 가구 공급과 RBMS·드론 기반 안전관리를 설명한다. 모든 자회사의 센서·AMI·앱 보급률이 동일하다는 의미는 아니다. ([SRC-ENS-D04-0002])

| TECH ID | 기술 | Layer | 입력 데이터 | 출력·제어 | KPI | 상태 | O/I |
|---|---|---|---|---|---|---|---|
| `TECH-ENS-CG-01` | 배관 RBMS 위험도 평가 | L3/L4 | 매설연도, 재질, 압력, 부식, 사고·굴착 | 구간 위험도·점검순위 | 사고·누출, 점검효율 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-CG-02` | 가스 누출센서·이동형 탐지 | L1 | 가스농도, 풍향, GPS, 영상 | 누출위치·농도·경보 | 탐지거리·시간, 오경보 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-CG-03` | 드론·영상 배관 순회점검 | L1/L3 | RGB·열화상, 위치, 시설물 지도 | 이상후보·점검경로 | 점검시간, 발견률 | `OPERATING_CONFIRMED` | 높음 |
| `TECH-ENS-CG-04` | 압력·유량 이상탐지 | L2/L3 | SCADA 압력·유량, 밸브, 수요 | 누출·설비이상 후보 | 탐지시간, 오탐률 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-CG-05` | AMI·원격검침 | L1/L4 | 계량값, 통신상태, 시간대 사용량 | 검침·사용량 데이터 | 검침성공률, 방문감축 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-CG-06` | 계량기 OCR·오입력 탐지 | L3 | 계량기 이미지, 과거 사용량, 기기유형 | 판독값·신뢰도·재검요청 | 정확도, 재처리율 | `CAPABILITY_CONFIRMED` | 높음 |
| `TECH-ENS-CG-07` | 고객 사용량·요금 이상분석 | L3/L4 | 사용량, 날씨, 가구·사업장 유형, 청구 | 급증·누락·절감 알림 | 민원, 조기탐지, 상담시간 | `ENABLING_CANDIDATE` | 높음 |
| `TECH-ENS-CG-08` | 상담·전출입·현장출동 자동화 | L4 | 신청, 주소, 계약, 민원, 작업자·차량 | 분류·배정·동선 | 처리시간, 재방문율 | `CAPABILITY_CONFIRMED` | 높음 |
