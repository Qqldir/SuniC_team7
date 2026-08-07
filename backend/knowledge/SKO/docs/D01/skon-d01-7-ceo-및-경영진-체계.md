---
id: skon-d01-7-ceo-및-경영진-체계
title: CEO 및 경영진 체계
summary: "SK온의 초대 대표부터 현재까지의 경영진 변화 이력과 2025년 각자대표 체계 구축, 현재 확인된 대표이사 정보를 정리한 자료다."
tags: [d01, identity, schema, table]
keywords: [대표이사, 각자대표, SK이노베이션, 이용욱, 이석희, 2025년 인사, 공동대표, 리더십, 조직 개편, 최고경영진, 경영진개편, 제조운영, 북미]
related: []
priority: normal
domain: D01
section: 7
source: SK온_D01_Corporate_Identity.md
breadcrumb: ""
tokens: 986
updated: 2026-08-03
---

> SK온 · D01 기업 기본정보·법인구조·연혁

# 7. CEO 및 경영진 체계

## 7.1 대표이사 이력

### 초기 대표체계

SK온 출범 당시 초대 대표이사는 지동섭 사장이었다. 이후 글로벌 성장전략과 내부경영을 분담하는 각자대표 구조가 운영됐으며, 시기에 따라 최재원 수석부회장, 지동섭 사장, 이석희 사장 등이 대표이사 역할을 수행했다. ([연합뉴스][1])

### 2025년 경영진 개편

SK이노베이션은 2025년 10월 30일 이용욱 사장을 SK온 사장으로 선임하고, 이석희 사장과 각자대표 체계를 구축한다고 공식 발표했다. 당시 역할 분담은 이용욱 사장이 제조와 운영 전반을, 이석희 사장이 북미 고객관리와 R&D 기술혁신을 담당하는 구조로 설명됐다. ([ASK Inno][9])

2025년 12월과 2026년 1월 공식 SK이노베이션 콘텐츠는 이용욱을 SK온 CEO 또는 대표이사 사장으로 명시하고, 2026년 신년 메시지는 이석희·이용욱 사장 공동 명의로 제시했다. 따라서 최소한 2026년 1월 초까지는 각자대표 체계가 공식적으로 확인된다. ([ASK Inno][10])

## 7.2 기준일 대표이사 상태

| 필드             | 데이터                                    |
| -------------- | -------------------------------------- |
| 최신 공식 확인 대표    | 이용욱 대표이사 사장                            |
| 최신 공식 공동대표 확인  | 이석희 사장·이용욱 사장                          |
| 최신 공식 확인 시점    | 2026년 1월                               |
| 2026년 6월 이후 상태 | 공식 원문 추가 확인 필요                         |
| 데이터 상태         | `pending_latest_registry_verification` |

2026년 6월 외부 보도에서는 이용욱 단독대표 체제로의 전환과 이석희 사장의 사임이 언급됐으나, 이번 조사에서는 해당 변화를 확정하는 SK온·SK이노베이션 공식 보도자료나 최신 법인등기 원문을 확보하지 못했다. 따라서 데이터베이스에서는 이용욱을 현재 확인 가능한 대표이사로 기록하되, 단독대표 전환 여부는 `external_report_pending_official_confirmation`으로 관리한다. ([CEO스코어데일리][11])

### 대표이사 레코드

```yaml
executive_id: EXEC-SKON-LYW
name_ko: 이용욱
name_en: Lee Young-wook
position: 대표이사 사장 / CEO
appointment_announced: 2025-10-30
responsibility_at_appointment:
  - manufacturing
  - operations
previous_positions:
  - SK실트론 대표이사 사장
  - SK머티리얼즈 대표이사 사장
fact_status: official_fact
```

```yaml
executive_id: EXEC-SKON-LSH
name_ko: 이석희
position: 대표이사 사장
officially_confirmed_role:
  - North American customer relations
  - R&D technology innovation
official_confirmation_period: 2025-10 to 2026-01
current_status: pending_official_verification
```

---
