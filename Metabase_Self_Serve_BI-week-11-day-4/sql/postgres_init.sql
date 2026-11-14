CREATE TABLE IF NOT EXISTS sales_performance (
    order_date DATE,
    year INTEGER,
    month INTEGER,
    region TEXT,
    product_category TEXT,
    orders INTEGER,
    sales NUMERIC(14,2),
    profit NUMERIC(14,2)
);
