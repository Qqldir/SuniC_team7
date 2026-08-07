---
id: skon-d06-d06-rp-002-cell-assembly-research-pack
title: 002. Cell Assembly Research Pack
summary: "배터리 셀 조립 공정에서 사용되는 Z-폴딩, 분리막 함침, 전해액 주입, 탭 접합 등의 기술들을 다루는 기술자료와 연구논문 종합자료집"
tags: [d06, process, schema]
keywords: [Z-Folding, 셀 조립, 전극 적층, 분리막, 전해액 주입, 건식 조립, 리튬이온 배터리, 탭 용접, Z-폴딩, 분리막 함침, 건식조립, 탭 접합, 극판, 전기자동차 배터리]
related: []
priority: normal
domain: D06
section: D06-RP
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1163
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-RP-002. Cell Assembly Research Pack

## SRC-SKON-D06-011 — Z-Folding 공식 기술자료

```yaml
source_id: SRC-SKON-D06-011
title: Z-Folding, a Technique that Ensures the Safety of SK Batteries
publisher: SK Innovation
source_type: Official Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Continuous separator is folded in a zigzag pattern
  - Positive and negative electrodes are inserted alternately
  - The process is intended to reduce physical contact between electrodes
  - The technology is associated with SK On pouch-cell manufacturing

not_confirmed:
  - Actual stacking speed
  - Electrode alignment tolerance
  - Separator tension
  - Yield
  - Current equipment vendor
```

SK온은 Z-Folding을 연속 분리막을 지그재그로 적층하면서 양극과 음극을 교대로 삽입하는 기술로 설명하며, 전극 간 물리적 접촉을 방지하는 안전 목적을 제시한다. ([ASK Inno][1])

---

## SRC-BASE-D06-012 — Cell Assembly Manufacturing Review

```yaml
source_id: SRC-BASE-D06-012
title: State-of-the-Art and Prospective Technologies for Lithium-Ion Battery Electrode Processing
publisher: Oak Ridge National Laboratory
publication_year: 2021
source_type: Peer-Reviewed Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_scope:
  - Dry cell assembly
  - Winding and stacking
  - Separator stacking
  - Z-folding
  - Cell enclosure
  - Electrolyte filling
```

리튬이온 셀의 건식 조립은 전극을 적층하거나 권취하는 방식, 분리막을 개별 적층하거나 Z-folding하는 방식 등으로 구분할 수 있다. 이는 일반 제조기술 분류이며 SK온의 세부 라인 구성을 의미하지 않는다. ([OSTI][2])

---

## SRC-BASE-D06-013 — Separator Wetting Research

```yaml
source_id: SRC-BASE-D06-013
title: On Electrolyte Wetting through Lithium-Ion Battery Separators
source_type: Peer-Reviewed Research
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_scope:
  - Separator electrolyte absorption
  - Wetting speed
  - Ionic-transport preparation
  - Filling-process implications
```

전해액이 분리막과 전극의 기공구조에 빠르고 균일하게 침투하는 것은 이온전달과 셀 조립 생산성에 중요하다. ([OSTI][3])

---

## SRC-BASE-D06-014 — Electrolyte Filling & Wetting Review

```yaml
source_id: SRC-BASE-D06-014
title: Systematic Literature Analysis on Electrolyte Filling and Wetting
publication_year: 2023
source_type: Peer-Reviewed Systematic Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_scope:
  - Electrolyte dosing
  - Vacuum-assisted filling
  - Pressure-assisted infiltration
  - Soaking and wetting
  - Filling quality
  - Manufacturing cost and cycle time
```

전해액 주입과 함침은 셀 품질에 직접 영향을 주면서도 공정시간과 비용 부담이 큰 제조단계로 평가된다. ([MDPI][4])

---

## SRC-BASE-D06-015 — Joining Technology Review

```yaml
source_id: SRC-BASE-D06-015
title: Tab-to-Busbar Interconnections in Electric-Vehicle Battery Packs
publication_year: 2025
source_type: Peer-Reviewed Review
source_grade: A_PLUS
evidence_level: THIRD_PARTY_VERIFIED

covered_joining_methods:
  - Laser-beam welding
  - Ultrasonic welding
  - Resistance welding

covered_quality_dimensions:
  - Electrical resistance
  - Mechanical strength
  - Heat generation
  - Process repeatability
  - Dissimilar-material joining
```

배터리 접합에는 레이저·초음파·저항용접 등이 사용될 수 있으며, 적합한 방식은 소재조합·접합부 형상·생산속도와 요구 전기저항에 따라 달라진다. 이는 일반 산업 기준이며 SK온이 특정 공법을 사용하는지에 대한 직접 근거는 아니다. ([ScienceDirect][5])

---
