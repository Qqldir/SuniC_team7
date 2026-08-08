---
id: skon-d05-d05-46-geographic-coverage-patent-term-map
title: Geographic Coverage·Patent-Term Map
summary: SK온 배터리 특허 포트폴리오의 각 기술별 명목 존속기간(2030년대~2040년대) 및 한미유중일 등 국가별 등록 현황을 보여주는 매트릭스 문서.
tags: [d05, rnd, schema, table]
keywords: [특허 존속기간, 명목 보호구간, 특허 만료 계획, Patent Term Adjustment, 배터리 IP 포트폴리오, 급속충전 전극, 건식전극, 지역별 등록 현황, 선행출원 기준, 전고체 배터리, 출원일, 우선권, 국가별 등록, 특허족, 포트폴리오 계획, 배터리 IP, 미국 특허청, 지역별 보호 현황]
related: []
priority: normal
domain: D05
section: D05-46.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1263
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-46. Geographic Coverage·Patent-Term Map

## 46.1 Term Calculation Rule

미국 실용특허의 일반적인 존속기간은 관련 미국 출원의 출원일 또는 특정 선행출원을 기준으로 20년이며, 계속·분할출원도 선행출원 기준의 영향을 받을 수 있다. 유럽 특허 역시 출원일로부터 최대 20년이지만 연차료 미납·취하·무효로 더 일찍 소멸할 수 있다. 따라서 아래 기간은 법적 만료일이 아니라 **포트폴리오 계획용 명목 구간**이다. ([미국 특허청][11])

```yaml
term_estimation_policy:

  term_basis:
    us:
      general_rule: 20 years from relevant filing date
      adjustments:
        - Patent Term Adjustment
        - Patent Term Extension
        - Terminal disclaimer
        - Earlier domestic application benefit

    ep:
      general_rule: 20 years from filing date
      early_termination:
        - Nonpayment of renewal fee
        - Withdrawal
        - Revocation
        - Opposition outcome

  prohibited_output:
    - Exact expiration date without official audit
    - Active-right conclusion from publication number alone

  permitted_output:
    - NOMINAL_TERM_BAND
    - EARLY / MID / LATE 2030s
    - EARLY / MID / LATE 2040s
```

---

## 46.2 Term-Band Map

| Patent cluster   | 최초 출원·우선권 시대 | 명목 보호구간     | 해석              |
| ---------------- | -----------: | ----------- | --------------- |
| Legacy Z-Folding |    2012~2013 | 2030년대 초·중반 | 존속여부 확인 우선      |
| 고전압 멀티나이트릴       |    2013~2014 | 2030년대 중반   | 구형 플랫폼 IP       |
| NCM 조성           |    2018~2019 | 2030년대 후반   | 계속출원 존재 가능      |
| 열 차단 모듈          |    2020~2021 | 2040년대 초    | 상용 안전기술 핵심      |
| 급속충전 전극          |    2020~2021 | 2040년대 초    | 분할출원 주의         |
| Battery Ledger   |    2021~2022 | 2040년대 초    | 디지털 생애주기 IP     |
| 실리콘 다층 음극        |    2021~2022 | 2040년대 초    | SF+ 연계 후보       |
| 건식전극             |    2022~2023 | 2040년대 초·중반 | 심사 중 권리범위 변화 가능 |
| 현대 Z-Folding     |    2022~2023 | 2040년대 초·중반 | 개선발명 중심         |
| On-Vent          |    2022~2023 | 2040년대 초·중반 | 미국 등록문서 확인      |
| CTP·열경로          |    2020~2023 | 2040년대 초·중반 | 복수 세대 패밀리       |
| EIS BMS          |    2023~2024 | 2040년대 중반   | 유럽 등록·타국 심사 진행  |
| 전고체 복합양극         |    2023~2024 | 2040년대 중반   | 공개출원 단계         |
| LLZO 공동 IP       |    2023~2024 | 2040년대 중반   | 공동출원 계약 중요      |

---

## 46.3 Geographic Coverage Map

```yaml
geographic_coverage_snapshot:

  fast_charging_electrode:
    identified:
      - KR
      - US
      - EP
      - CN
      - JP
    strategic_value: GLOBAL_AUTOMOTIVE_MARKETS

  dry_electrode:
    identified:
      - EP
    incomplete_search:
      - KR
      - US
      - CN
      - JP

  battery_ledger:
    identified:
      - US
      - EP
    additional_members: REQUIRE_AUDIT

  thermal_barrier:
    identified:
      - US
      - KR
      - CN
      - DE
    status: PARTIAL_FAMILY_RECONCILIATION

  on_vent:
    identified:
      - KR priority
      - US
    gap:
      - EP
      - CN
      - JP

  modern_z_folding:
    identified:
      - KR priority
      - US
      - EP
      - CN
    status: APPLICATION_STAGE_RECONCILIATION

  lithium_metal_glass_laminate:
    identified:
      - PCT
      - KR
      - CN
      - JP
      - EP
    ownership: JOINT_WITH_POLYPLUS

  composite_cathode:
    identified:
      - PCT
      - KR
      - EP
    additional_members: REQUIRE_AUDIT
```

PCT 절차 자체가 세계특허를 부여하는 것은 아니며, 통상 우선일로부터 약 30개월 전후에 각 국가·지역 단계로 진입해야 개별 권리화가 진행된다. ([WIPO][12])

---
