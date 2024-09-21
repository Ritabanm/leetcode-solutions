
with t as (
    select
        member_id, 
        100 * sum(if(charged_amount, 1, 0)) / count(*) as r
    from visits as v 
    left join purchases as p 
    on v.visit_id = p.visit_id
    group by member_id
), 

t1 as (
    select 
        member_id, 
        case 
            when r >= 80 then 'Diamond'
            when r >= 50 then 'Gold'
            else 'Silver'
        end as category 
    from t 
)

select 
    m.member_id, 
    name, 
    ifnull(category, 'Bronze') as category
from members as m 
left join t1
on m.member_id = t1.member_id



