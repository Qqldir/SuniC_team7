---
id: skes-d16-9-vendor-due-diligence-checklist
title: Vendor Due-Diligence Checklist
summary: 외부 벤더 평가·선정 시 필요한 기술·보안·데이터·규제 실사항목(30개)과 종합 평가 스코어카드(11개 차원)를 제시한다.
tags: [d16, ecosystem, table, "xref:d17", "xref:d15", "xref:d11"]
keywords: [벤더평가, 공급업체심사, 검증항목, 평가점수, 기술적합도, 보안정책, 규제준수, 총소유비용]
related: [DD-001, DD-002, DD-003, DD-004, DD-005, DD-006, DD-007, DD-008, DD-009, DD-010, DD-011, DD-012, DD-013, DD-014, DD-015, DD-016, DD-017, DD-018, DD-019, DD-020, DD-021, DD-022, DD-023, DD-024]
priority: normal
domain: D16
section: 9
source: SK이노베이션E&S_D16_External_Technologies_Solutions_Companies_and_Startups.md
breadcrumb: ""
tokens: 2147
updated: 2026-08-06
---

> SK이노베이션 E&S · D16 외부 기술·솔루션·기업·스타트업

# 9. Vendor Due-Diligence Checklist

| DD ID | 검증항목 | 필수 증거 |
|---|---|---|
| `DD-001` | 법인·재무 지속가능성 | audited/official financial information |
| `DD-002` | 실제 reference customer | 고객명·asset/use case |
| `DD-003` | product lifecycle | version·support/EOL policy |
| `DD-004` | data ownership | contract clause |
| `DD-005` | raw data export | open format/API test |
| `DD-006` | model portability | export/retrain path |
| `DD-007` | security architecture | diagram·certification |
| `DD-008` | vulnerability handling | PSIRT/SLA |
| `DD-009` | identity/access | SSO·RBAC·MFA |
| `DD-010` | encryption/key ownership | at-rest/in-transit/KMS |
| `DD-011` | audit logging | immutable/time-synced logs |
| `DD-012` | cloud region/residency | hosting evidence |
| `DD-013` | subprocessor | list/change notice |
| `DD-014` | OT protocol support | lab test |
| `DD-015` | offline/edge mode | fail-safe test |
| `DD-016` | latency | measured P95/P99 |
| `DD-017` | data loss behavior | outage/reconnect test |
| `DD-018` | false-positive handling | alert workflow |
| `DD-019` | model explainability | feature/evidence trace |
| `DD-020` | drift monitoring | threshold/rollback |
| `DD-021` | functional safety boundary | SIS independence evidence |
| `DD-022` | calibration traceability | instrument certificates |
| `DD-023` | hazardous area compliance | Ex/ATEX/IECEx/Korean applicability |
| `DD-024` | BESS standards | UL/NFPA/AHJ applicability |
| `DD-025` | legal/tax disclaimer | decision ownership |
| `DD-026` | SLA | availability/support response |
| `DD-027` | pricing model | user/tag/asset/API/compute basis |
| `DD-028` | scale economics | 1 site→fleet TCO |
| `DD-029` | implementation partner | roles/RACI |
| `DD-030` | exit plan | data/model/config return/deletion |

## 9.1 D17 Solution Evaluation Scorecard

점수는 서로 다른 외부기술을 비교하기 위한 screening 도구다. 공개자료만으로 실제 ROI나 회사 공식투자등급을 만들지 않는다. 각 항목은 `0~5`이나 내부값이 없으면 `NA`로 남기고, `NA=0`으로 자동 치환하지 않는다.

| Dimension | Weight | 0점 | 3점 | 5점 | 필수 증거 |
|---|---:|---|---|---|---|
| Pain Criticality | 15 | 경미/불명 | 반복 손실·업무부담 | 안전·가동·대규모 손실 연결 | D15 FM/Risk |
| Evidence Strength | 12 | marketing only | 제품+외부 case | 유사자산 실증+검증자료 | EVD/SRC |
| E&S Data Readiness | 12 | 데이터 부재 | 일부 tag/로그 존재 | ground truth 포함 usable data | DR 확인 |
| Technical Fit | 10 | 핵심기능 불일치 | customization 필요 | direct fit | fit workshop |
| Value Measurability | 10 | KPI 불명 | proxy KPI | baseline/outcome 명확 | D11 KPI |
| Time to PoC | 8 | >12개월/불명 | 3~6개월 | read-only 4~8주 가능 | architecture |
| Integration Friction | 8 | legacy/closed | connector 개발 | standard interface | lab test |
| Safety/Regulatory Fit | 8 | 통제경계 충돌 | 승인·MOC 필요 | read-only/non-safety use | HSE/Legal |
| Cyber/Data Fit | 7 | 정책충돌 | 조건부 가능 | approved pattern | CISO review |
| Scale Economics | 5 | site당 비용 급증 | 불명/중립 | fleet scale benefit | vendor quote/TCO |
| Strategic Control | 5 | data/model lock-in | export 일부 | canonical data·exit 확보 | contract test |

