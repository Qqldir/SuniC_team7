---
id: skon-d07-d07-27-utility-labor-environmental-footprint-ri
title: Utility·Labor·Environmental Footprint Risk
summary: 배터리 생산 시설의 에너지·물·인력·환경 리스크 평가 프레임과 헝가리·미국 거점의 구체적 리스크 현황을 다루는 문서
tags: [d07, footprint, schema]
keywords: [배터리 제조, 자원 위험, 에너지 조달, Workforce Risk, 환경 인허가, 탄소집약도, 공장 클러스터, ESS, 자원 리스크, 헝가리 클러스터, 미국 인력, 환경 기준선, Utility 조달, ESS 전환, Pre-SOP]
related: []
priority: normal
domain: D07
section: D07-27.
source: SK온_D07_Manufacturing_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 1070
updated: 2026-08-03
---

> SK온 · D07 생산거점·캐파

# D07-27. Utility·Labor·Environmental Footprint Risk

## 27.1 Resource Risk Schema

```yaml
plant_resource_risk:

  plant_id: required

  electricity:
    - Contracted capacity
    - Peak demand
    - Grid reliability
    - Renewable share
    - Price and volatility
    - Carbon intensity

  thermal_and_dry_room:
    - Natural gas
    - Steam
    - Chilled water
    - Dry air
    - Heat-recovery opportunity

  water:
    - Withdrawal limit
    - Process demand
    - Wastewater capacity
    - Recycling rate
    - Drought risk

  labor:
    - Headcount requirement
    - Qualified maintenance
    - Process engineers
    - Training capacity
    - Turnover
    - Wage inflation

  environmental:
    - Air permit
    - Solvent emissions
    - Hazardous material
    - Waste
    - Fire water
    - Site remediation
    - Community acceptance

  evidence:
    - Permit
    - Utility contract
    - Government report
    - Company disclosure
```

---

## 27.2 Hungary Cluster Risk

유럽연합의 2026년 Hungary Country Report는 Battery Manufacturing을 에너지·물·인력 소요가 큰 산업으로 분류하며, Hungary의 에너지 수입의존성도 지적한다. 따라서 코마롬·이반차 Capacity는 단순 설비 GWh와 함께 Utility 조달능력, 에너지 가격·탄소집약도와 숙련인력 경쟁을 평가해야 한다. ([Economy and Finance][17])

```yaml
hungary_cluster_risk:

  plants:
    - Komarom_1
    - Komarom_2
    - Ivancsa

  concentration:
    - Same-country manufacturing concentration
    - Shared national energy-market exposure
    - Shared labor-market exposure
    - Shared EU regulatory exposure

  required_controls:
    - Plant-level power and water capacity
    - Renewable electricity strategy
    - Workforce and contractor pool
    - Cross-site emergency capacity
    - Carbon-footprint data
```

---

## 27.3 United States Workforce·Incentive Risk

SKBA Commerce는 두 공장을 통해 대규모 현지인력을 채용해 왔고, Tennessee와 HSBMA도 별도의 Workforce 구축이 필요하다. 특히 Pre-SOP·Ramp 단계에서는 생산직 수만이 아니라 유지보수·품질·자동화·Formation·EHS 숙련인력의 자격상태가 병목이 될 수 있다. ([켐프 주지사 사무실][18])

```yaml
us_workforce_risk:

  SKBA_Commerce:
    stage: SERIAL_PRODUCTION
    risk:
      - Retention
      - Product-mix change
      - ESS retraining

  HSBMA:
    stage: CUSTOMER_RAMP
    risk:
      - New-hire certification
      - Yield learning
      - HMG schedule synchronization

  Tennessee:
    stage: PRE_SOP
    risk:
      - Workforce retention before 2028
      - Training decay
      - Product-scenario uncertainty
      - Systems commissioning
```

---

## 27.4 Tennessee Environmental Baseline Control

```yaml
tennessee_environmental_baseline:

  historical_assessment:
    project: BlueOval_SK_45_GWh

  current_use:
    - Site and utility reference
    - Historical permitting baseline

  revalidation_required_for:
    - Product change
    - EV-to-ESS conversion
    - Chemistry change
    - Capacity change
    - Ownership and operating-model change
    - Material and solvent changes
```

과거 DOE 환경평가는 45GWh EV Battery Plant를 기준으로 작성됐기 때문에, ESS·다른 Cell 사양·다른 생산량으로 전환한다면 기존 환경분석과 인허가의 적용가능성을 재검토해야 한다. 이는 현재 인허가가 무효라는 뜻이 아니라 변경범위 확인이 필요하다는 분석이다. ([The Department of Energy's Energy.gov][10])

---
