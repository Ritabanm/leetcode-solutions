select order_id
from OrdersDetails
group by order_id
having max(quantity) > 
(select max(t1.avg_quantity)
from
(select avg(quantity) avg_quantity
from OrdersDetails
group by order_id) t1)