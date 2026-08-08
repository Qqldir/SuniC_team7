---
id: skon-d08-d08-02-cathode-supply-chain-목적과-경계
title: Cathode Supply Chain — 목적과 경계
summary: "SK온 양극재 공급망의 관리 경계와 데이터 수집 기준을 정의하며, 계약·시설·원산지·당사자·구매 확정 등의 구분 원칙을 명시한다."
tags: [d08, supply-chain]
keywords: [양극활물질, 전구체, 공급사, 계약물량, 출하량, 원산지, 확정 구매, 법적 주체, pCAM, CAM, 니켈, 코발트, 망간, 광산·정련, 공급계약, 구매 확정]
related: []
priority: normal
domain: D08
section: D08-02
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain"
tokens: 542
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Cathode Supply Chain

### 1. 목적과 경계

D08-02는 양극 원료가 **전구체(pCAM) → 양극활물질(CAM) → 고객 승인 grade → SK온 셀 공장 투입**으로 이어지는 구조와 공개된 공급계약·JV·현지화 프로젝트를 관리한다. 리튬·니켈·코발트·망간의 광산·정련 경로는 D08-03, 공급계약 전체 원장과 실제 발주·실적은 D08-06, 미국 PFE 판정은 D08-08에서 확장한다.

공개자료상 SK온과 직접 연결되는 양극재 관계라도 다음을 구분한다.

1. **계약물량과 실제 출하량:** 장기계약 총량·추정금액은 실제 연도별 구매실적이나 확정 backlog가 아니다.
2. **공급사와 공급시설:** 공급사 계약이 확인돼도 어느 공장에서 어느 SK온 공장으로 공급하는지 공개되지 않았다면 시설 간 edge를 만들지 않는다.
3. **전구체와 양극재:** CAM 공급사가 전구체를 내재화하거나 제3자로부터 조달할 수 있으므로, CAM 계약만으로 pCAM 원산지를 확정하지 않는다.
4. **법적 계약당사자와 사업승계:** 2021년 에코프로비엠 계약은 당시 SK이노베이션 명의로 발표됐다. SK온이 해당 배터리 사업을 승계했더라도 계약상 지위 이전 문서가 공개되지 않았다면 `buyer_of_record_as_announced`를 보존한다.
5. **MOU와 확정 구매:** 공급 논의, 공동평가, 우선협상 또는 잠재 물량은 실제 발주가 확인될 때까지 `sk_on_procurement_confirmed=false|unknown`으로 둔다.
