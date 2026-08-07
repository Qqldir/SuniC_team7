---
id: skon-d01-11-해외-법인-및-글로벌-정체성
title: 해외 법인 및 글로벌 정체성
summary: "SK온의 해외 법인 및 생산 거점 구조와 엔티티 분류 방식, 그리고 해외 사업장 데이터 관리 규칙을 설명하는 문서."
tags: [d01, identity, table]
keywords: [엔티티 분류, 완전자회사, 합작법인, JV, 지역 생산법인, SK Battery America, 조지아, 테네시, 헝가리, 생산능력, 생산 거점, 지분율, Legal Entity ID, 데이터 품질 규칙]
related: []
priority: normal
domain: D01
section: 11
source: SK온_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 552
updated: 2026-08-03
---

> SK온 · D01 기업 기본정보·법인구조·연혁

# 11. 해외 법인 및 글로벌 정체성

SK온은 미국, 유럽, 중국 등 주요 전기차 시장을 중심으로 해외 생산 및 사업 법인을 구축해 왔다. 공식 글로벌 네트워크에는 미국 조지아, 테네시 등 북미 거점과 헝가리 및 중국 생산 관련 법인이 포함된다. ([SK On][13])

## 11.1 해외 엔티티 분류

| Entity Type | 예시                 | DB 처리                    |
| ----------- | ------------------ | ------------------------ |
| 완전자회사       | SK Battery America | 별도 Company Entity        |
| 지역 생산법인     | 헝가리 생산법인           | 별도 Company Entity        |
| 합작법인        | OEM·파트너와의 JV       | Joint Venture Entity     |
| 해외 공장       | 조지아·헝가리·중국 공장      | Site Entity              |
| 해외 영업·관리 조직 | 지역별 법인 또는 사무소      | Organization/Site Entity |

## 11.2 주요 해외 사업장 예시

SK온 공식 해외 사업장 페이지는 미국 조지아주의 SK Battery America와 테네시주의 SK On Tennessee를 포함한 글로벌 거점을 안내한다. 정확한 법인명, 주소, 생산능력, 가동상태 및 소유구조는 D07에서 개별 Site ID와 Legal Entity ID를 연결해 관리한다. ([SK On][14])

### 데이터 품질 규칙

해외 공장을 기록할 때 다음을 반드시 분리한다.

* 법인명
* 공장명
* 소재지
* 소유주체
* JV 여부
* 지분율
* 건설 상태
* 시험생산 상태
* 상업가동 상태
* 명목 생산능력
* 실제 생산량
* 주요 고객
* 기준일

---
