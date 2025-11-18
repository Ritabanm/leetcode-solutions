# Write your MySQL query statement below
WITH CTE AS(
    SELECT state, SUM(LEFT(state,1)=LEFT(city,1)) matching_letter_count, COUNT(*) CNT
    FROM cities
    GROUP BY 1
)

SELECT S.state, GROUP_CONCAT(city order by city SEPARATOR ', ' ) cities, matching_letter_count
FROM CTE JOIN cities S USING(state)
WHERE matching_letter_count >=1 AND CNT >=3
GROUP BY 1
order by matching_letter_count desc, 1