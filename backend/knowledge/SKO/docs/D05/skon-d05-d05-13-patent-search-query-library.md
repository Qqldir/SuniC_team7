---
id: skon-d05-d05-13-patent-search-query-library
title: Patent Search Query Library
summary: SK온 배터리 기술 특허를 효율적으로 검색하기 위한 출원인명·기술키워드·IPC분류 코드 조합 방법
tags: [d05, rnd, schema]
keywords: [출원인 검색, 기술 키워드셋, IPC 분류, 급속 충전, 건식 전극, 전고체 전지, KIPRIS, 배터리 특허, Z폴딩, 진단, 특허 검색, 출원인명, 기술 키워드, 배터리, 검색 쿼리, 특허 조회]
related: []
priority: normal
domain: D05
section: D05-13.
source: SK온_D05_RnD_Patents_and_Intellectual_Property.md
breadcrumb: ""
tokens: 929
updated: 2026-08-03
---

> SK온 · D05 R&D·특허·지식재산

# D05-13. Patent Search Query Library

## 13.1 Applicant Search Set

```yaml
applicant_queries:

  korean:
    - 에스케이온
    - 에스케이이노베이션
    - 에스케이아이이테크놀로지

  english:
    - SK On Co Ltd
    - SK ON CO LTD
    - SK Innovation Co Ltd
    - SK IE Technology Co Ltd

  joint_applicant_search:
    - SK On AND SK Innovation
    - SK On AND Solid Power
    - SK On AND PolyPlus
    - SK On AND university partner
```

KIPRIS에서는 단순 문자열보다 출원인 입력도우미의 법인 식별번호를 이용해 검색하는 것이 동명이인·표기차이 누락을 줄일 수 있다. ([KIPRIS][1])

---

## 13.2 Technology Keyword Sets

```yaml
technology_keyword_sets:

  fast_charging:
    korean:
      - 급속 충전
      - 초급속 충전
      - 리튬 석출
      - 저저항 음극
      - 이중층 전극
    english:
      - fast charging
      - rapid charging
      - lithium plating
      - low resistance anode
      - multilayer electrode

  dry_electrode:
    korean:
      - 건식 전극
      - 건식 전극 시트
      - 무용매 전극
      - 건식 코팅
    english:
      - dry electrode
      - dry electrode sheet
      - solvent-free electrode
      - dry coating
      - fibrillated binder

  folding:
    korean:
      - Z 폴딩
      - 지그재그 폴딩
      - 전극 조립체 적층
      - 스택형 젤리롤
    english:
      - Z-folding
      - zigzag folding
      - electrode assembly stacking
      - stack-type jelly roll

  safety:
    korean:
      - 배기구
      - 벤트홀
      - 가스 배출
      - 열전파
      - 열 차단
    english:
      - vent hole
      - ventilation device
      - gas discharge
      - thermal propagation
      - thermal barrier

  diagnostics:
    korean:
      - 배터리 건강상태
      - 이상감지
      - 고장진단
      - 잔여수명
    english:
      - state of health
      - abnormal fault detection
      - battery diagnosis
      - remaining useful life

  solid_state:
    korean:
      - 전고체 전지
      - 황화물 고체전해질
      - 리튬메탈
      - 고체 계면
    english:
      - all-solid-state battery
      - sulfide solid electrolyte
      - lithium metal
      - solid-solid interface
      - composite cathode
```

---

## 13.3 Classification Seed Set

```yaml
classification_seed_set:

  H01M:
    use: Battery materials, cells, modules and manufacturing

  G01R31_36:
    use: Battery electrical condition testing and monitoring

  G01R31_392:
    use: Battery ageing and SOH estimation

  H01M50_30:
    use: Gas escape and vent arrangements

  B60L:
    use: Electric-vehicle battery monitoring and control

search_rule:
  - 키워드 단독검색과 분류 단독검색을 모두 실행
  - 이후 Applicant AND Keyword AND Classification으로 교집합 생성
```

SOH 특허에는 `G01R31/392`, 모듈 벤트 특허에는 `H01M50/30` 분류가 실제로 부여돼 있어 검색 Seed로 활용할 수 있다. ([구글 특허][4])

---
