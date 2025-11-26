
with t1 as (
    select 
        max(salary) as n1
    from salaries 
    where department = 'Marketing'
), 

t2 as (
    select 
        max(salary) as n2
    from salaries 
    where department = 'Engineering'
)

select 
    abs(n1 - n2) as salary_difference 
from t1
join t2


