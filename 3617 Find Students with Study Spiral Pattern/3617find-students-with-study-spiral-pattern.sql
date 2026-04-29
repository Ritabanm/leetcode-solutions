WITH cte AS (
    SELECT
        *,
        session_date - LAG(session_date) OVER(PARTITION BY student_id ORDER BY session_date) AS session_delta
    FROM study_sessions
)
SELECT
    t.student_id,
    MAX(s.student_name) AS student_name,
    MAX(s.major) AS major,
    COUNT(DISTINCT t.subject) AS cycle_length,
    SUM(t.hours_studied) AS total_study_hours
FROM cte t
JOIN students s USING (student_id)
GROUP BY student_id
HAVING MAX(session_delta) <= 2
    AND COUNT(DISTINCT subject) >= 3
    AND COUNT(*) >= 6
ORDER BY cycle_length DESC, total_study_hours DESC;