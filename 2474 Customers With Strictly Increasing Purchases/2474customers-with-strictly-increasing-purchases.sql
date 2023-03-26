# Write your MySQL query statement below
WITH table_year AS (
SELECT
    customer_id, 
    YEAR(order_date) AS order_year,
    SUM(price) AS total_price
FROM
    Orders
GROUP BY 
    customer_id, YEAR(order_date)), 

    table_lag_price AS (
SELECT
    customer_id,
    order_year, 
    total_price,
    LAG(total_price) OVER(PARTITION BY customer_id ORDER BY order_year) AS lag_price,
    LAG(order_year) OVER(PARTITION BY customer_id ORDER BY order_year) AS lag_year
FROM
    table_year),

    temp_table AS (
SELECT 
    customer_id,
    order_year - lag_year AS yr_diff,
    total_price - lag_price AS price_diff
FROM 
    table_lag_price
WHERE
    lag_price IS NOT NULL)

SELECT 
    DISTINCT customer_id
FROM
    Orders
WHERE 
    customer_id NOT IN (
                        SELECT
                            customer_id
                        FROM 
                            temp_table
                        WHERE 
                            price_diff <= 0 OR yr_diff > 1);