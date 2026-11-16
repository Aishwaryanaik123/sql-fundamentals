# ADR-001: Layered Analytics Platform

**Status:** Proposed reference design; not deployed.

## Context
A production analytics workflow may combine databases, files, and APIs; data preparation; SQL/Python transformations; dashboards; and optional forecasting or ML. It needs traceability, quality gates, controlled access, and reliable operations.

## Decision
Use modular layers:
1. Sources and approved inputs.
2. Ingestion/orchestration with retries and idempotency.
3. Raw landing storage and curated SQL/warehouse tables.
4. Version-controlled transformations and automated quality checks.
5. BI/analytics and optional ML with dataset/model versioning.
6. Governed dashboards and approved exports.
7. Cross-cutting identity, secrets, encryption, audit, monitoring, backup, CI/CD, and cost controls.

Technology choices remain capability-based until organization standards, workload, budget, and security needs are confirmed.

## Alternatives
- Spreadsheet-only reporting: quick start, weak repeatability and governance.
- Direct BI access to operational DBs: simple, but risks source load and inconsistent logic.
- One monolithic script: initially simple, harder to test, monitor, and maintain.

## Consequences
Benefits: clearer ownership, reproducibility, quality, safer access, and scale.
Trade-offs: added setup, monitoring, documentation, and operating cost.

## Open questions
Cloud/provider, data classification, data volume, user count, refresh SLA, RPO/RTO, budget, and operational ownership are not supplied.
