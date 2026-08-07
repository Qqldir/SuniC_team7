---
id: skon-d00-d00-02-canonical-source-master
title: Canonical Source Master
summary: 출처의 신뢰도(S1A~S5)와 증거 수준(E0~E4)을 정의하고 URL 정규화·관리하는 표준 스키마 및 분류 체계
tags: [d00, governance, schema, table, "xref:d09", "xref:d13", "xref:d08", "xref:d11"]
keywords: [출처 등급, 신뢰도 분류, 증거 수준, URL 정규화, Canonical Source, 메타데이터 스키마, Source Record, 출처 검증, 신뢰도 등급, Canonical ID, 출처 분류, 사실 확정, S1A~S5, E0~E4, 정규화 규칙, 검증 기준]
related: [SRC-CAN-000001, SRC-CAN-000002, SRC-CAN-000003, SRC-CAN-000004, SRC-CAN-000005, SRC-CAN-000006, SRC-CAN-000007, SRC-CAN-000008, SRC-CAN-000009, SRC-CAN-000010, SRC-CAN-000011, SRC-CAN-000012, SRC-CAN-000013, SRC-CAN-000014, SRC-CAN-000015, SRC-CAN-000016, SRC-CAN-000017, SRC-CAN-000018, SRC-CAN-000019, SRC-CAN-000020, SRC-D01-LEG-001, S03-008, SRC-D08-S03-008]
priority: normal
domain: D00
section: D00-02
source: SK온_D00_Source_Entity_ID_Change_Log_Master.md
breadcrumb: "SK온 D00 — Source, Entity, ID & Change-Log Master"
tokens: 2317
updated: 2026-08-03
---

> SK온 · D00 소스·엔티티·ID·변경이력 마스터 · SK온 D00 — Source, Entity, ID & Change-Log Master

## D00-02 Canonical Source Master

### 1. Source Record Schema

```yaml
source_record:
  canonical_source_id: SRC-CAN-000001
  legacy_source_ids: []
  title: ""
  publisher_legal_entity_id: ""
  source_type: LAW|REGULATOR|FILING|COMPANY_PRIMARY|STANDARD|RESEARCH|MEDIA|VENDOR_CLAIM
  original_url: ""
  canonical_url: ""
  document_identifier: ""
  publication_date: null
  effective_date: null
  access_date: YYYY-MM-DD
  language: ""
  jurisdiction: ""
  version_or_filing_period: ""
  reliability_grade: S1A|S1B|S2|S3|S4|S5
  evidence_level: E0|E1|E2|E3|E4
  accessibility_status: OPEN_CONFIRMED|LOGIN_REQUIRED|PAYWALL|MOVED|BROKEN|NOT_RECHECKED_D00
  content_hash: null
  owner_domain: D00
  used_by_domains: []
  supported_claim_ids: []
  supersedes_source_ids: []
  superseded_by_source_ids: []
  last_verified_at: YYYY-MM-DDThh:mm:ss+09:00
  next_review_at: null
  notes: ""
```

### 2. 출처 등급

| Grade | 출처 유형 | 허용 용도 | 단독 확정 제한 |
|---|---|---|---|
| `S1A` | 법령·정부·규제기관·법원·거래소·SEC/DART·공식 등록부 | 법적 상태·공시수치·시행일의 우선 근거 | 적용대상 해석·비공개 사실은 별도 검토 |
| `S1B` | 당사자 공식 홈페이지·IR·보도자료·연차보고서 | 회사 발표 사실·관계·목표·실적 | 회사 Claim과 독립검증을 구분 |
| `S2` | 국제기구·학술논문·공공연구기관·표준기관 | 산업 Baseline·기술원리·방법론 | 특정 SK온 내부 적용을 자동 확정하지 않음 |
| `S3` | 신뢰 언론·통신사 | 사건·업계 맥락·교차검증 | 계약·권리·정확한 내부 수치 단독 확정 금지 |
| `S4` | 전문매체·컨설팅·산업 DB·기업 홍보성 Case | 후보 탐색·정황·Benchmark | 핵심 Fact는 S1/S2와 교차검증 |
| `S5` | 검색요약·블로그·출처불명·재전재 | 키워드 발견 | 사실 확정 금지 |

### 3. Source Evidence Level

| Level | 의미 | 예시 |
|---|---|---|
| `E0` | 존재 주장만 있음 | 제품 소개·마케팅 페이지 |
| `E1` | 관계 또는 계획 발표 | MOU·투자검토·개발계획 |
| `E2` | 구속력/실행 Event 확인 | 계약·발주·대출종결·설비설치 |
| `E3` | 운영·양산·고객적용 확인 | 상업생산·고객출하·현장 적용 |
| `E4` | 검증된 성과·감사·규제판정 | 독립검증 KPI·감사보고·행정판정 |

`Evidence Level`은 출처 신뢰도와 다르다. 공식 회사 발표는 `S1B`일 수 있지만 내용이 MOU라면 실행수준은 `E1`이다.

### 4. URL 정규화 규칙

1. `utm_source=chatgpt.com` 등 추적 파라미터를 Canonical URL에서 제거한다.
2. SEC accession, 법령 CELEX, 특허번호, 보고서 DOI처럼 문서 식별자가 있으면 URL보다 우선키로 사용한다.
3. 같은 PDF의 언어·미러 URL은 Source Alias로 묶되 원문 발행자 URL을 Canonical로 둔다.
4. 회사 뉴스룸의 한국어·영어 페이지가 같은 발표라도 번역 차이가 있으면 별도 Source Version으로 보존한다.
5. 동적 재무·법령 페이지는 `access_date`, `effective_date`, `content_hash` 없이 같은 문서로 간주하지 않는다.
6. URL Redirect는 기존 ID를 삭제하지 않고 `canonical_url`만 갱신하며 변경이력을 남긴다.
7. Paywall 기사로만 확인된 핵심 사실은 `S4_PENDING_PRIMARY` 검증 큐에 넣는다.

