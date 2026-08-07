---
id: skes-d09-6-public-customer-and-relationship-ledger
title: Public Customer and Relationship Ledger
summary: "PPA, 도시가스, 전력시장 등 사업 부문별 고객사와의 거래 관계를 정리한 원장표로, 고객 유형, 규모, 계약 상태를 한눈에 파악할 수 있다."
tags: [d09, customer, table, "xref:d07", "xref:d08", "xref:d05", "xref:d06"]
keywords: [PPA, 도시가스, 전력시장, 거래처, 계약, 오프테이크, 배터리, 공급, 고객사, 규모]
related: [REL-ENS-D09-0001, REL-ENS-D09-0002, REL-ENS-D09-0003, REL-ENS-D09-0004, REL-ENS-D09-0005, REL-ENS-D09-0006, REL-ENS-D09-0007, REL-ENS-D09-0008, REL-ENS-D09-0009, REL-ENS-D09-0010, REL-ENS-D09-0011, REL-ENS-D09-0012, REL-ENS-D09-0013, REL-ENS-D09-0014, REL-ENS-D09-0015, REL-ENS-D09-0016, REL-ENS-D09-0017, REL-ENS-D09-0018, REL-ENS-D09-0019, REL-ENS-D09-0020, REL-ENS-D09-0021, REL-ENS-D09-0022, REL-ENS-D09-0023, REL-ENS-D09-0024]
priority: normal
domain: D09
section: 6
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 1610
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 6. Public Customer and Relationship Ledger

