-- Synthetic audit reference schema for PostgreSQL training.
CREATE TABLE audit_users (
    user_id INT PRIMARY KEY,
    username TEXT,
    account_status TEXT,          -- ACTIVE / DISABLED
    last_login DATE,
    service_account BOOLEAN
);

CREATE TABLE audit_roles (
    role_name TEXT PRIMARY KEY,
    privilege_level TEXT          -- READ / WRITE / ADMIN
);

CREATE TABLE user_role_grants (
    username TEXT,
    role_name TEXT,
    grant_date DATE,
    granted_by TEXT
);

CREATE TABLE data_assets (
    asset_name TEXT PRIMARY KEY,
    contains_sensitive_data BOOLEAN,
    classification TEXT            -- PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED
);

CREATE TABLE asset_permissions (
    username TEXT,
    asset_name TEXT,
    permission TEXT               -- SELECT / INSERT / UPDATE / DELETE / ALL
);

CREATE TABLE audit_log_config (
    event_type TEXT,
    logging_enabled BOOLEAN,
    retention_days INT
);

-- Example training data (synthetic only).
INSERT INTO audit_users VALUES
(1,'analyst_jane','ACTIVE','2026-11-10',FALSE),
(2,'etl_service','ACTIVE','2026-11-17',TRUE),
(3,'temp_user','ACTIVE','2026-06-01',FALSE),
(4,'former_staff','DISABLED','2026-03-12',FALSE),
(5,'admin_ops','ACTIVE','2026-11-18',FALSE);

INSERT INTO audit_roles VALUES
('analyst_read','READ'),
('etl_write','WRITE'),
('platform_admin','ADMIN');

INSERT INTO user_role_grants VALUES
('analyst_jane','analyst_read','2026-01-15','admin_ops'),
('etl_service','etl_write','2026-01-15','admin_ops'),
('temp_user','platform_admin','2026-04-01','admin_ops'),
('admin_ops','platform_admin','2025-12-01','security_admin');

INSERT INTO data_assets VALUES
('customer_profiles',TRUE,'RESTRICTED'),
('sales_summary',FALSE,'INTERNAL'),
('employee_records',TRUE,'CONFIDENTIAL'),
('product_catalog',FALSE,'PUBLIC');

INSERT INTO asset_permissions VALUES
('analyst_jane','sales_summary','SELECT'),
('analyst_jane','customer_profiles','SELECT'),
('etl_service','sales_summary','INSERT'),
('temp_user','customer_profiles','ALL'),
('former_staff','employee_records','SELECT'),
('admin_ops','customer_profiles','ALL');

INSERT INTO audit_log_config VALUES
('authentication',TRUE,180),
('role_changes',TRUE,180),
('data_access',FALSE,0),
('data_exports',FALSE,0);
