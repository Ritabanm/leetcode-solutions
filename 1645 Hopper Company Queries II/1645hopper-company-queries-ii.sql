# Write your MySQL query statement below

WITH recursive months AS(
    SELECT MONTH(date'2020-01-01') as months, date'2020-01-31' AS dates
    FROM drivers
    UNION
    SELECT months + 1 as months, 
        CASE WHEN DAY(dates) = 29 THEN LAST_DAY(dates + INTERVAL '1' MONTH)
             WHEN DAY(dates) = 30 THEN LAST_DAY(dates + INTERVAL '1' MONTH)
             ELSE DATE_ADD(dates,INTERVAL '1' MONTH) END as dates
    FROM months
    WHERE months <= 11
)
, driver_count AS(
SELECT months, SUM(CASE WHEN join_date <= dates THEN 1 ELSE 0 END) as drivers
FROM months
CROSS JOIN drivers
GROUP BY 1
)
, accepted_count AS(
SELECT MONTH(r.requested_at) as months, COUNT(DISTINCT ar.driver_id) driver_cnt
FROM acceptedrides ar
LEFT JOIN rides r
ON ar.ride_id = r.ride_id
WHERE r.requested_at BETWEEN date'2020-01-01' AND date'2020-12-31'
GROUP BY 1
)
SELECT d.months as month, IFNULL(ROUND(a.driver_cnt/IFNULL(d.drivers,0) * 100,2),0) as working_percentage
FROM driver_count d
LEFT JOIN accepted_count a
ON d.months = a.months
ORDER BY 1