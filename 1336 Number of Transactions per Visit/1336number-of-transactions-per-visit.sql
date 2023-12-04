with recursive a as(
    select a.user_id ,visit_date ,
    sum(case when transaction_date is null then 0 else 1 end )transactions_count 
    from Visits a
    left join Transactions b
on a.user_id=b.user_id 
and a.visit_date =b.transaction_date
group by 1,2 ),
 b as(
select transactions_count,count(*) visits_count  from a
group by 1)
, c as(
    select 0 as transactions_count ,max(transactions_count )temp   from b
    union all
select transactions_count+1,temp from c
where transactions_count< temp
)
select transactions_count ,ifnull(visits_count ,0) visits_count 
from c
left join b
using(transactions_count) 