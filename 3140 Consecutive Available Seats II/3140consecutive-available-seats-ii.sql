-- Write your PostgreSQL query statement below
with base as (
select 
seat_id, 
free, 
seat_id - row_number()over(partition by free order by seat_id) as delta
from Cinema
where free=1),

final as (select delta, 
count(seat_id) as consecutive_seats_len, 
max(seat_id) as last_seat_id, 
min(seat_id) as first_seat_id, 
dense_rank()over(order by count(seat_id) desc) as dr
from base 
group by 1)


select first_seat_id, 
last_seat_id, 
consecutive_seats_len

from final 
where dr=1
order by 1