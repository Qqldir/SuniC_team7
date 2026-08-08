---
id: skes-d17-d17-07-external-evidence-e-s-task-mapping
title: External Evidence → E&S Task Mapping
summary: "외부에서 확인한 기술·플랫폼 사례를 SK이노베이션 E&S 과제별로 매핑하고, 각 과제별 추가 검증 사항과 권장 협력 방식(CO-DEVELOP, BUY, PARTNER 등)을 제시하는 표"
tags: [d17, oi-portfolio, schema, table, "xref:d16"]
keywords: [External Evidence, Capability Mapping, Digital Twin, 협력 모드, 기술 검증, LNG 터미널, BESS, APM, O/I Mode, 과제 포트폴리오]
related: []
priority: normal
domain: D17
section: D17-07
source: SK이노베이션E&S_D17_Open_Innovation_Opportunity_Portfolio_AI_Task_Recommendation.md
breadcrumb: ""
tokens: 1352
updated: 2026-08-06
---

> SK이노베이션 E&S · D17 오픈이노베이션 과제 포트폴리오·AI 추천

# D17-07 External Evidence → E&S Task Mapping

## 1. 사용 원칙

아래 표는 D16에서 확인한 **외부 Capability Evidence를 E&S의 문제 가설에 연결하는 탐색지도**다. 공급사 추천·구매승인이 아니며, 외부사례의 정량효과는 E&S Business Case에 직접 입력하지 않는다.

| D17 과제 | 외부 Evidence / Capability | D16 Evidence 의미 | E&S에서 새로 검증할 것 | 권장 O/I Mode |
|---|---|---|---|---|
| 006 LNG–Terminal–Power Twin | AVEVA/industrial twin, LNG case references; OR/market data | LNG terminal·산업 데이터 통합이 상용 가능 | E&S 계약권리·재고·발전제약 공동 최적화의 실제가치 | CO-DEVELOP + BUY |
| 008 Terminal Energy–BOG | Dragon LNG industrial digital twin; Honeywell UniSim | LNG 공정/에너지 digital twin 사례 존재 | E&S tag·BOG route·운전제약·kWh/GJ 개선 | BUY/CO-DEVELOP |
| 009 Vessel ETA/Berth | Kongsberg voyage optimisation; S&P vessel/flow data | 해상 ETA·route·market data capability | E&S cargo/berth/demurrage와의 join·권리 | BUY + PARTNER |
| 011 Heat-Rate Twin | Seeq–RWE generation; industrial analytics | 발전 시계열 condition/performance 분석 사례 | E&S corrected heat-rate baseline과 Finance value | BUY/CO-DEVELOP |
| 012 Turbine Trip Precursor | C3 AI–Shell APM; GE Vernova APM; Seeq | 대규모 APM/발전 analytics capability | E&S GT label·OEM 권리·warning lead·false alarm | BENCHMARK + BUY |
| 015 O&M Copilot | source-locked industrial knowledge workflow | 문서·시계열·작업지시 연결 가능 | 안전지시 정확성·citation·operator usefulness | CO-DEVELOP |
| 021 Offshore Wind Twin | Vestas digital service; Siemens Gamesa maintenance; APM | OEM/풍력 digital O&M capability | Multi-OEM data right·marine access·cable tail-risk | PARTNER + BUY |
| 026 BESS Bidder | Fluence Mosaic/Nispera; Wärtsilä GEMS | BESS market/asset optimization 상용기술 | KCE 기존 MarketCapture 대비 blind counterfactual | BENCHMARK / BUILD+PARTNER |
| 027 BESS Thermal Fusion | UL 9540A; BESS monitoring/APM ecosystem | 화재시험/안전평가와 asset analytics 존재 | precursor lead·false alarm·installed sensor coverage | PARTNER + BUY |
| 028 Counterfactual Lab | BESS optimizer/EMS ecosystem | bid/dispatch tool은 존재 | KCE 자체 alpha·settlement leakage 독립검증 | BUILD |
| 031 Charger Remote Fix | ChargePoint operations platform | charging management/remote operations capability | EverCharge fault taxonomy·first-fix economics | BENCHMARK + BUY |
| 032 Site Power Headroom | WeaveGrid/managed charging; charging+BESS patterns | grid-aware charging capability | Site one-line·utility limit·ESS economics | CO-DEVELOP |
| 036 LH2 Barrier Health | H2 sensors; Emerson valve/pressure solution | H2/cryogenic sensing·valve capability | 실제 installed barrier·proof-test·failure semantics | PARTNER + BUY |
| 037 LH2 Mass Balance | Emerson Micro Motion cryogenic flow | LH2 극저온 질량유량 계측 capability | meter uncertainty·custody boundary·paid kg reconciliation | PARTNER + BUILD |
| 038 kWh/kg Optimizer | process twin + cryogenic instrumentation | 공정모델/계측 기술은 성숙 | E&S liquefier safe envelope 내 실제 kWh/kg | CO-DEVELOP |
| 041 CCS Digital MMV | SLB risk-based MMV / Sequestri | risk-based MMV·storage evaluation capability | 프로젝트별 permit/risk/sensor/evidence lineage | PARTNER + CO-DEVELOP |
| 043 Subsurface Ensemble | SLB CCS evaluation | subsurface uncertainty modeling capability | E&S/Partner 데이터권리·injectivity decision range | PARTNER |
| 056 OT Asset Census | Dragos passive OT visibility | OT asset/threat 가시화 capability | E&S zone·remote access·zero-impact inventory | BUY/BENCHMARK |
| 057 OT Safety–Cyber | Dragos + internal barrier model | OT alert는 가능, safety context는 별도 | cyber alert와 barrier/operating state correlation | CO-DEVELOP |
| 004 Common Vendor Benchmark | D16 60 vendor / 96 solution registry | 비교대상 충분 | 동일 data/KPI/TCO/exit 조건에서 실제 비교 | BENCHMARK |

## 2. 외부사례 수치 처리 규칙

```yaml
external_evidence_value_rule:
  vendor_claim:
    use_as: hypothesis_prior
    use_as_ens_roi: false
  customer_case:
    use_as: capability_and_deployment_evidence
    use_as_ens_roi: false
  standard_or_regulator:
    use_as: gate_or_requirement_evidence
    use_as_product_performance: false
  ens_internal_poc:
    use_as: measured_evidence_if_baseline_and_counterfactual_valid
    finance_value_requires: finance_validation
```

---
