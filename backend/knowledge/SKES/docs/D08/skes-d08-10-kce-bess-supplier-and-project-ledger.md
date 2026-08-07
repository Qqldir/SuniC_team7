---
id: skes-d08-10-kce-bess-supplier-and-project-ledger
title: KCE BESS Supplier and Project Ledger
summary: "BESS 프로젝트의 공급자 정보, 프로젝트별 공급자 배정, 조달 데이터 구조, 리스크 신호를 한눈에 보는 공급망 관리 참고자료"
tags: [d08, supply-chain, table]
keywords: [배터리 저장소, OEM, EPC, BMS, PCS, 공급사, 조달, 리스크 신호, LTSA, KCE]
related: [SUP-ENS-D08-0001, SUP-ENS-D08-0002, SUP-ENS-D08-0003, SUP-ENS-D08-0004, SUP-ENS-D08-0005, SUP-ENS-D08-0006, SUP-ENS-D08-0007]
priority: normal
domain: D08
section: 10
source: SK이노베이션E&S_D08_Supply_Chain_Procurement_Raw_Materials_and_Logistics.md
breadcrumb: ""
tokens: 823
updated: 2026-08-06
---

> SK이노베이션 E&S · D08 공급망·조달·설비·물류

# 10. KCE BESS Supplier and Project Ledger

## 10.1 Public Supplier Master

| Supplier ID | 공급자 | 공개 역할 | 적용 범위 | 오인 방지 |
|---|---|---|---|---|
| `SUP-ENS-D08-0001` | Powin | integrated BESS·BMS·service | NY3·Texas 일부 | 전체 KCE 포트폴리오 표준 아님 |
| `SUP-ENS-D08-0002` | SunGrid Solutions | EPC/BOP | NY3 | 소유자 아님 |
| `SUP-ENS-D08-0003` | Black & McDonald | EPC/BOP·engineering | NY3/NY6 | BESS OEM 아님 |
| `SUP-ENS-D08-0004` | Mitsubishi Power Americas | turnkey EPC/system integration/LTSA | Texas 200/230MW 관계 | cell 공급자와 구분 |
| `SUP-ENS-D08-0005` | Sungrow Americas | integrated BESS·PCS·software·maintenance | 390MW frame·TX13·NY6 | 프로젝트별 actual delivery 확인 |
| `SUP-ENS-D08-0006` | O&R | NY3 owner/operator/customer interface | NY3 | KCE 소유자산으로 오인 금지 |
| `SUP-ENS-D08-0007` | National Grid | interconnection | NY6 | 설비 공급자 아님 |

## 10.2 Project-Supplier Ledger

| Project | BESS/OEM | EPC/BOP | 서비스·제어 | 공개범위 |
|---|---|---|---|---|
| KCE NY3 | Powin | SunGrid + Black & McDonald | Powin commissioning/scheduling | cells~controls 통합공급 공개 |
| KCE NY6 20MW/45.6MWh | Sungrow | Black & McDonald | Sungrow maintenance | cells·enclosure·cable·transformer·PCS·software 공개 |
| KCE TX11/12/23 200MW | Powin | Mitsubishi Power | LTSA/BMS | integrated battery·BMS·long-term service 공개 |
| KCE TX13 50MW | Sungrow | internal-required | commissioning | 390MW supply agreement 일부 |

## 10.3 BESS Procurement Data Pack

| Layer | 필수 필드 | 상업/기술 Gate |
|---|---|---|
| cell | maker·plant·chemistry·lot·date | bankability·origin·recall |
| module/rack | serial genealogy·configuration | thermal propagation·replaceability |
| BMS | version·limits·alarm·access | data ownership·cyber |
| PCS | topology·efficiency·grid code | warranty·harmonics |
| enclosure/HVAC | rating·thermal design | ambient derating·fire |
| fire protection | detection·suppression·cause isolation | AHJ/insurer acceptance |
| EMS/PPC | dispatch·interface·fallback | market compliance |
| warranty | throughput·availability·capacity retention | dispatch constraint |
| LTSA | SLA·spares·response·remote access | lifecycle cost |
| EPC handover | as-built·test·point list·training | operations readiness |

## 10.4 BESS Supplier Risk Signals

1. cell recall·thermal incident·quality bulletin.
2. OEM liquidity·warranty reserve·M&A.
3. tariff·sanction·country-of-origin rule change.
4. PCS/transformer lead-time.
5. firmware vulnerability·remote-access dependency.
6. spare availability와 model discontinuation.
7. capacity-retention underperformance.
8. EPC punch-list aging과 as-built 누락.
9. fire-code/insurer requirement 변경.
10. warranty 조건과 MarketCapture dispatch의 충돌.

---
