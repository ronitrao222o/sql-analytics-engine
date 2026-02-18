SELECT
    ROUND(SUM(quantity * price) * 1.0 / COUNT(order_id), 2) AS average_order_value
FROM sales;
