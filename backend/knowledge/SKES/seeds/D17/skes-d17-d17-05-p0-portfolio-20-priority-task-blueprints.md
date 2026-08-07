---
id: skes-d17-d17-05-p0-portfolio-20-priority-task-blueprints
title: P0 Portfolio — 20 Priority Task Blueprints
summary: "SK이노베이션 E&S의 우선 과제 20개를 가버넌스·운영·성장·위험 관리 4개 Wave로 구분하여, 가설·범위·담당자·KPI를 담은 실행 블루프린트."
tags: [d17, oi-portfolio, oi-seed, table, "xref:d11", "xref:d16"]
keywords: [과제 우선순위, Wave 기반 실행, 가버넌스, LNG/전력/가스 운영, 신사업 검증, 포트폴리오 관리, KPI 설정, 스톱게이트, 위험 관리, 가설 검증]
related: []
priority: normal
domain: D17
section: D17-05
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 2336
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-05 P0 Portfolio — 20 Priority Task Blueprints

## 1. 실행 순서

| Wave | 과제 | 목적 |
|---|---|---|
| `W0 Governance` | 001·002·003 | Problem·Evidence·Finance·Stop Gate를 먼저 강제 |
| `W1 Core Operations` | 006·007·008·011·012·013·016 | LNG–Power–City Gas의 반복 현금·가동·안전 기반 |
| `W2 Growth & New Operations` | 021·026·027·028·036·037 | Offshore/BESS/LH2의 성장과 신규 운영위험을 검증 |
| `W3 Strategic Risk` | 041·046·047·057 | CCS·탄소·Tax·OT의 tail-risk와 market access 통제 |

## 2. P0 Blueprint — W0 Governance

| ID | Hypothesis | 최소 Scope | Owner 조합 | External Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 001 | Seed–Pain–Owner–Data–Provider–Gate를 Graph로 연결하면 중복 Scout와 무주인 과제를 줄일 수 있다. | D11~D16 상위 50 Seed | O/I·전략·Data·Domain Owner | KG·Workflow·Portfolio analytics | Duplicate↓·Owner coverage↑ / 자동예산배정 금지 | G0 |
| 002 | Claim의 주체·날짜·단계·원문을 versioning하면 MOU/Marketing을 운영실적으로 오인하는 오류를 줄일 수 있다. | 외부 Claim 50개 | O/I·법무·전략·Research | Evidence AI·Source monitoring | stale↓·stage precision↑ / 원문 없는 Claim 승격 금지 | G0 |
| 003 | Baseline·Counterfactual·Finance 검증·Stop/Scale을 Gate로 강제하면 Zombie PoC와 과장 ROI를 줄일 수 있다. | PoC 5개 | O/I·FP&A·Domain·법무/SHE/CISO | workflow·benefit ledger | verified KRW·overlap=0 / Vendor 자체 ROI 금지 | G0 |

## 3. P0 Blueprint — LNG / Power / City Gas

| ID | Hypothesis | 최소 Scope | Owner 조합 | External Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 006 | Cargo·Tank·Terminal·Power 제약을 함께 최적화하면 공급충격에서 개별 최적화보다 재고/긴급조달/마진 의사결정이 개선된다. | 과거 Shock period 한 Slice replay | LNG Supply·Terminal·Power Trading·Finance | industrial twin·OR·market data | demurrage·stockout·replacement cost·margin / 계약권리 밖 배분 금지 | G0 |
| 007 | Cargo별 계약공식·Freight·Tolling·BOG·FX·Right를 실제 정산과 대사하면 구매가격 중심 판단의 누락비용을 줄일 수 있다. | 10~20 Cargo | LNG·SCM·Trading·Finance·Legal | contract analytics·cost twin | 95%+ reconciliation 목표는 내부 확인 후 확정 / 권리 추정 금지 | G0 |
| 008 | Tank/BOG/send-out와 전력사용을 한 모델로 보면 안전범위 내 에너지·BOG 원인을 더 정확히 분해할 수 있다. | Terminal 한 운영구간 Shadow | Terminal Ops·Process·Energy·SHE | process twin·time-series analytics | kWh/GJ·BOG attribution·constraint violations / SIS 독립 | G1 |
| 011 | Ambient/load/start mode를 정상화한 Heat-rate residual을 가격·연료·탄소와 연결하면 가장 가치있는 효율 Gap을 찾을 수 있다. | CCGT Unit 1개 | Plant·Performance·Trading·Finance·Environment | performance analytics·digital twin | corrected heat rate·KRW/MWh·carbon intensity / setpoint 자동변경 금지 | G0 |
| 012 | Historian signal과 Alarm/Trip/CMMS 작업을 asset ID로 묶으면 고장 precursor를 경제손실과 연결해 정비 우선순위를 개선할 수 있다. | GT Family 1개 | Plant·Maintenance·OEM·Data·SHE | APM·time-series AI | warning lead·precision·lost margin / shutdown 자동결정 금지 | G1 |
| 013 | CHP는 전력과 열을 공동 최적화해야 total margin이 개선된다. | CHP 1곳·동절기/하절기 한 주기 | CHP Ops·Heat sales·Trading·Finance | optimization·forecast | joint margin·fuel/GJ·heat SLA / 열공급 의무 hard constraint | G0 |
| 016 | GIS·배관·정압기·검사·누출·굴착을 canonical network로 만들면 RBMS의 설명가능성과 점검 생산성을 높일 수 있다. | 도시가스 자회사 1곳 | Gas Safety·GIS·Integrity·Field·Data | graph·geospatial analytics | ID coverage·risk recall·inspection yield / 법정점검 대체 금지 | G0 |

