---
id: skes-d11-0-domain-boundary
title: Domain Boundary
summary: "LNG·발전·도시가스·재생에너지 등 E&S 사업의 손익과 현금흐름을 일관되게 분석하는 D11 도메인의 역할, 포함 범위, 타 도메인과의 관계, 데이터 검증 규칙을 정의한 기준 문서."
tags: [d11, cost, core-candidate, table, "xref:d02", "xref:d03", "xref:d06", "xref:d07"]
keywords: [원가·수익성 분석, EBIT/EBITDA, Unit Economics, Cost Driver, Cash Contribution, LNG 포트폴리오, 발전소 가동률, 재생에너지 PPA, Scenario Engine, O/I 경제성]
related: [ORG-SKI-ENS-CIC-000001, ORG-SKENS-LEGAL-000001]
priority: critical
domain: D11
section: 0
source: SK이노베이션E&S_D11_Cost_Profitability_and_Business_Economics.md
breadcrumb: ""
tokens: 1903
updated: 2026-08-06
---

> SK이노베이션 E&S · D11 원가·수익성·비즈니스 이코노믹스

# SK이노베이션 E&S AI Knowledge Database

## D11. Cost, Profitability & Business Economics｜원가·수익성·사업경제성

**Version 1.0 / 기준일: 2026년 8월 6일 / 상태: REPRESENTATIVE_COMPANY_DEEP_DB**

- Canonical target entity: `ORG-SKI-ENS-CIC-000001`
- Historical legal entity: `ORG-SKENS-LEGAL-000001`
- Economics namespace: `ECO-ENS-D11-*`
- Cost-driver namespace: `CST-ENS-D11-*`
- KPI namespace: `KPI-ENS-D11-*`
- Scenario namespace: `SCN-ENS-D11-*`
- Pain-point namespace: `PAIN-ENS-D11-*`
- O/I Seed namespace: `SEED-ENS-D11-*`
- Source namespace: `SRC-ENS-D11-*`
- 상속 도메인: `D02 Business Portfolio`, `D03 Products and Solutions`, `D06 Process and Operations`, `D07 Footprint`, `D08 Supply Chain`, `D09 Customers and Contracts`, `D10 Market Dynamics`
- 작성 목적: 공개 손익을 보존하면서 LNG·발전·도시가스·재생에너지/PPA·BESS·EV 충전·액화수소·CCS의 경제성을 동일한 원가·현금·위험 언어로 연결하고, D17에서 검증 가능한 O/I 과제를 생성

---

# 0. Domain Boundary

## 0.1 D11의 역할

D11은 재무제표 요약 문서가 아니다. D02~D10에서 확인한 사업·자산·공정·계약·시장 변수를 실제 손익과 현금으로 변환하는 경제성 계층이다.

```text
Asset / Contract / Customer / Market / Period
→ Physical volume and availability
→ Realized price and contractual settlement
→ Variable cost and fixed-cost absorption
→ Reliability·quality·carbon·working-capital leakage
→ Recurring EBIT / EBITDA / cash contribution / ROIC
→ Controllable driver and decision lever
→ Finance-verified O/I benefit
→ D17 opportunity recommendation
```

E&S의 핵심 경제성 질문은 `매출이 얼마인가`가 아니라 다음과 같다.

1. LNG 포트폴리오의 어느 공급·운송·터미널·발전 경로가 위험조정 마진을 만드는가?
2. 발전소의 가동률·열효율·정비·SMP가 동일 기간 손익으로 어떻게 연결되는가?
3. 도시가스의 계절 수요와 고객별 Cost-to-Serve를 어떻게 분리하는가?
4. PPA·BESS·충전·수소·CCS의 발표 규모가 실제 계약 현금흐름으로 전환될 확률은 얼마인가?
5. 개선 과제의 절감액이 회계상 절감·현금 절감·회피비용 중 무엇이며, 중복계상되지 않았는가?

## 0.2 포함 범위

