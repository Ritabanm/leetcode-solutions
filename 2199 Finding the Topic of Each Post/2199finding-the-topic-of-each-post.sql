-- Using CTE to handle the preliminary matching and final grouping
WITH all_result AS 
(
    -- Selecting posts and topic IDs where keywords are matched as whole words within the content
    SELECT p.post_id, k.topic_id AS topic
    FROM Posts p 
    LEFT JOIN Keywords k 
    ON LOCATE(CONCAT(' ', k.word, ' '), CONCAT(' ', p.content, ' ')) > 0
) 
-- Selecting final results with grouped topic IDs or marking as 'Ambiguous!' if no topics are found
SELECT post_id, 
       CASE 
           WHEN topic IS NULL THEN "Ambiguous!" 
           ELSE GROUP_CONCAT(DISTINCT topic ORDER BY topic) 
       END AS topic
FROM all_result 
GROUP BY post_id;