---
id: skes-d04-11-application-technology-data-crosswalk
title: Application–Technology–Data Crosswalk
summary: "SK이노베이션 E&S의 21개 에너지솔루션 애플리케이션별로 필수 기술, 핵심 데이터, 권고 아키텍처, 보유역량·외부필요 현황을 매핑한 마스터 표로서 각 앱 구축에 필요한 기술조합과 역량 구성을 한눈에 파악할 수 있다."
tags: [d04, technology, table]
keywords: [APP-ENS, 기술군, 데이터 매트릭스, 아키텍처, 역량 현황, LNG 포트폴리오, 선박터미널, 가스수요예측, ESS, DERMS]
related: [APP-ENS-001, APP-ENS-002, APP-ENS-003, APP-ENS-004, APP-ENS-005, APP-ENS-006, APP-ENS-007, APP-ENS-008, APP-ENS-009, APP-ENS-010, APP-ENS-011, APP-ENS-012, APP-ENS-013, APP-ENS-014, APP-ENS-015, APP-ENS-016, APP-ENS-017, APP-ENS-018, APP-ENS-019, APP-ENS-020, APP-ENS-021, APP-ENS-022, APP-ENS-023, APP-ENS-024]
priority: normal
domain: D04
section: 11
source: SK이노베이션E&S_D04_Technology_Taxonomy_v2_보강본.md
breadcrumb: Part 2. 대표기업 기술체계 심층 확장
tokens: 1375
updated: 2026-08-06
---

> SK이노베이션 E&S · D04 기술 분류체계·핵심기술 마스터 · Part 2. 대표기업 기술체계 심층 확장

## 11. Application–Technology–Data Crosswalk

| APP ID | 필수 기술군 | 핵심 데이터 | 권고 아키텍처 | 보유역량/외부필요 | 초기 Gate |
|---|---|---|---|---|---|
| `APP-ENS-001` LNG portfolio | 최적화·시나리오·설명 AI | 계약제약·수요·가격·일정 | secure data mart + solver | 내부 수급지식 핵심, 최적화 partner 가능 | 계약·거래통제 |
| `APP-ENS-002` vessel-terminal | ETA ML·schedule optimization | AIS·기상·berth·재고 | streaming ETA + constraint solver | 외부 AIS/기상 + 내부 운영 | 선박/터미널 권리 |
| `APP-ENS-003` BOG/inventory | process model·anomaly·optimizer | tank·cargo·BOG·send-out | historian + hybrid model | 공정 partner 가능 | 공정안전·OT |
| `APP-ENS-004` CCGT dispatch | heat-rate model·asset health·optimizer | 시장·연료·historian·CMMS | plant twin + dispatch DSS | OEM/내부/AI 결합 | 운전승인·LTSA |
| `APP-ENS-005` CHP | load forecast·multi-objective optimizer | 열수요·기상·가격·축열 | forecast + MPC/DSS | 외부 알고리즘 가능 | 열공급 신뢰도 |
| `APP-ENS-006` gas demand | 시계열·hierarchical forecast | 송출·기상·달력·고객군 | batch/stream forecast | 공통모델+자회사 보정 | 개인정보 최소화 |
| `APP-ENS-007` pipeline risk | geospatial ML·survival·risk scoring | GIS·점검·굴착·기상·사고 | spatial feature store + RBMS | RBMS 보유 공개, 보강 partner | 법정점검·설명 |
| `APP-ENS-008` excavation | GIS rule·vision AI·event detection | 허가·배관·드론/차량 영상 | geofence + edge/cloud vision | 드론 운영 공개, vision partner | 비행·영상보안 |
| `APP-ENS-009` meter OCR | OCR·anomaly·human review | 이미지·계량기·과거값 | mobile OCR + validation | 외부 OCR 가능 | 개인정보·청구정확성 |
| `APP-ENS-010` field routing | scheduling·routing·workflow | 예약·주소·기사·소요시간 | CRM/FSM + optimizer | FSM partner 가능 | 노동·현장안전 |
| `APP-ENS-011` solar | forecast·loss attribution·vision | 기상·SCADA·image·CMMS | RE data platform | 외부 forecast/vision | 자산별 권리 |
| `APP-ENS-012` offshore O&M | condition monitoring·weather window·routing | SCADA·파고·선박·부품 | O&M decision platform | 전문 vendor/partner | 해상안전 |
| `APP-ENS-013` PPA design | load/asset simulation·risk analytics | 부하·자산·가격·신용 | commercial scenario engine | E&S PPA 경험 + external analytics | 계약·신용 |
| `APP-ENS-014` PPA settlement | meter validation·rules engine·lineage | 계량·계약·시장·인증 | immutable lineage + workflow | 내부 rule + data platform | 회계·법무 |
| `APP-ENS-015` LH2 plant | hybrid process model·predictive maintenance | feed·process·power·trip | OT historian + advisory model | OEM/공정 partner | 극저온안전 |
| `APP-ENS-016` H2 logistics | demand forecast·inventory routing | 생산·탱크·차량·충전소 | supply-chain digital twin | 외부 최적화 + 내부 운영 | 위험물·비상 |
| `APP-ENS-017` demand ESS | load forecast·MPC·degradation | 부하·요금·SOC/SOH·생산 | site EMS | 기존 ESS + optimizer | 배터리안전 |
| `APP-ENS-018` RE ESS | forecast·dispatch·degradation | 발전·제약·PPA/시장·SOH | renewable+ESS EMS | E&S/KCE 경험 재사용 | 계통·보증 |
| `APP-ENS-019` grid ESS bid | price forecast·RL/optimization·MLOps | 시장·asset·bid·dispatch | MarketCapture | KCE 보유역량 우선 | 시장규칙·IP |
| `APP-ENS-020` DERMS | network model·state estimate·DER control | topology·AMI·SCADA·DER | DERMS/ADMS integration | Ensolve 기반 추진 | 사이버·제어권한 |
| `APP-ENS-021` VPP | onboarding·baseline·forecast·settlement | DER·meter·market·consent | minimum VPP platform | 검토단계, partner 가능 | 동의·규제·경제성 |
| `APP-ENS-022` RE O&M | anomaly·vision·CMMS optimization | SCADA·image·work order | fleet O&M platform | 계획단계, vendor 가능 | 드론·보증 |
| `APP-ENS-023` smart charging | dynamic load·session forecast·mesh | charger·vehicle·building | EverCharge SmartPower | 보유역량 재사용 | 결제·개인정보 |
| `APP-ENS-024` charging+BESS | site forecast·EMS·sizing optimizer | building·charging·ESS·tariff | site energy orchestrator | EverCharge+PassKey 공개협력 | 화재·전기안전 |
| `APP-ENS-025` CCS MRV | meter QA·mass balance·lineage·anomaly | CO2 meter·lab·custody·storage | MRV data platform | 외부 전문 partner | 국제규제·책임 |
