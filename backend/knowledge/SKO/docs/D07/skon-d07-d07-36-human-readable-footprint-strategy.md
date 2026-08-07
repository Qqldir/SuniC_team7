---
id: skon-d07-d07-36-human-readable-footprint-strategy
title: Human-Readable Footprint Strategy
summary: "SK온의 공장별 설계역량이 실제 고객 출하 역량으로 전환되지 못하는 구조적 문제를 진단하고, 계약·공장·제품·고객 연결 관계를 추적하는 관리 시스템 5가지를 제안한다."
tags: [d07, footprint]
keywords: [캐파시티 전환율, 고객 승인 능력, HSBMA, Nissan Slate 계약, ESS 사업, 지분통합, 공정 호환성, 가동률, Cell 합격생산량, 정책적격 물량, Capacity 전환율, 고객승인 역량, Qualified Capacity, Contract-to-Capacity, Plant-Line-Product, 공장배정, SKBA, Tennessee]
related: []
priority: normal
domain: D07
section: D07-36.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1166
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-36. Human-Readable Footprint Strategy

## 1. SK온의 문제는 Capacity 부족보다 **Capacity 전환율**이다

공식 공시상 생산능력은 2024년 71.5GWh에서 2025년 94.6GWh, 2026년 1분기 97.4GWh로 증가했지만 평균 가동률은 2026년 1분기 36.5%였다. 두 수치의 산식은 다르지만, 설비 확장만으로 충분한 고객출하량과 수익성이 보장되지 않는다는 점은 분명하다. ([KIND][3])

따라서 핵심 KPI는 명목 GWh가 아니라 다음 네 가지가 되어야 한다.

```text
Design Capacity
→ Customer-Qualified Capacity
→ Good-Output Capacity
→ Commercially Allocable Capacity
```

---

## 2. 미국 Footprint는 세 가지 성격으로 분리된다

**SKBA Commerce**는 기존 양산거점이다. F-150 Lightning과 ID.4 생산이력은 확인되지만 현재 고객 Mix와 ESS 전환범위는 다시 확인해야 한다. ([켐프 주지사 사무실][1])

**HSBMA**는 현대차그룹과 연결된 50:50 JV다. 35GWh는 물리적 총설계능력이지만 다른 고객이나 ESS 사업에 자유롭게 전환할 수 있는 SK온 단독 Capacity가 아니다. ([HSAGP ENERGY LLC][2])

**Tennessee**는 향후 선택권이다. 2028년 생산개시까지 제품·고객·화학계·설비구성과 Workforce를 결정하고 검증해야 한다. ([SK][4])

---

## 3. Nissan·Slate 계약은 공장배정 문제가 남아 있다

Nissan 약 100GWh와 Slate 약 20GWh 계약은 미국산 배터리를 요구하지만 생산공장은 공개되지 않았다. 계약 총량을 연도별 수요곡선으로 나누고, 제품·화학계·고객승인·정책요건을 각 미국공장과 연결해야 실제 Capacity 요구량이 산출된다. ([SK][7])

---

## 4. HSBMA의 초기 과제는 35GWh 달성이 아니라 고객 Ramp 안정화다

HSBMA는 상업생산을 시작했지만, 상업생산 개시는 35GWh 전체가 즉시 합격품으로 공급된다는 의미가 아니다. 초기에는 IONIQ 9 생산계획과 Cell 합격생산량, 고객승인, 물류재고와 품질격리를 하나의 Control Tower에서 관리해야 한다. ([HSAGP ENERGY LLC][2])

---

## 5. 중국 재편은 지분통합과 공정통합을 구분해야 한다

SK On Jiangsu 지분을 100%로 높이고 Huizhou 지분을 처분하더라도, Yancheng의 서로 다른 공장과 Line이 동일 제품·고객을 즉시 생산할 수 있다는 뜻은 아니다. 지분통합 이후에도 설비·제품·고객승인·소재공급망의 실제 호환성을 별도로 검증해야 한다. ([KIND][5])

---

## 6. 가장 먼저 구축할 시스템

### ① Qualified Capacity Ledger

공장별 Capacity를 설계·설치·가용·고객승인·합격생산·경제가용 단계로 나눈다.

### ② Plant–Line–Product–Customer Graph

공장과 고객·차종·Cell Revision·화학계·계약·승인이 어느 시점에 연결됐는지 기록한다.

### ③ Contract-to-Capacity Bridge

Nissan·Slate·현대차그룹·ESS 계약을 연도별 GWh와 공장별 생산계획으로 전환한다.

### ④ Alternative Site Qualification Engine

공장중단 시 물리적으로 유사한 공장이 아니라 실제 고객승인과 정책요건을 충족한 대체공장을 찾는다.

### ⑤ 45X·PFE Eligibility Twin

미국 공장 생산량 중 실제 정책적격 가능 물량을 소재원산지·공급업체 지배구조와 함께 계산한다.

---
