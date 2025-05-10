
with t as (
    select 
        departure_airport as airport_id, 
        flights_count
    from flights
    union all 
    select 
        arrival_airport, 
        flights_count
    from flights
), 

t1 as (
    select 
        airport_id, 
        sum(flights_count) as c
    from t 
    group by airport_id
), 

t2 as (
    select 
        max(c) as mx
    from t1
)

select 
    airport_id
from t1
where c = (select mx from t2)





