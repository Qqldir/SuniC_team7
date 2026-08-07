---
id: skes-d09-17-o-i-pain-point-register
title: O/I Pain-Point Register
summary: "고객·계약·수요 관리 영역에서 발생하는 30개 데이터 갭과 시스템 연계 문제를 정리한 이슈 레지스터. 각 문제의 근본 원인과 영향받는 KPI, 우선순위를 명시한다."
tags: [d09, customer, table, "xref:d11"]
keywords: [데이터 갭, 시스템 연계, KPI 영향, 고객 정보, 계약 관리, 수요 예측, 도시가스 (LNG/City Gas), CRM·청구 (Billing), 우선순위 (Priority), 에너지 데이터]
related: [PAIN-ENS-D09-001, PAIN-ENS-D09-002, PAIN-ENS-D09-003, PAIN-ENS-D09-004, PAIN-ENS-D09-005, PAIN-ENS-D09-006, PAIN-ENS-D09-007, PAIN-ENS-D09-008, PAIN-ENS-D09-009, PAIN-ENS-D09-010, PAIN-ENS-D09-011, PAIN-ENS-D09-012, PAIN-ENS-D09-013, PAIN-ENS-D09-014, PAIN-ENS-D09-015, PAIN-ENS-D09-016, PAIN-ENS-D09-017, PAIN-ENS-D09-018, PAIN-ENS-D09-019, PAIN-ENS-D09-020, PAIN-ENS-D09-021, PAIN-ENS-D09-022, PAIN-ENS-D09-023, PAIN-ENS-D09-024]
priority: normal
domain: D09
section: 17
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 927
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 17. O/I Pain-Point Register

| Pain ID | Pain Point | Root data gap | Affected KPI | Priority |
|---|---|---|---|---|
| `PAIN-ENS-D09-001` | 고객·파트너·시장기관 혼합 | 관계유형 없음 | concentration | P0 |
| `PAIN-ENS-D09-002` | MOU가 수주로 집계 | commitment state 없음 | pipeline quality | P0 |
| `PAIN-ENS-D09-003` | 계약량·예측·실적 혼합 | demand version 없음 | forecast | P0 |
| `PAIN-ENS-D09-004` | PPA 부하·발전 profile 불일치 | interval data 분리 | imbalance | P0 |
| `PAIN-ENS-D09-005` | 계약조항과 운영 KPI 단절 | clause 구조화 부족 | obligation | P0 |
| `PAIN-ENS-D09-006` | 도시가스 고객 ID 불일치 | CRM-billing-meter key | bill accuracy | P0 |
| `PAIN-ENS-D09-007` | 계량 이상 늦은 발견 | AMI quality feature | read quality | P0 |
| `PAIN-ENS-D09-008` | 긴급신고 분류 편차 | 음성·사례 taxonomy | arrival | P0 |
| `PAIN-ENS-D09-009` | 산업고객 수요 급변 | 생산신호 미연계 | volume variance | P1 |
| `PAIN-ENS-D09-010` | CHP 열수요와 전력 최적화 분리 | thermal model gap | total margin | P0 |
| `PAIN-ENS-D09-011` | KCE bid-telemetry-settlement 단절 | lineage gap | leakage | P0 |
| `PAIN-ENS-D09-012` | BESS 열화 미반영 입찰 | warranty data gap | lifecycle value | P0 |
| `PAIN-ENS-D09-013` | 충전 site 확장시점 불명확 | adoption curve gap | saturation | P1 |
| `PAIN-ENS-D09-014` | fleet 출차요구 미반영 | route/SOC gap | departure SOC | P0 |
| `PAIN-ENS-D09-015` | session-payment orphan | system join gap | leakage | P1 |
| `PAIN-ENS-D09-016` | 수소 계획수요 과대평가 | stage model 없음 | utilization | P0 |
| `PAIN-ENS-D09-017` | station 재고·차량·trailer 분리 | control tower 부재 | stockout | P0 |
| `PAIN-ENS-D09-018` | 고객 데이터 권리 불명확 | consent/contract gap | PoC speed | P0 |
| `PAIN-ENS-D09-019` | 관계담당자 지식 개인화 | interaction 기록 부족 | renewal | P1 |
| `PAIN-ENS-D09-020` | 공개 고객정보 기준일 혼재 | source effective date | accuracy | P1 |
| `PAIN-ENS-D09-021` | 그룹 내부·외부 거래 혼재 | related-party flag | reporting | P0 |
| `PAIN-ENS-D09-022` | 고객별 수익성 계산 경계 불일치 | D11 join gap | margin | P1 |
| `PAIN-ENS-D09-023` | 계약변경 영향 수작업 | amendment diff gap | compliance | P1 |
| `PAIN-ENS-D09-024` | REC·계량 증빙 수작업 | document lineage gap | evidence | P0 |
| `PAIN-ENS-D09-025` | 상담원 지식검색 지연 | fragmented manuals | AHT/FCR | P1 |
| `PAIN-ENS-D09-026` | 공급가능 조회 반복 | GIS/CRM gap | lead time | P1 |
| `PAIN-ENS-D09-027` | 취약고객 지원 누락 위험 | eligibility update gap | support | P1 |
| `PAIN-ENS-D09-028` | rule change model 반영 지연 | rule registry gap | invalid bid | P0 |
| `PAIN-ENS-D09-029` | 익명 사례 중복·오연결 | entity resolution | knowledge quality | P2 |
| `PAIN-ENS-D09-030` | PoC 효과 baseline 부재 | counterfactual 없음 | ROI | P0 |

---