## 4. P0 Blueprint — Offshore / BESS / Hydrogen

| ID | Hypothesis | 최소 Scope | Owner 조합 | External Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 021 | 상태·Metocean·Marine access·부품·Cable risk를 함께 보면 긴 MTTR의 tail을 줄이는 정비 시점을 더 잘 선택할 수 있다. | 허용된 OWF subsystem | Offshore O&M·Marine·SHE·Finance | multi-OEM APM·weather routing | downtime·vessel day·warning lead / 해상안전 우선 | G1 |
| 026 | Bid에 SOH·Efficiency·Warranty throughput·Cycle cost를 내재화하면 단기 gross revenue가 아니라 lifecycle net margin을 개선할 수 있다. | KCE 1 asset replay→shadow | KCE Market·Asset Mgmt·OEM·Finance | bid optimization·battery analytics | lifecycle net margin·SOH·violation=0 / live bid human approval | G1 |
| 027 | BMS/PCS/EMS·온도·가스/연기·alarm·정비를 fusion하면 safety precursor의 lead time을 늘릴 수 있다. | BESS Site 1곳 read-only | KCE Ops·Fire/SHE·OEM·CISO | anomaly fusion·BESS safety analytics | critical recall·false alarm·lead / 보호계전·BMS 보호로직 우회 금지 | G1 |
| 028 | 동일 데이터·제약에서 실제 Bid와 Counterfactual을 replay하면 MarketCapture/optimizer alpha와 settlement leakage를 분리검증할 수 있다. | 시장 1곳·1~2 asset | KCE Market·Finance·Risk·Data | counterfactual lab·MLOps | risk-adjusted uplift·settlement accuracy / hindsight leakage 금지 | G0 |
| 036 | proof-test·bypass·alarm·maintenance를 barrier object로 관리하면 액화수소의 latent impairment를 조기 가시화할 수 있다. | 선정 Barrier read-only | H2 Plant·SHE·Maintenance·OEM | barrier management·sensor analytics | impairment hours·overdue test·miss=0 / SIS 의존성 생성 금지 | G1 |
| 037 | 생산–저장–출하–배송–판매–수금 계량을 한 질량수지로 대사하면 BOG/계량오차/재고와 실제 kg 경제성을 분리할 수 있다. | Plant→Station Route 1개 | H2 Ops·Logistics·Sales·Finance·Metrology | cryogenic metering·mass-balance twin | unexplained kg·paid/produced·KRW/paid-kg / 계량불확도 표시 | G0 |

## 5. P0 Blueprint — CCS / Policy / OT

| ID | Hypothesis | 최소 Scope | Owner 조합 | External Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 041 | Storage risk와 측정목적을 연결한 risk-based MMV가 sensor 나열식 설계보다 규제증빙·비용의 추적성을 높인다. | CCS concept 1개 | CCS Tech·MRV·Legal·Partner | subsurface modeling·digital MMV | risk coverage·evidence completeness / Regulator requirement 누락=NO-GO | G0 |
| 046 | K-ETS 할당·배출·발전량·heat rate·dispatch를 한 Position으로 보면 탄소비용이 실제 발전의사결정에 반영된다. | 발전자산 1~2개 | Environment·Power Trading·Plant·Finance | carbon analytics·scenario engine | position forecast·KRW/MWh / 할당·가격 추정 Version 표시 | G0 |
| 047 | KCE BOM·Supplier ownership·Project basis·PIS를 evidence graph로 묶으면 48E/PFE 검토의 누락과 사후 tax risk를 줄일 수 있다. | US BESS Project 1개 | KCE Tax·Procurement·Legal·Finance | supplier KG·TaxTech·document AI | evidence completeness·exception age / 최종 Tax 판정은 Human | G1 |
| 057 | OT cyber alert를 asset criticality·Safety barrier·운전상태와 연계하면 단순 CVSS보다 incident triage를 개선할 수 있다. | 격리 Site 1곳 | CISO·OT·SHE·Operations | passive OT security·risk correlation | critical triage lead·false escalation·RTO / active scan 금지 | G1 |

---
