---
id: skes-d09-8-city-gas-customer-and-service-journey
title: City-Gas Customer and Service Journey
summary: 도시가스 고객의 신규가입부터 해지까지 12개 단계 여정에서의 의사결정·Pain Point·KPI와 수요예측 및 프라이버시 관리 전략
tags: [d09, customer, table]
keywords: [고객여정, 수요예측, Pain Point, KPI, 검침, 요금청구, 취약고객, 프라이버시, AMI, DSM]
related: []
priority: normal
domain: D09
section: 8
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 1048
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 8. City-Gas Customer and Service Journey

## 8.1 Portfolio Boundary

- 공개 포트폴리오 스냅샷: 7개 도시가스사, 8개 권역, 약 510만 가구, 2023년 약 54억㎥, 시장점유율 22.6%.
- 개별 자회사 고객 수의 기준일이 다르므로 합산 검산이 필요하다.
- 산업용 대량고객은 수가 적어도 판매량·마진·수요변동 영향이 크다.
- 가정용 고객은 건당 사용량은 작지만 서비스·결제·개인정보·안전 event가 대량 발생한다.

## 8.2 Customer Journey

| Journey | 입력 | 현재 의사결정 | 대표 Pain Point | 핵심 KPI |
|---|---|---|---|---|
| 공급가능 조회 | 주소·공급관·공사계획 | 가능/불가·예정 | GIS 불일치·반복문의 | 자동판정률 |
| 신규 공급신청 | 건물·사용량·공사 | 투자·공사·분담 | 장기 대기·서류누락 | lead time |
| 전입 | 주소·계량기·일정 | 개통·안전점검 | 방문 부재 | first-time success |
| 전출 | 최종검침·정산 | 차단·환불 | 검침오류 | same-day closure |
| 검침 | 계량값·사진·AMI | 사용량 확정 | 접근불가·오검침 | read accuracy |
| 청구 | 사용량·요금·세금 | 고지 | 이상요금·설명부족 | bill accuracy |
| 납부 | 계좌·카드·연체 | 수납·독촉 | 이중납부·체납 | collection rate |
| 요금상담 | 청구·사용패턴 | 설명·조정 | 반복호출 | FCR |
| 안전신고 | 냄새·압력·위치 | 긴급출동 | 위치·심각도 오분류 | arrival time |
| 기기교체 | 계량기·조정기 이력 | 교체 우선순위 | 자산·고객정보 분리 | repeat visit |
| 취약고객 | 사용·체납·복지자격 | 지원안내 | 과도한 프로파일링 | 적정지원률 |
| 해지/churn | 전출·연료전환 | 관계종료 | 사유코드 부재 | avoidable churn |

## 8.3 Demand Segmentation

| Segment | Forecast driver | Granularity | O/I use |
|---|---|---|---|
| 가정 난방 | HDD·주거형태·요일 | 권역/시간 | cold-wave forecast |
| 취사 | 가구·시간대 | 권역/시간 | baseline separation |
| 상업 | 영업시간·업종·날씨 | 계량점/일 | anomaly and tariff |
| 업무 | 근무일·면적·냉난방 | 건물/시간 | DSM |
| 산업 | 생산계획·공정·가격 | 고객/시간 | account forecast |
| 열병합 | 전력·열 dispatch | site/시간 | integrated dispatch |
| 연료전지 | 가동률·정비 | unit/시간 | fuel nomination |
| 수송 | 차량·충전소 | station/시간 | capacity planning |

## 8.4 Privacy-by-Design

1. 가정 고객은 주소·전화번호 대신 가명 `service_point_id`로 분석한다.
2. 안전출동 모델은 긴급 대응 목적과 요금마케팅 목적 데이터를 분리한다.
3. 체납 예측은 취약계층 차별·자동차단에 사용하지 않고 상담 우선순위 추천으로 제한한다.
4. 고객상담 음성은 동의·보유기간·접근권한을 확인하고 민감정보를 마스킹한다.
5. AMI 시계열은 생활패턴 추론 가능성이 있으므로 최소해상도·최소기간 원칙을 둔다.

---
