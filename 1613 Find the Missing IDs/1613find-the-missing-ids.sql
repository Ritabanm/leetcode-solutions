WITH RECURSIVE seq AS (
    SELECT 1 AS value UNION ALL SELECT value + 1 FROM seq WHERE value < (SELECT MAX(customer_id) FROM Customers))
SELECT DISTINCT s.value AS ids
FROM seq s, Customers c
WHERE s.value not in (SELECT customer_id FROM Customers)
ORDER BY 1 ASC;