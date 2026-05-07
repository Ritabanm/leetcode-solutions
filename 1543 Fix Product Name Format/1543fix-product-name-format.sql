# Write your MySQL query statement below
SELECT TRIM(LOWER(product_name)) AS product_name,LEFT(sale_date,7) AS sale_date,COUNT(*) AS total
FROM Sales
GROUP BY 1,2
ORDER BY 1 ASC,2 ASC