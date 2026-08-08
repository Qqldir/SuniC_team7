---
id: skon-d16-d16-04-external-solution-provider-master
title: External Solution Provider Master
summary: "배터리 제조, 품질, R&D 및 필드 운영에 적용 가능한 외부 솔루션 제공업체의 역량과 적용 가설, 검증 갭을 평가한 공급자 비교표."
tags: [d16, ecosystem, table, "xref:d06", "xref:d14"]
keywords: [제조데이터, 배터리기술, 품질관리, 벤더평가, ESS운영, Digital Twin, Battery Analytics, 데이터통합, MES, 배터리 제조, 품질 데이터, ESS 운영, PLM, 솔루션 평가, 필드 인텔리전스, Telemetry, OT/IT 통합]
related: []
priority: normal
domain: D16
section: D16-04
source: SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md
breadcrumb: "SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem"
tokens: 3116
updated: 2026-08-03
---

> SK온 · D16 외부 솔루션·스타트업·벤더 생태계 · SK온 D16 — External Solutions, Startups, Vendors & Open-Innovation Ecosystem

## D16-04 External Solution Provider Master

### 1. 제조·품질·R&D Data

| Provider | Capability | 공개 Reference | Evidence | SK온 적용 가설 | 주요 검증 Gap |
|---|---|---|---:|---|---|
| Palantir | Foundry 기반 제조 Data Ontology·운영 Workflow | Panasonic Energy Nevada Smart Factory; Sensor·IT/OT 통합과 Waste·Uptime Use Case | E3 | 1개 공장의 Material–Process–Quality–Cost Graph | Data Lock-in·Cloud/Edge·Model/IP·총소유비용 ([Panasonic](https://na.panasonic.com/news/palantir-and-panasonic-energy-of-north-america-sign-multi-year-agreement)) |
| Siemens | PLM·MES·Automation·Digital Twin·Edge | SK온 MOU, ACC·FREYR Battery Factory 협력 | E2 | 기존 접점을 D06·D07의 Virtual Commissioning·Line Twin으로 확장 | 기존 Stack 중복·구현상태·License·Integrator 책임 ([Siemens–FREYR](https://press.siemens.com/global/en/pressrelease/freyr-scale-battery-cell-gigafactory-production-siemens-xcelerator)) |
| Voltaiq | Battery Test·Manufacturing Quality Data Layer | AWS Marketplace·Siemens 협력, Battery Ramp Analytics | E2 | Formation·Aging·EoL과 전극공정 Data를 Cell 단위로 연결 | named production outcome·대규모 ingestion·Label portability ([Voltaiq–AWS](https://www.voltaiq.com/resources/aws-partnership)) |
| Liminal Insights / Waygate | Inline Ultrasound + Radiography/CT Multi-modal Inspection | 양사 전략적 Battery Inspection 협력 | E2 | Pouch/Prismatic Cell 내부결함을 파괴검사보다 이르게 분류 | Line speed·False reject·Form factor·Defect ground truth ([Waygate](https://www.bakerhughes.com/waygate-technologies/news/waygate-technologies-and-liminal-insights-announce-strategic-partnership)) |
| Sight Machine | 제조 Data Model·Industrial AI·Factory Copilot | Siemens Industrial Edge와 On-premise 협력 | E2 | 기존 PLC/MES 위에 Cross-line Bottleneck·Yield 분석 | Battery-specific reference·Edge resource·Model governance ([Sight Machine](https://www.sightmachine.com/news-siemens-industrial-edge)) |
| Monolith AI | Test Data 기반 Surrogate Model·Fault Isolation·DoE | Webasto Battery Fault Isolation 사례, BMW Engineering 사례 | E3 | Cell/Module Test의 반복실험 감소와 실패원인 후보 정렬 | Extrapolation·물리 제약·Safety sign-off·재현성 ([Monolith](https://www.monolithai.com/battery-testing)) |
| Hexagon | Battery Multi-physics·Metrology·Digital Reality | Fraunhofer ITWM Battery Cell Simulation 결합 | E2 | R&D Simulation–CT/Metrology–Manufacturing Change 연결 | 실제 SK온 Format·Solver validation·PLM 연동 ([Hexagon](https://hexagon.com/company/newsroom/press-releases/2024/hexagon-and-fraunhofer-itwm-accelerate-new-battery-design-with-electrochemical-simulation-solution)) |

### 2. Battery Field·ESS Intelligence

| Provider | Capability | 공개 Reference | Evidence | SK온 적용 가설 | 주요 검증 Gap |
|---|---|---|---:|---|---|
| TWAICE | EV·Fleet·BESS Health·Safety·Simulation | Automotive·ESS 운영용 Battery Analytics; Quick Check는 2025-02-28 종료 | E2 | OEM 승인 Telemetry의 SOH·이상·Warranty Signal 보조 | 종료 Product와 현행 Core 분리·차종별 Calibration·Data right ([TWAICE](https://www.twaice.com/newsroom/battery-quick-check-market-launch-successfully-completed)) |
| ACCURE | BESS Safety·SOC·Performance Predictive Analytics | UBS AM의 Texas 4개 Project 730MW 배포, Repsol 20MW 사례 | E4 | GRIDON 및 외부 Cell 혼합 ESS의 독립 Safety/Performance Layer | Cell maker 간 책임·Alarm action·보험/보증 데이터권리 ([ACCURE](https://www.accure.net/news/accure-battery-intelligence-predictive-analytics-tech-to-increase-battery-safety-and-performance-of-energy-storage-projects)) |

### 3. Traceability·DPP·LCA·Supply-chain Compliance

| Provider | Capability | 공개 Reference | Evidence | SK온 적용 가설 | 주요 검증 Gap |
|---|---|---|---:|---|---|
| Circulor | 원재료 Traceability·Carbon·Battery Passport | Volvo EX90 양산차 개별 Battery Passport | E4 | EU Program 1개의 Mine–Material–Cell–Battery Passport | Upstream onboarding·Primary evidence·OEM/Cell maker 권한 ([Circulor](https://circulor.com/articles/worlds-first-battery-passport)) |
| Minespider | Battery Passport·Lifecycle Version·On-premise Option | TEMSA가 EUBR 대응용 구현 시작 | E3 | Hungary Program의 On-premise DPP와 Supplier 제출 Workflow | Catena-X 인증·현재 상호운용성·API·Role model ([Minespider](https://www.minespider.com/press/temsa-partners-with-minespider-to-be-the-first-e-bus-company-compliant-with-eu-battery-regulation)) |
| Circularise | Supplier Data Collection·Selective Disclosure·Passport/API | Honda Motor Europe 2027 Battery Passport 준비협력 | E2 | 영업비밀을 공개하지 않는 Supplier Data Exchange | Interoperability·검증자 역할·장기 Version 유지 ([Circularise](https://www.circularise.com/press-releases/honda-uses-circularise-to-strengthen-battery-passport-readiness-ahead-of-2027-eu-requirements/)) |
| Makersite | BOM Enrichment·LCA·Product Carbon Footprint | 복잡 제조업용 AI LCA/Product Sustainability Platform | E2 | 제품·공장별 kgCO2e/kWh 계산의 Secondary-data 보완 | Primary/Secondary 구분·배터리 PCR·Assurance ([Makersite](https://makersite.io/insights/all-you-need-to-do-about-the-new-eu-batteries-regulation/)) |
| Prewave | Multi-tier Risk Signal·Supplier Engagement·Due Diligence | Battery Regulation용 Product/Environmental Compliance Workflow | E2 | Supplier Risk와 시정조치·증빙을 Lot/Material에 연결 | 공급망 Mapping 정확도·False positive·한국/중국 언어 Coverage ([Prewave](https://www.prewave.com/solutions/product-environmental-compliance)) |
| Assent / IPOINT | Product Compliance·Material Declaration·LCA·DPP | 2026년 IPOINT 인수로 Automotive LCA·Product Stewardship 결합 | E2 | IMDS·화학물질·PFAS·DPP Data Foundation 통합 | 인수 후 Product 통합·중복 Data Model·Implementation scope ([Assent](https://www.assent.com/newsroom/assent-acquires-ipoint-uniting-ai-powered-compliance-and-product-intelligence/)) |
| Exiger | Entity Network·Forced-labor·Supply-chain Risk | Automotive·Critical Mineral/UFLPA Risk Platform | E2 | PFE/UFLPA Entity Graph와 Supplier Due Diligence 보조 | Material Lot traceability·판정설명·Tax/Legal approval ([Exiger](https://www.exiger.com/perspectives/automakers-forced-labor-concerns-path-affordable-electrified-future/)) |

### 4. OT·계약·CAPEX Decision Support

| Provider | Capability | 공개 Reference | Evidence | SK온 적용 가설 | 주요 검증 Gap |
|---|---|---|---:|---|---|
| Claroty | CPS Asset Discovery·Exposure·Remote Access·Risk Context | Battery Recycler Hydrovolt OT Cyber 사례 | E3 | 1개 Line의 Asset–Remote Access–Patch–Backup–Safety Map | Passive/Active scan 안전성·PLC Coverage·SOC 운영모델 ([Claroty](https://claroty.com/resources/case-studies/how-hydrovolt-powers-up-ot-cyber-resilience)) |
| Icertis | CLM·Clause/Obligation Intelligence·ERP 연결 | Mercedes-Benz 50만 Supplier 계약 중앙화, Turnaround 6주→1주 회사사례 | E4 | JV·Offtake·Supply·Incentive Clause를 실행 Evidence에 연결 | 한국/미국/EU 법률검토·Clause accuracy·Commercial data isolation ([Icertis](https://www.icertis.com/customers/customer-stories/mercedes-benz/)) |
| nPlan | Historical Schedule 기반 AI Schedule Risk | LNG Canada·Network Rail 등 대형 Project Reference | E3 | Gigafactory P6 일정의 지연 Driver·Risk Range 비교 | Battery-specific class·Schedule quality·원인/상관 구분 ([nPlan](https://www.nplan.io/case-studies/using-ai-led-forecasting-and-risk-management-to-reduce-delivery-risk-during-the-construction-of-lng-canada)) |
| ALICE Technologies | Generative Construction Schedule·Resource Optimization | 미국 Industrial Project 입찰·Data Center Recovery 사례 | E2 | 공장전환·증설의 대안 Schedule·Crew·장비 Scenario | Constraint completeness·EPC adoption·Baseline governance ([ALICE](https://blog.alicetechnologies.com/case-studies/how-alice-helped-win-an-industrial-project-bid-through-schedule-optimization)) |

### 5. Circularity·Recycling·Second-life

| Provider | Capability | 공개 Reference | Evidence | SK온 적용 가설 | 주요 검증 Gap |
|---|---|---|---:|---|---|
| Ascend Elements | Recycling·Hydro-to-Cathode pCAM·CAM | Honda 자원조달 협력; SK ecoplant·TES Kentucky JV | E3 | 미국 Scrap→Black Mass→재생소재 Qualification Closed Loop | Kentucky 실제가동·Yield·Spec·경제성·SK온 직접권리 ([Honda](https://global.honda/en/newsroom/news/2023/c230227aeng.html)) |
| Redwood Materials | 회수·진단·재활용·재생소재·Second-life ESS | Toyota Closed Loop·Material Supply | E3 | 미국 Cell Scrap/EOL과 ESS 전환 Option의 통합평가 | 경쟁관계·물량·Material spec·Offtake·Data ownership ([Redwood–Toyota](https://www.redwoodmaterials.com/news/toyota-redwood-cathode-anode/)) |
| Nth Cycle | Modular Electro-extraction·Black Mass Refining | Ohio Commercial-scale Nickel/Cobalt Scrap Refining 운영 발표 | E3 | 중앙대형정제소 외에 지역형 Scrap Refining Option | Feed variability·Li recovery·OPEX·Permit·품질보증 ([Nth Cycle](https://nthcycle.com/newsroom/nth-cycle-begins-operations-of-first-domestic-commercial-scale-nickel-an-cobalt-scrap-refining-system-in-fairfield-ohio)) |
| Princeton NuEnergy | 저온 Plasma 기반 Direct Cathode Recycling | Pilot·Scale-up·Honda 평가·NSF 지원 | E2 | High-Nickel Cathode Scrap의 구조 보존형 직접재생 | Chemistry별 impurity·cycle performance·throughput·Scale economics ([PNE](https://pnecycle.com/)) |

### 6. Master 해석

- `E3~E4`는 곧바로 구매할 기업이라는 의미가 아니라 **명명된 운영 Reference를 실사할 가치가 높다**는 뜻이다.
- `E2` 후보는 기술이 부족하다는 의미가 아니라, 공개자료만으로 생산확산·ROI를 확인할 수 없으므로 PoC Gate를 더 엄격히 둔다는 뜻이다.
- Siemens·Solid Power·Factorial처럼 이미 SK온 접점이 있는 기업은 신규 Scout보다 먼저 계약범위·성과·잔여 Option을 확인한다.
- Circulor·Minespider·Circularise는 한 업체를 즉시 선정하지 않고 동일한 D14 Mandatory Field·API·Access-control Test Pack으로 비교한다.
- TWAICE와 ACCURE, Redwood와 Ascend/Nth Cycle/PNE는 같은 범주 안에서도 사업모델이 다르므로 단순 점수합으로 대체하지 않는다.

---
