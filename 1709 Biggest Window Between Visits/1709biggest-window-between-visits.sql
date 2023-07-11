select
    user_id,
    max(window1) biggest_window
from
(
select
    user_id,
    abs(datediff( visit_date, ifnull( lead(visit_date) over(partition by user_id order by visit_date), '2021-1-1'))) window1
from UserVisits 
) t    
group by user_id
order by 1