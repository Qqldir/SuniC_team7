---
id: skes-d08-5-lng-source-contract-and-rights-ledger
title: "LNG Source, Contract and Rights Ledger"
summary: "Tangguh, Freeport, Barossa 등 주요 LNG 공급원별 장기·단기 계약과 도입권, 터미널 이용 현황 및 계약 정보 공개 레벨을 정리한 계약 대장."
tags: [d08, supply-chain, table, "xref:d13"]
keywords: [LNG 공급원, 도입권, LONG_TERM_OFFTAKE, SPOT_PURCHASE, 터미널 사용, Freeport, 용선, 공급망, 계약 조건, 공개 현황]
related: [CTR-ENS-D08-0001, CTR-ENS-D08-0002, CTR-ENS-D08-0003, CTR-ENS-D08-0004, CTR-ENS-D08-0005, CTR-ENS-D08-0006, CTR-ENS-D08-0007, CTR-ENS-D08-0008, CTR-ENS-D08-0009, CTR-ENS-D08-0010, CTR-ENS-D08-0011, CTR-ENS-D08-0012, SUP-ENS-D08-0008, SUP-ENS-D08-0009, SUP-ENS-D08-0010, SUP-ENS-D08-0011, SUP-ENS-D08-0012, SUP-ENS-D08-0013, SUP-ENS-D08-0014, SUP-ENS-D08-0015, SUP-ENS-D08-0016, SUP-ENS-D08-0017, SUP-ENS-D08-0018, SUP-ENS-D08-0019]
priority: normal
domain: D08
section: 5
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 3424
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 5. LNG Source, Contract and Rights Ledger

## 5.1 Public Contract/Right Master

| Contract ID | 상대방/프로젝트 | 유형 | 공개 규모·기간 | 공급경로 | 상태·주의 |
|---|---|---|---|---|---|
| `CTR-ENS-D08-0001` | Tangguh, Indonesia | LONG_TERM_OFFTAKE | 연 50~60만 톤; 2004/2005 이후 | Tangguh→Gwangyang | 실제 연도별 인도량 internal |
| `CTR-ENS-D08-0002` | Continental Resources/Woodford | EQUITY_PRODUCTION/JDA | 약 110만 톤/년 생산 설명 | Woodford→U.S. network | 전량 E&S 도입으로 해석 금지 |
| `CTR-ENS-D08-0003` | Freeport LNG | TOLLING_USE_OR_PAY | 220만 톤/년·20년 | feed gas→Train 3 | 계약가격·availability 조항 비공개 |
| `CTR-ENS-D08-0004` | Barossa JV/Santos | EQUITY_PRODUCTION | E&S 37.5% 지분 관계 | field→FPSO→Darwin | D13에서 JV 상세 |
| `CTR-ENS-D08-0005` | Barossa/Darwin LNG | LONG_TERM_OFFTAKE/LIQUEFACTION | 약 130만 톤/년 도입 설명 | Darwin→Korea | 지분·도입·액화 중복 금지 |
| `CTR-ENS-D08-0006` | Darwin LNG/Bayu-Undan | EQUITY/JV | 25% 공개관계 | Darwin/Bayu-Undan | CCS 전환권 상세 internal |
| `CTR-ENS-D08-0007` | LNG carriers 1~2 | TIME_CHARTER | 2016 계약·2019 인수; 2척 | Freeport route | 선주·용선기간 내부확인 |
| `CTR-ENS-D08-0008` | LNG carriers 3~4 | TIME_CHARTER/UNKNOWN | 2021·2022 인수 | portfolio | 실명·사양·계약 상대 internal |
| `CTR-ENS-D08-0009` | Boryeong LNG Terminal | TERMINAL_USE_AGREEMENT | 350만 톤/년 사용권 | import→storage→sendout | 지분 매각 후 권리 유지 |
| `CTR-ENS-D08-0010` | Ganyu LNG Terminal | TERMINAL_USE_AGREEMENT | 일부 설비 사용권; 2027 예정 | China LNG business | 운영실적 아님 |
| `CTR-ENS-D08-0011` | Sabine Pass spot cargo | SPOT_PURCHASE | 2017 공개 사례 | U.S.→Paju | historical example |
| `CTR-ENS-D08-0012` | spot/portfolio LNG | SPOT_PURCHASE | 물량·상대 미공개 | flexible | 내부 trade blotter 필요 |

## 5.2 Contract Field Gap Matrix

| Field | Tangguh | Woodford | Freeport | Barossa | Boryeong | 내부 우선순위 |
|---|---|---|---|---|---|---|
| annual entitlement | partial | partial | disclosed capacity | partial | disclosed right | P0 |
| monthly delivery profile | unknown | unknown | unknown | unknown | NA | P0 |
| pricing/index formula | unknown | unknown | unknown | unknown | unknown | P0-confidential |
| take/use-or-pay | unknown | NA | use-or-pay confirmed | unknown | unknown | P0 |
| destination flexibility | unknown | NA | unknown | unknown | NA | P1 |
| quality specification | internal | internal | internal | internal | service spec | P0 |
| outage/maintenance notice | internal | internal | internal | internal | internal | P0 |
| make-up/carry-forward | unknown | NA | unknown | unknown | unknown | P1 |
| credit support | unknown | unknown | unknown | unknown | unknown | D13 |
| telemetry/data right | unknown | JV data | operator notice | JV/operator data | terminal data | P0 |

