-- Security audit checks (PostgreSQL-style, illustrative)
-- Run against the synthetic schema in data/schema_reference.sql.
-- 1) Active accounts that have not logged in for 90+ days
SELECT username, last_login, account_status
FROM audit_users
WHERE account_status = 'ACTIVE'
  AND last_login < CURRENT_DATE - INTERVAL '90 days'
ORDER BY last_login;

-- 2) Privileged role grants (ADMIN)
SELECT g.username, g.role_name, g.grant_date, g.granted_by
FROM user_role_grants g
JOIN audit_roles r USING (role_name)
WHERE r.privilege_level = 'ADMIN'
ORDER BY g.username;

-- 3) Disabled accounts with any role grant (verify and remove stale grants)
SELECT u.username, g.role_name
FROM audit_users u
JOIN user_role_grants g USING (username)
WHERE u.account_status = 'DISABLED';

-- 4) Direct access to sensitive assets
SELECT p.username, p.asset_name, p.permission, a.classification
FROM asset_permissions p
JOIN data_assets a USING (asset_name)
WHERE a.contains_sensitive_data = TRUE
ORDER BY a.classification DESC, p.username;

-- 5) Broad permissions (ALL) on sensitive assets
SELECT p.username, p.asset_name, p.permission
FROM asset_permissions p
JOIN data_assets a USING (asset_name)
WHERE a.contains_sensitive_data = TRUE
  AND p.permission = 'ALL';

-- 6) Audit coverage and retention gaps
SELECT event_type, logging_enabled, retention_days
FROM audit_log_config
WHERE logging_enabled = FALSE OR retention_days < 90;

-- 7) Permissions outside least-privilege principle: non-admin users with write/delete
SELECT p.username, p.asset_name, p.permission
FROM asset_permissions p
LEFT JOIN user_role_grants g USING (username)
LEFT JOIN audit_roles r USING (role_name)
WHERE p.permission IN ('INSERT','UPDATE','DELETE','ALL')
  AND COALESCE(r.privilege_level,'') <> 'ADMIN';
