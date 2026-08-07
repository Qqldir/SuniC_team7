---
id: skes-d06-19-o-i-pain-point-register
title: O/I Pain-Point Register
summary: LNG·발전·가스배급·신재생에너지 등 E&S 밸류체인의 운영 pain point 30개를 필요 데이터·개선 가치·준비도별로 정리한 레지스트리
tags: [d06, process, table]
keywords: [운영 문제점, 밸류체인, LNG, 발전, 가스배급, 신재생에너지, 데이터 준비도, 가치 레버]
related: [PAIN-ENS-D06-001, PAIN-ENS-D06-002, PAIN-ENS-D06-003, PAIN-ENS-D06-004, PAIN-ENS-D06-005, PAIN-ENS-D06-006, PAIN-ENS-D06-007, PAIN-ENS-D06-008, PAIN-ENS-D06-009, PAIN-ENS-D06-010, PAIN-ENS-D06-011, PAIN-ENS-D06-012, PAIN-ENS-D06-013, PAIN-ENS-D06-014, PAIN-ENS-D06-015, PAIN-ENS-D06-016, PAIN-ENS-D06-017, PAIN-ENS-D06-018, PAIN-ENS-D06-019, PAIN-ENS-D06-020, PAIN-ENS-D06-021, PAIN-ENS-D06-022, PAIN-ENS-D06-023, PAIN-ENS-D06-024]
priority: normal
domain: D06
section: 19
source: SK이노베이션E&S_D06_Process_and_Operations.md
breadcrumb: ""
tokens: 1156
updated: 2026-08-06
---

> SK이노베이션 E&S · D06 운영 프로세스·밸류체인 운전

# 19. O/I Pain-Point Register

| Pain ID | Chain | Pain point | Needed data | Value lever | Data readiness hypothesis |
|---|---|---|---|---|---|
| `PAIN-ENS-D06-001` | LNG | cargo·terminal·발전 계획 분절 | cargo, tank, sendout, dispatch | 조달/재고/급전 최적화 | Medium |
| `PAIN-ENS-D06-002` | LNG | ETA 오차가 탱크와 berth에 전파 | AIS/voyage, weather, slot | demurrage·재고 | Medium-high |
| `PAIN-ENS-D06-003` | LNG | BOG 생성 원인과 회수 성과 불명확 | tank/BOG/compressor/sendout | 가스손실·안전 | Medium |
| `PAIN-ENS-D06-004` | LNG | 물리·상업 재고 reconciliation | meter, density, title, use | 재고/정산 | Medium |
| `PAIN-ENS-D06-005` | PWR | 기동시간·연료·배출 변동 | event sequence, fuel, CEMS | 급전·연료·배출 | High |
| `PAIN-ENS-D06-006` | PWR | 열효율 저하 원인 분리 어려움 | ambient, GT/HRSG/ST tags | 연료비 | High |
| `PAIN-ENS-D06-007` | PWR | historian–work order 연결 약함 | tags, alarms, EAM | 예지정비 | Medium |
| `PAIN-ENS-D06-008` | PWR | water·CEMS·발전운전 통합 최적화 | chemistry, CEMS, load | 환경·효율 | Medium |
| `PAIN-ENS-D06-009` | CHP | 열수요 예측과 전력급전 충돌 | weather, heat, power | 열원가·서비스 | High |
| `PAIN-ENS-D06-010` | CG | GIS·검사·사고 이력 정합성 | GIS, inspection, work | 안전·CAPEX | Medium-low |
| `PAIN-ENS-D06-011` | CG | RBMS score 설명성과 backtest | risk data, incident | 안전·투자 | Medium |
| `PAIN-ENS-D06-012` | CG | 드론 영상이 자산/작업과 미연결 | image, geometry, work | 검사 생산성 | Medium |
| `PAIN-ENS-D06-013` | CG | 정압기 이상 조기감지 | pressure, position, work | 안전·가동 | Medium-high |
| `PAIN-ENS-D06-014` | CG | 계량오차·통신·실제손실 분리 | custody, meter, event | 매출·손실 | Medium |
| `PAIN-ENS-D06-015` | CG | 누출 신고·출동·차단 시간 최적화 | calls, GIS, crew | 안전·서비스 | High |
| `PAIN-ENS-D06-016` | REN | 예측오차에 고장·curtailment 혼입 | forecast, SCADA, curtailment | imbalance | High |
| `PAIN-ENS-D06-017` | REN | lost energy 원인분류 불일치 | expected, SCADA, work | 발전량·O&M | Medium |
| `PAIN-ENS-D06-018` | WIND | 해상 접근창·부품·정비 결합 | weather, vessel, spare | downtime | Medium |
| `PAIN-ENS-D06-019` | PPA | meter–REC–계약 정산 예외 | meter, contract, REC | 정산·신뢰 | High |
| `PAIN-ENS-D06-020` | ESS | 가격·열화·보증 제약 공동최적화 | bids, SOC/SOH, warranty | 수익·수명 | High |
| `PAIN-ENS-D06-021` | ESS | SOC/가용성 정보 지연 | BMS/EMS/market | penalty | High |
| `PAIN-ENS-D06-022` | ESS | 안전경보와 정상 열거동 구분 | cell/rack thermal, gas | 안전·가동 | Medium |
| `PAIN-ENS-D06-023` | EVC | 사이트 용량과 고객충전 목표 충돌 | building/load/session | CAPEX·서비스 | High |
| `PAIN-ENS-D06-024` | EVC | 고장코드·현장수리 재발 연결 | charger/work/firmware | uptime | Medium-high |
| `PAIN-ENS-D06-025` | H2 | 액화 specific energy·BOR 원인 | process, tank, energy | 원가·손실 | Medium |
| `PAIN-ENS-D06-026` | H2 | 공급망 transfer loss와 dwell | load/delivery/station | 손실·공급 | Medium |
| `PAIN-ENS-D06-027` | H2 | 안전 barrier impairment 통합시야 | detector/ESD/permit | 안전 | Medium |
| `PAIN-ENS-D06-028` | CCS | 발전부하와 capture 운전 동기화 | unit/capture/steam | 감축·효율 | Low-medium |
| `PAIN-ENS-D06-029` | CCS | source–transport–sink 가용성 불일치 | chain state | capture loss | Low |
| `PAIN-ENS-D06-030` | Common | 서로 다른 법인·OT 시스템 ID 단절 | asset/tag/entity master | 전 과제 기반 | Medium-low |

---
