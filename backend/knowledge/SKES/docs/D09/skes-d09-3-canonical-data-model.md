---
id: skes-d09-3-canonical-data-model
title: Canonical Data Model
summary: "E&S 사업의 고객, 계약, 관계, 수요 등 주요 데이터의 필드와 구조를 정의한 스키마"
tags: [d09, customer, schema]
keywords: [데이터스키마, 고객마스터, 관계마스터, 계약정보, 수요기록, 서비스이벤트, 정규화, offtaker, PPA, YAML]
related: []
priority: normal
domain: D09
section: 3
source: SK이노베이션E&S_D09_Customers_Orders_Contracts_Demand_and_Relationships.md
breadcrumb: ""
tokens: 969
updated: 2026-08-06
---

> SK이노베이션 E&S · D09 고객·수요·계약·Offtake

# 3. Canonical Data Model

## 3.1 Customer Master

```yaml
customer_id: CUS-ENS-D09-0001
legal_name: string
display_name: string
customer_type: CORPORATE_OFFTAKER | HOUSEHOLD | INDUSTRIAL | UTILITY | MARKET_OPERATOR | MUNICIPALITY | SITE_HOST | FLEET_OPERATOR | INTERNAL_AFFILIATE
segment: LNG | POWER | HEAT | CITY_GAS | PPA | BESS | EV_CHARGING | HYDROGEN | CCS
country_region: string
parent_group_id: string|null
public_or_private: PUBLIC | PRIVATE | MIXED
relationship_owner_org: string
pii_presence: NONE | LOW | HIGH
status: PROSPECT | NEGOTIATION | CONTRACTED | OPERATING | SUSPENDED | ENDED | PLAN_ONLY
evidence_status: string
source_ids: []
```

## 3.2 Relationship Master

```yaml
relationship_id: REL-ENS-D09-0001
customer_id: CUS-ENS-D09-0001
seller_entity_id: string
relationship_type: PPA_OFFTAKE | REGULATED_SUPPLY | MARKET_PARTICIPATION | UTILITY_SERVICE | SITE_HOST | MOU | INTERNAL_TRANSFER | O_AND_M | CHARGING_SERVICE | HYDROGEN_SUPPLY | CCS_CHAIN
start_date: date|null
end_date: date|null
state: DISCLOSED_CONTRACT | DISCLOSED_RELATIONSHIP | MARKET_PARTICIPATION | MOU_OR_PLAN | OPERATING_CASE
commercial_commitment: FIRM | CONDITIONAL | NON_BINDING | UNKNOWN
asset_ids: []
product_ids: []
data_access_right: CONFIRMED | LIMITED | UNKNOWN
source_ids: []
```

## 3.3 Contract Demand Record

```yaml
demand_id: DEM-ENS-D09-0001
contract_id: CTR-ENS-D09-0001
customer_id: CUS-ENS-D09-0001
commodity: LNG | ELECTRICITY | HEAT | CITY_GAS | REC | BESS_SERVICE | CHARGING | HYDROGEN | CO2_STORAGE
period_start: datetime
period_end: datetime
demand_stage: CONTRACT_MAX | FORECAST | NOMINATION | FIRM_ORDER | DISPATCH | METERED | SETTLED
quantity: number|null
unit: MW | MWh | Gcal | Nm3 | MMBtu | kgH2 | tCO2 | session
confidence: number|null
version: string
weather_scenario: string|null
price_index_id: string|null
source_system: string
```

## 3.4 Customer Service Event

```yaml
service_event_id: EVT-ENS-D09-0001
customer_id: string
service_point_id: string
channel: WEB | APP | CALL | FIELD | API | MARKET_GATEWAY
event_type: MOVE_IN | MOVE_OUT | BILLING | PAYMENT | OUTAGE | LEAK_REPORT | METER | CONTRACT_CHANGE | CHARGE_FAILURE | CLAIM
opened_at: datetime
closed_at: datetime|null
severity: S0 | S1 | S2 | S3 | S4
first_contact_resolution: boolean|null
root_cause_code: string|null
asset_id: string|null
privacy_class: PUBLIC | INTERNAL | PERSONAL | SENSITIVE
```

## 3.5 Contract Header and Obligation

```yaml
contract_id: CTR-ENS-D09-0001
relationship_id: REL-ENS-D09-0001
contract_type: PPA | GAS_SUPPLY | HEAT_SUPPLY | MARKET_REGISTRATION | CAPACITY | NWA | CHARGING_SAAS | HYDROGEN_SUPPLY | MOU
effective_date: date|null
term_end: date|null
volume_basis: FIXED | TAKE_OR_PAY | PAY_AS_USED | MARKET_DISPATCH | CAPACITY_PAYMENT | UNKNOWN
price_visibility: PUBLIC | CONFIDENTIAL | UNKNOWN
settlement_interval: string|null
delivery_point: string|null
meter_id: string|null
credit_support: string|null
change_control: string|null
termination_right: string|null
source_ids: []
```

## 3.6 Demand-State Reconciliation Rule

`CONTRACT_MAX → BASE_FORECAST → CUSTOMER_NOMINATION → FIRM_ORDER/DISPATCH → METERED_DELIVERY → ACCEPTED/SETTLED → ADJUSTMENT`

각 상태는 같은 수요의 버전이지 동일한 값이 아니다. AI가 계약 최대량을 실제 매출로 환산하거나, 시장 dispatch를 고객 forecast로 덮어쓰지 못하도록 별도 테이블과 lineage를 유지한다.

---
