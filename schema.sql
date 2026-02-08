CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    customer_id TEXT,
    product TEXT,
    category TEXT,
    order_date DATE,
    quantity INTEGER,
    price REAL
);

CREATE INDEX IF NOT EXISTS idx_sales_order_date
ON sales(order_date);

CREATE INDEX IF NOT EXISTS idx_sales_customer_id
ON sales(customer_id);
