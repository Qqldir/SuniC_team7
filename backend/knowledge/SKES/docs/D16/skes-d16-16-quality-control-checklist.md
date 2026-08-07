---
id: skes-d16-16-quality-control-checklist
title: Quality-Control Checklist
summary: "외부 기술 솔루션 도입 시 벤더 주장을 E&S 사업 조건과 분리하고, OT 시스템 아키텍처 안전성을 검증하며, 운영 통합 요구사항을 확인하는 품질 관리 체크리스트"
tags: [d16, ecosystem, "xref:d15", "xref:d17"]
keywords: [벤더평가, 외부기술검증, OT아키텍처, 데이터모델, ROI검증, 운영KPI, 시스템보안, 기술도입]
related: []
priority: normal
domain: D16
section: 16
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 528
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 16. Quality-Control Checklist

## 16.1 Factual QC

- [x] 벤더 product claim과 customer case를 분리
- [x] Dragon LNG의 약 $1M 공개효과를 E&S 기대효과로 전이하지 않음
- [x] RWE/Seeq 사례를 E&S GT 성능으로 일반화하지 않음
- [x] Shell/C3 AI의 10,000+ equipment 사례를 fleet-scale evidence로만 사용
- [x] Fluence 3~10% profitability 문구를 E&S ROI로 채택하지 않음
- [x] UL 9540A test를 실시간 fire prediction 솔루션으로 오인하지 않음
- [x] LH2 계측 기술자료의 정확도를 실제 E&S installed accuracy로 사용하지 않음
- [x] SLB 120+ CCUS project 경험을 독립 실적 검증으로 승격하지 않음
- [x] 외부 OT threat/solution 정보를 E&S 침해사건으로 기록하지 않음

## 16.2 Architecture QC

- [x] OT read-only/shadow/bounded-write 단계를 분리
- [x] safety/SIS/ESD와 optimization AI의 권한 경계 유지
- [x] canonical data model·source lineage·timestamp 포함
- [x] OEM-specific/multi-OEM/lock-in 조건 분리
- [x] model drift·rollback·audit log 요구 포함
- [x] cloud 가능성과 cloud 허용을 분리
- [x] vendor exit/data export 조건 포함

## 16.3 O/I QC

- [x] `D15 Pain→Technology→Vendor→Evidence→Fit→PoC→D17` 연결
- [x] 80개 Seed가 기술명 나열이 아니라 운영 KPI를 포함
- [x] Priority PoC 25개에 Stop Condition 포함
- [x] 내부 데이터 요청 50개 정의
- [x] ROI는 내부 baseline 없이 확정하지 않음
- [x] Legal/Tax/CISO/HSE/Operations 승인자를 우회하지 않음
- [x] D17에서 vendor endorsement가 아닌 과제 문제정의 중심으로 랭킹 가능

---
