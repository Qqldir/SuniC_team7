---
id: skon-d06-d06-rp-004-module-pack-assembly-research-pack
title: 004. Module·Pack Assembly Research Pack
summary: "SK온의 CTP 기술과 LSC, 파우치-프리즘 통합 등 모듈·팩 조립 변형 기술의 공식 기술 사양과 성능 개선 사항을 정리한 기술 자료 모음입니다."
tags: [d06, process, schema]
keywords: [CTP, 셀투팩, 냉각판, LSC, 파우치 셀, 프리즘형, 모듈 제거, 배터리 팩, 조립 공정, 팩 냉각, Cell-to-Pack, 셀 직접 조립, 프리즘셀, 배터리 팩 구조, 열관리 기술, 포우치-프리즘 통합]
related: []
priority: normal
domain: D06
section: D06-RP
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 2237
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-RP-004. Module·Pack Assembly Research Pack

## SRC-SKON-D06-024 — SK온 CTP 공식 기술자료

```yaml
source_id: SRC-SKON-D06-024
title: Cell-to-Pack Technology
publisher: SK Innovation
publication_date: 2026-01
source_type: Official Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - CTP removes the separate module stage
  - Cells are installed directly into the pack structure
  - Module-related components and assembly steps can be reduced
  - Pouch-type CTP is an SK On development direction

not_confirmed:
  - Commercial production plant
  - Actual manufacturing cost reduction
  - Actual pack yield
  - Customer nomination
```

SK온은 CTP를 셀을 먼저 모듈로 조립한 뒤 팩에 탑재하는 기존 구조와 달리, 셀을 팩 구조에 직접 조립해 모듈 단계를 제거하는 기술로 설명한다. 공간·중량·조립단계 절감은 회사가 제시한 기술적 기대효과이며 실제 양산원가 실적으로 해석하지 않는다. ([ASK Inno][1])

---

## SRC-SKON-D06-025 — Large-Surface Cooling CTP

```yaml
source_id: SRC-SKON-D06-025
title: Large-Surface Cooling CTP
publisher: SK Innovation
publication_date: 2026-03
source_type: Official Exhibition Technology Description
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Cooling plates are applied to cell contact surfaces
  - Technology is presented as part of SK On's CTP portfolio
  - Pouch CTP, LSC CTP, pouch-integrated prismatic and immersion-cooling packs were exhibited

manufacturer_claim:
  metric:
    name: Cooling performance improvement
    value: up_to_3_times
    comparator: Conventional indirect cooling
  claim_status: MANUFACTURER_CLAIM

not_confirmed:
  - Test method
  - Coolant conditions
  - Cell format
  - Pack boundary
  - Independent third-party verification
```

SK온은 LSC를 셀의 넓은 접촉면 사이에 냉각판을 적용하는 구조로 설명하며, 기존 간접냉각 대비 냉각성능이 최대 3배 향상된다고 주장한다. 해당 수치는 회사 설명에 따른 제조사 주장으로만 저장한다. ([ASK Inno][2])

---

## SRC-SKON-D06-026 — Pouch-Integrated Prismatic Cell

```yaml
source_id: SRC-SKON-D06-026
title: Pouch-Integrated Prismatic Cell
publisher: SK Innovation
publication_date: 2026-04-17
source_type: Official Technology Article
source_grade: A
evidence_level: DIRECT_OFFICIAL

confirmed:
  - Multiple mid-nickel pouch cells are stacked in an aluminum case
  - Pouch cells are bonded to a bottom cooling plate using thermal adhesive
  - Cooling plates may be placed between wide cell surfaces
  - Compression pads are positioned between cells
  - External busbars can connect directly to a PCB
  - Directional venting is integrated
  - Existing pouch-cell production lines may be utilized
  - Technology remains at prototype and final-validation stage

manufacturer_claims:
  - Improved internal pack-space utilization of approximately 6.1 percent
  - Reduced additional equipment investment
  - Assembly efficiency comparable to prismatic cells

claim_status: MANUFACTURER_CLAIM
```

공식 설명에 따르면 이 구조는 파우치 셀 적층체를 알루미늄 케이스에 수용하고, 열접착제로 하부 냉각판과 결합하며 셀 사이에는 압축패드를 둔다. 외부 버스바·PCB 연결과 방향성 벤팅도 포함되지만, 현재 상태는 최종 성능검증을 위한 시제품 단계다. ([ASK Inno][3])

