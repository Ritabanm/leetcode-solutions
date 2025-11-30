# Write your MySQL query statement below
WITH ranked AS (
    SELECT o.seller_id, COUNT(DISTINCT o.item_id) AS num_items, RANK() OVER(ORDER BY COUNT(DISTINCT o.item_id) DESC) AS rankk
    FROM Orders o
    JOIN Items i ON o.item_id = i.item_id
    JOIN Users u ON o.seller_id = u.seller_id AND i.item_brand != u.favorite_brand
    GROUP BY o.seller_id
)

SELECT seller_id, num_items
FROM ranked
WHERE rankk = 1
ORDER BY seller_id;