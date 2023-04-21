-- Step 1: Get student-wise course flags based on course type and grades
WITH course_flags AS (
    SELECT
        s.student_id,
        
        -- Flag for mandatory courses:
        -- 1 → if grade is A, 2 → if not A or NULL, 0 → not a mandatory course
        CASE 
            WHEN mandatory = 'yes' AND grade = 'A' THEN 1 
            WHEN mandatory = 'yes' AND (grade <>'A' OR grade IS NULL) THEN 2 
            ELSE 0 
        END AS man_fg,

        -- Flag for optional courses:
        -- 1 → if grade is A or B, 2 → if not A/B, 0 → not an optional course
        CASE 
            WHEN mandatory = 'no' AND grade IN ('A', 'B') THEN 1
            WHEN mandatory = 'no' AND grade NOT IN ('A', 'B') THEN 2 
            ELSE 0 
        END AS opt_fg

    FROM students s
    JOIN courses c USING (major)  -- Joining on same major
    LEFT JOIN enrollments e USING (student_id, course_id)  -- Matching enrollments with students and courses
),

-- Step 2: Filter students who have GPA >= 2.5
gpa_qualified AS (
    SELECT student_id
    FROM enrollments
    GROUP BY student_id
    HAVING AVG(GPA) >= 2.5
)

-- Step 3: Final filtering based on flags and GPA qualification
SELECT student_id
FROM course_flags 
JOIN gpa_qualified 
    USING(student_id)  -- Only keep GPA-qualified students

GROUP BY 1
HAVING 
    MAX(man_fg) = 1         -- At least one mandatory course with A grade
    AND MAX(opt_fg) = 1     -- At least one optional course with A or B
    AND SUM(opt_fg) >= 2    -- Must have taken at least two optional courses

ORDER BY 1
