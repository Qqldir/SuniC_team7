---
id: skon-d07-d07-02-ownership-jv-structure
title: Ownership·JV Structure
summary: "SK온과 계열사의 생산거점별 소유권 현황 및 합작투자 구조, BlueOval SK 분리와 중국 EUE 지분 스왑 등 소유권 변화 내역"
tags: [d07, footprint, schema]
keywords: [소유권, 합작회사, 자회사, JV, SK온 Jiangsu, HSBMA, 지분 스왑, BlueOval, SK온, 생산거점, 합작투자, 지분, 소유관계]
related: []
priority: normal
domain: D07
section: D07-02.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 629
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-02. Ownership·JV Structure

## 02.1 Canonical Ownership Tree

```text
SK On
│
├── Wholly Owned / Consolidated
│   ├── Korea — Seosan
│   ├── SK On Hungary
│   │   └── Komárom 1
│   ├── SK Battery Manufacturing Kft.
│   │   ├── Komárom 2
│   │   └── Iváncsa
│   ├── SK Battery America
│   │   ├── Georgia 1
│   │   ├── Georgia 2
│   │   └── SK On Tennessee
│   ├── SK On Jiangsu — 70% at Q1 2026
│   │   ├── Yancheng 1
│   │   └── Yancheng 2
│   └── SK On Yancheng — 100%
│       └── Yancheng 3
│
├── Joint Ventures / Equity-Method Sites
│   ├── HSBMA — SK On 50% / Hyundai Motor Group 50%
│   ├── Beijing BESK — Changzhou
│   └── Huizhou EVE United Energy — SK On 49%, disposal pending
│
└── Transferred Footprint
    ├── Kentucky 1 → Ford
    └── Kentucky 2 → Ford
```

2026년 1분기 기준 SK On Jiangsu는 SK온이 70%를 보유한 종속기업이고 SK On Yancheng은 100% 자회사였다. 후이저우 EUE는 SK온이 49%를 보유한 JV이며, 지분 Swap이 예정대로 종결되면 SK On Jiangsu는 100% 자회사로 전환되고 후이저우 지분은 EVE로 넘어가게 된다. ([KIND][1])

---

## 02.2 Ownership Status Record

```yaml
ownership_change_master:

  - event_id: OWN-D07-001
    subject: BlueOval_SK
    event: JV_DISSOLUTION_AND_ASSET_SEPARATION
    effective_date: 2026-05-20

    result:
      tennessee:
        controller: SK_On
        ownership: 100_percent_through_SKBA

      kentucky_1:
        controller: Ford

      kentucky_2:
        controller: Ford

    evidence_level: DIRECT_REGULATORY
    source_ids:
      - SRC-REG-D07-003

  - event_id: OWN-D07-002
    subject: China_EVE_JV_Portfolio
    event: STAKE_SWAP

    current_status:
      as_of: 2026-08-02
      value: PENDING

    expected_result:
      SK_On_Jiangsu:
        sk_on_ownership: 100_percent

      Huizhou_EUE:
        sk_on_ownership: 0_percent

    source_ids:
      - SRC-REG-D07-006

  - event_id: OWN-D07-003
    subject: HSBMA
    event: COMMERCIAL_PRODUCTION_START

    effective_date: 2026-06-01
    ownership:
      SK_On: 50_percent
      Hyundai_Motor_Group: 50_percent

    gross_design_capacity_gwh: 35

    source_ids:
      - SRC-OFF-D07-005
```

---
