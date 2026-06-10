-- ENUMS --

CREATE TYPE vendor_name AS ENUM (
    'adobe',
    'microsoft'
);

CREATE TYPE adobe_plan_type AS ENUM (
    'individual',
    'teams',
    'enterprise_etla',
    'unsure'
);
 
CREATE TYPE adobe_sku_type AS ENUM (
    'all_apps',
    'single_app',
    'acrobat'
);
 
CREATE TYPE primary_use_case AS ENUM (
    'graphic',
    'video_editing',
    'marketing',
    'pdf_editing_only',
    'esign_workflows',
    'light_use'
);
 
CREATE TYPE m365_plan_type AS ENUM (
    'microsoft_365_business_basic',
    'microsoft_365_business_standard',
    'microsoft_365_business_premium'
);

CREATE TYPE subscription_term AS ENUM (
    'monthly',
    'annual_paid_monthly',
    'annual_prepaid',
    'multi_year'
);
 
CREATE TYPE subscription_status AS ENUM (
    'active',
    'inactive',
    'cancelled',
    'past_due',
    'trialing'
);
 
CREATE TYPE billing_cycle AS ENUM (
    'monthly',
    'annual'
);
 
CREATE TYPE conversation_status AS ENUM (
    'in_progress',
    'completed',
    'recommended',
    'archived'
);
 
CREATE TYPE migration_path AS ENUM (
    'none',
    'individual_to_teams_vip',
    'individual_to_enterprise',
    'teams_to_enterprise',
    'consolidate_renewals',
    'm365_basic_to_standard',
    'm365_standard_to_premium',
    'other'
);
 
CREATE TYPE order_type AS ENUM (
    'new',
    'upgrade',
    'downgrade',
    'renewal',
    'cancellation'
);
 
CREATE TYPE order_status AS ENUM (
    'pending',
    'processing',
    'completed',
    'failed',
    'cancelled'
);
 
CREATE TYPE payment_status AS ENUM (
    'pending',
    'paid',
    'failed',
    'refunded'
);
 
CREATE TYPE tool_call_status AS ENUM (
    'success',
    'failed',
    'pending'
);
 
 
-- TABLES --

