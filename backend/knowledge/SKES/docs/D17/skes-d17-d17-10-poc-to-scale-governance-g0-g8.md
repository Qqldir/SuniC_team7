---
id: skes-d17-d17-10-poc-to-scale-governance-g0-g8
title: PoC-to-Scale Governance — G0~G8
summary: "기술실증부터 운영 확대까지 AI 프로젝트의 8단계 게이트별 산출물, 통과 조건, 의사결정 권한을 정의하는 거버넌스 프레임워크다."
tags: [d17, oi-portfolio, table]
keywords: [Gate, 기술실증, 확대, 의사결정, 산출물, 데이터보안, Shadow Mode, 독립검증, 사후평가, 통제]
related: []
priority: normal
domain: D17
section: D17-10
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 625
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-10 PoC-to-Scale Governance — G0~G8

| Gate | 필수 산출물 | 통과 조건 | 중단 조건 |
|---|---|---|---|
| `G0 Problem Proof` | Pain·Owner·Exposure unit·Baseline | 문제·의사결정·분모 재현 | Solution-first·Owner 없음 |
| `G1 Data/Rights/SHE/Cyber` | Data map·rights·zone·safety boundary·consent | 최소권한·source lineage·rollback | 권리 UNKNOWN·SIS 침해·uncontrolled export |
| `G2 Offline Replay` | 과거 Data·기존 rule/model 비교 | leakage 없는 유의미 개선 | hindsight leakage·label 오류 |
| `G3 Shadow Mode` | 실제 운영 예측·drift·latency | 운영 영향 없이 재현 | alert flood·latency·critical miss |
| `G4 Bounded Live PoC` | 좁은 asset/site·Human approval | KPI 개선·Guardrail 유지 | 안전·품질·시장·고객 SLA 악화 |
| `G5 Independent Validation` | Finance·SHE·Legal/Tax·Cyber 검증 | 가치·부작용·재현성 승인 | Vendor 자체평가뿐임 |
| `G6 Scale Gate` | TCO·Architecture·Support·Exit | repeatable business case | integration/change cost가 편익 초과 |
| `G7 Multi-Asset/Region` | 표준 template·local exception | 자산별 통제와 성과 유지 | 예외·drift·support debt 누적 |
| `G8 PIR / Exit` | 가정–실제·계약/모델 update·lessons | 학습 재사용 또는 안전종료 | Zombie 운영·책임Owner 부재 |

## Gate별 의사결정 권한

| 의사결정 | 필수 Human Authority |
|---|---|
| 발전/CHP/LNG 운전 setpoint·정비·trip 대응 | Operations + SHE + OT/MOC |
| 도시가스 누출·긴급출동·차단 | Gas Safety + Field command |
| BESS bid/dispatch·safety setting | KCE Market + Asset/Safety + Risk |
| LH2 ESD/SIS·공정변경 | Hydrogen Ops + Process Safety + MOC |
| CCS MRV·규제제출·저장승인 | CCS Technical + Legal/Regulator interface |
| Tax/ETS/PFE/48E 판정 | Tax + Legal + Finance/Environment |
| JV/계약의무·Consent | Legal + JV Governance |
| CAPEX/PF/Guarantee | Investment/Finance + authorized committee |
| 외부 AI Data/IP·Cyber | Data Owner + Legal/IP + CISO |

---
