WITH RECURSIVE Tab AS
(SELECT 1 as month UNION ALL SELECT month+1 FROM Tab WHERE month<=11),

TOT AS (
SELECT
        t.month, IFNULL(SUM(ride_distance),0) as dist, IFNULL(SUM(ride_duration),0) as dur
FROM
        Rides r
JOIN    AcceptedRides a
        ON a.ride_id = r.ride_id AND YEAR(requested_at)=2020
RIGHT JOIN Tab t
        ON MONTH(r.requested_at) = t.month
GROUP BY 1 ORDER BY 1)

SELECT a.month, ROUND((a.dist+b.dist+c.dist)/3,2) as average_ride_distance, ROUND((a.dur+b.dur+c.dur)/3,2) as average_ride_duration
FROM TOT a
JOIN TOT b ON a.month=b.month-1
JOIN TOT c ON a.month=c.month-2
GROUP BY 1 ORDER BY 1