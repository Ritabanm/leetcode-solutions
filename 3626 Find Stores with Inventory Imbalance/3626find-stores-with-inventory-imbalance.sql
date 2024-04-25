# Write your MySQL query statement below
with cte as(
    select store_id, max(price) as maxprice, min(price) as minprice
from inventory group by store_id having count(*)>2
),

cte2 as(
select c.store_id, i.product_name as exp, i.quantity as maxpcnt
from cte c join
inventory i
on c.store_id=i.store_id and c.maxprice=i.price
group by i.store_id, i.price
),

cte3 as(
select c.store_id, i.product_name as cheap, i.quantity as minpcnt
from cte c join
inventory i
on c.store_id=i.store_id and c.minprice=i.price
group by i.store_id, i.price
),

cte4 as(
    select c2.store_id
    from cte2 c2 join cte3 c3 on c2.store_id=c3.store_id
    where c2.maxpcnt<c3.minpcnt
)

select distinct i.store_id, s.store_name, s.location, c2.exp as most_exp_product,
c3.cheap as cheapest_product, round((c3.minpcnt/c2.maxpcnt),2) as imbalance_ratio
from inventory i join cte2 c2
on i.store_id=c2.store_id
join cte3 c3 on c2.store_id=c3.store_id
join stores s on c3.store_id=s.store_id
join cte4 c4 on s.store_id=c4.store_id
order by 6 desc, 2