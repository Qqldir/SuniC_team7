---
id: skon-d06-d06-61-human-readable-manufacturing-strategy-re
title: Human-Readable Manufacturing Strategy Report
summary: "배터리 제조에서 SK온의 파우치·CTP·검사기술 강점을 바탕으로 제조데이터 연결, 결함상류화, 공정최적화, 양산성 확보를 위한 6단계 실행전략"
tags: [d06, process]
keywords: [파우치 셀, 전극공정, 건식전극, 포메이션, CTP, 결함검사, Digital Twin, Ramp-Up, Genealogy, Reworkability, 파우치셀, Z-Folding, 결함상류화, Formation, 양산화, Rework, 공정데이터]
related: []
priority: normal
domain: D06
section: D06-61.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 1691
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-61. Human-Readable Manufacturing Strategy Report

## 61.1 SK온 제조기술의 공개 강점

### ① 파우치 셀 적층과 구조설계

SK온은 Z-Folding을 핵심 파우치 셀 조립기술로 공개하고 있다. 최근에는 기존 파우치 구조를 유지하면서 CTP, 넓은 면적 냉각과 파우치 통합 각형 등으로 팩 통합범위를 확장하고 있다.

### ② 전극공정의 차세대화

건식전극과 AI 기반 캘린더링은 용매·건조 부담과 전극 균일성 문제를 개선하려는 기술방향이다. 다만 현재 공개된 내용은 기술개발과 공정제어 개념이며 실제 대량생산 수율과 원가효과는 확인되지 않았다.

### ③ 검사기술의 다중화

공개특허에는 포메이션 곡선, 절연저항, 열화상, 누설, X-ray와 전기검사를 이용한 셀 결함검출 기술이 나타난다. 이는 SK온이 단일 검사보다 여러 신호를 조합하는 방향으로 개발 중임을 보여준다.

### ④ Digital Twin 협력

Siemens DISW와의 협력은 공장·공정 시뮬레이션, Virtual Commissioning과 Ramp-Up 개선의 기반이 될 수 있다. 다만 공개자료만으로는 연결형 Digital Twin이나 자동제어 수준까지 확인할 수 없다.

---

## 61.2 핵심 제조 Pain Point

### 후기공정에서 발견되는 상류불량

코팅·압연·절단·적층·용접·함침에서 발생한 문제가 포메이션, 에이징 또는 X-ray에서 뒤늦게 검출될 수 있다. 검출이 늦을수록 소재·공정·검사비가 누적돼 Value-Added Scrap이 커진다.

### 포메이션·에이징 WIP

포메이션과 에이징은 처리시간과 설비·공간 점유가 크다. 고정 Recipe와 고정 대기시간은 정상 셀의 과잉처리와 이상 셀의 지연검출을 동시에 만들 수 있다.

### CTP의 Rework 문제

CTP는 부품과 조립단계를 줄일 수 있지만 하나의 결함이 더 큰 Pack Assembly에 영향을 미칠 가능성이 있다. Cell 또는 부분 Assembly를 안전하게 제거·교체하는 Rework 설계가 중요하다.

### 공장 간 학습의 단절

동일 제품이라도 설비규모·센서·소재·환경이 다르면 공정 설정값을 그대로 복사하기 어렵다. 숫자 Recipe가 아니라 공정의 목표품질과 정규화된 물리량을 이전해야 한다.

---

## 61.3 최우선 실행전략

### 1단계 — 제조 데이터 기반

먼저 소재 Lot, 전극 Roll 좌표, Cell·Module·Pack Serial과 설비 Event를 연결해야 한다. Genealogy가 없으면 결함예측이나 AI는 원인분석 도구가 아니라 상관관계 Dashboard에 머무를 가능성이 높다.

### 2단계 — 결함 검출의 상류 이동

Formation·X-ray·Pack EoL에서 발견되는 불량을 코팅, 절단, 적층, 접합과 열전도재 도포 단계에서 조기에 예측해야 한다. 목표는 검사장비 추가가 아니라 폐기범위와 결함검출 지연을 줄이는 것이다.

### 3단계 — Cell Finishing 최적화

Adaptive Formation, Accelerated Aging, Formation Energy Recovery와 WIP Scheduling을 하나의 과제로 묶어야 한다. 품질을 희생하지 않는 범위에서 처리시간과 에너지·재공품을 함께 줄이는 것이 중요하다.

### 4단계 — CTP 제조성 확보

압축, 열전도계면, Busbar 접합, 냉각누설과 Reworkability를 CTP 설계단계부터 함께 다뤄야 한다. 제품 공간효율만으로는 양산성과 유지보수성을 보장할 수 없다.

### 5단계 — Ramp-Up 지식 재사용

신규 공장에서 발생한 문제와 해결책을 Recipe 문서가 아니라 `문제–원인–조치–검증–적용범위` 구조로 저장해야 한다. Virtual Commissioning과 Cross-Plant Transfer는 이 지식이 표준화된 뒤 효과가 커진다.

### 6단계 — 제조 AI·OT 통제

AI Model, PLC Logic, Robot Program과 Recipe 변경을 하나의 변경관리 체계로 묶고, 승인·검증·Rollback·Cybersecurity 기록을 남겨야 한다.

---

## 61.4 FACT·ANALYSIS·HYPOTHESIS

**FACT**

SK온은 Z-Folding, 건식전극과 AI 캘린더링, CTP·LSC, 파우치 통합 각형, Digital Twin 협력을 공식 공개했다. 포메이션·X-ray·누설·열화상 등 검사 관련 특허출원도 확인된다.

**ANALYSIS**

공개자료상 SK온의 제조 차별화 방향은 파우치 셀 기술을 기반으로 전극공정·검사·CTP·Digital Twin을 연결하는 데 있다. 제조경쟁력을 실제로 확보하려면 개별 기술보다 소재–공정–검사–수율의 데이터 연결이 우선돼야 한다.

**HYPOTHESIS**

Material-to-Pack Digital Thread와 Yield Causal Knowledge Graph가 구축되면, 후기불량의 상류 원인 추적과 국부 Scrap 격리, 공장 간 Ramp-Up 학습의 재사용성이 크게 높아질 가능성이 있다.

---
