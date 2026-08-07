---
id: skes-d15-0-domain-boundary
title: Domain Boundary
summary: "E&S 포트폴리오 전체의 위험이 노출·감지·전파·통제·복구되는 과정을 추적하기 위한 D15 도메인의 범위, 역할, 개념 분리 원칙을 정의한 문서"
tags: [d15, risk, core-candidate, schema, "xref:d01", "xref:d14", "xref:d06", "xref:d07"]
keywords: [위험 전파, 조기경보, 실패모드, 회복탄력성, 손실경로, 통제 체계, 포트폴리오 리스크, 개념 분리]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D15
section: 0
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1885
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# SK이노베이션 E&S AI Knowledge Database

## D15. Enterprise Risk, Issues, Failure Modes & Resilience｜리스크·이슈·실패모드·회복탄력성

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Risk namespace: `RISK-ENS-D15-*`
- Event namespace: `EVT-ENS-D15-*`
- Failure-mode namespace: `FM-ENS-D15-*`
- Control namespace: `CTRL-ENS-D15-*`
- KRI namespace: `KRI-ENS-D15-*`
- Scenario namespace: `SCN-ENS-D15-*`
- Recovery namespace: `RCV-ENS-D15-*`
- Pain-point namespace: `PAIN-ENS-D15-*`
- O/I Seed namespace: `SEED-ENS-D15-*`
- Data-request namespace: `DR-ENS-D15-*`
- Source namespace: `SRC-ENS-D15-*`
- 상속 도메인: `D01~D14`; 특히 `D06 Process`, `D07 Assets`, `D08 Supply Chain`, `D09 Customers`, `D10 Market`, `D11 Economics`, `D12 CAPEX`, `D13 Governance`, `D14 Regulation`
- 작성 목적: E&S의 사업·자산·계약·시장·규제 위험을 **조기경보–사건–통제–손실–복구–학습**으로 연결하여, D17에서 비용·안전·가동률·현금흐름·규제준수 개선형 O/I 과제를 선별할 수 있게 한다.

---

# 0. Domain Boundary

## 0.1 D15의 역할

D15는 위험요인 목록이 아니다. 핵심 관리단위는 **특정 위험이 어느 자산·계약·시장·법인에 노출되고, 어떤 조기신호와 통제가 존재하며, 실패 시 어떤 손실경로가 열리고, 어느 조건에서 정상상태로 복구됐다고 볼 수 있는가**이다.

```text
Hazard / Uncertainty / External Shock / Weak Signal
→ Exposure Unit
→ KRI / Detection
→ Failure Mode / Risk Event
→ Preventive & Detective Controls
→ Incident / Loss / Covenant / Compliance / Customer Impact
→ Containment / Crisis Decision
→ Recovery / Workaround / Alternate Supply or Asset
→ Control Effectiveness Validation
→ Residual Risk / Cross-business Propagation
→ D17 Open-Innovation Seed
```

## 0.2 E&S에서 D15가 중요한 이유

E&S는 단일 공장형 사업이 아니라 LNG upstream·shipping·terminal usage·발전·CHP·도시가스·재생에너지·PPA·BESS·EV charging·액화수소·CCS·해외 LNG-to-power가 연결된 포트폴리오다. 따라서 같은 충격이 서로 다른 방식으로 전파된다.

예를 들어 LNG 공급차질은 `cargo 부족 → 대체조달 비용 → 발전 fuel cost → SMP/dispatch → 고객·계약 → 현금흐름`으로 전파될 수 있다. 반대로 BESS 장애는 LNG 조달과 직접 관련이 없지만 `availability → bid performance → market settlement → warranty/degradation → tax/PF covenant` 경로로 손실이 발생할 수 있다. D15는 이 전파경로를 구분한다.

## 0.3 Hard Guardrails

1. `Hazard`, `Risk`, `Issue`, `Incident`, `Loss Event`, `Control Failure`, `Near Miss`를 분리한다.
2. 공개된 사고·중단·정책변화를 E&S 전체의 사고율 또는 품질수준으로 일반화하지 않는다.
3. `발표된 위험`, `실현된 사건`, `외부 산업사례`, `내부 가설`을 동일 상태로 저장하지 않는다.
4. Severity×Likelihood 점수는 우선순위 정렬용이다. 예상손실·VaR·Cash-at-Risk를 의미하지 않는다.
5. 공개되지 않은 사고빈도, 보험한도, deductible, VaR, hedge limit, LNG 계약가격, 실제 H2 가동률을 추정 확정값으로 채우지 않는다.
6. 운영자산과 개발 pipeline, 소유자산과 사용권, JV 경제적 지분과 operational control을 분리한다.
7. LNG 가격상승이 항상 손실이라는 단방향 가정을 금지한다. 계약 index·hedge·발전 SMP·재고·판매계약에 따라 순효과가 달라진다.
8. 발전소 정비·planned outage와 forced outage를 분리한다.
9. BESS MW와 MWh, installed·registered·available·dispatchable capacity를 분리한다.
10. H2 생산능력과 실제 생산·출하·판매·수금 kg을 분리한다.
11. CCS의 announced capacity, permitted capacity, injectivity, firm contracted tCO2를 분리한다.
12. permit delay와 regulation change를 같은 위험으로 합치지 않는다. 하나는 프로젝트 실행, 다른 하나는 rule-state risk다.
13. MOU·정책목표·개발계획을 firm demand·COD·cash inflow로 취급하지 않는다.
14. 인증·검사 통과는 통제증거이지 미래 무사고 보증이 아니다.
15. AI는 발전정지·가스차단·BESS emergency shutdown·수소설비 ESD·규제신고·시장입찰·hedge·보험통지·대외공지를 독자 승인하지 않는다.
16. Safety/EHS, Legal, Tax, Finance, CISO, Market Operator, JV 권한이 필요한 조치는 해당 승인자를 우회하지 않는다.
17. 2024-11-01 이전 `SK E&S`와 이후 `SK이노베이션 E&S CIC`의 법적·시점 경계를 유지한다.
18. D15의 O/I Score는 D17 선별도구이며 회사의 공식 ERM 결론이 아니다.

## 0.4 Risk State Vocabulary

```yaml
risk_event_status:
  WEAK_SIGNAL: 이상징후이나 사건 여부 미확정
  WATCH: 임계치 접근 또는 외부충격 관찰
  UNDER_TRIAGE: 영향·원인·즉시조치 판단 중
  ACTIVE_ISSUE: 문제는 존재하지만 손실사건 범위 미확정
  INCIDENT_ACTIVE: 운영·안전·보안·계약 통제 이탈 발생
  CONTAINED: 추가 노출 억제, 근본조치 미완료
  RECOVERY_IN_PROGRESS: 대체운영·복구 중
  EFFECTIVENESS_VALIDATION: 통제·재발방지 검증 중
  CLOSED_WITH_RESIDUAL_RISK: 종결, 잔여위험 모니터링
  REOPENED: 재발·신규증거로 재개

evidence_state:
  PUBLIC_CONFIRMED: 공식 공개자료로 사건/조건 확인
  EXTERNAL_SIGNAL: 외부 시장·산업사례이며 E&S 사건 아님
  INTERNAL_REQUIRED: 내부 로그/계약/센서 없이는 확인 불가
  HYPOTHESIS: 분석가설, 사실로 승격 금지
```

---
