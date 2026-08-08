---
id: skes-d15-11-ot-cyber-data-ai-resilience
title: "OT Cyber, Data & AI Resilience"
summary: E&S 발전·가스 등 에너지 인프라의 OT·데이터·AI 보안 위협을 다루는 실패 모드(FM)와 위험 지표(KRI) 정의 문서.
tags: [d15, risk, table]
keywords: [SCADA/PLC, 위협 모델, 실패 모드, 핵심 위험 지표, OT 보안, 권한 관리, 데이터 품질, AI 거버넌스, 백업복구]
related: [FM-ENS-D15-087, FM-ENS-D15-088, FM-ENS-D15-089, FM-ENS-D15-090, FM-ENS-D15-091, FM-ENS-D15-092, FM-ENS-D15-093, FM-ENS-D15-094, FM-ENS-D15-095, FM-ENS-D15-096, FM-ENS-D15-097, FM-ENS-D15-098, FM-ENS-D15-099, FM-ENS-D15-100, FM-ENS-D15-101, FM-ENS-D15-102, FM-ENS-D15-103, FM-ENS-D15-104, KRI-ENS-D15-053, KRI-ENS-D15-054, KRI-ENS-D15-055, KRI-ENS-D15-056, KRI-ENS-D15-057, KRI-ENS-D15-058]
priority: normal
domain: D15
section: 11
source: SK이노베이션E&S_D15_Enterprise_Risk_Issues_Failure_Modes_and_Resilience.md
breadcrumb: ""
tokens: 1001
updated: 2026-08-06
---

> SK이노베이션 E&S · D15 리스크·실패모드·회복탄력성

# 11. OT Cyber, Data & AI Resilience

## 11.1 OT Cyber Threat Model

E&S의 발전·도시가스·LH2·BESS·충전 인프라는 물리설비와 디지털 제어가 결합되어 있다. 2026년 CISA는 인터넷에 노출된 OT를 대상으로 한 위협 활동을 별도 경고했다. 이것은 E&S가 침해됐다는 증거가 아니라 **인터넷 노출·원격접속·기본 credential·세분화·backup/recovery**를 KRI로 관리해야 한다는 외부 신호다. `[SRC-ENS-D15-0029][SRC-ENS-D15-0030]`

| FM ID | Failure Mode | Consequence | Required Control |
|---|---|---|---|
| `FM-ENS-D15-087` | internet-exposed OT | unauthorized access | inventory·firewall·isolation |
| `FM-ENS-D15-088` | vendor remote access compromise | lateral movement | MFA·JIT·session logging |
| `FM-ENS-D15-089` | IT→OT segmentation failure | process disruption | network zoning |
| `FM-ENS-D15-090` | PLC/SCADA configuration change untracked | unsafe/control drift | signed config·change control |
| `FM-ENS-D15-091` | ransomware affects HMI/historian | blind/degraded operation | immutable backup·manual mode |
| `FM-ENS-D15-092` | BESS/charger cloud outage | dispatch/service loss | local safe control |
| `FM-ENS-D15-093` | telemetry manipulation | unsafe/market error | sensor plausibility·cross-check |
| `FM-ENS-D15-094` | credential overprivilege | unauthorized action | PAM/RBAC |
| `FM-ENS-D15-095` | vulnerability patch lag | exploit exposure | risk-based patch window |
| `FM-ENS-D15-096` | recovery backup unusable | RTO failure | restore drill |

## 11.2 AI/Data Failure Modes

| FM ID | Failure Mode | Example | Guardrail |
|---|---|---|---|
| `FM-ENS-D15-097` | stale regulation | 취소된 H2 입찰을 active로 표시 | effective-date lock |
| `FM-ENS-D15-098` | hallucinated contract clause | 공개되지 않은 LD 추정 | source-locked extraction |
| `FM-ENS-D15-099` | unit/period mismatch | MW↔MWh, annual↔quarter | metadata validation |
| `FM-ENS-D15-100` | entity lineage error | SK E&S→E&S CIC 계약 승계 오인 | canonical entity graph |
| `FM-ENS-D15-101` | model drift | BESS bid regime 변화 미반영 | monitoring/champion challenger |
| `FM-ENS-D15-102` | data leakage | confidential contract in external model | data classification/DLP |
| `FM-ENS-D15-103` | automation without approval | dispatch/ESD/filing 자동실행 | human-in-command |
| `FM-ENS-D15-104` | false confidence from missing data | public gap을 zero로 처리 | UNKNOWN/INTERNAL_REQUIRED state |

## 11.3 Cyber/Data KRIs

| KRI ID | KRI | Meaning |
|---|---|---|
| `KRI-ENS-D15-053` | Unknown OT Asset Count | inventory completeness gap |
| `KRI-ENS-D15-054` | Internet-exposed OT Count | 직접 노출 최소화 |
| `KRI-ENS-D15-055` | Privileged Remote Session Exception | 승인 없는/정책 이탈 세션 |
| `KRI-ENS-D15-056` | Critical Patch Aging | risk-accepted 제외 aging |
| `KRI-ENS-D15-057` | Backup Restore Success | 실제 restore drill 성공률 |
| `KRI-ENS-D15-058` | Config Drift | golden config 대비 변경 |
| `KRI-ENS-D15-059` | Stale-source Ratio | 유효일 지난 rule/source 비율 |
| `KRI-ENS-D15-060` | Uncited Decision Input | source 없는 AI output 비율 |
| `KRI-ENS-D15-061` | Human Override Rate | 자동권고 이상 신호; 높고 낮음 모두 분석 |
| `KRI-ENS-D15-062` | Data Quality Exception Aging | 미해결 lineage/unit/state 오류 |

---
