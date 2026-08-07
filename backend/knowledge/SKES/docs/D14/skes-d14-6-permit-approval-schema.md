---
id: skes-d14-6-permit-approval-schema
title: Permit & Approval Schema
summary: "에너지 프로젝트의 인가·승인 표준 데이터 구조, 상태 단계별 흐름, 프로젝트 유형별 임계 경로와 위험 요소를 정의한 스키마"
tags: [d14, policy, core-candidate, schema, table]
keywords: [인가절차, 규제승인, 상태전환, 임계경로, BESS, LNG, COD, 프로젝트패밀리, 실패모드, 인가기록]
related: [PER-ENS-D14-0001, PER-ENS-D14-0002, PER-ENS-D14-0003, PER-ENS-D14-0004, PER-ENS-D14-0005, PER-ENS-D14-0006, PER-ENS-D14-0007, PER-ENS-D14-0008, PER-ENS-D14-0009]
priority: critical
domain: D14
section: 6
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 576
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 6. Permit & Approval Schema

## 6.1 Canonical Permit Record

```yaml
permit_record:
  permit_id: required
  jurisdiction: required
  regulator: required
  legal_entity: required
  asset_id: required
  permit_type: required
  application_date: nullable
  accepted_date: nullable
  approval_date: nullable
  effective_date: nullable
  expiry_date: nullable
  renewal_window: nullable
  conditions: list
  evidence_required: list
  reporting_frequency: nullable
  owner: required
  status: required
  blocking_milestone: nullable
  source_id: required
```

## 6.2 Permit State

```text
Not Required / Screening
→ Pre-application
→ Submitted
→ Accepted
→ Under Review
→ Public Consultation / Supplemental Request
→ Approved / Conditionally Approved
→ Conditions Precedent Satisfied
→ Construction
→ Commissioning Approval
→ Operating
→ Renewal / Modification / Transfer
→ Suspended / Revoked / Expired / Closed
```

## 6.3 Permit Critical Path Families

| PER ID | Project family | Permit chain | Failure mode |
|---|---|---|---|
| `PER-ENS-D14-0001` | Korea power | generation license→grid→construction→inspection→market | COD slip |
| `PER-ENS-D14-0002` | Korea offshore wind | zone/site→environment→electricity→grid→marine/land→construction | multi-agency delay |
| `PER-ENS-D14-0003` | Korea LH2 | high-pressure/H2 facility approvals→inspection→operation | safety hold |
| `PER-ENS-D14-0004` | US NY BESS | site/local→interconnection→ISO registration→commissioning | queue/permit delay |
| `PER-ENS-D14-0005` | US TX BESS | local/site→GINR→ERCOT registration→energization | study/network upgrade |
| `PER-ENS-D14-0006` | US EV charging | utility service→building/electrical→inspection→energization | transformer/service delay |
| `PER-ENS-D14-0007` | Australia LNG | offshore petroleum/environment/Safeguard→operation | environmental condition |
| `PER-ENS-D14-0008` | CCS | storage title→injection plan→MRV→operation/closure | long-tail liability |
| `PER-ENS-D14-0009` | Vietnam LNG-to-power | planning→investment→land/port→EIA→grid→PPA→EPC→COD | 2031 mechanism loss |

---
