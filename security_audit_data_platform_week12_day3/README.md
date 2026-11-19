# Security Audit on Data Platform
**Role:** Data Analyst Intern  
**Week:** 12 — Day 3  
**Task:** Security Audit on Data Platform

## Objective
Review a sample data-platform environment for common security risks: excessive privileges, inactive accounts, weak credential hygiene indicators, sensitive-data exposure, and audit-log coverage.

> This is a training/demo audit using synthetic data. It does not connect to or modify a production platform.

## Folder contents
- `sql/security_audit_checks.sql` — reusable audit queries (PostgreSQL-style examples)
- `data/` — synthetic audit inputs
- `reports/audit_findings.csv` — issue register with severity and recommendations
- `reports/audit_summary.md` — executive summary and detailed findings
- `worklog.md` — work process, time estimate, and tools used

## How to run the SQL
The script uses the illustrative tables in `data/schema_reference.sql`. In a real audit, map these checks to the platform's catalog views and identity/access-management tables.

1. Review `data/schema_reference.sql` to understand the sample table definitions.
2. Run the setup file in a PostgreSQL sandbox if desired.
3. Run `sql/security_audit_checks.sql`.
4. Compare the results with the findings register and document remediation.

## Audit scope
- User and account status
- Role grants and privileged access
- Least-privilege review
- Sensitive data permissions
- Audit-log coverage / retention

## Audit limitations
This sample audit cannot validate MFA, network controls, encryption configuration, real credential age, actual log retention, or whether the sample privileges are operationally enforced. These should be confirmed through platform configuration and security-team evidence.
