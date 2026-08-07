---
id: skes-d15-10-contract-finance-regulation-counterparty
title: "Contract, Finance, Regulation & Counterparty Risk"
summary: "계약·재무·규제 영역의 12가지 실패 모드(default, covenant 위반 등)를 매트릭스로 정리하고, 자동화 의존 위험성을 경고하는 문서"
tags: [d15, risk, table, "xref:d13", "xref:d14"]
keywords: [실패모드, default, covenant, 자동화 위험, 세제혜택, JV, K-ETS, 보험, ABAC]
related: [FM-ENS-D15-075, FM-ENS-D15-076, FM-ENS-D15-077, FM-ENS-D15-078, FM-ENS-D15-079, FM-ENS-D15-080, FM-ENS-D15-081, FM-ENS-D15-082, FM-ENS-D15-083, FM-ENS-D15-084, FM-ENS-D15-085, FM-ENS-D15-086]
priority: normal
domain: D15
section: 10
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 437
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 10. Contract, Finance, Regulation & Counterparty Risk

## 10.1 Failure Modes

| FM ID | Failure Mode | D13/D14 Link | Impact |
|---|---|---|---|
| `FM-ENS-D15-075` | contract obligation missed | notice/SLA/deadline | LD/default/rights loss |
| `FM-ENS-D15-076` | change-of-control consent gap | ownership change | default/termination |
| `FM-ENS-D15-077` | JV reserved matter deadlock | governance | schedule/capital |
| `FM-ENS-D15-078` | capital call surprise | sponsor support | liquidity |
| `FM-ENS-D15-079` | PF covenant headroom erosion | DSCR/covenant | distribution lock/default |
| `FM-ENS-D15-080` | tax credit eligibility gap | 48E/PFE/PWA | clawback/lost benefit |
| `FM-ENS-D15-081` | permit condition overdue | permit register | stop/delay/penalty |
| `FM-ENS-D15-082` | K-ETS position underhedged | allowance plan | carbon cash cost |
| `FM-ENS-D15-083` | sanctions/ABAC screening failure | supplier/JV | legal/reputation |
| `FM-ENS-D15-084` | insurance coverage mismatch | asset/contract | uninsured loss |
| `FM-ENS-D15-085` | claim notification late | policy term | recovery loss |
| `FM-ENS-D15-086` | receivable/credit deterioration | customer/offtaker | cash/default |

## 10.2 Governance Principle

계약·재무·규제 위험은 자동화가 특히 위험한 영역이다. `규칙/계약 원문 → applicability → 계산 → evidence → human approval`을 분리하고, AI가 만든 요약만으로 default·termination·tax eligibility·regulatory filing 여부를 판단하지 않는다.

---
