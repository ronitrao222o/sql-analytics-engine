SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(quantity * price) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
