WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', order_date) AS month,
        customer_id,
        SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY month, customer_id
)

SELECT
    month,
    customer_id,
    revenue,
    RANK() OVER (
        PARTITION BY month
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM monthly_revenue
ORDER BY month, revenue_rank;
