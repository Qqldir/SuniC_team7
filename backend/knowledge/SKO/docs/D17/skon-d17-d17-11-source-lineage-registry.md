---
id: skon-d17-d17-11-source-lineage-registry
title: Source & Lineage Registry
summary: "D17 과제가 참조하는 D01~D16 도메인별 Source 파일, 사용 범위, 외부 Source 통제 방식을 정의한 매핑 레지스트리"
tags: [d17, oi-portfolio, table, "xref:d01", "xref:d02", "xref:d03", "xref:d04"]
keywords: [도메인 매핑, 참조 Source, D01~D16, 선행 도메인, 소스 관리, 계약 검증, 혈통 추적, 메타데이터, Source ID, 라인리지, 사용 범위, 원문 검증, Source 통제, 계약 Version]
related: [SRC-D17-D01, SRC-D17-D02, SRC-D17-D03, SRC-D17-D04, SRC-D17-D05, SRC-D17-D06, SRC-D17-D07, SRC-D17-D08, SRC-D17-D09, SRC-D17-D10, SRC-D17-D11, SRC-D17-D12, SRC-D17-D13, SRC-D17-D14, SRC-D17-D15, SRC-D17-D16]
priority: normal
domain: D17
section: D17-11
source: SK온_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation
tokens: 704
updated: 2026-08-03
---

> SK온 · D17 오픈이노베이션 과제 포트폴리오·AI 추천 · SK온 D17 Open-Innovation Opportunity Portfolio & AI Task Recommendation

## D17-11 Source & Lineage Registry

### 1. 선행 도메인

| Source ID | 파일 | D17 사용 범위 |
|---|---|---|
| `SRC-D17-D01` | `SK온_D01_Corporate_Identity.md` | 법인·조직·CEO·통합구조 Scope |
| `SRC-D17-D02` | `SK온_D02_Business_Portfolio.md` | 사업·고객가치·Portfolio Boundary |
| `SRC-D17-D03` | `SK온_D03_Products_and_Solutions.md` | EV·ESS·BaaS·차세대 Product Seed |
| `SRC-D17-D04` | `SK온_D04_Technology_Taxonomy.md` | Safety·Digital·제조·차세대·외부기술 Seed |
| `SRC-D17-D05` | `SK온_D05_RnD_Patents_and_Intellectual_Property.md` | 공개 R&D·Patent Family·Claim 사전 Map·FTO Gate·공동 IP 원장. 최종 권리·제품 실시·법률결론은 내부 Gate 필요 |
| `SRC-D17-D06` | `SK온_D06_Manufacturing_Process_and_Operations.md` | 공정·Defect·49개 제조 Seed |
| `SRC-D17-D07` | `SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md` | Plant·Capacity·Ramp·21개 Seed |
| `SRC-D17-D08` | `SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md` | 소재·공급망·원산지·순환 15개 Seed |
| `SRC-D17-D09` | `SK온_D09_Customers_Orders_OEM_Relationships.md` | 고객·계약·Call-off·ESS Pipeline 14개 Seed |
| `SRC-D17-D10` | `SK온_D10_Market_Competition_Industry_Dynamics.md` | 시장·경쟁·Portfolio 15개 Seed |
| `SRC-D17-D11` | `SK온_D11_Cost_Profitability_Business_Economics.md` | accepted-kWh 원가·반복이익 15개 Seed |
| `SRC-D17-D12` | `SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md` | CAPEX·Funding·Liquidity 15개 Seed |
| `SRC-D17-D13` | `SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md` | 계약·JV·IP·Exit 15개 Seed |
| `SRC-D17-D14` | `SK온_D14_Policy_Regulation_Incentives_Compliance.md` | 정책·규제·증빙 15개 Seed |
| `SRC-D17-D15` | `SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md` | Risk·Field·SHE·BCP 15개 Seed |
| `SRC-D17-D16` | `SK온_D16_External_Solutions_Startups_Vendors_Open_Innovation_Ecosystem.md` | Provider·Evidence·Scorecard·G0~G8·15개 Seed |

### 2. 외부 Source 처리

D17은 새로운 시장·법률·기업 사실을 추가하지 않고 D01~D16의 Source Lineage를 재사용한다. 최종 승인 전에는 각 과제의 `source_ids`가 해당 도메인의 원문 Source ID와 최신 시행일·계약 Version까지 연결되는지 다시 검증한다.

---