---

## SRC-PAT-D06-027 — Direct-to-Pack Pouch Architecture

```yaml
source_id: SRC-PAT-D06-027
title: Pouch-Type Battery Cell and Battery Pack Including the Same
publication_number: US12113191B2
document_type: Patent Publication Reproduction
delivery_channel: PATENT_MIRROR
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

technical_scope:
  - Pouch-cell assembly seated directly in pack housing
  - Heat-exchange portion contacting thermal-conduction member
  - Refrigerant channel in pack bottom
  - Busbar assembly and insulation structure
  - Sidewall and center-beam gas-discharge holes
  - Neighboring cell-assembly fastening structure

legal_status:
  official_register_verified: false
  status_use: DOCUMENT_IDENTIFIED_ONLY
```

특허문서는 파우치 셀의 열교환부를 팩 하부 열전도부재와 직접 접촉시키고, 팩 하부 냉매채널·버스바·절연구조·가스 배출구를 결합하는 CTP 구조를 다룬다. 미러에 표시된 존속·소유권 정보는 공식 등록부 확인 전 확정하지 않는다. ([구글 특허][4])

---

## SRC-PAT-D06-028 — Busbar·Sensing Module Architecture

```yaml
source_id: SRC-PAT-D06-028
title: Busbar and Battery Module Including Same
publication_number: US12597680B2
document_type: Patent Publication Reproduction
delivery_channel: PATENT_MIRROR
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

technical_scope:
  - Pouch cells arranged in module housing
  - Electrode tabs inserted through housing and busbar openings
  - Tabs bent and joined to busbar plate
  - Busbar connected to sensing module and FPCB
  - Laser welding disclosed as one joining option

legal_status:
  official_register_verified: false
```

이 특허문서는 파우치 셀 전극탭을 하우징과 버스바판의 슬롯에 통과시킨 뒤 절곡·접합하고, 버스바 어셈블리와 FPCB 기반 센싱모듈을 연결하는 구조를 설명한다. ([구글 특허][5])

---

## SRC-PAT-D06-029 — Heat-Blocking Member Assembly Equipment

```yaml
source_id: SRC-PAT-D06-029
title: Battery Module, Assembly Apparatus and Assembly Method
publication_number: US20250079580A1
document_type: Patent Application Publication Reproduction
delivery_channel: PATENT_MIRROR
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

technical_scope:
  - Pre-assembled cell assembly and busbar assembly
  - Alignment member inserted between neighboring cells
  - Solid heat-blocking member inserted into separation space
  - Pressure sensing during insertion
  - Cell and heat-blocking-member height inspection

legal_status:
  official_register_verified: false
  status_use: PENDING_APPLICATION_DOCUMENT_IDENTIFIED
```

SK온 출원은 인접 셀 사이 공간을 정렬부재로 확보한 뒤 고체형 열차단부재를 삽입하고, 삽입압력과 셀·차단재 높이를 검사하는 조립장비를 제안한다. 이는 공개출원 기술이며 실제 양산설비 적용 여부는 확인되지 않았다. ([구글 특허][6])

---

## SRC-PAT-D06-030 — Cooling·Blocking Integrated Battery Case

```yaml
source_id: SRC-PAT-D06-030
title: Battery Case and Battery Pack Including the Same
publication_number: US20240283052A1
document_type: Patent Application Publication Reproduction
delivery_channel: PATENT_MIRROR
source_grade: A_PLUS
evidence_level: DIRECT_REGULATORY

technical_scope:
  - Cooling panels and blocking panels arranged in pack case
  - Coolant inlet, outlet and circulation channels
  - Battery assemblies inserted into accommodating spaces
  - Cooling panel provides heat-transfer contact
  - Blocking panel limits thermal propagation

legal_status:
  official_register_verified: false
```

이 출원은 팩 내부에서 냉각패널과 차단패널을 번갈아 배치하고, 냉매 입·출구 및 순환유로를 통해 셀을 냉각하면서 구획 간 열전파를 억제하는 구조를 다룬다. ([구글 특허][7])

---
