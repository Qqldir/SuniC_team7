---
id: skes-d15-21-source-registry
title: Source Registry
summary: "리스크 평가의 정보 출처 신뢰도를 5단계(E1A~INT)로 분류하고 LNG, 재생에너지, 수소 등 각 사업의 정보 출처 31개를 매핑하는 마스터 테이블."
tags: [d15, risk, schema, table, "xref:d06", "xref:d07", "xref:d08", "xref:d09"]
keywords: [Evidence Tier, 신뢰도 등급, 리스크 판정, 정보 출처, 데이터 거버넌스, 회복탄력성, LNG·수소·BESS, D15 기준, 정보 신뢰성, 사업영역]
related: [SRC-ENS-D15-0001, SRC-ENS-D15-0002, SRC-ENS-D15-0003, SRC-ENS-D15-0004, SRC-ENS-D15-0005, SRC-ENS-D15-0006, SRC-ENS-D15-0007, SRC-ENS-D15-0008, SRC-ENS-D15-0009, SRC-ENS-D15-0010, SRC-ENS-D15-0011, SRC-ENS-D15-0012, SRC-ENS-D15-0013, SRC-ENS-D15-0014, SRC-ENS-D15-0015, SRC-ENS-D15-0016, SRC-ENS-D15-0017, SRC-ENS-D15-0018, SRC-ENS-D15-0019, SRC-ENS-D15-0020, SRC-ENS-D15-0021, SRC-ENS-D15-0022, SRC-ENS-D15-0023, SRC-ENS-D15-0024]
priority: normal
domain: D15
section: 21
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 2654
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 21. Source Registry

## 21.1 Evidence Tier

| Tier | 정의 | 사용원칙 |
|---|---|---|
| `E1A` | 법령·정부·시장운영기관·규제기관·세무당국 | 의무·경보·시장규칙·공공안전 기준 |
| `E1B` | SK Innovation/E&S 공식·IR | 자산·사업·거버넌스·공개 통제 |
| `E2` | JV/operator/자회사 공식 | 프로젝트 상태·운영 partner 정보 |
| `E3` | 국제기구·공공 기술기관 | 산업 risk baseline·외부 scenario |
| `INT` | 내부 OT/ERP/CLM/CMMS/CRM/보험/Incident | 실제 residual risk 판정 |

## 21.2 Source Master

