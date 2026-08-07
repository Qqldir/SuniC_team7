---
id: skon-d15-d15-02-enterprise-risk-taxonomy-public-signal-r
title: Enterprise Risk Taxonomy & Public Signal Register
summary: 전사 리스크 12개 범주별 모니터링 지표(KRI)와 공개 이슈의 리스크 해석을 정의한 분류 체계
tags: [d15, risk, core-candidate, table, "xref:d03", "xref:d04", "xref:d06", "xref:d09"]
keywords: [전사 리스크, 리스크 분류, 선행지표 KRI, NHTSA 리콜, 배터리, 공급망, 정책 규제, 제조품질, IT·OT 보안, 자연재해, KRI, 선행지표, 규제, 리콜, NHTSA, 안전, 정책, 조기경보, 공개사건]
related: [RISK-D15-01, RISK-D15-02, RISK-D15-03, RISK-D15-04, RISK-D15-05, RISK-D15-06, RISK-D15-07, RISK-D15-08, RISK-D15-09, RISK-D15-10, RISK-D15-11, RISK-D15-12, EVT-D15-SKBA-2023-01, EVT-D15-LGES-EQ22-001, EVT-D15-BOSK-2026, EVT-D15-US-POLICY-2025, EVT-D15-EU-DATA-2027, EVT-D15-CYBER-CONTROL, EVT-D15-SHE-BASELINE, EVT-D15-INDUSTRY-FIRE]
priority: critical
domain: D15
section: D15-02
source: SK온_D15_Enterprise_Risk_Quality_Safety_Resilience.md
breadcrumb: "SK온 D15 — Enterprise Risk, Quality, Safety & Resilience"
tokens: 1587
updated: 2026-08-03
---

> SK온 · D15 전사 리스크·품질·안전·회복탄력성 · SK온 D15 — Enterprise Risk, Quality, Safety & Resilience

## D15-02 Enterprise Risk Taxonomy & Public Signal Register

### 1. 전사 Risk Taxonomy

| Risk ID | 범주 | 대표 Exposure | 선행 KRI 예시 | 주요 연결 |
|---|---|---|---|---|
| `RISK-D15-01` | 제품품질·필드안전 | Cell–Pack–Vehicle/ESS | defect escape, complaint rate, field anomaly | D03·D04·D06·D09 |
| `RISK-D15-02` | 제조품질·Ramp | Line·공정·검사·변경 | FPY drift, hold aging, Cpk, change backlog | D06·D07·D11 |
| `RISK-D15-03` | 공장 SHE | 화학물질·고전압·화재·분진·중량물 | near miss, barrier impairment, overdue action | D06·D07·D14 |
| `RISK-D15-04` | 공급망·원산지 | 광산~소재~물류~Lot | single-source exposure, late delivery, evidence gap | D08·D14 |
| `RISK-D15-05` | 고객·수요·집중 | OEM·Program·ESS Project | forecast revision, call-off variance, concentration | D09·D10 |
| `RISK-D15-06` | 가동률·원가·현금 | 공장·Program·CAPEX | utilization gap, cash burn, cost-to-complete | D11·D12 |
| `RISK-D15-07` | 계약·JV·상대방 | JV·License·Offtake·보증 | covenant breach, dispute, capital-call stress | D12·D13 |
| `RISK-D15-08` | 정책·규제·시장접근 | 법인·제품·거래 | rule change, eligibility exception, audit gap | D14 |
| `RISK-D15-09` | IT·OT·데이터·IP | MES·PLC·BMS·Cloud·R&D | unpatched asset, privileged access, model drift | D05·D06 |
| `RISK-D15-10` | 기후·자연재해·Utility | 공장·Supplier·물류 Corridor | heat/flood/drought, grid outage, water stress | D07·D08 |
| `RISK-D15-11` | 인력·조직·안전문화 | 신공장·교대·협력사 | turnover, training gap, fatigue, contractor exposure | D01·D07 |
| `RISK-D15-12` | 평판·이해관계자 | 고객·지역사회·정부·투자자 | complaint velocity, media escalation, trust index | D01·D09·D14 |

