---
id: skon-d03-d03-rp-005-경쟁제품-source-library-등록
title: 005. 경쟁제품 Source Library 등록
summary: "경쟁사 CATL의 EV배터리 및 에너지저장 제품의 공식 성능사양, 기술특성, 안전기술을 추적하는 정보소스"
tags: [d03, product, schema]
keywords: [CATL, Shenxing, TENER, LFP 배터리, 4C 충전, 에너지저장장치, 에너지밀도, CTP, 배터리 벤치마킹, 제품 데이터베이스, EV배터리, 에너지저장시스템, 급속충전, LFP, 주행거리, 열안전, 경쟁분석]
related: []
priority: normal
domain: D03
section: D03-RP
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 3603
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# SK온 D03 Products & Solutions

## Part 4. Competitive Product Mapping

**문서 버전:** D03 v1.3
**기준일:** 2026-07-30
**이전 완료 지점:** `D03-06 Customer Mapping`

---

# D03-RP-005. 경쟁제품 Source Library 등록

## SRC-SKON-D03-037 — CATL Shenxing PLUS

```yaml
source_id: SRC-SKON-D03-037
title: CATL Unveils Shenxing PLUS, Enabling 1,000-km Range and 4C Superfast Charging
publisher: CATL
source_type: Official Product Release
publication_date: 2024-04-25
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - Shenxing PLUS
  - LFP EV Battery
  - CTP 3.0
  - 4C Fast Charging
```

CATL은 Shenxing PLUS를 LFP 기반 4C 급속충전 제품으로 공개했다. 공식 발표 기준 시스템 에너지밀도는 205Wh/kg이며, CTP 3.0 기반 모듈리스 구조로 패킹 효율을 높였다. 1,000km 주행거리와 10분 충전 시 600km라는 수치는 차량·시험조건이 결합된 제조사 발표값이므로 셀 단독 성능으로 사용하지 않는다. ([CATL][1])

---

## SRC-SKON-D03-038 — CATL 2세대 Shenxing

```yaml
source_id: SRC-SKON-D03-038
title: Naxtra Battery Breakthrough & Dual-Power Architecture
publisher: CATL
source_type: Official Product Release
publication_date: 2025-04-21
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - Second-Generation Shenxing
  - 12C Peak Charging
  - LFP Battery
  - Low-Temperature Fast Charging
```

CATL의 2세대 Shenxing은 공식 발표상 LFP 화학계에서 800km 주행거리, 12C 피크 충전율, 최대 1.3MW 충전전력을 목표로 한다. 영하 10℃ 환경에서 5%에서 80%까지 15분 충전 성능도 제시됐다. 다만 피크 C-rate와 차량 충전시간은 지속충전율, 차량 전압, 열관리 조건과 구분해야 한다. ([CATL][2])

---

## SRC-SKON-D03-039 — CATL Shenxing Pro

```yaml
source_id: SRC-SKON-D03-039
title: CATL Launches Shenxing Pro
publisher: CATL
source_type: Official Product Release
publication_date: 2025-09-07
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - Shenxing Pro Long-Life Variant
  - Shenxing Pro Fast-Charging Variant
  - NP 3.0 Safety Technology
  - European EV Market
```

Shenxing Pro는 장수명·장거리형과 급속충전형으로 구분된다. CATL은 장수명형에 대해 12년·100만km, 급속충전형에 대해 10분 충전 시 WLTP 기준 478km를 제시하며, 열폭주 이후에도 화염과 연기 발생을 억제하는 NP 3.0 안전기술을 강조한다. 모두 CATL의 공식 제품 주장으로 저장하되 독립 시험 결과와는 구분한다. ([CATL][3])

---

## SRC-SKON-D03-040 — CATL TENER

```yaml
source_id: SRC-SKON-D03-040
title: CATL Unveils TENER
publisher: CATL
source_type: Official ESS Product Release
publication_date: 2024-04-09
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - TENER
  - LFP ESS Cell
  - 6.25MWh Container
  - Five-Year Zero Degradation Claim
  - AI Risk Monitoring
```

TENER는 20피트 컨테이너에 6.25MWh를 수용하고, LFP ESS 셀 기준 430Wh/L를 제시한 CATL의 ESS 솔루션이다. CATL은 초기 5년간 용량과 출력의 열화가 없다는 제품 주장을 제시하며, 운전 이후 AI 기반 위험 모니터링과 조기경보도 운영체계에 포함한다. ([CATL][4])

