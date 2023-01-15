# Write your MySQL query statement below
Select e1.Name as employee
from employee e1 join employee e2
on e1.managerId = e2.id
and e1.Salary>e2.Salary