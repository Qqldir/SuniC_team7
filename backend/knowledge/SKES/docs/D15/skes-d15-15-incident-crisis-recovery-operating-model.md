---
id: skes-d15-15-incident-crisis-recovery-operating-model
title: "Incident, Crisis & Recovery Operating Model"
summary: "사건 포착부터 학습까지 T0~T7 단계별 의사결정·기록 방식과 복구 종료 기준, 백업 계획 검증을 위한 6가지 훈련 유형을 정의한 위기 운영 모델"
tags: [d15, risk, schema, table]
keywords: [사건 대응, Incident Command, 위기 의사결정, Recovery Exit Criteria, 복구 기준, BCP 테스트, CAPA, Tabletop 훈련]
related: []
priority: normal
domain: D15
section: 15
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 700
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 15. Incident, Crisis & Recovery Operating Model

## 15.1 Incident Command Timeline

| Phase | 목표 | 필수 기록 |
|---|---|---|
| `T0 Detect` | 사실/신호 포착 | first observed time·source·quality |
| `T1 Safe` | 인명·환경·설비 안전상태 확보 | ESD/isolation/evacuation decision |
| `T2 Scope` | 영향범위와 종속성 파악 | asset·contract·customer·market |
| `T3 Contain` | 추가 손실 억제 | hold/alternate supply/manual mode |
| `T4 Notify` | 내부/규제/시장/고객 통지 | legal trigger·deadline·approver |
| `T5 Recover` | 최소서비스→정상서비스 | RTO·workaround·restoration |
| `T6 Validate` | 재발방지/통제 검증 | root cause·CAPA·retest |
| `T7 Learn` | cross-asset 학습 | lesson·standard change·closure |

## 15.2 Crisis Decision Log

```yaml
decision_id: DEC-ENS-D15-XXXX
incident_id: string
timestamp: ISO8601
decision: string
alternatives_considered: []
inputs_and_versions: []
uncertainties: []
authority: role
safety_legal_market_gates: []
manual_override: true|false
next_review_at: datetime
```

## 15.3 Recovery Exit Criteria

복구는 `설비가 다시 켜짐`으로 종료하지 않는다.

- 안전 barrier가 요구상태로 복구되고 시험증빙이 존재할 것.
- 운영 KPI가 정의된 안정화 기간 동안 정상범위에 있을 것.
- backlog·manual workaround·temporary bypass가 식별되고 승인될 것.
- market/customer/contract settlement exception이 해소될 것.
- cyber incident의 경우 credential·configuration·persistence 확인 후 복구할 것.
- 데이터 손상 시 source lineage와 reconciliation을 완료할 것.
- CAPA owner와 effectiveness review date가 설정될 것.
- 잔여위험을 명시적으로 승인하고 expiry/reopen trigger를 둘 것.

## 15.4 BCP Test Types

| Test | 목적 | 적용 예 |
|---|---|---|
| Tabletop | 의사결정·권한 검증 | LNG disruption, H2 leak, OT incident |
| Simulation | 데이터/알람/시장 대응 | BESS telemetry loss |
| Technical Failover | 시스템 복구 | EMS/SCADA/charger cloud |
| Restore Drill | backup 실효성 | historian/ERP/CLM |
| Supplier Drill | 대체조달 | critical spare/LNG logistics |
| Cross-Business Exercise | 전파위험 | extreme weather + grid + LNG |

---