---

## SRC-SKON-D03-041 — CATL TENER Stack

```yaml
source_id: SRC-SKON-D03-041
title: CATL Launches 9MWh TENER Stack
publisher: CATL
source_type: Official ESS Product Release
publication_date: 2025-05-07
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - TENER Stack
  - 9MWh ESS Solution
  - Transportable ESS Architecture
```

CATL은 2025년 9MWh급 TENER Stack을 양산형 초대용량 ESS 솔루션으로 공개했다. 이는 컨테이너 단위 고집적화와 현장 설치 효율이 ESS 경쟁의 핵심 축으로 이동하고 있음을 보여주는 벤치마크다. ([CATL][5])

---

## SRC-SKON-D03-042 — BYD Blade Battery

```yaml
source_id: SRC-SKON-D03-042
title: A Glimpse into BYD's Blade Battery Factory in Chongqing
publisher: BYD
source_type: Official Product and Manufacturing Article
publication_date: 2020-06-04
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - Blade Battery
  - LFP Cell
  - Cell-to-Pack Architecture
  - Nail Penetration Test
```

BYD Blade Battery는 길고 얇은 LFP 셀을 팩의 구조요소로 활용하는 제품이다. BYD는 기존 팩 대비 공간 활용률을 50% 이상 높였다고 설명하며, 10%에서 80%까지 33분 충전, 3,000회 충·방전 후 누적 120만km 가능성을 발표했다. 이는 2020년 제품 기준 제조사 수치로 최신 세대와 직접 동일시하지 않는다. ([BYD Global][6])

---

## SRC-SKON-D03-043 — LG에너지솔루션 제품 로드맵

```yaml
source_id: SRC-SKON-D03-043
title: LG Energy Solution's Battery Technology Roadmap
publisher: LG Energy Solution
source_type: Official Technology Article
publication_date: 2025-06-20
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - High-Nickel Premium Battery
  - High-Voltage Mid-Nickel Battery
  - LFP Affordable Battery
  - Dry Electrode Process
  - Silicon Anode
```

LG에너지솔루션은 EV 제품군을 Premium·Standard·Affordable로 구분한다. 프리미엄에는 하이니켈과 실리콘 음극, 표준형에는 니켈 60~70% 수준의 고전압 미드니켈, 보급형에는 LFP와 건식전극 공정을 연결한다. 이 구조는 고객 가격대별 제품 포트폴리오를 명확히 구분하는 경쟁사 사례다. ([BATTERY INSIDE][7])

---

## SRC-SKON-D03-044 — LG에너지솔루션 LFP 파우치 공급

```yaml
source_id: SRC-SKON-D03-044
title: LG Energy Solution to Supply LFP EV Batteries to Ampere
publisher: LG Corporation / LG Energy Solution
source_type: Official Press Release
publication_date: 2024-07-02
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - LFP Pouch Battery
  - Cell-to-Pack
  - Ampere
  - Renault Group
```

LG에너지솔루션은 르노그룹 전기차 계열사 Ampere에 2025년 말부터 2030년까지 약 39GWh의 파우치형 LFP 배터리를 공급하는 계약을 체결했다. 약 59만 대의 전기차 생산에 해당한다고 회사는 설명했다. 이는 한국 배터리 기업의 EV용 파우치 LFP가 계약단계까지 진입한 직접 비교사례다. ([LG][8])

---

## SRC-SKON-D03-045 — LG에너지솔루션 46시리즈

```yaml
source_id: SRC-SKON-D03-045
title: LG Energy Solution 46-Series Product Lineup
publisher: LG Energy Solution
source_type: Official Product and IR Disclosure
publication_date:
  - 2025
  - 2026
access_date: 2026-07-30
language:
  - Korean
  - English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - 4680
  - 4695
  - 46120
  - Cylindrical EV Battery
```

LG에너지솔루션은 4680·4695·46120으로 구성된 46시리즈 원통형 제품군을 공개했다. 2026년 1분기 기준 회사는 46시리즈 신규 수주를 100GWh 이상 추가해 수주잔고가 440GWh를 넘었다고 발표했으며, 오창에서 4695 양산을 시작하고 미국 애리조나에서 복수 규격 양산을 준비했다. ([LG엔솔 뉴스][9])

