# Write your MySQL query statement below
with cte as (
    select log_id, row_number() over(order by log_id) rn
    from Logs
 )

 select min(log_id) start_id, max(log_id) end_id
 from cte
 group by log_id - rn