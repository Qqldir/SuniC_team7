---
id: skes-d03-part-2-대표기업-심층-확장팩-확장-source-library와-증거-2
title: Part 2. 대표기업 심층 확장팩 — 확장 Source Library와 증거 규칙
summary: SK E&S의 신재생에너지·도시가스·수소·EV충전 등 주요 사업별 정보 출처 및 팩트 검증 기준
tags: [d03, product, table, "xref:d17"]
keywords: [Fact Class, 신재생에너지, 도시가스, 수소, EV충전, ESS, PPA, 신뢰도 등급]
related: [SRC-ENS-D03-0009, SRC-ENS-D03-0010, SRC-ENS-D03-0011, SRC-ENS-D03-0012, SRC-ENS-D03-0013, SRC-ENS-D03-0014, SRC-ENS-D03-0015, SRC-ENS-D03-0016, SRC-ENS-D03-0017, SRC-ENS-D03-0018, SRC-ENS-D03-0019, SRC-ENS-D03-0020, SRC-ENS-D03-0021, SRC-ENS-D03-0022]
priority: normal
domain: D03
section: ""
source: SK이노베이션E&S_D03_Products_and_Solutions_v2_보강본.md
breadcrumb: Part 2. 대표기업 심층 확장팩
tokens: 1501
updated: 2026-08-06
---

> SK이노베이션 E&S · D03 제품·솔루션 · Part 2. 대표기업 심층 확장팩

## 14. 확장 Source Library와 증거 규칙

### 14.1 Fact Class

| Fact Class | 의미 | 허용 예시 | D17 사용 규칙 |
|---|---|---|---|
| `DISCLOSED_FACT` | E&S·SK·자회사·계약 상대방이 공개한 사실 | 설비용량, 공급권역, 계약 체결, 제품 기능 | 직접 근거로 사용 |
| `CALCULATED_FACT` | 공개 수치로 계산한 값 | 비중, 단순 환산 | 계산식과 원수치 보존 |
| `STRUCTURAL_ANALYSIS` | 밸류체인·서비스 구조에서 도출한 분석 | 터미널 병목 후보, PPA 정산 데이터 흐름 | 분석임을 표시하고 내부 확인 |
| `OI_HYPOTHESIS` | 현업 인터뷰 전의 문제 가설 | 예지보전 필요, 배차 최적화 가능성 | D17 후보만 허용 |
| `UNDISCLOSED_GAP` | 공개되지 않은 핵심 정보 | 가격, 실제 가동률, 고객별 계약조건 | 숫자 추정 금지 |

### 14.2 확장 자료 등록부

| Source ID | Tier | 기준일/발표일 | 자료 | 검증 범위 | URL |
|---|---|---|---|---|---|
| `SRC-ENS-D03-0009` | S1B | 2025-05 | E&S Renewable Energy | 태양광 운영·개발 3.5GW, 약 5GW 파이프라인, 해상풍력 1단계 상업운전, 2·3단계 계획 | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=recycleenergy |
| `SRC-ENS-D03-0010` | S1B | Current | E&S City Gas | 7개 자회사·8개 권역·약 510만 가구·2023년 54억㎥·22.6% 점유율 | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=citygas |
| `SRC-ENS-D03-0011` | S1B | Current | E&S Energy Solution | Ensolve·ESS·VPP 검토·iPARKING·KCE 약 0.6GW | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=energysolution |
| `SRC-ENS-D03-0012` | S1B | Current | E&S Hydrogen Energy | 인천 액화수소 3만톤/년·5만㎡·전국 공급·블루수소 검토 | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=h2 |
| `SRC-ENS-D03-0013` | S1C | 2022-03-23 | EverCharge acquisition | 턴키 충전, 공동주택·Fleet, mesh network, 동적부하관리, 설치밀도 주장 | https://evercharge.com/blog/sk-e/ |
| `SRC-ENS-D03-0014` | S1C | 2022-12-13 | KCE MarketCapture | ERCOT용 AI/ML 자동입찰·5분 실시간 최적화·성과 리포팅 | https://keycaptureenergy.com/key-capture-energy-launches-powerful-ai-driven-energy-bidding-optimization-tool/ |
| `SRC-ENS-D03-0015` | S1C | 2025-01-07 | KCE Texas 200MW completion | 200MW 프로젝트·운영 포트폴리오 620MW 이상 | https://keycaptureenergy.com/key-capture-energy-completes-construction-and-itc-transfer-for-200mw-of-battery-energy-storage-in-texas/ |
| `SRC-ENS-D03-0016` | S1C | 2023-05-02 | BASF–SK E&S PPA term sheet | 2025년부터 20년, BASF 한국 전력수요 16%, 2045년까지 90만톤 감축 기대 | https://www.basf.com/hk/en/media/news-releases/kr/2023/05/basf-and-sk-e-s-sign-power-purchase-agreement-for-renewable-ener |
| `SRC-ENS-D03-0017` | S1C | 2022-03-22 | Amorepacific direct PPA | 국내 최초 직접 PPA, 5MW, 20년, 대전사업장 공급 계획 | https://www.asiae.co.kr/en/article/2022032210413322033 |
| `SRC-ENS-D03-0018` | S1B | Current | SK Group E&S profile | LNG 전 밸류체인·가스전·Freeport 터미널 사용권·도시가스 7개사 | https://eng.sk.com/companies/info/sk-e-s |
| `SRC-ENS-D03-0019` | S1B | 2025 | SK Group PassKey profile | 북미 EV 충전·ESS·소프트웨어 투자 플랫폼 | https://eng.sk.com/investments/info/new-york |
| `SRC-ENS-D03-0020` | S1C | 2023-03-02 | EverCharge–PassKey BESS partnership | 충전부지 전력제약 대응용 BESS·충전 통합 | https://www.businesswire.com/news/home/20230302005702/en/EverCharge-and-PassKey-Partner-to-Develop-Battery-Energy-Storage-Systems-to-Solve-for-Lack-of-Sufficient-Energy-at-EV-Charging-Locations |
| `SRC-ENS-D03-0021` | S2A | 2024-05-09 | Korea.net 인천 액화수소 | 연 3만톤 생산능력, 대규모 액화수소 인프라 | https://www.korea.net/NewsFocus/Sci-Tech/view?articleId=251172 |
| `SRC-ENS-D03-0022` | S1B | Current | E&S LNG Value Chain | upstream–liquefaction–shipping–terminal–power/heat·저탄소 LNG 계획 | https://www.skens.com/en/sk/content/view.do?cate=energy&m1=lngcondition |

### 14.3 출처 적용 제한

1. 같은 E&S 홈페이지라도 숫자의 기준일이 다르면 최신값으로 기계적 치환하지 않는다.
2. `운영 및 개발`, `pipeline`, `상업운전`을 서로 다른 상태값으로 저장한다.
3. 계약 상대방이 공개한 PPA 기간·비중은 해당 계약에만 적용한다.
4. 자회사 제품 기능은 E&S 전 계열 공통 기능으로 확장하지 않는다.
5. KCE·EverCharge의 북미 제품을 국내 E&S가 이미 판매하는 제품으로 표시하지 않는다.
6. 자회사·투자회사 발표 수치는 연결실적·지분귀속량과 구분한다.

---
