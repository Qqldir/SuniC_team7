---
id: skes-d03-9-d03-직접-o-i-seed
title: D03 직접 O/I Seed
summary: "LNG·발전·수소·ESS 등 에너지 사업별 AI 도입 가능 문제 21개를 정리한 표로, 각 문제의 연결 사업, 기대 KPI, 우선도(P0/P1)를 명시한다."
tags: [d03, product, oi-seed, table, "xref:d17"]
keywords: [문제 후보, 예측, 최적화, BOG, ESS, KPI, 우선도, Seed, AI 도입, 의사결정]
related: [SEED-ENS-D03-001, SEED-ENS-D03-002, SEED-ENS-D03-003, SEED-ENS-D03-004, SEED-ENS-D03-005, SEED-ENS-D03-006, SEED-ENS-D03-007, SEED-ENS-D03-008, SEED-ENS-D03-009, SEED-ENS-D03-010, SEED-ENS-D03-011, SEED-ENS-D03-012, SEED-ENS-D03-013, SEED-ENS-D03-014, SEED-ENS-D03-015, SEED-ENS-D03-016, SEED-ENS-D03-017, SEED-ENS-D03-018, SEED-ENS-D03-019, SEED-ENS-D03-020, SEED-ENS-D03-021]
priority: normal
domain: D03
section: 9
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: ""
tokens: 1164
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션

# 9. D03 직접 O/I Seed

아래 Seed는 제품·솔루션 관점에서 도출한 문제 후보이며 D17에서 내부 데이터 존재 여부와 경제성을 확인한 뒤 과제로 승격한다.

| Seed ID | 연결 PS | 문제정의 | 기대 KPI | 우선도 |
|---|---|---|---|---|
| `SEED-ENS-D03-001` | LNG-03/04 | 선박 ETA·터미널 재고·발전수요가 분리돼 도입일정 최적화가 어려움 | 대기시간, 재고, 긴급조달비 | P0 |
| `SEED-ENS-D03-002` | LNG-04 | BOG 발생과 처리 의사결정의 예측성이 낮음 | BOG 손실, 에너지사용 | P0 |
| `SEED-ENS-D03-003` | PWR-01 | 설비상태·SMP·연료비를 함께 반영한 발전계획이 제한적일 수 있음 | 발전마진, heat rate | P0 |
| `SEED-ENS-D03-004` | PWR-02 | 전력과 열수요의 동시예측·최적화가 필요 | 종합효율, 열손실 | P0 |
| `SEED-ENS-D03-005` | CG-01/03 | 배관 위험데이터가 분산돼 점검 우선순위 정밀화가 어려움 | 사고·누출, 점검생산성 | P0 |
| `SEED-ENS-D03-006` | CG-02 | 계량기 사진 자가검침의 오입력·재처리 비용 | 검침정확도, 처리시간 | P0 |
| `SEED-ENS-D03-007` | CG-02 | 요금·전출입·자동이체 상담의 반복업무 비중 | 상담시간, 1회 해결률 | P0 |
| `SEED-ENS-D03-008` | REN-01/02 | 기상·설비 데이터를 결합한 발전량 예측오차 | 예측오차, 정산비용 | P0 |
| `SEED-ENS-D03-009` | REN-02/ES-06 | 해상풍력 접근성 제약으로 정비일정 최적화가 어려움 | downtime, 선박·인력비 | P0 |
| `SEED-ENS-D03-010` | REN-03/04 | 고객별 PPA 비용·위험 시나리오 비교가 복잡 | 제안시간, 계약전환율 | P0 |
| `SEED-ENS-D03-011` | REN-05 | 발전·사용·계약·정산 데이터의 대사 부담 | 정산시간, 오류율 | P0 |
| `SEED-ENS-D03-012` | H2-01 | 액화플랜트 전력소비와 생산수율 최적화 필요 | kWh/kg-H2, 가동률 | P0 |
| `SEED-ENS-D03-013` | H2-02/03 | 수요·재고·배송경로의 통합계획 필요 | 물류비, 품절, BOG | P0 |
| `SEED-ENS-D03-014` | H2-03 | 충전소 재고·대기·고장 예측 부족 | 가동률, 대기시간 | P0 |
| `SEED-ENS-D03-015` | ES-01 | 피크저감과 배터리 열화를 함께 반영한 ESS 제어 필요 | 절감액, 열화비용 | P0 |
| `SEED-ENS-D03-016` | ES-02/03 | 발전·시장가격·열화·안전을 통합한 ESS 입찰제어 필요 | 거래수익, 가용성 | P0 |
| `SEED-ENS-D03-017` | ES-04/05 | 분산자원 데이터 모델·통신규격 불일치 | 연동시간, 제어성공률 | P1 |
| `SEED-ENS-D03-018` | ES-06 | 재생자산 SCADA·이미지·정비이력 기반 고장진단 | 발전손실, MTTR | P1 |
| `SEED-ENS-D03-019` | ES-07 | 충전기 고장과 현장출동의 사후대응 비중 | 충전성공률, MTTR | P0 |
| `SEED-ENS-D03-020` | ES-07 | 주차·충전·건물부하의 동시 최적화 필요 | 피크, 회전율, 대기 | P0 |
| `SEED-ENS-D03-021` | CCS-01/02 | CO2 계측·운송·저장 데이터 계보와 MRV 체계 필요 | 검증시간, 데이터완전성 | P1 |

### Seed 사용 제한

- `필요`, `어려움`, `부족`은 공개자료에서 내부 문제가 확인됐다는 뜻이 아니라 제품구조상 검증해야 할 가설이다.
- P0 Seed도 내부 KPI·데이터·현업 Sponsor가 없으면 D17 실행과제로 확정하지 않는다.
- CCS·블루수소·DERMS·VPP Seed는 사업단계 Gate를 먼저 통과해야 한다.

---
