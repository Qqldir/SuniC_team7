---
id: skon-d06-d06-48-factory-cybersecurity
title: Factory Cybersecurity
summary: "제조공정의 OT 보안 아키텍처, 제어 기준, 공급업체 접근 관리, AI 보안, 사건 복구를 다루는 종합 사이버보안 가이드."
tags: [d06, process, schema]
keywords: [OT 보안, 운영기술, PLC, 산업용 DMZ, 벤더 원격 접근, 제조 AI, 보안 통제, 인시던트 대응, OT, 산업 DMZ, 공급업체 접근, 원격 점검, 다중 인증, AI 위협, 센서 공격, 사건 복구, 공정 안전]
related: []
priority: normal
domain: D06
section: D06-48.
source: SK온_D06_Manufacturing_Process_and_Operations.md
breadcrumb: ""
tokens: 976
updated: 2026-08-03
---

> SK온 · D06 제조공정·운영

# D06-48. Factory Cybersecurity

## 48.1 OT Zone Architecture

```text
Enterprise IT
      ↓
Industrial DMZ
      ↓
Site Manufacturing Operations
      ↓
Area / Line OT Zone
      ↓
Cell / Equipment Zone
      ↓
Safety System
```

NIST는 OT 보안에서 일반 IT 보안뿐 아니라 공정의 안전·신뢰성·가용성을 고려하도록 요구하며, 제조환경의 보안분리는 공격이나 오작동의 확산을 제한하는 핵심 수단이다. ([NIST][9])

---

## 48.2 OT Security Control Master

```yaml
ot_security_controls:

  asset_management:
    - PLC, robot, sensor and industrial PC inventory
    - Firmware and software version
    - Network address and owner
    - Criticality
    - Approved communication path

  network:
    - Zone and conduit
    - Firewall allow list
    - Industrial DMZ
    - Remote-access gateway
    - Unauthorized-device detection

  identity:
    - Named account
    - Role-based privilege
    - Multi-factor authentication for remote access
    - Shared-account elimination
    - Privileged-session recording

  change_control:
    - PLC logic baseline
    - Recipe change
    - Robot program change
    - Firmware update
    - Model deployment
    - Digital signature and rollback

  monitoring:
    - OT network anomaly
    - Controller logic modification
    - Sensor-value anomaly
    - Authentication failure
    - Historian and MES data-integrity event

  recovery:
    - Offline controller backup
    - Golden configuration
    - Spare controller
    - Recovery runbook
    - Isolated restoration test
```

---

## 48.3 Secure Vendor Access

```yaml
secure_remote_access:

  prohibited:
    - Direct internet access to PLC
    - Permanent vendor account
    - Unmonitored remote desktop
    - Unapproved USB
    - Shared generic credential

  required:
    - Approved service ticket
    - Time-limited access
    - Industrial DMZ jump host
    - Multi-factor authentication
    - Session recording
    - Command and file logging
    - Automatic account expiration
    - Post-service configuration verification
```

---

## 48.4 Manufacturing AI Security

```yaml
manufacturing_ai_security:

  threats:
    - Training-data poisoning
    - Label manipulation
    - Model replacement
    - Sensor spoofing
    - Unauthorized threshold change
    - Confidential recipe extraction

  controls:
    - Dataset version and hash
    - Model signature
    - Approved deployment pipeline
    - Shadow validation
    - Feature-distribution monitoring
    - Model rollback
    - Separation of training and production credentials

  automatic_control:
    requirements:
      - Model confidence
      - Valid operating range
      - Independent safety constraints
      - Manual override
      - Immutable decision log
```

---

## 48.5 OT Incident Recovery Record

```yaml
ot_incident_record:

  detection:
    - Incident ID
    - Detection source
    - Affected zone
    - Initial time

  operational_impact:
    - Equipment stopped
    - Product and WIP affected
    - Safety impact
    - Data-integrity impact

  containment:
    - Network isolation
    - Account disablement
    - Equipment safe state
    - Production hold

  recovery:
    - Configuration restoration
    - Firmware or software verification
    - Sensor validation
    - Trial production
    - Quality release

  post_incident:
    - Root cause
    - Vulnerability
    - Corrective action
    - Model and rule update
```

---
