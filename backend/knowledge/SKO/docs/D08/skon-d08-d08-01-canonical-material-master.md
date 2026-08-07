---
id: skon-d08-d08-01-canonical-material-master
title: Canonical Material Master
summary: "리튬·니켈·코발트·망간 등 배터리 핵심 원료부터 양극·음극 활물질까지 표준 명칭, 공급단계, 주요 기능, 위험요소를 정의한 소재 마스터 테이블"
tags: [d08, supply-chain, table]
keywords: [배터리 양극, 배터리 음극, 리튬, 니켈, NCM 삼원, LFP, 흑연, 원료 공급망, 리스크 태그, 소재 표준화, 배터리 소재, 양극 원료, 음극 원료, NCM, 공급 단계, 리스크 분류]
related: [MAT-LI-SPOD-CONC, MAT-LI-BRINE, MAT-LI-CARB-BG, MAT-LI-OH-BG, MAT-NI-ORE, MAT-NI-MHP, MAT-NI-MATTE, MAT-NI-SULFATE-BG, MAT-CO-HYDROXIDE, MAT-CO-SULFATE-BG, MAT-MN-ORE, MAT-MN-SULFATE-BG, MAT-NCM-PCAM, MAT-NCM-CAM-HN, MAT-NCM-CAM-GEN, MAT-FE-PHOS-PREC, MAT-PHOS-ACID-BG, MAT-LFP-CAM, MAT-CATHODE-ADDITIVE, MAT-GR-NAT-FLAKE, MAT-GR-SPG, MAT-GR-CSPG, MAT-COKE-ANODE, MAT-GR-SYN-AAM]
priority: normal
domain: D08
section: D08-01
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Battery Material Taxonomy"
tokens: 2697
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Battery Material Taxonomy

### 3. Canonical Material Master

#### 3.1 양극·양극 원료

| material_id | 표준명 | 단계 | 주요 기능/경로 | SK온 관련성 | 핵심 리스크 태그 |
|---|---|---|---|---|---|
| `MAT-LI-SPOD-CONC` | 스포듀민 정광 | SC02 | 광석계 리튬 정광→리튬 화합물 | NCM/LFP 공통 upstream | 국가·프로젝트·정련경로 |
| `MAT-LI-BRINE` | 리튬 브라인/염수 농축물 | SC00-02 | 염호·직접리튬추출→리튬 화합물 | NCM/LFP 공통 upstream | 수자원·DLE 상용성·지역사회 |
| `MAT-LI-CARB-BG` | 배터리급 탄산리튬 | SC03 | LFP CAM 및 일부 양극·전해질 원료 | `GENERIC_CELL_INPUT` | 정련국·순도·가격 |
| `MAT-LI-OH-BG` | 배터리급 수산화리튬 | SC03 | 하이니켈 NCM 양극의 대표 리튬원 | NCM9 연계, 실제 등급·공급사는 별도 확인 | 정련집중·전환수율·탄소 |
| `MAT-NI-ORE` | 니켈 광석·정광 | SC00-02 | 황화광·라테라이트→니켈 중간재 | 하이니켈 upstream | 인도네시아 집중·환경·에너지 |
| `MAT-NI-MHP` | 니켈 MHP | SC02 | HPAL 중간재→황산니켈 | 하이니켈 upstream | HPAL 안정성·폐기물·중국계 지분 |
| `MAT-NI-MATTE` | 니켈 매트 | SC02 | 제련 중간재→배터리급 니켈 | 하이니켈 upstream | 탄소집약·전환설비 |
| `MAT-NI-SULFATE-BG` | 배터리급 황산니켈 | SC03 | NCM pCAM의 니켈원 | `GENERIC_NCM_INPUT` | 순도·불순물·정련/PFE |
| `MAT-CO-HYDROXIDE` | 코발트 수산화물·중간재 | SC02 | 코발트 광산/동광 부산물→정련 | NCM upstream | DRC·인권·ASM·추적성 |
| `MAT-CO-SULFATE-BG` | 배터리급 황산코발트 | SC03 | NCM pCAM의 코발트원 | `GENERIC_NCM_INPUT` | DRC-정련 경로·가격 |
| `MAT-MN-ORE` | 망간 광석·중간재 | SC00-02 | 고순도 망간 화합물의 원료 | NCM upstream | 고순도 전환능력·지역 집중 |
| `MAT-MN-SULFATE-BG` | 배터리급 황산망간 | SC03 | NCM pCAM의 망간원 | `GENERIC_NCM_INPUT` | 배터리급 공급능력·순도 |
| `MAT-NCM-PCAM` | NCM 전구체(pCAM) | SC04 | Ni·Co·Mn 공침 전구체 | NCM9/기타 NCM 직접 연계 | 중국 집중·조성·고객승인 |
| `MAT-NCM-CAM-HN` | 하이니켈 NCM 양극활물질 | SC05 | 리튬원+pCAM 소성·표면처리 | `COMMERCIAL_CONFIRMED` 화학계 | 수율·열안정성·원가·탄소 |
| `MAT-NCM-CAM-GEN` | 기타 NCM 양극활물질 | SC05 | 제품별 NCM 조성 | `COMMERCIAL_CONFIRMED` 상위군 | 조성별 가격·성능·공급사 승인 |
| `MAT-FE-PHOS-PREC` | 철인산 전구체 | SC04 | LFP CAM 전구체 | `ANNOUNCED/COMMERCIALIZATION` | 중국 공급집중·순도 |
| `MAT-PHOS-ACID-BG` | 배터리급 인산/인산염 원료 | SC03-04 | LFP 인 공급원 | `GENERIC_LFP_INPUT` | 정제능력·중국 의존 |
| `MAT-LFP-CAM` | LFP 양극활물질 | SC05 | 리튬·철·인 기반 양극 | SK온 LFP 기술축 확인, 공급사는 미확정 | 중국 집중·IP·현지생산 |
| `MAT-CATHODE-ADDITIVE` | 양극 도핑·코팅 첨가재 | SC05 | 고전압·수명·안전성 개선 | 조성 비공개, 후보군 | 공급사 lock-in·극미량 품질 |

