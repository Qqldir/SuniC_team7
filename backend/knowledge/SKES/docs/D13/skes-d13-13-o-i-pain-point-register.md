---
id: skes-d13-13-o-i-pain-point-register
title: O/I Pain Point Register
summary: "SK이노베이션 E&S D13 JV 운영 중 계약관리·거버넌스·재무에서 발생하는 35개 주요 이슈의 원인과 영향도, 우선순위 정리"
tags: [d13, contract, table, "xref:d17"]
keywords: [계약관리, 거버넌스, 합작투자, JV, 데이터 통합, 운영통제, 재무위험, 의사결정 지연]
related: [PAIN-ENS-D13-0001, PAIN-ENS-D13-0002, PAIN-ENS-D13-0003, PAIN-ENS-D13-0004, PAIN-ENS-D13-0005, PAIN-ENS-D13-0006, PAIN-ENS-D13-0007, PAIN-ENS-D13-0008, PAIN-ENS-D13-0009, PAIN-ENS-D13-0010, PAIN-ENS-D13-0011, PAIN-ENS-D13-0012, PAIN-ENS-D13-0013, PAIN-ENS-D13-0014, PAIN-ENS-D13-0015, PAIN-ENS-D13-0016, PAIN-ENS-D13-0017, PAIN-ENS-D13-0018, PAIN-ENS-D13-0019, PAIN-ENS-D13-0020, PAIN-ENS-D13-0021, PAIN-ENS-D13-0022, PAIN-ENS-D13-0023, PAIN-ENS-D13-0024]
priority: normal
domain: D13
section: 13
source: SK이노베이션E&S_D13_JV_Partnerships_Contracts_and_Governance.md
breadcrumb: ""
tokens: 1252
updated: 2026-08-06
---

> SK이노베이션 E&S · D13 JV·파트너십·계약·거버넌스

# 13. O/I Pain Point Register

| ID | Pain Point | Root cause | Business impact | Priority |
|---|---|---|---|---|
| `PAIN-ENS-D13-0001` | 법인명과 브랜드명 혼용 | entity master 단절 | 계약검색 누락 | P0 |
| `PAIN-ENS-D13-0002` | 합병 전후 계약승계 불투명 | successor ledger 없음 | 권리/보증 누락 | P0 |
| `PAIN-ENS-D13-0003` | JV 지분을 통제권으로 오인 | governance clause 비정형 | 승인오류 | P0 |
| `PAIN-ENS-D13-0004` | Reserved Matter 검색 어려움 | 계약별 표현 상이 | 의사결정 지연 | P0 |
| `PAIN-ENS-D13-0005` | Board/committee 권한 최신성 부족 | 조직/위임 변경 | 잘못된 승인경로 | P0 |
| `PAIN-ENS-D13-0006` | cash call 사전예측 부족 | 운영계획-재무 분리 | 유동성 변동 | P0 |
| `PAIN-ENS-D13-0007` | 보증·Sponsor Support 분산 | 법무/재무 원장 분리 | contingent exposure | P0 |
| `PAIN-ENS-D13-0008` | 사용권과 소유권 혼동 | asset/right 동일 키 | 가치/위험 왜곡 | P0 |
| `PAIN-ENS-D13-0009` | TUA/LTA 의무와 실제 사용 단절 | contract-ops 미연계 | idle fee | P0 |
| `PAIN-ENS-D13-0010` | JV lifting·cargo 정산 수작업 | multi-party data | mismatch/claim | P0 |
| `PAIN-ENS-D13-0011` | 계약변경이 운영에 늦게 반영 | amendment propagation 부족 | SLA/가격 오류 | P0 |
| `PAIN-ENS-D13-0012` | side letter/waiver 추적 어려움 | 저장소 분산 | 예외 누락 | P1 |
| `PAIN-ENS-D13-0013` | claim notice deadline 누락 위험 | 비정형 clause | 회수권 상실 | P0 |
| `PAIN-ENS-D13-0014` | 보험·indemnity 연결 부족 | policy/contract 분리 | 손실회수 지연 | P1 |
| `PAIN-ENS-D13-0015` | PPA 조항과 meter 정산 분리 | CLM/계량 단절 | leakage | P0 |
| `PAIN-ENS-D13-0016` | REC 증빙 lineage 부족 | certificate silo | audit risk | P0 |
| `PAIN-ENS-D13-0017` | 풍력 PF consent 수작업 | covenant 비정형 | 승인 누락 | P1 |
| `PAIN-ENS-D13-0018` | 주민참여 정산 복잡 | beneficiary/rule 분리 | 민원/오류 | P1 |
| `PAIN-ENS-D13-0019` | KCE 프로젝트별 계약구조 상이 | portfolio 표준화 한계 | 비교 어려움 | P0 |
| `PAIN-ENS-D13-0020` | BESS warranty와 dispatch 분리 | warranty/BMS/market silo | lifecycle value 하락 | P0 |
| `PAIN-ENS-D13-0021` | vendor LTSA 성과비교 부족 | SLA 정의 상이 | O&M cost | P1 |
| `PAIN-ENS-D13-0022` | EverCharge site data 권리 불명확 | host/customer/driver 다층 | AI PoC 제약 | P0 |
| `PAIN-ENS-D13-0023` | Hyverse 지분변동 최신화 지연 | 공개원장 시차/충돌 | 잘못된 governance | P0 |
| `PAIN-ENS-D13-0024` | 기술계약 존속범위 불명확 | equity exit와 license 혼동 | 공급/서비스 위험 | P0 |
| `PAIN-ENS-D13-0025` | H2 MOU가 확정사업처럼 보임 | commitment taxonomy 부족 | CAPEX 과대 | P0 |
| `PAIN-ENS-D13-0026` | 충전소·차량·연료계약 단계 단절 | ecosystem owner 분산 | 수요예측 오류 | P0 |
| `PAIN-ENS-D13-0027` | Quynh Lap CP 다기관 관리 | cross-border approval | 일정지연 | P0 |
| `PAIN-ENS-D13-0028` | EPC digital handover 뒤늦음 | 계약단계 requirement 부족 | 운영데이터 품질 | P0 |
| `PAIN-ENS-D13-0029` | 해외 JV data residency 불명확 | jurisdiction 차이 | analytics 제한 | P0 |
| `PAIN-ENS-D13-0030` | 파트너 실사 반복 | KYC/DD 자료 재수집 | lead time | P1 |
| `PAIN-ENS-D13-0031` | 동일 파트너 중복 master | 사업부별 vendor/customer ID | exposure 누락 | P0 |
| `PAIN-ENS-D13-0032` | 계약 KPI 정의 불일치 | 문서별 단위/기간 상이 | dashboard 왜곡 | P1 |
| `PAIN-ENS-D13-0033` | 비공개 계약 AI 활용 제약 | 접근권/보안 | 검색 생산성 | P0 |
| `PAIN-ENS-D13-0034` | 법무 검토 흔적 부족 | reviewer audit trail 부족 | AI 신뢰성 | P0 |
| `PAIN-ENS-D13-0035` | D17 과제 효과와 계약권리 단절 | solution-first 기획 | 실행불가 PoC | P0 |

---
