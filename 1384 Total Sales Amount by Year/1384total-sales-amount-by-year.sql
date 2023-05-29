# Write your MySQL query statement below
WITH RECURSIVE enumerate_year AS (
    SELECT MIN(YEAR(period_start)) AS report_year
    FROM Sales
    UNION ALL
    SELECT report_year + 1 AS report_year
    FROM enumerate_year
    WHERE report_year < (
        SELECT MAX(YEAR(period_end))
        FROM Sales
    )
)
SELECT 
    product_id,
    product_name,
    CAST(report_year AS CHAR) AS report_year,
    average_daily_sales
        * (1+DATEDIFF(
            LEAST(DATE(CONCAT(report_year,'-12-31')), period_end),
            GREATEST(MAKEDATE(report_year, 1), period_start) 
        )) AS total_amount
FROM enumerate_year
LEFT JOIN Sales
ON YEAR(period_start) <= report_year AND YEAR(period_end) >= report_year
LEFT JOIN Product
USING (product_id)
ORDER BY product_id, report_year