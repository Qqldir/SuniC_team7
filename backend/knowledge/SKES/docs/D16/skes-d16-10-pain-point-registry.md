---
id: skes-d16-10-pain-point-registry
title: Pain Point Registry
summary: SK이노베이션 E&S의 에너지 전환 사업 전반에서 마주하는 31개 운영 과제와 각각의 기술 솔루션 패턴을 정리한 레지스트리 표
tags: [d16, ecosystem, table, "xref:d15", "xref:d06"]
keywords: [LNG, 발전, BESS, 수소, CCS, 디지털트윈, 해상풍력, 도시가스]
related: [PAIN-ENS-D16-001, PAIN-ENS-D16-002, PAIN-ENS-D16-003, PAIN-ENS-D16-004, PAIN-ENS-D16-005, PAIN-ENS-D16-006, PAIN-ENS-D16-007, PAIN-ENS-D16-008, PAIN-ENS-D16-009, PAIN-ENS-D16-010, PAIN-ENS-D16-011, PAIN-ENS-D16-012, PAIN-ENS-D16-013, PAIN-ENS-D16-014, PAIN-ENS-D16-015, PAIN-ENS-D16-016, PAIN-ENS-D16-017, PAIN-ENS-D16-018, PAIN-ENS-D16-019, PAIN-ENS-D16-020, PAIN-ENS-D16-021, PAIN-ENS-D16-022, PAIN-ENS-D16-023, PAIN-ENS-D16-024]
priority: normal
domain: D16
section: 10
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 1696
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 10. Pain Point Registry

