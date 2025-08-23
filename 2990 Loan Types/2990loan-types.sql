
with t1 as (
    select 
        distinct user_id
    from loans 
    where loan_type = 'Mortgage'
), 

t2 as (
    select 
        distinct user_id
    from loans 
    where loan_type = 'Refinance'
)

select 
    t1.user_id
from t1
join t2 
on t1.user_id = t2.user_id
order by t1.user_id


