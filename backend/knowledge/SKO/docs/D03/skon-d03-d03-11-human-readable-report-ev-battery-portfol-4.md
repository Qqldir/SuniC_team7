---
id: skon-d03-d03-11-human-readable-report-ev-battery-portfol-4
title: Human-Readable Report — EV Battery Portfolio
summary: "SK온의 전기차 배터리 포트폴리오(하이니켈 파우치, SF 급속충전, LFP, 각형 배터리)의 기술 현황과 상용화 진도 및 경쟁력을 정리한 평가 자료."
tags: [d03, product, schema]
keywords: [전기차 배터리, 하이니켈, 파우치형, 급속충전, LFP, 각형 셀, 에너지밀도, SF Battery, 충전시간, 상용화 현황, 각형배터리, 양산, NCM9+, SUFast]
related: []
priority: normal
domain: D03
section: D03-11.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Human-Readable Report
tokens: 2037
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Human-Readable Report

## 11.2 EV Battery Portfolio

### 11.2.1 High-Nickel Pouch Battery

SK온의 전통적 핵심 제품은 하이니켈 NCM 계열의 파우치형 전기차 배터리다. 하이니켈 배터리는 제한된 팩 공간에서 높은 에너지밀도와 긴 주행거리를 확보하는 데 유리하며, SK온은 이를 기반으로 SF Battery와 NCM9+ 등 제품·기술 브랜드를 개발해 왔다. ([SK Innovation][5])

D03에서 하이니켈 파우치 배터리는 다음과 같이 분류한다.

```yaml
product_family: High-Nickel Pouch Battery
commercial_status: COMMERCIAL
core_roles:
  - Long-range EV
  - Premium EV
  - Fast-charging EV
key_strengths:
  - Energy density
  - Established pouch manufacturing experience
  - Fast-charge product lineage
principal_risks:
  - Thermal stability
  - Raw-material cost
  - Fast-charge degradation
  - Silicon-anode expansion
```

개별 제품의 Ah 용량, 중량당 에너지밀도, 셀 수명, 고객별 셀 규격은 대부분 공개되지 않았다. 따라서 D03은 공식적으로 확인되는 제품군과 기술 특성을 저장하되, 고객별 사양을 유사 셀 데이터로 추정하지 않는다.

---

### 11.2.2 SF Fast-Charging Family

SF Battery는 약 18분 동안 배터리 충전상태를 10%에서 80%까지 높이는 것을 핵심 가치로 하는 급속충전 제품이다. 후속 제품인 Advanced SF는 자기정렬 공정을 적용해 기존 SF 대비 에너지밀도를 약 8% 높이면서 급속충전 성능을 유지하도록 개발됐다. ([ASK Inno][6])

SF+는 실리콘과 흑연을 결합한 이중층 음극 구조를 통해 10%에서 80%까지의 충전시간을 약 15분으로 줄인 공개 제품기술이다. 다만 구체적인 적용 차량과 양산물량은 공개자료에서 확인되지 않는다. ([ASK Inno][6])

Hyper Fast Battery는 SK온이 2026년 공개한 초급속충전 기술 시제품이다. 회사는 전극설계와 충전 프로토콜을 통합 최적화하는 SUFast 기술을 바탕으로 10%에서 80%까지 7분 미만 충전, 650Wh/L의 에너지밀도를 제시했다. 이 성능은 기술 시연값이며, 현재 상용 양산차의 확정 성능으로 해석해서는 안 된다. ([ASK Inno][7])

```text
SF Battery
  ↓
Advanced SF / SF+
  ↓
Hyper Fast Battery
  ↓
Required commercial validation
  ├─ 반복 급속충전 수명
  ├─ 저온 충전성능
  ├─ 리튬 도금 억제
  ├─ 차량·충전기 통합
  └─ 양산수율
```

**D03 분석**

