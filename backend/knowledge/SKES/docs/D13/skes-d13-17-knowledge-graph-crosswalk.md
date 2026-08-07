---
id: skes-d13-17-knowledge-graph-crosswalk
title: Knowledge Graph Crosswalk
summary: "SK이노베이션 E&S의 LNG 터미널, 재생에너지, 충전 인프라 등 에너지 자산에서 지분 소유권, 운영권, 계약권의 관계를 체계적으로 정의하고 오류 가능성이 있는 관계를 명시적으로 제외하는 문서이다."
tags: [d13, contract]
keywords: [지분율, LNG 터미널, 운영권, 계약권, 에너지 자산, 재생에너지, 파트너사, Darwin LNG, 소유권, 자산 포트폴리오]
related: []
priority: normal
domain: D13
section: 17
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 386
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 17. Knowledge Graph Crosswalk

## 17.1 Representative Edges

```text
PRISM Energy International Australia --HOLDS_37.5_PERCENT--> Barossa
Santos --OPERATES--> Barossa
JERA Australia --HOLDS_12.5_PERCENT--> Barossa
Barossa --FEEDS--> Darwin LNG
SK/E&S historical interest --HOLDS_25_PERCENT_HISTORICAL_PUBLIC--> Darwin LNG
SK E&S LNG LLC --HOLDS_LTA_RIGHT--> Freeport Train 3
E&S --RETAINED_TUA_RIGHT_AFTER_EQUITY_SALE--> Boryeong LNG Terminal
SK Innovation E&S --HOLDS_51_PERCENT--> Jeonnam OWF1
CIP --HOLDS_49_PERCENT--> Jeonnam OWF1
SK E&S --ACQUIRED_MAJORITY--> KCE
KCE --CONTRACTS_WITH--> Sungrow
KCE --PARTICIPATES_IN--> ERCOT
EverCharge --OPERATES--> Charging solution network
Plug Power --FORMERLY_HELD_49_PERCENT--> SK Plug Hyverse
Plug Power --SOLD_49_PERCENT_ON_2025_12_31--> SK Plug Hyverse interest
SK Innovation + PV Power + NASU --CONSORTIUM_FOR--> Quynh Lap
Amorepacific --HAS_PPA_WITH--> E&S renewable supply
```

## 17.2 Prohibited Edges

```text
Freeport LTA --IS_NOT--> Freeport plant ownership
Boryeong TUA --IS_NOT--> Boryeong equity
MOU --IS_NOT--> firm offtake
51_percent_equity --IS_NOT_ALWAYS--> unilateral control
non_recourse_PF --DOES_NOT_PROVE--> zero sponsor support
JV shareholder --DOES_NOT_AUTOMATICALLY_HAVE--> raw data AI rights
2021_board --IS_NOT--> 2026 current board
Plug Power --IS_NOT_CURRENT_49_PERCENT_HOLDER--> Hyverse after 2025-12-31
```

---