| Relationship ID | Counterparty/customer | Segment | Public state | Public scale | Commercial interpretation | Source |
|---|---|---|---|---|---|---|
| `REL-ENS-D09-0001` | Amorepacific Daejeon Daily Beauty | PPA | contracted | 5MW, 20 years | firm disclosed PPA; actual MWh separate | 0005 |
| `REL-ENS-D09-0002` | SK Specialty/materials affiliates | PPA | contracted | 50MW, 2024~2044 | group-related offtake; connected transaction check | 0006 |
| `REL-ENS-D09-0003` | BASF Korea | PPA | contracted/announced | approx. 16% of 2025 demand described | volume and price internal-required | 0008 |
| `REL-ENS-D09-0004` | LG Innotek | PPA | disclosed relationship | undisclosed | contract ledger required | 0007 |
| `REL-ENS-D09-0005` | AWS | PPA | disclosed relationship | undisclosed | data-center load profile; terms confidential | 0007 |
| `REL-ENS-D09-0006` | Iljin Global | PPA | disclosed relationship | undisclosed | industrial offtaker | 0007 |
| `REL-ENS-D09-0007` | Ko-one service region | city gas | operating regulated supply | historical public 1.476m demand accounts | basis date control required | 0028 |
| `REL-ENS-D09-0008` | Busan households/businesses | city gas | operating | 1.59m households, 2023-12 | household 1.52m; commercial etc. 0.07m | 0029 |
| `REL-ENS-D09-0009` | Youngnam Gumi region | city gas | operating | 332,573 households, 2023-10 | seven-area regional aggregate | 0030 |
| `REL-ENS-D09-0010` | Youngnam Pohang region | city gas | operating | 190,353 accounts | usage class breakdown public | 0031 |
| `REL-ENS-D09-0011` | Gangwon region | city gas | operating | 151,145 households, 2022-10 | old snapshot; refresh required | 0032 |
| `REL-ENS-D09-0012` | Jeonbuk Iksan/Jeongeup | city gas | operating | 151,401 accounts, 2026-06 | latest disclosed classification | 0033 |
| `REL-ENS-D09-0013` | Chungcheong region | city gas | operating | portfolio aggregate only here | detailed source refresh | 0001 |
| `REL-ENS-D09-0014` | Jeonnam region | city gas | operating | portfolio aggregate only here | detailed source refresh | 0001 |
| `REL-ENS-D09-0015` | KPX | power market | market participation | Gwangyang/Paju/Yeoju/CHP output | market/settlement, not end customer | 0034 |
| `REL-ENS-D09-0016` | KEPCO grid | power/PPA | network interface | wheeled power | network service, not offtaker | 0004 |
| `REL-ENS-D09-0017` | Heat-service customers | CHP | operating | undisclosed | weather-driven contract demand | 0002 |
| `REL-ENS-D09-0018` | ERCOT | KCE BESS | market participation | portfolio-linked | bid/award/dispatch/settlement | 0011,0013 |
| `REL-ENS-D09-0019` | NYISO | KCE BESS | market participation | NY assets | market and interconnection relationship | 0010,0014 |
| `REL-ENS-D09-0020` | Orange & Rockland | utility NWA | selected/contracted case | KCE NY3 | NWA service, not spot-market-only | 0012 |
| `REL-ENS-D09-0021` | Avis/Budget IAH | fleet charging | operating case | L2+DCFC, number not normalized | fleet availability use case | 0015 |
| `REL-ENS-D09-0022` | 340 On The Park | residential charging | operating case | undisclosed | premium condo amenity | 0016 |
| `REL-ENS-D09-0023` | Metropolis Tower 2/FirstService | residential charging | operating case | 16 chargers; ~$100k avoided upgrade | quantified value case | 0017 |
| `REL-ENS-D09-0024` | AFC headquarters | workplace charging | operating case | 13 L2 | employee benefit and visibility | 0018 |
| `REL-ENS-D09-0025` | Anonymous corporate campus | workplace charging | operating case | 173 EVSE | anonymized; do not infer client | 0019 |
| `REL-ENS-D09-0026` | The Legacy | residential charging | operating case | 80 chargers + 67 ready circuits | installed vs ready separated | 0020 |
| `REL-ENS-D09-0027` | Las Flores | residential charging | operating case | 55-car design context | load-management case | 0021 |
| `REL-ENS-D09-0028` | SK hynix Icheon commute buses | hydrogen mobility | operating supply case | station can serve up to 120 buses/day | capacity not actual daily demand | 0026 |
| `REL-ENS-D09-0029` | KD Transport Group | hydrogen mobility | MOU/rollout | 6+ stations planned | MOU not firm take-or-pay | 0024 |
| `REL-ENS-D09-0030` | Cheonan City/bus operators | hydrogen mobility | MOU/plan | 350 buses by 2027 plan | vehicles and station demand conditional | 0025 |
| `REL-ENS-D09-0031` | Incheon City/ministries/Hyundai | hydrogen ecosystem | implementation agreement | bus rollout | multi-party enablement relationship | 0027 |
| `REL-ENS-D09-0032` | Busan/Cheongju/Icheon demand areas | hydrogen mobility | rollout | station network plan | actual active stations refresh required | 0023 |
| `REL-ENS-D09-0033` | Santos/JV partners | CCS chain | development partnership | undisclosed | not CO2 storage customer | D07/D08 |
| `REL-ENS-D09-0034` | Potential Korean/Asian emitters | CCS | prospect class | undisclosed | no named offtake stored | D05/D06 |

## 6.1 Public-to-Internal Reconciliation

공개원장은 관계의 존재를 보여줄 뿐 수익성·계약강도·잔여기간·신용보강을 완성하지 않는다. 내부 CRM/계약시스템에서 각 `REL`을 실제 `contract_id`, `billing_account_id`, `asset_id`, `settlement_id`와 연결해야 한다.

필수 검증 순서는 다음과 같다.

1. 법적 계약 당사자와 브랜드명 일치 여부.
2. 계약 체결, 공급개시, 상업운전, 만료 상태 분리.
3. 명목 MW와 실제 월별 MWh 분리.
4. 그룹 내부거래와 외부거래 표시.
5. 매출인식 주체와 운영주체 분리.
6. 계약변경·양도·해지·재협상 event 보존.

---
