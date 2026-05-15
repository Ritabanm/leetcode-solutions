# Write your MySQL query statement below
with cte as (
    select *, dense_rank() over(partition by dept order by salary desc) rnk
    from employees
)

select emp_id, dept from cte
where rnk = 2
order by 1;