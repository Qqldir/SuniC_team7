---
id: skes-d07-1-evidence-claim-status-and-capacity-polic
title: "Evidence, Claim Status and Capacity Policy"
summary: "용량 데이터를 어떻게 분류하고 합산하는지, 그리고 실제 적용 시 어떤 주의사항이 있는지 규정하는 정책 문서"
tags: [d07, footprint, table]
keywords: [검증 상태, 용량 분류, DISCLOSED_FACT, 합산 규칙, NAMEPLATE_GROSS, 실제 생산량, 지분환산, ESS]
related: []
priority: normal
domain: D07
section: 1
source: SK이노베이션E&S_D07_Footprint_Plants_and_Capacity.md
breadcrumb: ""
tokens: 869
updated: 2026-08-06
---

> SK이노베이션 E&S · D07 터미널·발전소·배관 등 자산·용량

# 1. Evidence, Claim Status and Capacity Policy

## 1.1 Claim Status

| Code | 의미 | 저장 예시 |
|---|---|---|
| DISCLOSED_FACT | 회사·JV·공시·규제자료에서 직접 확인 | Paju 1,800MW |
| CALCULATED_FACT | 공개값을 단순 산술 변환 | 96MW × 51% = 48.96MW 지분환산 참고값 |
| STRUCTURAL_ANALYSIS | 공개사실 간 운영구조 분석 | 보령은 equity-exited, usage-right-retained |
| OI_HYPOTHESIS | 데이터 확보 후 검증할 개선가설 | BOG 예측으로 compressor cycling 감소 |
| UNDISCLOSED_GAP | 내부자료 없이는 확정 불가 | 탱크별 BOR, GT별 heat rate |

## 1.2 Capacity Type Vocabulary

| capacity_type | 정의 | 합산 규칙 |
|---|---|---|
| NAMEPLATE_GROSS | 자산 전체 명목능력 | 동일 자산 중복 레이어와 합산 금지 |
| EQUITY_ATTRIBUTABLE | 지분율을 곱한 분석 참고값 | 회사가 공시한 귀속능력과 구분 |
| CONTRACTED_RIGHT | tolling·사용·도입 계약권 | 소유능력으로 합산 금지 |
| ACTUAL_OUTPUT | 기준기간 실제 생산·판매 | nameplate와 직접 합산 금지 |
| OPERATING_PORTFOLIO | 운영 상태 프로젝트 합계 | 개별 프로젝트 포함관계 태깅 |
| OPERATING_AND_DEVELOPING | 운영과 개발의 혼합합계 | 운영능력으로 재분류 금지 |
| DEVELOPMENT_PIPELINE | 개발 후보·계획 합계 | 투자확정·COD로 해석 금지 |
| OAM_MANAGED | O&M 수탁 범위 | 소유·연결능력으로 합산 금지 |
| THERMAL_CAPACITY | 열 Gcal/h 또는 증기 t/h | 전력 MW와 합산 금지 |
| ENERGY_CAPACITY | ESS MWh | ESS MW와 합산 금지 |

## 1.3 Hard Guardrails

1. 보령 LNG터미널 총 처리능력 700만 톤/년과 E&S 계열 사용권 350만 톤/년은 별도 레코드다.
2. 2025년 지분 매각 이후 보령은 E&S 소유 자산으로 분류하지 않는다.
3. Freeport 220만 톤/년은 계약된 액화설비 사용권이지 실제 생산량이 아니다.
4. Barossa 130만 톤/년은 E&S가 장기 도입할 예정인 설명물량이며 Barossa 전체 생산능력과 다르다.
5. 재생에너지 3.5GW는 운영·개발 혼합값이고, 약 5GW는 pipeline이다.
6. KCE 623MW는 운영 포트폴리오 합계이고 8GW는 개발 파이프라인이다.
7. 인천 액화수소 3만 톤/년은 명목능력이지 실제 연간 생산량이 아니다.
8. EV-ready circuit는 설치된 충전 port로 계산하지 않는다.
9. O&M 관리능력은 E&S의 지분 소유능력으로 합산하지 않는다.
10. 계획 CCS·블루수소·VPP는 운영자산으로 표시하지 않는다.

---
