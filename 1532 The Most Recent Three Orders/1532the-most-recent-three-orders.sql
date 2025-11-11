with r as (
    select *, rank() over(partition by customer_id order by order_date desc) as rk from orders
)

select c.name as customer_name, r.customer_id, r.order_id, r.order_date
from r
join customers c using(customer_id)
where rk<=3
order by name, customer_id, order_date desc
