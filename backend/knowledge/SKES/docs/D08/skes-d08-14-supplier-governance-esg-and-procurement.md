---
id: skes-d08-14-supplier-governance-esg-and-procurement
title: "Supplier Governance, ESG and Procurement Workflow"
summary: "협력사 ESG 평가 기준과 Source-to-Pay 프로세스 각 단계의 필수 통제사항, 공급사 점수 산정 방법을 다루는 문서"
tags: [d08, supply-chain, table]
keywords: [협력사 평가, Source-to-Pay, 공급망 위험, 환경·사회·지배구조 실사, RFx, OTIF, 공급사 점수, 조달 윤리]
related: []
priority: normal
domain: D08
section: 14
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 836
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 14. Supplier Governance, ESG and Procurement Workflow

## 14.1 Publicly Confirmed Governance

E&S는 공급망 ESG 정책·협력사 행동강령·공정입찰 가이드·조달윤리 원칙을 운영한다. 2021년부터 ESG 실사를 시행했고 LNG열병합·신재생·도시가스·통합구매 우수협력사 등 약 100개사를 실사 대상 pool로 선정했으며, 2022년에는 자발적으로 참여한 26개사를 실사했다. 1차 진단은 환경·사회·지배구조 21개 핵심 관리항목과 33개 세부요소를 점수화하고 A/B/C 등급을 부여하며, 개선계획 이후 약 4~6개월 뒤 2차 진단하는 구조다.

## 14.2 Source-to-Pay Workflow

| 단계 | 필수 통제 | 데이터 산출물 | O/I 가능성 |
|---|---|---|---|
| demand intake | spec·budget·need date | purchase requisition | 중복수요 탐지 |
| sourcing | bidder pool·conflict check | RFx | 공급사 추천 |
| evaluation | technical/commercial/ESG | scorecard | 설명가능 비교 |
| contracting | clause·approval·data right | contract | clause extraction |
| ordering | price·quantity·schedule | PO | anomaly detection |
| expediting | milestone·document·ETA | progress event | delay prediction |
| receipt | quantity·quality·serial | GR/inspection | image/document QA |
| invoice | PO/GR/invoice | payable | 3-way match |
| performance | OTIF·defect·safety·ESG | supplier score | risk forecast |
| renewal/exit | dependency·BCP·switch cost | decision record | scenario analysis |

## 14.3 Supplier ESG Score

| Dimension | 예시 지표 | 증빙 | 위험도 |
|---|---|---|---|
| environment | permit·energy·GHG·waste·water | license·meter·report | 25% |
| safety/health | incident·training·machine safety | record·certificate | 25% |
| labor/human rights | working time·wage·grievance | policy·audit | 15% |
| ethics/governance | anti-bribery·whistleblowing | policy·case | 15% |
| quality/BCP | defect·recall·alternate site | KPI·test | 15% |
| cyber/data | SBOM·access·incident response | assessment | 5% |

가중치는 예시이며 실제 E&S 평가표가 확보되면 교체한다. 안전·인권 위반 등 knockout 항목은 가중평균으로 상쇄하지 않는다.

## 14.4 Third-Party Data Rules

1. 공개형 AI에 계약가격·물량·counterparty limit를 입력하지 않는다.
2. supplier가 제공한 telemetry의 소유·재사용·모델학습 권리를 확인한다.
3. remote access는 named account·MFA·time-bound approval·session log가 필요하다.
4. 공급사 score는 설명가능한 근거와 이의제기 절차를 가진다.
5. 제재·인권·ESG 경보는 자동배제보다 human review gate를 둔다.

---
