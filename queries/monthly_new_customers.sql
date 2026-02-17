WITH first_orders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM sales
    GROUP BY customer_id
)

SELECT
    strftime('%Y-%m', first_order_date) AS month,
    COUNT(customer_id) AS new_customers
FROM first_orders
GROUP BY month
ORDER BY month;
