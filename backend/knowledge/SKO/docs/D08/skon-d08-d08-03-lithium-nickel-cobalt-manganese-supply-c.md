---
id: skon-d08-d08-03-lithium-nickel-cobalt-manganese-supply-c
title: Lithium / Nickel / Cobalt / Manganese Supply Chain — 목적과 경계
summary: "리튬·니켈·코발트·망간의 공급망 추적에서 원소 형태, 계약 상태, 물리 흐름을 구분하는 SK온의 데이터 관리 원칙을 설명한다."
tags: [d08, supply-chain]
keywords: [리튬, 니켈, 코발트, 망간, 원산지, CAM, 공급계약, 배터리, LCE, 조달, 원산지추적, 광산정련, 배터리셀, 양극재, 공개정보, D08-03, 함유금속량]
related: []
priority: normal
domain: D08
section: D08-03
source: SK온_D08_Raw_Materials_Suppliers_Supply_Chain.md
breadcrumb: "SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain"
tokens: 688
updated: 2026-08-03
---

> SK온 · D08 원소재·공급사·공급망 · SK온 D08 — Raw Materials, Suppliers & Supply Chain > Lithium / Nickel / Cobalt / Manganese Supply Chain

### 1. 목적과 경계

D08-03은 리튬·니켈·코발트·망간이 **광산·염호 → 정광·브라인·MHP·수산화물 → 배터리급 금속염 → pCAM/CAM → SK온 셀**로 이동하는 경로를 관리한다. 양극재 공급계약은 D08-02, 전체 계약 원장과 실제 PO·입고실적은 D08-06, 국가·광산·정련 원산지의 상세 노드는 D08-07, 미국 PFE 법적 판정은 D08-08에서 확장한다.

이 모듈은 공개 발표를 실제 조달로 과대 해석하지 않기 위해 다음 원칙을 적용한다.

1. **원소와 제품형태를 분리한다.** `리튬 2.5만t`이라는 발표가 탄산리튬·수산화리튬·LCE 중 무엇인지 밝히지 않으면 `material_id=UNKNOWN`, `disclosed_form=UNSPECIFIED`를 유지한다.
2. **총량·연간량·함유금속량을 분리한다.** 계약 총량, `tpa`, LCE, 수산화리튬 제품톤, 니켈·코발트 함유금속톤을 서로 환산·합산하지 않는다.
3. **계약과 물리 흐름을 분리한다.** 구속력 있는 계약이 있어도 품질인증·첫 출하·실제 drawdown이 확인되지 않으면 `physical_supply_confirmed=false|unknown`이다.
4. **기업 국적·정련국·광산국을 분리한다.** 한국에서 생산한 수산화리튬도 상류 광물 원산지가 공개되지 않으면 한국산 광물로 기록하지 않는다.
5. **프로젝트 설계와 가동을 분리한다.** 발표된 광산·HPAL·DLE 프로젝트 능력은 FID·준공·시운전·상업생산 근거가 없으면 현행 공급능력에 합산하지 않는다.
6. **양극재 계약에서 상류 원산지를 역추론하지 않는다.** CAM 공급사가 확인돼도 Ni·Co·Mn sulfate 공급사와 광산은 별도 증거가 필요하다.
7. **현재 미확인은 부존재가 아니다.** 공개 1차 자료에서 현행 계약을 찾지 못한 경우 `NOT_PUBLICLY_CONFIRMED`로 저장하며, 비공개 구매계약이 없다고 단정하지 않는다.
