---
id: skes-d15-2-enterprise-risk-taxonomy
title: Enterprise Risk Taxonomy
summary: "LNG·발전·가스·재생에너지·수소 등 사업 영역별 26개 리스크의 ID, 범주, 노출점, 선행지표를 정리한 종합 마스터 테이블"
tags: [d15, risk, core-candidate, table, "xref:d08", "xref:d10", "xref:d11", "xref:d06"]
keywords: [리스크분류, 위험ID, KRI, 선행지표, 노출, LNG, 도시가스, 재생에너지, BESS, 수소]
related: [RISK-ENS-D15-001, RISK-ENS-D15-002, RISK-ENS-D15-003, RISK-ENS-D15-004, RISK-ENS-D15-005, RISK-ENS-D15-006, RISK-ENS-D15-007, RISK-ENS-D15-008, RISK-ENS-D15-009, RISK-ENS-D15-010, RISK-ENS-D15-011, RISK-ENS-D15-012, RISK-ENS-D15-013, RISK-ENS-D15-014, RISK-ENS-D15-015, RISK-ENS-D15-016, RISK-ENS-D15-017, RISK-ENS-D15-018, RISK-ENS-D15-019, RISK-ENS-D15-020, RISK-ENS-D15-021, RISK-ENS-D15-022, RISK-ENS-D15-023, RISK-ENS-D15-024]
priority: critical
domain: D15
section: 2
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 2319
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 2. Enterprise Risk Taxonomy

## 2.1 Taxonomy Master

| Risk ID | 범주 | 대표 Exposure | 대표 선행 KRI | 주요 상속 |
|---|---|---|---|---|
| `RISK-ENS-D15-001` | LNG 공급·지정학 | Gulf/US/Australia cargo·route | export loss·route closure·ETA variance | D08·D10 |
| `RISK-ENS-D15-002` | LNG 가격·Basis | JKM/HH/oil-linked portfolio | basis·volatility·hedge ratio | D10·D11 |
| `RISK-ENS-D15-003` | Shipping·Terminal | vessel·slot·tank·TUA | ETA drift·tank heel·demurrage | D06·D08·D13 |
| `RISK-ENS-D15-004` | 발전 Reliability | LNG CCGT/CHP | trip·heat rate·forced outage | D06·D07·D11 |
| `RISK-ENS-D15-005` | 발전 Market | SMP·dispatch·reserve | clean spark spread·dispatch hours | D10·D11 |
| `RISK-ENS-D15-006` | 도시가스 안전 | pipeline·station·customer supply | leak alarm·pressure anomaly·odorant | D06·D07·D14 |
| `RISK-ENS-D15-007` | 도시가스 수요 | 7개 도시가스 권역 | HDD·customer churn·load deviation | D09·D10 |
| `RISK-ENS-D15-008` | 재생 자산 Reliability | solar·wind·offshore wind | availability·wake/loss·fault | D06·D07 |
| `RISK-ENS-D15-009` | 계통·Curtailment | renewable/PPA/BESS | congestion·curtailment hours·queue | D10·D14 |
| `RISK-ENS-D15-010` | PPA Shape·Credit | corporate PPA | hourly gap·AR·rating | D09·D11·D13 |
| `RISK-ENS-D15-011` | BESS Asset | KCE projects | SOH·availability·thermal alarm | D06·D07·D10 |
| `RISK-ENS-D15-012` | BESS Market/Model | ERCOT·NYISO | spread decay·bid error·model drift | D10·D14 |
| `RISK-ENS-D15-013` | EV Charging | EverCharge | uptime·session fail·site power | D06·D09·D11 |
| `RISK-ENS-D15-014` | 액화수소 공정안전 | Incheon LH2 | pressure·temperature·BOG·ESD | D06·D07·D14 |
| `RISK-ENS-D15-015` | 수소 수요·가동률 | plant→trailer→station→vehicle | sold kg·station uptime·active vehicles | D09·D11 |
| `RISK-ENS-D15-016` | CCS subsurface/MRV | Bayu-Undan concept·future chain | injectivity·plume·MRV gap | D04·D10·D14 |
| `RISK-ENS-D15-017` | Project Schedule | offshore wind·Quynh Lap·CCS | critical-path slip·permit aging | D12·D14 |
| `RISK-ENS-D15-018` | CAPEX·Funding | PF/JV/projects | EAC variance·DSCR headroom·cash call | D11·D12 |
| `RISK-ENS-D15-019` | Contract/JV | TUA·PPA·JV·EPC·LTSA | covenant·SLA·dispute·capital call | D13 |
| `RISK-ENS-D15-020` | Regulatory/Tax | K-ETS·48E·PFE·H2·permits | rule delta·evidence gap·deadline | D14 |
| `RISK-ENS-D15-021` | OT Cyber | PLC·SCADA·EMS·BMS·charger | remote access·asset exposure·alert | D06·D14 |
| `RISK-ENS-D15-022` | IT/Data/AI | ERP·CLM·trading·RAG | stale data·lineage gap·model drift | D00·D14 |
| `RISK-ENS-D15-023` | Climate/Extreme Weather | plant·grid·wind·terminal | heat/flood/wind/water outage | D07·D10 |
| `RISK-ENS-D15-024` | Supplier/EPC | turbine·cable·BESS·critical spares | lead time·quality escape·concentration | D08·D12 |
| `RISK-ENS-D15-025` | Counterparty/Credit | offtaker·JV·vendor·utility | AR aging·rating·collateral | D09·D13 |
| `RISK-ENS-D15-026` | Compliance/ABAC/Sanctions | global procurement/JV | screening hit·exception·country risk | D13·D14 |
| `RISK-ENS-D15-027` | Workforce/Contractor | plant·construction·field service | training overdue·fatigue·turnover | D06·D07 |
| `RISK-ENS-D15-028` | Reputation/Stakeholder | community·customer·regulator | complaint velocity·media escalation | D09·D14 |
| `RISK-ENS-D15-029` | Insurance/Recovery | major assets·projects | coverage gap·claim aging·BI mismatch | D11·D12 |
| `RISK-ENS-D15-030` | Portfolio Contagion | LNG↔power↔gas↔new energy | correlated loss·liquidity·shared vendor | D10~D14 |