## 5.3 LNG Supply-Source Profiles

### 5.3.1 Tangguh Long-Term Supply

- 공개확인: 2004년 또는 2005년 이후 연 50~60만 톤 규모 천연가스를 도입해 광양발전 연료로 사용했다.
- 권리 성격: 가스전 전체 지분 생산이 아니라 장기 LNG 도입 관계로 저장한다.
- 공급망 변수: cargo window, LNG 조성·발열량, 운송일수, 광양 발전계획, 터미널 slot, 선박 배정.
- 주요 위험: upstream/액화설비 outage, 인도네시아 정책, 항로·기상, 품질 편차, 발전수요와 cargo 고정성 불일치.
- 내부데이터: SPA amendment, annual delivery programme, cargo history, deviation notice, claim/penalty, quality certificate.
- O/I 접점: cargo ETA 예측, 품질기반 발전 heat-rate 보정, 계약 유연성 가치평가.

### 5.3.2 Woodford–Freeport Integrated Route

- 공개확인: Woodford 공동개발 생산 약 110만 톤/년, Freeport 액화 사용권 220만 톤/년, 2020년부터 미국산 셰일가스 도입.
- 구조해석: Woodford 생산만으로 Freeport 220만 톤/년을 모두 충당한다고 단정할 수 없다. 미국 가스망에서 추가 feed gas 조달·portfolio balancing 가능성을 내부자료로 확인한다.
- 경제변수: Henry Hub/지역 basis, pipeline tariff, liquefaction fixed fee, fuel gas, shipping, boil-off, 환율, JKM/국내 발전가치.
- 운영변수: upstream nomination, pipeline imbalance, Train 3 availability, storage/loading window, vessel ETA, Boryeong tank ullage.
- 주요 위험: 허리케인·freeze·액화설비 outage, pipeline constraint, use-or-pay under-utilization, 선박 지연, 국내 수요 급변.
- O/I 접점: feed-gas–tolling–cargo–terminal–dispatch 통합 이익 최적화와 outage 시나리오 자동 재계획.

### 5.3.3 Barossa–Darwin Route

- 공개확인: Santos 운영 Barossa, E&S 37.5% 관계, FPSO·subsea·262km gas export pipeline·Darwin LNG 연결, 2026년 첫 cargo 및 한국 도입.
- 권리분리: Barossa 지분, Darwin LNG 지분, 연 130만 톤 도입 설명물량을 별도 계약·capacity record로 유지한다.
- 데이터 연결: well/FPSO production, gas quality, GEP pressure, Darwin feed, train outage, LNG tank, lifting schedule, carrier, Boryeong arrival.
- 주요 위험: offshore reliability, cyclonic weather, pipeline availability, Darwin brownfield integration, JV data latency, cargo ramp-up, CCS transition dependency.
- O/I 접점: ramp-up anomaly detection, JV entitlement reconciliation, cargo quality/quantity mass balance, end-to-end carbon-intensity ledger.

### 5.3.4 Spot and Portfolio Procurement

- 공개확인: Sabine Pass 현물 구매 사례가 있으며 중장기 계약 외 spot 활용이 언급됐다.
- 미공개: 현재 승인 trader, counterparty limit, 거래한도, pricing window, hedge, optionality, destination clause.
- 필수통제: deal capture–confirmation–credit–nomination–invoice를 하나의 trade ID로 연결한다.
- O/I 접점: spot buy/sell 추천은 자동체결보다 설명가능한 의사결정 지원부터 시작한다.
- 성과분해: 최적화 절감액을 시장가격 효과, 계약 유연성 효과, forecast 효과, trader override 효과로 나눠야 한다.

## 5.4 Canonical Supplier and Partner Master

