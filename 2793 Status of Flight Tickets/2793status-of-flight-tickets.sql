with booking_order as (
    select
        passenger_id,
        flight_id,
        rank() over(partition by flight_id order by booking_time) as order_rnk,
        capacity
    from Passengers p
    join Flights f using(flight_id)
)

select
    passenger_id,
    case when order_rnk <= capacity then 'Confirmed' else 'Waitlist' end as Status
from booking_order
order by 1;