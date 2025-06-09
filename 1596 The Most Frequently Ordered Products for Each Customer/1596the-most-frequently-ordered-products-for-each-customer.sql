# Write your MySQL query statement below

WITH CTE AS(
SELECT * 
        ,DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY product_count DESC) AS rnk
FROM (
SELECT customer_id
        ,product_id
        ,COUNT(product_id) AS product_count
FROM Orders
GROUP BY customer_id, product_id
)a    
)
SELECT c.customer_id
        ,c.product_id
        ,p.product_name
FROM CTE c
JOIN Products p
ON c.product_id=p.product_id
WHERE c.rnk=1
