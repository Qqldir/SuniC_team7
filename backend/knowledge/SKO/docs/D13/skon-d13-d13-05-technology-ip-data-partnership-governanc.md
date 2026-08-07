---
id: skon-d13-d13-05-technology-ip-data-partnership-governanc
title: "Technology, IP & Data Partnership Governance"
summary: "기술·IP·데이터 협력 계약에서 권리를 체계적으로 분해하고, Background/Foreground IP부터 데이터 소유권, 실시권까지 관리하는 방법을 다룬 계약 거버넌스 가이드."
tags: [d13, contract, schema, table]
keywords: [Background IP, Foreground IP, 지식재산권 라이선스, Field of Use, 파트너십 거버넌스, Solid Power, 데이터 소유권, 배타적 라이선스, R&D 계약, 기술 협력 조건, 실시권, 지식재산권, 데이터 소유, 기술협력, 라이선스]
related: []
priority: normal
domain: D13
section: D13-05
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 723
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-05 Technology, IP & Data Partnership Governance

### 1. 권리 분해

| 권리 | 필수 질문 |
|---|---|
| Background IP | 계약 전 각 당사자가 보유한 특허·Know-how는 무엇인가? |
| Foreground IP | 공동개발 결과의 소유·공동출원·비용·실시권은 누구에게 있는가? |
| Improvements | 기존기술의 개량이 Background인지 Foreground인지? |
| Field of Use | R&D·Pilot·상업 Cell·ESS·자동차 중 어디까지 허용되는가? |
| Territory/Site | 어느 국가·법인·공장·Line에서 사용할 수 있는가? |
| Exclusivity | 독점·비독점·고객/지역 제한과 경쟁사 협력 제한은 무엇인가? |
| Sublicense/Transfer | JV·계열사·OEM·위탁생산자에게 재허용 가능한가? |
| Data | 원시공정·시험·실패·모델·파생데이터의 소유와 사용범위는? |
| Confidentiality | 인력 이동·공급사·AI 학습·Cloud 사용 시 통제는? |
| Termination Survival | 종료 후 License·재고·설비·데이터·비밀유지 의무는? |

### 2. Solid Power 계약군 판정

```yaml
solid_power_sk_on_public_contract_map:
  r_and_d_license:
    term_payment_USD_million: 20
    payment_period: 2024_to_2027
    trigger: milestones
    field_of_use: research_and_development_only
    commercial_cell_production: prohibited_under_public_description
  line_installation:
    estimated_value_USD_million: 22
    trigger: milestones_and_acceptance
    site_acceptance: completed_2026_Q1
  electrolyte_supply:
    minimum_quantity_metric_tons: 8
    through: 2030
    latest_supplier_expected_minimum_revenue_USD_million: 8.3
  unresolved:
    - commercial_license_conversion_trigger
    - foreground_IP_and_improvement_rights
    - validation_failure_and_remedy
    - data_and_model_usage_rights
```

Ferrari MOU는 전문성과 Insight 공유라는 협력방향만 공개했다. 이를 공동특허·독점개발·신규차종 수주로 확장하지 않는다. ExxonMobil MOU도 최종 Offtake 계약 전에는 가격·품질·Project FID·공급의무가 확정되지 않은 상태다. ([Ferrari](https://eng.sk.com/news/sk-on-ferrari-strengthen-partnership-to-lead-innovation-in-cell-technology), [ExxonMobil](https://corporate.exxonmobil.com/news/news-releases/2024/0625_exxonmobil-sk-lithium-supply-agreement))

---
