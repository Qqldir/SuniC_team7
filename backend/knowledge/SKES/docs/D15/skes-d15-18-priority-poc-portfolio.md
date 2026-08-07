---
id: skes-d15-18-priority-poc-portfolio
title: Priority PoC Portfolio
summary: "SK이노베이션 E&S 우선 AI/Digital PoC 20개 프로젝트의 추진 배경, KPI, 중단 조건 및 실행 게이트 기준을 정리한 포트폴리오 표."
tags: [d15, risk, table, "xref:d14", "xref:d17"]
keywords: [PoC, AI 프로젝트, KPI, 게이트, LNG, 액화수소, BESS, 탄소포집, OT보안, 리스크]
related: []
priority: normal
domain: D15
section: 18
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 824
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 18. Priority PoC Portfolio

## 18.1 Priority 20

| Rank | Seed | Why now | KPI | Stop Condition |
|---:|---|---|---|---|
| 1 | `044` K-ETS Position Twin | 2026~30 비용구조 변화 | carbon cost forecast error | allowance/dispatch data 권리 없음 |
| 2 | `002` LNG–Terminal–Power Twin | 2026 LNG 공급충격 | replacement/demurrage/margin | contract index/position 미연결 |
| 3 | `029` LH2 Barrier Health | 안전 최우선 | impairment hours·overdue test | safety owner 승인/센서검증 실패 |
| 4 | `028` LH2 Mass Balance | 수요·BOG·경제성 동시 | unexplained kg·sold ratio | custody-quality data 부족 |
| 5 | `023` Market Rule Change Agent | KCE rule drift | rule→deployment latency | human market approval 불가 |
| 6 | `021` Degradation-Aware BESS Bidder | 경쟁/열화 동시 | lifecycle net margin | safety envelope 위반 |
| 7 | `045` PFE Supplier Graph | 세액공제 보전 | evidence completeness | Tax/Legal 해석 미확정 |
| 8 | `038` Quynh Lap Deadline Monte Carlo | 2031 임계조건 | P(deadline)·critical slack | schedule/permit owner 불명 |
| 9 | `039` Offshore Permit Dependency AI | 2·3단계 개발 | permit lead/aging | authoritative register 부재 |
| 10 | `057` OT Safety-Cyber Correlation | 2026 OT 위협 | triage lead/RTO | CISO/SHE 공동승인 없음 |
| 11 | `007` Turbine Trip Precursor AI | 발전가동 손실 | avoided outage/precision | false alarm 운영부담 과다 |
| 12 | `015` Offshore Cable Health | 긴 MTTR tail | warning lead/outage days | sensor coverage 부족 |
| 13 | `036` CCS Digital MRV | bankability 핵심 | evidence completeness | legal/MRV 기준 미확정 |
| 14 | `034` CCS FID Graph | announced→firm 구분 | firm volume forecast | counterparty data 권리 없음 |
| 15 | `054` OT Asset Exposure Map | 기본 통제 | unknown/exposed assets | active scan 안전성 미확보 |
| 16 | `042` Contract Obligation Graph | 계약 다층화 | missed deadline | confidential doc access 불가 |
| 17 | `060` AI Source Freshness | D14 stale 방지 | stale ratio | authoritative fetch 실패 |
| 18 | `066` Portfolio Stress Engine | cross-business contagion | coverage/decision time | loss inputs 미검증 |
| 19 | `068` Critical Spare Optimizer | multi-asset downtime | stockout/downtime | BOM/failure 데이터 품질 낮음 |
| 20 | `079` O/I Gate Scorer | D17 안전장치 | unsafe seed pass=0 | human gate owner 미설정 |

## 18.2 PoC Common Gate

```text
1. Problem Owner exists
2. Exposure Unit is identifiable
3. Minimum historical/event data exists
4. Source/Data rights are valid
5. Safety/Legal/Tax/Cyber gate applicable?
6. Human approval point defined
7. Baseline KPI measurable
8. Counterfactual or before-after test possible
9. Stop condition predefined
10. Production integration reversible
```

---
