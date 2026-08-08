---
id: skon-d03-d03-11-human-readable-report-ess-product-portfo-5
title: Human-Readable Report — ESS Product Portfolio
summary: "SK온의 LFP 기반 ESS 제품들(GRIDON Gen 1/2)의 기술 특징, 상용화 일정, 경쟁사 대비 차별화 요소를 설명한다."
tags: [d03, product, schema]
keywords: [GRIDON, LFP 배터리, EIS 진단 기술, 냉각수 침지, 에너지저장시스템, 컨테이너 블록, BMS, 미국 생산, 에너지밀도, 안전기술, LFP, 에너지저장장치, EIS 진단, 파우치 셀, 미국 시장, 상용화 계획]
related: []
priority: normal
domain: D03
section: D03-11.
source: SK온_D03_Products_and_Solutions.md
breadcrumb: Human-Readable Report
tokens: 1214
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션 · Human-Readable Report

## 11.3 ESS Product Portfolio

### 11.3.1 LFP Pouch Battery for ESS

SK온 ESS 제품의 핵심 화학계는 LFP다. 회사는 NCM 배터리 개발에서 축적한 전극설계와 공정기술을 LFP에 적용해 저온성능, 수명, 에너지밀도를 개선하고 있다고 설명한다. ([ASK Inno][8])

인터배터리 2026에서는 대형 셀 수요에 대응한 고에너지밀도 파우치형 LFP ESS 배터리가 공개됐다. 동일 전시에서 EIS 기반 예방·진단 시스템을 컨테이너형 ESS DC 블록에 적용한 구조도 소개됐다. ([ASK Inno][7])

```yaml
entity: PROD-SKON-ESS-001
chemistry: LFP
form_factor: POUCH
commercial_status: CONTRACTED_OR_PRODUCTION_PLANNED
detailed_cell_capacity: NOT_DISCLOSED
cycle_life: NOT_DISCLOSED
warranty_terms: NOT_DISCLOSED
```

---

### 11.3.2 GRIDON Gen 1

GRIDON은 셀·모듈·랙·컨테이너와 BMS, 열관리 및 화재대응을 통합한 SK온의 ESS 솔루션 브랜드다. 회사는 GRIDON의 가치제안을 안전성, 경제성, 운전효율 및 고객 맞춤형 구조로 설명한다. ([ASK Inno][2])

GRIDON의 주요 기술은 다음과 같다.

```text
GRIDON
├─ LFP pouch cell
├─ ESS module and rack
├─ Containerized DC block
├─ EIS-based BMS
├─ Predictive diagnostics
├─ Coolant immersion
├─ Dual-valve structure
└─ Fire-response architecture
```

EIS 기반 BMS는 소형 교류 신호를 이용해 배터리 내부 임피던스 성분을 분석하는 비파괴 진단기술이다. SK온은 이 기술을 ESS의 실시간 상태진단과 고장 예측에 활용한다고 설명한다. ([ASK Inno][2])

---

### 11.3.3 GRIDON Gen 2

GRIDON Gen 2는 미국 ESS 시장의 고객 요구를 반영해 개발 중인 후속 제품이다. SK온은 2026년 중 미국에서 Gen 1 생산을 시작하고, Gen 2는 2027년 3분기 상업생산을 목표로 한다고 발표했다. ([ASK Inno][13])

Gen 2는 배터리 중심의 DC 블록과 PCS가 결합된 AC 블록을 모두 지원하도록 개발되고 있다. 이전 세대 대비 DC 컨테이너당 에너지용량을 평균 15% 높이고, EIS와 냉각수 기반 화재억제 기능을 적용할 계획이다. ([ASK Inno][13])

```yaml
entity: PROD-SKON-ESS-003
name: GRIDON Gen 2
status: UNDER_DEVELOPMENT
commercial_production_target: 2027_Q3
supports:
  - DC Block
  - AC Block
capacity_improvement_target: approximately_15_percent
absolute_container_capacity: NOT_DISCLOSED
```

---

### 11.3.4 ESS Competitive Position

GRIDON의 강점은 EIS 진단과 냉각수 기반 안전기술을 제품 차별화 요소로 명확히 제시했다는 점이다. 그러나 검토된 공식자료에서는 컨테이너당 절대 MWh, 왕복효율, 보증기간, 수명주기, 가동률 및 장기 운영실적이 공개되지 않았다.

CATL TENER는 20피트 컨테이너에 6.25MWh를 저장하고 LFP 셀 기준 430Wh/L를 구현한다는 사양을 공개했다. CATL은 초기 5년간 용량·출력 열화가 없다는 제조사 주장과 AI 기반 위험감시 체계도 제시한다. ([CATL][14])

삼성SDI SBB 1.7은 동일한 20피트 컨테이너에 6.14MWh를 저장하며, 기존 SBB 1.5 대비 에너지밀도가 약 17% 높다고 발표됐다. SBB 1.7과 LFP 기반 SBB 2.0에는 화재 발생 모듈에 소화약제를 직접 주입하는 EDI와 AI 예지정비·수명예측 기술이 적용된다. ([삼성SDI][15])

```text
GRIDON differentiation
├─ EIS diagnosis
├─ Coolant immersion
├─ Flexible DC/AC architecture
└─ U.S. localized production

GRIDON evidence gaps
├─ Absolute MWh/container
├─ RTE
├─ Cycle life
├─ Warranty conditions
├─ Availability
├─ Operating references
└─ PCS/EMS partner disclosure
```

---
