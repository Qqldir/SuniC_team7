---
id: skes-d15-16-pain-point-register
title: Pain Point Register
summary: "LNG, 발전, BESS, 수소 등 사업별 데이터 사일로와 시스템 단절로 인한 위험 30개를 근본원인, KPI, 우선순위로 분류한 관리표"
tags: [d15, risk, table, "xref:d17"]
keywords: [데이터 사일로, risk 가시성, 근본원인, LNG, 발전, BESS, 수소, CCS, margin-at-risk, 우선순위]
related: [PAIN-ENS-D15-001, PAIN-ENS-D15-002, PAIN-ENS-D15-003, PAIN-ENS-D15-004, PAIN-ENS-D15-005, PAIN-ENS-D15-006, PAIN-ENS-D15-007, PAIN-ENS-D15-008, PAIN-ENS-D15-009, PAIN-ENS-D15-010, PAIN-ENS-D15-011, PAIN-ENS-D15-012, PAIN-ENS-D15-013, PAIN-ENS-D15-014, PAIN-ENS-D15-015, PAIN-ENS-D15-016, PAIN-ENS-D15-017, PAIN-ENS-D15-018, PAIN-ENS-D15-019, PAIN-ENS-D15-020, PAIN-ENS-D15-021, PAIN-ENS-D15-022, PAIN-ENS-D15-023, PAIN-ENS-D15-024]
priority: normal
domain: D15
section: 16
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1726
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 16. Pain Point Register

