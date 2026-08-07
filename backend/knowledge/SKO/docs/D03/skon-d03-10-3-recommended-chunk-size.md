---
id: skon-d03-10-3-recommended-chunk-size
title: Recommended Chunk Size
summary: "검색 시스템의 효율적인 텍스트 분할을 위한 청크 크기, 토큰 범위, 오버랩, 분할 우선순위 표준"
tags: [d03, product, schema, "xref:d00"]
keywords: [청킹 정책, 토큰 범위, 오버랩, 분할 우선순위, Entity boundary, 문서 분할, 검색 최적화, chunking_policy, 청크 스키마, 혼합 금지, 청킹, chunking, 토큰, token, 엔티티 경계, 벡터 검색, RAG, 텍스트 분할, 슬라이딩 윈도우]
related: []
priority: normal
domain: D03
section: 10.3
source: SK온_D03_Products_and_Solutions.md
breadcrumb: ""
tokens: 1063
updated: 2026-08-03
---

> SK온 · D03 제품·솔루션

# 10.3 Recommended Chunk Size

```yaml
chunking_policy:

  target_token_range:
    minimum: 250
    optimal: 450
    maximum: 700

  overlap_tokens:
    default: 60

  split_priority:
    - Entity boundary
    - Product generation
    - Commercial status
    - Application
    - Evidence source
    - Fact and analysis boundary

  prohibited_mixed_chunks:
    - Commercial product plus unrelated R&D concept
    - SK On fact plus competitor manufacturer claim without labels
    - Historical plan plus current result
    - Cell specification plus vehicle performance without boundary
```

---

## 이번 구간 완료

* D00 Source Library 추가 등록: `SRC-SKON-D03-051~063`
* `D03-08 Product Relationship Graph`

  * Graph ontology
  * Node·Edge schema
  * 제품 계층 그래프
  * 급속충전 제품 진화 그래프
  * ESS·BaaS·전고체 그래프
  * 경쟁제품 Benchmark Graph
  * Pain Point·OI Seed Graph
  * Canonical Triple Registry
  * Graph Query Template
* `D03-09 Integrated Entity Master`

  * 총 178개 등록 엔티티 스냅샷
  * 제품·서비스·기술 통합 마스터
  * 상용화 상태 표준
  * Alias Dictionary
* `D03-10 Chunk Library`

  * Chunk Schema
  * 표준 청크 15개
  * Retrieval Rules
  * Chunking Policy

## 다음 시작점

`D03-11 Human-Readable Report`

이후:

```text
D03-11 Human-Readable Report
→ D03-12 Data Quality & Gap Register
→ D03-13 Source Index
→ D03 Final YAML
→ D03 완료
```

[1]: https://www.skinnovation.com/company/rnd?utm_source=chatgpt.com "R&D < About us < Company < SK Innovation"
[2]: https://askinno.com/global/archives/154332?utm_source=chatgpt.com "[Battery Deep Dive] Part 5: Seven-Minute Fast Charging - Ask Inno Global"
[3]: https://askinno.com/global/archives/154394?utm_source=chatgpt.com "[Battery Deep Dive] Part 6: On-vent Prismatic Cell - Ask Inno Global"
[4]: https://askinno.com/global/archives/154429?utm_source=chatgpt.com "[Battery Deep Dive] Part 7: Pouch-Integrated Prismatic Cell - Ask Inno Global"
[5]: https://askinno.com/global/archives/21968?utm_source=chatgpt.com "SK On Opens All-Solid-State Battery Pilot Plant, Eyes 2029 Commercialization - Ask Inno Global"
[6]: https://askinno.com/global/archives/8067?utm_source=chatgpt.com "SK On develops battery diagnosis technology that allows electric vehicle drivers to self-check - Ask Inno Global"
[7]: https://askinno.com/global/archives/154549 "[Inside ESS] Powering the Future of Energy SK On ESS: GRIDON - Ask Inno Global"
[8]: https://askinno.com/global/archives/154786 "SK On Expands U.S. ESS Push at ACP CLEANPOWER 2026 - Ask Inno Global"
[9]: https://askinno.com/global/archives/153882?utm_source=chatgpt.com "[Battery Deep Dive] Part 4: Cell-to-Pack Technology - Ask Inno Global"
[10]: https://www.catl.com/en/news/6239.html?pubDate=20250523&utm_source=chatgpt.com "CATL Unveils Shenxing PLUS, Enabling 1,000-km Range and 4C Superfast Charging"
[11]: https://www.catl.com/en/news/6232.html?utm_source=chatgpt.com "CATL Unveils TENER, the World's First Five-Year Zero Degradation Energy Storage System with 6.25MWh Capacity"
[12]: https://www.lgcorp.com/media/release/27840?utm_source=chatgpt.com "Press Release | Media | LG"
[13]: https://news.samsungsdi.com/global/articleView?seq=313&utm_source=chatgpt.com "SAMSUNG SDI Debuts New SBB Products Featuring High Capacity and Enhanced Safety"
[14]: https://askinno.com/global/archives/12091?utm_source=chatgpt.com "SK On and SK Signet sign an MOU to diagnose EV Battery lifespans and residual values with a charger - Ask Inno Global"
[15]: https://askinno.com/global/archives/17216?utm_source=chatgpt.com "SK On strengthens partnership with Solid Power to accelerate all-solid-state battery development - Ask Inno Global"

---
