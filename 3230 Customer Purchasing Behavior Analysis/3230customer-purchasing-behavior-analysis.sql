# Write your MySQL query statement below

WITH cte AS (
    SELECT  customer_id,
            category,
            SUM(amount) AS total_amount,
            COUNT(transaction_id) AS transaction_count,
            RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(transaction_id) DESC, MAX(transaction_date) DESC) AS rank_num
    FROM Transactions JOIN Products USING(product_id)
    GROUP BY customer_id, category
    ORDER BY 1,5
)

SELECT  customer_id,
        SUM(total_amount) AS total_amount,
        SUM(transaction_count) AS transaction_count,
        COUNT(category) AS unique_categories,
        ROUND(SUM(total_amount)/SUM(transaction_count),2) AS avg_transaction_amount,
        category AS top_category,
        SUM(transaction_count)*10 + ROUND(SUM(total_amount)/100,2) AS loyalty_score 
FROM cte 
GROUP BY customer_id
ORDER BY 7 DESC, 1

