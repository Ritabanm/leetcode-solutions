# Write your MySQL query statement below
select salesperson_id ,name,ifnull(sum(price),0) total 
from Salesperson 
left join Customer 
using(salesperson_id )
left join Sales 
using(customer_id )
group by 1,2