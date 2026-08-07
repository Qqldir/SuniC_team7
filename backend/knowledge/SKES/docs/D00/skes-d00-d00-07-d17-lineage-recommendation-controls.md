---
id: skes-d00-d00-07-d17-lineage-recommendation-controls
title: D17 Lineage & Recommendation Controls
summary: E&S 프로젝트 과제가 승인받기 위해 충족해야 할 필수 조건과 Finance·Contract·Cyber 등 Hard Gate 거부 기준을 정의한 문서
tags: [d00, governance, "xref:d17", "xref:d01", "xref:d14", "xref:d15"]
keywords: [과제 승인 조건, Hard Gate, 편익 검증, Finance, Contract/JV, Regulation/Tax, Safety/OT, Cyber/Data, Evidence/Measurement, PoC, 과제 승인, Finance 검증, Cyber/Data 심사, Dependency, Evidence, Baseline]
related: []
priority: normal
domain: D00
section: D00-07
source: SK이노베이션E&S_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master"
tokens: 318
updated: 2026-08-06
---

> SK이노베이션 E&S · D00 소스·엔티티·ID·변경이력 마스터 · SK이노베이션 E&S D00 — Source, Entity, ID & Change-Log Master

## D00-07 D17 Lineage & Recommendation Controls

### 최소 Lineage

```text
D01~D14 Fact/Claim
→ D15 Risk/Pain/Failure Mode
→ D16 External Evidence/Solution Fit
→ O/I Seed
→ D17 Final Task
→ KPI/Baseline/Guardrail/Stop Condition
→ G0~G8 Decision Log
```

### D17 과제 승인 조건

모든 과제는 최소한 다음을 가져야 한다.

- 검증된 문제 또는 명시적 `INTERNAL_REQUIRED` 가설
- 적용 자산·프로세스·Owner
- Source/Evidence와 외부사례의 범위
- 필요 데이터와 데이터 권리
- Baseline·KPI·Guardrail·Stop Condition
- 편익 계산식과 Finance 검증 주체
- Safety/OT·Cyber·법률·세무·계약/JV Gate
- Build/Buy/Partner 판단
- PoC 최소범위·기간·확산조건
- 다른 과제와의 Dependency 및 편익 이중계상 방지

### Hard Gate

`Finance`, `Contract/JV`, `Regulation/Tax`, `SHE/OT`, `Cyber/Data`, `Evidence/Measurement` 중 하나라도 실패하면 `HOLD`다. 우선순위 점수는 Hard Gate를 우회하지 못한다.

---
