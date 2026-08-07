---
id: skon-d17-d17-05-p0-portfolio-20-priority-task-blueprints
title: P0 Portfolio — 20 Priority Task Blueprints
summary: 배터리 제조업의 governance부터 decision twin까지 4단계 Wave로 추진할 P0 우선과제 20개의 가설·최소scope·KPI·guardrail을 정의한 PoC 블루프린트 설계서.
tags: [d17, oi-portfolio, oi-seed, table, "xref:d11", "xref:d16"]
keywords: [Wave단계, PoC설계, 가설검증, 거버넌스, 데이터기반, 가치검증, 의사결정, KPI, 실행순서, 우선순위과제, PoC 설계, Wave 실행순서, Governance, Canonical Link, Genealogy, Causal AI, Decision Twin, Guardrail, 배터리 제조]
related: []
priority: normal
domain: D17
section: D17-05
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 1905
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-05 P0 Portfolio — 20 Priority Task Blueprints

### 1. P0 목록과 실행 순서

| Wave | 과제 | 이유 |
|---|---|---|
| `W0 Governance` | 001·002·003·004 | 과제·근거·비교·중단 통제 구축 |
| `W1 Data Foundation` | 006·011·016·031·046 | 제조·Capacity·Field·공급망·계약의 Canonical Link 확보 |
| `W2 Value Proof` | 007·008·009·021·036 | 수율·Flow·검사·원가·정책현금을 실제 분모로 검증 |
| `W3 Decision Twin` | 010·012·013·017·018·041 | 공장전환·리콜범위·필드신호·투자결정을 Closed Loop로 연결 |

### 2. P0 PoC 설계 — W0/W1

| ID | Hypothesis | 최소 Scope | Owner 조합 | Partner Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 001 | Seed–Capability–Provider를 한 Graph로 연결하면 중복 Scout와 무주인 과제를 줄일 수 있다. | D11~D16 P0/P1 | O/I·전략·Data Architecture·Domain Owner | Knowledge Graph·Workflow | Coverage·Duplicate / 승인 없는 자동추천 금지 | G0 |
| 002 | Claim의 단계·날짜·주체를 추적하면 MOU를 상용성과로 오인하는 오류를 줄일 수 있다. | 기존 협력 10개 | O/I·구매·법무·재무 | Evidence AI·Research Workflow | Stage Precision / 원문 Link 필수 | G0 |
| 003 | Baseline·Stop·Scale·PIR을 Gate로 강제하면 Zombie PoC를 줄일 수 있다. | PoC 5개 | O/I·재무·구매·Domain Owner | Decision Workflow·Process Mining | Gate Cycle·Validated Value / 편익 이중계상 금지 | G0 |
| 004 | 동일 Data·KPI·보안조건에서 Vendor를 비교하면 성능과 Lock-in을 공정하게 판단할 수 있다. | 후보 2~3개 | IT·Data·Cyber·법무·품질 | Clean Room·MLOps | Comparable Test·Leakage 0 / 생산 Write 금지 | G1 |
| 006 | Lot–Roll–Cell Genealogy가 완성되면 국부 Scrap과 원인추적 범위를 줄일 수 있다. | 한 공정·한 Cell Rev | 제조·품질·MES·Data | Industrial Data Fabric·Graph | Coverage·Query Time / 원본 Timestamp 보존 | G0 |
| 011 | 명목 Capacity를 승인단계별로 나누면 실제 공급가능량과 병목을 정확히 볼 수 있다. | 한 고객–한 Line | S&OP·영업·제조·품질 | PLM·Graph·Planning | Qualified GWh / JV Gross 합산 금지 | G0 |
| 016 | 제조 Genealogy와 Field Signal을 연결하면 Return 진단과 CAPA를 앞당길 수 있다. | 한 Failure Family | 품질·제조·BMS·Warranty | Quality Data Fabric·Causal AI | Diagnosis Time / Recall 자동판정 금지 | G1 |
| 031 | Supplier Lot부터 Battery까지 연결하면 규제증빙과 영향범위를 같은 Lineage에서 재현할 수 있다. | 한 핵심소재 | 구매·품질·SCM·Compliance | Traceability·Graph | Coverage·Query Time / 미확인 Origin 추정 금지 | G0 |
| 046 | Clause–Obligation–Entity–Asset를 연결하면 누락의무와 경제적 Exposure를 줄일 수 있다. | 한 JV 계약군 | 법무·JV·재무·사업 | CLM·Knowledge Graph | Coverage·Missed Duty / AI 법률판정 금지 | G1 |

