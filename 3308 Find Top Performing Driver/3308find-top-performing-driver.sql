# Write your MySQL query statement below
with a as (
    select d.driver_id, d.accidents, v.vehicle_id, v.fuel_type, 
    t.trip_id, t.distance, t.rating
    from
    Drivers d
    JOIN Vehicles v
    on d.driver_id = v.driver_id
    JOIN Trips t
    on v.vehicle_id = t.vehicle_id
),


b as (
    select driver_id, 
    fuel_type,
    round(avg(rating),2) as rating,
    sum(distance) as distance,
    accidents
    from a
    group by fuel_type, driver_id
    )

select fuel_type, driver_id, rating, distance
from(
    select *,
    rank() over(
        partition by fuel_type 
        order by rating desc, distance desc, accidents asc) as rk
    from b
) as c
where rk = 1
order by fuel_type asc