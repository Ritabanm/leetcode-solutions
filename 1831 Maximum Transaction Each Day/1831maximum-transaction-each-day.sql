
with t as (
    select 
        day, 
        max(amount) as mx 
    from transactions 
    group by day
)

select 
    transaction_id 
from transactions as t1
join t
on t1.day = t.day 
and t1.amount = t.mx 
order by transaction_id 

