---
id: skon-d05-d05-16-patent-data-quality-register-v1
title: Patent Data Quality Register v1
summary: "SK온 특허 포트폴리오의 데이터 품질 이슈 8가지(법적 상태 신뢰성, 권리이전 정규화, 중복 가능성, 브랜드 기술 범위 등)를 심각도·조치·상태별로 추적하는 관리 레지스터"
tags: [d05, rnd, core-candidate, schema]
keywords: [특허 품질 이슈, 권리이전 정규화, 중복 가능성, PCT 상태 혼동, KIPRIS, 데이터 정제, Family ID, 심각도 분류, SK Innovation 이전, 특허 추적, 특허 데이터 검증, Z-Folding, Google Patents, 법적 상태, Patent Family, 중복 제거, PCT 국가단계, 데이터 정합성]
related: []
priority: critical
domain: D05
section: D05-16.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 1778
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-16. Patent Data Quality Register v1

```yaml
patent_data_quality:

  - issue_id: DQ-D05-PAT-001
    issue: Google Patents 법적 상태는 공식 법률판단이 아님
    severity: VERY_HIGH
    action:
      - KIPRIS
      - USPTO Patent Center
      - EP Register
      - PATENTSCOPE
    status: OPEN

  - issue_id: DQ-D05-PAT-002
    issue: SK Innovation에서 SK On으로 이전된 권리 정규화 필요
    severity: VERY_HIGH
    action:
      - Assignment event table 생성
      - 국가별 이전등록 확인
    status: IN_PROGRESS

  - issue_id: DQ-D05-PAT-003
    issue: 동일 제목의 분할·계속출원 중복 가능성
    examples:
      - Fast-Charging Electrode
      - Dry Electrode Sheet
    severity: HIGH
    status: OPEN

  - issue_id: DQ-D05-PAT-004
    issue: 동일 우선일이지만 별도 발명인 팩 특허 존재
    severity: HIGH
    control:
      - Priority application number
      - Inventor
      - Independent claim
      - Family ID 동시 비교
    status: CONTROL_DEFINED

  - issue_id: DQ-D05-PAT-005
    issue: PCT 종료와 국가단계 권리상태 혼동 위험
    example:
      - PF-SKON-D05-012
    severity: VERY_HIGH
    status: CONTROL_DEFINED

  - issue_id: DQ-D05-PAT-006
    issue: Z-Folding 브랜드 기술과 실제 유효 특허군의 범위가 아직 미정
    severity: VERY_HIGH
    action:
      - 후속 electrode assembly patents 검색
      - 국가별 존속권리 확인
      - 청구항 비교
    status: OPEN

  - issue_id: DQ-D05-PAT-007
    issue: AI Researcher 셀 설계·원가예측 전용 특허군 미확인
    severity: HIGH
    action:
      - AI·설계·예측 키워드 확장
      - 공동출원·영업비밀 가능성 검토
    status: OPEN

  - issue_id: DQ-D05-PAT-008
    issue: 특허 존재가 실제 제품 적용을 의미하지 않음
    severity: VERY_HIGH
    control:
      - PATENT_SUPPORTS_TECHNOLOGY
      - PATENT_APPLIED_TO_PRODUCT
      관계 분리
    status: CONTROL_IMPLEMENTED
```

---

## 이번 구간 완료

* `D05-10 Patent Research Protocol`
* 특허 Evidence Hierarchy·Canonical Schema
* SK이노베이션·SK온·SKIET 출원인 정규화
* 권리이전·공동출원 관리규칙
* `D05-12 Patent Taxonomy v1.0`
* Applicant·Technology Query Library
* 초기 Patent Family Master **12개**

  * Z-Folding
  * 급속충전 전극
  * 건식전극
  * BMS 보정
  * SOH 추정
  * Battery Ledger
  * AI 이상감지
  * 파우치 배기
  * 모듈 벤트
  * 팩 조립
  * 전고체 복합양극
  * 리튬메탈-유리전해질 적층
* Patent–Technology Map
* Patent Data Quality Register v1

## 현재 D05 진행상태

```yaml
progress:
  D05_00_to_09_rnd_programs: COMPLETE_V1
  D05_10_patent_protocol: COMPLETE
  D05_11_applicant_normalization: COMPLETE_V1
  D05_12_patent_taxonomy: COMPLETE_V1
  D05_13_query_library: COMPLETE_V1
  D05_14_initial_family_master: COMPLETE_V1
  verified_patent_families: 12
  official_legal_status_audit: NOT_STARTED
  full_portfolio_search: IN_PROGRESS
```

## 다음 시작점

`D05-17 Expanded Patent Family Master`

```text
D05-17 Expanded Patent Family Master
├── High-Nickel Cathode
├── Mid-Nickel & High-Voltage Electrolyte
├── Silicon–Graphite Anode
├── Separator·SKIET Joint IP
├── Electrode Assembly Inspection
├── Thermal Barrier·Cooling
├── CTP·Pack Gas Path
├── Solid Electrolyte
├── Lithium-Metal Interface
├── ESS·EIS Diagnostics
└── AI Researcher Patent Gap
```

[1]: https://kipris.or.kr/khome/board/help/searchByRights.do?tab=patent&utm_source=chatgpt.com "홈 > 고객지원 > 검색도움말 > 권리별검색(특허)"
[2]: https://patents.google.com/patent/US20220102727A1/en "US20220102727A1 - Electrode for Secondary Battery Having Improved Fast Charging Performance, Method of Manufacturing the Same, and Secondary Battery Including the Same - Google Patents"
[3]: https://patents.google.com/patent/US12517185B2/zh "US12517185B2 - Method for detecting abnormal condition or fault of battery, and a battery management system operating the same 
        \- Google Patents"
[4]: https://patents.google.com/patent/US20230132102A1/ko "US20230132102A1 - Method for estimating state of health (soh) of battery 
        \- Google Patents"
[5]: https://patents.google.com/patent/WO2014042424A1/en "WO2014042424A1 - Method for stacking cells inside secondary battery and cell stack manufactured using same - Google Patents"
[6]: https://patents.google.com/patent/EP4283698A1/zh "EP4283698A1 - Method and apparatus for preparing dry electrode sheet for secondary battery, dry electrode sheet for secondary battery, electrode for secondary battery, and secondary battery - Google Patents"
[7]: https://patents.google.com/patent/US11811024B2/en "US11811024B2 - BMS and battery system 
        \- Google Patents"
[8]: https://patents.google.com/patent/US20230009714A1 "US20230009714A1 - Battery ledger management system and method of battery ledger management 
        \- Google Patents"
[9]: https://patents.google.com/patent/US20220407169A1/en "US20220407169A1 - Ventilation device for pouch-type secondary battery and battery module including the same - Google Patents"
[10]: https://patents.google.com/patent/US20240258640A1/ko "US20240258640A1 - Battery module comprising venting hole and battery pack comprising the same 
      \- Google Patents"
[11]: https://patents.google.com/patent/US20240178497A1/en "US20240178497A1 - Battery pack and method of assembling the same - Google Patents"
[12]: https://patents.google.com/patent/EP4376184A1/en "EP4376184A1 - Battery pack 
        \- Google Patents"
[13]: https://patents.google.com/patent/EP4651239A1/zh "EP4651239A1 - Composite cathode for all-solid-state lithium secondary battery, and all-solid-state lithium secondary battery including same - Google Patents"
[14]: https://patents.google.com/patent/WO2024025344A1/en "WO2024025344A1 - Negative electrode-glass electrolyte layer laminate, all-solid-state secondary battery including the same, and method of manufacturing the same 
        \- Google Patents"

---
