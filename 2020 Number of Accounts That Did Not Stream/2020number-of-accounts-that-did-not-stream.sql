with t as (
    select
        account_id
    from subscriptions
    where 2021 between year(start_date) and year(end_date)
), 

t1 as (
    select 
        account_id 
    from streams
    where year(stream_date) = 2021
)

select 
    count(account_id) as accounts_count 
from t
where account_id not in (select account_id from t1)





