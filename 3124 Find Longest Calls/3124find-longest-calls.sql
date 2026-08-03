-- Write your PostgreSQL query statement below
WITH call_duration_ranked AS (
SELECT 
    contact_id,
    type,
    dense_rank() over(partition by type ORDER BY duration DESC) AS rnk,
    duration
FROM calls )
SELECT
    c.first_name,
    type,
    to_char(make_interval(secs => cdr.duration), 'HH24:MI:SS') AS duration_formatted
FROM contacts c
INNER JOIN call_duration_ranked cdr
ON c.id = cdr.contact_id
AND cdr.rnk <= 3
ORDER BY type DESC, duration DESC, first_name DESC
