---
id: skes-d15-20-d17-handoff-rules
title: D17 Handoff Rules
summary: Seed를 D17 단계로 승격하기 위한 10개 기준과 상위 우선순위 후보 리스트(Tier A/B)를 제시하는 게이팅 및 평가 기준서
tags: [d15, risk, schema, table, "xref:d17"]
keywords: [D17, Seed, 승격기준, Gate, Exposure, KPI, 우선순위, 성능제약, 데이터통합, 디지털트윈]
related: []
priority: normal
domain: D15
section: 20
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 796
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 20. D17 Handoff Rules

## 20.1 Handoff Object

```yaml
d17_candidate:
  seed_id: SEED-ENS-D15-XXX
  linked_risks: []
  linked_failure_modes: []
  linked_pains: []
  exposure_units: []
  baseline_kri: []
  proposed_solution_pattern: string
  required_internal_data: []
  data_rights: status
  safety_gate: status
  legal_tax_gate: status
  cyber_privacy_gate: status
  success_kpi: []
  stop_condition: []
  owner: role
  source_ids: []
```

## 20.2 D17 Promotion Criteria

Seed는 아래 조건을 만족해야 `PROMOTE_TO_D17`로 승격한다.

1. 실제 E&S Exposure와 연결된다.
2. 기존 통제의 공백 또는 성능제약이 설명된다.
3. 해결 시 KPI 변화가 계량 가능하다.
4. 필요한 데이터가 식별되고 접근 가능성 검토가 끝난다.
5. Safety/Legal/Tax/Cyber/Privacy 중 해당 Gate가 지정된다.
6. 사람이 승인해야 할 의사결정이 정의된다.
7. 실패 시 Stop Condition이 있다.
8. 외부 공급사/스타트업으로 해결 가능한 기술·서비스 경계가 존재한다.
9. 단순 보고서 자동화보다 운영·비용·안전·복구 성과 개선이 크다.
10. 다른 Seed와 중복이면 통합하거나 차별점을 명시한다.

## 20.3 Top Handoff Candidates

| Tier | Seed | D17 문제정의 |
|---|---|---|
| A | `002` | LNG cargo·terminal·발전 데이터를 결합해 공급충격 시 최소비용 대응 |
| A | `044` | K-ETS 할당·배출·dispatch를 연결한 carbon position twin |
| A | `029` | LH2 safety-critical barrier 상태를 proof-test와 OT data로 실시간 가시화 |
| A | `028` | LH2 생산→저장→출하→판매 mass balance 및 loss/BOG 최적화 |
| A | `021` | SOH·열화를 내재화한 BESS bid optimization |
| A | `023` | ERCOT/NYISO rule change를 optimizer/control에 안전하게 배포 |
| A | `045` | 48E/PFE supplier evidence를 tier-n까지 추적하는 graph |
| A | `038` | Quynh Lap 2031 critical deadline Monte Carlo 및 permit dependency |
| A | `057` | OT cyber alert를 safety barrier·운영위험과 결합한 triage |
| A | `036` | CCS MRV sensor→evidence→regulatory lineage 구축 |
| B | `007` | 발전설비 trip precursor와 정지손실을 연결한 predictive maintenance |
| B | `015` | 해상풍력 export cable 상태·marine access 통합 예지보전 |
| B | `034` | CCS emitter FID–storage readiness 동기화 |
| B | `042` | JV/TUA/PPA/EPC 의무·통지·동의 deadline graph |
| B | `060` | 규제/계약/시장 AI의 source freshness와 effective-date 오류 차단 |

---