CREATE TABLE customers(
         id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 name             VARCHAR,
		 email            VARCHAR UNIQUE,
		 company          VARCHAR,
		 Phone            VARCHAR,
		 preferences      JSONB,
		 created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
		 updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE plans(
         id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 vendor           vendor_name NOT NULL,
		 plan_name        VARCHAR NOT NULL,
		 plan_tier        VARCHAR,
		 sku_code         VARCHAR UNIQUE,
		 price_monthly    DECIMAL,
		 price_annual     DECIMAL,
		 max_users        INTEGER,
		 features         JSONB,
		 upgrade_paths    JSONB,
		 is_active        BOOLEAN NOT NULL DEFAULT TRUE,
		 updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE subscriptions(
         id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 customer_id      UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
		 plan_id          UUID NOT NULL REFERENCES plans(id) ON DELETE RESTRICT,
		 vendor           vendor_name,
         status           subscription_status,
         seat_count       INTEGER,
         seats_used       INTEGER,
         billing_cycle    billing_cycle,
         renewal_date     DATE,
         start_date       DATE,
         auto_renew       BOOLEAN,
         metadata         JSONB,
         created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
         updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE orders(
         id                       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 customer_id              UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
		 subscription_id          UUID NOT NULL REFERENCES subscriptions(id) ON DELETE CASCADE,
		 target_plan_id           UUID NOT NULL REFERENCES plans(id) ON DELETE RESTRICT,
		 order_type               order_type,
		 status	                  order_status,
		 amount                   DECIMAL,
		 currency                 VARCHAR,
		 stripe_session_id        VARCHAR,
		 stripe_payment_intent    VARCHAR,
		 order_details            JSONB,
		 created_at               TIMESTAMPTZ NOT NULL DEFAULT now(),
		 updated_at               TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE payments (
         id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
         order_id                UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
         stripe_payment_id       VARCHAR,
         status                  payment_status,
         amount                  DECIMAL,
         currency                VARCHAR,
         payment_method          VARCHAR,
         receipt_url             TEXT,
         paid_at                 TIMESTAMPTZ,
         created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE conversations(
         id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 customer_id             UUID NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
		 tavus_conversation_id   VARCHAR,
		 persona_id              VARCHAR,
		 status                  conversation_status,
		 duration_seconds        INTEGER,
		 context_snapshot        JSONB,
		 started_at              TIMESTAMPTZ NOT NULL DEFAULT now(),
		 ended_at                TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE transcripts(
         id                     UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 conversation_id        UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE, 
		 messages               JSONB,
		 summary                TEXT,
		 action_items           JSONB,
		 created_at             TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE tool_calls(
         id                     UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		 conversation_id        UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
		 tool_name              VARCHAR,
		 arguments              JSONB,
		 result                 JSONB,
		 status                 tool_call_status,
		 called_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- INDEXES --

CREATE INDEX idx_subscription_customer ON subscriptions(customer_id);
CREATE INDEX idx_subscription_plan ON subscriptions(plan_id);
CREATE INDEX idx_subscription_vendor ON subscriptions(vendor);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_order_subscription ON orders(subscription_id);
CREATE INDEX idx_payments_order ON payments(order_id);
CREATE INDEX idx_conversation_customer ON conversations(customer_id);
CREATE INDEX idx_transcripts_conv ON transcripts(conversation_id);
CREATE INDEX idx_tool_calls_conv ON tool_calls(conversation_id);
CREATE INDEX idx_plans_vendor ON plans(vendor);

-- Triggers -- 

CREATE OR REPLACE FUNCTION set_updated_at() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_customers_updated BEFORE UPDATE ON customers
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_plans_updated BEFORE UPDATE ON plans
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER trg_subscriptions_updated BEFORE UPDATE ON subscriptions
  FOR EACH ROW EXECUTE FUNCTION set_updated_at();

INSERT INTO plans (vendor, plan_name, plan_tier, sku_code, price_monthly, price_annual, max_users, features, upgrade_paths) VALUES
 
('adobe', 'Creative Cloud All Apps', 'teams', 'CC_ALL_APPS_TEAMS',
    84.99, 899.88, NULL,
    '{"apps": ["Photoshop", "Illustrator", "Premiere Pro", "After Effects", "InDesign", "XD", "Acrobat Pro"], "storage": "1TB", "support": "24/7"}',
    '{"upgrade_to": ["enterprise_etla"]}'
),
 
('adobe', 'Creative Cloud All Apps', 'individual', 'CC_ALL_APPS_IND',
    59.99, 599.88, 1,
    '{"apps": ["Photoshop", "Illustrator", "Premiere Pro", "After Effects", "InDesign", "XD"], "storage": "100GB", "support": "standard"}',
    '{"upgrade_to": ["CC_ALL_APPS_TEAMS"]}'
),
 
('adobe', 'Acrobat Pro', 'teams', 'ACROBAT_PRO_TEAMS',
    23.99, 239.88, NULL,
    '{"apps": ["Acrobat Pro"], "features": ["PDF edit", "eSign", "OCR", "redact"], "storage": "100GB"}',
    '{"upgrade_to": ["CC_ALL_APPS_TEAMS"]}'
),
 
('adobe', 'Acrobat Standard', 'individual', 'ACROBAT_STD',
    12.99, 155.88, 1,
    '{"apps": ["Acrobat Standard"], "features": ["PDF edit", "basic eSign"], "storage": "2GB"}',
    '{"upgrade_to": ["ACROBAT_PRO_TEAMS"]}'
),
 
('adobe', 'Premiere Pro', 'individual', 'PREMIERE_PRO',
    54.99, 599.88, 1,
    '{"apps": ["Premiere Pro"], "features": ["video editing", "color grading", "audio tools"], "storage": "100GB"}',
    '{"upgrade_to": ["CC_ALL_APPS_TEAMS"]}'
),
 
('adobe', 'Photoshop', 'individual', 'PHOTOSHOP',
    22.99, 263.88, 1,
    '{"apps": ["Photoshop"], "features": ["photo editing", "compositing", "AI tools"], "storage": "100GB"}',
    '{"upgrade_to": ["CC_ALL_APPS_TEAMS"]}'
),
 
-- MICROSOFT 365 BUSINESS PLANS
('microsoft', 'Microsoft 365 Business Basic', 'business_basic', 'M365_BUS_BASIC',
    6.00, 60.00, 300,
    '{"apps": ["Teams", "Exchange", "SharePoint", "OneDrive"], "storage": "1TB OneDrive", "email": true, "desktop_apps": false, "support": "standard"}',
    '{"upgrade_to": ["M365_BUS_STD", "M365_BUS_PREM"]}'
),
 
('microsoft', 'Microsoft 365 Business Standard', 'business_standard', 'M365_BUS_STD',
    12.50, 150.00, 300,
    '{"apps": ["Teams", "Exchange", "SharePoint", "OneDrive", "Word", "Excel", "PowerPoint", "Outlook", "Access"], "storage": "1TB OneDrive", "email": true, "desktop_apps": true, "webinars": true, "support": "standard"}',
    '{"upgrade_to": ["M365_BUS_PREM"]}'
),
 
('microsoft', 'Microsoft 365 Business Premium', 'business_premium', 'M365_BUS_PREM',
    22.00, 264.00, 300,
    '{"apps": ["Teams", "Exchange", "SharePoint", "OneDrive", "Word", "Excel", "PowerPoint", "Outlook", "Access", "Intune", "Azure AD Premium"], "storage": "1TB OneDrive", "email": true, "desktop_apps": true, "advanced_security": true, "device_management": true, "support": "priority"}',
    '{"upgrade_to": []}'
);

SELECT c.name, c.email, p.plan_name, s.renewal_date, s.status
FROM subscriptions s
JOIN customers c ON c.id = s.customer_id
JOIN plans p ON p.id = s.plan_id
WHERE p.vendor = 'adobe';