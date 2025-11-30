# Write your MySQL query statement below
WITH CTE AS(SELECT *, CASE WHEN position='Manager' THEN COUNT(emp_id) ELSE 0  END AS count
FROM Employees
GROUP BY dep_id
),
CTE1 AS(SELECT *, RANK() OVER(ORDER BY count DESC) rnk
FROM CTE)
SELECT emp_name AS manager_name, dep_id
FROM CTE1
WHERE rnk=1
ORDER BY dep_id