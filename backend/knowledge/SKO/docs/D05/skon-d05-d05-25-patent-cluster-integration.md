---
id: skon-d05-d05-25-patent-cluster-integration
title: Patent Cluster Integration
summary: "CTP, On-Vent, 제조검사 시스템 관련 SK온 특허의 구성, 보호범위, IP갭, 협력 구조를 정리한 포트폴리오 가이드"
tags: [d05, rnd, schema]
keywords: [CTP, On-Vent, 제조검사, X-레이 검사, 버스바, 파열압력, FTO, 특허 포트폴리오, 셀 형상, AI 용접, 파우치셀, 열경로, X-ray, 가스배출, 용접제어, 검사시스템]
related: []
priority: normal
domain: D05
section: D05-25.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1232
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-25. Patent Cluster Integration

## 25.1 Form-Factor·CTP IP Cluster

```text
CTP AND FORM-FACTOR IP
│
├── PF-D05-027 Direct-to-Pack Pouch Cell
│   ├── Module casing reduction
│   ├── Bottom thermal contact
│   ├── Side-cover reinforcement
│   └── Gas-discharge channel
│
├── PF-D05-028 Corner-Lead Pouch Cell
│   ├── Reduced inactive area
│   ├── Multidirectional busbar joining
│   └── Direct pack installation
│
├── PF-D05-029 Thermal-Path CTP·CTC Pack
│   ├── Thermal-resistance path
│   ├── Independent cooling
│   └── Abnormal-group separation
│
└── PF-D05-010 Pack Assembly Structure
    └── Cell-stack positioning and fixing
```

### 포트폴리오 해석

```yaml
ctp_ip_interpretation:

  protected_layers:
    cell_geometry:
      - Corner lead
      - Heat-exchange surface
      - Inactive-space reduction

    cell_to_pack_interface:
      - Direct cell seating
      - Thermal interface
      - Electrical insulation
      - Busbar joining

    pack_structure:
      - Side-cover reinforcement
      - Thermal path
      - Gas discharge
      - Abnormal-cell or module separation

  evidence_gap:
    - S-Pack+ 전체 구조와의 일대일 매핑
    - 실제 양산팩 적용
    - 접착제·자동화·재작업 관련 특허
    - 파우치 통합 각형의 알루미늄 외부케이스 특허군
```

SK온의 CTP 관련 공개 IP는 단순 모듈 제거보다 셀 형상, 열교환면, 버스바 접합, 구조강성, 가스 배출과 열전파경로를 함께 보호하는 방향으로 형성돼 있다.

---

## 25.2 On-Vent IP Cluster

```yaml
on_vent_ip_cluster:

  core_families:
    - PF-SKON-D05-025
    - PF-SKON-D05-026

  claim_focus:
    - Vent-notch pattern
    - Stress concentration
    - Target fracture pressure
    - Case-side vent placement
    - Directional gas release

  patent_gap:
    - Laser engraving equipment
    - Inline notch-depth measurement
    - Closed-loop laser control
    - 100-percent rupture-pressure inspection
    - On-Vent pack gas-channel integration
```

공개된 On-Vent 핵심 패밀리는 노치 패턴과 파열압력 제어에 집중된다. 레이저 광원·스캐너·깊이 측정과 폐루프 공정제어는 별도 특허군 또는 장비기업의 Background IP일 가능성이 있어 FTO를 분리해야 한다.

---

## 25.3 Manufacturing Inspection IP Cluster

```text
MANUFACTURING INSPECTION IP
│
├── PF-D05-030 Cell Inspection System
│   ├── Multi-station cell handling
│   ├── Electrical inspection
│   └── Repeated X-ray imaging
│
├── PF-D05-031 X-Ray Alignment Inspection
│   ├── Electrode edge detection
│   ├── Reference-value comparison
│   └── Defect classification
│
└── PF-CAND-D05-002 AI Welding Control
    ├── Weld-image analysis
    ├── Defect prediction
    └── Closed-loop welding adjustment
```

### OI 연결

```yaml
inspection_oi_link:

  internal_ip_assets:
    - Inspection system architecture
    - X-ray alignment algorithm
    - Battery-specific defect criteria

  external_capability_candidates:
    - High-speed X-ray source
    - TDI line detector
    - Sparse-view CT
    - Synthetic defect data
    - AI reconstruction
    - Radiation-safe inline automation

  preferred_collaboration_structure:
    - SK On owns battery defect definitions
    - Equipment partner retains generic hardware IP
    - Joint foreground IP for battery-specific control
    - Production data remains SK On confidential
```

---

## 25.4 Oxide Solid-State IP Cluster

```text
OXIDE SOLID-STATE IP
│
├── PF-D05-032 Photonic-Sintered Electrolyte Sheet
│   ├── Light-absorbing oxide particles
│   ├── Pulsed-light sintering
│   ├── Thin and large-area sheet
│   └── Oxide solid-state cell
│
└── PF-D05-033 LLZO Ceramic Joint Patent
    ├── LLZO composition and microstructure
    ├── Oxide ceramic manufacturing
    ├── Lithium-metal / anode-free option
    └── Joint ownership with Dankook University
```

PF-D05-032는 제조공정·시트 구조에, PF-D05-033은 LLZO 소재와 전지구조에 상대적으로 초점이 있다. 두 패밀리를 조합하면 `소재 조성 → 박막 성형 → 광소결 → 전고체 셀 적용`의 IP 체인이 형성된다.

---
