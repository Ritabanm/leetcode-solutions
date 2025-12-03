select
    p.product_id, 
    (p.price * (100-coalesce(d.discount, 0))/(100::numeric)) as "final_price", 
    p.category
from Products as p
left join Discounts as d
    using(category)
order by 1