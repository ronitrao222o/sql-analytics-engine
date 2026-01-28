SELECT
    order_date,
    SUM(quantity * price) AS daily_revenue,
    SUM(SUM(quantity * price)) OVER (ORDER BY order_date) AS running_total
FROM sales
GROUP BY order_date;
