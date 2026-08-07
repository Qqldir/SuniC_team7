---
id: skes-d10-23-validation-and-completion-status
title: Validation and Completion Status
summary: "D10 도메인 분석의 데이터 신뢰도와 공개정보 한계 10개 명시, SK이노베이션 E&S의 LNG·발전·BESS·수소·CCS 통합 포트폴리오 경쟁력 구조"
tags: [d10, market, schema, "xref:d11", "xref:d17"]
keywords: [LNG 자산·권리, 발전·도시가스, 신재생 PPA, BESS·에너지저장, 액화수소, CCS·탄소포집저장, 시장신호, 경쟁사 아키타입, 공개정보 한계, 포트폴리오 경쟁력]
related: []
priority: normal
domain: D10
section: 23
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 987
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 23. Validation and Completion Status

## 23.1 Structural Checks

- [x] 시장 actual·잠정·전망·claim 상태 분리
- [x] LNG 권리·물량·자산 중복 합산 방지
- [x] power·city gas·renewable·PPA 구조화
- [x] KCE 운영 623MW와 8GW pipeline 분리 상속
- [x] ERCOT 최신 BESS snapshot 반영
- [x] EverCharge segment와 경쟁 signal 반영
- [x] 수소 MOU·차량·station·firm sale ladder
- [x] CCS 운영·pipeline·storage mismatch 분리
- [x] 경쟁사·대체재 25개 archetype/record
- [x] 시장 signal 18개·scenario 13개
- [x] risk 30개·pain point 40개
- [x] O/I Seed 60개·P0 12개
- [x] 내부 데이터 요청 30개
- [x] D11~D17 handover

## 23.2 Known Limitations

1. E&S 사업별 시장점유율·수익·계약가격은 공개자료만으로 확정할 수 없다.
2. 2026 LNG 전망은 중동 분쟁·통항 회복가정에 민감하다.
3. 한국 월간 SMP 속보는 잠정치이며 2026 연간 추세로 일반화할 수 없다.
4. 국내 직접 PPA의 전수 계약가격·실제 MWh·shape cost는 비공개다.
5. KCE 시장별 revenue stack·asset별 bid 성과·SOH는 내부자료가 필요하다.
6. EverCharge의 active port·ARR·churn·site payback은 공개되지 않았다.
7. 액화수소 실제 생산·출하·판매 kg와 station 가동률은 내부원장이 필요하다.
8. Bayu-Undan CCS의 firm emitter·storage capacity·tariff·liability는 확정 공개값이 부족하다.
9. 경쟁사 ledger는 동일 scope의 시장점유율 순위가 아니라 archetype 비교다.
10. D10의 score·scenario probability는 공개사실이 아니며 내부 승인 후 사용한다.

## 23.3 Completion Summary

```yaml
domain: D10
status: COMPLETE_REPRESENTATIVE_COMPANY_DEEP_DB
as_of: 2026-08-05
source_count: 47
market_segments: 9
public_fact_records: 24
strategic_battlefields: 11
competitor_records: 25
market_signals: 18
scenarios: 13
risk_records: 30
pain_point_records: 40
oi_seed_records: 60
p0_shortlist: 12
internal_data_requests: 30
retrieval_chunks: 14
next_domain: D11_COST_PROFITABILITY_AND_BUSINESS_ECONOMICS
```

---

## Final Interpretation

SK이노베이션 E&S의 시장경쟁력은 어느 한 사업의 시장점유율로 설명되지 않는다. 핵심은 LNG 공급권과 발전·도시가스 수요, 재생에너지와 PPA 고객, KCE의 BESS 운영·입찰, EverCharge의 부하관리, 액화수소 수요생태계, CCS 저장권을 하나의 option portfolio로 운영하는 능력이다.

D10의 핵심 O/I 방향은 다음 네 가지다.

1. 외부 시장신호를 내부 자산·계약·KPI로 연결하는 Market-to-Asset Graph.
2. 발표 pipeline과 실제 운영·확정수요를 구분하는 probability·stage gate.
3. LNG·CHP·BESS·PPA처럼 복수 가격과 제약이 결합된 최적화.
4. forecast·경쟁사 claim·AI 추천을 versioned evidence와 human decision log로 통제하는 구조.

이 구조를 기준으로 D11은 시장성장률을 반복하지 않고, 각 사업의 원가·마진·손익·현금흐름·민감도를 계산해야 한다.
