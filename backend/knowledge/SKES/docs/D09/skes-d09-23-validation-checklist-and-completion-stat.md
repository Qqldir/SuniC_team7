---
id: skes-d09-23-validation-checklist-and-completion-stat
title: Validation Checklist and Completion Status
summary: "SK이노베이션 E&S의 고객·계약·수요·정산 데이터 구조화 현황과 공개정보 한계, 그리고 시장분석 다음단계를 종합평가한다."
tags: [d09, customer, schema, "xref:d03", "xref:d06", "xref:d07", "xref:d08"]
keywords: [고객관계, PPA, 도시가스, 정산조건, 오프테이커, 수소, EverCharge, CCS, 시장운영기관, 데이터품질]
related: []
priority: normal
domain: D09
section: 23
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 947
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 23. Validation Checklist and Completion Status

## 23.1 Structural Checks

- [x] Customer·Relationship·Contract·Demand·Service Event 분리
- [x] 고객·시장운영기관·지자체·파트너 분리
- [x] PPA 공개 고객 6개 관계 원장
- [x] 도시가스 권역별 공개 고객 스냅샷과 기준일 통제
- [x] KCE 시장형·utility형 관계 분리
- [x] EverCharge 공개 고객사례 8개 구조화
- [x] 수소 MOU·계획·운영수요 상태 분리
- [x] CCS 잠재고객을 상용계약으로 오인하지 않음
- [x] Risk 30개·Pain Point 30개·Seed 60개 작성
- [x] P0 15개·내부 데이터 요청 28개 작성
- [x] D03·D06·D07·D08 및 D10~D17 인계 정의

## 23.2 Known Limitations

1. PPA 가격·발전원·고객별 실제 MWh·불균형 조건은 공개되지 않았다.
2. 도시가스 자회사별 고객 수 기준일이 달라 2026 동일시점 전수 합계는 내부자료가 필요하다.
3. 발전·CHP의 개별 오프테이커·열공급 계약·정산조건은 공개자료만으로 확정할 수 없다.
4. KCE 시장별 실제 매출·상품구성·입찰성과는 공개되지 않았다.
5. EverCharge 사례의 실제 계약금액·활성사용자·SLA는 공개되지 않았다.
6. 액화수소 station 운영 수·실제 kg 판매·최소구매의무는 최신 내부 원장이 필요하다.
7. CCS는 공개된 상용 고객·확정 저장계약보다 개발·파트너 관계가 중심이다.

## 23.3 Completion Summary

```yaml
domain: D09
status: COMPLETE_REPRESENTATIVE_COMPANY_DEEP_DB
as_of: 2026-08-05
source_count: 40
public_relationship_records: 34
customer_segments: 13
public_ppa_records: 6
evercharge_case_records: 8
risk_records: 30
pain_point_records: 30
oi_seed_records: 60
p0_shortlist: 15
internal_data_requests: 28
retrieval_chunks: 14
next_domain: D10_MARKET_COMPETITION_INDUSTRY_DYNAMICS
```

---

## Final Interpretation

SK이노베이션 E&S의 고객구조는 단일 제조업체의 수주잔고처럼 볼 수 없다. 도시가스는 대규모 규제소매 고객과 안전·서비스 event, 발전·BESS는 시장운영기관의 dispatch·정산, PPA는 장기 기업 오프테이크, EV 충전은 사이트와 최종 사용자, 수소는 지자체·차량·충전소·연료계약이 결합된 생태계다.

D09의 핵심 O/I 방향은 고객추천 챗봇 자체가 아니라 다음 네 가지다.

1. 계약–수요–계량–정산의 Golden Thread.
2. 시장·자산·고객수요를 잇는 운영 최적화.
3. MOU·계획·계약·실적을 구분하는 수요 신뢰도 통제.
4. 개인정보·계약기밀·시장규칙을 지키는 human-in-the-loop 의사결정.

이 구조를 기준으로 D10은 고객목록을 반복하지 않고, 각 segment의 시장규모·경쟁사·가격형성·수요변동·대체재를 분석해야 한다.
