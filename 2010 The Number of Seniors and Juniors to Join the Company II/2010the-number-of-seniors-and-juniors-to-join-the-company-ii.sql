
with total_sal as (
select *, sum(salary) over(partition by experience order by salary) as run_sum from candidates
) 
,senior_cte as (
select * from total_sal where experience ='Senior' and run_sum<70000
) 
select employee_id from total_sal where experience='Junior' and run_sum<70000-(select coalesce(sum(salary),0) from senior_cte)
union 
select employee_id from senior_cte