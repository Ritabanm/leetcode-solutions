with r as (
    select fail_date as date, 'failed' as period_state,
    rank() over(order by fail_date asc) as rk
    from failed
    where fail_date between '2019-01-01' and '2019-12-31'
    union
    select success_date as date, 'succeeded' as period_state,
    rank() over(order by success_date asc) as rk
    from succeeded
    where success_date between '2019-01-01' and '2019-12-31')

select period_state, min(date) as start_date, max(date) as end_date
from r
group by period_state, (date_sub(date, interval rk day)) 
order by start_date