---

## SRC-SKON-D03-046 — 삼성SDI PRiMX680-EV

```yaml
source_id: SRC-SKON-D03-046
title: Samsung SDI Wins Four CES 2025 Innovation Awards
publisher: Samsung SDI
source_type: Official Product Release
publication_date: 2024-11-15
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - PRiMX680-EV
  - PRiMX680 Module+
  - High-Nickel NCA
  - Prismatic Cell
```

PRiMX680-EV는 하이니켈 NCA 양극을 사용하는 각형 EV 배터리다. PRiMX680 Module+는 무선 통신을 적용해 모듈 구조를 단순화하고 생산 효율과 품질을 높이는 방향이며, CT 검사와 독자 모듈설계가 안전기술로 제시된다. ([삼성SDI][10])

---

## SRC-SKON-D03-047 — 삼성SDI SBB

```yaml
source_id: SRC-SKON-D03-047
title: Samsung SDI Debuts SBB 1.7 and SBB 2.0
publisher: Samsung SDI
source_type: Official ESS Product Release
publication_date: 2025-09-09
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - SBB 1.7
  - SBB 2.0
  - NCA ESS
  - LFP ESS
  - EDI Fire Suppression
  - AI Predictive Maintenance
```

SBB 1.7은 하이니켈 NCA 셀을 적용한 6.14MWh급 20피트 컨테이너 제품이며, SBB 1.5보다 에너지밀도가 약 17% 높다. SBB 2.0은 삼성SDI 최초의 각형 LFP 기반 SBB로 공개됐다. 두 제품 모두 EDI 화재억제와 AI 기반 예지정비·내구수명 예측을 포함한다. ([삼성SDI][11])

---

## SRC-SKON-D03-048 — Panasonic 2170

```yaml
source_id: SRC-SKON-D03-048
title: Panasonic Energy Begins Mass Production at Kansas Factory
publisher: Panasonic Energy
source_type: Official Press Release
publication_date: 2025-07-14
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - 2170 Cylindrical Cell
  - Kansas Factory
  - North American EV Battery Production
```

Panasonic Energy는 미국 캔자스 공장에서 2170 원통형 셀 양산을 시작했다. 향후 목표 생산능력은 약 32GWh이며, 기존 네바다 공장과 합치면 미국 내 약 73GWh의 생산능력을 목표로 한다. 회사는 캔자스 라인의 생산성을 네바다보다 약 20% 높이고, 향후 셀 용량을 약 5% 높이는 소재를 도입할 계획이라고 밝혔다. ([파나소닉 에너지][12])

---

## SRC-SKON-D03-049 — Tesla 4680 및 건식전극

```yaml
source_id: SRC-SKON-D03-049
title: Tesla 2025 Q4 Update
publisher: Tesla
source_type: Official IR Material
publication_date: 2026-01-28
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: PDF_OPEN_CONFIRMED

covered_entities:
  - 4680 Cell
  - Dry Electrode
  - Model Y Battery Pack
  - In-House Cathode
```

Tesla는 일부 Model Y용 배터리팩에 자체 4680 셀을 사용하기 시작했으며, 미국 오스틴에서 음극과 양극 모두 건식전극 방식으로 생산한다고 밝혔다. 이는 건식공정이 시험단계를 넘어 실제 차량용 생산에 적용되고 있다는 경쟁 벤치마크다. ([Tesla][13])

---

## SRC-SKON-D03-050 — Tesla Megapack

```yaml
source_id: SRC-SKON-D03-050
title: Tesla Megapack
publisher: Tesla
source_type: Official Product Page
publication_date: null
access_date: 2026-07-30
language: English
reliability_grade: A+
accessibility_status: OPEN_CONFIRMED

covered_entities:
  - Megapack
  - Utility-Scale ESS
  - Integrated Energy Storage Product
```

Tesla는 Megapack을 전력망 안정화와 정전 방지를 위한 대규모 전력저장 제품으로 정의한다. 배터리 하드웨어와 전력변환·제어·운영 소프트웨어를 결합하는 통합형 사업모델이라는 점에서 GRIDON의 시스템·서비스 확장 방향과 비교할 가치가 있다. ([Tesla][14])

---
