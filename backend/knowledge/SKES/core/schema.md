# SK이노베이션 E&S 지식 베이스 스키마

## 도메인 코드

| 코드 | 주제 | 태그 | 문서 |
|---|---|---|---|
| `D00` | 소스·엔티티·ID·변경이력 마스터 | `governance` | 9 |
| `D01` | 기업 기본정보·법인구조·연혁 | `identity` | 17 |
| `D02` | 사업 포트폴리오 | `business` | 12 |
| `D03` | 제품·솔루션 | `product` | 33 |
| `D04` | 기술 분류체계·핵심기술 마스터 | `technology` | 26 |
| `D05` | R&D·특허·지식재산 | `rnd` | 23 |
| `D06` | 운영 프로세스·밸류체인 운전 | `process` | 28 |
| `D07` | 터미널·발전소·배관 등 자산·용량 | `footprint` | 18 |
| `D08` | 공급망·조달·설비·물류 | `supply-chain` | 24 |
| `D09` | 고객·수요·계약·Offtake | `customer` | 24 |
| `D10` | 시장·경쟁·산업동향 | `market` | 24 |
| `D11` | 원가·수익성·비즈니스 이코노믹스 | `cost` | 22 |
| `D12` | CAPEX·투자·자금조달 | `capex` | 15 |
| `D13` | JV·파트너십·계약·거버넌스 | `contract` | 21 |
| `D14` | 정책·규제·인센티브·컴플라이언스 | `policy` | 19 |
| `D15` | 리스크·실패모드·회복탄력성 | `risk` | 24 |
| `D16` | 외부 기술·솔루션·기업·스타트업 | `ecosystem` | 17 |
| `D17` | 오픈이노베이션 과제 포트폴리오·AI 추천 | `oi-portfolio` | 22 |

## 문서 id 규칙

`skes-{도메인}-{절번호}-{제목슬러그}` — 예: `skes-d03-6-에너지솔루션`.
id 는 파일명과 일치하며, 인덱스나 검색 결과에 없는 id 는 존재하지 않는다.

## 선반

| 선반 | 내용 | 언제 |
|---|---|---|
| `seeds/` | 도메인별 O/I 과제 후보 · D17 포트폴리오 — 문서 18건 | 과제 발굴 |
| `docs/` | 도메인 본문 (사업·운영·원가·계약·규제 등) | 근거 확인 |

## 태그 어휘

`business` `capex` `contract` `core-candidate` `cost` `customer` `d00` `d01` `d02` `d03` `d04` `d05` `d06` `d07` `d08` `d09` `d10` `d11` `d12` `d13` `d14` `d15` `d16` `d17` `ecosystem` `footprint` `governance` `identity` `market` `oi-portfolio` `oi-seed` `policy` `process` `product` `risk` `rnd` `schema` `supply-chain` `table` `technology`

`xref:d##` 태그는 그 문서가 다른 도메인을 참조한다는 뜻이다.
