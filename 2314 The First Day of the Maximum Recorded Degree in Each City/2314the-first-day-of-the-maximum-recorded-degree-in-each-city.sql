select city_id,day,degree
from
(
    select *, row_number() over(partition by city_id order by degree desc, day) as rnk
    from weather
)t 
where rnk = 1
order by city_id