| Source ID | Tier | Source | D15 사용 |
|---|---|---|---|
| `SRC-ENS-D15-0001` | E1B | SK Innovation 2025 Integrated Report portal | 전사 sustainability/risk context |
| `SRC-ENS-D15-0002` | E1B | SK Innovation Safety & Health | SHE policy/operating system |
| `SRC-ENS-D15-0003` | E1B | SK Innovation Board Activities | safety/health governance signal |
| `SRC-ENS-D15-0004` | E1B | SK Innovation Information Risk | cyber governance baseline |
| `SRC-ENS-D15-0005` | E1B | E&S LNG value chain | LNG exposure boundary |
| `SRC-ENS-D15-0006` | E1B | E&S power generation | power/CHP boundary |
| `SRC-ENS-D15-0007` | E1B | E&S city gas | city gas boundary |
| `SRC-ENS-D15-0008` | E3 | IEA Gas Market Report Q3-2026 | 2026 LNG supply shock |
| `SRC-ENS-D15-0009` | E1B | E&S renewable | renewable/PPA boundary |
| `SRC-ENS-D15-0010` | E1B | E&S energy solution | KCE/EverCharge boundary |
| `SRC-ENS-D15-0011` | E1B | E&S hydrogen | LH2 value-chain boundary |
| `SRC-ENS-D15-0012` | E2 | Santos Barossa project | operator/project baseline |
| `SRC-ENS-D15-0013` | E2 | Santos 2025 Q4 | first LNG cargo loading 2026 |
| `SRC-ENS-D15-0014` | E2 | Santos 2026 Investor Briefing | Barossa ramp status |
| `SRC-ENS-D15-0015` | E1B | Jeonnam Offshore Wind | 96MW COD / 2·3 stage |
| `SRC-ENS-D15-0016` | E2 | KCE projects | operating/development BESS boundary |
| `SRC-ENS-D15-0017` | E1A | ERCOT 2025 Annual Report | 2026 BESS/reliability environment |
| `SRC-ENS-D15-0018` | E1A | ERCOT MORA June 2026 | low-wind/limited-BESS risk profile |
| `SRC-ENS-D15-0019` | E1A | NYISO Energy Storage | NY storage market interface |
| `SRC-ENS-D15-0020` | E1A | MOTIE ICHS 2025 | LH2 safety/public context |
| `SRC-ENS-D15-0021` | E1A | KPX H2 auction cancellation | demand state control |
| `SRC-ENS-D15-0022` | E1A | Korea K-ETS Phase 4 | carbon cost risk |
| `SRC-ENS-D15-0023` | E1A | IRS 48E | BESS tax eligibility |
| `SRC-ENS-D15-0024` | E1A | IRS PFE guidance | supplier evidence risk |
| `SRC-ENS-D15-0025` | E1A | IRS OBBBA 30C FAQ | charging incentive cliff |
| `SRC-ENS-D15-0026` | E1A | Australia Safeguard Mechanism | Barossa/Darwin carbon risk |
| `SRC-ENS-D15-0027` | E3 | IEA Financing CCUS at Scale | CCS bankability/risk allocation |
| `SRC-ENS-D15-0028` | E3 | IEA CCUS progress 2026 | capture-storage mismatch |
| `SRC-ENS-D15-0029` | E1A | CISA Cross-Sector CPG 2.0 | OT/IT control baseline |
| `SRC-ENS-D15-0030` | E1A | CISA Iranian-affiliated OT advisory 2026 | current OT external threat signal |
| `SRC-ENS-D15-0031` | E2 | Plug Power 2025 10-K | Hyverse ownership transition |
| `SRC-ENS-D15-0032` | E1A | Vietnam MOIT project acceleration | Quynh Lap schedule mechanism |
| `SRC-ENS-D15-0033` | E1B | SK Innovation 2026 Q2 results | E&S current business status |
| `SRC-ENS-D15-0034` | E2 | Freeport LNG gas liquefaction | long-term tolling interface |
| `SRC-ENS-D15-0035` | E2 | Kinder Morgan–SK E&S transport | US gas transport interface |
| `SRC-ENS-D15-0036` | E1A | Korean High-pressure Gas Act | LNG/LH2 safety interface |
| `SRC-ENS-D15-0037` | E1A | Korean City Gas Act | city-gas safety/operation |
| `SRC-ENS-D15-0038` | E1A | Korean Electrical Safety Act | power/BESS safety interface |
| `SRC-ENS-D15-0039` | E1A | ERCOT Nodal Protocols | BESS rule-current source |
| `SRC-ENS-D15-0040` | E1A | NYISO ICAP storage requirement | BESS capacity/rule risk |
| `SRC-ENS-D15-0041` | INT | D06 Process Master | equipment/process/failure crosswalk |
| `SRC-ENS-D15-0042` | INT | D07 Asset Master | exposure unit crosswalk |
| `SRC-ENS-D15-0043` | INT | D08 Supply Chain Master | source/vendor/logistics crosswalk |
| `SRC-ENS-D15-0044` | INT | D09 Customer Master | demand/counterparty crosswalk |
| `SRC-ENS-D15-0045` | INT | D10 Market Master | market KRI/scenario crosswalk |
| `SRC-ENS-D15-0046` | INT | D11 Economics Master | margin/cash risk crosswalk |
| `SRC-ENS-D15-0047` | INT | D12 CAPEX Master | EAC/PF/cash-call crosswalk |
| `SRC-ENS-D15-0048` | INT | D13 Governance Master | contract/JV obligation crosswalk |
| `SRC-ENS-D15-0049` | INT | D14 Regulation Master | rule/permit/compliance crosswalk |

## 21.3 Source URL Master