SK온은 급속충전 기술 자체에서는 경쟁력 있는 성능을 공개하고 있다. 그러나 기술 시제품을 실제 제품 우위로 전환하려면 고객차량 적용, 충전 인프라 연동, 저온 운전, 반복 충전에 따른 수명 및 보증비용을 함께 검증해야 한다.

---

### 11.2.3 LFP EV Platform

SK온은 2023년 한국 배터리 기업 최초의 파우치형 LFP 시제품을 공개한 뒤, 저온성능·수명·에너지밀도를 개선하는 개발을 이어가고 있다고 설명한다. 공식 2026년 자료는 LFP를 EV와 ESS에 모두 적용 가능한 차세대 제품군으로 제시하고 있지만, D03 검토 범위에서는 EV용 LFP의 실명 고객계약과 양산개시를 확인하지 못했다. ([ASK Inno][8])

따라서 상태값은 다음과 같이 확정한다.

```yaml
entity: PROD-SKON-EV-007
name: LFP EV Platform
technology_status: DEVELOPMENT_CONFIRMED
commercial_status: PRE_COMMERCIAL
named_ev_customer: NOT_CONFIRMED
mass_production_start: NOT_CONFIRMED
```

경쟁사 LG에너지솔루션은 Renault Group의 Ampere와 39GWh 규모의 파우치형 LFP 공급계약을 확보했고, 파우치형 CTP를 적용한다고 발표했다. 이는 SK온이 EV용 LFP를 상용제품으로 전환할 때 직접 비교해야 할 사례다. ([LG][9])

---

### 11.2.4 Prismatic Platform

SK온은 2026년 각형 배터리 포트폴리오로 **On-Vent Prismatic Cell**과 **Pouch-Integrated Prismatic Cell**을 공개했다.

On-Vent 셀은 각형 알루미늄 캔에 레이저로 벤트 구조를 직접 가공해, 배출 위치와 방향을 팩 설계에 맞게 조정할 수 있도록 한 기술이다. 공식 자료에는 6,000회 이상의 반복 압력시험 후에도 목표 파열압력을 충족했다는 회사 시험결과가 제시됐다. ([ASK Inno][10])

Pouch-Integrated Prismatic Cell은 SK온의 파우치 셀 기술을 각형 외장구조와 결합해 설계 유연성과 구조적 안정성을 동시에 확보하려는 하이브리드 개념이다. 회사는 이를 셀 단위가 아니라 셀 배열과 팩 구조까지 포함한 시스템 기술로 설명한다. ([ASK Inno][11])

```yaml
prismatic_platform:
  status: PRE_COMMERCIAL
  prototypes:
    - On-Vent Prismatic Cell
    - Pouch-Integrated Prismatic Cell
  confirmed_mass_production: false
  confirmed_customer: false
  required_next_steps:
    - OEM validation
    - Can and sealing process validation
    - Vent reliability verification
    - Mass-production yield
    - Pack integration
```

---

### 11.2.5 CTP and Pack Architecture

SK온은 모듈 단계를 줄이거나 제거해 셀을 팩에 직접 구성하는 파우치형 CTP 기술을 개발하고 있다. CTP는 부품 수, 구조 중량 및 조립공정을 줄여 팩 공간효율과 가격경쟁력을 개선할 수 있지만, 열전파 방지와 구조 안전, 정비성 확보가 동시에 필요하다. ([ASK Inno][12])

인터배터리 2026에서는 파우치 CTP, Large-Surface Cooling CTP, 파우치 통합 각형 팩, 액침냉각 팩 등 네 가지 팩 솔루션이 공개됐다. LSC 구조는 셀 접촉면에 냉각판을 배치해 기존 간접냉각 대비 냉각성능을 최대 세 배 높인다는 회사 설명이 제시됐다. ([ASK Inno][7])

이 제품군은 D03에서 `PACK_SOLUTION_PROTOTYPE` 또는 `DEVELOPMENT` 상태로 관리한다. 전시된 구조의 존재는 확인되지만, 각 기술의 양산차 적용과 계약 여부는 별도 근거가 필요하다.

---
