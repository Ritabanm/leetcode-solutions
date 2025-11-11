
with losses as (
    select 
        paid_by as user_id, 
        sum(amount) as loss
    from transactions
    group by user_id
), 

gains as (
    select 
        paid_to as user_id, 
        sum(amount) as gain
    from transactions
    group by user_id
), 

credit as (
    select 
        u.user_id, 
        user_name, 
        credit - ifnull(loss,0) + ifnull(gain,0) as credit
    from users as u 
    left join losses as l
    on u.user_id = l.user_id
    left join gains as g
    on u.user_id = g.user_id
)

select 
    *, 
    if(credit < 0, 'Yes', 'No') as credit_limit_breached 
from credit     