| ID | URL |
|---|---|
| `0001` | https://www.skinnovation.com/esg/Sustainability_Report |
| `0002` | https://www.skinnovation.com/esg/social-safety |
| `0003` | https://www.skinnovation.com/esg/directorate_02 |
| `0004` | https://www.skinnovation.com/esg/gov-security |
| `0005` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=lngcondition |
| `0006` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=powergeneration |
| `0007` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=citygas |
| `0008` | https://www.iea.org/reports/gas-market-report-q3-2026/executive-summary |
| `0009` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=recycleenergy |
| `0010` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=energysolution |
| `0011` | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=h2 |
| `0012` | https://www.santos.com/barossa/ |
| `0013` | https://www.santos.com/wp-content/uploads/2026/01/2025-Santos-Fourth-Quarter-Report.pdf |
| `0014` | https://www.santos.com/wp-content/uploads/2026/05/Santos-2026-Investor-Briefing-Day_ASX.pdf |
| `0015` | https://askinno.com/global/archives/21360 |
| `0016` | https://keycaptureenergy.com/projects/ |
| `0017` | https://www.ercot.com/files/docs/2026/03/19/2025-ERCOT-Annual-Report-Final-Single-Pages-March-19-2026.pdf |
| `0018` | https://www.ercot.com/files/docs/2026/04/02/MORA_June2026.pdf |
| `0019` | https://www.nyiso.com/energy-storage |
| `0020` | https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/170950/view |
| `0021` | https://new.kpx.or.kr/board.es?act=view&bid=0042&list_no=76081&mid=a10501010000 |
| `0022` | https://www.me.go.kr/home/web/newsRead.do?boardId=1831130 |
| `0023` | https://www.irs.gov/credits-deductions/clean-electricity-investment-credit |
| `0024` | https://www.irs.gov/newsroom/treasury-irs-provide-guidance-for-certain-energy-tax-credits-regarding-material-assistance-provided-by-prohibited-foreign-entities-under-the-one-big-beautiful-bill |
| `0025` | https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb |
| `0026` | https://www.dcceew.gov.au/climate-change/emissions-reporting/national-greenhouse-energy-reporting-scheme/safeguard-mechanism |
| `0027` | https://www.iea.org/reports/financing-ccus-at-scale |
| `0028` | https://www.iea.org/commentaries/policy-and-financing-momentum-sustain-ccus-progress-despite-setbacks |
| `0029` | https://www.cisa.gov/cross-sector-cybersecurity-performance-goals/cross-sector-cybersecurity-performance-goals |
| `0030` | https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a |
| `0031` | https://www.sec.gov/Archives/edgar/data/1093691/000110465926022286/plug-20251231x10k.htm |
| `0032` | https://moit.gov.vn/en/news/ministry-of-industry-and-trade-accelerates-implementation-of-key-power-projects.html |
| `0033` | https://askinno.com/global/archives/156625 |
| `0034` | https://freeportlng.com/our-business/gas-liquefaction |
| `0035` | https://ir.kindermorgan.com/news/news-details/2014/Kinder-Morgan-and-SK-ES-LNG-Announce-Long-Term-Intrastate-Transportation-Agreement-and-Lateral-Development-Project/default.aspx |
| `0036` | https://law.go.kr/LSW/lsInfoP.do?lsiSeq=286839 |
| `0037` | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=285295 |
| `0038` | https://law.go.kr/LSW/lsInfoP.do?lsiSeq=287605 |
| `0039` | https://www.ercot.com/mktrules/nprotocols/current |
| `0040` | https://www.nyiso.com/documents/20142/50467048/MST%205.12%20FID5213_3.21.pdf |
| `0041` | LOCAL:D06 |
| `0042` | LOCAL:D07 |
| `0043` | LOCAL:D08 |
| `0044` | LOCAL:D09 |
| `0045` | LOCAL:D10 |
| `0046` | LOCAL:D11 |
| `0047` | LOCAL:D12 |
| `0048` | LOCAL:D13 |
| `0049` | LOCAL:D14 |

---

# 22. Machine-readable Summary

```yaml
domain: D15
entity: ORG-SKI-ENS-CIC-000001
as_of: 2026-08-06
status: REPRESENTATIVE_COMPANY_DEEP_DB
counts:
  risk_taxonomy: 30
  public_external_signals: 15
  failure_modes: 104
  kri: 62
  stress_scenarios: 24
  controls: 50
  enterprise_risk_records: 60
  pain_points: 50
  oi_seeds: 80
  priority_poc: 20
  internal_data_requests: 45
  sources: 49
top_cross_business_risks:
  - LNG supply and route shock
  - power reliability and margin compression
  - grid and BESS market/rule risk
  - LH2 process safety and utilization
  - CCS FID/MRV/storage mismatch
  - project schedule and PF/JV governance
  - OT cyber and AI/data integrity
d17_gate:
  safety: required_where_applicable
  legal_tax: required_where_applicable
  cyber_privacy: required_where_applicable
  human_approval: mandatory_for_material_decisions
  source_lineage: mandatory
```

---
