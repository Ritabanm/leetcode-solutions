# Write your MySQL query statement below

WITH RECURSIVE cte AS (
    SELECT  ROW_NUMBER() OVER (ORDER BY hall_id, start_day) AS id,
            hall_id,
            start_day,
            end_day
    FROM HallEvents
), cte2 AS (
    SELECT  id,
            hall_id,
            start_day,
            end_day
    FROM cte
    WHERE id = 1

    UNION ALL

    SELECT  cte.id,
            cte.hall_id,
            (CASE WHEN cte.hall_id = cte2.hall_id AND DATEDIFF(cte2.end_day,cte.start_day)>=0 THEN cte2.start_day ELSE cte.start_day END) AS start_day,
            (CASE WHEN cte.hall_id = cte2.hall_id AND DATEDIFF(cte2.end_day,cte.start_day)>=0 THEN GREATEST(cte2.end_day,cte.end_day) ELSE cte.end_day END) AS end_day
    FROM cte2 JOIN cte ON cte2.id + 1 = cte.id
)

SELECT  hall_id,
        start_day,
        MAX(end_day) AS end_day
FROM cte2
GROUP BY hall_id, start_day
