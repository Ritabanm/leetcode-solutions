# Write your MySQL query statement below
WITH top_performers AS (
    SELECT
        user_id
    FROM course_completions
    GROUP BY user_id
    HAVING
        COUNT(*) >= 5
        AND AVG(course_rating) >= 4
)
, ordered_courses AS (
    SELECT
        c.user_id,
        c.course_id,
        c.course_name,
        c.completion_date,
        LEAD(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS next_course_name
    FROM course_completions AS c
    WHERE c.user_id IN (SELECT user_id FROM top_performers)
)
, course_pairs AS (
    SELECT
        course_name      AS first_course,
        next_course_name AS second_course
    FROM ordered_courses
    WHERE next_course_name IS NOT NULL
)
SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM course_pairs
GROUP BY
    first_course,
    second_course
ORDER BY
    transition_count DESC,
    LOWER(first_course) ASC,
    LOWER(second_course) ASC
;