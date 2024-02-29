# Write your MySQL query statement below
WITH immediate AS (
SELECT order_date, COUNT(*) AS c FROM Delivery WHERE order_date = customer_pref_delivery_date GROUP BY order_date),

total AS (
SELECT order_date, COUNT(*) AS c FROM Delivery GROUP BY order_date)

SELECT b.order_date, COALESCE(ROUND(a.c * 100 / b.c, 2), 0) AS immediate_percentage FROM immediate a RIGHT JOIN total b ON a.order_date = b.order_date ORDER BY order_date