### Hard Gate

다음 중 하나라도 `FAIL`이면 총점이 높아도 D17 우선 PoC로 승격하지 않는다.

1. Safety-critical action이 SIS/ESD 또는 법정 안전장치를 우회한다.
2. E&S가 필요한 데이터 사용권을 확보하지 못한다.
3. cyber architecture가 OT segmentation 원칙과 충돌하고 보완책이 없다.
4. legal/tax/regulatory 판단을 AI 또는 벤더가 무승인 자동확정한다.
5. PoC가 원래 운영 baseline을 보존하지 않아 효과를 측정할 수 없다.
6. vendor가 raw data/export/log access를 제공하지 않아 독립 검증이 불가능하다.
7. 모델/제어 오류 때 안전한 rollback 또는 manual override가 없다.

## 9.2 Evidence-to-Claim Rule

| Claim | 최소 Evidence | 예시 |
|---|---|---|
| “제품 기능이 존재한다” | E3 | 공식 product page |
| “산업에서 적용됐다” | E2 | named customer case |
| “유사 LNG/CCGT/BESS에서 적용됐다” | E2 + asset type match | Dragon LNG/RWE 등 |
| “E&S에서 기술적으로 작동한다” | L3/L4 | 내부 offline/shadow test |
| “E&S 비용을 절감한다” | L5 + financial baseline | D11 unit economics |
| “전사 확대 가치가 있다” | L5/L6 + TCO + control | multi-site evidence |

## 9.3 PoC Baseline Protocol

| Step | 필수 산출물 | 실패 시 |
|---|---|---|
| 1. Baseline Freeze | KPI 정의·기간·제외조건 | 시작 보류 |
| 2. Data QA | missing·latency·sensor drift·ground truth | 데이터 보강 |
| 3. Offline Replay | 과거 사건 재현 precision/recall | 모델 재설계 |
| 4. Shadow Live | 운영개입 없이 live 성능 | 안정화 |
| 5. Human-in-loop | 추천→승인→조치 로그 | 승인흐름 수정 |
| 6. Outcome Window | 기술·운영·재무 KPI | 기간 연장/종료 |
| 7. Adverse Test | 통신단절·stale data·bad sensor | fail-safe 검증 |
| 8. Exit Test | data/model/config export | scale 금지 |

## 9.4 Vendor Lock-in Decomposition

| Lock-in | 질문 | 완화책 |
|---|---|---|
| Data | raw/processed data를 다른 시스템으로 이동 가능한가 | open format·API·bulk export |
| Model | 학습모델/feature 정의를 재현 가능한가 | model card·feature spec |
| Workflow | work order/approval logic이 proprietary인가 | BPM/API abstraction |
| Hardware | sensor/controller가 특정 cloud에 종속되는가 | protocol gateway |
| Identity | vendor IAM을 강제하는가 | enterprise SSO/federation |
| Historian | tag/context가 vendor namespace에 갇히는가 | canonical asset ID |
| Contract | egress/termination 비용이 과도한가 | exit clause/price cap |
| Skills | 운영자가 vendor만 통해 문제해결 가능한가 | training/runbook/source access |

## 9.5 Startup-specific Gate

스타트업은 대기업 벤더보다 빠르게 특화기술을 제공할 수 있지만, energy infrastructure에서는 제품 기능 외 생존성·지원성도 검증한다.

| Gate | 확인항목 |
|---|---|
| Runway | 공개/제공 가능한 범위에서 financing·runway·key-person risk |
| Support | 24/7 critical support 여부와 escalation path |
| Insurance | cyber/professional/product liability coverage |
| IP | 핵심 software/model 소유권·third-party dependency |
| Escrow | 사업중단 시 code/config/data 접근 대안 |
| Deployment | on-prem/edge/hybrid 대안 |
| Reference | 최소 1개 named industrial reference 또는 controlled benchmark |
| Scale | 1 site PoC 이후 multi-site architecture |
| Security | SOC2/ISO27001 등 증거와 실제 architecture review를 분리 |
| Exit | vendor 종료 시 운영 연속성 |

---
