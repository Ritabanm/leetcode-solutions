select order_id,customer_id,order_type from
(select order_id,customer_id,order_type,
dense_rank() over(partition by customer_id order by order_type) as rnk
from orders 
group by order_id,customer_id,order_type) a
where rnk=1