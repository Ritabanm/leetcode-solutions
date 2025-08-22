-- Write your PostgreSQL query statement below

WITH ranked AS (
select *,
count(1) over (partition by username ) as total,
rank() over (partition by username order by startdate desc) as rn
from useractivity
)



SELECT username, 
       MAX(activity) AS activity, 
       MAX(startdate) AS startdate, 
       MAX(enddate) AS enddate
FROM ranked
WHERE rn = 2 or total = 1
GROUP BY username
ORDER BY username