| 포함 | 설명 |
|---|---|
| 공개 실적 기준선 | E&S 사업의 연간·분기 매출, 영업이익, 단순 영업이익률 |
| 반복이익 Bridge | 계절성·정비·가격·가동률·재고·일회성·개발비 구분 |
| 사업별 Unit Economics | LNG, 발전/CHP, 도시가스, 재생/PPA, BESS, EV 충전, 수소, CCS |
| 원가 Driver Tree | 조달·운송·연료·효율·정비·인력·품질·탄소·금융·운전자본 |
| 수익성 KPI | 물량·가격·원가·마진·현금·ROIC·위험조정 지표 |
| Scenario Engine | 가격·환율·수요·가동률·고장·지연·정책·금리 충격 |
| O/I 경제성 | Baseline, 투자비, 편익, 검증 방식, 중복방지, Scale-up Gate |
| D17 Handoff | 경제적 문제, 내부 데이터, 외부 파트너, PoC, 성공 KPI |

## 0.3 제외·후속 이관

| 제외 또는 원본 도메인 | D11 처리 방식 |
|---|---|
| 상세 공정·태그·고장모드 | D06 원본을 참조하고 경제적 영향만 조인 |
| 자산 소유권·사용권·명목능력 | D07 원본 유지; 소유자산과 계약권리를 합산하지 않음 |
| 공급계약·물류 Flow | D08 원본 유지; 가격·Take-or-pay 등 비공개 조항은 내부확인 |
| 고객·PPA·시장기관 관계 | D09 원본 유지; MOU를 수주나 확정수익으로 승격하지 않음 |
| 시장전망·경쟁사·가격신호 | D10 원본 유지; D11은 손익 전파경로만 계산 |
| CAPEX·조달·재무구조 상세 | D12에서 자산·프로젝트·자금원별 심화 |
| JV·계약상 경제적 귀속 | D13에서 권리·의무·보증·Exit 구조 확인 |
| 규제·보조금 적격성 | D14에서 법적 판정; D11은 조건부 Scenario만 사용 |
| 전사 Risk 원장 | D15에서 통합; D11은 Margin-at-Risk와 Cash-at-Risk 제공 |
| 외부 공급사 실사 | D16에서 후보·역량·보안·현장적합성 검증 |

## 0.4 Hard Guardrails

1. `SK이노베이션 연결`, `E&S 사업`, `E&S CIC`, `종속회사`, `JV`, `개별 프로젝트` 손익을 동일 Scope로 간주하지 않는다.
2. 2024년 11월 1일 합병 전 SK E&S 실적과 합병 후 E&S 사업 실적은 회계범위가 다를 수 있으므로 직접 시계열 비교 시 Scope Bridge가 필요하다.
3. 공시된 E&S 사업 매출·영업이익을 LNG·발전·도시가스·수소 등으로 임의 배분하지 않는다.
4. 명목용량을 실제 판매량·처리량·계약량으로 대체하지 않는다.
5. `발표`, `MOU`, `개발 Pipeline`, `FID`, `건설`, `운영`, `현금수취`를 구분한다.
6. Take-or-pay, use-or-pay, Tolling, PPA, 시장입찰 등 계약유형이 다르면 매출과 위험의 인식 방식을 분리한다.
7. EBITDA, EBIT, 프로젝트 현금흐름, 회계상 당기손익, Equity 배당을 섞지 않는다.
8. 공개되지 않은 LNG 도입가격, 발전소 Heat Rate, PPA 가격, KCE 프로젝트 매출, 수소 원가를 확정값으로 추정하지 않는다.
9. 절감액은 `회계상 실현`, `현금 실현`, `회피비용`, `잠재가치`로 구분한다.
10. O/I 효과는 재무조직의 Baseline 승인과 사후 검증 전까지 `HYPOTHESIS`다.
11. 안전·급전·입찰·정비·투자 의사결정은 Human Approval 없이 자동 실행하지 않는다.
12. D11은 투자권유·기업가치평가·내부 예산 또는 투자심의를 대체하지 않는다.

---
