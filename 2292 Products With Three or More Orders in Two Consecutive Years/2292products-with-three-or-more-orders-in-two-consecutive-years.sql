WITH GROUPED AS (
    SELECT product_id, YEAR(purchase_date) AS year, COUNT(order_id) AS orders
    FROM Orders
    GROUP BY product_id, YEAR(purchase_date)
    HAVING COUNT(order_id) >= 3
)

SELECT DISTINCT g1.product_id
FROM GROUPED g1
JOIN GROUPED g2 ON g1.year = g2.year+1 AND g1.product_id = g2.product_id