#### 3.2 음극·음극 원료

| material_id | 표준명 | 단계 | 주요 기능/경로 | SK온 관련성 | 핵심 리스크 태그 |
|---|---|---|---|---|---|
| `MAT-GR-NAT-FLAKE` | 천연 플레이크 흑연 | SC01-02 | 구형화·정제 전 원료 | 흑연 음극 upstream | 채굴국과 정제국 분리·ESG |
| `MAT-GR-SPG` | 구형정제흑연(SPG) | SC03 | 천연흑연 AAM 중간재 | `GENERIC_CELL_INPUT` | 중국 정제집중·산세·수율 |
| `MAT-GR-CSPG` | 코팅 구형정제흑연(cSPG) | SC05 | 천연흑연 음극활물질 | `GENERIC_CELL_INPUT` | 코팅공정·고객승인·PFE |
| `MAT-COKE-ANODE` | 석유코크스·니들코크스 | SC00-02 | 합성흑연 원료 | 합성흑연 upstream | 원료 가격·에너지·지역집중 |
| `MAT-GR-SYN-AAM` | 합성흑연 음극활물질 | SC05 | 셀 음극의 주활물질/혼합재 | `GENERIC_CELL_INPUT` | 전력비·탄소·중국 graphitization |
| `MAT-SI-OX` | 실리콘산화물(SiOx) | SC05 | 흑연 혼합 고용량 음극재 | `RND/ADVANCED` | 팽창·초기효율·수명 |
| `MAT-SI-COMP` | 실리콘-탄소 복합 음극재 | SC05 | 고용량·급속충전 음극 | `RND_CONFIRMED` 기술축 | 팽창·바인더·양산수율 |
| `MAT-ANODE-BINDER` | SBR·CMC·PAA계 음극 바인더 | SC05 | 활물질 결착·팽창 제어 | `GENERIC_CELL_INPUT` | 조성비밀·품질편차 |
| `MAT-CONDUCTIVE` | 카본블랙·CNT 도전재 | SC05 | 전자 전도경로 형성 | `GENERIC_CELL_INPUT` | 분산성·고순도·공급집중 |

#### 3.3 전해액·전고체 전해질