### 3. P0 PoC 설계 — W2/W3

| ID | Hypothesis | 최소 Scope | Owner 조합 | Partner Capability | KPI / Guardrail | 첫 Gate |
|---|---|---|---|---|---|---|
| 007 | 공정원인을 원화·accepted-kWh 손실로 연결하면 수율개선 우선순위가 달라진다. | 한 Defect Family | 제조·품질·원가·Data | Causal AI·Process Analytics | FPY·Recovered Margin / 상관관계의 인과 단정 금지 | G2 |
| 008 | Formation·Aging의 Cell 상태와 Queue를 함께 최적화하면 품질을 해치지 않고 WIP·에너지를 줄일 수 있다. | 한 Tray/Rack 구간 | 제조·품질·Energy·생산관리 | OR·Battery Analytics | Lead time·Energy / 품질 Release 자동화 금지 | G2 |
| 009 | Ground Truth Cell Library로 NDI를 비교하면 False Reject와 Miss를 동시에 줄일 수 있다. | Defect 2~3종 | 품질·설비·Metrology | NDT·Vision·Lab Consortium | Recall·False Reject·Takt / Vendor 단독 Label 금지 | G1 |
| 010 | 설비·소재·측정 Bias를 정규화하면 검증 Recipe의 공장 간 Transfer 기간을 줄일 수 있다. | Source/Target 각 한 Line | 제조기술·품질·공장운영 | Transfer Learning·Metrology | Transfer Time·Cpk / 숫자 Setpoint 복사 금지 | G1 |
| 012 | 시장·고객·화학계 수요를 Qualified Capacity와 연결하면 증설·전환 결정을 개선할 수 있다. | 한 지역·Segment | 전략·S&OP·영업·재무 | Market Data·Optimization | Gap·Forecast Calibration / Forecast와 Actual 분리 | G0 |
| 013 | EV↔ESS 전환을 Real Option으로 평가하면 성급한 증설 또는 유휴를 줄일 수 있다. | 한 Brownfield Line | 전략·제조·재무·영업 | Industrial Twin·TEA·OR | NPV·Lead time / 고객승인 미확정은 0 Capacity | G0 |
| 017 | Genealogy와 증거를 이용한 Population 경계설정은 과대·과소 Recall 위험을 줄인다. | 한 Failure Mode | 품질·안전·법무·보험 | Reliability AI·Graph | Precision/Recall·Unknown Tail / Human Recall 승인 | G2 |
| 018 | DTC·Telemetry·Complaint·Warranty를 결합하면 이상신호를 더 일찍 찾을 수 있다. | 한 Program | Field Quality·BMS·OEM | Anomaly AI·Connected Data | Lead time·False Alarm / OEM Data 권리 필수 | G1 |
| 021 | 실제 고객 인수량을 분모로 쓰면 Line·Program 경제성을 일관되게 비교할 수 있다. | 한 Program·월 | 원가·재무·제조·영업 | Industrial Cost Twin | Cost/accepted-kWh / 내부단가 외부반출 금지 | G0 |
| 036 | PFE/MACR와 45X 증빙을 Lot·BOM·법인·판매량에 연결하면 적격금액과 Audit Gap을 재현할 수 있다. | 미국 한 Product/기간 | 세무·통상·구매·제조·법무 | RegTech·TaxTech·Graph | Eligibility Coverage·Exceptions / Human 세무·법률 승인 | G1 |
| 041 | 수요·승인·정책 Trigger별 Option을 비교하면 회수불가능 CAPEX를 줄일 수 있다. | 한 Project Option | 투자·재무·S&OP·법무 | Real Options·Scenario Analytics | Avoided CAPEX·NPV / 승인 가정 Version 보존 | G0 |

---
