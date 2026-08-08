---
id: skes-d10-13-competitor-and-substitute-master
title: Competitor and Substitute Master
summary: "LNG, BESS, EV 충전 등 주요 사업 세그먼트별 직·간접 경쟁사와 대체기술을 비교 분석하는 마스터 데이터베이스로, 동일 고객문제·지역·계약단위 기준의 경쟁사 분류와 비교지표를 제시한다."
tags: [d10, market, table, "xref:d08", "xref:d05"]
keywords: [경쟁사 분석, 대체기술, Competitor Ledger, LNG, BESS, EV 충전, 수소, 사업 포트폴리오, 경쟁 지형]
related: [COM-ENS-D10-0001, COM-ENS-D10-0002, COM-ENS-D10-0003, COM-ENS-D10-0004, COM-ENS-D10-0005, COM-ENS-D10-0006, COM-ENS-D10-0007, COM-ENS-D10-0008, COM-ENS-D10-0009, COM-ENS-D10-0010, COM-ENS-D10-0011, COM-ENS-D10-0012, COM-ENS-D10-0013, COM-ENS-D10-0014, COM-ENS-D10-0015, COM-ENS-D10-0016, COM-ENS-D10-0017, COM-ENS-D10-0018, COM-ENS-D10-0019, COM-ENS-D10-0020, COM-ENS-D10-0021, COM-ENS-D10-0022, COM-ENS-D10-0023, COM-ENS-D10-0024]
priority: normal
domain: D10
section: 13
source: SK이노베이션E&S_D10_Market_Competition_and_Industry_Dynamics.md
breadcrumb: ""
tokens: 1209
updated: 2026-08-06
---

> SK이노베이션 E&S · D10 시장·경쟁·산업동향

# 13. Competitor and Substitute Master

## 13.1 Comparison Rule

경쟁사는 회사 규모가 아니라 `동일 고객문제·동일 지역·동일 계약단위`로 비교한다. 통합에너지사와 software vendor를 매출순으로 비교하지 않는다.

## 13.2 Competitor Ledger

| ID | Entity/archetype | Segment | Overlap | Public move/capability | Comparison metric | Source |
|---|---|---|---|---|---|---|
| `COM-ENS-D10-0001` | KOGAS | LNG/city gate | direct/partner | national wholesale·terminal·pipeline | delivered LNG·terminal access | public register |
| `COM-ENS-D10-0002` | POSCO International | LNG/power | direct | gas field–terminal–power integrated chain | chain margin·capacity | 0043 |
| `COM-ENS-D10-0003` | GS Energy | LNG/power/new energy | direct | LNG·E&P·power·hydrogen/SMR portfolio | project return·integration | 0044 |
| `COM-ENS-D10-0004` | global portfolio major | LNG | direct | multi-basin portfolio·trading | optionality·liquidity | structural |
| `COM-ENS-D10-0005` | coal/nuclear/renewables | power | substitute | lower variable cost/low carbon | system cost·availability | 0014-15 |
| `COM-ENS-D10-0006` | Tesla Energy | BESS | direct/adjacent | 46.7GWh deployed 2025 | deployment·solution margin | 0041 |
| `COM-ENS-D10-0007` | Wärtsilä | BESS | partner/competitor | hardware+controls+lifecycle, 130+ sites claim | availability·lifecycle | 0042 |
| `COM-ENS-D10-0008` | Powin | BESS | supplier/competitor | system supply·service | cost·warranty·delivery | D08 |
| `COM-ENS-D10-0009` | Sungrow | BESS | supplier/competitor | battery/PCS scale | DC/AC cost·bankability | D08 |
| `COM-ENS-D10-0010` | Mitsubishi Power | BESS | supplier/competitor | integrated storage project | EPC·LTSA | D08 |
| `COM-ENS-D10-0011` | merchant optimizer | BESS | direct | algorithmic bidding | risk-adjusted margin uplift | structural |
| `COM-ENS-D10-0012` | incumbent utility/developer | PPA | direct | owned renewable+customer base | bankable MW·price | structural |
| `COM-ENS-D10-0013` | REC/green premium | PPA | substitute | lower contracting complexity | all-in compliance cost | 0021 |
| `COM-ENS-D10-0014` | self-generation | PPA | substitute | onsite control | LCOE·site constraint | structural |
| `COM-ENS-D10-0015` | ChargePoint | EV charging | direct | session +34%, port +16% company data | ports·session·software revenue | 0030 |
| `COM-ENS-D10-0016` | OBE Power model | EV charging | direct | owned-operated multifamily rollout | funded ports·site conversion | 0031 |
| `COM-ENS-D10-0017` | Blink/other CPO | EV charging | direct | hardware+network+service | uptime·gross margin·ports | public filings |
| `COM-ENS-D10-0018` | local electrical integrator | EV charging | price competitor | low-cost install | install cost·SLA | internal quotes |
| `COM-ENS-D10-0019` | battery bus | hydrogen mobility | substitute | mature charging ecosystem | route TCO | 0028 |
| `COM-ENS-D10-0020` | CNG/diesel | hydrogen mobility | substitute | incumbent asset base | fuel+carbon TCO | market data |
| `COM-ENS-D10-0021` | gaseous H2 | liquid H2 | substitute | lower liquefaction cost | delivery radius·density | 0032 |
| `COM-ENS-D10-0022` | global industrial gas | hydrogen | direct/partner | molecule·liquefaction·station expertise | delivered cost/kg | company sources |
| `COM-ENS-D10-0023` | O&G storage operator | CCS | direct/partner | subsurface·well·permit | permitted Mtpa | 0037 |
| `COM-ENS-D10-0024` | capture technology vendor | CCS | partner | capture process/IP | capture cost·energy penalty | D05 |
| `COM-ENS-D10-0025` | CCS hub aggregator | CCS | direct | multi-emitter network | contracted tCO2 | 0039 |

## 13.3 Competitive Response Codes

| Code | 의미 | 적용 조건 |
|---|---|---|
| `BUILD` | 내부 개발 | 핵심차별·데이터권리 보유 |
| `BUY` | 솔루션 구매 | 표준화·속도 우선 |
| `PARTNER` | 공동개발·JV | 자산·기술 상호보완 |
| `HEDGE` | 가격·계약 완충 | 변동성 관리 |
| `REPOSITION` | 고객·제품·지역 재배치 | 구조적 수요변화 |
| `EXIT_OR_STOP` | 개발 중단·보류 | bankability gate 미충족 |
| `MONITOR` | signal 추적 | 불확실성 높고 option 유지 |

---
