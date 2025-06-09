# Write your MySQL query statement below
select employee_id, count(team_id) over(partition by team_id) team_size
from employee;