# Write your MySQL query statement below
WITH flag AS (
		SELECT *
			,CASE 
				WHEN score = (max(score) OVER (PARTITION BY exam_id))
					THEN 1
				WHEN score = (min(score) OVER (PARTITION BY exam_id))
					THEN 1
				ELSE 0
				END AS flag
		FROM Exam
		)

SELECT f.student_id
	,s.student_name
FROM flag f
LEFT JOIN Student s ON f.student_id = s.student_id
GROUP BY f.student_id
HAVING sum(flag) = 0
ORDER BY f.student_id
