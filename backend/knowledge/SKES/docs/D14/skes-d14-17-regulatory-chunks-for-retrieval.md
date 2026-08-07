---
id: skes-d14-17-regulatory-chunks-for-retrieval
title: Regulatory Chunks for Retrieval
summary: "K-ETS, 청정수소, 미국 세액공제, 배터리 저장 등 주요 에너지·환경 규제의 적용 기준·기한·조건을 국가별로 정리한 규제 정책 참고 자료."
tags: [d14, policy, "xref:d11", "xref:d17", "xref:d07"]
keywords: [K-ETS Phase 4, 청정수소 경매, 48E 세액공제, 시장안정화예비분, BESS 시장 참여, 호주 Safeguard, PFE 공급망, Vietnam LNG, 탄소배출권거래, 규제 기한]
related: []
priority: normal
domain: D14
section: 17
source: SK이노베이션E&S_D14_Policy_Regulation_Incentives_and_Compliance.md
breadcrumb: ""
tokens: 1787
updated: 2026-08-06
---

> SK이노베이션 E&S · D14 정책·규제·인센티브·컴플라이언스

# 17. Regulatory Chunks for Retrieval

## CHUNK-ENS-D14-0001｜K-ETS Phase 4

2026~2030 제4차 계획기간에서 발전부문 유상할당은 2026년 15%, 2027년 20%, 2028년 30%, 2029년 40%, 2030년 50%로 단계 상승한다. E&S LNG 발전·CHP는 이 경로를 D11 spark-spread/heat economics에 반영하되, 전국 발전부문 할당량을 E&S 몫으로 비례배분하지 않는다.

## CHUNK-ENS-D14-0002｜K-MSR

제4기 K-ETS에는 시장안정화예비분이 도입됐다. 배출권 시장의 가격 또는 수량이 설정기준을 벗어날 때 경매 공급량 조정에 사용할 수 있으므로 Treasury의 KAU 조달은 단순 고정가격 예산이 아니라 auction state와 reserve intervention을 추적해야 한다.

## CHUNK-ENS-D14-0003｜Hydrogen auction state

KPX가 2025-05-09 청정수소발전시장 경쟁입찰을 공고했으나 2025-10-17 취소했다. 따라서 해당 round는 낙찰수요·장기매출·확정 hydrogen demand로 집계할 수 없다. 이후 신규 공고가 있을 때 새 event/auction ID로 생성해야 한다.

## CHUNK-ENS-D14-0004｜Hydrogen law future change

기준일 2026-08-06 현재 수소법 시행령의 청정수소 인증체계가 효력 중이다. 2026-03-17 공포된 추가 개정법은 2026-09-18 시행 예정이며 등급별 청정수소 인증과 생산·수입·판매량 및 구매자 신고 등 변화가 포함된다. D14은 이를 현재 의무가 아닌 ENACTED_FUTURE로 관리한다.

## CHUNK-ENS-D14-0005｜48E for KCE

미국 48E Clean Electricity Investment Credit은 2024-12-31 이후 placed in service된 energy storage technology에 적용 가능하다. IRS 기준 기본액 6%, PWA 충족 시 5배 구조가 존재하지만 KCE 각 프로젝트는 qualified basis, PIS, PWA, domestic content, energy community, PFE 조건을 개별 검증한 후 실제 수령액을 확정해야 한다.

## CHUNK-ENS-D14-0006｜PFE supply-chain gate

2025 OBBBA 이후 특정 청정에너지 세액공제에는 prohibited foreign entity의 material assistance 관련 제한이 추가됐다. KCE는 배터리 셀·모듈·PCS 등 BOM뿐 아니라 vendor ownership과 공급계약을 tax eligibility와 연결해야 하며, 단순 제조국가 필드만으로 판정하면 안 된다.

## CHUNK-ENS-D14-0007｜EverCharge 30C cutoff

IRS OBBBA FAQ에 따르면 alternative fuel vehicle refueling property credit 30C는 2026-06-30 이후 placed in service된 property에는 허용되지 않는다. EverCharge의 신규 고객 ROI 계산기는 과거 incentive assumption을 자동으로 상속하지 말고 site별 PIS date를 기준으로 판단해야 한다.

## CHUNK-ENS-D14-0008｜NY/ERCOT BESS market compliance

FERC Order 841은 organized wholesale market에서 storage의 capacity·energy·ancillary service 참여 장벽을 제거하는 기반이다. 실제 KCE 운영은 NYISO와 ERCOT의 현재 tariff/protocol, resource registration, interconnection, telemetry, capacity accreditation을 project별로 적용해야 한다.

## CHUNK-ENS-D14-0009｜Australia Safeguard

호주 Safeguard Mechanism은 일반적으로 연 100,000tCO2-e 초과 산업시설에 적용되고 baseline은 2030년까지 통상 연 4.9% 감소한다. 법적 책임은 operational control을 가진 사업자가 부담하므로 Barossa/Darwin의 E&S 경제적 지분율과 compliance entity를 동일시하지 않는다.

## CHUNK-ENS-D14-0010｜Quynh Lap regulatory clock

Vietnam MOIT는 LNG 발전사업이 Decree 56/2025 및 100/2025의 관련 메커니즘을 적용받으려면 2031-01-01 전에 운영에 들어가야 한다고 명시했다. Quynh Lap의 2030 목표는 따라서 permit/EPC/PPA 지연확률과 결합해 economic cliff로 모델링해야 하며, 개발자 선정이나 PDP 포함을 COD로 간주하지 않는다.

## CHUNK-ENS-D14-0011｜Regulatory AI

규제 AI의 답은 최신 법령만 잘 검색한다고 끝나지 않는다. 법적주체·자산·관할·행위·기준일을 먼저 식별하고 그 날짜에 효력이 있는 rule version만 검색해야 한다. 근거 URL과 applicability 조건이 없으면 자동 의사결정 또는 공식 제출에 사용하지 않는다.

## CHUNK-ENS-D14-0012｜D17 gate

D14의 목적은 규제 아이디어를 늘리는 것이 아니라 D17에서 실행 가능한 O/I 과제를 거르는 것이다. 각 Seed는 `rule source → applicable entity/asset → data right → safety/privacy/cyber → economic KPI → human owner`를 통과해야 PoC로 승격한다.

---

# 18. Quality-Control Checklist

## 18.1 Temporal QC

- [x] 기준일 2026-08-06 명시
- [x] 2026-09-18 수소법 개정은 future로 분리
- [x] 2025 청정수소 입찰은 cancelled로 분리
- [x] 2026-06-30 30C cutoff 반영
- [x] K-ETS 연도별 유상할당 비율 분리
- [x] Vietnam 2031-01-01 deadline을 future milestone로 분리

## 18.2 Scope QC

- [x] SK그룹/통합법인/E&S CIC/자회사/JV/SPV 법적경계 유지
- [x] 한국/미국/호주/베트남 관할 분리
- [x] 운영자산·개발자산·사용권 분리
- [x] policy target·permit·auction·award·received 분리
- [x] statutory tax rate와 realized cash benefit 분리
- [x] asset ID는 D07 canonical IDs 사용

## 18.3 D17 Readiness

- [x] Risk→Pain→Seed 연결 가능
- [x] 60 O/I Seed 제공
- [x] 우선 PoC 15개 선정
- [x] 내부 데이터 요청 35개 정의
- [x] Legal/Tax/EHS/CISO Gate 포함
- [x] 공식 출처 중심 source registry 구성

---
