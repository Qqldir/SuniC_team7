---
id: skon-d05-d05-18-expanded-patent-cluster-map
title: Expanded Patent Cluster Map
summary: 배터리 핵심 기술 영역별 특허 포트폴리오 현황과 강점·한계를 보여주는 SK온 특허 지도
tags: [d05, rnd, schema]
keywords: [배터리 특허, 양극 활물질, 실리콘 음극, 고전압 전해액, 분리막, 열전파, LiDFOP, 급속충전, NCM, 특허 포트폴리오, 양극활물질, 고전압전해액, 실리콘음극, 열차단, 고속충전, 특허포트폴리오, Cathode, Anode, 기술클러스터]
related: [PF-D05-002, PF-D05-016, PF-D05-017]
priority: normal
domain: D05
section: D05-18.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1593
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-18. Expanded Patent Cluster Map

## 18.1 Cathode·Electrolyte Cluster

```text
High-Nickel / High-Voltage Cell
│
├── PF-D05-013 NCM Cathode Active Material
│   ├── composition control
│   ├── doping elements
│   └── capacity–life–safety balance
│
├── PF-D05-014 Multi-Nitrile High-Voltage Electrolyte
│   ├── oxidation suppression
│   ├── swelling suppression
│   └── high-temperature stability
│
└── PF-D05-015 LiDFOP Additive System
    ├── electrode-interface protection
    ├── additive combination
    └── electrolyte stabilization
```

### IP Interpretation

```yaml
cluster_interpretation:
  strength:
    - 양극 활물질과 고전압 전해액을 모두 포괄하는 특허축 존재
    - 구형 플랫폼 특허와 신규 첨가제 특허가 시간적으로 연결됨

  limitation:
    - 미드니켈 제품과 직접 대응하는 특허가 아직 확정되지 않음
    - 양극·전해액의 실제 상용 조합은 공개되지 않음
    - 소재 공급사와의 공동 IP 여부 추가 조사 필요
```

특허 포트폴리오는 양극 조성 자체뿐 아니라 고전압에서 발생하는 전해액 산화·스웰링·계면 문제를 함께 다루는 형태다. 이는 고전압 셀을 소재 하나가 아니라 양극-전해액 계면 시스템으로 보호하는 전략으로 해석할 수 있다. ([구글 특허][1])

---

## 18.2 Silicon Fast-Charging Cluster

```text
Fast-Charging Anode IP
│
├── PF-D05-002 Fast-Charging Electrode
├── PF-D05-016 Silicon Anode Active Material
├── PF-D05-017 Multi-Layer Silicon–Graphite Anode
└── PF-D05-025 Candidate Family
    └── Earlier Two-Layer Graphite–Silicon Anode
```

`PF-D05-002`는 급속충전 전극의 광범위한 구조, `PF-D05-016`은 실리콘계 활물질 수명, `PF-D05-017`은 고용량층과 저저항층의 조합에 초점을 둔다. 세 패밀리를 하나로 병합하지 않고 `FAST_CHARGING_ANODE_CLUSTER` 아래에서 상호보완 IP로 연결한다. ([구글 특허][4])

### Candidate Family Registration

```yaml
candidate_patent_family:
  candidate_id: PF-CAND-SKON-D05-001
  representative_publications:
    - US20210408534A1
    - US12062784B2
    - US12266792B2

  earliest_priority_date: 2020-06-30

  concept:
    - First anode active-material layer
    - Second graphite-based layer
    - Silicon material selectively included by layer
    - Capacity and resistance balancing

  status:
    - FAMILY_CONFIRMED
    - CANONICAL_SCOPE_REVIEW_REQUIRED
```

이 후보 패밀리는 두 음극 활물질층을 이용하고 특정 층에서 실리콘계 성분과 흑연 구조를 달리하는 구성을 다룬다. SF+ 및 이후 다층 음극 특허의 선행 내부 IP일 가능성이 높지만 청구항 중복범위 분석이 필요하다. ([구글 특허][13])

---

## 18.3 Separator Ownership Cluster

```text
SK On-Owned Separator IP
├── PF-D05-018 Porous Composite Separator
└── PF-D05-019 High-Withstand-Voltage Separator

SKIET-Owned or Affiliate Separator IP
└── ENPASS / Ceramic-Coated Separator Families
    └── Separate applicant and ownership audit required
```

SK온 자체 출원 분리막 특허와 SKIET 소재 특허는 기술적으로 관련되더라도 법적 소유주체가 다르다. 제품 BOM을 확인하지 않고 `SK온이 SKIET 분리막 특허를 소유한다`거나 `모든 SK온 셀에 SK온 자체 분리막 특허가 적용된다`고 표현해서는 안 된다. ([구글 특허][7])

---

## 18.4 Thermal Propagation Cluster

```text
Thermal Propagation IP Evolution
│
├── PF-D05-020 Thermal Barrier Module
│   └── Basic inter-cell heat barrier
│
├── PF-D05-021 Flame Blocking Member
│   └── Fire-resistant and insulated cell spaces
│
├── PF-D05-022 Multilayer Blocking Assembly
│   ├── Silica aerogel
│   ├── Fireproof sheets
│   └── Buffer pads
│
├── PF-D05-008 Pouch Ventilation Device
└── PF-D05-009 Module Vent Hole and Gas Path
```

초기 패밀리는 셀 사이의 열 차단에 집중하고, 후속 특허는 난연층·에어로젤·완충패드와 가스 배출구조를 복합화하는 방향으로 확장된다. 이는 D04에서 정의한 `단열 → 화염차단 → 팽창흡수 → 가스배출`의 계층형 안전구조와 일치하는 포트폴리오 흐름이다. ([구글 특허][8])

---

## 18.5 Diagnostics·Lifecycle Cluster

```text
Battery Intelligence IP
│
├── PF-D05-004 Voltage Measurement Correction
├── PF-D05-005 SOH Estimation
├── PF-D05-006 Battery Ledger
├── PF-D05-007 AI Fault Detection
└── PF-D05-023 EIS-Based Abnormality Detection
```

```yaml
cluster_layers:
  sensing_and_correction:
    - PF-D05-004

  state_estimation:
    - PF-D05-005

  lifecycle_identity:
    - PF-D05-006

  data_driven_fault_detection:
    - PF-D05-007

  electrochemical_diagnostics:
    - PF-D05-023
```

이 클러스터는 단순 BMS 보호로직에서 SOH·배터리 원장·AI 이상감지·EIS 진단까지 확장된다. 즉 SK온의 디지털 IP는 `센서값 보정 → 상태 추정 → 생애주기 추적 → 이상 예측`의 연속 구조로 정리할 수 있다.

---
