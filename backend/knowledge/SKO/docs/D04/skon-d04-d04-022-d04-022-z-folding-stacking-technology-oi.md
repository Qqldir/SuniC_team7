---
id: skon-d04-d04-022-d04-022-z-folding-stacking-technology-oi
title: D04-022 — Z-Folding Stacking Technology — OI Metadata
summary: "배터리 Z-Folding Stacking 공정에 필요한 기술 역량과 세라믹 코팅 분리막의 구조, 기능, 설계 트레이드오프"
tags: [d04, technology, schema]
keywords: [Z-Folding Stacking, 스택킹 속도, 전극 정렬 오차, 분리막 주름, 세라믹 코팅, ENPASS CCS, 분리막 안전 인터페이스, 내부 단락, 배터리 조립, 열 안전 기술, 세라믹 코팅 분리막, Ceramic-coated separator, Electrode alignment, Separator wrinkle detection, Thermal safety, Cell assembly]
related: []
priority: normal
domain: D04
section: D04-022
source: SK온_D04_Technology_Taxonomy.md
breadcrumb: Safety & Thermal Technology Master > D04-022 — Z-Folding Stacking Technology
tokens: 639
updated: 2026-08-03
---

> SK온 · D04 기술 분류체계·핵심기술 마스터 · Safety & Thermal Technology Master > D04-022 — Z-Folding Stacking Technology

### OI Metadata

```yaml
oi_metadata:
  preliminary_priority: HIGH

  external_capability_needs:
    - High-speed electrode-position vision
    - Separator wrinkle detection
    - Edge-burr inspection
    - Web-tension closed-loop control
    - Electrostatic particle-removal system
    - AI-based stacking drift prediction

  poc_kpis:
    - Electrode alignment error
    - Separator wrinkle density
    - Stacking speed
    - Internal-short defect rate
    - False detection rate
    - Equipment downtime
```

---

## TECH-SKON-D04-023 — Ceramic-Coated Separator Safety Interface

```yaml
technology_id: TECH-SKON-D04-023
canonical_name: Ceramic-Coated Separator Safety Interface
korean_name: 세라믹 코팅 분리막 안전 인터페이스

technology_category:
  - Separator Material
  - Thermal Safety
  - Affiliate Technology Interface

technology_status: COMMERCIAL_MATERIAL_TECHNOLOGY

technology_owner:
  company: SK IE Technology
  relationship_to_sk_on:
    - AFFILIATE_TECHNOLOGY
    - POTENTIAL_OR_ACTUAL_COMPONENT_INTERFACE
    - NOT_SK_ON_OWNED

material_structure:
  base:
    - Microporous polymer separator
  surface:
    - Ultra-thin ceramic coating

principal_functions:
  - Physically separate anode and cathode
  - Permit lithium-ion transport
  - Improve heat resistance
  - Reduce separator dimensional instability
  - Support cell safety under elevated temperature

named_affiliate_product:
  - ENPASS CCS

related_sk_on_technology:
  - Z-Folding
  - Pouch Cell Assembly
  - High-Nickel Cell Safety

technical_tradeoffs:
  - Added coating cost
  - Thickness-energy-density tradeoff
  - Ceramic-particle dispersion
  - Coating adhesion
  - Pore blockage
  - Electrolyte wettability
  - High-speed coating uniformity

source_ids:
  - SRC-SKON-D04-028

confidence:
  affiliate_technology: VERY_HIGH
  exact_sk_on_product_mapping: NOT_DISCLOSED
```

분리막은 양극과 음극의 물리적 접촉을 차단하면서 이온 이동은 허용하는 소재다. SKIET의 ENPASS CCS는 초박형 세라믹층을 적용해 내열성을 높인 기술로 공개됐지만, SK온의 모든 셀에 동일 사양이 적용된다고 일반화할 수는 없다. ([ASK Inno][2])
