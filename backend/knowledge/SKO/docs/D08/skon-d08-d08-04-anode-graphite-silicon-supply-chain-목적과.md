---
id: skon-d08-d08-04-anode-graphite-silicon-supply-chain-목적과
title: Anode / Graphite / Silicon Supply Chain — 목적과 경계
summary: "음극 원료의 채굴부터 셀 조립까지 공급망 범위를 정의하고, 구매 관계를 3단계로 분류하며, 흑연 공정별 추적해야 할 주요 필드를 제시한다."
tags: [d08, supply-chain]
keywords: [구형화, 정제, 코팅, 공급사 분류, 채굴국, AAM, 흑연화, 원산지 추적, 통제주체, 음극활물질, 음극, 흑연, 실리콘, 공급망, 원산지]
related: []
priority: normal
domain: D08
section: D08-04
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain"
tokens: 455
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Anode / Graphite / Silicon Supply Chain

### 1. 목적과 경계

D08-04는 음극 원료가 **천연흑연 채굴·선광 또는 석유계 탄소원 → 구형화·정제 또는 흑연화 → 코팅 음극활물질(AAM) → 실리콘계 첨가·혼합 → SK온 셀 음극**으로 이어지는 경로를 관리한다. 음극 바인더·도전재는 소재 분류상 D08-01에 남기되, 공급사·계약은 D08-05 이후의 보조소재 구간에서 확장한다. 전체 계약 원장과 실제 PO·입고실적은 D08-06, 광산·정제국 원산지는 D08-07, 미국 PFE 판정은 D08-08에서 상세화한다.

공개자료의 음극 공급망은 다음 세 층으로 분리한다.

1. **상용 구매관계:** 제품, 공급자, 구매자와 공급 개시가 확인된 관계
2. **조건부·개발관계:** JDA, 샘플 평가, 품질승인 또는 시설 완공을 전제로 한 관계
3. **그룹 인접관계:** SK㈜·SKC 등 다른 SK 계열사의 투자·JV로, SK온의 구매계약과 동일시할 수 없는 관계

흑연은 채굴국보다 구형화·정제·코팅·흑연화 공정의 국가와 통제주체가 규제·비용·탄소에 더 직접적인 영향을 줄 수 있다. 따라서 `mine_country`, `concentrate_supplier`, `purification_country`, `coating_country`, `AAM_facility`, `supplier_control`을 별도 필드로 둔다.