| Pain ID | Pain Point | D15 연결 | Solution Pattern |
|---|---|---|---|
| `PAIN-ENS-D16-001` | LNG price·flow·AIS·contract 정보가 분절 | LNG shock | commodity data fusion |
| `PAIN-ENS-D16-002` | Cargo ETA 변경이 tank/slot/발전계획과 늦게 연결 | shipping | event graph |
| `PAIN-ENS-D16-003` | LNG terminal conservative setpoint의 비용을 실시간 계산 곤란 | terminal | process twin |
| `PAIN-ENS-D16-004` | compressor/pump 이상과 work order 연결 지연 | reliability | APM→CMMS |
| `PAIN-ENS-D16-005` | 발전 GT 센서 drift와 실제 equipment fault 구분 어려움 | power trip | condition model |
| `PAIN-ENS-D16-006` | heat rate drift 원인 분리 부담 | economics | digital twin/analytics |
| `PAIN-ENS-D16-007` | 정비 우선순위에 위험·손익·parts가 함께 반영되지 않음 | maintenance | risk-based EAM |
| `PAIN-ENS-D16-008` | 도시가스 GIS topology와 현장 상태 불일치 가능 | city gas | network truth engine |
| `PAIN-ENS-D16-009` | 굴착·공사 risk signal이 분산 | city gas safety | field risk analytics |
| `PAIN-ENS-D16-010` | methane alarm의 source attribution 불확실 | methane | sensor+wind+GIS fusion |
| `PAIN-ENS-D16-011` | 해상풍력 SCADA/CMS/OEM 데이터 silo | wind | multi-OEM APM |
| `PAIN-ENS-D16-012` | marine access 일정과 고장 criticality 동기화 부족 | wind | weather-window optimizer |
| `PAIN-ENS-D16-013` | blade inspection 결과와 work order linkage 수작업 | wind | drone→EAM |
| `PAIN-ENS-D16-014` | 발전량 forecast error와 PPA imbalance 원인 분리 어려움 | PPA | forecast attribution |
| `PAIN-ENS-D16-015` | BESS 수익 최적화와 degradation 비용이 분리 | BESS market | degradation-aware bidding |
| `PAIN-ENS-D16-016` | BMS alarm noise와 실제 thermal precursor 구분 | BESS safety | multimodal safety analytics |
| `PAIN-ENS-D16-017` | warranty constraint가 bid engine에 실시간 반영 안될 수 있음 | BESS | warranty-aware optimizer |
| `PAIN-ENS-D16-018` | bid-dispatch-meter-settlement 불일치 추적 부담 | BESS | reconciliation engine |
| `PAIN-ENS-D16-019` | charger failure를 remote fix/truck roll로 분류 어려움 | EV | remote diagnostics |
| `PAIN-ENS-D16-020` | MUD/fleet site 전력제약과 charging SLA 충돌 | EV | site power twin |
| `PAIN-ENS-D16-021` | session/payment/energy 로그 reconciliation 부담 | EV | revenue assurance |
| `PAIN-ENS-D16-022` | LH2 detector/valve/ESD proof status 통합시야 부족 | H2 safety | barrier health |
| `PAIN-ENS-D16-023` | LH2 극저온 계측 불확실성이 mass balance에 전파 | H2 economics | metering uncertainty model |
| `PAIN-ENS-D16-024` | production→storage→trailer→sold kg 손실경로 분리 어려움 | H2 | mass-balance twin |
| `PAIN-ENS-D16-025` | BOG 발생원인·회수/vent 경제성 실시간 비교 부담 | H2 | BOG optimizer |
| `PAIN-ENS-D16-026` | CCS storage capacity와 injectivity uncertainty 혼재 | CCS | subsurface ensemble |
| `PAIN-ENS-D16-027` | MMV 기술 선택이 risk와 cost에 직접 연결되지 않을 수 있음 | CCS | risk-based MMV |
| `PAIN-ENS-D16-028` | emitter FID와 storage readiness 시점 mismatch | CCS | readiness matcher |
| `PAIN-ENS-D16-029` | CCS 장기 liability evidence가 여러 시스템에 분산 | CCS | evidence graph |
| `PAIN-ENS-D16-030` | OT asset inventory의 unknown/obsolete device | cyber | passive discovery |
| `PAIN-ENS-D16-031` | OT vulnerability priority가 process impact와 분리 | cyber | risk-context vuln mgmt |
| `PAIN-ENS-D16-032` | vendor remote access session 통제 증거 분산 | cyber | secure access audit |
| `PAIN-ENS-D16-033` | incident 때 IT/OT/physical dependency 수작업 파악 | BCP | dependency graph |
| `PAIN-ENS-D16-034` | 계약 의무·notice·consent deadline 누락 위험 | governance | contract intelligence |
| `PAIN-ENS-D16-035` | 규정의 현재/미래/종료 상태를 AI가 혼동 가능 | regulation | effective-date RAG |
| `PAIN-ENS-D16-036` | PFE/세액공제 공급망 증거 체인 복잡 | tax | evidence engine |
| `PAIN-ENS-D16-037` | 프로젝트 permit/JV/EPC critical path 분산 | project | Monte Carlo graph |
| `PAIN-ENS-D16-038` | AI answer가 source freshness를 숨길 수 있음 | AI risk | source-locked RAG |
| `PAIN-ENS-D16-039` | 같은 자산이 D06~D15에서 서로 다른 이름 | data | canonical entity resolution |
| `PAIN-ENS-D16-040` | vendor PoC 효과를 서로 다른 baseline으로 비교 | O/I | common evaluation protocol |
| `PAIN-ENS-D16-041` | SaaS 단가와 fleet scale TCO의 비선형성 | finance | TCO model |
| `PAIN-ENS-D16-042` | pilot 종료 후 모델/데이터 반출 불확실 | vendor | exit-by-design |
| `PAIN-ENS-D16-043` | field worker가 alert reason을 신뢰하지 않을 가능성 | adoption | explainable workflow |
| `PAIN-ENS-D16-044` | false alarm이 오히려 운영부담 증가 | analytics | precision-first gate |
| `PAIN-ENS-D16-045` | safety signal과 optimization signal 혼재 | safety | safety separation |
| `PAIN-ENS-D16-046` | cloud outage 시 운영 의존성 | resilience | edge/fallback |
| `PAIN-ENS-D16-047` | OEM warranty와 third-party analytics 충돌 | asset | warranty-safe shadow mode |
| `PAIN-ENS-D16-048` | 학습데이터에 failure label 부족 | ML | semi-supervised/anomaly |
| `PAIN-ENS-D16-049` | 외부 vendor marketing KPI가 실제 가치평가를 왜곡 | governance | evidence-tier scoring |
| `PAIN-ENS-D16-050` | 여러 PoC가 비슷한 데이터 pipeline을 중복 구축 | architecture | shared data foundation |

---
