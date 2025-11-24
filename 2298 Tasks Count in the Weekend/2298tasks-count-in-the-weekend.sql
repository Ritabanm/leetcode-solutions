
with weekend_count as (
    select
        count(*) as weekend_cnt
    from tasks 
    where weekday(submit_date) in (5, 6)
), 

working_count as (
    select
        count(*) as working_cnt 
    from tasks 
    where weekday(submit_date) not in (5, 6)
)

select 
    weekend_cnt, 
    working_cnt
from weekend_count
join working_count



