# Write your MySQL query statement below

with cte as
(
    select distinct spend_date, 'desktop' as platform from spending
    union
    select distinct spend_date, 'mobile' as platform from spending
    union
    select distinct spend_date, 'both' as platform from spending
),

cte2 as
(
    select *, case when count(distinct platform) = 1 then platform 
    when count( distinct platform) = 2 then 'both' end as plat,
    sum(amount) amt
    from spending
    group by spend_date, user_id
)

select c.spend_date, c.platform, sum(coalesce(amt,0)) total_amount, count(distinct user_id) total_users
from cte c left join cte2 c2
on c.spend_date = c2.spend_date
and c.platform = c2.plat
group by spend_date, platform