## 2.2 2026 Public/External Signal Board

| Event ID | 공개 사실/외부 신호 | 상태 | D15 해석 |
|---|---|---|---|
| `EVT-ENS-D15-001` | IEA Q3-2026은 중동 전쟁과 호르무즈 해협 사실상 폐쇄로 기존 글로벌 LNG 공급의 약 20%에 해당하던 흐름이 방해받아 가격변동성이 확대됐다고 평가 | `EXTERNAL_SIGNAL` | E&S 특정 cargo 손실을 의미하지 않음. route·supplier·inventory·hedge stress trigger로 사용 `[SRC-ENS-D15-0008]` |
| `EVT-ENS-D15-002` | Santos는 2026년 1월 Barossa 첫 LNG cargo 선적, 2026년 5월에는 Barossa가 가동 중이며 계획된 2026 생산률의 약 75% 수준이라고 공개 | `PUBLIC_CONFIRMED` | 개발위험 중심에서 ramp/reliability/production entitlement 위험으로 전환 `[SRC-ENS-D15-0013][SRC-ENS-D15-0014]` |
| `EVT-ENS-D15-003` | 전남해상풍력 1단계 96MW는 2025년 5월 상업운전 시작 | `PUBLIC_CONFIRMED` | 운영 availability·해상정비·계통·PPA/REC 위험과 2·3단계 개발위험을 분리 `[SRC-ENS-D15-0015]` |
| `EVT-ENS-D15-004` | ERCOT 2025 Annual Report는 2026년 2월 말 BESS 약 16GW와 weatherization inspection 확대를 제시 | `EXTERNAL_SIGNAL` | KCE 개별 availability가 아니라 Texas 경쟁·가격잠식·reliability 환경 신호 `[SRC-ENS-D15-0017]` |
| `EVT-ENS-D15-005` | ERCOT 2026 MORA는 low-wind와 limited-BESS-availability 결합을 별도 risk profile로 분석 | `EXTERNAL_SIGNAL` | BESS의 시장가치와 availability risk가 동시 존재함을 반영 `[SRC-ENS-D15-0018]` |
| `EVT-ENS-D15-006` | 2025 ICHS 공식행사에서 인천 액화수소플랜트 현장방문과 SK Innovation E&S 산업계 기조연설이 포함됨 | `PUBLIC_CONFIRMED` | 안전관리의 중요성을 보여주는 사업·정책 맥락. 사고발생 증거로 사용 금지 `[SRC-ENS-D15-0020]` |
| `EVT-ENS-D15-007` | 2025 청정수소발전시장 입찰은 취소됨 | `PUBLIC_CONFIRMED` | 정책 수요를 firm offtake로 계산하면 utilization risk 과소평가 `[SRC-ENS-D15-0021]` |
| `EVT-ENS-D15-008` | K-ETS 4기에서 발전부문 유상할당 비율이 2026년 15%에서 2030년 50%로 단계 상승 | `PUBLIC_CONFIRMED` | 발전 탄소비용의 구조적 KRI. 단, 실제 cost는 배출·할당·KAU position 필요 `[SRC-ENS-D15-0022]` |
| `EVT-ENS-D15-009` | 미국 48E와 PFE 관련 규칙은 KCE BESS의 공급망·세액공제 검증항목 | `PUBLIC_CONFIRMED_RULE` | 실제 credit 수령액/eligibility는 프로젝트별 내부 검증 `[SRC-ENS-D15-0023][SRC-ENS-D15-0024]` |
| `EVT-ENS-D15-010` | 2026-06-30 이후 설치된 qualifying property에 대해 30C 조기종료 규칙이 적용 | `PUBLIC_CONFIRMED_RULE` | EverCharge 고객경제성·sales funnel stress 요인 `[SRC-ENS-D15-0025]` |
| `EVT-ENS-D15-011` | 호주 Safeguard Mechanism은 적용시설 baseline을 일반적으로 연 4.9% 낮추는 구조 | `PUBLIC_CONFIRMED_RULE` | Barossa/Darwin의 compliance entity·배출·지분을 자동 곱하지 않고 operational control 확인 `[SRC-ENS-D15-0026]` |
| `EVT-ENS-D15-012` | CISA 2026 advisory는 인터넷 연결 OT를 겨냥한 이란 연계 행위자의 활동을 경고 | `EXTERNAL_SIGNAL` | E&S/KCE가 공격받았다는 뜻이 아님. internet-exposed OT·remote access hygiene stress trigger `[SRC-ENS-D15-0030]` |
| `EVT-ENS-D15-013` | SK Innovation은 SHE를 최우선 경영사항으로 두고 통합 SHE 관리체계를 공개 | `PUBLIC_CONTROL_BASELINE` | 그룹 정책을 E&S 각 자산의 실제 barrier test 결과로 복사 금지 `[SRC-ENS-D15-0002]` |
| `EVT-ENS-D15-014` | SK Innovation 이사회 공개활동에는 2025 Safety & Health Management Plan 항목이 포함 | `PUBLIC_GOVERNANCE_SIGNAL` | Board/경영진 oversight의 증거; 개별 현장 통제효과는 내부 검증 `[SRC-ENS-D15-0003]` |
| `EVT-ENS-D15-015` | Plug Power는 2025-12-31 SK Plug Hyverse 49% 지분을 전량 매각했다고 10-K에 공시 | `PUBLIC_CONFIRMED` | JV 구조변화 시 H2 계약·기술·서비스·IP·운영 continuity 검증 필요 `[SRC-ENS-D15-0031]` |

---