| Supplier ID | Legal/Project Name | Role | Relationship | Scope | Claim Status |
|---|---|---|---|---|---|
| `SUP-ENS-D08-0008` | Santos | upstream operator/JV partner | Barossa·Darwin/Bayu-Undan | production·operator data | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0009` | JERA | Barossa JV partner | Barossa | equity partner | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0010` | Continental Resources | upstream development partner | Woodford | joint development | DISCLOSED_FACT |
| `SUP-ENS-D08-0011` | Freeport LNG | liquefaction service provider | Train 3 LTA | 2.2Mt/y use-or-pay | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0012` | Tangguh LNG project/counterparty | LNG source | long-term supply | 0.5~0.6Mt/y | DISCLOSED_FACT; legal seller internal |
| `SUP-ENS-D08-0013` | Boryeong LNG Terminal operator/SPV | terminal service | TUA | 3.5Mt/y E&S right | DISCLOSED_FACT; current contract party validate |
| `SUP-ENS-D08-0014` | Ganyu LNG Terminal project | terminal service | planned partial usage | China | DISCLOSED_FACT; terms internal |
| `SUP-ENS-D08-0015` | SK Shipping charter interface | marine/charter | carrier 1~2 historical disclosure | LNG shipping | DISCLOSED_FACT; current party validate |
| `SUP-ENS-D08-0016` | Hyundai Heavy Industries shipyard | shipbuilding | carrier 1~2 construction | LNG vessels | DISCLOSED_FACT |
| `SUP-ENS-D08-0017` | GTT technology | cargo-containment technology | Mark III Flex | carrier 1~2 | DISCLOSED_FACT; licensor/contract boundary validate |
| `SUP-ENS-D08-0018` | power OEM—GE interface | turbine OEM | Gwangyang public configuration | F-class GT | DISCLOSED_FACT; LTSA internal |
| `SUP-ENS-D08-0019` | power OEM—Siemens interface | turbine OEM | Paju/Yeoju/Wirye public configuration | H-class/GT/ST | DISCLOSED_FACT; LTSA internal |
| `SUP-ENS-D08-0020` | power OEM—Doosan interface | turbine OEM | Hanam public configuration | G-class GT | DISCLOSED_FACT; LTSA internal |
| `SUP-ENS-D08-0021` | CIP/Copenhagen Infrastructure Partners | JV/investor partner | Jeonnam OWF1 | 49% context | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0022` | Powin | BESS integrator/OEM | KCE NY3/Texas disclosed projects | cells~controls/BMS/LTSA | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0023` | SunGrid Solutions | EPC/BOP | KCE NY3 | EPC/BOP | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0024` | Black & McDonald | EPC/BOP | KCE NY3/NY6 | engineering/construction | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0025` | Mitsubishi Power Americas | integrator/EPC/service | KCE Texas | EPC/system integration/LTSA | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0026` | Sungrow Americas | BESS/PCS OEM | 390MW frame·TX13·NY6 | integrated system/maintenance | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0027` | Orange & Rockland | owner/grid customer | KCE NY3 | non-wires alternative | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0028` | National Grid | grid/interconnection | KCE NY6 | interconnection | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0029` | EverCharge | affiliate manufacturer/service | EV charging | hardware/software/turnkey | DISCLOSED_FACT |
| `SUP-ENS-D08-0030` | Plug Power/SK Plug Hyverse | JV technology/service | hydrogen | electrolyzer/fuel cell | COUNTERPARTY_CONFIRMED; not E&S-owned IP |
| `SUP-ENS-D08-0031` | Honeywell | capture technology partner | CCS collaboration | ASCC | COUNTERPARTY_CONFIRMED; not E&S-owned IP |
| `SUP-ENS-D08-0032` | KIER | R&D partner | CCUS | capture research | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0033` | CE TECH | R&D/engineering partner | CCUS | process engineering | COUNTERPARTY_CONFIRMED |
| `SUP-ENS-D08-0034` | City-gas wholesale supplier node | gas supplier | 7 affiliates/8 regions | city-gate gas | UNDISCLOSED_GAP |
| `SUP-ENS-D08-0035` | City-gas pipe/valve/meter vendor pool | material suppliers | regional procurement | network materials | INDUSTRY_BASELINE; names internal |
| `SUP-ENS-D08-0036` | Incheon byproduct-H₂ source node | feedstock supplier | IGE/LH₂ plant | hydrogen feed | UNDISCLOSED_GAP |
| `SUP-ENS-D08-0037` | LH₂ trailer/transport vendor pool | logistics | station supply | cryogenic transport | UNDISCLOSED_GAP |

## 5.5 Supplier-Normalization Rules

1. 프로젝트명·브랜드·법인명을 각각 별도 alias로 유지하고 계약 법인명을 canonical key로 삼는다.
2. Santos는 Barossa operator와 Darwin/Bayu-Undan partner 역할을 계약별로 분리한다.
3. Freeport LNG는 LNG commodity seller가 아니라 공개상 액화서비스 제공자이므로 `supplier_role=toller`로 저장한다.
4. Boryeong 물리자산 소유자, 운영사, TUA 계약상대, E&S 권리자를 하나의 supplier로 합치지 않는다.
5. Powin·Sungrow는 공개된 KCE 프로젝트에만 `SUPPLIES` edge를 만들고 미공개 프로젝트에는 후보 edge를 만들지 않는다.
6. OEM 공개구성은 장기서비스계약 존재·기간·보증을 의미하지 않는다. LTSA는 내부 contract master로 검증한다.
7. R&D partner 기술을 E&S 소유품목이나 승인 공급사로 자동 승격하지 않는다.
8. `vendor pool` node는 개별 법인정보가 없는 placeholder이며 공급사 수로 집계하지 않는다.

---
