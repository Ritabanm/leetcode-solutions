
select 
    distinct c1.user_id
from Confirmations as c1 
join Confirmations as c2
on c1.user_id = c2.user_id
and c1.time_stamp > c2.time_stamp
and unix_timestamp(c1.time_stamp) - unix_timestamp(c2.time_stamp) <= 86400
