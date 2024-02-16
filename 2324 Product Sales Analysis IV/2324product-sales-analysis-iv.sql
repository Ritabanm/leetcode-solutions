# Write your MySQL query statement below
select user_id, product_id
from (
    select user_id, product_id, 
    rank()over(partition by user_id order by sum(price*quantity) desc) as rnk
    from sales join product using (product_id)
    group by 1,2
) a
where rnk=1
