---
id: skon-d04-d04-051-d04-051-solvent-drying-recovery-oi-metad
title: D04-051 — Solvent Drying & Recovery — OI Metadata
summary: "배터리 전극 제조의 용제 건조·회수와 후속 가공 공정(캘린더링, 슬리팅)의 기술 메타데이터 및 핵심 공정 파라미터 정리"
tags: [d04, technology, schema]
keywords: [열펌프 건조, 배기열 회수, 전극 캘린더링, 밀도 제어, 기공률, 슬리팅, 노칭, 집전체 접착, 포로시티, 롤 압력, 용제 건조, solvent recovery, 건식전극, 열펌프, 회수율, 공정 파라미터, 에너지 효율, roll-to-roll]
related: []
priority: normal
domain: D04
section: D04-051
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Manufacturing Technology Master > D04-051 — Solvent Drying & Recovery
tokens: 1193
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Manufacturing Technology Master > D04-051 — Solvent Drying & Recovery

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - Heat-pump drying
    - Infrared or microwave-assisted drying
    - Exhaust heat recovery
    - Solvent concentration sensor
    - Drying-profile digital twin
    - Binder-migration control

  poc_kpis:
    - Energy per square meter
    - Residual solvent
    - Drying time
    - Solvent recovery rate
    - Electrode adhesion
    - Factory footprint
```

---

## TECH-SKON-D04-052 — Electrode Calendering

```yaml
technology_id: TECH-SKON-D04-052
canonical_name: Electrode Calendering
korean_name: 전극 캘린더링

technology_category:
  - Electrode Densification
  - Roll-to-Roll Manufacturing
  - Thickness and Porosity Control

technology_status:
  wet_electrode: COMMERCIAL_INDUSTRY_BASELINE
  dry_electrode: CRITICAL_DEVELOPMENT_TECHNOLOGY

process_mechanism:
  - Pass electrode through rotating rolls
  - Compress active-material layer
  - Control thickness and density
  - Improve particle and current-collector contact
  - Establish target porosity

critical_process_parameters:
  - Roll gap
  - Roll pressure
  - Roll temperature
  - Line speed
  - Electrode temperature
  - Incoming thickness
  - Material formulation

critical_quality_attributes:
  - Electrode density
  - Thickness
  - Porosity
  - Surface flatness
  - Adhesion
  - Through-plane transport
  - Mechanical integrity

technical_tradeoffs:
  - Higher density versus ion transport
  - Lower porosity versus electrolyte wetting
  - High pressure versus cracking
  - High speed versus uniformity
  - Energy density versus fast-charge performance

related_ai:
  - TECH-SKON-D04-039 AI Calendering Process Control

source_ids:
  - SRC-SKON-D04-035
  - SRC-SKON-D04-040

confidence:
  process_definition: VERY_HIGH
  sk_on_control_window: NOT_DISCLOSED
```

캘린더링은 전극의 두께·밀도·기공률을 결정하는 핵심 공정이다. 특히 건식전극에서는 분말층을 균일하게 압착하고 집전체에 결합해야 하므로 롤 속도·압력·온도를 동시에 관리하는 것이 양산성의 핵심으로 제시된다. SK온은 이 단계에 실시간 AI 제어를 적용하고 있다고 공개했다. ([ASK Inno][7])

---

## TECH-SKON-D04-053 — Slitting, Notching & Edge Quality

```yaml
technology_id: TECH-SKON-D04-053
canonical_name: Electrode Slitting, Notching and Edge-Quality Control
korean_name: 전극 슬리팅·노칭·단면 품질제어

technology_category:
  - Electrode Finishing
  - Precision Cutting
  - Defect Prevention

technology_status:
  base_process: INDUSTRY_BASELINE
  sk_on_specific_method: NOT_DISCLOSED

process_functions:
  slitting:
    - Divide wide coated electrode roll into narrower rolls

  notching:
    - Cut electrode into required cell geometry
    - Form tab or uncoated connection region

  punching:
    - Produce individual electrode sheets where required

critical_process_parameters:
  - Cutting speed
  - Blade or laser condition
  - Web tension
  - Cut position
  - Tool alignment
  - Dust extraction
  - Heat-affected zone for laser process

critical_quality_attributes:
  - Dimensional accuracy
  - Edge straightness
  - Burr height
  - Particle generation
  - Tab geometry
  - Coating-edge integrity

defect_modes:
  - Metallic burr
  - Delamination
  - Edge crack
  - Dust contamination
  - Misaligned tab
  - Heat damage
  - Inconsistent electrode dimensions

safety_link:
  - Burr or metal particle may damage separator
  - Dimensional error may degrade Z-Folding alignment

source_ids:
  - SRC-SKON-D04-036
  - SRC-SKON-D04-039
  - SRC-SKON-D04-040

confidence:
  industry_process: VERY_HIGH
  sk_on_cutting_method: NOT_DISCLOSED
```

DOE 공정분류에는 캘린더링 이후 슬리팅·펀칭과 적층이 포함된다. SK온의 Z-Folding은 전극과 분리막 가장자리의 정밀한 정렬을 안전요소로 강조하므로, 전단면의 버·분진·치수오차는 후속 적층 안전과 직접 연결되는 품질항목으로 관리할 필요가 있다. ([energy.gov][5])
