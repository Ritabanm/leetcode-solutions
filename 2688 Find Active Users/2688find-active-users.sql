# Write your MySQL query statement below
with cte as (
    select user_id,
    created_at,
    lag(created_at) over (partition by user_id order by created_at desc) next_purchase
    from Users
)
select distinct user_id from cte
where datediff(next_purchase, created_at)<=7