# Write your MySQL query statement below
SELECT student_id,
    department_id,
    COALESCE(ROUND(
            (RANK () OVER (PARTITION BY department_id ORDER BY mark DESC) - 1) * 100 / 
            (SELECT COUNT(*) - 1 FROM Students s1 WHERE Students.department_id = s1.department_id)
            ,2),0) AS percentage
FROM Students