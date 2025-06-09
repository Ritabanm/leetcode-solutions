# Write your MySQL query statement below
with cte as (select employee_id 
from Employees 
where manager_id=1

union  

select employee_id
from Employees 
where manager_id in (select employee_id 
from Employees 
where manager_id=1)

union 
select employee_id
from Employees 
where manager_id in (select employee_id
from Employees 
where manager_id in (select employee_id 
from Employees 
where manager_id=1)) )

select employee_id 
from cte 
where employee_id <> 1