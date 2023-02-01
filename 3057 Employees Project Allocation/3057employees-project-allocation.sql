-- Write your PostgreSQL query statement below
WITH TeamAvg AS (
    SELECT 
        e.team,
        AVG(p.workload) AS avg_workload
    FROM Project p
    JOIN Employees e ON p.employee_id = e.employee_id
    GROUP BY e.team
)
SELECT 
    p.employee_id,
    p.project_id,
    e.name AS employee_name,
    p.workload AS project_workload
FROM Project p
JOIN Employees e ON p.employee_id = e.employee_id
JOIN TeamAvg t ON e.team = t.team
WHERE p.workload > t.avg_workload
ORDER BY p.employee_id, p.project_id;