select e.employee_id
from employees e left join logs l using(employee_id)
group by e.employee_id
having max(needed_hours)*60>ifnull(sum(ceil(timestampdiff(second, in_time, out_time)/60)),0)