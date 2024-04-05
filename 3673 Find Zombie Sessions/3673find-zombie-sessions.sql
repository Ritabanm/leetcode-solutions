SELECT
    session_id,
    user_id,
    extract(epoch from max(event_timestamp) - min(event_timestamp)) / 60 as session_duration_minutes,
    count(*) FILTER (WHERE event_type = 'scroll') as scroll_count
FROM 
    app_events
GROUP BY 1, 2
HAVING 
    max(event_timestamp) - interval '30 mins' > min(event_timestamp) 
    AND count(*) FILTER (WHERE event_type = 'scroll') >= 5
    AND ROUND(
        CAST(count(*) FILTER (WHERE event_type = 'click') AS numeric) / 
            CAST(count(*) FILTER (WHERE event_type = 'scroll') AS numeric), 2) < 0.2
    AND count(*) FILTER (WHERE event_type = 'purchase') = 0
ORDER BY scroll_count DESC, session_id ASC