| Pain ID | Pain Point | Root Cause | KPI | Priority |
|---|---|---|---|---|
| `PAIN-ENS-D15-001` | 사업별 Risk ID가 분리돼 전파경로가 안 보임 | entity/asset ID 단절 | correlated exposure | P0 |
| `PAIN-ENS-D15-002` | LNG cargo·hedge·terminal·발전 exposure가 silo | system 분산 | margin-at-risk | P0 |
| `PAIN-ENS-D15-003` | 지정학 event 반영이 수기 | event-data 지연 | response lead time | P0 |
| `PAIN-ENS-D15-004` | cargo ETA와 terminal ullage 통합예측 부족 | AIS/ops 단절 | demurrage | P0 |
| `PAIN-ENS-D15-005` | use-or-pay capacity 활용률과 value 연결 부족 | contract/ops silo | capacity value | P1 |
| `PAIN-ENS-D15-006` | 발전 trip precursor와 경제효과가 분리 | OT/finance 단절 | avoided outage | P0 |
| `PAIN-ENS-D15-007` | 정비일정을 scarcity value와 함께 못 봄 | market/CMMS silo | outage margin | P0 |
| `PAIN-ENS-D15-008` | CHP 전력·열 공동위험 모델 부족 | separate planning | joint margin | P0 |
| `PAIN-ENS-D15-009` | 도시가스 leak/pressure signal이 GIS·work와 분리 | OT/GIS silo | incident lead time | P0 |
| `PAIN-ENS-D15-010` | 도시가스 기상·구조수요 혼합 | normalization 부족 | demand error | P1 |
| `PAIN-ENS-D15-011` | 해상풍력 고장과 marine access를 따로 관리 | maintenance/weather silo | MTTR | P0 |
| `PAIN-ENS-D15-012` | cable health 조기경보 부족 | condition data gap | outage days | P1 |
| `PAIN-ENS-D15-013` | curtailment와 PPA shortfall 연결 부족 | grid/contract silo | imbalance cost | P0 |
| `PAIN-ENS-D15-014` | RE100 attribute evidence가 계약과 분리 | manual ledger | exception rate | P1 |
| `PAIN-ENS-D15-015` | BESS SOH 경제비용이 bid에 실시간 반영 안 됨 | model silo | lifecycle margin | P0 |
| `PAIN-ENS-D15-016` | BESS market saturation 반영 지연 | external data lag | revenue forecast | P0 |
| `PAIN-ENS-D15-017` | Market rule change→optimizer deployment 추적 부족 | governance gap | rule latency | P0 |
| `PAIN-ENS-D15-018` | BESS thermal alarm과 asset genealogy 분리 | vendor silo | containment time | P0 |
| `PAIN-ENS-D15-019` | charger offline 원인분류·원격복구 한계 | device heterogeneity | uptime/MTTR | P1 |
| `PAIN-ENS-D15-020` | site 전력제약이 sales pipeline 후반에 발견 | utility data gap | conversion | P1 |
| `PAIN-ENS-D15-021` | LH2 train/BOG/출하/판매량 통합 mass balance 부족 | process/commercial silo | sold kg | P0 |
| `PAIN-ENS-D15-022` | 안전 barrier impairment 실시간 가시성 부족 | proof-test/OT 분리 | impairment hours | P0 |
| `PAIN-ENS-D15-023` | 수소 MOU·차량계획을 실제수요로 오인 위험 | stage taxonomy | utilization | P0 |
| `PAIN-ENS-D15-024` | station inventory와 trailer routing 분리 | logistics silo | stockout | P0 |
| `PAIN-ENS-D15-025` | CCS 발표 capacity와 firm volume 혼합 | stage discipline | contracted tCO2 | P0 |
| `PAIN-ENS-D15-026` | emitter FID와 storage readiness 동기화 부족 | cross-party dependency | utilization | P0 |
| `PAIN-ENS-D15-027` | CCS MRV 증빙 lineage 복잡 | sensor/contract/reg silo | verification | P0 |
| `PAIN-ENS-D15-028` | 장기책임·보험·계약배분 비교 어려움 | legal data unstructured | tail exposure | P1 |
| `PAIN-ENS-D15-029` | Quynh Lap critical path 통합모델 부족 | permit/EPC/grid 분리 | deadline slack | P0 |
| `PAIN-ENS-D15-030` | project EAC와 JV capital call 신호 지연 | finance/project silo | cash forecast | P0 |
| `PAIN-ENS-D15-031` | reserved matter/consent aging 추적 부족 | contract text | decision latency | P1 |
| `PAIN-ENS-D15-032` | 계약 notice/deadline 수기관리 | CLM 부족 | missed obligation | P0 |
| `PAIN-ENS-D15-033` | K-ETS position과 dispatch forecast 분리 | carbon/trading silo | carbon cost | P0 |
| `PAIN-ENS-D15-034` | 48E/PFE supplier evidence graph 부재 | tier-n opacity | credit-at-risk | P0 |
| `PAIN-ENS-D15-035` | 규정 효력일·취소·종료 상태 stale | manual monitoring | compliance error | P0 |
| `PAIN-ENS-D15-036` | OT asset inventory 불완전 가능성 | heterogeneous legacy | unknown assets | P0 |
| `PAIN-ENS-D15-037` | vendor remote access session risk | third-party access | exception rate | P0 |
| `PAIN-ENS-D15-038` | backup 존재와 실제 restore 가능성 혼동 | test 부족 | restore success | P0 |
| `PAIN-ENS-D15-039` | OT event와 safety barrier context 단절 | cyber/SHE silo | triage time | P0 |
| `PAIN-ENS-D15-040` | AI가 public data gap을 zero로 취급할 위험 | null semantics | false confidence | P0 |
| `PAIN-ENS-D15-041` | AI 규제·계약 요약이 원문 version과 분리 | provenance gap | citation coverage | P0 |
| `PAIN-ENS-D15-042` | risk scoring이 tail loss를 가림 | ordinal score bias | tail exposure | P1 |
| `PAIN-ENS-D15-043` | 보험과 운영 incident taxonomy 불일치 | finance/risk silo | recovery rate | P1 |
| `PAIN-ENS-D15-044` | cross-business crisis command rehearsal 부족 가능 | drill data 필요 | RTO | P1 |
| `PAIN-ENS-D15-045` | 외부 case를 E&S incident로 오인할 위험 | evidence state 부족 | factual accuracy | P0 |
| `PAIN-ENS-D15-046` | CAPA 종료와 효과검증 종료 혼동 | workflow gap | recurrence | P1 |
| `PAIN-ENS-D15-047` | risk acceptance 만료 추적 부족 | governance | overdue acceptance | P1 |
| `PAIN-ENS-D15-048` | supplier concentration과 spare criticality 별도 | procurement/maintenance silo | downtime | P0 |
| `PAIN-ENS-D15-049` | 기후위험이 자산별만 평가돼 portfolio correlation 누락 | aggregation gap | multi-asset outage | P1 |
| `PAIN-ENS-D15-050` | D17 과제추천에서 안전·법률 Gate가 후순위화될 위험 | ROI-only scoring | gate failure | P0 |

---
