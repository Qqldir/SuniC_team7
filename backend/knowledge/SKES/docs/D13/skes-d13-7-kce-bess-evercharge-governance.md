---
id: skes-d13-7-kce-bess-evercharge-governance
title: "KCE, BESS & EverCharge Governance"
summary: "SK E&S의 미국 BESS·충전 사업에서 KCE와 EverCharge의 소유권 구조, 거버넌스 레이어, 계약 스택, 각 이해관계자의 권리·의무를 정의하는 문서."
tags: [d13, contract, table]
keywords: [소유권 구조, 거버넌스 레이어, 계약 스택, LTSA, SPV, ITC, EPC, 이해관계자, 에너지저장장치, 충전 인프라]
related: []
priority: normal
domain: D13
section: 7
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 595
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 7. KCE, BESS & EverCharge Governance

## 7.1 KCE ownership and delegation

KCE는 2021년 SK E&S가 majority owner가 된 미국 BESS 사업 플랫폼이다. 당시 closing 후 SK E&S 출신 3명이 KCE Board에 합류한 사실이 공개됐다. 다만 **2021 Board를 2026 현 Board로 복사하지 않는다.** `[SRC-ENS-D13-0021]`

| Governance layer | 공개 사실 | 2026 내부 필요 |
|---|---|---|
| ownership | SK E&S majority-owner acquisition | exact current cap table |
| board | 2021 SK directors added | current directors/committees |
| project SPV | multi-project portfolio | site별 legal owner/borrower |
| market | ERCOT/NYISO relationships | registration/collateral owner |
| tax | ITC monetization 사례 | tax-credit owner/transfer approval |
| procurement | multiple vendor contracts | portfolio master vs project contract |
| data | MarketCapture/BMS/EMS | parent access·vendor restrictions |

## 7.2 BESS Contract Stack

```text
Land / site control
→ Interconnection
→ Utility / ISO registration
→ EPC / BOP
→ Battery / PCS supply
→ LTSA / warranty
→ EMS / MarketCapture
→ Financing / ITC transfer
→ Insurance
→ Dispatch / settlement
```

모든 계약을 `KCE vendor contract` 한 줄로 합치지 않는다. 프로젝트 SPV·supplier·guarantor·warranty beneficiary가 다를 수 있다.

## 7.3 EverCharge

EverCharge는 E&S의 미국 charging solution 포트폴리오에 포함되며 site-host·building owner·fleet·driver·payment processor·utility가 서로 다른 당사자다. `[SRC-ENS-D13-0027~0028]`

| Contract layer | 핵심 권리/의무 |
|---|---|
| Site host | 설치공간·전기용량·접근·보험 |
| EVSE | 하드웨어 인도·warranty·spares |
| SmartPower | controller/software license·availability |
| Network | connectivity·remote update·cyber |
| Driver | account·payment·privacy·refund |
| Fleet | departure SLA·priority charging·roaming |
| Utility | interconnection·tariff·demand limit |
| Data | session·vehicle·building-load ownership/use |

---
