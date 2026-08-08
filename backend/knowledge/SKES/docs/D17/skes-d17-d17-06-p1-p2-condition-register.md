---
id: skes-d17-d17-06-p1-p2-condition-register
title: P1/P2 Condition Register
summary: 각 프로젝트가 Live PoC 진입 전에 충족해야 할 핵심조건과 저지조건을 정의한 단계별 체크리스트
tags: [d17, oi-portfolio, table]
keywords: [Live PoC, 사업성숙도, 데이터권리, 규제확실성, 진입조건, Kill/Hold 조건, PIR, 사전조건, READY 기준, 체크리스트]
related: []
priority: normal
domain: D17
section: D17-06
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 1327
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-06 P1/P2 Condition Register

P1·P2는 낮은 가치라는 뜻이 아니다. **선행조건·사업성숙도·데이터권리·규제확실성이 덜 닫혀 있어 지금 바로 Live PoC에 들어가면 안 된다는 뜻**이다.

| ID | Tier | READY가 되기 위한 핵심조건 | Kill / Hold 조건 |
|---|---|---|---|
| 004 | P1 | 동일 데이터·KPI·보안조건으로 2~3 Vendor blind test | 데이터 Export/삭제 불가 |
| 005 | P1 | 종료·보류 과제 Archive와 실제 PIR 확보 | 실패사유 없는 결과평가 |
| 009 | P1 | AIS/ETA/berth/cargo/재고 history와 demurrage baseline | 항만/계약 데이터권리 없음 |
| 010 | P1 | Lifecycle boundary·methodology·primary activity data | 홍보성 감축률만 존재 |
| 014 | P1 | Asset BOM·failure·lead-time·inventory·lost-margin mapping | safety critical spare를 재고비만으로 축소 |
| 015 | P1 | 승인 Manual·work order·as-found labels | 출처없는 정비지시 생성 |
| 017 | P1 | 누출·굴착 ground truth와 privacy/geospatial gate | 고위험 recall 불충분 |
| 018 | P1 | custody input–meter–billing의 시간정합 | 계량불확도·운영사용 미분리 |
| 019 | P1 | 고위험 신고 Label·SOP·crew availability | high-risk recall 악화 |
| 020 | P2 | Cohort/기상/건물/서비스비용의 집계 데이터 | 개인 추론·차별적 targeting 위험 |
| 022 | P1 | curtailment·weather·SCADA·work order 분리 | Curtailment를 고장으로 오분류 |
| 023 | P1 | 15분/시간 Load·Gen·REC·contract shape | Credit/contract term 미반영 |
| 024 | P1 | clause–meter–certificate–invoice ID join | 회계/법률 승인 없는 자동정산 |
| 025 | P2 | 24/7 CFE 고객수요와 BESS/REC 권리 확인 | 상용수요 없는 기술 demo |
| 029 | P1 | authoritative ISO rule·change owner·config mapping | AI 단독 market rule 판정/배포 |
| 030 | P2 | queue study·permit·CAPEX·probability history | pipeline MW를 운영 MW로 표시 |
| 031 | P1 | heartbeat/error/truck-roll/parts label | remote action이 고객 실패 악화 |
| 032 | P1 | one-line·transformer/panel limit·session·load | 전기보호 한계 초과 |
| 033 | P1 | paid session·power cost·host share·O&M | Port count를 수익으로 대체 |
| 034 | P2 | departure request/SOC·site power·customer consent | 출차 SLA 악화 |
| 035 | P2 | quote template에서 PIS/date-aware incentive 제거 | 종료된 30C 가정 재사용 |
| 038 | P1 | train historian·product quality·meter uncertainty·safe envelope | kWh/kg 개선이 안전 margin 잠식 |
| 039 | P2 | station/offtake 실제수요와 logistics rights | MOU를 firm demand로 입력 |
| 040 | P2 | 단계정의·계약·vehicle/station rollout | 정책목표를 판매량으로 변환 |
| 042 | P1 | firm/conditional emitter 상태와 storage readiness | MOU를 firm tCO2로 분류 |
| 043 | P2 | subsurface ensemble·injectivity·uncertainty owner | 단일 deterministic capacity 사용 |
| 044 | P2 | MRV/closure/transfer/indemnity 원문 | long-tail 책임의 임의 확률화 |
| 045 | P2 | methane·liquefaction·shipping boundary와 verifier | 저탄소 Claim의 경계 불명 |
| 048 | P1 | authoritative source owner·effective-date parser | stale/uncited legal answer |
| 049 | P2 | operational-control·facility baseline·production/emission data | E&S 지분율=법적책임으로 단순화 |
| 050 | P2 | 현행 auction/event ID·certification rule | 취소된 round를 demand로 계상 |
| 051 | P1 | 계약 30~50건·amendment·entity master | 법률 false-negative 허용 불가 |
| 052 | P1 | 완료 프로젝트 10+ reference class·EAC history | garbage WBS/dependency graph |
| 053 | P1 | permit/EPC/PPA/JV critical path owner | 목표일을 확정 COD로 기록 |
| 054 | P2 | debt/guarantee/support/covenant 원문 | Gross project debt를 E&S debt로 합산 |
| 055 | P2 | hurdle rate·forward cash·option trigger | sunk cost·지원금 중복 |
| 056 | P1 | passive SPAN/TAP·authoritative asset inventory | active scan이 운영영향 발생 |
| 058 | P1 | BCP RTO/RPO·dependency·tabletop logs | 문서 checklist만 있고 복구검증 없음 |
| 059 | P2 | validated dependency + loss input | false dependency가 alert overload 유발 |
| 060 | P2 | approval router·rollback·model registry·audit | AI bypass 경로 존재 |

---
