# SK온 지식 베이스 스키마

## 도메인 코드

| 코드 | 주제 | 태그 | 문서 |
|---|---|---|---|
| `D00` | 소스·엔티티·ID·변경이력 마스터 | `governance` | 14 |
| `D01` | 기업 기본정보·법인구조·연혁 | `identity` | 18 |
| `D02` | 사업 포트폴리오 | `business` | 20 |
| `D03` | 제품·솔루션 | `product` | 90 |
| `D04` | 기술 분류체계·핵심기술 마스터 | `technology` | 98 |
| `D05` | R&D·특허·지식재산 | `rnd` | 138 |
| `D06` | 제조공정·운영 | `process` | 106 |
| `D07` | 생산거점·캐파 | `footprint` | 70 |
| `D08` | 원소재·공급사·공급망 | `supply-chain` | 67 |
| `D09` | 고객·수주·OEM 관계 | `customer` | 10 |
| `D10` | 시장·경쟁·산업동향 | `market` | 11 |
| `D11` | 원가·수익성·비즈니스 이코노믹스 | `cost` | 13 |
| `D12` | CAPEX·투자·자금조달 | `capex` | 14 |
| `D13` | 계약·JV·거버넌스·파트너십 | `contract` | 14 |
| `D14` | 정책·규제·인센티브·컴플라이언스 | `policy` | 16 |
| `D15` | 전사 리스크·품질·안전·회복탄력성 | `risk` | 15 |
| `D16` | 외부 솔루션·스타트업·벤더 생태계 | `ecosystem` | 15 |
| `D17` | 오픈이노베이션 과제 포트폴리오·AI 추천 | `oi-portfolio` | 13 |

## 문서 id 규칙

`skon-{도메인}-{절번호}-{제목슬러그}` — 예: `skon-d08-d08-12-우선-o-i-후보-15개`.
id 는 파일명과 일치하며, 인덱스나 검색 결과에 없는 id 는 존재하지 않는다.

## 선반

| 선반 | 내용 | 언제 |
|---|---|---|
| `seeds/` | 도메인별 O/I 과제 후보, D17 최종 포트폴리오 60건 | 과제 발굴 |
| `docs/` | 도메인 본문 (공정·원가·계약·규제 등) | 근거 확인 |

## 태그 어휘

`build-log` `business` `capex` `contract` `core-candidate` `cost` `customer` `d00` `d01` `d02` `d03` `d04` `d05` `d06` `d07` `d08` `d09` `d10` `d11` `d12` `d13` `d14` `d15` `d16` `d17` `ecosystem` `footprint` `governance` `identity` `market` `oi-portfolio` `oi-seed` `policy` `process` `product` `risk` `rnd` `schema` `supply-chain` `table` `technology`

`xref:d##` 태그는 그 문서가 다른 도메인을 참조한다는 뜻이다.
