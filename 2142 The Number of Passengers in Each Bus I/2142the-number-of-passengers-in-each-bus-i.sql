
SELECT
    T.bus_id,
    COUNT(p.passenger_id) AS passengers_cnt
FROM
    (
    SELECT
        b.bus_id,
        b.arrival_time,
        coalesce(LAG(b.arrival_time,1) OVER (ORDER BY b.arrival_time),0) as prev_arrival_time
    FROM
        Buses b
    ) T
    LEFT JOIN Passengers p
    ON p.arrival_time <= T.arrival_time AND p.arrival_time > T.prev_arrival_time
GROUP BY 1
ORDER BY 1