# Security Audit — Summary Report

## Executive summary
A training review of the sample data platform identified **4 high-severity** and **2 medium-severity** control concerns. The most important risks are retained access for a disabled account, an inactive user with administrator privileges, overly broad permissions on restricted customer data, and missing data-access/export logging.

## Scope and method
Reviewed sample user/account status, role assignments, asset permissions, data classification, and audit-event configuration. Used SQL checks aligned to least privilege and access-review practices. All data is synthetic.

## Findings
| ID | Severity | Finding | Recommended action |
|---|---|---|---|
| F-01 | High | Disabled account retains access to employee records | Revoke permission and validate offboarding |
| F-02 | High | Inactive account retains platform-admin role | Confirm owner; disable/revoke if no business need |
| F-03 | High | `ALL` permission on restricted customer data | Replace with minimum necessary grants |
| F-04 | High | Access/export logging disabled | Enable logging, test alerts, and verify retention |
| F-05 | Medium | Analyst has direct access to restricted customer profiles | Verify need; prefer masking/aggregated access |
| F-06 | Medium | Grant approval/owner evidence needs review | Keep access-review and approval records |

## Priority remediation plan
1. **Immediately:** revoke access for disabled accounts and review inactive privileged users.
2. **High priority:** replace broad permissions with least-privilege access.
3. **High priority:** enable data-access and export audit events; validate log retention and alerting.
4. **Next review cycle:** check sensitive-data access justification, role owners, and approvals.
5. **Ongoing:** conduct quarterly access reviews and track remediation to closure.

## Conclusion
The sample environment demonstrates why account lifecycle management, least-privilege access, sensitive-data controls, and complete audit logging are essential. Remediation should be verified by rerunning audit queries and retaining evidence of approved changes.

## Limitations
This is a sample audit, not a certification or production assessment. It does not verify MFA, encryption at rest/in transit, network segmentation, secrets management, endpoint security, real log retention, or platform-specific settings.
