# Write your MySQL query statement below
WITH cte AS(
    SELECT user_id1 AS id1, user_id2 AS id2
    FROM Friends
    UNION ALL
    SELECT user_id2 AS id1, user_id1 AS id2
    FROM Friends
)
SELECT *
FROM Friends
EXCEPT
SELECT f.user_id1, f.user_id2
FROM Friends f
JOIN cte c1
ON f.user_id1 = c1.id1
JOIN cte c2
ON f.user_id2 = c2.id1
WHERE c1.id2 = c2.id2
ORDER BY user_id1, user_id2