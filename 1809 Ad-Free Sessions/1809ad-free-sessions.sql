# Write your MySQL query statement below

SELECT p2.session_id
FROM Playback as p2
WHERE p2.session_id NOT IN 
(
SELECT p.session_id
FROM Playback as p
JOIN Ads as a ON p.customer_id=a.customer_id AND a.timestamp >= p.start_time AND a.timestamp <= p.end_time
)