### 2. Public Signal Register

| Event ID | 공개 사실 | 상태·범위 | D15 해석 |
|---|---|---|---|
| `EVT-D15-SKBA-2023-01` | NHTSA 23V-168은 2023 F-150 BEV 18대의 고전압 Cell 제조편차와 내부단락·화재 가능성을 보고했고 공급사를 SK Battery America로 명시 | 역사적 리콜; 2023-01-20~26 생산차량, Pack 교체 | 숨길 사건이 아니라 Genealogy·Narrow Population·공정편차·CAPA 효과검증의 기준사례 ([NHTSA 23V-168](https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V168-8458.PDF)) |
| `EVT-D15-LGES-EQ22-001` | NHTSA는 여러 OEM의 LGES 고전압 Battery Failure를 묶어 Equipment Query 개시 | 외부 산업사례; 138,324 Population | 같은 Cell/유사 설비가 여러 OEM·공장으로 퍼질 때 Cross-customer·Cross-plant Common Cause 탐지가 필요 ([NHTSA EQ22-001](https://static.nhtsa.gov/odi/inv/2022/INOA-EQ22001-7596.PDF)) |
| `EVT-D15-BOSK-2026` | BlueOval SK 구조조정으로 Kentucky와 Tennessee 자산·부채·의무가 재배분 | 2026 구조변경; D12·D13 원본 | 품질기록·보증·인력·보험·IT·규제 Evidence의 Separation Continuity가 재무분리만큼 중요 |
| `EVT-D15-US-POLICY-2025` | 미국 30D 종료와 45X PFE/MACR 신설·강화가 수요와 생산수익에 다른 방향으로 작용 | 현재 정책 Event; D14 원본 | 시장·공장·현금 Risk를 하나의 정책점수로 합치지 않고 전파경로별 Stress Test 필요 |
| `EVT-D15-EU-DATA-2027` | EU Battery Passport와 공급망 실사 일정이 제품·공급망 Data 의무를 확대 | 미래 시행; D14 원본 | Data completeness가 시장접근·고객승인·리콜범위와 동시에 연결 |
| `EVT-D15-CYBER-CONTROL` | SK이노베이션 계열은 ISO/IEC 27001·27701 기반 정보보호 체계와 PDCA를 공개 | 공개 통제기반; SK온 개별 OT Coverage는 미공개 | Enterprise ISMS를 Line·PLC·Historian·Vendor Remote Access의 OT Control로 검증 필요 ([SK이노베이션](https://www.skinnovation.com/esg/gov-security)) |
| `EVT-D15-SHE-BASELINE` | SK이노베이션은 CSO·Safety Committee·사업장별 SHE 체계와 2022년 314회 비상훈련을 공개 | 그룹 공개자료; 현재 SK온 Site별 수치로 복사 금지 | Drill 횟수보다 시나리오 Coverage·Barrier Failure·RTO·후속조치 종결률을 관리 ([ESG Report](https://www.skinnovation.com/files/sustainability/esg_report/2022%20SKI%20ESG%20Report_eng.pdf)) |
| `EVT-D15-INDUSTRY-FIRE` | NTSB는 고전압 배터리의 감전·열폭주·재점화와 Stranded Energy를 긴급대응 Risk로 확인 | 산업 Hazard | 사고종료가 아닌 이송·격리·보관·재점화 감시까지 Recovery Plan에 포함 ([NTSB SR-20-01](https://www.ntsb.gov/safety/safety-studies/Pages/HWY19SP002.aspx)) |

`EVT-D15-SKBA-2023-01`은 공개적으로 확인되는 SK온 관련 부정적 품질사건이다. 동시에 NHTSA 보고서는 Ford가 공급사 공정·정비기록과 Pack-to-Vehicle 추적을 사용해 18대의 특정 VIN까지 좁혔다고 명시한다. D15는 이 두 사실을 모두 보존하며, `리콜 발생=전체 제품 불량` 또는 `범위 축소=위험 해소` 중 어느 쪽으로도 과장하지 않는다.

---
