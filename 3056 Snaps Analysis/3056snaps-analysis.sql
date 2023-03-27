# Write your MySQL query statement below
WITH a AS (SELECT ag.age_bucket, ag.user_id, ac.activity_type, ac.time_spent FROM Activities ac LEFT JOIN Age ag ON ac.user_id = ag.user_id),
c AS (SELECT age_bucket, ROUND(SUM(time_spent) * 100 / (SELECT SUM(time_spent) FROM a a_1 WHERE a_1.age_bucket = a.age_bucket), 2) AS send_perc FROM a WHERE activity_type = 'send' GROUP BY age_bucket)

SELECT age_bucket, send_perc, 100 - send_perc AS open_perc FROM c