### 5. 반복 사용 핵심 Source Cluster

아래 ID는 기존 도메인 Source ID를 대체하지 않고, 같은 원문을 묶는 D00 Canonical Alias다.

| Canonical ID | 원문 | 핵심 사용범위 |
|---|---|---|
| `SRC-CAN-000001` | [SK Innovation 2026 Q2 Results](https://askinno.com/global/archives/156625) | D09~D13 수요·보상·손익·BOSK·ESS |
| `SRC-CAN-000002` | [IRS Notice 2026-15](https://www.irs.gov/pub/irs-drop/n-26-15.pdf) | D08·D11·D14 PFE/MACR·45X |
| `SRC-CAN-000003` | [SK On Tennessee Launch](https://eng.sk.com/news/sk-on-tennessee-becomes-newest-sk-on-u-s-company) | D07·D09·D12·D13 법인·공장·전환 |
| `SRC-CAN-000004` | [Ford 2026-05-20 Form 8-K](https://www.sec.gov/Archives/edgar/data/37996/000003799626000093/f-20260520.htm) | D07·D09·D12·D13 BOSK 분리·Note·보증 |
| `SRC-CAN-000005` | [HSBMA Commercial Production](https://www.hyundainews.com/releases/4876) | D07·D09·D12·D13 상업생산·JV |
| `SRC-CAN-000006` | [SK Innovation 2025 Q3 Results](https://askinno.com/global/archives/22126) | D02·D09·D11·D13 통합범위·ESS 계약 |
| `SRC-CAN-000007` | [DOE Advanced Battery Supply Chain Review](https://www.energy.gov/sites/default/files/2024-12/20212024-Four%20Year%20Review%20of%20Supply%20Chains%20for%20the%20Advanced%20Batteries%20Sector.pdf) | D06·D08·D10 제조·공급망·시장 |
| `SRC-CAN-000008` | [EU Batteries Regulation consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A02023R1542-20250731) | D08·D14 Passport·실사·탄소·재생원료 |
| `SRC-CAN-000009` | [SK Innovation 2025 Q4 & FY Results](https://askinno.com/global/archives/153922) | D11·D12 손익·손상·현금·투자 |
| `SRC-CAN-000010` | [IRS 45X Final Regulations](https://www.irs.gov/irb/2024-51_IRB) | D11·D14 Cell/Module 생산세액공제 |
| `SRC-CAN-000011` | [SK On–Nissan Supply Agreement](https://eng.sk.com/news/sk-on-signs-battery-supply-agreement-with-nissan) | D09·D13 계약량·기간·제품범위 |
| `SRC-CAN-000012` | [SK On–Siemens Digital Twin](https://eng.sk-on.com/company/press_view.asp?CompanyCode=011&idx=145&page=1&schtxt=) | D04·D06·D16 제조 Digital Twin 협력 |
| `SRC-CAN-000013` | [SK On BaaS](https://eng.sk-on.com/business/business_03.asp) | D02·D03·D08 서비스·재사용·재활용 |
| `SRC-CAN-000014` | [HMG–SK On Georgia JV](https://www.hyundaimotorgroup.com/en/news/CONT0000000000089410) | D07·D12 HSBMA 50:50·35GWh·투자구조 |
| `SRC-CAN-000015` | [SK Innovation 2026 Q1 Results](https://askinno.com/global/archives/154570) | D10·D11 시장·손익 Baseline |
| `SRC-CAN-000016` | [BMW Virtual Factory](https://www.press.bmwgroup.com/global/article/detail/T0450699EN/bmw-group-scales-virtual-factory?language=en) | D06·D11·D12 외부 Digital Twin 사례 |
| `SRC-CAN-000017` | [Solid Power 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1844862/000110465926019435/sldp-20251231x10k.htm) | D05·D13 R&D License·설비·전해질·권리범위 |
| `SRC-CAN-000018` | [SK Innovation R&D](https://www.skinnovation.com/company/rnd) | D04·D05 연구영역·시설 |
| `SRC-CAN-000019` | [NHTSA Recall 23V-168](https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V168-8458.PDF) | D15 F-150 사건·대상 Population·추적성 |
| `SRC-CAN-000020` | [CATL 2025 Annual Report Release](https://www.catl.com/en/news/6773.html) | D10·D11 경쟁·판매·Capacity·재무 Claim |

### 6. Source ID Migration Rule

| Legacy 형태 | 처리 | 예시 |
|---|---|---|
| 번호 링크만 존재 | 도메인 Alias 생성 | D01 `[1]` → `SRC-D01-LEG-001` |
| `SRC-SKON-Dxx-nnn` | 그대로 보존 | D03~D07 |
| `S02/S03/S04/S05/S08X-nnn` | D08 namespace를 붙인 Alias 생성 | `S03-008` → `SRC-D08-S03-008` |
| `SRC-Dxx-nnn` | 그대로 보존 | D09~D16 |
| `SRC-D17-Dxx` | 파일 Lineage ID로 보존 | 외부 원문 Source와 구분 |
| 같은 URL의 여러 ID | `canonical_source_id`로 묶음 | D11·D14의 IRS 45X |

Legacy ID는 삭제하거나 일괄 치환하지 않는다. D17과 기존 Graph의 참조가 깨질 수 있기 때문에 `legacy_source_id → canonical_source_id` Crosswalk를 추가한다.

---