| material_id | 표준명 | 단계 | 주요 기능/경로 | SK온 관련성 | 핵심 리스크 태그 |
|---|---|---|---|---|---|
| `MAT-LIPF6` | LiPF6 전해질염 | SC03-05 | 액체 전해액의 대표 리튬염 | `GENERIC_CELL_INPUT` | 불산·수분민감·중국 생산집중 |
| `MAT-LIFSI` | LiFSI 전해질염 | SC03-05 | 고전압·급속충전 보조/대체 염 | `WATCH/ADVANCED` | 원가·부식·특허 |
| `MAT-ELY-SOLVENT` | EC·EMC·DMC·DEC계 용매 | SC03-05 | 리튬염 용해·이온전달 | `GENERIC_CELL_INPUT` | 고순도·화재·물류 |
| `MAT-ELY-ADDITIVE` | VC·FEC 등 전해액 첨가제 | SC05 | SEI 형성·수명·안전성 조절 | `GENERIC_CELL_INPUT` | 소량 핵심재·배합 IP |
| `MAT-ELY-BLEND` | 완성 전해액 블렌드 | SC05-06 | 셀 주액용 승인 전해액 | `GENERIC_CELL_INPUT` | 현지화·유효기간·위험물 운송 |
| `MAT-SSE-SULFIDE` | 황화물계 고체전해질 | SC05 | 전고체 이온전도체 | `RND_CONFIRMED` | 수분민감·H2S·원가·양산성 |

#### 3.4 분리막·집전체·공정 보조재

| material_id | 표준명 | 단계 | 주요 기능/경로 | SK온 관련성 | 핵심 리스크 태그 |
|---|---|---|---|---|---|
| `MAT-SEP-BASE` | PE/PP계 분리막 원단 | SC05 | 양극·음극 절연 및 이온 통과 | `GENERIC_CELL_INPUT` | 박막 균일성·shutdown·증설 |
| `MAT-SEP-CERAMIC` | 세라믹 코팅재 | SC05 | 내열성·안전성 강화 | `GENERIC_CELL_INPUT` | 입도·코팅접착·수분 |
| `MAT-SEP-COATED` | 코팅 분리막 | SC05-06 | 승인된 완성 분리막 | `GENERIC_CELL_INPUT` | 고객승인·공급집중·현지화 |
| `MAT-CU-FOIL` | 전해동박 | SC05-06 | 음극 집전체 | `GENERIC_CELL_INPUT` | 박막화·핀홀·구리/전력가격 |
| `MAT-AL-FOIL` | 배터리용 알루미늄박 | SC05-06 | 양극 집전체 | `GENERIC_CELL_INPUT` | 두께·표면처리·알루미늄 탄소 |
| `MAT-CATHODE-BINDER` | PVDF계 양극 바인더 | SC05 | 양극 활물질 결착 | `GENERIC_CELL_INPUT` | 불소계 규제·원가·공급집중 |
| `MAT-NMP` | NMP 용제 | SC05-06 | PVDF 용해·양극 슬러리 제조 | `GENERIC_PROCESS_INPUT` | 회수율·노출·규제·에너지 |
| `MAT-TAB-LEAD` | Cu·Al·Ni 탭/리드 소재 | SC05-06 | 전류 인출·셀 연결 | `GENERIC_CELL_INPUT` | 용접성·저항·도금 품질 |

#### 3.5 순환공급망 원료

| material_id | 표준명 | 단계 | 주요 기능/경로 | SK온 관련성 | 핵심 리스크 태그 |
|---|---|---|---|---|---|
| `MAT-SCRAP-PROD` | 셀 제조 공정스크랩 | SC07 | 전극·셀 불량 및 트리밍 폐기물 | `CLOSED_LOOP_PRIORITY` | 분리배출·오염·회수물류 |
| `MAT-EOL-BATT` | 사용후 EV/ESS 배터리 | SC07 | 재사용·재제조·재활용 원료 | `CLOSED_LOOP_PRIORITY` | 소유권·SoH·운송·화재 |
| `MAT-BLACK-MASS` | 블랙매스 | SC08 | Li·Ni·Co·Mn·흑연 함유 중간재 | `CLOSED_LOOP_PRIORITY` | 폐기물 지위·국경이동·품질 |
| `MAT-REC-LI` | 재생 배터리급 리튬염 | SC08→03 | CAM/전해질 공급망 복귀 | `CLOSED_LOOP_TARGET` | 순도·탄소·mass balance |
| `MAT-REC-NCM-SALT` | 재생 Ni·Co·Mn 염 | SC08→03 | pCAM 공급망 복귀 | `CLOSED_LOOP_TARGET` | 불순물·회수율·추적성 |
| `MAT-REC-GRAPHITE` | 재생 흑연 | SC08→05 | 음극재 또는 보조 용도 복귀 | `WATCH/CLOSED_LOOP` | 재생성능·경제성·승인 |
| `MAT-REC-CU-AL` | 회수 구리·알루미늄 | SC08 | 집전체·금속 공급망 복귀 | `CLOSED_LOOP_TARGET` | 분리순도·재용해 탄소 |
