select country_name, 
case when avg(weather_state)<=15 then 'Cold'
when avg(weather_state)>=25 then 'Hot'
else 'Warm' end as weather_type
from countries
join weather on countries.country_id = weather.country_id
and year(day) = '2019' and month(day) = '11'
group by country_name