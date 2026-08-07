---
id: skes-d12-10-capex-funding-pain-point-register
title: CAPEX / Funding Pain-Point Register
summary: "자본지출과 펀딩에서 발생하는 예산·계약·환율·보증·세금 관련 33개 문제점의 원인, 손실규모, 필요 데이터를 정리한 등록부."
tags: [d12, capex, table, "xref:d07", "xref:d17"]
keywords: [자본지출, 자금조달, 프로젝트파이낸스, 차입금관리, 환위험, 계약변경, 비용초과, 투자심사, 캐시플로우, 손상차손]
related: [PAIN-ENS-D12-0001, PAIN-ENS-D12-0002, PAIN-ENS-D12-0003, PAIN-ENS-D12-0004, PAIN-ENS-D12-0005, PAIN-ENS-D12-0006, PAIN-ENS-D12-0007, PAIN-ENS-D12-0008, PAIN-ENS-D12-0009, PAIN-ENS-D12-0010, PAIN-ENS-D12-0011, PAIN-ENS-D12-0012, PAIN-ENS-D12-0013, PAIN-ENS-D12-0014, PAIN-ENS-D12-0015, PAIN-ENS-D12-0016, PAIN-ENS-D12-0017, PAIN-ENS-D12-0018, PAIN-ENS-D12-0019, PAIN-ENS-D12-0020, PAIN-ENS-D12-0021, PAIN-ENS-D12-0022, PAIN-ENS-D12-0023, PAIN-ENS-D12-0024]
priority: normal
domain: D12
section: 10
source: SK이노베이션E&S_D12_CAPEX_Investment_Funding_and_Financial_Structure.md
breadcrumb: ""
tokens: 1202
updated: 2026-08-06
---

> SK이노베이션 E&S · D12 CAPEX·투자·자금조달

# 10. CAPEX / Funding Pain-Point Register

| ID | Pain Point | 원인 | 경제적 누수 | 필요한 데이터 |
|---|---|---|---|---|
| `PAIN-ENS-D12-0001` | 발표총액과 실제지급 혼합 | stage 미분리 | 투자과대/과소 | budget/PO/AP |
| `PAIN-ENS-D12-0002` | JV gross와 E&S share 혼합 | scope 오류 | exposure 왜곡 | equity-call ledger |
| `PAIN-ENS-D12-0003` | PF 한도와 잔액 혼합 | debt state 오류 | leverage 왜곡 | lender statement |
| `PAIN-ENS-D12-0004` | non-recourse 과신 | support clause 미가시성 | tail risk | finance docs |
| `PAIN-ENS-D12-0005` | 보증 분산관리 | entity silo | contingent liability | guarantee master |
| `PAIN-ENS-D12-0006` | change order 후행관리 | EPC 문서 비정형 | overrun | contract/RFI/CO |
| `PAIN-ENS-D12-0007` | EAC 업데이트 지연 | 시스템 분리 | 늦은 대응 | WBS progress |
| `PAIN-ENS-D12-0008` | 물리/원가진척 불일치 | EPC reporting | cash surprise | earned value |
| `PAIN-ENS-D12-0009` | 지연 현금효과 미산정 | schedule/finance silo | NPV 손실 | critical path |
| `PAIN-ENS-D12-0010` | FX exposure 뒤늦게 인식 | PO/treasury disconnect | 환차손 | currency schedule |
| `PAIN-ENS-D12-0011` | PF covenant 수기관리 | 계약문서 비정형 | breach risk | covenant terms |
| `PAIN-ENS-D12-0012` | 정책지원 단계 혼합 | award/cash 혼합 | liquidity 오류 | claim ledger |
| `PAIN-ENS-D12-0013` | clawback 조건 누락 | 법무/재무 silo | 반환위험 | clause evidence |
| `PAIN-ENS-D12-0014` | ITC 중복계상 | project/tax silo | 수익성 과대 | tax credit registry |
| `PAIN-ENS-D12-0015` | 자산/사용권 혼합 | D07 crosswalk 부족 | ROIC 왜곡 | rights master |
| `PAIN-ENS-D12-0016` | pipeline을 committed로 오인 | status master 부재 | capex 과대 | gate status |
| `PAIN-ENS-D12-0017` | 수소 capacity 중심 투자평가 | 판매 ramp 부족 | cash burn | sold kg |
| `PAIN-ENS-D12-0018` | BESS MW 중심 평가 | MWh/열화/노드 누락 | lifecycle margin 오류 | EMS/BMS |
| `PAIN-ENS-D12-0019` | 해상풍력 총MW 중심 | curtailment/PPA 누락 | DSCR 변동 | meter/settlement |
| `PAIN-ENS-D12-0020` | LNG 사용권 활용도 미가시성 | contract silo | use-or-pay leakage | slot/cargo |
| `PAIN-ENS-D12-0021` | 유지보수 CAPEX 우선순위 | risk value 부재 | 고장/과잉투자 | EAM+finance |
| `PAIN-ENS-D12-0022` | impairment 후행 | trigger 단절 | 늦은 구조조정 | forecast/carrying |
| `PAIN-ENS-D12-0023` | Exit cost 누락 | sunk cost bias | 잘못된 계속투자 | remediation |
| `PAIN-ENS-D12-0024` | 매각 후 권리 추적 부족 | legal/asset silo | 권리누락 | contract graph |
| `PAIN-ENS-D12-0025` | Portfolio liquidity silo | SPV별 관리 | 자금비효율 | 13-week cash |
| `PAIN-ENS-D12-0026` | refinance timing 비최적 | market/asset silo | 이자비용 | curves/covenant |
| `PAIN-ENS-D12-0027` | partner call 예측 부족 | JV reporting lag | cash surprise | JV forecast |
| `PAIN-ENS-D12-0028` | 보험과 위험가치 단절 | claim silo | 중복/공백 | policy/asset |
| `PAIN-ENS-D12-0029` | 디지털투자 효과 미검증 | benefit owner 없음 | 반복투자 | KPI baseline |
| `PAIN-ENS-D12-0030` | D17 과제 절감액 중복 | 공통 driver | portfolio 과대 | value lineage |
| `PAIN-ENS-D12-0031` | 내부 hurdle rate 버전혼선 | governance | 투자비교 불가 | policy version |
| `PAIN-ENS-D12-0032` | P50/P90 불확실성 미반영 | deterministic case | downside 과소 | probabilistic model |
| `PAIN-ENS-D12-0033` | vendor financing 누락 | procurement silo | funding stack 오류 | payment terms |
| `PAIN-ENS-D12-0034` | 세무/회계/현금 timing 혼합 | period mismatch | cash forecast 오류 | tax/accounting |
| `PAIN-ENS-D12-0035` | Post-investment review 부족 | 승인 후 추적단절 | 학습손실 | case vs actual |

---
