---
id: skon-d13-d13-02-public-agreement-partnership-ledger
title: Public Agreement & Partnership Ledger
summary: "SK온이 국내외 주요 파트너(현대·기아, Ford, Nissan 등)와 맺은 공개된 계약과 협력 관계를 현황별로 정리한 테이블이다."
tags: [d13, contract, table]
keywords: [HSBMA, BlueOval SK, 배터리공급, Solid Power, 리튬공급, 지분율, JV, 전해질, 공급확보, 파트너현황, 배터리 장기공급계약, Nissan, Solid Power 기술협력, ExxonMobil 리튬, NCM 양극재, LFP, 전해질 공급, 파트너십]
related: [AGR-D13-HSBMA, AGR-D13-BOSK, AGR-D13-SLDP, AGR-D13-NISSAN, AGR-D13-SLATE, AGR-D13-FLATIRON, AGR-D13-EXXON, AGR-D13-FERRARI]
priority: normal
domain: D13
section: D13-02
source: SK온_D13_Contracts_Joint_Ventures_Governance_Partnerships.md
breadcrumb: "SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure"
tokens: 1392
updated: 2026-08-03
---

> SK온 · D13 계약·JV·거버넌스·파트너십 · SK온 D13 — Contracts, Joint Ventures, Governance & Partnership Structure

## D13-02 Public Agreement & Partnership Ledger

| ID | 관계·계약 | 공개된 핵심 구조 | 2026-08 상태 | 핵심 미공개·주의 |
|---|---|---|---|---|
| `AGR-D13-HSBMA` | HMG–SK On / HSBMA | 약 50억달러, 양측 50%, 35GWh 설계, HMG EV 지원 | `ACTIVE_JV_COMMERCIAL_OPERATION` | Board·Reserved Matter·Capital Call·가격·Exit 조항 |
| `AGR-D13-BOSK` | Ford–SK On / BlueOval SK | 과거 50:50 JV, 2026-05-20 거래종결 후 Kentucky→Ford, Tennessee와 BOSK 지분→SKBA 측 | `RESTRUCTURED_AND_SEPARATED` | SK온 측 잔여 차입·보증·Ford 공급관계·사후책임 전체 |
| `AGR-D13-SLDP` | Solid Power–SK On | R&D License·Line Installation·Electrolyte Supply 3계약, Milestone 기반 | `ACTIVE_R_AND_D_ONLY` | 상업생산 License·Foreground IP·검증실패 Remedy |
| `AGR-D13-NISSAN` | Nissan–SK On | 미국산 High-Nickel Pouch 약 100GWh, 2028~2033 | `ACTIVE_FUTURE_SUPPLY` | 연도별 Call-off·가격식·Take-or-pay·공장·해지 |
| `AGR-D13-SLATE` | Slate–SK On | 미국산 High-Nickel NCM 약 20GWh, 2026~2031 + 추가 Option | `ACTIVE_PARTLY_OPTIONAL` | 기본량의 연도별 확정성·Option 조건·Startup Credit Risk |
| `AGR-D13-FLATIRON` | Flatiron–SK On | 1GWh LFP ESS 계약 + 추가 6.2GWh 우선협상권 | `ACTIVE_PARTLY_OPTIONAL` | 추가분 전환조건·Project Finance/COD·LD·Warranty |
| `AGR-D13-EXXON` | ExxonMobil–SK On | 미국산 Lithium 다년 공급 최대 10만t을 검토하는 비구속 MOU | `NON_BINDING_MOU` | 최종 수량·기간·가격·품질·Project FID |
| `AGR-D13-FERRARI` | Ferrari–SK On | Cell 기술 전문성·Insight 공유 확대 MOU | `NON_BINDING_TECH_MOU` | 공동개발범위·IP·Data·상업제품·비용분담 |

HSBMA는 지분 50:50과 35GWh 설계, 2026년 6월 상업생산 개시까지는 확인된다. 그러나 지분율로 Board Quorum, Veto, Capital Call, 보증, 배터리가격과 손실분담을 역산할 수 없다. D13은 `ownership_pct=50`을 저장하되 Governance와 Economic Attribution은 계약 원문 검증 전까지 비워 둔다. ([JV 발표](https://www.hyundainews.com/releases/3821), [상업생산](https://www.hyundainews.com/releases/4876))

Ford의 2026년 5월 20일 8-K는 BOSK에 총 78.3554억달러가 인출됐고, Ford의 50% 지급보증과 최대 66억달러 자본출자의무가 거래종결과 함께 종료됐다고 밝혔다. Ford는 Kentucky 자산과 관련 38.0504억달러 Note를 인수했고, 공개된 JVDA 구조상 SKBA가 BOSK 지분 100%를 보유하며 BOSK는 Tennessee 자산을 유지한다. 이는 `지분 해소`만이 아니라 자산·차입·보증·자본의무가 함께 이동한 사례다. ([Ford 8-K](https://www.sec.gov/Archives/edgar/data/37996/000003799626000093/f-20260520.htm), [Loan Exhibit](https://www.sec.gov/Archives/edgar/data/37996/000003799626000093/exhibit10tofordmay2020268-k.htm), [SK On Tennessee](https://eng.sk.com/news/sk-on-tennessee-becomes-newest-sk-on-u-s-company))

Solid Power 계약군은 기술협력의 구속력 차이를 잘 보여준다. SK온은 2024~2027년 마일스톤에 따라 총 2,000만달러를 지급하는 **R&D 전용** License를 보유하며 상업생산에는 사용할 수 없다. 별도 설치계약은 약 2,200만달러 규모이고, 전해질 계약은 2030년까지 최소 8t 구매를 요구한다. 최신 10-K의 예상 최소 전해질 매출은 830만달러이며, 2026년 1분기 Pilot Line Site Acceptance가 완료됐지만 상업양산 License 획득을 뜻하지 않는다. ([Solid Power 2025 10-K](https://www.sec.gov/Archives/edgar/data/1844862/000110465926019435/sldp-20251231x10k.htm), [2026 Q1 Result](https://www.sec.gov/Archives/edgar/data/1844862/000110465926055631/tm2613507d1_ex99-1.htm))

Nissan·Slate·Flatiron은 각각 장기 총량, 기본량+Option, 확정분+우선협상권이라는 다른 구조다. 특히 Flatiron의 추가 6.2GWh는 확정수주가 아니므로 1GWh와 분리하고, ExxonMobil의 최대 10만t도 비구속 MOU이므로 공급확보량으로 집계하지 않는다. ([Nissan](https://eng.sk.com/news/sk-on-signs-battery-supply-agreement-with-nissan), [Slate](https://eng.sk.com/news/sk-on-selected-as-battery-supplier-for-u-s-ev-startup-slate), [Flatiron](https://askinno.com/global/archives/22126), [ExxonMobil](https://corporate.exxonmobil.com/news/news-releases/2024/0625_exxonmobil-sk-lithium-supply-agreement))

---
