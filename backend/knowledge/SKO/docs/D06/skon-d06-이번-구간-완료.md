---
id: skon-d06-이번-구간-완료
title: 이번 구간 완료
summary: SK온 배터리 제조공정 D06 단계에서 완료된 전극 제조 공정들과 다음 시작점인 셀 조립 단계의 진행 로드맵을 제시한 문서
tags: [d06, process, build-log, schema]
keywords: [D06, 제조공정, 셀 어셈블리, 전극 제조, 드라이룸, 프로세스 스키마, 제조 진행상황, Z폴딩, 파우치 포밍, Manufacturing Research Pack, 습식 혼합, 셀 조립, Z-폴딩, 캘린더링, 원재료 입고, 공정 흐름도, Pain Point, OI Seeds]
related: []
priority: reference
domain: D06
section: ""
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 958
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# 이번 구간 완료

* `D06-00 Domain Boundary`
* 제조근거 경계 및 SK온·산업 Baseline 분리
* Manufacturing Research Pack **10건**
* End-to-End 셀·팩 제조공정 흐름
* Manufacturing Process Schema
* Process Entity **24개** 초기 등록
* 원재료 입고·저장·계량
* 습식 혼합·Slurry Data Model
* 코팅·건조·용매회수
* 캘린더링·AI Data Architecture
* 슬리팅·노칭·최종 전극건조
* Material-to-Cell Genealogy
* Electrode Process Pain Point **7개**
* Manufacturing OI Seed **7개**

## 현재 D06 진행상태

```yaml
progress:
  D06_00_domain_boundary: COMPLETE
  D06_RP_001_research_pack: COMPLETE_V1
  D06_01_end_to_end_flow: COMPLETE_V1
  D06_02_process_schema: COMPLETE_V1

  electrode_manufacturing:
    receiving_and_storage: COMPLETE_V1
    wet_mixing: COMPLETE_V1
    coating_and_drying: COMPLETE_V1
    calendering: COMPLETE_V1
    slitting_and_notching: COMPLETE_V1
    final_electrode_drying: COMPLETE_V1

  manufacturing_genealogy: COMPLETE_V1
  initial_pain_point_register: COMPLETE_V1
  initial_oi_seeds: COMPLETE_V1

  cell_assembly: NOT_STARTED
  cell_finishing: NOT_STARTED
  module_pack_ctp: NOT_STARTED
  smart_factory_operations: PARTIALLY_PREPARED
```

## 다음 시작점

`D06-11 Cell Assembly & Dry-Room Operations`

```text
D06-11 Dry Room·Material Transfer
→ D06-12 Z-Folding·Precision Stacking
→ D06-13 Tab Joining·Current-Collector Welding
→ D06-14 Pouch Forming·Electrode Insertion
→ D06-15 Electrolyte Filling·Wetting
→ D06-16 Temporary Sealing
→ D06-17 Cell Assembly Defect Graph
→ D06-18 Cell Assembly OI Seeds
```

[1]: https://askinno.com/global/archives/153845?utm_source=chatgpt.com "[Battery Deep Dive] Part 3: The Dry Electrode Process"
[2]: https://askinno.com/global/archives/6216?utm_source=chatgpt.com "Z-folding, a technique that ensures the safety of SK ..."
[3]: https://eng.sk-on.com/company/press_view.asp?CompanyCode=011&idx=145&page=1&schtxt=&utm_source=chatgpt.com "Press Release < Press < Company < SK-ON"
[4]: https://www.linkedin.com/posts/sk-on_sk-on-cooperates-with-domestic-and-foreign-activity-7145402065891057666-S6Lt?utm_source=chatgpt.com "SK On's Post - LinkedIn"
[5]: https://askinno.com/global/archives/154429?utm_source=chatgpt.com "[Battery Deep Dive] Part 7: Pouch-Integrated Prismatic Cell"
[6]: https://publications.anl.gov/anlpubs/2019/03/150624.pdf "Report Number"
[7]: https://www.osti.gov/servlets/purl/1839768?utm_source=chatgpt.com "State-of-the-Art and Prospective Technologies for Lithium- ..."
[8]: https://www.osti.gov/biblio/1546514?utm_source=chatgpt.com "Electrode manufacturing for lithium-ion batteries—Analysis of current and next generation processing (Journal Article) | OSTI.GOV"
[9]: https://greet.anl.gov/files/Li_battery_update_2017?utm_source=chatgpt.com "Update of Life Cycle Analysis of Lithium-ion Batteries in the ..."
[10]: https://www.nrel.gov/docs/fy14osti/61889.pdf?utm_source=chatgpt.com "EERE Quality Control Workshop Final Report"
[11]: https://www.ornl.gov/research-highlight/identifying-degradation-mechanisms-lithium-ion-batteries-coating-defects-cathode?utm_source=chatgpt.com "Identifying degradation mechanisms in lithium-ion batteries with coating defects at the cathode"
[12]: https://askinno.com/global/archives/153845 "[Battery Deep Dive] Part 3: The Dry Electrode Process - Ask Inno Global"

---
