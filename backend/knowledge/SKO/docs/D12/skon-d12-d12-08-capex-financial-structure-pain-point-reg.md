---
id: skon-d12-d12-08-capex-financial-structure-pain-point-reg
title: CAPEX & Financial-Structure Pain-Point Register
summary: "공장 투자·부채·정책 지원 관련 데이터 혼동에서 비롯한 SK온의 14개 재무 위험을 ID, 우선순위, KPI로 정의하는 문서."
tags: [d12, capex, table]
keywords: [투자위험, 자금관리, 재무리스크, 공장건설, DOE, 손상회계, 고객수요, 현금흐름, 부채보증, 녹색금융, 부채 추적, 정책 지원금, 자산 손상, 현금 흐름, greenfield, JV, 보증, 투자 회수]
related: [PP-D12-01, PP-D12-02, PP-D12-03, PP-D12-04, PP-D12-05, PP-D12-06, PP-D12-07, PP-D12-08, PP-D12-09, PP-D12-10, PP-D12-11, PP-D12-12, PP-D12-13, PP-D12-14]
priority: normal
domain: D12
section: D12-08
source: SK온_D12_CAPEX_Investment_Funding_Financial_Structure.md
breadcrumb: "SK온 D12 — CAPEX, Investment, Funding & Financial Structure"
tokens: 830
updated: 2026-08-03
---

> SK온 · D12 CAPEX·투자·자금조달 · SK온 D12 — CAPEX, Investment, Funding & Financial Structure

## D12-08 CAPEX & Financial-Structure Pain-Point Register

| Pain Point ID | 문제 | 공개 근거·징후 | 내부 확인 KPI | 우선순위 |
|---|---|---|---|---|
| `PP-D12-01` | 공장 총투자와 SK온 귀속부담 혼합 | HSBMA 50억달러·50:50 발표 | gross-to-net exposure coverage | P0 |
| `PP-D12-02` | 대출한도와 실제 인출·차입금 혼동 | BOSK DOE 최대 96.3억달러 | committed/drawn/accounting balance | P0 |
| `PP-D12-03` | JV 해소 후 부채·보증·자산 Lineage 단절 | Kentucky 이전·Tennessee 잔존 | obligation transfer completeness | P0 |
| `PP-D12-04` | 그룹 연결과 SK온 가용현금 혼합 | 2025 연결현금 16.09조원 | entity-restricted cash | P0 |
| `PP-D12-05` | 투자비·일정·Ramp 데이터를 별도 관리 | 대규모 다지역 공장·전환 | EAC accuracy, schedule variance | P0 |
| `PP-D12-06` | 고객수요보다 CAPEX Commitment가 선행 | 북미 수요변화·BOSK 재편 | qualified demand / committed GWh | P0 |
| `PP-D12-07` | Brownfield 전환비용·재승인기간 불투명 | EV→ESS·제품형태 전환 필요 | conversion NPV, qualification months | P0 |
| `PP-D12-08` | 정책지원의 인식·현금·Clawback 혼동 | DOE·45X·주정부 Incentive | awarded-to-cash, clawback-at-risk | P0 |
| `PP-D12-09` | PRS·우선주·영구채의 경제적 비용 분산 | 2025 PRS·FI Exit 구조 | all-in funding cost, settlement VaR | P0 |
| `PP-D12-10` | Partner Capital Call·보증 Exposure 불투명 | 고객·모회사 연계자금 | unpaid call, guarantee headroom | P0 |
| `PP-D12-11` | 손상은 후행 회계 Event로만 관리 | 2025 SK온 관련 약 4.2조원 | impairment lead time | P0 |
| `PP-D12-12` | 매몰비용 편향으로 Exit 지연 | 대규모 Greenfield Asset | forward NPV vs exit value | P1 |
| `PP-D12-13` | 투자절감·현금절감·회피비용 중복 | Scope 축소·발주 지연·가격절감 | finance-verified cash benefit | P1 |
| `PP-D12-14` | Green Finance 적격자산과 실제 Use-of-Proceeds 연결 부족 | Framework는 공개, Instrument 배분은 별도 | allocation and impact coverage | P1 |

### 핵심 해석

SK온의 투자위험은 `공장을 많이 지었다`는 한 문장으로 설명되지 않는다. 고객수요·제품전환·정책·Ramp가 바뀌는 동안 **법인별 자산·부채·보증·지원금·미집행 CAPEX가 같은 속도로 재배치되지 않는 것**이 핵심이다. D17은 투자금액 Dashboard보다 `수요 Trigger → Stage Gate → 자금의무 → 합격 kWh 현금 → 전환·Exit`의 폐쇄루프를 우선해야 한다.

---
